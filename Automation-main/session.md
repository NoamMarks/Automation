# session.md — Teach Everyone the Zira QA Automation Project

> A practical tour of this repo. Start here. Read in order. By the end you should be able to run the suite, read the reports, and know where to make any change.

---

## 1. What this project is, in one paragraph

This is the **end-to-end QA automation suite for the Zira admin portal**
(`https://front-zira.dev.orangepeak.net/`). It drives a real Chromium browser
through 114 tests across 16 feature areas, captures forensic artifacts on
every failure, and emits **four** consolidated reports + **one email** so any
audience — manager, QA, developer, WhatsApp group — gets the right view of
the run without anyone hand-massaging output.

It is built on **Playwright + pytest + Page Object Model**. The application
under test is in Hebrew (RTL), uses **Azure B2C** for auth, and is a React +
MUI + styled-components SPA.

---

## 2. The 30-second mental model

```
You run        →  python tests/run_multiple.py
The executor   →  runs the suite N times (default 5) in subprocesses
Each run       →  pytest discovers tests/test_*.py → real Chromium
On failure     →  screenshot + console errors saved automatically
After all runs →  4 reports generated + email sent (if SMTP set)
```

The four reports are deliberately tailored to four different readers:

| Reader | File | Purpose |
| --- | --- | --- |
| Manager / stakeholder | `Test_Dashboard_<TS>.html` | Charts, KPIs, mobile-friendly |
| QA tester | `Test_Summary_<TS>.md` | Plain-English narrative, translated errors |
| Developer / DevOps | `Master_Run_Report_<TS>.md` | Stack traces, stability index, forensics |
| Team chat | `WhatsApp_Summary_<TS>.txt` | 10-line Hebrew, copy-paste ready |

---

## 3. Repo layout

```
Automation-main/
├── .env                           SMTP + login creds (gitignored)
├── pytest.ini                     browser/headed config + 'stress' marker
├── requirements.txt               playwright 1.55, pytest 8.4, Pillow, dotenv...
├── ARCHITECTURE.md                visual deep-dive (14 diagrams)
├── CALL_GRAPH.md                  class/function-level call graph
├── DIAGRAMS_VISUAL.md             Mermaid layered flowchart
│
├── tests/                         L3: 16 test files, 114 tests
│   ├── conftest.py                fixtures + hooks (auth, capture)
│   ├── run_multiple.py            the executor entry point
│   └── test_*.py
│
├── pages/                         L4: Page Object Model
│   ├── login_page.py              with storage_state idempotency
│   ├── navigation_page.py         sidebar buttons
│   ├── domains_page.py            עולמות תוכן CRUD
│   ├── tags_page.py               תגיות CRUD
│   ├── messages_page.py           מודעות CRUD + popup + image upload
│   ├── environments_page.py       סביבות CRUD
│   └── links_page.py              קישורים CRUD + click-count reader
│
├── utils/                         L5: report generators + helpers
│   ├── generate_simple_summary.py     friendly markdown
│   ├── generate_html_dashboard.py     visual dashboard
│   ├── generate_master_report.py      engineer diagnostics
│   ├── generate_whatsapp_summary.py   chat-friendly text
│   ├── send_email.py                  SMTP delivery (Gmail STARTTLS)
│   ├── cleanup_orphans.py             orphan-data sweeper
│   ├── image_gen.py                   PIL-based image factory
│   └── performance.py                 perf-step context manager
│
├── reports/master/                ALL run outputs land here
└── zero_touch_logs/errors/        screenshots + console logs on failure
```

---

## 4. The 5 architectural layers

```
L1  ENTRY POINT          tests/run_multiple.py   (orchestrator)
L2  FIXTURES + HOOKS     tests/conftest.py        (auth, capture, makereport)
L3  TESTS                tests/test_*.py          (16 files, 114 tests)
L4  PAGE OBJECT MODEL    pages/*.py               (selectors + UI actions)
L5  REPORTS + EMAIL      utils/generate_*.py + send_email.py
```

Read [ARCHITECTURE.md](ARCHITECTURE.md) for diagrams of each.

---

## 5. The fixture choreography (this is the magic)

Most people get tripped up by the auth flow. Here's how it works:

```
session start
  └─ _auth_state_path  (session-scoped fixture)
       1. open real browser
       2. real B2C login with APP_USERNAME / APP_PASSWORD
       3. context.storage_state(path=auth.json)
       4. return that JSON path        ◄── reused for ALL tests below

  ├─ TestClassA  ── page fixture ── new context preloaded with storage_state
  │     ├─ test_01 → _capture_on_failure autouse fixture
  │     ├─ test_02 → _capture_on_failure autouse fixture
  │     └─ ...
  │
  ├─ TestClassB  ── page fixture ── fresh context, same storage_state
  │     └─ ...
  └─ session end
```

