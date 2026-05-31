"""
Multi-run pytest executor with consolidated reporting.

Runs the test suite NUM_RUNS times and produces a single Master Run Report
(markdown) that aggregates results, failures, and zero-touch debugging
artifacts across all runs.

Two entry points:

  1. CLI / module:
        py -3.13 tests/run_multiple.py
        # or via the venv:
        .venv\\Scripts\\python.exe tests/run_multiple.py

  2. Library — used by the desktop launcher (run_gui.py / ZiraQARunner.exe)
     to invoke the suite in-process. Subprocess is avoided in the frozen
     .exe because PyInstaller's onefile bundle doesn't ship a callable
     python.exe:
        from tests.run_multiple import run_suite
        run_suite(num_runs=5, headless=False, reports_dir=r"C:\\out")

What you get:
    reports/master/run_<N>_report.html      — pytest-html per-run report
    reports/master/run_<N>_junit.xml        — junit XML per run
    reports/master/Master_Run_Report_<TS>.md — consolidated master report
"""

import os
import sys
from datetime import datetime

# Force UTF-8 on stdout/stderr so emoji + Hebrew print correctly on Windows
# (default cp1255 console codec mangles them and crashes the script).
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Make the project's `utils` package importable when this script is run
# directly (i.e. without installing the project as a package).
_HERE = os.path.dirname(os.path.abspath(__file__))
_PROJECT_ROOT = os.path.dirname(_HERE)
sys.path.insert(0, _PROJECT_ROOT)


def _maybe_load_dotenv():
    """Best-effort .env load. The launcher already injects creds via os.environ
    when running from the frozen .exe, so a missing .env file is fine there."""
    try:
        from dotenv import load_dotenv
        env_path = os.path.join(_PROJECT_ROOT, ".env")
        if os.path.exists(env_path):
            load_dotenv(env_path)
    except Exception:
        pass


_maybe_load_dotenv()

from utils.generate_master_report import generate_master_report  # noqa: E402
from utils.generate_simple_summary import generate_simple_summary  # noqa: E402
from utils.generate_html_dashboard import generate_html_dashboard  # noqa: E402
from utils.generate_whatsapp_summary import generate_whatsapp_summary  # noqa: E402
from utils.dashboard_to_pdf import dashboard_html_to_pdf  # noqa: E402
from utils.send_email import send_run_email  # noqa: E402


# ============================================================
# CONFIGURATION
# ============================================================

import shlex  # noqa: E402


def _default_test_path():
    """Where the tests live. In a PyInstaller onefile, the tests/ dir is
    unpacked into sys._MEIPASS at runtime; outside the .exe, use the
    sibling tests/ folder."""
    if getattr(sys, "frozen", False):
        return os.path.join(getattr(sys, "_MEIPASS", _PROJECT_ROOT), "tests")
    return os.path.join(_PROJECT_ROOT, "tests")


# ============================================================
# Implementation
# ============================================================


def _run_once(run_idx, total, master_reports_dir, test_path, extra_args):
    """Execute a single pytest invocation in-process and return a run-record."""
    run_html = os.path.join(master_reports_dir, f"run_{run_idx}_report.html")
    run_junit = os.path.join(master_reports_dir, f"run_{run_idx}_junit.xml")

    pytest_args = [
        # The GUI launcher redirects sys.stdout/stderr to a queue-backed
        # writer that doesn't expose fileno(). pytest's faulthandler plugin
        # crashes the whole session with INTERNALERROR when it can't read
        # stderr's fileno — disable it. We're a GUI app catching exceptions
        # in Python; we don't need C-level segfault dumps.
        "-p", "no:faulthandler",
        test_path,
        f"--html={run_html}",
        "--self-contained-html",
        f"--junitxml={run_junit}",
        *extra_args,
    ]

    run_start = datetime.now()
    print()
    print("-" * 72)
    print(f"🚀  Run {run_idx}/{total} — {run_start.isoformat(timespec='seconds')}")
    print(f"    pytest {' '.join(pytest_args)}")
    print("-" * 72)

    # In-process invocation. This is critical for the frozen .exe — there is
    # no python.exe to subprocess into. It also works fine for normal CLI use.
    #
    # Note: each pytest.main() is its own session. Session-scoped fixtures
    # (e.g. _auth_state_path) re-run per iteration, which is the same
    # behaviour the old subprocess-per-run path had.
    import pytest
    exit_code = pytest.main(pytest_args)
    run_end = datetime.now()

    duration = (run_end - run_start).total_seconds()
    print()
    print(f"    Run {run_idx} finished — exit={exit_code}, "
          f"wall-clock={duration:.1f}s")

    return {
        "run_idx":    run_idx,
        "start":      run_start,
        "end":        run_end,
        "exit_code":  int(exit_code),
        "junit_path": run_junit,
        "html_path":  run_html,
    }


