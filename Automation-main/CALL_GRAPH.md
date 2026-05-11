# Class & Function Call Graph

Every class, every function, and what calls what. Read top-to-bottom — it
follows the runtime order: entry point → fixtures → tests → page objects
→ report generators → email.

Notation:
```
  ClassName / file.py
  ├── public_method()              ◄── what calls it
  │     → calls another_method()    ◄── what it calls
  └── _private_helper()
```

---

## 0. Top-level call graph

```
┌──────────────────────────────────────────────────────────────────────┐
│                                                                      │
│  python tests/run_multiple.py                                        │
│      │                                                               │
│      ▼                                                               │
│  ┌────────────────────────────────────────────┐                      │
│  │ run_multiple.main()                        │                      │
│  └─┬──────────────────────────────────────────┘                      │
│    │                                                                 │
│    │ for each run i:                                                 │
│    └─▶ _run_once(i, N) ──▶ subprocess: pytest                        │
│                                  │                                   │
│                                  ▼                                   │
│       ┌──────────────────────────────────────────────┐               │
│       │ pytest discovers tests/test_*.py             │               │
│       │                                              │               │
│       │  conftest.pytest_configure (hook)            │               │
│       │  conftest._auth_state_path (session fixture) │               │
│       │       │                                      │               │
│       │       └─▶ LoginPage.fill_credentials()       │               │
│       │           LoginPage.click_login()            │               │
│       │           LoginPage.wait_for_dashboard()     │               │
│       │           context.storage_state(path=...)    │               │
│       │                                              │               │
│       │  conftest.page (class fixture)               │               │
│       │       └─▶ new browser context w/ storage     │               │
│       │           attach console/pageerror listeners │               │
│       │                                              │               │
│       │  conftest.pytest_runtest_makereport (hook)   │               │
│       │       └─▶ stash item.rep_<phase>             │               │
│       │                                              │               │
│       │  conftest._capture_on_failure (autouse)      │               │
│       │       └─▶ page.screenshot() + log dump       │               │
│       │                                              │               │
│       │  TestClass.test_NN()                         │               │
│       │       └─▶ uses pages/*.py POMs               │               │
│       └──────────────────────────────────────────────┘               │
│    after all runs:                                                   │
│      ├─▶ generate_master_report(runs, ...)                           │
│      ├─▶ generate_simple_summary(runs, ...)                          │
│      ├─▶ generate_html_dashboard(runs, ...)                          │
│      ├─▶ generate_whatsapp_summary(runs, ...)                        │
│      └─▶ send_run_email(runs, summary, dashboard, ...)               │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 1. The executor — `tests/run_multiple.py`

```
run_multiple.py  (no classes — script)
  │
  ├── module-level constants & setup
  │     load_dotenv(.env)
  │     NUM_RUNS, TEST_PATH, EXTRA_PYTEST_ARGS, MASTER_REPORTS_DIR
  │
  ├── _run_once(run_idx, total)              ◄── called by main()
  │     ├── subprocess.run([python, -m, pytest, ...])
  │     └── returns dict {run_idx, start, end, exit_code,
  │                       junit_path, html_path}
  │
  └── main()                                  ◄── the entry point
        ├── for i in 1..NUM_RUNS:
        │     └── _run_once(i, NUM_RUNS)
        ├── generate_master_report(runs, master_path)
        ├── generate_simple_summary(runs, summary_path)
        ├── generate_html_dashboard(runs, dashboard_path)
        ├── generate_whatsapp_summary(runs, whatsapp_path)
        └── send_run_email(runs, summary_path,
                           dashboard_path, master_path)
