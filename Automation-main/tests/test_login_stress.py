"""
Login form-rendering stress / flake-detection.

Targets the suspected flake: after clicking 'התחבר' on the homepage,
the Azure B2C form (#pretty-username field) sometimes does not render.

How it works:
  - Each iteration creates a brand-new browser context (NO storage_state),
    so every attempt is a fresh, fully-unauthenticated visit.
  - Navigate to APP_URL → dismiss the cookie banner → click 'התחבר'.
  - Wait up to 10 s for `#pretty-username` to appear.
  - Record per-iteration result with diagnostics (URL we ended up on,
    console-error count during the click window, screenshot if it failed).
  - Sleep a random 5-8 s between iterations to avoid Azure B2C rate-limit
    (~10-15 logins/IP/min triggers temporary lockout).

Marked `stress` so it's excluded from default pytest runs. Invoke with:

    pytest -m stress -v -s
    LOGIN_STRESS_ITERATIONS=30 pytest -m stress -v -s   # bump count

Iterations default to 10. ~10 s per iteration → ~2-3 min total.
"""

import os
import random
import time
from datetime import datetime

import pytest
from playwright.sync_api import sync_playwright

APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")
ITERATIONS = int(os.getenv("LOGIN_STRESS_ITERATIONS", "10"))

# Where to put screenshots / logs from failed iterations
_DIAG_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "zero_touch_logs", "login_stress",
)


def _open_fresh_context(browser):
    """A brand-new, unauthenticated browser context. No cookies, no
    localStorage, no sessionStorage — guarantees a real login flow."""
    ctx = browser.new_context(viewport={"width": 1280, "height": 720})
    page = ctx.new_page()
    return ctx, page


def _capture_diagnostics(page, iteration, console_errors):
    """Save a screenshot + a small text log for one failing iteration."""
    os.makedirs(_DIAG_DIR, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    base = os.path.join(_DIAG_DIR, f"iter{iteration:02d}_{ts}")
    try:
        page.screenshot(path=f"{base}.png", full_page=True)
    except Exception as e:
        print(f"  (screenshot failed: {type(e).__name__}: {e})")
    with open(f"{base}.txt", "w", encoding="utf-8") as f:
        f.write(f"Iteration  : {iteration}\n")
        f.write(f"Final URL  : {page.url}\n")
        f.write(f"Page title : {page.title()}\n\n")
        f.write(f"Console errors during the click ({len(console_errors)}):\n")
        for line in console_errors:
            f.write(f"  - {line}\n")


@pytest.mark.stress
def test_login_form_renders_on_click():
    """Click 'התחבר' N times in a row from a clean state. The B2C form
    (`#pretty-username`) must appear every time within 10 s.

    A failure is recorded — but not raised — until all iterations have
    finished, so we get a hit-rate even when the flake fires partway."""

    print(f"\n[login-stress] starting — ITERATIONS={ITERATIONS}, "
          f"diag dir={_DIAG_DIR}")

    results = []  # list of (iteration, status, detail)
    diag_dir_made = False

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=os.getenv("HEADLESS", "0") == "1",
            slow_mo=80 if os.getenv("HEADLESS", "0") == "1" else 200,
        )
        try:
            for i in range(1, ITERATIONS + 1):
                t_start = time.time()
                ctx, page = _open_fresh_context(browser)

                # Capture console errors that fire DURING the click+wait window
                console_errors = []
                page.on(
                    "pageerror",
                    lambda e: console_errors.append(f"[pageerror] {e}"),
                )
                page.on(
                    "console",
                    lambda m: console_errors.append(f"[{m.type}] {m.text}")
                    if m.type in ("error", "warning") else None,
                )

                status, detail = "pass", ""
                try:
                    page.goto(APP_URL, wait_until="domcontentloaded")
                    try:
                        page.get_by_role("button", name="הבנתי").click(timeout=3000)
                    except Exception:
                        pass

                    page.wait_for_timeout(800)
                    page.get_by_text("התחבר").first.click(timeout=5000)

                    # The flake target — does the username field render in time?
                    page.locator("#pretty-username").wait_for(
                        state="visible", timeout=10000
                    )
                    status = "pass"
                except Exception as e:
                    status = "fail"
                    detail = f"{type(e).__name__}: {str(e)[:200]}"
                    if not diag_dir_made:
                        os.makedirs(_DIAG_DIR, exist_ok=True)
                        diag_dir_made = True
                    _capture_diagnostics(page, i, console_errors)

                duration = time.time() - t_start
                results.append((i, status, detail, duration))
                icon = "✅" if status == "pass" else "❌"
                print(f"[login-stress] iter {i:02d}/{ITERATIONS}  {icon} "
                      f"{status.upper():4}  ({duration:.1f}s)  {detail}")

                ctx.close()

                # Avoid B2C rate-limit; small random jitter between attempts
                if i < ITERATIONS:
                    time.sleep(random.uniform(5, 8))
        finally:
            browser.close()

    # --- Summary ---
    n_pass = sum(1 for r in results if r[1] == "pass")
    n_fail = sum(1 for r in results if r[1] == "fail")
    rate = 100.0 * n_pass / max(1, len(results))
    print()
    print("=" * 60)
    print(f"[login-stress] SUMMARY — {n_pass}/{ITERATIONS} passed "
          f"({rate:.0f}% pass rate)")
    print("=" * 60)
    if n_fail:
        print(f"[login-stress] failed iterations:")
        for i, status, detail, dur in results:
            if status == "fail":
                print(f"  iter {i}: {detail}  ({dur:.1f}s)")
        print(f"[login-stress] diagnostics saved under {_DIAG_DIR}")

    # Assert 100% pass — any flake means the bug fired and the test
    # should fail loudly. If you want to allow some flake, replace with
    #     assert rate >= 95, "..."
    assert n_fail == 0, (
        f"Login-form-rendering flake fired: {n_fail} of {ITERATIONS} "
        f"attempts failed to render the B2C `#pretty-username` field "
        f"within 10s of clicking 'התחבר'. "
        f"See {_DIAG_DIR} for screenshots + console-error logs per "
        f"failed iteration."
    )
