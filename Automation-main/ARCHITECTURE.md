# Zira QA Automation — Architecture Diagrams

This file is a visual map of the codebase. Read it in order — each
diagram builds on the previous one.

---

## 1. The 30-second overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   You type:   python tests/run_multiple.py                          │
│       │                                                             │
│       ▼                                                             │
│   ┌──────────────────────────────────────────────┐                  │
│   │  THE EXECUTOR  (tests/run_multiple.py)       │                  │
│   │  Runs the suite N times (default 5)          │                  │
│   └────────────────────┬─────────────────────────┘                  │
│                        │                                            │
│                        ▼                                            │
│   ┌──────────────────────────────────────────────┐                  │
│   │  114 TESTS in a real Chromium browser        │                  │
│   │  Login, CRUD, Cascades, XSS, Regressions...  │                  │
│   └────────────────────┬─────────────────────────┘                  │
│                        │                                            │
│                        ▼                                            │
│   ┌──────────────────────────────────────────────┐                  │
│   │  4 REPORTS + 1 EMAIL                         │                  │
│   │  • Test_Summary_<TS>.md     (plain English)  │                  │
│   │  • Test_Dashboard_<TS>.html (charts, mobile) │                  │
│   │  • Master_Run_Report_<TS>.md (for engineers) │                  │
│   │  • WhatsApp_Summary_<TS>.txt (for chat)      │                  │
│   │  ✉  Email with dashboard + summary attached  │                  │
│   └──────────────────────────────────────────────┘                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Project folder structure

```
Automation-main/
│
├── .env                       <─ SMTP creds, login creds (gitignored)
├── pytest.ini                 <─ browser/headed config + 'stress' marker
├── requirements.txt
│
├── tests/                     ╔══ THE TEST LAYER ═══════════════════╗
│   │                          ║                                     ║
│   ├── conftest.py            ║  Fixtures + hooks (auth, capture)   ║
│   ├── run_multiple.py        ║  The executor entry point           ║
│   │                          ║                                     ║
│   └── test_*.py (16 files)   ║  114 tests across 16 feature areas  ║
│       ├── test_zira.py                                              ║
│       ├── test_cascade.py                                           ║
│       ├── test_cascade_expanded.py                                  ║
│       ├── test_messages_flows.py                                    ║
│       ├── test_public_homepage.py                                   ║
│       ├── test_regression_bugs.py                                   ║
│       └── ... (etc.)         ╚═════════════════════════════════════╝
│
├── pages/                     ╔══ PAGE OBJECT MODEL ════════════════╗
│   │                          ║                                     ║
│   ├── login_page.py          ║  Login flow (with idempotency)      ║
│   ├── navigation_page.py     ║  Sidebar buttons                    ║
│   ├── domains_page.py        ║  עולמות תוכן CRUD                    ║
│   ├── tags_page.py           ║  תגיות CRUD                          ║
│   ├── messages_page.py       ║  מודעות CRUD + preview popup        ║
│   ├── environments_page.py   ║  סביבות CRUD                         ║
│   └── links_page.py          ║  קישורים CRUD                        ║
│                              ╚═════════════════════════════════════╝
│
├── utils/                     ╔══ REPORT GENERATORS + HELPERS ══════╗
│   │                          ║                                     ║
│   ├── generate_simple_summary.py     <- friendly markdown          ║
│   ├── generate_html_dashboard.py     <- visual dashboard           ║
│   ├── generate_master_report.py      <- engineer diagnostics       ║
│   ├── generate_whatsapp_summary.py   <- chat-friendly text         ║
│   ├── send_email.py                  <- SMTP delivery              ║
│   ├── cleanup_orphans.py             <- orphan-data sweeper        ║
│   └── image_gen.py                   <- PIL-based image factory    ║
│                              ╚═════════════════════════════════════╝
│
├── reports/master/            <─ ALL OUTPUTS land here
│   ├── run_N_junit.xml           (raw pytest junit, N per run)
│   ├── run_N_report.html         (pytest-html per-run report)
│   ├── Test_Summary_<TS>.md
│   ├── Test_Dashboard_<TS>.html
│   ├── Master_Run_Report_<TS>.md
│   └── WhatsApp_Summary_<TS>.txt
│
└── zero_touch_logs/errors/    <─ FAILURE FORENSICS
    ├── <testname>_<TS>.png          (screenshot at failure)
    └── <testname>_<TS>_logs.txt     (console + network errors)
```

