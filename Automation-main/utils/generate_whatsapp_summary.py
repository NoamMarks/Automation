"""
WhatsApp-friendly short summary for sharing in chat.

Plain text (UTF-8), Hebrew-localized. Generated alongside the other
reports by `tests/run_multiple.py`. The file lives at:

    reports/master/WhatsApp_Summary_<TS>.txt

Same call signature as the other report generators:
    generate_whatsapp_summary(runs, output_path, pdf_path=None)

The message is deliberately minimal — when, how big the run was, how it
scored overall, how long it took. Deep diagnostics (stability alerts,
per-area outliers, individual failing tests) live in the attached PDF
dashboard.
"""

import os
import xml.etree.ElementTree as ET
from datetime import datetime


def _parse_junit(junit_path):
    """Read one JUnit XML's <testsuite> attributes. Returns None if unreadable."""
    if not junit_path or not os.path.exists(junit_path):
        return None
    try:
        root = ET.parse(junit_path).getroot()
        suite = root.find("testsuite") if root.tag != "testsuite" else root
        tests = int(suite.attrib.get("tests", 0))
        failures = int(suite.attrib.get("failures", 0))
        errors = int(suite.attrib.get("errors", 0))
        skipped = int(suite.attrib.get("skipped", 0))
        return {
            "tests": tests,
            "passed": tests - failures - errors - skipped,
            "skipped": skipped,
        }
    except Exception:
        return None


def _fmt_dur(seconds):
    """510.4 → '8m 30s' ; 65 → '1m 05s' ; 45 → '45s'."""
    if seconds < 60:
        return f"{int(round(seconds))}s"
    m, s = divmod(int(round(seconds)), 60)
    if m < 60:
        return f"{m}m {s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m"


def generate_whatsapp_summary(runs, output_path, pdf_path=None):
    """Build the WhatsApp-shareable summary. Returns the path written.

    `pdf_path` kwarg is accepted for backward compatibility with callers
    but ignored — the message text no longer references the PDF (the PDF
    is attached to the WhatsApp chat manually by the sender).
    """
    parsed = [_parse_junit(r.get("junit_path")) for r in runs]
    valid = [d for d in parsed if d is not None]
    n_runs = len(parsed)
    now = datetime.now()

    total_exec = sum(d["tests"] for d in valid)
    total_pass = sum(d["passed"] for d in valid)
    pass_rate = (100 * total_pass / total_exec) if total_exec else 0.0

    durations = [(r["end"] - r["start"]).total_seconds() for r in runs]

    lines = []
    lines.append("*סיכום הרצת אוטומציה*")
    lines.append("")
    lines.append(f"*תאריך:* {now.strftime('%d.%m.%Y')}  🕒 {now.strftime('%H:%M')}")
    lines.append("")
    lines.append(
        f"*הרצות:* {n_runs} איטרציות "
        f"(סה\"כ {total_exec} בדיקות)"
    )
    lines.append(f"*אחוז הצלחה כללי:* {pass_rate:.1f}%📊")
    lines.append("")

    if durations:
        lines.append("*זמני הרצה:* ")
        lines.append(f"ממוצע: {_fmt_dur(sum(durations) / len(durations))}")
        lines.append(f"מקסימום: {_fmt_dur(max(durations))}")
        lines.append(f"מינימום: {_fmt_dur(min(durations))}")
        lines.append("")

    lines.append("לשאלות נוספות, צוות ה-QA זמין עבורכם👾")

    text = "\n".join(lines)
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
