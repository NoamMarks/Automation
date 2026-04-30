"""
Performance measurement utilities for Playwright tests.

Provides:
- measure_loader_cycle: detects and times the app's loading spinner
- performance_step: context manager that measures action + loader time and reports to HTML/terminal
- print_performance_summary: session-scoped fixture that prints a summary table at the end
"""

import time
import pytest
from contextlib import contextmanager
from pytest_html import extras as html_extras


# --- Global list to collect results for the terminal summary report ---
PERFORMANCE_RESULTS = []


def measure_loader_cycle(page) -> float:
    """
    Wait for the loader spinner to appear and disappear.
    Uses a short detection window (300ms) so tests aren't delayed when there's no loader.
    Returns the duration the loader was visible, in seconds.
    """
    loader = page.locator("#loader svg")
    popup_btn = page.get_by_role("button", name="הבנתי")

    start_time = time.perf_counter()

    try:
        loader.wait_for(state="visible", timeout=300)
    except:
        return 0.0

    try:
        loader.wait_for(state="hidden", timeout=15000)
    except Exception as e:
        print(f"⚠️ Warning: loader did not disappear within 15 seconds: {e}")

    if popup_btn.is_visible():
        popup_btn.click()

    end_time = time.perf_counter()
    return end_time - start_time


@contextmanager
def performance_step(step_name, extras, page=None, limit_ms=5000):
    """
    Context manager that:
    1. Times the code block (the 'action')
    2. Measures the loader spinner duration after the action
    3. Records results for both HTML and terminal reports
    """
    start_action = time.time()
    loader_duration_sec = 0.0
    status = "PASS"

    try:
        # --- 1. Run the action (e.g. clicking 'Save') ---
        yield
        end_action = time.time()

        # --- 2. Measure loader ---
        if page:
            loader_duration_sec = measure_loader_cycle(page)

        # --- 3. Calculate durations ---
        action_duration_ms = (end_action - start_action) * 1000
        loader_duration_ms = loader_duration_sec * 1000
        total_duration_ms = action_duration_ms + loader_duration_ms

        if total_duration_ms > limit_ms:
            status = "SLOW"

        print(f"   ⏱️  {step_name} >> Action: {action_duration_ms:.0f}ms | Loader: {loader_duration_ms:.0f}ms | Total: {total_duration_ms:.0f}ms")

        # --- Save to global list for terminal summary ---
        PERFORMANCE_RESULTS.append({
            "name": step_name,
            "total": total_duration_ms,
            "loader": loader_duration_ms,
            "limit": limit_ms,
            "status": status
        })

        # --- Write to HTML report ---
        if status == "PASS":
            extras.append(html_extras.html(f"""
                <div style='padding: 5px; margin: 2px; border-left: 5px solid green; background-color: #e8f5e9;'>
                    <span style='color: green; font-weight: bold;'>✅ PASS:</span> {step_name} <br>
                    <span style='font-size: 0.9em;'>
                        <b>Loader Time:</b> {loader_duration_ms:.0f}ms <br>
                        Total Time: {total_duration_ms:.2f}ms (Limit: {limit_ms}ms)
                    </span>
                </div>
            """))
        else:
            extras.append(html_extras.html(f"""
                <div style='padding: 5px; margin: 2px; border-left: 5px solid orange; background-color: #fff3e0;'>
                    <span style='color: darkorange; font-weight: bold;'>⚠️ SLOW:</span> {step_name} <br>
                    <span style='font-size: 0.9em;'>
                        <b>Loader Time:</b> {loader_duration_ms:.0f}ms <br>
                        Total Time: {total_duration_ms:.2f}ms (Limit: {limit_ms}ms)
                    </span>
                </div>
            """))

    except Exception as e:
        end_time = time.time()
        total_fail = (end_time - start_action) * 1000

        PERFORMANCE_RESULTS.append({
            "name": step_name,
            "total": total_fail,
            "loader": 0,
            "limit": limit_ms,
            "status": "FAIL"
        })

        extras.append(html_extras.html(f"""
            <div style='padding: 5px; margin: 2px; border-left: 5px solid red; background-color: #ffebee;'>
                <span style='color: red; font-weight: bold;'>❌ FAILED:</span> {step_name} <br>
                <span>Stopped after: {total_fail:.2f}ms</span>
            </div>
        """))
        raise e


@pytest.fixture(scope="session", autouse=True)
def print_performance_summary():
    """
    Session-scoped fixture that prints a summary table to the terminal
    after all tests have completed.
    """
    yield

    print("\n\n" + "=" * 95)
    print(f"📊  PERFORMANCE SUMMARY REPORT (TERMINAL)")
    print("=" * 95)
    print(f"{'Step Name':<35} | {'Total Time':<12} | {'Loader Time':<12} | {'Limit':<8} | {'Status'}")
    print("-" * 95)

    for res in PERFORMANCE_RESULTS:
        step_name = res['name']
        total = res['total']
        loader = res['loader']
        limit = res['limit']
        status = res['status']

        icon = "✅ PASS"
        if status == "SLOW": icon = "⚠️ SLOW"
        elif status == "FAIL": icon = "❌ FAIL"

        print(f"{step_name:<35} | {total:<8.0f}ms   | {loader:<8.0f}ms   | {limit:<6}ms | {icon}")

    print("=" * 95 + "\n")
