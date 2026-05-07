"""
Plain-English test run report.

Produces a single markdown file that a non-technical reader (PM, manager,
business stakeholder) can pick up and understand without needing to know
what pytest, Playwright, or a "selector" is.

Same call signature as before:
    generate_simple_summary(runs, output_path)
where `runs` is the list of run-dicts from run_multiple.py.

Output sections:
    1. At a glance        — headline numbers + plain-English bottom line
    2. What does this mean — a short primer for non-technical readers
    3. By feature area    — each test class translated to a feature, with status
    4. What broke         — every failure with plain-English why + technical why
    5. What was deferred  — skipped tests with plain-English reason
    6. Full pass list     — compact view of every passing test
    7. Glossary           — terms used in this report
"""

import os
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime


# ============================================================
# Translation tables — what each test class actually tests
# ============================================================

FEATURE_AREAS = {
    "TestCascade": {
        "title": "Domain–Link basic relationships",
        "explanation": "Creating a domain, attaching a link to it, then trying to delete the domain. Verifies the system handles parent-child cleanup correctly.",
    },
    "TestDiscard": {
        "title": "Discard / cancel safety",
        "explanation": "When you close a form without saving (X button or Cancel), the system must not accidentally save or delete data. Also covers the delete-confirmation dialog.",
    },
    "TestDomainLinkCascade": {
        "title": "Domain → Link cascade behavior",
        "explanation": "By design, when a domain is deleted the links attached to it are silently removed (this is the spec). This test verifies the silent-cascade behavior matches the spec.",
    },
    "TestEndUserFlows": {
        "title": "End-user (visitor) journeys on the public site",
        "explanation": "Real-world user actions: searching for a link, clicking it (and verifying the click count goes up), navigating between domains. This is what an actual visitor experiences.",
    },
    "TestEnvironmentLinkCascade": {
        "title": "Environment ↔ Link relationships",
        "explanation": "Creating environments, attaching them to links, deleting environments and confirming the link's environment list updates correctly.",
    },
    "TestImageUpload": {
        "title": "Image upload validation",
        "explanation": "Uploading images for messages: a valid image under the size limit must succeed; a too-large image must be rejected; a wrong-format file (e.g. .txt) must be rejected.",
    },
    "TestInactiveLink": {
        "title": "Inactive link visibility",
        "explanation": "When an admin marks a link as 'inactive', it must NOT show up on the public site. Inactive = hidden from visitors.",
    },
    "TestLinksAdminGrid": {
        "title": "Admin links list — search and sort",
        "explanation": "On the admin Links page, can you search the list by typing? Can you sort by clicking a column header? These are basic admin productivity features.",
    },
    "TestMessageReactivation": {
        "title": "Message activation round-trip",
        "explanation": "Toggling a popup message between active and inactive (and back, and again). Each toggle must correctly show or hide the message on the public homepage.",
    },
    "TestMessagesFlows": {
        "title": "Popup messages (notifications)",
        "explanation": "Creating a popup-style message with an attached image, previewing it from the admin, verifying it appears on the public site, toggling its status.",
    },
    "TestModeratorWorkflow": {
        "title": "Moderator role permissions (legacy file — known broken)",
        "explanation": "Tests for the moderator user role. This file has a known code bug (a missing import statement) that we deliberately left in place as a sanity-check signal — if these 5 tests ever start passing, something has changed.",
    },
    "TestNegLinks": {
        "title": "Link form input validation (negative tests)",
        "explanation": "Wrong inputs must be rejected: blank title, blank URL, no domain selected, name longer than 30 characters, description longer than the limit.",
    },
    "TestPortalClient": {
        "title": "Admin CRUD basics — every resource type",
        "explanation": "Create / Update / Delete operations on every admin resource: domains, environments, links, messages, tags. The fundamental building blocks.",
    },
    "TestPublicHomepage": {
        "title": "Public homepage layout & navigation",
        "explanation": "What a visitor sees on the front page: footer (version + logos), header (date + status badge), domain carousel arrow, message carousel navigation, support contact link, app tabs.",
    },
    "TestSecurityRouting": {
        "title": "Moderator role validation — direct URL access",
        "explanation": "If a moderator-level user pastes an admin-only URL into the address bar, the system should not let them reach the admin features. Validates that the page either redirects, returns a 'no permission' state, or renders an empty shell — and that admin create/edit buttons are never visible to a moderator.",
    },
    "TestTagLinkCascade": {
        "title": "Tag ↔ Link cascade",
        "explanation": "Attaching a tag to a link, then deleting the tag. The link should remain but lose the tag (NULLIFY behavior).",
    },
    "TestTagMessageCascade": {
        "title": "Tag ↔ Message cascade",
        "explanation": "Attempting to attach a tag to a message. (Per spec, messages don't actually accept tags — this verifies that constraint.)",
    },
    "TestURLAppend": {
        "title": "Environment URL-parameter append",
        "explanation": "When a link is opened from inside a specific environment, the environment's URL parameter can optionally be appended to the link's URL. Tests both the 'append' and 'don't append' settings.",
    },
    "TestXSSLink": {
        "title": "Basic XSS sanitization smoke (NOT a security audit)",
        "explanation": (
            "Three small smoke checks on the link form: a `<svg onload=...>` "
            "payload in the title, the same payload in the description, and a "
            "`javascript:` URL in the URL field. Verifies these specific inputs "
            "are escaped/blocked when rendered on the public site. "
            "**This is NOT a full security review.** It does not cover: stored "
            "XSS in other forms (messages, tags, domains, environments), DOM-based "
            "XSS, CSP / SRI / CORS headers, CSRF tokens, authentication boundaries, "
            "rate limiting, SQL/NoSQL injection, file-upload exploits, or any "
            "fuzzed payload library. A proper penetration test by a security "
            "specialist is still required before treating the system as 'secure'."
        ),
    },
    "TestKnownRegressions": {
        "title": "Known open bugs (regression tracker)",
        "explanation": "These tests assert the *correct* behavior for documented bugs that DevOps has not yet fixed. Until each bug is fixed, the matching test will FAIL — that is the intended signal. When a test in this group starts passing again, the corresponding bug has been fixed.",
    },
}