---

## 3. The 5 architectural layers

```
        ┌───────────────────────────────────────────────────────┐
        │  L1: ENTRY POINT                                      │
        │       run_multiple.py                                 │
        │       (the orchestrator)                              │
        └───────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌───────────────────────────────────────────────────────┐
        │  L2: FIXTURES + HOOKS                                 │
        │       conftest.py                                     │
        │       • _auth_state_path  (session login)             │
        │       • page              (class browser context)     │
        │       • _capture_on_failure (autouse forensics)       │
        │       • pytest_runtest_makereport (hook)              │
        └───────────────────────────────────────────────────────┘
                              │
                              ▼
        ┌───────────────────────────────────────────────────────┐
        │  L3: TESTS                                            │
        │       tests/test_*.py                                 │
        │       16 files, 114 tests                             │
        └───────────────────────────────────────────────────────┘
                              │
                              ▼  uses
        ┌───────────────────────────────────────────────────────┐
        │  L4: PAGE OBJECT MODEL                                │
        │       pages/*.py                                      │
        │       LoginPage, NavigationPage, DomainsPage, etc.    │
        │       (encapsulates selectors + UI actions)           │
        └───────────────────────────────────────────────────────┘
                              │
                              ▼  produces
        ┌───────────────────────────────────────────────────────┐
        │  L5: REPORTS + EMAIL                                  │
        │       utils/generate_*.py + send_email.py             │
        │       (consume JUnit XMLs, emit 4 report files)       │
        └───────────────────────────────────────────────────────┘
```

---

## 4. Test execution lifecycle (what happens to ONE test)

```
                        pytest discovers test
                                │
                                ▼
                  ╔══════════════════════════════╗
                  ║  pytest_configure (hook)     ║
                  ║  Force UTF-8 stdout          ║
                  ╚══════════════╤═══════════════╝
                                 │
                                 ▼
       ┌─────────────────────────────────────────────────────┐
       │   SESSION-SCOPED FIXTURE (runs ONCE per session)    │
       │                                                     │
       │   _auth_state_path(tmp_path_factory):               │
       │     1. Open real browser                            │
       │     2. Real B2C login (APP_USERNAME / APP_PASSWORD) │
       │     3. context.storage_state(path=auth.json)        │
       │     4. Return JSON path                             │
       │                                                     │
       │   WHY:  Azure B2C rate-limits at ~10 logins/min     │
       │         One real login → reused across all tests    │
       └─────────────────────┬───────────────────────────────┘
                             │
                             ▼
       ┌─────────────────────────────────────────────────────┐
       │   CLASS-SCOPED FIXTURE (per test class)             │
       │                                                     │
       │   page(request, _auth_state_path):                  │
       │     1. browser.new_context(storage_state=auth.json) │
       │        → context already logged in                  │
       │     2. Attach console/pageerror/response listeners  │
       │     3. page._error_log = {} (buckets)               │
       │     4. yield page                                   │
       │     5. teardown: context.close()                    │
       └─────────────────────┬───────────────────────────────┘
                             │
                             ▼
                ┌───────────────────────────┐
                │  test_NN_<name>(self, page) │  ◄── your test runs
                │                           │
                │  uses pages/*.py POMs:    │
                │    LinksPage(page).…      │
                │    NavigationPage(page).… │
                │                           │
                └───────────────┬───────────┘
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
              ▼ pass                              ▼ fail
       ┌──────────────┐              ┌────────────────────────┐
       │  rep_call    │              │  pytest_runtest_make-  │
       │  .failed=F   │              │  report hook stashes   │
       │  Continue.   │              │  rep_call on item      │
       └──────────────┘              └────────────┬───────────┘
                                                  │
                                                  ▼
                                  ┌────────────────────────────────┐
                                  │  AUTOUSE FUNCTION FIXTURE      │
                                  │  _capture_on_failure:          │
                                  │    if rep.failed:              │
                                  │      page.screenshot() → .png  │
                                  │      dump _error_log → .txt    │
                                  │      → zero_touch_logs/errors/ │
                                  └────────────────────────────────┘
```

