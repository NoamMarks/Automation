"""
Master Run Report generator — aggregates multiple pytest runs into one
consolidated markdown report.

Used by run_multiple.py. Pulls together:
  - per-run JUnit XML (test counts, failures, durations)
  - per-run pytest-html report (linked, not embedded)
  - zero-touch artifacts (screenshots + error logs) matched to each run
    by the artifact-filename timestamp falling inside the run window
"""

import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime, timedelta


# ============================================================
# JUnit parsing
# ============================================================

def _parse_junit(junit_path):
    """Parse a pytest junit XML. Returns dict or None if unparseable/missing."""
    if not junit_path or not os.path.exists(junit_path):
        return None
    try:
        tree = ET.parse(junit_path)
        root = tree.getroot()
        suite = root.find("testsuite") if root.tag != "testsuite" else root
        return {
            "tests":     int(suite.attrib.get("tests", 0)),
            "failures":  int(suite.attrib.get("failures", 0)),
            "errors":    int(suite.attrib.get("errors", 0)),
            "skipped":   int(suite.attrib.get("skipped", 0)),
            "time":      float(suite.attrib.get("time", 0)),
            "timestamp": suite.attrib.get("timestamp", ""),
            "testcases": [_testcase_dict(tc) for tc in suite.findall("testcase")],
        }
    except Exception:
        return None


def _testcase_dict(tc):
    failure = tc.find("failure")
    error = tc.find("error")
    skipped = tc.find("skipped")
    msg = ""
    if failure is not None:
        msg = failure.attrib.get("message", "")
    elif error is not None:
        msg = error.attrib.get("message", "")
    elif skipped is not None:
        msg = skipped.attrib.get("message", "")
    return {
        "classname":       tc.attrib.get("classname", ""),
        "name":            tc.attrib.get("name", ""),
        "time":            float(tc.attrib.get("time", 0)),
        "failed":          (failure is not None) or (error is not None),
        "skipped":         skipped is not None,
        "failure_message": msg,
    }


# ============================================================
# Artifact matching
# ============================================================

_TS_RE = re.compile(r"(\d{8})_(\d{6})")


