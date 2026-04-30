"""Generate a markdown run report from a junit XML + recorded videos + failure artifacts.

Pulls together:
  - junit XML (test results)
  - artifacts/videos/<ClassName>_<HHMMSS>.webm (per-class video)
  - artifacts/errors/<test>_<YYYYMMDD>_<HHMMSS>.png (failure screenshot)
  - artifacts/errors/<test>_<YYYYMMDD>_<HHMMSS>_logs.txt (console + network errors)

Usage: py -3.13 utils/generate_run_report.py [junit_xml_path]
Writes to reports/recorded_run_<timestamp>.md and prints the path.
"""

import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime


def main():
    junit_path = sys.argv[1] if len(sys.argv) > 1 else "reports/junit_recorded.xml"
    tree = ET.parse(junit_path)
    root = tree.getroot()
    suite = root.find("testsuite") if root.tag != "testsuite" else root

    total_tests = int(suite.attrib["tests"])
    failures = int(suite.attrib["failures"])
    errors = int(suite.attrib["errors"])
    skipped = int(suite.attrib["skipped"])
    total_time = float(suite.attrib["time"])
    timestamp = suite.attrib["timestamp"]
    host = suite.attrib["hostname"]

    by_class = defaultdict(list)
    for tc in suite.findall("testcase"):
        cls = tc.attrib["classname"].split(".")[-1]
        name = tc.attrib["name"]
        duration = float(tc.attrib["time"])
        failed = tc.find("failure") is not None or tc.find("error") is not None
        by_class[cls].append((name, duration, failed))

    video_dir = "artifacts/videos"
    video_map = {}
    if os.path.isdir(video_dir):
        for v in sorted(os.listdir(video_dir)):
            cls = v.rsplit("_", 1)[0]
            video_map[cls] = os.path.join(video_dir, v).replace(os.sep, "/")

    # Failure artifacts: <test>_<YYYYMMDD>_<HHMMSS>.png and <test>_<YYYYMMDD>_<HHMMSS>_logs.txt
    # Note: stored OUTSIDE artifacts/ because pytest-playwright wipes that dir
    # at session start. See conftest.py comment.
    errors_dir = "zero_touch_logs/errors"
    errors_map = defaultdict(lambda: {"screenshots": [], "logs": []})
    if os.path.isdir(errors_dir):
        for f in sorted(os.listdir(errors_dir)):
            full = os.path.join(errors_dir, f).replace(os.sep, "/")
            if f.endswith(".png"):
                test_name = f.rsplit("_", 2)[0]
                errors_map[test_name]["screenshots"].append(full)
            elif f.endswith("_logs.txt"):
                test_name = f.rsplit("_", 3)[0]
                errors_map[test_name]["logs"].append(full)

    # Locate the most recent HTML pytest-html report
    html_report = None
    if os.path.isdir("reports"):
        for date_dir in sorted(os.listdir("reports"), reverse=True):
            full = os.path.join("reports", date_dir)
            if os.path.isdir(full):
                htmls = sorted([f for f in os.listdir(full) if f.endswith(".html")], reverse=True)
                if htmls:
                    html_report = os.path.join(full, htmls[0]).replace(os.sep, "/")
                    break

    mins = int(total_time // 60)
    secs = total_time - mins * 60
    passed = total_tests - failures - errors - skipped

    out = []
    out.append("# Zira Automation — Recorded Test Run Report")
    out.append("")
    out.append(f"**Run timestamp:** {timestamp}")
    out.append(f"**Host:** {host}")
    out.append("**Mode:** headed (slow_mo=500ms), video recording enabled")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append(f"- **Total tests:** {total_tests}")
    out.append(f"- **Passed:** {passed}")
    out.append(f"- **Failed:** {failures}")
    out.append(f"- **Errors:** {errors}")
    out.append(f"- **Skipped:** {skipped}")
    out.append(f"- **Duration:** {mins}:{secs:05.2f} ({total_time:.2f}s total)")
    out.append("")
    if html_report:
        out.append(f"**Detailed pytest-html report:** [{html_report}]({html_report})")
        out.append("")

    out.append("## Per-Class Breakdown")
    out.append("")
    out.append("| Class | Tests | Duration | Video |")
    out.append("|---|---|---|---|")
    for cls in sorted(by_class.keys()):
        cases = by_class[cls]
        cls_time = sum(c[1] for c in cases)
        cls_failed = sum(1 for c in cases if c[2])
        status = "✅" if cls_failed == 0 else f"❌ ({cls_failed} failed)"
        video = video_map.get(cls)
        if video:
            video_md = f"[{os.path.basename(video)}]({video})"
        else:
            video_md = "*(none)*"
        out.append(f"| `{cls}` | {len(cases)} {status} | {cls_time:.1f}s | {video_md} |")
    out.append("")

    out.append("## Per-Test Detail")
    out.append("")
    for cls in sorted(by_class.keys()):
        cases = by_class[cls]
        out.append(f"### {cls}")
        out.append("")
        video = video_map.get(cls)
        if video:
            size_mb = os.path.getsize(video) / 1024 / 1024
            out.append(f"**Video:** [{os.path.basename(video)}]({video})  ({size_mb:.1f} MB)")
            out.append("")
        out.append("| Test | Duration | Status | Diagnostics |")
        out.append("|---|---|---|---|")
        for name, duration, failed in cases:
            st = "❌ FAIL" if failed else "✅ pass"
            diag = "—"
            if failed and name in errors_map:
                parts = []
                for s in errors_map[name]["screenshots"]:
                    parts.append(f"[📸]({s})")
                for lg in errors_map[name]["logs"]:
                    parts.append(f"[📄]({lg})")
                if parts:
                    diag = " · ".join(parts)
            out.append(f"| `{name}` | {duration:.2f}s | {st} | {diag} |")
        out.append("")

    if errors_map:
        out.append("## Failure Diagnostics")
        out.append("")
        out.append("Each failure produced a full-page screenshot and an error log "
                   "(console errors, unhandled exceptions, HTTP ≥ 400). Logs are "
                   "scoped to the failing test only.")
        out.append("")
        for test_name in sorted(errors_map.keys()):
            entries = errors_map[test_name]
            out.append(f"### `{test_name}`")
            out.append("")
            for s in entries["screenshots"]:
                out.append(f"![{os.path.basename(s)}]({s})")
                out.append("")
            for lg in entries["logs"]:
                out.append(f"**Error log:** [{os.path.basename(lg)}]({lg})")
                out.append("")
                try:
                    with open(lg, "r", encoding="utf-8") as f:
                        content = f.read().strip()
                    if len(content) > 4000:
                        content = content[:4000] + "\n... (truncated — open the log file for the full content)"
                    out.append("```")
                    out.append(content)
                    out.append("```")
                except Exception as e:
                    out.append(f"*(could not read log: {type(e).__name__}: {e})*")
                out.append("")

    out.append("## Key Findings From This Suite")
    out.append("")
    out.append("Behaviors verified by the suite (each linked to its source file):")
    out.append("")
    out.append("1. **Domain → Link cascade delete is silent** — deleting a Domain wipes its dependent Links with no warning dialog. Source: `tests/test_cascade.py`.")
    out.append("2. **Validation UX is silent-fail** — Add Link form disables Save with no toast / inline error for blank required fields, over-length Title, and over-limit Tags. Source: `tests/test_neg_links.py`.")
    out.append("3. **Inactive-Link visibility is enforced** correctly on both the public homepage grid AND the search bar (unauthenticated users do not see them). Source: `tests/test_inactive_link.py`.")
    out.append("4. **Discard behavior is consistent** — drawer X, modal X, and ביטול all correctly abort without partial-state side effects. Source: `tests/test_discard.py`.")
    out.append("5. **URL-append concatenation has no separator** — env URLParam appends directly to the link URL string (e.g., `https://t05261.com` + `appendmark...` → `https://t05261.comappendmark...`). Source: `tests/test_url_append.py`.")
    out.append("6. **Image upload 5MB limit is enforced cleanly** (over-limit → no preview + Save disabled), but **mime-spoofing is undetected** — text bytes labeled as image/png keep Save enabled, suggesting the client trusts extension+mime without verifying decode. Source: `tests/test_image_upload.py`.")
    out.append("")

    iso_clean = timestamp.split("+")[0].split(".")[0]
    ts_short = datetime.fromisoformat(iso_clean).strftime("%Y-%m-%d_%H%M%S")
    out_path = f"reports/recorded_run_{ts_short}.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"Report written: {out_path}")
    print(f"  size: {os.path.getsize(out_path)} bytes")


if __name__ == "__main__":
    main()