---

## 5. Multi-run executor flow

```
   python tests/run_multiple.py
            │
            ▼
   ┌─────────────────────┐
   │ run_multiple.main() │
   │ • load .env         │
   │ • mkdir reports/    │
   └──────────┬──────────┘
              │
              ▼
        ┌─────────────────────────────────────────┐
        │   for i in 1..NUM_RUNS:                 │
        │                                         │
        │     ┌─────────────────────────────┐     │
        │     │  _run_once(i, NUM_RUNS):    │     │
        │     │    run_start = now()        │     │
        │     │    subprocess.run([         │     │
        │     │       'python', '-m',       │     │
        │     │       'pytest', './tests/', │     │
        │     │       '--html=run_i.html',  │     │
        │     │       '--junitxml=run_i.xml'│     │
        │     │    ])                       │     │
        │     │    run_end = now()          │     │
        │     │    return {                 │     │
        │     │      run_idx: i,            │     │
        │     │      start: run_start,      │     │
        │     │      end: run_end,          │     │
        │     │      junit_path, html_path  │     │
        │     │    }                        │     │
        │     └─────────────────────────────┘     │
        │                                         │
        │     runs.append(...)                    │
        └──────────────┬──────────────────────────┘
                       │
                       ▼
       ┌─────────────────────────────────────────────────┐
       │  4 REPORT GENERATORS (in sequence)              │
       │                                                 │
       │  generate_master_report(runs, master_path)      │
       │  generate_simple_summary(runs, summary_path)    │
       │  generate_html_dashboard(runs, dashboard_path)  │
       │  generate_whatsapp_summary(runs, whatsapp_path) │
       │                                                 │
       │  All read the SAME `runs` list + JUnit XMLs     │
       └─────────────────────┬───────────────────────────┘
                             │
                             ▼
       ┌─────────────────────────────────────────────────┐
       │  send_run_email(runs, summary, dashboard, ...)  │
       │                                                 │
       │  if EMAIL_FROM/PASS/TO set in .env:             │
       │    SMTP via STARTTLS (smtp.gmail.com:587)       │
       │    Attach: dashboard.html + summary.md→.txt     │
       │  else:                                          │
       │    print "skipping" (no-op, no crash)           │
       └─────────────────────────────────────────────────┘
```

---

## 6. Report generator pipeline (single shape)

