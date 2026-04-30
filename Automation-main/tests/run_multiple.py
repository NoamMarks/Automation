"""
Multi-run pytest executor with consolidated reporting.

Runs the test suite NUM_RUNS times and produces a single Master Run Report
(markdown) that aggregates results, failures, and zero-touch debugging
artifacts across all runs.

Usage:
    py -3.13 tests/run_multiple.py
    # or via the venv:
    .venv\\Scripts\\python.exe tests/run_multiple.py

What you get:
    reports/master/run_<N>_report.html      — pytest-html per-run report
    reports/master/run_<N>_junit.xml        — junit XML per run
    reports/master/Master_Run_Report_<TS>.md — consolidated master report
"""

import os
import subprocess
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

from utils.generate_master_report import generate_master_report  # noqa: E402


# ============================================================
# CONFIGURATION
# ============================================================

# How many times to run the suite end-to-end.
# Override at runtime: set the NUM_RUNS env var.
NUM_RUNS = int(os.getenv("NUM_RUNS", "5"))

# What to test (path relative to project root, or specific test files).
# Override at runtime: set the TEST_PATH env var.
TEST_PATH = os.getenv("TEST_PATH", "./tests/")

# Extra pytest args appended to every run. Examples:
#   ["-k", "smoke"]                  → only tests whose nodeid matches 'smoke'
#   ["--reruns", "2"]                → retry failed tests up to 2× per run
#   ["-x"]                           → stop on first failure
EXTRA_PYTEST_ARGS = []


# ============================================================
# Implementation
# ============================================================

MASTER_REPORTS_DIR = os.path.join(_PROJECT_ROOT, "reports", "master")


def _run_once(run_idx, total):
    """Execute a single pytest invocation, returning a run-record dict."""
    run_html = os.path.join(MASTER_REPORTS_DIR, f"run_{run_idx}_report.html")
    run_junit = os.path.join(MASTER_REPORTS_DIR, f"run_{run_idx}_junit.xml")

    cmd = [
        sys.executable, "-m", "pytest", TEST_PATH,
        f"--html={run_html}",
        "--self-contained-html",
        f"--junitxml={run_junit}",
        *EXTRA_PYTEST_ARGS,
    ]

    run_start = datetime.now()
    print()
    print("-" * 72)
    print(f"🚀  Run {run_idx}/{total} — {run_start.isoformat(timespec='seconds')}")
    print(f"    {' '.join(cmd)}")
    print("-" * 72)

    # Don't capture output — we want pytest's live progress visible while it runs.
    result = subprocess.run(cmd, cwd=_PROJECT_ROOT, shell=False)
    run_end = datetime.now()

    duration = (run_end - run_start).total_seconds()
    print()
    print(f"    Run {run_idx} finished — exit={result.returncode}, "
          f"wall-clock={duration:.1f}s")

    return {
        "run_idx":    run_idx,
        "start":      run_start,
        "end":        run_end,
        "exit_code":  result.returncode,
        "junit_path": run_junit,
        "html_path":  run_html,
    }


def main():
    suite_start = datetime.now()
    print("=" * 72)
    print(f"MULTI-RUN EXECUTOR — {NUM_RUNS} run(s) of {TEST_PATH}")
    print(f"Started: {suite_start.isoformat(timespec='seconds')}")
    if EXTRA_PYTEST_ARGS:
        print(f"Extra args: {EXTRA_PYTEST_ARGS}")
    print("=" * 72)

    os.makedirs(MASTER_REPORTS_DIR, exist_ok=True)
    runs = []

    try:
        for i in range(1, NUM_RUNS + 1):
            runs.append(_run_once(i, NUM_RUNS))
    except KeyboardInterrupt:
        print()
        print("!" * 72)
        print(f"  INTERRUPTED — generating master report with {len(runs)} "
              f"completed run(s)")
        print("!" * 72)

    # ---- Master report ----
    suite_end = datetime.now()
    timestamp = suite_end.strftime("%Y%m%d_%H%M%S")
    master_path = os.path.join(MASTER_REPORTS_DIR, f"Master_Run_Report_{timestamp}.md")

    print()
    print("=" * 72)
    print("GENERATING MASTER REPORT")
    print("=" * 72)
    written = generate_master_report(runs, master_path)

    total_dur = (suite_end - suite_start).total_seconds()
    nonzero = sum(1 for r in runs if r["exit_code"] != 0)
    print()
    print(f"Suite finished in {total_dur:.1f}s.")
    print(f"Runs with non-zero exit code: {nonzero}/{len(runs)}")
    print(f"Master report:  {written}")
    if os.path.exists(written):
        print(f"   size:        {os.path.getsize(written):,} bytes")


if __name__ == "__main__":
    main()
