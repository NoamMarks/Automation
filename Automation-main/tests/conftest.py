import os
import sys
import datetime
import pytest
from playwright.sync_api import sync_playwright

# Force UTF-8 on stdout/stderr so emoji + Hebrew print correctly on Windows
# (default cp1255 console codec mangles them and crashes the session teardown).
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Add the project root to sys.path so that 'pages' and 'utils' packages are importable
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

# Import the performance summary fixture so pytest auto-discovers it
from utils.performance import print_performance_summary  # noqa: F401


# ==========================================
# 1. HTML Report Configuration
# ==========================================
def pytest_configure(config):
    """
    Generate a dynamic HTML report path based on date + time, but ONLY when
    the user (or runner) hasn't given an explicit path. This lets tools like
    run_multiple.py supply their own per-run paths (e.g. reports/master/
    run_3_report.html) without being clobbered, while preserving the
    date-foldered default for plain `pytest` invocations.
    """
    if hasattr(config.option, "htmlpath"):
        current_path = config.option.htmlpath
        # The pytest.ini default (`reports/report.html`) and an unset path
        # both indicate the user did not pick a specific destination.
        # Anything else means an explicit override — leave it alone.
        if not current_path or current_path == "reports/report.html":
            now = datetime.datetime.now()
            date_folder = now.strftime("%Y-%m-%d")
            time_file = now.strftime("%H-%M-%S")
            reports_dir = os.path.join(os.getcwd(), "reports", date_folder)
            os.makedirs(reports_dir, exist_ok=True)
            report_path = os.path.join(reports_dir, f"report_{time_file}.html")
            config.option.htmlpath = report_path
            config.option.self_contained_html = True


# ==========================================
# 2. Make per-test outcome visible to fixtures
# ==========================================
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Stash the report on the item so fixtures can read item.rep_call / rep_setup."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)


# ==========================================
# 3a. Session-scoped admin login → saved storage_state
# ==========================================
@pytest.fixture(scope="session")
def _auth_state_path(tmp_path_factory):
    """Log in as admin ONCE per pytest session and persist the resulting
    cookies + localStorage to a JSON file. Each class-scoped `page` fixture
    then loads that file as its initial storage_state, so every browser
    context starts already authenticated. Cuts per-suite admin logins
    from ~13 (one per test class) to 1 — important for B2C rate limits
    and just plain faster locally.

    Failure-safe: if the session-level login fails for any reason, returns
    an empty path. The class fixture detects an empty/missing path and
    falls back to per-class login (the original behavior).
    """
    headless = os.getenv("HEADLESS", "0") == "1"
    state_path = tmp_path_factory.mktemp("auth") / "auth_state.json"
    app_url = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=headless, slow_mo=100 if headless else 300
            )
            context = browser.new_context()
            page = context.new_page()
            page.goto(app_url)
            try:
                page.get_by_role("button", name="הבנתי").click(timeout=3000)
            except Exception:
                pass

            # Avoid circular import: imported here, not at module top
            from pages.login_page import LoginPage
            login = LoginPage(page)
            login.fill_credentials()
            login.click_login()
            # Wait for the post-login welcome text to confirm auth landed.
            # We do NOT call wait_for_dashboard() here because that does
            # menu-navigation we don't need for state capture.
            page.get_by_text("שלום מנהלן ראשי").first.wait_for(
                state="visible", timeout=20000
            )

            context.storage_state(path=str(state_path))
            print(f"\n[auth] session login OK; storage_state saved → {state_path}")

            context.close()
            browser.close()
        return str(state_path)
    except Exception as e:
        print(f"\n[auth] WARNING: session-level login failed "
              f"({type(e).__name__}: {e}). Tests will fall back to per-class login.")
        return ""