```
                          ┌─────────────────────┐
                          │   runs list         │
                          │   [{run_idx,        │
                          │     start, end,     │
                          │     junit_path,     │
                          │     html_path,      │
                          │     exit_code}, …]  │
                          └──────────┬──────────┘
                                     │
            ┌────────────────────────┼──────────────────────────┐
            │                        │                          │
            ▼                        ▼                          ▼
   ┌────────────────┐    ┌─────────────────────┐    ┌──────────────────┐
   │  _parse_junit  │    │  _parse_junit       │    │  _parse_junit    │
   │  (each one)    │    │  (each one)         │    │  (each one)      │
   └────────┬───────┘    └──────────┬──────────┘    └────────┬─────────┘
            │                       │                        │
            │  ┌────────────────────┘                        │
            │  │  ┌──────────────────────────────────────────┘
            ▼  ▼  ▼
   ┌──────────────────────────────────────────────────────────┐
   │  Common data shape used by all generators:               │
   │    tests, passed, failed, skipped, rate, testcases[]     │
   └────┬────────────────────┬──────────────────┬─────────────┘
        │                    │                  │
        ▼                    ▼                  ▼
  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
  │ Simple       │   │ HTML         │   │ Master       │   ┌──────────────┐
  │ Summary      │   │ Dashboard    │   │ Report       │   │ WhatsApp     │
  │              │   │              │   │              │   │ Summary      │
  │ FEATURE_     │   │ • SVG donut  │   │ • Stability  │   │              │
  │   AREAS map  │   │ • KPI tiles  │   │   index      │   │ HEBREW_      │
  │ + human-     │   │ • Hbars      │   │ • Error      │   │   AREA_NAMES │
  │   ized error │   │ • Tab bar    │   │   buckets    │   │ + _build_    │
  │   strings    │   │ • Tooltips   │   │ • Per-run    │   │   status_    │
  │              │   │ • Forensics  │   │   details    │   │   line()     │
  │              │   │ • Mobile CSS │   │ • Truncated  │   │              │
  │              │   │              │   │   logs       │   │              │
  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘   └──────┬───────┘
         │                  │                  │                  │
         ▼                  ▼                  ▼                  ▼
  Test_Summary_      Test_Dashboard_     Master_Run_         WhatsApp_
   <TS>.md            <TS>.html           Report_<TS>.md     Summary_<TS>.txt
```

---

## 7. The 4 reports — who reads what

```
┌────────────────────────────────────────────────────────────────────┐
│                                                                    │
│  👨‍💼 MANAGER / STAKEHOLDER                                          │
│  ──────────────────────                                            │
│         │                                                          │
│         └──▶ 📊 Test_Dashboard_<TS>.html                            │
│                • Donut chart + KPI tiles                           │
│                • Tab per run                                       │
│                • Hover/tap tooltips on tests                       │
│                • Mobile-friendly (≤768px + ≤480px)                 │
│                                                                    │
│                                                                    │
│  👩‍💻 QA TESTER                                                      │
│  ───────────                                                       │
│         │                                                          │
│         └──▶ 📝 Test_Summary_<TS>.md                                │
│                • Plain-English narrative                           │
│                • Translated error messages                         │
│                • Per-area status + glossary                        │
│                                                                    │
│                                                                    │
│  👨‍🔧 DEVELOPER / DEVOPS                                             │
│  ──────────────────                                                │
│         │                                                          │
│         └──▶ 🔬 Master_Run_Report_<TS>.md                           │
│                • Exception-type buckets                            │
│                • Stability index (cross-run)                       │
│                • Full stack traces                                 │
│                • Inline screenshots + log files                    │
│                                                                    │
│                                                                    │
│  💬 TEAM CHAT / WHATSAPP                                            │
│  ──────────────────────                                            │
│         │                                                          │
│         └──▶ 📱 WhatsApp_Summary_<TS>.txt                           │
│                • 10-line emoji-rich Hebrew text                    │
│                • Auto status line                                  │
│                • Copy-paste ready                                  │
│                                                                    │
└────────────────────────────────────────────────────────────────────┘
```

---

## 8. Failure forensics — how it all hooks together

```
  test_xx_doing_something  ────────►  ❌  fails
                                      │
                                      ▼
  ┌──────────────────────────────────────────────────────┐
  │  pytest_runtest_makereport hook (conftest.py)        │
  │  Stashes TestReport on item as item.rep_call         │
  └─────────────────────┬────────────────────────────────┘
                        │
                        ▼
  ┌──────────────────────────────────────────────────────┐
  │  _capture_on_failure  (autouse, runs around test)    │
  │  reads item.rep_call/rep_setup                       │
  │  if .failed:                                         │
  │    page.screenshot(full_page=True)                   │
  │    write page._error_log                             │
  └─────────────────────┬────────────────────────────────┘
                        │
                        ▼
  ┌──────────────────────────────────────────────────────┐
  │  zero_touch_logs/errors/                             │
  │    <test>_<TS>.png                                   │
  │    <test>_<TS>_logs.txt                              │
  └─────────────────────┬────────────────────────────────┘
                        │
        ┌───────────────┼─────────────────┐
        │               │                 │
        ▼               ▼                 ▼
  Master Report    HTML Dashboard    (also linked
  inlines them   embeds as base64    by run-window
  + truncated    + console logs in    matching with
   log content   collapsible details   2s buffer)
```