```

---

## 2. The connective tissue — `tests/conftest.py`

```
conftest.py  (no classes — fixtures + hooks)
  │
  ├── pytest_configure(config)               ◄── pytest calls this once
  │     └── reconfigure stdout to UTF-8
  │
  ├── pytest_runtest_makereport(item, call)  ◄── pytest calls per phase
  │     └── stash TestReport on item as
  │         item.rep_setup / item.rep_call / item.rep_teardown
  │
  ├── _auth_state_path(tmp_path_factory)     ◄── session-scoped fixture
  │     │  (runs ONCE per pytest session)
  │     ├── playwright launch + new_context + new_page
  │     ├── LoginPage(page).navigate()
  │     ├── LoginPage(page).fill_credentials()
  │     ├── LoginPage(page).click_login()
  │     ├── LoginPage(page).wait_for_dashboard()
  │     ├── context.storage_state(path=auth_state.json)
  │     └── return auth_state.json path
  │
  ├── page(request, _auth_state_path)        ◄── class-scoped fixture
  │     │  (runs per test class)
  │     ├── browser.new_context(storage_state=_auth_state_path)
  │     ├── page = context.new_page()
  │     ├── page._error_log = {console_errors, warnings,
  │     │                      page_exceptions, network_failures}
  │     ├── attach: on("console"), on("pageerror"), on("response")
  │     ├── yield page              ◄── tests receive this
  │     └── context.close()         ◄── teardown
  │
  └── _capture_on_failure(request, page)     ◄── autouse function-scoped
        │  (runs around every test)
        ├── yield (let test execute)
        ├── if item.rep_call.failed or item.rep_setup.failed:
        │     ├── page.screenshot(path=zero_touch_logs/errors/<test>_<ts>.png)
        │     └── write page._error_log → ..._logs.txt
        └── (graceful — never raises on cleanup)
```

---

## 3. Test classes — `tests/test_*.py`

All test classes share the same call pattern:

```
TestClass(self, page)        ◄── conftest's `page` fixture
  │
  ├── test_01_login(page)
  │     └── LoginPage(page).fill_credentials/click_login/wait_for_dashboard
  │
  ├── test_NN_<action>(page, shared_class_data)
  │     ├── NavigationPage(page).go_to_<section>()
  │     ├── <Section>Page(page).<action>()
  │     └── assert ...
  │
  └── test_summary(shared_class_data)
        └── print collected state
```

### Specific classes and what they use

```
TestPortalClient                          (tests/test_zira.py)
  └── uses: LoginPage, NavigationPage,
            DomainsPage, TagsPage, MessagesPage,
            EnvironmentsPage, LinksPage

TestCascade                               (tests/test_cascade.py)
  └── uses: LoginPage, NavigationPage,
            DomainsPage, LinksPage

TestDomainLinkCascade                     (tests/test_cascade_expanded.py)
TestTagLinkCascade                        (same file)
TestTagMessageCascade                     (same file)
TestEnvironmentLinkCascade                (same file)
  └── all use: LoginPage, NavigationPage,
               DomainsPage, TagsPage, MessagesPage,
               EnvironmentsPage, LinksPage
               + image_gen.make_png_bytes() for messages

TestMessagesFlows                         (tests/test_messages_flows.py)
TestMessageReactivation                   (tests/test_reactivation_flows.py)
  └── uses: LoginPage, NavigationPage, MessagesPage,
            image_gen.make_png_bytes()

TestImageUpload                           (tests/test_image_upload.py)
  └── uses: LoginPage, NavigationPage, MessagesPage,
            image_gen.make_png_bytes,
            image_gen.make_text_file_bytes

TestInactiveLink                          (tests/test_inactive_link.py)
TestNegLinks                              (tests/test_neg_links.py)
TestXSSLink                               (tests/test_xss_sanitization.py)
TestURLAppend                             (tests/test_url_append.py)
TestDiscard                               (tests/test_discard.py)
  └── all use: LoginPage, NavigationPage, LinksPage,
               EnvironmentsPage (URLAppend only)

TestLinksAdminGrid                        (tests/test_admin_grid_controls.py)
  └── uses: LoginPage, NavigationPage, LinksPage

TestEndUserFlows                          (tests/test_end_user_flows.py)
  └── uses: LoginPage, NavigationPage, LinksPage, DomainsPage

TestPublicHomepage                        (tests/test_public_homepage.py)
  └── uses: a separate `public_browser` fixture (no storage_state)
            to test the public-facing site without admin auth