DEFAULT_AREA = {
    "title": "(unrecognized test file)",
    "explanation": "This test class isn't in our translation table. See the test file directly for what it covers.",
}


# ============================================================
# Error message translation — turn a stack trace into one English sentence
# ============================================================

def _humanize_error(msg):
    """Convert a raw exception message to a plain-English explanation."""
    if not msg:
        return "(no error message was captured)"

    # First non-empty line of the message
    line = msg.strip().splitlines()[0]
    line = re.sub(r"\s+", " ", line).strip()

    # Specific, well-known patterns first
    if re.search(r"NameError.*'os' is not defined", line):
        return ("A line of code in this test file uses the `os` tool but the file "
                "is missing an `import os` line at the top. The test crashes "
                "before doing anything. This is a code bug, not a website bug. "
                "(One-line fix: add `import os` to the top of the file.)")
    if re.search(r"NameError.*not defined", line):
        return ("The test file references a name that wasn't imported or defined. "
                "Code bug in the test itself, not a website issue.")
    if re.search(r"TimeoutError.*Locator\.click", line):
        return ("The test tried to click a button and waited 30 seconds for it to "
                "become clickable, but the button never reacted. The page froze "
                "or the button stayed disabled. Could be slow backend, missing form "
                "field, or a UI regression.")
    if re.search(r"TimeoutError.*Locator\.fill", line):
        return ("The test tried to type into a form field, but the field never "
                "became typeable within 30 seconds.")
    if re.search(r"TimeoutError.*locator|TimeoutError.*expected to|TimeoutError.*to_be_visible", line):
        return ("The test was waiting for an element on the page to appear or "
                "change, and gave up after 30 seconds because nothing happened.")
    if re.search(r"500 Internal Server Error|status code 500|HTTP 500", line):
        return ("The backend server returned an error. The frontend was sending "
                "a valid request — the server-side code crashed. Backend team "
                "needs to investigate the server log.")
    if re.search(r"AxiosError.*Request failed", line):
        return ("The frontend tried to save or load data, but the request to "
                "the backend failed. Often points to a server-side bug.")
    if re.search(r"KeyError", line):
        return ("This test depends on data from an earlier step in the same test "
                "class. That earlier step failed, so this one couldn't run. "
                "Fix the earlier failure and this one will likely pass on its own.")
    if re.search(r"AssertionError", line):
        return ("The test ran successfully, but the result was different from "
                "what was expected. The website behaved differently than the "
                "spec describes.")
    if re.search(r"failed on setup", line):
        return ("The test never got to run — it failed during the setup step "
                "(usually login or navigation).")

    # Fallback — return the raw line, but flag it
    return f"Technical error (no plain-English translation available): {line[:200]}"


# ============================================================
# Test name humanization
# ============================================================