def run_suite(num_runs=None, headless=None, reports_dir=None,
              test_path=None, extra_pytest_args=None):
    """Programmatic entry point used by the GUI launcher.

    All args optional — falls back to env vars / sensible defaults so the
    CLI path (main()) can share this function.
    """
    # ---- Resolve config from args → env → defaults ----
    if num_runs is None:
        num_runs = int(os.getenv("NUM_RUNS", "5"))
    if headless is not None:
        os.environ["HEADLESS"] = "1" if headless else "0"
    if test_path is None:
        test_path = os.getenv("TEST_PATH") or _default_test_path()
    if extra_pytest_args is None:
        env_extras = os.getenv("PYTEST_EXTRA_ARGS", "").strip()
        extra_pytest_args = shlex.split(env_extras) if env_extras else []

    if reports_dir is None:
        # Default writes alongside the project; the launcher overrides this
        # to a user-chosen folder when running from the .exe.
        reports_dir = os.path.join(_PROJECT_ROOT, "reports", "master")
    master_reports_dir = reports_dir
    os.makedirs(master_reports_dir, exist_ok=True)

    suite_start = datetime.now()
    print("=" * 72)
    print(f"MULTI-RUN EXECUTOR — {num_runs} run(s) of {test_path}")
    print(f"Reports: {master_reports_dir}")
    print(f"Started: {suite_start.isoformat(timespec='seconds')}")
    if extra_pytest_args:
        print(f"Extra args: {extra_pytest_args}")
    print("=" * 72)

    runs = []
    try:
        for i in range(1, num_runs + 1):
            runs.append(_run_once(i, num_runs, master_reports_dir,
                                  test_path, extra_pytest_args))
    except KeyboardInterrupt:
        print()
        print("!" * 72)
        print(f"  INTERRUPTED — generating master report with {len(runs)} "
              f"completed run(s)")
        print("!" * 72)

    # ---- Reports ----
    suite_end = datetime.now()
    timestamp = suite_end.strftime("%Y%m%d_%H%M%S")
    master_path = os.path.join(master_reports_dir, f"Master_Run_Report_{timestamp}.md")
    summary_path = os.path.join(master_reports_dir, f"Test_Summary_{timestamp}.md")
    dashboard_path = os.path.join(master_reports_dir, f"Test_Dashboard_{timestamp}.html")
    dashboard_pdf_path = os.path.join(master_reports_dir, f"Test_Dashboard_{timestamp}.pdf")
    whatsapp_path = os.path.join(master_reports_dir, f"WhatsApp_Summary_{timestamp}.txt")

    print()
    print("=" * 72)
    print("GENERATING REPORTS")
    print("=" * 72)
    written_master = generate_master_report(runs, master_path)
    written_summary = generate_simple_summary(runs, summary_path)
    written_dashboard = generate_html_dashboard(runs, dashboard_path)

    written_pdf = None
    try:
        written_pdf = dashboard_html_to_pdf(written_dashboard, dashboard_pdf_path)
        print(f"[pdf] dashboard PDF written: {written_pdf} "
              f"({os.path.getsize(written_pdf):,} bytes)")
    except Exception as e:
        print(f"[pdf] FAILED to generate dashboard PDF: "
              f"{type(e).__name__}: {e}")

    written_whatsapp = generate_whatsapp_summary(
        runs, whatsapp_path, pdf_path=written_pdf
    )

    total_dur = (suite_end - suite_start).total_seconds()
    nonzero = sum(1 for r in runs if r["exit_code"] != 0)
    print()
    print(f"Suite finished in {total_dur:.1f}s.")
    print(f"Runs with non-zero exit code: {nonzero}/{len(runs)}")
    print(f"Plain summary:  {written_summary}")
    print(f"HTML dashboard: {written_dashboard}")
    if written_pdf:
        print(f"Dashboard PDF:  {written_pdf}")
    print(f"Master report:  {written_master}")
    print(f"WhatsApp text:  {written_whatsapp}")

    try:
        with open(written_whatsapp, encoding="utf-8") as f:
            wa_text = f.read()
        print()
        print("-" * 72)
        print("WHATSAPP MESSAGE (copy below):")
        print("-" * 72)
        print(wa_text)
        print("-" * 72)
    except Exception as e:
        print(f"[whatsapp] could not echo content: {type(e).__name__}: {e}")

    # ---- Post-run email ----
    print()
    print("=" * 72)
    print("POST-RUN EMAIL")
    print("=" * 72)
    send_run_email(
        runs,
        summary_path=written_summary,
        dashboard_path=written_dashboard,
        master_path=written_master,
    )

    return {
        "runs": runs,
        "reports_dir": master_reports_dir,
        "master": written_master,
        "summary": written_summary,
        "dashboard": written_dashboard,
        "pdf": written_pdf,
        "whatsapp": written_whatsapp,
    }


def main():
    run_suite()


if __name__ == "__main__":
    main()