**Why one session login?** Azure B2C rate-limits to ~10 logins/IP/min. With 16
classes each doing their own login, we'd lock ourselves out on every full
suite run. The session-scoped fixture does it once and every class boots
already authenticated via `storage_state`.

**Idempotency guard.** `LoginPage._is_already_logged_in()` short-circuits
`fill_credentials()` and `click_login()` when the storage state has already
populated the context — so test files written before the optimization
("login → navigate" at the top of every class) still work unchanged.

**Failure forensics.** `_capture_on_failure` is `autouse=True`. It:

1. Clears the page's `_error_log` *before* each test.
2. On failure, saves `<test>_<TS>.png` (full page screenshot) and
   `<test>_<TS>_logs.txt` (console errors, warnings, page exceptions,
   HTTP ≥ 400) to `zero_touch_logs/errors/` — **outside** `artifacts/`
   because pytest-playwright wipes `artifacts/` at session start, which
   would lose every previous run's evidence in multi-run mode.

---

## 6. The page object model — read these to understand selectors

Every UI surface in the app has a class in [pages/](pages/). Three patterns
are worth knowing:

**Hebrew accessible names.** Selectors are by Hebrew label:
```python
self._add_link_btn = page.get_by_role("button", name="הוספת קישור")
self._save_btn     = page.get_by_role("button", name="שמירה")
```

**Styled-component class hashes rotate per build** — match by substring:
```python
_ROW_SELECTOR  = "[class*='SingleLinkstyled__SingleLinkWrapper']"
_NAME_SELECTOR = "[class*='SingleLinkstyled__StyledLinkName']"
```

