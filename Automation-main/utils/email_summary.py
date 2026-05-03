"""
Build an email-friendly digest from the latest Master Run Report.

CI workflow calls this AFTER run_multiple.py. It produces:
  - reports/master/email_body.md   — short markdown digest (used as email body)
  - GitHub Actions outputs          — counts and a status emoji for the subject line

Usage:
    py -3.13 utils/email_summary.py
"""

import glob
import os
import re
import sys


def _force_utf8():
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass


def find_latest_master_md(reports_dir="reports/master"):
    files = glob.glob(os.path.join(reports_dir, "Master_Run_Report_*.md"))
    return max(files, key=os.path.getmtime) if files else None


def extract_section(content, header_text):
    """Return everything between '## <header_text>' and the next '## ' (or EOF)."""
    pattern = rf"## {re.escape(header_text)}\s*\n(.+?)(?=\n## |\Z)"
    m = re.search(pattern, content, re.DOTALL)
    return m.group(1).strip() if m else ""


def parse_totals(content):
    """Pull the numeric TOTAL row out of the Summary table."""
    line = re.search(
        r"\|\s*\*\*TOTAL\*\*\s*\|.*?\|\s*\*\*([\d.]+)s?\*\*\s*\|"
        r"\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|"
        r"\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|",
        content,
    )
    if not line:
        return None
    duration, total, pass_, fail, skip, err = line.groups()
    return {
        "duration": float(duration),
        "total":    int(total),
        "pass":     int(pass_),
        "fail":     int(fail),
        "skip":     int(skip),
        "err":      int(err),
    }


def build_summary(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    summary  = extract_section(content, "Summary")
    stab     = extract_section(content, "Stability Index — Tests with Failures")
    skipped  = extract_section(content, "Skipped Tests")
    totals   = parse_totals(content) or {}

    pass_rate = ""
    m = re.search(r"\*\*Aggregate pass rate:\*\*\s*([^\n]+)", content)
    if m:
        pass_rate = m.group(1).strip()

    out = []
    out.append("# Zira E2E — Run Summary")
    out.append("")
    if pass_rate:
        out.append(f"**Aggregate pass rate:** {pass_rate}")
        out.append("")

    if summary:
        out.append("## Summary")
        out.append("")
        out.append(summary)
        out.append("")

    if stab:
        out.append("## Stability Index — Tests with Failures")
        out.append("")
        # Cap stability section so emails stay readable when many tests flake.
        if len(stab) > 4000:
            stab = stab[:4000] + "\n\n*(truncated — see attached master report)*"
        out.append(stab)
        out.append("")

    if skipped:
        out.append("## Skipped Tests")
        out.append("")
        out.append(skipped)
        out.append("")

    out.append("---")
    out.append("")
    out.append(f"_Source master report:_ `{os.path.basename(md_path)}` (attached)  ")
    out.append("_Per-run pytest-html report and JUnit XML are also attached._")
    return "\n".join(out), totals


def status_emoji(totals):
    if not totals:
        return "❓"
    if totals.get("fail", 0) + totals.get("err", 0) == 0:
        return "✅"
    return "❌"


def write_github_outputs(md_path, body_path, totals, emoji):
    """If running inside GitHub Actions, emit step outputs for downstream steps
    (subject line, attachment globs, etc.)."""
    out_file = os.environ.get("GITHUB_OUTPUT")
    if not out_file:
        return
    with open(out_file, "a", encoding="utf-8") as f:
        f.write(f"master_md_path={md_path}\n")
        f.write(f"email_body_path={body_path}\n")
        f.write(f"status_emoji={emoji}\n")
        for key in ("total", "pass", "fail", "skip", "err"):
            f.write(f"{key}={totals.get(key, 0)}\n")


def main():
    _force_utf8()
    md_path = find_latest_master_md()
    if not md_path:
        print("ERROR: no Master_Run_Report_*.md in reports/master/", file=sys.stderr)
        sys.exit(1)

    body, totals = build_summary(md_path)
    body_path = os.path.join("reports", "master", "email_body.md")
    os.makedirs(os.path.dirname(body_path), exist_ok=True)
    with open(body_path, "w", encoding="utf-8") as f:
        f.write(body)

    emoji = status_emoji(totals)
    print(f"[email_summary] master report: {md_path}")
    print(f"[email_summary] email body   : {body_path}")
    print(f"[email_summary] totals       : {totals}")
    print(f"[email_summary] status emoji : {emoji}")
    write_github_outputs(md_path, body_path, totals, emoji)


if __name__ == "__main__":
    main()