TestKnownRegressions                      (tests/test_regression_bugs.py)
  └── uses: LoginPage, NavigationPage,
            EnvironmentsPage, MessagesPage
  └── helpers: _short_id() — generates unique test-data suffixes

(disabled — not collected)
_TestModeratorWorkflow_DISABLED           (tests/test_mod_security.py)
_TestSecurityRouting_DISABLED             (tests/test_security_routing.py)
```

---

## 4. Page Object Model — `pages/*.py`

### `LoginPage` — `pages/login_page.py`

```
LoginPage(page)
  │
  ├── __init__(page)
  │     └── locators: _login_link, _username_input, _password_input,
  │                   _login_button, _post_login_indicator
  │
  ├── navigate()                        ◄── conftest._auth_state_path
  │     └── page.goto(APP_URL)
  │
  ├── _is_already_logged_in(wait_ms=1500)
  │     └── page.get_by_text("שלום מנהלן ראשי").wait_for(visible)
  │
  ├── fill_credentials()                ◄── tests, conftest
  │     ├── if _is_already_logged_in(): return  ← idempotency guard
  │     ├── _login_link.click()
  │     ├── #pretty-username.wait_for(visible)
  │     ├── #pretty-username.fill(APP_USERNAME)
  │     └── #pretty-password.fill(APP_PASSWORD)
  │
  ├── click_login()                     ◄── tests, conftest
  │     ├── if _is_already_logged_in(): return
  │     └── button.button-submit.click()
  │
  ├── wait_for_dashboard(timeout=15000, attempts=3)  ◄── tests, conftest
  │     └── retry-loop (up to `attempts` times):
  │           user_profile.click()
  │           menu.wait_for(visible)
  │           menu.click()
  │           _post_login_indicator.wait_for(visible)
  │
  └── login()                           ◄── public convenience
        ├── navigate()
        ├── fill_credentials()
        └── click_login()
```

### `NavigationPage` — `pages/navigation_page.py`

```
NavigationPage(page)
  │
  ├── __init__(page)
  │     └── locators per sidebar button
  │
  ├── go_to_content_worlds()            ◄── any test that creates/edits domains
  ├── go_to_tags()                      ◄── tag tests
  ├── go_to_messages()                  ◄── message tests
  ├── go_to_environments()              ◄── env tests
  └── go_to_links()                     ◄── link tests
```

### Resource page objects — same shape

```
DomainsPage / TagsPage / EnvironmentsPage / LinksPage / MessagesPage
  │
  ├── __init__(page)
  │     └── locators: _add_btn, _name_input, _save_btn, _confirm_btn,
  │                   _delete_confirm_btn, ROW_SELECTOR, NAME_SELECTOR
  │
  ├── open_add_<X>_dialog()
  ├── fill_<X>_form(name, ...)
  ├── click_save_and_confirm()
  ├── click_delete_and_confirm()
  ├── click_edit_on_row(name)
  ├── click_delete_on_row(name)
  ├── fill_edit_<X>_name(new_name)
  ├── verify_<X>_visible(name)
  ├── verify_<X>_not_attached(name)
  │
  └── high-level wrappers:
        create_<X>(...)
        update_<X>(old_name, new_name)
        delete_<X>(name)
```

### `MessagesPage` — extras unique to this POM

```
MessagesPage(page)  (additional members beyond the common shape)
  │
  ├── select_type(type_name)            ◄── 'popup' / 'homepage' / 'both'
  │     └── input[value=type_name].check()
  │
  ├── upload_image(file_name, buffer, mime_type)  ◄── image_gen output
  │     └── _file_input.set_input_files([{name, mimeType, buffer}])
  │
  ├── get_status_checked()
  │     └── _status_switch_input.is_checked()
  │
  ├── toggle_status()                   ◄── active/inactive switch
  │     ├── _status_switch_root.click()
  │     └── returns (before, after)
  │
  ├── click_preview()                   ◄── opens "תצוגה מקדימה" popup
  │     └── _preview_btn.click()
  │
  ├── _wait_backdrop_clear()            ◄── used by click_save_and_confirm
  │     └── poll backdrop pointer-events until clear
  │
  └── create_popup_message(name, desc, image_buffer, image_name)
        ├── open_add_message_dialog()
        ├── fill_message_form(name, desc)
        ├── select_type("popup")
        └── upload_image(image_name, image_buffer)
```

### `LinksPage` — extras unique to links

```
LinksPage(page)  (additional members)
  │
  ├── select_combobox_options(combobox_index, count)
  │     └── used to pick domains/tags/envs in the link form
  │
  ├── select_option_by_name(name, combobox_index)
  │     └── pick a specific named option in a combobox
  │
  ├── set_url_append(append: bool)
  │     └── click כן / לא radio
  │
  ├── toggle_active_off()
  │     └── flip the active-status switch
  │
  └── get_click_count(link_name)
        └── opens public homepage, reads visit count from card
```

---

## 5. Report generators — `utils/*.py`

All four read JUnit XMLs and write one output file each. They share the
same input shape (the `runs` list) but never call each other.

### `utils/generate_simple_summary.py`

```
generate_simple_summary(runs, output_path)         ◄── called by run_multiple.main()
  │
  ├── FEATURE_AREAS dict
  │     also imported by → generate_html_dashboard.py
  │
  ├── _parse_junit(junit_path)
  │     └── returns list of testcase dicts
  │
  ├── _humanize_error(msg)
  │     └── translates raw exception → plain English sentence
  │
  ├── _humanize_test_name(test_name)
  │     └── 'test_02_create_link' → 'Create link'
  │
  ├── _short_id(classname, name)
  │     └── 'ClassName::method_name'
  │
  ├── _fmt_duration(seconds)
  │     └── e.g. '5 minutes 30 seconds'
  │
  └── builds 7-section markdown:
        Headline → What does this mean → By feature area →
        What broke → What was deferred → Everything passed → Glossary
```

### `utils/generate_html_dashboard.py`

```
generate_html_dashboard(runs, output_path)         ◄── called by run_multiple.main()
  │
  ├── imports FEATURE_AREAS, DEFAULT_AREA from generate_simple_summary
  ├── _CSS  (module-level constant string, includes mobile media queries)
  ├── _TAB_SWITCHER_JS  (module-level constant string)
  │
  ├── _parse_junit(junit_path)
  ├── _short_id(classname, name)
  ├── _error_bucket(msg)
  ├── _fmt_duration(seconds)
  │
  ├── _collect_test_docstrings(tests_dir=_TESTS_DIR)
  │     └── uses ast to extract docstrings from every test_*.py
  │     └── powers hover/tap tooltips
  │
  ├── _parse_artifact_ts(filename)
  │     └── parses 'YYYYMMDD_HHMMSS' from a filename
  │
  ├── _collect_artifacts_for_runs(runs, errors_dir)
  │     └── uses _parse_artifact_ts to match screenshots/logs
  │         to each run's [start, end+2s] window
  │
  ├── _img_data_url(path)
  │     └── reads PNG → base64-encoded data: URL
  │
  ├── _read_log_file(path, max_chars=8000)
  │     └── reads + truncates console log
  │
  ├── _svg_donut(passed, failed, skipped)
  │     └── hand-rendered SVG donut chart
  │
  ├── _hbar(label, value, total, color, width=320)
  │     └── HTML for one horizontal-bar row
  │
  ├── _build_view_html(runs_subset, tip_for)
  │     ├── calls _parse_junit, _svg_donut, _hbar
  │     ├── calls _collect_artifacts_for_runs(runs_subset)
  │     ├── calls _img_data_url and _read_log_file for forensics
  │     ├── uses tip_for closure for tooltips
  │     └── returns HTML parts list (status banner → full grid)
  │
  ├── _render_trend_table(runs)
  │     └── per-run trend table (always shows ALL runs)
  │
  ├── _render_tab_bar(runs)
  │     └── tab bar: "All runs" + one per run
  │
  └── orchestration:
        docstrings = _collect_test_docstrings()
        tip_for = closure over docstrings + FEATURE_AREAS
        for view in (all, run_1, run_2, ...):
            _build_view_html(view_subset, tip_for)
        embed _CSS, _TAB_SWITCHER_JS
        write file
```

### `utils/generate_master_report.py`

```
generate_master_report(runs, output_path)          ◄── called by run_multiple.main()
  │
  ├── _parse_junit(junit_path)
  │     └── uses _testcase_dict() per testcase
  │
  ├── _testcase_dict(tc)
  │     └── extract {classname, name, time, failed, skipped, msg}
  │
  ├── _parse_artifact_ts(filename)
  │     └── same as dashboard's version
  │
  ├── _find_artifacts_for_run(errors_dir, run_start, run_end, buffer_sec=2)
  │     └── window-matches screenshots + logs to ONE run
  │
  ├── _rel(target, from_path)
  │     └── compute relative path for links in the markdown
  │
  ├── _error_key(msg)
  │     └── reduce error msg to exception-type bucket
  │         (e.g. 'TimeoutError', 'AssertionError')
  │
  ├── _build_failure_analysis(parsed)
  │     └── uses _error_key to group failures across runs
  │     └── detects class-wide failures (≥80% of class failed)
  │
  └── orchestration:
        for run in runs: _parse_junit(...)
        _build_failure_analysis(parsed)
        stability index, per-run details
        per failed test: _find_artifacts_for_run + inline screenshots
        write markdown
```

### `utils/generate_whatsapp_summary.py`

```
generate_whatsapp_summary(runs, output_path)       ◄── called by run_multiple.main()
  │
  ├── HEBREW_AREA_NAMES dict
  │     └── used by _build_status_line
  │
  ├── _parse_junit(junit_path)
  │     └── returns {tests, passed, failed, skipped, rate, cases[]}
  │
  ├── _build_status_line(parsed_runs)
  │     ├── tally fails per class across runs
  │     ├── pick one of 4 sentences:
  │     │     ✅ everything passed
  │     │     ⚠️ recurring failures in <X>   (50%+ fails, in 2+ runs)
  │     │     ⚠️ mainly in <X>                (50%+ fails, single run)
  │     │     ⚠️ scattered across components
  │     └── uses HEBREW_AREA_NAMES to display the top class
  │
  └── builds 10-line plain text:
        header → date → time → runs list → status → footer
```

### `utils/send_email.py`

```
send_run_email(runs, summary_path,                 ◄── called by run_multiple.main()
               dashboard_path, master_path)
  │
  ├── _parse_junit_summary(junit_path)
  │     └── {tests, passed, failed, skipped, duration}
  │
  ├── _aggregate(runs)
  │     └── sum counts across all runs
  │
  ├── _fmt_duration(seconds)
  │
  ├── _build_html_body(runs, agg, summary_path, dashboard_path)
  │     └── HTML email body with KPI table
  │     └── renames summary_path '.md' → '.txt' in the body text
  │
  └── send_run_email orchestration:
        ├── read EMAIL_FROM, EMAIL_PASS, EMAIL_TO from env
        ├── if missing: print "skipping" and return None
        ├── build subject "[Zira QA] N FAIL · X/Y (Z%) · M runs · DD-MMM HH:MM"
        ├── EmailMessage:
        │     set plain-text body
        │     add HTML alternative (_build_html_body)
        │     attach dashboard.html
        │     attach summary.md (renamed to .txt for inline preview)
        └── smtplib.SMTP + STARTTLS + login + send_message
```

---

## 6. Helper modules — `utils/*.py`

### `utils/image_gen.py`

```
make_png_bytes(size_mb=0.3)                ◄── called by test_image_upload,
  │                                              test_messages_flows,
  └── PIL.Image.new(...).save(BytesIO)         test_reactivation_flows,
        returns the bytes                      test_cascade_expanded
                                                   (for popup-message tests)

make_text_file_bytes()                     ◄── called by test_image_upload
  └── returns plain text bytes               (used as a "wrong format" file)
```

### `utils/cleanup_orphans.py`

```
(standalone CLI — not imported by any test)
  │
  └── Run manually: python utils/cleanup_orphans.py
        Sweeps test prefixes (CasLink*, RegBug*, etc.)
        Deletes orphan envs, links, messages, tags
```

### `utils/performance.py`

```
(used inside disabled test_mod_security.py only)
  │
  └── performance_step(step_name, extras, limit_ms)
        Context manager for timing UI steps with HTML output
```

### `utils/email_summary.py`

```
(used by CI workflow only — extracts a digest from
 Master Run Report for the dawidd6/action-send-mail step)
```

---

## 7. Cross-cutting dependencies

This is the only "lateral" connection in the codebase — `FEATURE_AREAS`
is defined once and reused by the HTML dashboard so the friendly-summary
and the dashboard agree on feature-area names:

```
                  generate_simple_summary.py
                            │
                            │  FEATURE_AREAS, DEFAULT_AREA
                            ▼
                  generate_html_dashboard.py
                            │  imports them via:
                            │  from utils.generate_simple_summary
                            │       import FEATURE_AREAS, DEFAULT_AREA
                            ▼
                  (uses them in _build_view_html
                   for the "Per feature area" bars
                   and the tip_for closure)
```

Everything else is hierarchical with **no circular imports**:

```
run_multiple → conftest → tests → pages → playwright
                                       └─→ utils.image_gen → PIL

run_multiple → utils.generate_master_report
            → utils.generate_simple_summary
            → utils.generate_html_dashboard ───► generate_simple_summary
            → utils.generate_whatsapp_summary
            → utils.send_email
```

---

## 8. Class & function index — where each lives

```
SYMBOL                                        FILE                                    KIND
──────                                        ────                                    ────

run_multiple.py
  _run_once                                   tests/run_multiple.py                   function
  main                                        tests/run_multiple.py                   function

conftest.py
  pytest_configure                            tests/conftest.py                       hook
  pytest_runtest_makereport                   tests/conftest.py                       hook
  _auth_state_path                            tests/conftest.py                       session fixture
  page                                        tests/conftest.py                       class fixture
  _capture_on_failure                         tests/conftest.py                       autouse fixture

Tests (classes)
  TestPortalClient                            tests/test_zira.py                      class
  TestCascade                                 tests/test_cascade.py                   class
  TestDomainLinkCascade                       tests/test_cascade_expanded.py          class
  TestTagLinkCascade                          tests/test_cascade_expanded.py          class
  TestTagMessageCascade                       tests/test_cascade_expanded.py          class
  TestEnvironmentLinkCascade                  tests/test_cascade_expanded.py          class
  TestDiscard                                 tests/test_discard.py                   class
  TestEndUserFlows                            tests/test_end_user_flows.py            class
  TestImageUpload                             tests/test_image_upload.py              class
  TestInactiveLink                            tests/test_inactive_link.py             class
  TestLinksAdminGrid                          tests/test_admin_grid_controls.py       class
  TestMessagesFlows                           tests/test_messages_flows.py            class
  TestMessageReactivation                     tests/test_reactivation_flows.py        class
  TestNegLinks                                tests/test_neg_links.py                 class
  TestPublicHomepage                          tests/test_public_homepage.py           class
  TestKnownRegressions                        tests/test_regression_bugs.py           class
  TestURLAppend                               tests/test_url_append.py                class
  TestXSSLink                                 tests/test_xss_sanitization.py          class
  _TestModeratorWorkflow_DISABLED             tests/test_mod_security.py              class (disabled)
  _TestSecurityRouting_DISABLED               tests/test_security_routing.py          class (disabled)
  test_login_form_renders_on_click            tests/test_login_stress.py              @pytest.mark.stress

Pages (classes)
  LoginPage                                   pages/login_page.py                     class
  NavigationPage                              pages/navigation_page.py                class
  DomainsPage                                 pages/domains_page.py                   class
  TagsPage                                    pages/tags_page.py                      class
  MessagesPage                                pages/messages_page.py                  class
  EnvironmentsPage                            pages/environments_page.py              class
  LinksPage                                   pages/links_page.py                     class

Utils (functions)
  generate_simple_summary                     utils/generate_simple_summary.py        public fn
  _humanize_error / _humanize_test_name       utils/generate_simple_summary.py        helpers
  _parse_junit / _short_id / _fmt_duration    utils/generate_simple_summary.py        helpers
  FEATURE_AREAS, DEFAULT_AREA                 utils/generate_simple_summary.py        constants

  generate_html_dashboard                     utils/generate_html_dashboard.py        public fn
  _build_view_html                            utils/generate_html_dashboard.py        helper
  _render_trend_table / _render_tab_bar       utils/generate_html_dashboard.py        helpers
  _collect_test_docstrings                    utils/generate_html_dashboard.py        helper
  _collect_artifacts_for_runs                 utils/generate_html_dashboard.py        helper
  _svg_donut / _hbar                          utils/generate_html_dashboard.py        helpers
  _img_data_url / _read_log_file              utils/generate_html_dashboard.py        helpers
  _parse_junit / _short_id / _error_bucket    utils/generate_html_dashboard.py        helpers
  _parse_artifact_ts / _fmt_duration          utils/generate_html_dashboard.py        helpers
  _CSS / _TAB_SWITCHER_JS                     utils/generate_html_dashboard.py        constants

  generate_master_report                      utils/generate_master_report.py         public fn
  _build_failure_analysis                     utils/generate_master_report.py         helper
  _find_artifacts_for_run                     utils/generate_master_report.py         helper
  _parse_junit / _testcase_dict / _rel        utils/generate_master_report.py         helpers
  _error_key / _parse_artifact_ts             utils/generate_master_report.py         helpers

  generate_whatsapp_summary                   utils/generate_whatsapp_summary.py      public fn
  _build_status_line                          utils/generate_whatsapp_summary.py      helper
  _parse_junit                                utils/generate_whatsapp_summary.py      helper
  HEBREW_AREA_NAMES                           utils/generate_whatsapp_summary.py      constant

  send_run_email                              utils/send_email.py                     public fn
  _build_html_body                            utils/send_email.py                     helper
  _aggregate / _parse_junit_summary           utils/send_email.py                     helpers
  _fmt_duration                               utils/send_email.py                     helper

  make_png_bytes                              utils/image_gen.py                      public fn
  make_text_file_bytes                        utils/image_gen.py                      public fn

  (standalone CLI)                            utils/cleanup_orphans.py                script
  (CI helper)                                 utils/email_summary.py                  script
  (decorators)                                utils/performance.py                    library
```

---

## 9. Putting it all together — three real example flows

### Example A: "Run the suite once"

```
$ python tests/run_multiple.py

run_multiple.main()
  └─ _run_once(1, 1)
      └─ subprocess: pytest ./tests/
          ├─ pytest_configure (UTF-8 stdout)
          ├─ _auth_state_path  (session)
          │   └─ LoginPage.navigate, fill_credentials, click_login, wait_for_dashboard
          │       (with retry inside wait_for_dashboard)
          │   └─ context.storage_state(path=auth.json)
          │
          ├─ for each test class:
          │   ├─ page fixture (class): browser context w/ storage_state
          │   │
          │   ├─ For each test method:
          │   │   ├─ pytest_runtest_makereport stashes rep_<phase>
          │   │   ├─ _capture_on_failure wraps test
          │   │   │
          │   │   └─ test_body uses POMs:
          │   │       LoginPage.<methods>  (idempotent — no-ops)
          │   │       NavigationPage.go_to_<section>
          │   │       <Section>Page.create_<X> / save / delete
          │   │
          │   │   if failed:
          │   │       page.screenshot → zero_touch_logs/errors/*.png
          │   │       dump _error_log → *_logs.txt
          │   │
          │   └─ page teardown: context.close()
          │
          └─ pytest exits, junit.xml + html report written

After loop:
  ├─ generate_master_report(runs, ...)
  │   ├─ _parse_junit per run
  │   ├─ _build_failure_analysis
  │   ├─ for each failure: _find_artifacts_for_run
  │   └─ writes Master_Run_Report_<TS>.md
  │
  ├─ generate_simple_summary(runs, ...)
  │   ├─ _parse_junit per run
  │   ├─ _humanize_error / _humanize_test_name
  │   └─ writes Test_Summary_<TS>.md
  │
  ├─ generate_html_dashboard(runs, ...)
  │   ├─ _collect_test_docstrings (ast parse of test files)
  │   ├─ _render_trend_table / _render_tab_bar
  │   ├─ for each view: _build_view_html
  │   │   ├─ _svg_donut, _hbar
  │   │   └─ _collect_artifacts_for_runs + _img_data_url
  │   └─ writes Test_Dashboard_<TS>.html
  │
  ├─ generate_whatsapp_summary(runs, ...)
  │   ├─ _parse_junit per run
  │   ├─ _build_status_line (uses HEBREW_AREA_NAMES)
  │   └─ writes WhatsApp_Summary_<TS>.txt
  │
  └─ send_run_email(runs, summary, dashboard, master)
      ├─ _aggregate runs
      ├─ _build_html_body
      ├─ attach dashboard.html + summary.md→.txt
      └─ smtplib.SMTP STARTTLS send
```

### Example B: "A test creates a message"

```
TestMessagesFlows.test_02_create_popup_with_image(self, page)
  │
  ├─ NavigationPage(page).go_to_messages()
  │   └─ self._messages_btn.click()
  │
  ├─ msgs = MessagesPage(page)
  │
  ├─ buffer = image_gen.make_png_bytes(0.3)   ← from utils/image_gen.py
  │   └─ PIL.Image.new(...) → BytesIO
  │
  ├─ msgs.create_popup_message(name, desc, buffer, "test.png")
  │   ├─ open_add_message_dialog()  (clicks הוספת מודעה)
  │   ├─ fill_message_form(name, desc)
  │   ├─ select_type("popup")
  │   └─ upload_image("test.png", buffer)
  │       └─ _file_input.set_input_files([{name, mimeType, buffer}])
  │
  ├─ msgs.click_save_and_confirm()
  │   ├─ _save_btn.click()
  │   ├─ poll for 'אישור' or 'הבנתי' button + click
  │   └─ _wait_backdrop_clear()  ← waits for MUI animations to settle
  │
  └─ msgs.verify_message_visible(name)
      └─ self.page.locator(TITLE_SELECTOR, has_text=name) → expect visible
```

### Example C: "Failure forensics happens"

```
test_xx fails
  │
  ▼
pytest_runtest_makereport(item, call)        ◄── conftest hook
  └─ item.rep_call = TestReport(passed=False, longrepr=...)
  │
  ▼
_capture_on_failure(request, page)           ◄── conftest autouse
  if item.rep_call.failed:
    │
    ├─ page.screenshot(path=zero_touch_logs/errors/test_xx_<TS>.png)
    └─ open(..._logs.txt, 'w') writes page._error_log
       (console_errors, warnings, page_exceptions, network_failures)
  │
  ▼
Run finishes. run_multiple.main() resumes.
  │
  ▼
generate_master_report
  └─ _find_artifacts_for_run(errors_dir, run_start, run_end, 2)
       └─ _parse_artifact_ts on each filename
       └─ filename timestamp ∈ [run_start, run_end+2s] → matched
       └─ embeds image + log content in the markdown
  │
generate_html_dashboard
  └─ _build_view_html
       └─ _collect_artifacts_for_runs(runs_subset)
            └─ same window-matching as master report
            └─ _img_data_url converts PNG → base64 data: URL
            └─ _read_log_file reads + truncates log
       └─ outputs <div class='forensic-block'>...</div>
```

---

*This document mirrors the runtime call graph. To regenerate, walk
each function in order from `run_multiple.main()` outward.*