---

## 9. The fixture choreography (timing diagram)

```
TIME ────────────────────────────────────────────────────────►

session start
│
├─ pytest_configure (UTF-8 stdout)
│
├─ _auth_state_path ──┐
│                     │ ONE real B2C login
│                     │ Save storage_state.json
│                     │ ◄─── reused for ALL tests below
│                     ▼
│
├─ TestClassA ────────► page fixture ───┐
│   │                                   │ new context (with storage_state)
│   ├─ test_01 ───► autouse capture     │
│   ├─ test_02 ───► autouse capture     │
│   └─ test_05 ───► autouse capture     │
│                                       │
│                  page teardown ◄──────┘ context.close()
│
├─ TestClassB ────────► page fixture ───┐
│   │                                   │ FRESH context (with same storage_state)
│   ├─ test_01 ───► autouse capture     │
│   └─ ...                              │
│                  page teardown ◄──────┘
│
└─ session end (storage_state.json discarded with tmp dir)
```

---

## 10. Mobile-friendly CSS layers

```
                       ┌─────────────────────┐
                       │  Base styles        │  applies always
                       │  (dark theme, neon) │
                       └──────────┬──────────┘
                                  │
              ┌───────────────────┴───────────────────┐
              │                                       │
              ▼                                       ▼
   ┌──────────────────────┐               ┌──────────────────────┐
   │ @media               │               │ @media (hover: none) │
   │  (max-width: 768px)  │               │                      │
   │                      │               │ Touch devices:       │
   │ TABLET / PHONE:      │               │  tap-and-hold        │
   │  • Stack KPIs 2-up   │               │  shows tooltip       │
   │  • Stack donut card  │               │  pinned to bottom    │
   │  • HBars → 3 lines   │               │                      │
   │  • Tables wrap       │               └──────────────────────┘
   │  • Smaller fonts     │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │ @media               │
   │  (max-width: 480px)  │
   │                      │
   │ SMALL PHONES:        │
   │  • Tighter padding   │
   │  • Even smaller text │
   │  • Tighter tab bar   │
   └──────────────────────┘
```

---

## 11. End-to-end data flow (one diagram to rule them all)

```
                       ┌─────────────────────┐
                       │   .env              │
                       │   (creds + config)  │
                       └──────────┬──────────┘
                                  │ load
                                  ▼
       ┌────────────────────────────────────────────────────┐
       │   tests/run_multiple.py (executor)                 │
       └────┬──────────────────────────────────────────┬────┘
            │                                          │
            │ for i in 1..NUM_RUNS                     │ after all runs
            ▼                                          │
  ┌─────────────────────────┐                          │
  │ subprocess: pytest      │                          │
  │   └─ conftest.py        │                          │
  │       └─ _auth_state    │                          │
  │       └─ page fixture   │                          │
  │       └─ _capture       │                          │
  │   └─ tests/test_*.py    │                          │
  │       └─ uses POMs      │                          │
  │           pages/*.py    │                          │
  └────────┬────────────────┘                          │
           │                                           │
           ▼ writes                                    │
  ┌─────────────────────────────────────┐              │
  │ reports/master/run_N_junit.xml      │              │
  │ reports/master/run_N_report.html    │              │
  │ zero_touch_logs/errors/*.png        │              │
  │ zero_touch_logs/errors/*_logs.txt   │              │
  └──────────────┬──────────────────────┘              │
                 │                                     │
                 │ all generators read these           │
                 ▼                                     │
       ┌────────────────────────────────────────────┐  │
       │ 4 GENERATORS (utils/generate_*.py)         │◄─┘
       │  • simple_summary  → Test_Summary_<TS>.md  │
       │  • html_dashboard  → Test_Dashboard.html   │
       │  • master_report   → Master_Run_Report.md  │
       │  • whatsapp_sum.   → WhatsApp_Summary.txt  │
       └──────────────┬─────────────────────────────┘
                      │
                      ▼
       ┌────────────────────────────────────────────┐
       │  utils/send_email.py                       │
       │   • Read EMAIL_FROM/PASS/TO from env       │
       │   • Attach summary.md→.txt + dashboard.html│
       │   • SMTP → STARTTLS → inbox                │
       └────────────────────────────────────────────┘
```