# ==========================================
# 3b. Playwright Browser Fixture (class-scoped)
# ==========================================
@pytest.fixture(scope="class")
def page(request, _auth_state_path):
    headless = os.getenv("HEADLESS", "0") == "1"
    record_video = os.getenv("RECORD_VIDEO", "0") == "1"

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless, slow_mo=100 if headless else 500)

        ctx_kwargs = {}
        # Preload the session-scoped admin auth so the test class starts
        # already logged in. If the session fixture failed, _auth_state_path
        # is empty and we fall through to per-class login.
        if _auth_state_path and os.path.exists(_auth_state_path):
            ctx_kwargs["storage_state"] = _auth_state_path

        video_dir = None
        if record_video:
            video_dir = os.path.join(os.getcwd(), "artifacts", "videos")
            os.makedirs(video_dir, exist_ok=True)
            ctx_kwargs["record_video_dir"] = video_dir
            ctx_kwargs["record_video_size"] = {"width": 1280, "height": 720}

        context = browser.new_context(**ctx_kwargs)
        page = context.new_page()

        # ------------------------------------------------------------------
        # Zero-touch debugging hooks. Listeners are attached BEFORE the
        # initial goto so we capture errors from first paint. The buckets
        # are cleared per-test by the _capture_on_failure autouse fixture
        # so each failure dump is scoped to the failing test.
        #
        # _error_log is a dict of four lists so the failure log can render
        # clearly separated sections:
        #   console_errors   — console.error / console.assert
        #   console_warnings — console.warning / console.trace
        #                      (React DOM-nesting warnings usually arrive as
        #                       'error' type with a 'Warning:' prefix, so the
        #                       errors bucket also catches those)
        #   page_exceptions  — uncaught JS exceptions on the page
        #   network_failures — HTTP responses with status >= 400
        # ------------------------------------------------------------------
        page._error_log = {
            "console_errors": [],
            "console_warnings": [],
            "page_exceptions": [],
            "network_failures": [],
        }

        def _ts():
            return datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]

        def _location_str(msg):
            try:
                loc = msg.location or {}
                url = loc.get("url", "") or ""
                line = loc.get("lineNumber", "")
                col = loc.get("columnNumber", "")
                if url or line != "":
                    return f"  ({url}:{line}:{col})"
            except Exception:
                pass
            return ""

        def _on_console(msg):
            try:
                type_ = msg.type
                text = msg.text
                where = _location_str(msg)
                entry = f"[{_ts()}] [{type_}] {text}{where}"
                if type_ in ("error", "assert"):
                    page._error_log["console_errors"].append(entry)
                elif type_ in ("warning", "trace"):
                    page._error_log["console_warnings"].append(entry)
            except Exception:
                pass

        def _on_pageerror(exc):
            try:
                name = (getattr(exc, "name", "") or "").strip()
                message = (getattr(exc, "message", "") or "").strip()
                stack = (getattr(exc, "stack", "") or "").strip()
                if not message:
                    message = str(exc).strip()
                header = f"{name}: {message}" if name and message else (name or message or "<unknown>")
                if stack and stack not in (header, message):
                    indented = "\n".join("    " + line for line in stack.splitlines())
                    entry = f"[{_ts()}] {header}\n{indented}"
                else:
                    entry = f"[{_ts()}] {header}"
                page._error_log["page_exceptions"].append(entry)
            except Exception:
                page._error_log["page_exceptions"].append(f"[{_ts()}] {exc!r}")

        def _on_response(response):
            try:
                status = response.status
                if status >= 400:
                    page._error_log["network_failures"].append(
                        f"[{_ts()}] [HTTP {status}] {response.request.method} {response.url}"
                    )
            except Exception:
                pass

        def _attach_listeners(target_page):
            target_page.on("console", _on_console)
            target_page.on("pageerror", _on_pageerror)
            target_page.on("response", _on_response)

        # Attach to the main page IMMEDIATELY (before any navigation).
        _attach_listeners(page)
        # Auto-attach to any popup spawned from this context (new tabs from
        # target=_blank links etc.) so their errors land in the same buckets.
        context.on("page", _attach_listeners)

        page.goto(os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/"))

        try:
            page.get_by_role("button", name="הבנתי").click(timeout=3000)
        except:
            pass

        yield page

        # Capture video path before context closes (Playwright finalizes the file on close)
        original_video_path = None
        if record_video:
            try:
                original_video_path = page.video.path() if page.video else None
            except Exception:
                pass

        context.close()
        browser.close()

        # Rename auto-generated UUID video file to <ClassName>_<HHMMSS>.webm for the report
        if record_video and original_video_path and os.path.exists(original_video_path):
            class_name = request.cls.__name__ if request.cls else "module"
            ts = datetime.datetime.now().strftime("%H%M%S")
            new_path = os.path.join(video_dir, f"{class_name}_{ts}.webm")
            try:
                os.rename(original_video_path, new_path)
            except Exception:
                pass


# ==========================================
# 4. Zero-touch failure capture (per-test)
# ==========================================
@pytest.fixture(autouse=True)
def _capture_on_failure(request):
    """
    Per-test wrapper that:
      - Clears the page's accumulated error log before the test (so the dump
        on failure contains only what happened during THIS test).
      - On failure (setup or call), saves:
          artifacts/errors/<test>_<timestamp>.png         (full-page screenshot)
          artifacts/errors/<test>_<timestamp>_logs.txt    (console + network errors)

    Skips silently for tests that don't use the Playwright `page` fixture.
    """
    def _reset_log(p):
        log = getattr(p, "_error_log", None)
        if isinstance(log, dict):
            for v in log.values():
                if isinstance(v, list):
                    v.clear()
        elif isinstance(log, list):
            log.clear()

    page_obj = None
    if "page" in request.fixturenames:
        try:
            page_obj = request.getfixturevalue("page")
            _reset_log(page_obj)
        except Exception:
            page_obj = None

    yield

    rep_call = getattr(request.node, "rep_call", None)
    rep_setup = getattr(request.node, "rep_setup", None)
    failed = (rep_call is not None and rep_call.failed) or (
        rep_setup is not None and rep_setup.failed
    )
    if not failed or page_obj is None:
        return

    # IMPORTANT: zero-touch artifacts must live OUTSIDE artifacts/ because
    # pytest.ini sets --output=artifacts (a pytest-playwright option) and the
    # plugin wipes that directory at every session start. If we wrote here,
    # multi-run mode (run_multiple.py) would lose every previous run's
    # screenshots/logs as soon as the next run started.
    errors_dir = os.path.join(os.getcwd(), "zero_touch_logs", "errors")
    os.makedirs(errors_dir, exist_ok=True)

    safe_name = (
        request.node.name.replace("[", "_").replace("]", "").replace("/", "_").replace("::", "_")
    )
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_path = os.path.join(errors_dir, f"{safe_name}_{ts}.png")
    log_path = os.path.join(errors_dir, f"{safe_name}_{ts}_logs.txt")

    try:
        page_obj.screenshot(path=screenshot_path, full_page=True)
        print(f"\n[zero-touch] screenshot: {screenshot_path}")
    except Exception as e:
        print(f"\n[zero-touch] screenshot failed: {type(e).__name__}: {e}")

    try:
        log = getattr(page_obj, "_error_log", {}) or {}
        if not isinstance(log, dict):
            # Backward-compat: if a flat list was used, re-bucket as "console_errors"
            log = {"console_errors": list(log), "console_warnings": [], "page_exceptions": [], "network_failures": []}

        sections = (
            ("Console Errors",                    log.get("console_errors", [])),
            ("Console Warnings",                  log.get("console_warnings", [])),
            ("Page Exceptions",                   log.get("page_exceptions", [])),
            ("Network Failures (HTTP >= 400)",    log.get("network_failures", [])),
        )

        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"Test     : {request.node.nodeid}\n")
            f.write(f"Failed at: {ts}\n")
            try:
                f.write(f"URL      : {page_obj.url}\n")
            except Exception:
                pass
            f.write("=" * 70 + "\n\n")

            total = 0
            for title, entries in sections:
                count = len(entries)
                total += count
                f.write(f"==== {title} ({count}) ====\n")
                if entries:
                    for e in entries:
                        f.write(e + "\n")
                else:
                    f.write("(none)\n")
                f.write("\n")

            if total == 0:
                f.write("(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)\n")

        counts = {title: len(entries) for title, entries in sections}
        print(
            f"[zero-touch] error log : {log_path} "
            f"(errors={counts.get('Console Errors', 0)}, "
            f"warnings={counts.get('Console Warnings', 0)}, "
            f"exceptions={counts.get('Page Exceptions', 0)}, "
            f"network={counts.get('Network Failures (HTTP >= 400)', 0)})"
        )
    except Exception as e:
        print(f"[zero-touch] log write failed: {type(e).__name__}: {e}")