def _humanize_test_name(test_name):
    """test_02_create_inactive_link → 'Create an inactive link'."""
    name = re.sub(r"^test_\d+_", "", test_name)
    name = name.replace("_", " ")
    name = name.replace("XSS", "XSS")  # keep acronyms upright
    return name[:1].upper() + name[1:] if name else test_name


# ============================================================
# JUnit parsing
# ============================================================

def _parse_junit(junit_path):
    if not junit_path or not os.path.exists(junit_path):
        return None
    try:
        tree = ET.parse(junit_path)
        root = tree.getroot()
        suite = root.find("testsuite") if root.tag != "testsuite" else root
        cases = []
        for tc in suite.findall("testcase"):
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
            cases.append({
                "classname": tc.attrib.get("classname", ""),
                "name":      tc.attrib.get("name", ""),
                "time":      float(tc.attrib.get("time", 0)),
                "failed":    (failure is not None) or (error is not None),
                "skipped":   skipped is not None,
                "msg":       msg,
            })
        return cases
    except Exception:
        return None


def _short_id(classname, name):
    cls = classname.split(".")[-1] if classname else ""
    return f"{cls}::{name}" if cls else name


def _fmt_duration(seconds):
    if seconds < 60:
        return f"{seconds:.1f} seconds"
    m, s = divmod(int(seconds), 60)
    if m < 60:
        return f"{m} minute{'s' if m != 1 else ''} {s} second{'s' if s != 1 else ''}"
    h, m = divmod(m, 60)
    return f"{h} hour{'s' if h != 1 else ''} {m} minute{'s' if m != 1 else ''}"


# ============================================================
# Main report builder
# ============================================================