---

## 12. Design principles cheat sheet

```
┌──────────────────────────────────────────────────────────────────┐
│                                                                  │
│   ONE LOGIN PER SESSION                                          │
│   ─────────────────────                                          │
│   storage_state preload avoids Azure B2C rate-limit lockout.     │
│                                                                  │
│   PAGE OBJECT MODEL                                              │
│   ─────────────────                                              │
│   Selectors live in one place. Tests speak in business actions.  │
│                                                                  │
│   TESTS CLEAN UP THEIR OWN DATA                                  │
│   ──────────────────────────────                                 │
│   Re-runnable infinitely. No accumulating orphans.               │
│                                                                  │
│   UI ASSERTIONS, NOT API                                         │
│   ───────────────────────                                        │
│   The bug only matters if the user can see it.                   │
│                                                                  │
│   FAILURE FORENSICS AUTO-CAPTURED                                │
│   ────────────────────────────────                               │
│   Every fail = screenshot + console errors. Zero touch required. │
│                                                                  │
│   REPORTS ARE SELF-CONTAINED                                     │
│   ───────────────────────────                                    │
│   HTML works offline. Email-able. No external dependencies.      │
│                                                                  │
│   REGRESSION TESTS FOR DOCUMENTED BUGS                           │
│   ──────────────────────────────────────                         │
│   When a test starts passing again, the bug is fixed.            │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 13. Where to look when something changes

```
WHAT CHANGED                        →  WHERE TO TOUCH
────────────────                        ──────────────

A new feature in the website        →  Create tests/test_<feature>.py
                                       Add page object in pages/ if new surface

A selector changed (button etc.)    →  Update the relevant pages/*.py
                                       Tests don't change

A new test class added              →  Add entry to FEATURE_AREAS in
                                       utils/generate_simple_summary.py
                                       (Hebrew name optional in
                                        utils/generate_whatsapp_summary.py)

A new known bug                     →  Add a method to TestKnownRegressions
                                       in tests/test_regression_bugs.py

DevOps fixed a bug                  →  Nothing! The regression test starts
                                       passing on its own.

Want to disable a test class        →  Rename class:  TestX → _TestX_DISABLED

Want to email a 2nd recipient       →  Add to EMAIL_TO in .env
                                       (comma-separated)

Want to run more/fewer times        →  NUM_RUNS=N python tests/run_multiple.py

Want to include @stress tests       →  PYTEST_EXTRA_ARGS='-m "stress or not stress"'
                                            python tests/run_multiple.py
```

---

## 14. Glossary

```
TERM                       MEANING
────                       ───────

POM                        Page Object Model — selectors live in pages/*.py
storage_state              Browser cookies + localStorage saved as JSON
                           Preloaded so tests don't re-login
JUnit XML                  pytest's standard machine-readable result format
B2C                        Azure Business-to-Customer auth (the login provider)
Fixture                    pytest's way to share setup/teardown across tests
Hook                       pytest's extension point — e.g. makereport
autouse                    A fixture that runs around every test automatically
Headed / Headless          Browser visible / invisible during test
Forensics                  Screenshot + console-error capture on failure
Stress test                Opt-in tests that hammer the same action repeatedly
                           to find rare flakes
```

---

*Last regenerated: alongside the architecture walkthrough.*
*This file is documentation, not code — feel free to edit/extend.*