**MUI Switch quirks.** The real checkbox is hidden under styled spans; we
click the `.MuiSwitch-root` and read the hidden `input[type='checkbox']` for
state. See [pages/links_page.py:48-60](pages/links_page.py#L48-L60).

**The popup-preview backdrop trap** ([pages/messages_page.py:128-190](pages/messages_page.py#L128-L190))
is a great study: MUI's animation-fading backdrop has `aria-hidden='true'`
(so Playwright thinks it's invisible) but still has size and
`pointer-events ≠ none`, so it intercepts every click underneath. The fix is
to poll `getComputedStyle(el).pointerEvents` ourselves and only proceed
when no backdrop is blocking.

---

## 7. The test files — what each one covers

| File | Class | Tests | Covers |
| --- | --- | --: | --- |
| `test_zira.py` | TestPortalClient | 18 | Admin CRUD on every resource type (links, domains, tags, messages, environments) |
| `test_regression_bugs.py` | TestKnownRegressions | 5 | Asserts CORRECT behavior for documented open bugs — fails while bug is open, passes when fixed |
| `test_cascade.py` | TestCascade | 5 | Domain ↔ Link parent-child cleanup |
| `test_cascade_expanded.py` | TestDomainLinkCascade / TestTag* / TestEnvironment* / TestTagMessage* | 20 | All cross-entity cascades (BLOCK / NULLIFY / CASCADE behaviours) |
| `test_messages_flows.py` | TestMessagesFlows | 5 | Popup messages: create with image → preview → public site → toggle active |
| `test_reactivation_flows.py` | TestMessageReactivation | 8 | Active ↔ inactive toggle round-trip |
| `test_public_homepage.py` | TestPublicHomepage | 7 | Guest-facing surface: footer, header date, status badge, carousels, app tabs |
| `test_end_user_flows.py` | TestEndUserFlows | 4 | Search, click-count increment, domain navigation as a visitor |
| `test_inactive_link.py` | TestInactiveLink | 5 | Inactive links must NOT appear on public site |
| `test_admin_grid_controls.py` | TestLinksAdminGrid | 3 | Admin links page search + sort |
| `test_neg_links.py` | TestNegLinks | 7 | Form validation: blank title/URL, no domain, over-length name/desc |
| `test_image_upload.py` | TestImageUpload | 6 | Image upload boundaries (valid / too-large / wrong format) |
| `test_xss_sanitization.py` | TestXSSLink | 8 | Smoke checks: `<svg onload>`, `<img onerror>`, `javascript:` URLs |
| `test_url_append.py` | TestURLAppend | 7 | Environment URL-param append (yes/no) |
| `test_security_routing.py` | TestSecurityRouting | 4 | Moderator role can't reach admin URLs |
| `test_discard.py` | TestDiscard | 7 | Cancel/X-button never accidentally saves or deletes |
| `test_mod_security.py` | _TestModeratorWorkflow_DISABLED | 6 | Disabled (broken `os.getenv` ref, kept intentionally as canary) |
| `test_login_stress.py` | (function) | 1 | `@stress` opt-in: B2C login-form flake detector |

**Naming convention.** Test data uses prefixes + a hex suffix so
[utils/cleanup_orphans.py](utils/cleanup_orphans.py) can sweep up after
crashes:

```
CasLink<hex>   CasDom<hex>   CasTag<hex>   CasMsg<hex>   CasEnv<hex>
TestLink_<hex> TestDomain<hex> Tag<hex5+> Msg_<hex> Env<hex5+>
DiscardLink<hex>  InactLink<hex>  AppendYes<hex>  NegLink<hex>
```

---

## 8. The executor — `tests/run_multiple.py`

The orchestrator. ~200 lines. Does five things:

1. Loads `.env`.
2. Loops `NUM_RUNS` times (default 5; override with env var). Each iteration
   `subprocess.run`s `pytest` with per-run `--junitxml` and `--html` paths
   so the parent process can later aggregate.
3. Records `{run_idx, start, end, exit_code, junit_path, html_path}` for
   each run.
4. Calls the four report generators in sequence, each consuming the same
   `runs` list of dicts + JUnit XMLs.
5. Calls `send_run_email(...)` — no-op if `EMAIL_FROM/PASS/TO` aren't set.

Environment knobs:

```bash
NUM_RUNS=10 python tests/run_multiple.py                 # run the suite 10×
TEST_PATH=./tests/test_cascade.py python tests/run_multiple.py
PYTEST_EXTRA_ARGS='-m "stress or not stress"' python tests/run_multiple.py
HEADLESS=1 python tests/run_multiple.py                  # no visible browser
RECORD_VIDEO=1 python tests/run_multiple.py              # save .webm per class
```

---

## 9. The four report generators — same shape, four audiences

All four consume `runs: list[dict]` and emit a single file:

```
runs ──▶ for each run:
            _parse_junit(junit_path)  →  tests, passed, failed, skipped, cases[]
         ↓
         common shape ─┬─▶ generate_simple_summary    → Test_Summary_<TS>.md
                       ├─▶ generate_html_dashboard    → Test_Dashboard_<TS>.html
                       ├─▶ generate_master_report     → Master_Run_Report_<TS>.md
                       └─▶ generate_whatsapp_summary  → WhatsApp_Summary_<TS>.txt
```

The art is in the **per-audience translation layers**:

- **simple_summary** has a `FEATURE_AREAS` dict that maps each test class to
  a human title + explanation, and `_humanize_error()` that turns
  `TimeoutError: Locator.click...` into *"The test tried to click a button
  and waited 30 seconds for it to become clickable, but the button never
  reacted."*
- **html_dashboard** builds an inline SVG donut chart, KPI tiles, per-test
  tooltips, and mobile-friendly CSS breakpoints at ≤768px and ≤480px.
  Self-contained — no external assets — so it works in email and offline.
- **master_report** matches `zero_touch_logs/errors/*.png` to each run
  by filename timestamp falling inside `[run_start, run_end + 2s]`
  (small buffer to avoid false-matches when runs are back-to-back).
- **whatsapp_summary** uses Hebrew area-name aliases and produces a
  10-line emoji-rich text — designed to be `cat`-printable straight into a
  WhatsApp/Slack chat. The executor echoes it to stdout for you.

---

## 10. Email delivery — [utils/send_email.py](utils/send_email.py)

Reads `EMAIL_FROM`, `EMAIL_PASS` (Gmail App Password, NOT account password),
`EMAIL_TO` (comma-separated for multiple recipients), optional `SMTP_HOST` /
`SMTP_PORT` (defaults Gmail STARTTLS). Attaches the **HTML dashboard** and
the **plain summary** (renamed `.md → .txt` so Gmail/Outlook preview it
inline). If any credential is missing, prints one line and no-ops — the
suite never fails because of email config.

---

## 11. Forensic artifacts on failure

```
test fails
   │
   ▼
pytest_runtest_makereport hook stashes the TestReport on item.rep_call
   │
   ▼
_capture_on_failure autouse fixture detects .failed
   │
   ▼
zero_touch_logs/errors/<test>_<TS>.png         ◄── full-page screenshot
zero_touch_logs/errors/<test>_<TS>_logs.txt    ◄── 4 buckets:
                                                     • Console Errors
                                                     • Console Warnings
                                                     • Page Exceptions
                                                     • Network Failures (HTTP ≥ 400)
```

The four buckets are populated by Playwright event listeners attached in the
`page` fixture **before the first navigation**, so the very first paint's
errors are captured too. Buckets are cleared per-test so the failure dump
is scoped to that single test.

---

## 12. Design principles cheat sheet

- **One login per session.** `storage_state` preload avoids B2C rate-limit.
- **Page Object Model.** Selectors live in `pages/*.py`. Tests speak in
  business actions ("create a link") not selectors.
- **Tests clean up their own data.** Re-runnable infinitely. No orphans
  accumulating in the dev environment.
- **UI assertions, not API.** The bug only matters if the user can see it.
- **Failure forensics auto-captured.** Every fail = screenshot + console
  errors. Zero touch required.
- **Reports are self-contained.** HTML works offline. Email-able. No CDN.
- **Regression tests for documented bugs.** When `test_bug_01_...` starts
  passing, the bug is fixed — no commit message needed.
- **Hex-suffixed test data.** Cleanup regex can scrub orphans without
  matching real production names.

---

## 13. How to do common things

| You want to... | Touch this |
| --- | --- |
| Run the suite once | `pytest -m "not stress"` (or just `pytest`) |
| Run the suite 5× and email reports | `python tests/run_multiple.py` |
| Run headless | `HEADLESS=1 python tests/run_multiple.py` |
| Add a test for a new feature | `tests/test_<feature>.py` + page object if new surface |
| Update a changed selector | `pages/*.py` only — tests don't change |
| Register a new test class in reports | Add to `FEATURE_AREAS` in `utils/generate_simple_summary.py` (Hebrew name in `generate_whatsapp_summary.py` optional) |
| Track a new known bug | Add a method to `TestKnownRegressions` in `tests/test_regression_bugs.py` |
| Disable a class temporarily | Rename `TestX` → `_TestX_DISABLED` (pytest skips it) |
| Run stress tests | `pytest -m stress` |
| Clean up orphan test data | `python utils/cleanup_orphans.py [--dry-run] [--headless]` |
| Email a 2nd recipient | Comma-separate `EMAIL_TO` in `.env` |

---

## 14. Required `.env`

```env
APP_URL=https://front-zira.dev.orangepeak.net/
APP_USERNAME=<B2C admin email>
APP_PASSWORD=<B2C admin password>

EMAIL_FROM=<gmail address>            # optional — no-ops if blank
EMAIL_PASS=<Gmail App Password>       # NOT your account password
EMAIL_TO=<recipient,recipient,...>
SMTP_HOST=smtp.gmail.com              # optional
SMTP_PORT=587                         # optional
```

Generate the Gmail App Password at https://myaccount.google.com/apppasswords.

---

## 15. First-time setup

```bash
python -m venv .venv
. .venv/Scripts/activate            # Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install --with-deps chromium
cp .env.example .env                 # then fill it in
python tests/run_multiple.py
```

Tested on Python 3.13, Windows 10. Headed by default (you'll see Chromium
pop up); pass `HEADLESS=1` for CI.

A note on Windows: `conftest.py` and `run_multiple.py` both reconfigure
`stdout`/`stderr` to UTF-8 at startup. The default `cp1255` Windows console
codec mangles Hebrew + emoji and crashes session teardown — this is why.

---

## 16. Glossary

| Term | Meaning |
| --- | --- |
| POM | Page Object Model — selectors live in `pages/*.py` |
| storage_state | Browser cookies + localStorage saved as JSON; preloaded so tests don't re-login |
| JUnit XML | pytest's standard machine-readable result format; consumed by every report generator |
| B2C | Azure Business-to-Customer auth (the login provider) |
| Fixture | pytest's way to share setup/teardown across tests |
| Hook | pytest's extension point (e.g. `pytest_runtest_makereport`) |
| autouse | Fixture that runs around every test automatically |
| Headed / Headless | Browser visible / invisible during test |
| Forensics | Screenshot + console-error capture on failure |
| Stress test | Opt-in tests (`@pytest.mark.stress`) hammering one action to find flakes |
| Cascade | What happens to child data when the parent is deleted (BLOCK / NULLIFY / CASCADE) |

---

## 17. Where to read next

- [ARCHITECTURE.md](ARCHITECTURE.md) — 14 diagrams covering folder structure, fixture timing, report pipeline, mobile CSS layers, end-to-end data flow
- [CALL_GRAPH.md](CALL_GRAPH.md) — every class, every method, what calls what
- [DIAGRAMS_VISUAL.md](DIAGRAMS_VISUAL.md) — Mermaid layered flowchart and sequence diagrams (paste into draw.io)
- [tests/conftest.py](tests/conftest.py) — read this once; it's the spine of the suite
- [tests/run_multiple.py](tests/run_multiple.py) — the orchestrator, ~200 lines, very readable

*Last updated alongside the architecture walkthrough.*