def generate_simple_summary(runs, output_path):
    """Build a non-technical-friendly markdown summary."""

    # ---------- Aggregate per-test outcome across all runs ----------
    by_id = {}
    classes = defaultdict(lambda: {"tests": [], "ids": []})

    for run in runs:
        cases = _parse_junit(run.get("junit_path")) or []
        for tc in cases:
            tid = _short_id(tc["classname"], tc["name"])
            cls_name = tc["classname"].split(".")[-1] or "<unknown>"

            entry = by_id.setdefault(tid, {
                "cls": cls_name, "name": tc["name"],
                "passes": 0, "fails": 0, "skips": 0,
                "last_fail_msg": "", "last_skip_msg": "",
            })
            if tc["failed"]:
                entry["fails"] += 1
                entry["last_fail_msg"] = tc["msg"]
            elif tc["skipped"]:
                entry["skips"] += 1
                entry["last_skip_msg"] = tc["msg"]
            else:
                entry["passes"] += 1

            if tid not in classes[cls_name]["ids"]:
                classes[cls_name]["ids"].append(tid)
                classes[cls_name]["tests"].append(entry)

    failed = [(tid, e) for tid, e in by_id.items() if e["fails"] > 0]
    skipped = [(tid, e) for tid, e in by_id.items()
               if e["fails"] == 0 and e["skips"] > 0]
    passed = [(tid, e) for tid, e in by_id.items()
              if e["fails"] == 0 and e["skips"] == 0]

    failed.sort(key=lambda x: x[0])
    skipped.sort(key=lambda x: x[0])
    passed.sort(key=lambda x: x[0])

    total_dur = sum((r["end"] - r["start"]).total_seconds() for r in runs)
    n_runs = len(runs)
    total = len(by_id)
    pass_rate = (100 * len(passed) / total) if total else 0

    out = []

    # ============================================================
    # Section 1 — At a glance
    # ============================================================
    out.append("# Test Run Report")
    out.append("")
    out.append(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
    out.append(f"**Total time:** {_fmt_duration(total_dur)}  ")
    out.append(f"**Number of full runs:** {n_runs}  ")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## At a glance")
    out.append("")
    out.append(f"- ✅ **{len(passed)} tests passed** out of {total} (**{pass_rate:.0f}%**)")
    out.append(f"- ❌ **{len(failed)} tests failed**")
    out.append(f"- ⏭️ **{len(skipped)} tests skipped** (deferred — see below)")
    out.append("")

    # Plain-English bottom-line
    if not failed and not skipped:
        verdict = "**Bottom line:** Everything passed. The website is healthy across every area we test."
    elif not failed:
        verdict = (f"**Bottom line:** No real failures. {len(skipped)} test(s) were "
                   "skipped because the feature they need isn't built yet (see "
                   "'What was deferred' below).")
    else:
        # Group failures by class to detect "all failures from one source"
        fail_classes = defaultdict(int)
        for _, e in failed:
            fail_classes[e["cls"]] += 1
        biggest_class, biggest_count = max(fail_classes.items(), key=lambda x: x[1])
        if biggest_count == len(failed) and len(fail_classes) == 1:
            area = FEATURE_AREAS.get(biggest_class, DEFAULT_AREA)
            verdict = (f"**Bottom line:** All {len(failed)} failures come from a single test file "
                       f"covering **{area['title']}**. "
                       "The rest of the website is healthy. See 'What broke' for the cause.")
        else:
            verdict = (f"**Bottom line:** {len(failed)} test(s) failed across "
                       f"{len(fail_classes)} feature area(s). "
                       "See 'What broke' for the plain-English explanation of each.")
    out.append(verdict)
    out.append("")

    # ============================================================
    # Section 2 — What does this mean
    # ============================================================
    out.append("---")
    out.append("")
    out.append("## What does this mean?")
    out.append("")
    out.append("A **test** is a small automated check. Examples:")
    out.append("")
    out.append("- *\"Click 'Add Link', fill the form, click Save, then verify the new link appears on the homepage.\"*")
    out.append("- *\"Try to log in with no password — verify the system blocks it.\"*")
    out.append("")
    out.append(f"We have **{total} of these tests** in total. They all run from scratch every time, "
               "in a real browser, on the actual website. Each one is independent.")
    out.append("")
    out.append("- ✅ **Passed** — the website behaved exactly as expected")
    out.append("- ❌ **Failed** — something didn't work. Could be a website bug, a backend bug, or a test bug. The plain-English reason for each is below.")
    out.append("- ⏭️ **Skipped** — the test detected its precondition is missing (e.g. the feature it tests doesn't exist in the website yet) and politely opted out. **Not a failure.**")
    out.append("")

    # ============================================================
    # Section 3 — By feature area
    # ============================================================
    out.append("---")
    out.append("")
    out.append("## By feature area")
    out.append("")
    out.append("Each test file covers one feature area. Status of each:")
    out.append("")

    # Sort: failed areas first, then skipped, then passed
    def _area_status(cls_name):
        tests = classes[cls_name]["tests"]
        n_fail = sum(1 for e in tests if e["fails"] > 0)
        n_skip = sum(1 for e in tests if e["fails"] == 0 and e["skips"] > 0)
        n_pass = sum(1 for e in tests if e["fails"] == 0 and e["skips"] == 0)
        return n_fail, n_skip, n_pass

    sorted_classes = sorted(
        classes.keys(),
        key=lambda c: (-_area_status(c)[0], -_area_status(c)[1], c)
    )

    for cls_name in sorted_classes:
        area = FEATURE_AREAS.get(cls_name, DEFAULT_AREA)
        n_fail, n_skip, n_pass = _area_status(cls_name)
        n_total = n_fail + n_skip + n_pass

        if n_fail == 0 and n_skip == 0:
            icon, status = "✅", f"All {n_pass} tests passed"
        elif n_fail == 0:
            icon, status = "⚠️", f"{n_pass} passed, **{n_skip} skipped** (feature not built yet)"
        elif n_fail == n_total:
            icon, status = "❌", f"**ALL {n_fail} tests in this area failed**"
        else:
            icon, status = "❌", f"{n_pass} passed, **{n_fail} failed**, {n_skip} skipped"

        out.append(f"### {icon} {area['title']}")
        out.append("")
        out.append(f"_{area['explanation']}_")
        out.append("")
        out.append(f"- **Status:** {status}")
        out.append(f"- Test file: `{cls_name}` ({n_total} test{'s' if n_total != 1 else ''})")
        out.append("")

    # ============================================================
    # Section 4 — What broke
    # ============================================================
    out.append("---")
    out.append("")
    out.append(f"## What broke ({len(failed)})")
    out.append("")

    if not failed:
        out.append("_No failures — nothing broke._")
        out.append("")
    else:
        out.append("Every failure below has three pieces of information: "
                   "**what the test was checking**, **why it failed in plain English**, "
                   "and the **technical error** for engineers.")
        out.append("")
        for tid, e in failed:
            cls_name = e["cls"]
            test_name = e["name"]
            area = FEATURE_AREAS.get(cls_name, DEFAULT_AREA)
            human_test = _humanize_test_name(test_name)
            human_error = _humanize_error(e["last_fail_msg"])
            stability = ""
            if n_runs > 1:
                stability = f" _(failed in {e['fails']} of {n_runs} runs)_"
            tech_line = (e["last_fail_msg"] or "").strip().splitlines()
            tech_first = tech_line[0][:240] if tech_line else "(no message)"

            out.append(f"### ❌ {human_test}{stability}")
            out.append("")
            out.append(f"- **Feature area:** {area['title']}")
            out.append(f"- **What this test does:** {human_test} — part of the {area['title']} flow.")
            out.append(f"- **Why it failed (plain English):** {human_error}")
            out.append("")
            out.append(f"<details><summary>Technical detail (for engineers)</summary>")
            out.append("")
            out.append(f"- **Test ID:** `{tid}`")
            out.append(f"- **First line of error:** `{tech_first}`")
            out.append("")
            out.append(f"</details>")
            out.append("")

    # ============================================================
    # Section 5 — What was deferred (skipped)
    # ============================================================
    out.append("---")
    out.append("")
    out.append(f"## What was deferred ({len(skipped)})")
    out.append("")
    out.append("These tests **didn't run on purpose**. The test detected that the feature "
               "it would test doesn't exist in the current website build, and politely "
               "opted out. None of these are failures — they're a signal that the test "
               "exists and is ready to run as soon as the feature is shipped.")
    out.append("")

    if not skipped:
        out.append("_No skipped tests._")
        out.append("")
    else:
        for tid, e in skipped:
            cls_name = e["cls"]
            area = FEATURE_AREAS.get(cls_name, DEFAULT_AREA)
            human_test = _humanize_test_name(e["name"])
            reason = e["last_skip_msg"]
            reason_one_line = re.sub(r"\s+", " ", (reason or "").strip())[:300] \
                              or "(no reason given)"
            out.append(f"### ⏭️ {human_test}")
            out.append("")
            out.append(f"- **Feature area:** {area['title']}")
            out.append(f"- **Why it was deferred:** {reason_one_line}")
            out.append(f"- **What would un-skip it:** Build the missing UI / feature this "
                       "test is waiting for.")
            out.append("")
            out.append(f"<details><summary>Technical detail</summary>")
            out.append("")
            out.append(f"- **Test ID:** `{tid}`")
            out.append("")
            out.append(f"</details>")
            out.append("")

    # ============================================================
    # Section 6 — Full pass list (compact)
    # ============================================================
    out.append("---")
    out.append("")
    out.append(f"## Everything that passed ({len(passed)})")
    out.append("")
    out.append("Grouped by feature area. Names are translated from technical to plain English.")
    out.append("")

    pass_by_class = defaultdict(list)
    for tid, e in passed:
        pass_by_class[e["cls"]].append(_humanize_test_name(e["name"]))

    for cls_name in sorted(pass_by_class.keys()):
        area = FEATURE_AREAS.get(cls_name, DEFAULT_AREA)
        names = pass_by_class[cls_name]
        out.append(f"### {area['title']} ({len(names)} ✅)")
        out.append("")
        for n in names:
            out.append(f"- ✅ {n}")
        out.append("")

    # ============================================================
    # Section 7 — Glossary
    # ============================================================
    out.append("---")
    out.append("")
    out.append("## Glossary (terms used above)")
    out.append("")
    out.append("- **Test** — one automated check, like a tiny robot user that performs a series of clicks and verifies the result.")
    out.append("- **Pass** — the test got the expected result.")
    out.append("- **Fail** — the test got a different result. The reason can be a website bug, a backend bug, or a test bug.")
    out.append("- **Skip** — the test detected its precondition is missing and opted out. Not a failure.")
    out.append("- **Headed run** — the tests run in a visible browser window (so you can watch them). Slow but observable.")
    out.append("- **Backend** — the server-side application that stores data and answers requests from the website.")
    out.append("- **Frontend** — the website itself, what you see in the browser.")
    out.append("- **Cascade** — what happens to 'child' data when the 'parent' is deleted. E.g. delete a tag → does each link keep the tag, lose the tag, or get deleted itself?")
    out.append("- **CRUD** — Create / Read / Update / Delete — the four basic operations on data.")
    out.append("- **XSS** — Cross-Site Scripting — an attack where someone tries to inject malicious code via input fields. Tests verify the website blocks it.")
    out.append("- **Moderator** — a user role with limited admin permissions (can edit links/tags/messages but not environments/domains).")
    out.append("- **Timeout** — how long a test waits before giving up. Default 30 seconds.")
    out.append("- **Selector / Locator** — how the test finds an element on the page (e.g. \"the button with label 'Save'\").")
    out.append("")

    # ---- Write file ----
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    return output_path
