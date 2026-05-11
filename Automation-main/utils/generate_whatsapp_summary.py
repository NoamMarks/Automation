"""
WhatsApp-friendly short summary for sharing in chat.

Plain text (UTF-8), emoji-rich, Hebrew-localized. Generated alongside
the other reports by `tests/run_multiple.py`. The file lives at:

    reports/master/WhatsApp_Summary_<TS>.txt

Same call signature as the other report generators:
    generate_whatsapp_summary(runs, output_path)
"""

import os
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime


# Hebrew display names for each test class. Used in the auto-generated
# status line ("recurring failures in <X>"). Falls back to the class
# name if a class is missing here.
HEBREW_AREA_NAMES = {
    "TestKnownRegressions":       "מעקב באגים פתוחים",
    "TestDomainLinkCascade":      "מחיקת עולמות תוכן",
    "TestEnvironmentLinkCascade": "סביבות וקישורים",
    "TestPortalClient":           "ניהול CRUD בסיסי",
    "TestMessagesFlows":          "מודעות (פופ-אפ)",
    "TestMessageReactivation":    "הפעלה/השבתה של מודעות",
    "TestPublicHomepage":         "דף הבית הציבורי",
    "TestEndUserFlows":           "חוויית משתמש קצה",
    "TestInactiveLink":           "קישורים לא פעילים",
    "TestLinksAdminGrid":         "טבלת קישורים בניהול",
    "TestImageUpload":            "העלאת תמונות",
    "TestNegLinks":               "ולידציה של טפסי קישור",
    "TestCascade":                "קשר עולם-תוכן ↔ קישור",
    "TestTagLinkCascade":         "תגיות ↔ קישורים",
    "TestTagMessageCascade":      "תגיות ↔ מודעות",
    "TestDiscard":                "ביטול/שמירה של טפסים",
    "TestURLAppend":              "פרמטרי URL בסביבות",
    "TestXSSLink":                "סינון קלט בסיסי (XSS)",
}


def _parse_junit(junit_path):
    """Read one JUnit XML and return per-run summary + per-test details."""
    if not junit_path or not os.path.exists(junit_path):
        return None
    try:
        root = ET.parse(junit_path).getroot()
        suite = root.find("testsuite") if root.tag != "testsuite" else root
        tests = int(suite.attrib.get("tests", 0))
        failures = int(suite.attrib.get("failures", 0))
        errors = int(suite.attrib.get("errors", 0))
        skipped = int(suite.attrib.get("skipped", 0))
        passed = tests - failures - errors - skipped
        failed = failures + errors
        rate = (100 * passed / tests) if tests else 0
        cases = []
        for tc in suite.findall("testcase"):
            cases.append({
                "classname": tc.attrib.get("classname", ""),
                "name":      tc.attrib.get("name", ""),
                "failed":    (tc.find("failure") is not None) or
                             (tc.find("error") is not None),
                "skipped":   tc.find("skipped") is not None,
            })
        return {
            "tests": tests, "passed": passed, "failed": failed,
            "skipped": skipped, "rate": rate, "cases": cases,
        }
    except Exception:
        return None


def _build_status_line(parsed_runs):
    """Pick the right Hebrew status line based on the failure pattern.

    Rules (in order):
      1. No failures anywhere       → "כל הבדיקות עברו בהצלחה."
      2. ≥50% of failures in one class AND that class failed in 2+ runs
                                    → "ישנן תקלות חוזרות ברכיב <X>"
      3. ≥50% of failures in one class (single run)
                                    → "נמצאו תקלות בעיקר ברכיב <X>"
      4. Failures scattered          → "נמצאו תקלות שונות במספר רכיבים"
    """
    class_fail_runs = defaultdict(set)   # class -> {run_idx, ...}
    class_fail_count = Counter()
    total_failures = 0

    for run, data in parsed_runs:
        if data is None:
            continue
        for tc in data["cases"]:
            if tc["failed"]:
                cls = tc["classname"].split(".")[-1] or "<unknown>"
                class_fail_runs[cls].add(run["run_idx"])
                class_fail_count[cls] += 1
                total_failures += 1

    if total_failures == 0:
        return "✅ סטטוס כללי: כל הבדיקות עברו בהצלחה."

    top_class, top_count = class_fail_count.most_common(1)[0]
    runs_with_top = len(class_fail_runs[top_class])
    top_name = HEBREW_AREA_NAMES.get(top_class, top_class)

    if top_count >= 0.5 * total_failures and runs_with_top >= 2:
        return f"⚠️ סטטוס כללי: ישנן תקלות חוזרות ברכיב {top_name}."
    if top_count >= 0.5 * total_failures:
        return f"⚠️ סטטוס כללי: נמצאו תקלות בעיקר ברכיב {top_name}."
    return "⚠️ סטטוס כללי: נמצאו תקלות שונות במספר רכיבים."


def generate_whatsapp_summary(runs, output_path):
    """Build the WhatsApp-shareable summary. Returns the path written."""
    parsed = [(r, _parse_junit(r.get("junit_path"))) for r in runs]
    now = datetime.now()

    lines = []
    lines.append("📊 תוצאות בדיקות אוטומציה - מערכת זירה")
    lines.append(f"🗓 תאריך: {now.strftime('%d.%m.%Y')}")
    lines.append(f"🕒 זמן הרצה: {now.strftime('%H:%M')}")
    lines.append("")
    lines.append("סיכום הרצות:")
    for run, data in parsed:
        if data is None:
            lines.append(f"🔹 הרצה מס' {run['run_idx']}: ⚠️ לא ניתן לקרוא נתוני JUnit")
            continue
        lines.append(
            f"🔹 הרצה מס' {run['run_idx']}: "
            f"✅ {data['passed']} | ❌ {data['failed']} | 🟡 {data['skipped']} "
            f"({data['rate']:.0f}% Pass)"
        )
    lines.append("")
    lines.append(_build_status_line(parsed))
    lines.append("")
    lines.append("לשאלות נוספות, צוות ה-QA זמין עבורכם.")

    text = "\n".join(lines)
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)
    return output_path