def _parse_artifact_ts(filename):
    m = _TS_RE.search(filename)
    if not m:
        return None
    try:
        return datetime.strptime(f"{m.group(1)}_{m.group(2)}", "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def _find_artifacts_for_run(errors_dir, run_start, run_end, buffer_sec=2):
    """Return {test_name: {screenshots: [...], logs: [...]}} for artifacts
    whose filename timestamp falls in the run's [start, end + buffer] window.

    The buffer is intentionally small (default 2s) because run_end is captured
    AFTER pytest fully exits (including teardown), so artifacts should already
    be on disk. A larger buffer causes false-matches when multiple short runs
    are scheduled back-to-back, which we observed empirically — Run N+1's
    artifact would otherwise also fall inside Run N's expanded window.
    """
    if not os.path.isdir(errors_dir):
        return {}
    grouped = defaultdict(lambda: {"screenshots": [], "logs": []})
    upper = run_end + timedelta(seconds=buffer_sec)
    lower = run_start
    for f in sorted(os.listdir(errors_dir)):
        ts = _parse_artifact_ts(f)
        if ts is None or not (lower <= ts <= upper):
            continue
        full = os.path.join(errors_dir, f).replace(os.sep, "/")
        if f.endswith(".png"):
            test_name = f.rsplit("_", 2)[0]
            grouped[test_name]["screenshots"].append(full)
        elif f.endswith("_logs.txt"):
            test_name = f.rsplit("_", 3)[0]
            grouped[test_name]["logs"].append(full)
    return dict(grouped)


def _rel(target, from_path):
    """Path relative to the report file's directory, with forward slashes."""
    try:
        return os.path.relpath(target, os.path.dirname(from_path)).replace(os.sep, "/")
    except ValueError:
        return target.replace(os.sep, "/")


# ============================================================
# Failure-pattern bucketing  (Surfacing root cause when many tests fail)
# ============================================================

_KNOWN_ERROR_TYPES = (
    "TimeoutError", "AssertionError", "NameError", "ValueError", "TypeError",
    "AttributeError", "KeyError", "IndexError", "FileNotFoundError",
    "ConnectionError", "PermissionError", "RuntimeError",
)


def _error_key(msg):
    """Reduce a failure_message string to a short bucket key like 'TimeoutError'.
    When multiple tests fail with the same exception type, they share a key."""
    if not msg:
        return "<no message>"
    line = msg.strip().splitlines()[0]
    m = re.search(r"([A-Z]\w*(?:Error|Exception))", line)
    if m:
        return m.group(1)
    for k in _KNOWN_ERROR_TYPES:
        if k in line:
            return k
    return line[:60]


def _build_failure_analysis(parsed):
    """Bucket failures across all runs by exception type AND by test class.

    Returns:
        error_buckets   {error_type: [{test, run, msg}, ...]}
        class_failures  {class_name: failure_count}
        class_totals    {class_name: total_test_count}
    """
    error_buckets = defaultdict(list)
    class_failures = defaultdict(int)
    class_totals = defaultdict(int)

    for run, data in parsed:
        if data is None:
            continue
        for tc in data["testcases"]:
            cls_name = tc["classname"].split(".")[-1] or "<unknown>"
            class_totals[cls_name] += 1
            if tc["failed"]:
                class_failures[cls_name] += 1
                key = _error_key(tc["failure_message"])
                first_line = (tc["failure_message"] or "").strip().splitlines()
                sample = first_line[0][:160] if first_line else ""
                error_buckets[key].append({
                    "test": f"{cls_name}::{tc['name']}",
                    "run":  run["run_idx"],
                    "msg":  sample,
                })
    return error_buckets, class_failures, class_totals


# ============================================================
# Master-report builder
# ============================================================

def generate_master_report(runs, output_path, errors_dir="zero_touch_logs/errors",
                           log_truncate_chars=3000):
    """Build a consolidated multi-run markdown report.

    runs: list of dicts, each with keys:
        run_idx     int
        start       datetime
        end         datetime
        exit_code   int
        junit_path  str  (may not exist if pytest crashed)
        html_path   str  (may not exist)
    output_path: destination .md file path.

    Returns: the path written.
    """
    parsed = [(r, _parse_junit(r.get("junit_path"))) for r in runs]

    out = []
    out.append("# Master Run Report")
    out.append("")
    out.append(f"**Generated:** {datetime.now().isoformat(timespec='seconds')}  ")
    out.append(f"**Number of runs:** {len(runs)}  ")
    out.append("")

    # ---------- Summary table ----------
    out.append("## Summary")
    out.append("")
    out.append("| Run | Started | Duration | Tests | Pass | Fail | Skip | Errors | Status |")
    out.append("|---:|---|---:|---:|---:|---:|---:|---:|:---:|")

    totals = {"tests": 0, "pass": 0, "fail": 0, "skip": 0, "err": 0, "dur": 0.0}
    for run, data in parsed:
        if data is None:
            wall = (run["end"] - run["start"]).total_seconds()
            out.append(f"| {run['run_idx']} | "
                       f"{run['start'].strftime('%Y-%m-%d %H:%M:%S')} "
                       f"| {wall:.1f}s* | — | — | — | — | — | ❌ no junit |")
            continue
        passed = data["tests"] - data["failures"] - data["errors"] - data["skipped"]
        failed_or_err = data["failures"] + data["errors"]
        status = "✅" if failed_or_err == 0 else "❌"
        out.append(
            f"| {run['run_idx']} | "
            f"{run['start'].strftime('%Y-%m-%d %H:%M:%S')} "
            f"| {data['time']:.1f}s | {data['tests']} | {passed} "
            f"| {data['failures']} | {data['skipped']} | {data['errors']} "
            f"| {status} |"
        )
        totals["tests"] += data["tests"]
        totals["pass"] += passed
        totals["fail"] += data["failures"]
        totals["skip"] += data["skipped"]
        totals["err"] += data["errors"]
        totals["dur"] += data["time"]

    grand = "✅" if totals["fail"] + totals["err"] == 0 else "❌"
    out.append(
        f"| **TOTAL** | — | **{totals['dur']:.1f}s** | **{totals['tests']}** "
        f"| **{totals['pass']}** | **{totals['fail']}** | **{totals['skip']}** "
        f"| **{totals['err']}** | **{grand}** |"
    )
    out.append("")
    out.append("*\\* duration shown is wall-clock when junit XML is missing.*")
    out.append("")

    if totals["tests"] > 0:
        rate = 100 * totals["pass"] / totals["tests"]
        out.append(f"**Aggregate pass rate:** "
                   f"{totals['pass']} / {totals['tests']} = **{rate:.1f}%**")
        out.append("")

    # ---------- Failure Analysis (root-cause pattern surfacing) ----------
    error_buckets, class_failures, class_totals = _build_failure_analysis(parsed)

    if error_buckets:
        out.append("## Failure Analysis")
        out.append("")
        out.append("Groups failures across all runs by exception type. When many tests "
                   "fail with the same exception, the root cause is usually upstream "
                   "(a broken fixture, login, or shared infra) — fix that one thing and "
                   "the bucket goes green.")
        out.append("")

        # Top error types
        sorted_errors = sorted(error_buckets.items(), key=lambda kv: -len(kv[1]))
        out.append("### Most common error patterns")
        out.append("")
        out.append("| Exception | Failures | Sample message |")
        out.append("|---|---:|---|")
        for err_key, hits in sorted_errors[:6]:
            sample = (hits[0]["msg"] if hits else "").replace("|", "\\|")[:120]
            out.append(f"| `{err_key}` | {len(hits)} | `{sample}` |")
        if len(sorted_errors) > 6:
            other_count = sum(len(v) for _, v in sorted_errors[6:])
            out.append(f"| _… {len(sorted_errors) - 6} other exception type(s)_ | {other_count} | |")
        out.append("")

        # Class-wide failure detection
        big_class_failures = []
        for cls, fail_count in class_failures.items():
            total = class_totals[cls]
            if total >= 2 and fail_count / total >= 0.8:
                big_class_failures.append((cls, fail_count, total))

        if big_class_failures:
            out.append("### Class-wide failures (≥80% of tests in the class failed)")
            out.append("")
            out.append("This pattern almost always means a class-scoped fixture, the "
                       "first `test_01_login` step, or a shared setup is failing — every "
                       "subsequent test in the class then cascades.")
            out.append("")
            out.append("| Test class | Failed | Total | Rate |")
            out.append("|---|---:|---:|---:|")
            for cls, fail, total in sorted(big_class_failures, key=lambda t: -t[1]):
                pct = int(100 * fail / total)
                out.append(f"| `{cls}` | {fail} | {total} | {pct}% |")
            out.append("")

    # ---------- Stability index ----------
    failed_in_runs = defaultdict(list)
    skipped_in_runs = defaultdict(list)
    for run, data in parsed:
        if data is None:
            continue
        for tc in data["testcases"]:
            full_id = f"{tc['classname'].split('.')[-1]}::{tc['name']}"
            if tc["failed"]:
                failed_in_runs[full_id].append(run["run_idx"])
            elif tc["skipped"]:
                skipped_in_runs[full_id].append(run["run_idx"])

    if failed_in_runs:
        out.append("## Stability Index — Tests with Failures")
        out.append("")
        out.append("Tests that failed in one or more runs (regression / flake candidates). "
                   "Sorted by failure rate × name; capped to top 10 below — full list is "
                   "in the attached per-run JUnit XML.")
        out.append("")
        out.append("| Test | Failed in runs | Failure rate |")
        out.append("|---|---|---:|")
        sorted_fails = sorted(failed_in_runs.items(),
                              key=lambda x: (-len(x[1]), x[0]))
        SHOW_STAB = 10
        for tid, idxs in sorted_fails[:SHOW_STAB]:
            rate = f"{len(idxs)} / {len(runs)}"
            out.append(f"| `{tid}` | {idxs} | {rate} |")
        if len(sorted_fails) > SHOW_STAB:
            out.append(f"| _… and **{len(sorted_fails) - SHOW_STAB}** more failed tests_ "
                       f"| _(see attached JUnit)_ | |")
        out.append("")

    if skipped_in_runs:
        out.append("## Skipped Tests")
        out.append("")
        out.append("Tests skipped in one or more runs (typically: feature gap / "
                   "control absent in current build):")
        out.append("")
        out.append("| Test | Skipped in runs |")
        out.append("|---|---|")
        for tid, idxs in sorted(skipped_in_runs.items()):
            out.append(f"| `{tid}` | {idxs} |")
        out.append("")

    # ---------- Per-run details ----------
    out.append("## Per-Run Details")
    out.append("")

    for run, data in parsed:
        out.append(f"### Run {run['run_idx']} — "
                   f"{run['start'].strftime('%Y-%m-%d %H:%M:%S')}")
        out.append("")

        if data is None:
            out.append("*JUnit XML missing or unparseable — pytest may have crashed "
                       "before writing output.*")
            if run.get("junit_path"):
                out.append(f"  - expected: `{run['junit_path']}`")
            out.append(f"  - exit code: `{run.get('exit_code', '?')}`")
            out.append("")
            continue

        passed = data["tests"] - data["failures"] - data["errors"] - data["skipped"]
        fe = data["failures"] + data["errors"]
        status = "✅ all passed" if fe == 0 else f"❌ {fe} failure(s)"
        out.append(f"- **Status:** {status}")
        out.append(f"- **Duration:** {data['time']:.2f}s")
        out.append(f"- **Tests:** {data['tests']} "
                   f"({passed} pass, {data['failures']} fail, "
                   f"{data['skipped']} skip, {data['errors']} err)")
        out.append(f"- **Exit code:** `{run.get('exit_code', '?')}`")
        if run.get("html_path") and os.path.exists(run["html_path"]):
            out.append(f"- **Detailed HTML report:** "
                       f"[`{run['html_path']}`]({_rel(run['html_path'], output_path)})")
        if run.get("junit_path") and os.path.exists(run["junit_path"]):
            out.append(f"- **JUnit XML:** "
                       f"[`{run['junit_path']}`]({_rel(run['junit_path'], output_path)})")
        out.append("")

        # Failure details + zero-touch artifacts (matched by run window)
        failures = [tc for tc in data["testcases"] if tc["failed"]]
        if not failures:
            out.append("*All tests passed in this run.*")
            out.append("")
            continue

        run_arts = _find_artifacts_for_run(errors_dir, run["start"], run["end"])

        # Cap how many failures we show in detail. The full list lives in the
        # attached per-run HTML/junit; the master report stays scannable.
        SHOW_FAILS_DETAIL = 5
        if len(failures) > SHOW_FAILS_DETAIL:
            out.append(f"*Showing first {SHOW_FAILS_DETAIL} of {len(failures)} failures "
                       f"in detail. Full list in attached `run_{run['run_idx']}_report.html`.*")
            out.append("")

        for tc in failures[:SHOW_FAILS_DETAIL]:
            test_name = tc["name"]
            cls_name = tc["classname"].split(".")[-1]
            full_id = f"{cls_name}::{test_name}"
            out.append(f"#### ❌ `{full_id}`")
            out.append("")
            if tc["failure_message"]:
                msg_one_line = tc["failure_message"].strip().splitlines()[0][:300]
                out.append(f"**Error:** `{msg_one_line}`")
                out.append("")

            arts = run_arts.get(test_name)
            if not arts:
                out.append("*(no zero-touch artifacts captured for this failure within "
                           "the run window — failure may have occurred during fixture "
                           "setup before the conftest hook ran)*")
                out.append("")
                continue

            for s in arts["screenshots"]:
                out.append(f"![{os.path.basename(s)}]({_rel(s, output_path)})")
                out.append("")

            for lg in arts["logs"]:
                out.append(f"**Zero-touch error log:** "
                           f"[`{os.path.basename(lg)}`]({_rel(lg, output_path)})")
                out.append("")
                try:
                    with open(lg, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                    if len(content) > log_truncate_chars:
                        content = (content[:log_truncate_chars]
                                   + "\n... (truncated — open the log file for the full content)")
                    out.append("```")
                    out.append(content)
                    out.append("```")
                except Exception as e:
                    out.append(f"*(could not read log: {type(e).__name__}: {e})*")
                out.append("")

    # ---- Write file ----
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return output_path
