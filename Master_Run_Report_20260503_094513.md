# Master Run Report

**Generated:** 2026-05-03T09:45:13  
**Number of runs:** 1  

## Summary

| Run | Started | Duration | Tests | Pass | Fail | Skip | Errors | Status |
|---:|---|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 2026-05-03 09:17:05 | 1686.8s | 113 | 25 | 83 | 0 | 5 | ❌ |
| **TOTAL** | — | **1686.8s** | **113** | **25** | **83** | **0** | **5** | **❌** |

*\* duration shown is wall-clock when junit XML is missing.*

**Aggregate pass rate:** 25 / 113 = **22.1%**

## Stability Index — Tests with Failures

Tests that failed in one or more runs (regression / flake candidates):

| Test | Failed in runs | Failure rate |
|---|---|---:|
| `TestCascade::test_01_login` | [1] | 1 / 1 |
| `TestCascade::test_02_create_domain` | [1] | 1 / 1 |
| `TestCascade::test_03_create_link_with_domain` | [1] | 1 / 1 |
| `TestCascade::test_04_attempt_delete_domain_and_observe` | [1] | 1 / 1 |
| `TestDiscard::test_01_login` | [1] | 1 / 1 |
| `TestDiscard::test_02_add_link_x_discards_draft` | [1] | 1 / 1 |
| `TestDiscard::test_03_setup_create_link` | [1] | 1 / 1 |
| `TestDiscard::test_04_delete_x_aborts` | [1] | 1 / 1 |
| `TestDiscard::test_05_delete_cancel_aborts` | [1] | 1 / 1 |
| `TestDiscard::test_06_delete_actually_works` | [1] | 1 / 1 |
| `TestDomainLinkCascade::test_01_login` | [1] | 1 / 1 |
| `TestDomainLinkCascade::test_02_create_domain` | [1] | 1 / 1 |
| `TestDomainLinkCascade::test_03_create_link_with_domain` | [1] | 1 / 1 |
| `TestDomainLinkCascade::test_04_delete_domain_asserts_silent_cascade` | [1] | 1 / 1 |
| `TestEndUserFlows::test_01_login_admin` | [1] | 1 / 1 |
| `TestEnvironmentLinkCascade::test_01_login` | [1] | 1 / 1 |
| `TestEnvironmentLinkCascade::test_02_create_env` | [1] | 1 / 1 |
| `TestEnvironmentLinkCascade::test_03_create_link_with_env` | [1] | 1 / 1 |
| `TestEnvironmentLinkCascade::test_04_delete_env_and_observe` | [1] | 1 / 1 |
| `TestImageUpload::test_01_login` | [1] | 1 / 1 |
| `TestImageUpload::test_02_probe_file_input` | [1] | 1 / 1 |
| `TestImageUpload::test_03_upload_valid_under_limit` | [1] | 1 / 1 |
| `TestImageUpload::test_04_upload_over_limit` | [1] | 1 / 1 |
| `TestImageUpload::test_05_upload_invalid_format` | [1] | 1 / 1 |
| `TestInactiveLink::test_01_login` | [1] | 1 / 1 |
| `TestInactiveLink::test_02_create_inactive_link` | [1] | 1 / 1 |
| `TestInactiveLink::test_03_check_public_homepage` | [1] | 1 / 1 |
| `TestLinksAdminGrid::test_01_login` | [1] | 1 / 1 |
| `TestLinksAdminGrid::test_02_seed_three_links` | [1] | 1 / 1 |
| `TestLinksAdminGrid::test_03_admin_search_filters_grid` | [1] | 1 / 1 |
| `TestLinksAdminGrid::test_04_sort_by_name_changes_top_row` | [1] | 1 / 1 |
| `TestMessageReactivation::test_01_login_admin` | [1] | 1 / 1 |
| `TestMessageReactivation::test_02_create_message_as_inactive` | [1] | 1 / 1 |
| `TestMessageReactivation::test_03_inactive_is_NOT_visible_on_public` | [1] | 1 / 1 |
| `TestMessageReactivation::test_04_toggle_inactive_to_active` | [1] | 1 / 1 |
| `TestMessageReactivation::test_05_active_IS_visible_on_public` | [1] | 1 / 1 |
| `TestMessageReactivation::test_06_toggle_active_back_to_inactive` | [1] | 1 / 1 |
| `TestMessageReactivation::test_07_inactive_again_NOT_visible_on_public` | [1] | 1 / 1 |
| `TestMessagesFlows::test_01_login_admin` | [1] | 1 / 1 |
| `TestMessagesFlows::test_02_create_popup_with_image` | [1] | 1 / 1 |
| `TestMessagesFlows::test_03_admin_popup_preview` | [1] | 1 / 1 |
| `TestMessagesFlows::test_04_public_popup_and_status_toggle` | [1] | 1 / 1 |
| `TestModeratorWorkflow::test_01_links_read_only` | [1] | 1 / 1 |
| `TestModeratorWorkflow::test_01_performance_landing_page` | [1] | 1 / 1 |
| `TestModeratorWorkflow::test_02_navigate_and_crud_tags` | [1] | 1 / 1 |
| `TestModeratorWorkflow::test_03_navigate_and_crud_messages` | [1] | 1 / 1 |
| `TestModeratorWorkflow::test_04_verify_restricted_pages_hidden` | [1] | 1 / 1 |
| `TestNegLinks::test_01_login` | [1] | 1 / 1 |
| `TestNegLinks::test_02_blank_title` | [1] | 1 / 1 |
| `TestNegLinks::test_03_blank_url` | [1] | 1 / 1 |
| `TestNegLinks::test_04_no_domain` | [1] | 1 / 1 |
| `TestNegLinks::test_05_overlength_title` | [1] | 1 / 1 |
| `TestNegLinks::test_06_overlength_description` | [1] | 1 / 1 |
| `TestPortalClient::test_create_domain` | [1] | 1 / 1 |
| `TestPortalClient::test_create_environment` | [1] | 1 / 1 |
| `TestPortalClient::test_create_link` | [1] | 1 / 1 |
| `TestPortalClient::test_create_message` | [1] | 1 / 1 |
| `TestPortalClient::test_create_tag` | [1] | 1 / 1 |
| `TestPortalClient::test_delete_domain` | [1] | 1 / 1 |
| `TestPortalClient::test_delete_environment` | [1] | 1 / 1 |
| `TestPortalClient::test_delete_link` | [1] | 1 / 1 |
| `TestPortalClient::test_delete_message` | [1] | 1 / 1 |
| `TestPortalClient::test_delete_tag` | [1] | 1 / 1 |
| `TestPortalClient::test_login` | [1] | 1 / 1 |
| `TestPortalClient::test_navigate` | [1] | 1 / 1 |
| `TestPortalClient::test_update_domain` | [1] | 1 / 1 |
| `TestPortalClient::test_update_environment` | [1] | 1 / 1 |
| `TestPortalClient::test_update_link` | [1] | 1 / 1 |
| `TestPortalClient::test_update_message` | [1] | 1 / 1 |
| `TestPortalClient::test_update_tag` | [1] | 1 / 1 |
| `TestTagLinkCascade::test_01_login` | [1] | 1 / 1 |
| `TestTagLinkCascade::test_02_create_tag` | [1] | 1 / 1 |
| `TestTagLinkCascade::test_03_create_link_with_tag` | [1] | 1 / 1 |
| `TestTagLinkCascade::test_04_delete_tag_and_observe` | [1] | 1 / 1 |
| `TestTagMessageCascade::test_01_login` | [1] | 1 / 1 |
| `TestTagMessageCascade::test_02_create_tag` | [1] | 1 / 1 |
| `TestTagMessageCascade::test_03_create_message_attempt_tag` | [1] | 1 / 1 |
| `TestTagMessageCascade::test_04_delete_tag_and_observe` | [1] | 1 / 1 |
| `TestURLAppend::test_01_login` | [1] | 1 / 1 |
| `TestURLAppend::test_02_create_test_env` | [1] | 1 / 1 |
| `TestURLAppend::test_03_create_link_append_yes` | [1] | 1 / 1 |
| `TestURLAppend::test_04_create_link_append_no` | [1] | 1 / 1 |
| `TestURLAppend::test_05_verify_on_homepage` | [1] | 1 / 1 |
| `TestXSSLink::test_01_login` | [1] | 1 / 1 |
| `TestXSSLink::test_02_create_link_with_xss_in_title` | [1] | 1 / 1 |
| `TestXSSLink::test_03_verify_title_payload_is_escaped_on_public` | [1] | 1 / 1 |
| `TestXSSLink::test_04_create_link_with_xss_in_description` | [1] | 1 / 1 |
| `TestXSSLink::test_05_verify_description_payload_is_escaped_on_public` | [1] | 1 / 1 |

## Per-Run Details

### Run 1 — 2026-05-03 09:17:05

- **Status:** ❌ 88 failure(s)
- **Duration:** 1686.78s
- **Tests:** 113 (25 pass, 83 fail, 0 skip, 5 err)
- **Exit code:** `1`
- **Detailed HTML report:** [`/home/runner/work/Automation/Automation/Automation-main/reports/master/run_1_report.html`](run_1_report.html)
- **JUnit XML:** [`/home/runner/work/Automation/Automation/Automation-main/reports/master/run_1_junit.xml`](run_1_junit.xml)

#### ❌ `TestLinksAdminGrid::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestLinksAdminGrid::test_02_seed_three_links`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_seed_three_links_20260503_091805.png](../../zero_touch_logs/errors/test_02_seed_three_links_20260503_091805.png)

**Zero-touch error log:** [`test_02_seed_three_links_20260503_091805_logs.txt`](../../zero_touch_logs/errors/test_02_seed_three_links_20260503_091805_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_02_seed_three_links
Failed at: 20260503_091805
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestLinksAdminGrid::test_03_admin_search_filters_grid`

**Error:** `KeyError: 'names'`

![test_03_admin_search_filters_grid_20260503_091805.png](../../zero_touch_logs/errors/test_03_admin_search_filters_grid_20260503_091805.png)

**Zero-touch error log:** [`test_03_admin_search_filters_grid_20260503_091805_logs.txt`](../../zero_touch_logs/errors/test_03_admin_search_filters_grid_20260503_091805_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_03_admin_search_filters_grid
Failed at: 20260503_091805
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestLinksAdminGrid::test_04_sort_by_name_changes_top_row`

**Error:** `KeyError: 'names'`

![test_04_sort_by_name_changes_top_row_20260503_091805.png](../../zero_touch_logs/errors/test_04_sort_by_name_changes_top_row_20260503_091805.png)

**Zero-touch error log:** [`test_04_sort_by_name_changes_top_row_20260503_091805_logs.txt`](../../zero_touch_logs/errors/test_04_sort_by_name_changes_top_row_20260503_091805_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_04_sort_by_name_changes_top_row
Failed at: 20260503_091805
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestCascade::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestCascade::test_02_create_domain`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_domain_20260503_091858.png](../../zero_touch_logs/errors/test_02_create_domain_20260503_091858.png)

![test_02_create_domain_20260503_091952.png](../../zero_touch_logs/errors/test_02_create_domain_20260503_091952.png)

**Zero-touch error log:** [`test_02_create_domain_20260503_091858_logs.txt`](../../zero_touch_logs/errors/test_02_create_domain_20260503_091858_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_02_create_domain
Failed at: 20260503_091858
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_02_create_domain_20260503_091952_logs.txt`](../../zero_touch_logs/errors/test_02_create_domain_20260503_091952_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_02_create_domain
Failed at: 20260503_091952
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestCascade::test_03_create_link_with_domain`

**Error:** `KeyError: 'domain_name'`

![test_03_create_link_with_domain_20260503_091858.png](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091858.png)

![test_03_create_link_with_domain_20260503_091952.png](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091952.png)

**Zero-touch error log:** [`test_03_create_link_with_domain_20260503_091858_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091858_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_03_create_link_with_domain
Failed at: 20260503_091858
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_03_create_link_with_domain_20260503_091952_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091952_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_03_create_link_with_domain
Failed at: 20260503_091952
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestCascade::test_04_attempt_delete_domain_and_observe`

**Error:** `KeyError: 'domain_name'`

![test_04_attempt_delete_domain_and_observe_20260503_091858.png](../../zero_touch_logs/errors/test_04_attempt_delete_domain_and_observe_20260503_091858.png)

**Zero-touch error log:** [`test_04_attempt_delete_domain_and_observe_20260503_091858_logs.txt`](../../zero_touch_logs/errors/test_04_attempt_delete_domain_and_observe_20260503_091858_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_04_attempt_delete_domain_and_observe
Failed at: 20260503_091858
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDomainLinkCascade::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestDomainLinkCascade::test_02_create_domain`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_domain_20260503_091858.png](../../zero_touch_logs/errors/test_02_create_domain_20260503_091858.png)

![test_02_create_domain_20260503_091952.png](../../zero_touch_logs/errors/test_02_create_domain_20260503_091952.png)

**Zero-touch error log:** [`test_02_create_domain_20260503_091858_logs.txt`](../../zero_touch_logs/errors/test_02_create_domain_20260503_091858_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_02_create_domain
Failed at: 20260503_091858
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_02_create_domain_20260503_091952_logs.txt`](../../zero_touch_logs/errors/test_02_create_domain_20260503_091952_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_02_create_domain
Failed at: 20260503_091952
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDomainLinkCascade::test_03_create_link_with_domain`

**Error:** `KeyError: 'domain_name'`

![test_03_create_link_with_domain_20260503_091858.png](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091858.png)

![test_03_create_link_with_domain_20260503_091952.png](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091952.png)

**Zero-touch error log:** [`test_03_create_link_with_domain_20260503_091858_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091858_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_03_create_link_with_domain
Failed at: 20260503_091858
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_03_create_link_with_domain_20260503_091952_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_domain_20260503_091952_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_03_create_link_with_domain
Failed at: 20260503_091952
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDomainLinkCascade::test_04_delete_domain_asserts_silent_cascade`

**Error:** `KeyError: 'domain_name'`

![test_04_delete_domain_asserts_silent_cascade_20260503_091952.png](../../zero_touch_logs/errors/test_04_delete_domain_asserts_silent_cascade_20260503_091952.png)

**Zero-touch error log:** [`test_04_delete_domain_asserts_silent_cascade_20260503_091952_logs.txt`](../../zero_touch_logs/errors/test_04_delete_domain_asserts_silent_cascade_20260503_091952_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_04_delete_domain_asserts_silent_cascade
Failed at: 20260503_091952
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagLinkCascade::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestTagLinkCascade::test_02_create_tag`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_tag_20260503_092046.png](../../zero_touch_logs/errors/test_02_create_tag_20260503_092046.png)

![test_02_create_tag_20260503_092234.png](../../zero_touch_logs/errors/test_02_create_tag_20260503_092234.png)

**Zero-touch error log:** [`test_02_create_tag_20260503_092046_logs.txt`](../../zero_touch_logs/errors/test_02_create_tag_20260503_092046_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_02_create_tag
Failed at: 20260503_092046
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_02_create_tag_20260503_092234_logs.txt`](../../zero_touch_logs/errors/test_02_create_tag_20260503_092234_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_02_create_tag
Failed at: 20260503_092234
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagLinkCascade::test_03_create_link_with_tag`

**Error:** `KeyError: 'tag_name'`

![test_03_create_link_with_tag_20260503_092046.png](../../zero_touch_logs/errors/test_03_create_link_with_tag_20260503_092046.png)

**Zero-touch error log:** [`test_03_create_link_with_tag_20260503_092046_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_tag_20260503_092046_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_03_create_link_with_tag
Failed at: 20260503_092046
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagLinkCascade::test_04_delete_tag_and_observe`

**Error:** `KeyError: 'tag_name'`

![test_04_delete_tag_and_observe_20260503_092046.png](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092046.png)

![test_04_delete_tag_and_observe_20260503_092235.png](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092235.png)

**Zero-touch error log:** [`test_04_delete_tag_and_observe_20260503_092046_logs.txt`](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092046_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_04_delete_tag_and_observe
Failed at: 20260503_092046
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_04_delete_tag_and_observe_20260503_092235_logs.txt`](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092235_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_04_delete_tag_and_observe
Failed at: 20260503_092235
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestEnvironmentLinkCascade::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestEnvironmentLinkCascade::test_02_create_env`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_env_20260503_092140.png](../../zero_touch_logs/errors/test_02_create_env_20260503_092140.png)

**Zero-touch error log:** [`test_02_create_env_20260503_092140_logs.txt`](../../zero_touch_logs/errors/test_02_create_env_20260503_092140_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_02_create_env
Failed at: 20260503_092140
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestEnvironmentLinkCascade::test_03_create_link_with_env`

**Error:** `KeyError: 'env_name'`

![test_03_create_link_with_env_20260503_092140.png](../../zero_touch_logs/errors/test_03_create_link_with_env_20260503_092140.png)

**Zero-touch error log:** [`test_03_create_link_with_env_20260503_092140_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_with_env_20260503_092140_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_03_create_link_with_env
Failed at: 20260503_092140
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestEnvironmentLinkCascade::test_04_delete_env_and_observe`

**Error:** `KeyError: 'env_name'`

![test_04_delete_env_and_observe_20260503_092140.png](../../zero_touch_logs/errors/test_04_delete_env_and_observe_20260503_092140.png)

**Zero-touch error log:** [`test_04_delete_env_and_observe_20260503_092140_logs.txt`](../../zero_touch_logs/errors/test_04_delete_env_and_observe_20260503_092140_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_04_delete_env_and_observe
Failed at: 20260503_092140
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagMessageCascade::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestTagMessageCascade::test_02_create_tag`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_tag_20260503_092046.png](../../zero_touch_logs/errors/test_02_create_tag_20260503_092046.png)

![test_02_create_tag_20260503_092234.png](../../zero_touch_logs/errors/test_02_create_tag_20260503_092234.png)

**Zero-touch error log:** [`test_02_create_tag_20260503_092046_logs.txt`](../../zero_touch_logs/errors/test_02_create_tag_20260503_092046_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_02_create_tag
Failed at: 20260503_092046
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_02_create_tag_20260503_092234_logs.txt`](../../zero_touch_logs/errors/test_02_create_tag_20260503_092234_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_02_create_tag
Failed at: 20260503_092234
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagMessageCascade::test_03_create_message_attempt_tag`

**Error:** `KeyError: 'tag_name'`

![test_03_create_message_attempt_tag_20260503_092235.png](../../zero_touch_logs/errors/test_03_create_message_attempt_tag_20260503_092235.png)

**Zero-touch error log:** [`test_03_create_message_attempt_tag_20260503_092235_logs.txt`](../../zero_touch_logs/errors/test_03_create_message_attempt_tag_20260503_092235_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_03_create_message_attempt_tag
Failed at: 20260503_092235
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestTagMessageCascade::test_04_delete_tag_and_observe`

**Error:** `KeyError: 'tag_name'`

![test_04_delete_tag_and_observe_20260503_092046.png](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092046.png)

![test_04_delete_tag_and_observe_20260503_092235.png](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092235.png)

**Zero-touch error log:** [`test_04_delete_tag_and_observe_20260503_092046_logs.txt`](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092046_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_04_delete_tag_and_observe
Failed at: 20260503_092046
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

**Zero-touch error log:** [`test_04_delete_tag_and_observe_20260503_092235_logs.txt`](../../zero_touch_logs/errors/test_04_delete_tag_and_observe_20260503_092235_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_04_delete_tag_and_observe
Failed at: 20260503_092235
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDiscard::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestDiscard::test_02_add_link_x_discards_draft`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_add_link_x_discards_draft_20260503_092328.png](../../zero_touch_logs/errors/test_02_add_link_x_discards_draft_20260503_092328.png)

**Zero-touch error log:** [`test_02_add_link_x_discards_draft_20260503_092328_logs.txt`](../../zero_touch_logs/errors/test_02_add_link_x_discards_draft_20260503_092328_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_02_add_link_x_discards_draft
Failed at: 20260503_092328
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDiscard::test_03_setup_create_link`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_03_setup_create_link_20260503_092358.png](../../zero_touch_logs/errors/test_03_setup_create_link_20260503_092358.png)

**Zero-touch error log:** [`test_03_setup_create_link_20260503_092358_logs.txt`](../../zero_touch_logs/errors/test_03_setup_create_link_20260503_092358_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_03_setup_create_link
Failed at: 20260503_092358
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDiscard::test_04_delete_x_aborts`

**Error:** `KeyError: 'link_name'`

![test_04_delete_x_aborts_20260503_092358.png](../../zero_touch_logs/errors/test_04_delete_x_aborts_20260503_092358.png)

**Zero-touch error log:** [`test_04_delete_x_aborts_20260503_092358_logs.txt`](../../zero_touch_logs/errors/test_04_delete_x_aborts_20260503_092358_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_04_delete_x_aborts
Failed at: 20260503_092358
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDiscard::test_05_delete_cancel_aborts`

**Error:** `KeyError: 'link_name'`

![test_05_delete_cancel_aborts_20260503_092358.png](../../zero_touch_logs/errors/test_05_delete_cancel_aborts_20260503_092358.png)

**Zero-touch error log:** [`test_05_delete_cancel_aborts_20260503_092358_logs.txt`](../../zero_touch_logs/errors/test_05_delete_cancel_aborts_20260503_092358_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_05_delete_cancel_aborts
Failed at: 20260503_092358
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestDiscard::test_06_delete_actually_works`

**Error:** `KeyError: 'link_name'`

![test_06_delete_actually_works_20260503_092358.png](../../zero_touch_logs/errors/test_06_delete_actually_works_20260503_092358.png)

**Zero-touch error log:** [`test_06_delete_actually_works_20260503_092358_logs.txt`](../../zero_touch_logs/errors/test_06_delete_actually_works_20260503_092358_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_06_delete_actually_works
Failed at: 20260503_092358
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestEndUserFlows::test_01_login_admin`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_admin_20260503_092421.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421.png)

![test_01_login_admin_20260503_092846.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846.png)

![test_01_login_admin_20260503_093306.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306.png)

**Zero-touch error log:** [`test_01_login_admin_20260503_092421_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421_logs.txt)

```
Test     : tests/test_end_user_flows.py::TestEndUserFlows::test_01_login_admin
Failed at: 20260503_092421
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bnZVbE9aWklRR0dHVU8zcElmY0dweGh1L0RsRWRyZ1o3UFo2SFl2SFZFWGxtNlhRcWlTTEJ6WlV1OVd1Q2Z4aTRHc3kwc3hEWTVNM2FjaTJaeFhzWFE9PTsyMDI2LTA1LTAzVDA5OjI0OjA1LjMwNzEyOTFaO1JUeDIvQ3RiWXpKdDFFdHlBa2NqQ2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%220074e4b5-6dd2-46a4-ae97-6e2879ed182f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A384%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800247%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A663%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:24:02.284] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:24:05.984] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded26-eb2e-7226-b953-8ee7cf837163&response_mode=fragment&client_info=1&clidata=1&nonce=019ded26-eb2f-7b4a-a178-1ab5c3d2fa32&state=eyJpZCI6IjAxOWRlZDI2LWViMmYtNzc4Ni04MWVlLTViNzI0Y2E3NDFmMSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=ztrAyg9l8cOhE496wCYmiDG9GPvVXXMHILrO5TG4QQQ&code_challenge_method=S256:16:0)
[09:24:09.473] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test:0:0)

==== Consol
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_092846_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_01_login_admin
Failed at: 20260503_092846
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:28:27.443] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:28:30.847] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-f521-7d81-ae79-160290b17e2e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-f522-7664-a5cf-2d479dd5ce60&state=eyJpZCI6IjAxOWRlZDJhLWY1MjItN2Q4NC04NmY3LTMxMzlmMWU0Y2I4OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=hUW8i1PdinTgspj2Ab4B-dRYTiGJ4pxMefAdnY08stY&code_challenge_method=S256:16:0)
[09:28:34.320] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_093306_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_01_login_admin
Failed at: 20260503_093306
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:32:47.047] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:32:50.738] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2e-eb47-71fd-a932-073af0034d50&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2e-eb48-7a20-bfea-8cdb44ff97e5&state=eyJpZCI6IjAxOWRlZDJlLWViNDgtN2Q1Ni1hNzgxLWYwNWY3NDdlNjFkNSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=jLRoz76OjMrUdMBCIDAkR6juHclB2eh65mlZ8vTR3-Q&code_challenge_method=S256:16:0)
[09:32:54.824] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test:0:0)


... (truncated — open the log file for the full content)
```

#### ❌ `TestImageUpload::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestImageUpload::test_02_probe_file_input`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_probe_file_input_20260503_092559.png](../../zero_touch_logs/errors/test_02_probe_file_input_20260503_092559.png)

**Zero-touch error log:** [`test_02_probe_file_input_20260503_092559_logs.txt`](../../zero_touch_logs/errors/test_02_probe_file_input_20260503_092559_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_02_probe_file_input
Failed at: 20260503_092559
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestImageUpload::test_03_upload_valid_under_limit`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_03_upload_valid_under_limit_20260503_092629.png](../../zero_touch_logs/errors/test_03_upload_valid_under_limit_20260503_092629.png)

**Zero-touch error log:** [`test_03_upload_valid_under_limit_20260503_092629_logs.txt`](../../zero_touch_logs/errors/test_03_upload_valid_under_limit_20260503_092629_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_03_upload_valid_under_limit
Failed at: 20260503_092629
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestImageUpload::test_04_upload_over_limit`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_04_upload_over_limit_20260503_092700.png](../../zero_touch_logs/errors/test_04_upload_over_limit_20260503_092700.png)

**Zero-touch error log:** [`test_04_upload_over_limit_20260503_092700_logs.txt`](../../zero_touch_logs/errors/test_04_upload_over_limit_20260503_092700_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_04_upload_over_limit
Failed at: 20260503_092700
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestImageUpload::test_05_upload_invalid_format`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_05_upload_invalid_format_20260503_092730.png](../../zero_touch_logs/errors/test_05_upload_invalid_format_20260503_092730.png)

**Zero-touch error log:** [`test_05_upload_invalid_format_20260503_092730_logs.txt`](../../zero_touch_logs/errors/test_05_upload_invalid_format_20260503_092730_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_05_upload_invalid_format
Failed at: 20260503_092730
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestInactiveLink::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestInactiveLink::test_02_create_inactive_link`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_inactive_link_20260503_092823.png](../../zero_touch_logs/errors/test_02_create_inactive_link_20260503_092823.png)

**Zero-touch error log:** [`test_02_create_inactive_link_20260503_092823_logs.txt`](../../zero_touch_logs/errors/test_02_create_inactive_link_20260503_092823_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_02_create_inactive_link
Failed at: 20260503_092823
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestInactiveLink::test_03_check_public_homepage`

**Error:** `KeyError: 'link_name'`

![test_03_check_public_homepage_20260503_092823.png](../../zero_touch_logs/errors/test_03_check_public_homepage_20260503_092823.png)

**Zero-touch error log:** [`test_03_check_public_homepage_20260503_092823_logs.txt`](../../zero_touch_logs/errors/test_03_check_public_homepage_20260503_092823_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_03_check_public_homepage
Failed at: 20260503_092823
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessagesFlows::test_01_login_admin`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_admin_20260503_092421.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421.png)

![test_01_login_admin_20260503_092846.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846.png)

![test_01_login_admin_20260503_093306.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306.png)

**Zero-touch error log:** [`test_01_login_admin_20260503_092421_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421_logs.txt)

```
Test     : tests/test_end_user_flows.py::TestEndUserFlows::test_01_login_admin
Failed at: 20260503_092421
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bnZVbE9aWklRR0dHVU8zcElmY0dweGh1L0RsRWRyZ1o3UFo2SFl2SFZFWGxtNlhRcWlTTEJ6WlV1OVd1Q2Z4aTRHc3kwc3hEWTVNM2FjaTJaeFhzWFE9PTsyMDI2LTA1LTAzVDA5OjI0OjA1LjMwNzEyOTFaO1JUeDIvQ3RiWXpKdDFFdHlBa2NqQ2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%220074e4b5-6dd2-46a4-ae97-6e2879ed182f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A384%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800247%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A663%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:24:02.284] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:24:05.984] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded26-eb2e-7226-b953-8ee7cf837163&response_mode=fragment&client_info=1&clidata=1&nonce=019ded26-eb2f-7b4a-a178-1ab5c3d2fa32&state=eyJpZCI6IjAxOWRlZDI2LWViMmYtNzc4Ni04MWVlLTViNzI0Y2E3NDFmMSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=ztrAyg9l8cOhE496wCYmiDG9GPvVXXMHILrO5TG4QQQ&code_challenge_method=S256:16:0)
[09:24:09.473] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test:0:0)

==== Consol
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_092846_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_01_login_admin
Failed at: 20260503_092846
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:28:27.443] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:28:30.847] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-f521-7d81-ae79-160290b17e2e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-f522-7664-a5cf-2d479dd5ce60&state=eyJpZCI6IjAxOWRlZDJhLWY1MjItN2Q4NC04NmY3LTMxMzlmMWU0Y2I4OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=hUW8i1PdinTgspj2Ab4B-dRYTiGJ4pxMefAdnY08stY&code_challenge_method=S256:16:0)
[09:28:34.320] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_093306_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_01_login_admin
Failed at: 20260503_093306
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:32:47.047] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:32:50.738] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2e-eb47-71fd-a932-073af0034d50&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2e-eb48-7a20-bfea-8cdb44ff97e5&state=eyJpZCI6IjAxOWRlZDJlLWViNDgtN2Q1Ni1hNzgxLWYwNWY3NDdlNjFkNSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=jLRoz76OjMrUdMBCIDAkR6juHclB2eh65mlZ8vTR3-Q&code_challenge_method=S256:16:0)
[09:32:54.824] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test:0:0)


... (truncated — open the log file for the full content)
```

#### ❌ `TestMessagesFlows::test_02_create_popup_with_image`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_popup_with_image_20260503_092917.png](../../zero_touch_logs/errors/test_02_create_popup_with_image_20260503_092917.png)

**Zero-touch error log:** [`test_02_create_popup_with_image_20260503_092917_logs.txt`](../../zero_touch_logs/errors/test_02_create_popup_with_image_20260503_092917_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_02_create_popup_with_image
Failed at: 20260503_092917
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessagesFlows::test_03_admin_popup_preview`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_03_admin_popup_preview_20260503_092947.png](../../zero_touch_logs/errors/test_03_admin_popup_preview_20260503_092947.png)

**Zero-touch error log:** [`test_03_admin_popup_preview_20260503_092947_logs.txt`](../../zero_touch_logs/errors/test_03_admin_popup_preview_20260503_092947_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_03_admin_popup_preview
Failed at: 20260503_092947
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessagesFlows::test_04_public_popup_and_status_toggle`

**Error:** `AssertionError: test_02 must have created a message first`

![test_04_public_popup_and_status_toggle_20260503_092947.png](../../zero_touch_logs/errors/test_04_public_popup_and_status_toggle_20260503_092947.png)

**Zero-touch error log:** [`test_04_public_popup_and_status_toggle_20260503_092947_logs.txt`](../../zero_touch_logs/errors/test_04_public_popup_and_status_toggle_20260503_092947_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_04_public_popup_and_status_toggle
Failed at: 20260503_092947
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestModeratorWorkflow::test_01_links_read_only`

**Error:** `failed on setup with "playwright._impl._errors.TargetClosedError: BrowserType.launch: Target page, context or browser has been closed`

*(no zero-touch artifacts captured for this failure within the run window — failure may have occurred during fixture setup before the conftest hook ran)*

#### ❌ `TestModeratorWorkflow::test_01_performance_landing_page`

**Error:** `failed on setup with "playwright._impl._errors.TargetClosedError: BrowserType.launch: Target page, context or browser has been closed`

*(no zero-touch artifacts captured for this failure within the run window — failure may have occurred during fixture setup before the conftest hook ran)*

#### ❌ `TestModeratorWorkflow::test_02_navigate_and_crud_tags`

**Error:** `failed on setup with "playwright._impl._errors.TargetClosedError: BrowserType.launch: Target page, context or browser has been closed`

*(no zero-touch artifacts captured for this failure within the run window — failure may have occurred during fixture setup before the conftest hook ran)*

#### ❌ `TestModeratorWorkflow::test_03_navigate_and_crud_messages`

**Error:** `failed on setup with "playwright._impl._errors.TargetClosedError: BrowserType.launch: Target page, context or browser has been closed`

*(no zero-touch artifacts captured for this failure within the run window — failure may have occurred during fixture setup before the conftest hook ran)*

#### ❌ `TestModeratorWorkflow::test_04_verify_restricted_pages_hidden`

**Error:** `failed on setup with "playwright._impl._errors.TargetClosedError: BrowserType.launch: Target page, context or browser has been closed`

*(no zero-touch artifacts captured for this failure within the run window — failure may have occurred during fixture setup before the conftest hook ran)*

#### ❌ `TestNegLinks::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestNegLinks::test_02_blank_title`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_blank_title_20260503_093042.png](../../zero_touch_logs/errors/test_02_blank_title_20260503_093042.png)

**Zero-touch error log:** [`test_02_blank_title_20260503_093042_logs.txt`](../../zero_touch_logs/errors/test_02_blank_title_20260503_093042_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_02_blank_title
Failed at: 20260503_093042
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestNegLinks::test_03_blank_url`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_03_blank_url_20260503_093112.png](../../zero_touch_logs/errors/test_03_blank_url_20260503_093112.png)

**Zero-touch error log:** [`test_03_blank_url_20260503_093112_logs.txt`](../../zero_touch_logs/errors/test_03_blank_url_20260503_093112_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_03_blank_url
Failed at: 20260503_093112
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestNegLinks::test_04_no_domain`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_04_no_domain_20260503_093142.png](../../zero_touch_logs/errors/test_04_no_domain_20260503_093142.png)

**Zero-touch error log:** [`test_04_no_domain_20260503_093142_logs.txt`](../../zero_touch_logs/errors/test_04_no_domain_20260503_093142_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_04_no_domain
Failed at: 20260503_093142
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestNegLinks::test_05_overlength_title`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_05_overlength_title_20260503_093213.png](../../zero_touch_logs/errors/test_05_overlength_title_20260503_093213.png)

**Zero-touch error log:** [`test_05_overlength_title_20260503_093213_logs.txt`](../../zero_touch_logs/errors/test_05_overlength_title_20260503_093213_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_05_overlength_title
Failed at: 20260503_093213
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestNegLinks::test_06_overlength_description`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_06_overlength_description_20260503_093243.png](../../zero_touch_logs/errors/test_06_overlength_description_20260503_093243.png)

**Zero-touch error log:** [`test_06_overlength_description_20260503_093243_logs.txt`](../../zero_touch_logs/errors/test_06_overlength_description_20260503_093243_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_06_overlength_description
Failed at: 20260503_093243
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_01_login_admin`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_admin_20260503_092421.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421.png)

![test_01_login_admin_20260503_092846.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846.png)

![test_01_login_admin_20260503_093306.png](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306.png)

**Zero-touch error log:** [`test_01_login_admin_20260503_092421_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092421_logs.txt)

```
Test     : tests/test_end_user_flows.py::TestEndUserFlows::test_01_login_admin
Failed at: 20260503_092421
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bnZVbE9aWklRR0dHVU8zcElmY0dweGh1L0RsRWRyZ1o3UFo2SFl2SFZFWGxtNlhRcWlTTEJ6WlV1OVd1Q2Z4aTRHc3kwc3hEWTVNM2FjaTJaeFhzWFE9PTsyMDI2LTA1LTAzVDA5OjI0OjA1LjMwNzEyOTFaO1JUeDIvQ3RiWXpKdDFFdHlBa2NqQ2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%220074e4b5-6dd2-46a4-ae97-6e2879ed182f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A384%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800245%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800247%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800246%2C%22acD%22%3A663%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:24:02.284] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:24:05.984] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded26-eb2e-7226-b953-8ee7cf837163&response_mode=fragment&client_info=1&clidata=1&nonce=019ded26-eb2f-7b4a-a178-1ab5c3d2fa32&state=eyJpZCI6IjAxOWRlZDI2LWViMmYtNzc4Ni04MWVlLTViNzI0Y2E3NDFmMSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=ztrAyg9l8cOhE496wCYmiDG9GPvVXXMHILrO5TG4QQQ&code_challenge_method=S256:16:0)
[09:24:09.473] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjZjgxZGMyNi01ZTU1LTQzYTQtOTRjNy1lYzljOWZlZmZmODMifQ&p=B2C_1_Zira-Test:0:0)

==== Consol
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_092846_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_092846_logs.txt)

```
Test     : tests/test_messages_flows.py::TestMessagesFlows::test_01_login_admin
Failed at: 20260503_092846
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=cVU1TWxpc3JERzY2RU5aNWdiUTY2SDBnTjVZSzhITWE2bExrR01CZDhEMEp0NHBJQXF0eWppcHZua1F5MEg0c2F1WFlxL3Z4TndKOGY5WE01Q25iTEE9PTsyMDI2LTA1LTAzVDA5OjI4OjI5Ljk0Nzc2MzlaO2h4ak96UXBydGNZcWVIQzJhMC9SS0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c4bc0c62-d1ed-41f7-b3a5-eac2466fa082%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A394%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800510%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800512%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800511%2C%22acD%22%3A914%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:28:27.443] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:28:30.847] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-f521-7d81-ae79-160290b17e2e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-f522-7664-a5cf-2d479dd5ce60&state=eyJpZCI6IjAxOWRlZDJhLWY1MjItN2Q4NC04NmY3LTMxMzlmMWU0Y2I4OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=hUW8i1PdinTgspj2Ab4B-dRYTiGJ4pxMefAdnY08stY&code_challenge_method=S256:16:0)
[09:28:34.320] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJhY2JkYjQyYS04NmRiLTQ5OWYtOGM1Ni01MmUwMzlhNTdkMzgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_admin_20260503_093306_logs.txt`](../../zero_touch_logs/errors/test_01_login_admin_20260503_093306_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_01_login_admin
Failed at: 20260503_093306
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:32:47.047] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:32:50.738] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2e-eb47-71fd-a932-073af0034d50&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2e-eb48-7a20-bfea-8cdb44ff97e5&state=eyJpZCI6IjAxOWRlZDJlLWViNDgtN2Q1Ni1hNzgxLWYwNWY3NDdlNjFkNSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=jLRoz76OjMrUdMBCIDAkR6juHclB2eh65mlZ8vTR3-Q&code_challenge_method=S256:16:0)
[09:32:54.824] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test:0:0)


... (truncated — open the log file for the full content)
```

#### ❌ `TestMessageReactivation::test_02_create_message_as_inactive`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_message_as_inactive_20260503_093337.png](../../zero_touch_logs/errors/test_02_create_message_as_inactive_20260503_093337.png)

**Zero-touch error log:** [`test_02_create_message_as_inactive_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_02_create_message_as_inactive_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_02_create_message_as_inactive
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_03_inactive_is_NOT_visible_on_public`

**Error:** `KeyError: 'msg_name'`

![test_03_inactive_is_NOT_visible_on_public_20260503_093337.png](../../zero_touch_logs/errors/test_03_inactive_is_NOT_visible_on_public_20260503_093337.png)

**Zero-touch error log:** [`test_03_inactive_is_NOT_visible_on_public_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_03_inactive_is_NOT_visible_on_public_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_03_inactive_is_NOT_visible_on_public
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_04_toggle_inactive_to_active`

**Error:** `KeyError: 'msg_name'`

![test_04_toggle_inactive_to_active_20260503_093337.png](../../zero_touch_logs/errors/test_04_toggle_inactive_to_active_20260503_093337.png)

**Zero-touch error log:** [`test_04_toggle_inactive_to_active_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_04_toggle_inactive_to_active_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_04_toggle_inactive_to_active
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_05_active_IS_visible_on_public`

**Error:** `KeyError: 'msg_name'`

![test_05_active_IS_visible_on_public_20260503_093337.png](../../zero_touch_logs/errors/test_05_active_IS_visible_on_public_20260503_093337.png)

**Zero-touch error log:** [`test_05_active_IS_visible_on_public_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_05_active_IS_visible_on_public_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_05_active_IS_visible_on_public
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_06_toggle_active_back_to_inactive`

**Error:** `KeyError: 'msg_name'`

![test_06_toggle_active_back_to_inactive_20260503_093337.png](../../zero_touch_logs/errors/test_06_toggle_active_back_to_inactive_20260503_093337.png)

**Zero-touch error log:** [`test_06_toggle_active_back_to_inactive_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_06_toggle_active_back_to_inactive_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_06_toggle_active_back_to_inactive
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestMessageReactivation::test_07_inactive_again_NOT_visible_on_public`

**Error:** `KeyError: 'msg_name'`

![test_07_inactive_again_NOT_visible_on_public_20260503_093337.png](../../zero_touch_logs/errors/test_07_inactive_again_NOT_visible_on_public_20260503_093337.png)

**Zero-touch error log:** [`test_07_inactive_again_NOT_visible_on_public_20260503_093337_logs.txt`](../../zero_touch_logs/errors/test_07_inactive_again_NOT_visible_on_public_20260503_093337_logs.txt)

```
Test     : tests/test_reactivation_flows.py::TestMessageReactivation::test_07_inactive_again_NOT_visible_on_public
Failed at: 20260503_093337
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=N24rQ2E1TEh3N29Ybnhiclg1Si9Uc2ZwM2FjMWtlVVVKWk80a0JJNWI4aEcvQzgzNWJrdmlNdWY5Q3lVQnhwL2hFaWJYQ1M4aU5hOHBIUjFmUWlzdEE9PTsyMDI2LTA1LTAzVDA5OjMyOjQ5LjgwODA1MjlaO0JxUVJ5SUhqZWtwSHUzbHZUbGZxbFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwYTA4YzZhMC01OWY5LTRkZGQtODVhYy00YTgxZGYzMGVmZGQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22b16645d7-55dd-4c7d-91c4-64db39b9d944%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A381%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800770%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800772%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800771%2C%22acD%22%3A928%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestURLAppend::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestURLAppend::test_02_create_test_env`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_test_env_20260503_093504.png](../../zero_touch_logs/errors/test_02_create_test_env_20260503_093504.png)

**Zero-touch error log:** [`test_02_create_test_env_20260503_093504_logs.txt`](../../zero_touch_logs/errors/test_02_create_test_env_20260503_093504_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_02_create_test_env
Failed at: 20260503_093504
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestURLAppend::test_03_create_link_append_yes`

**Error:** `KeyError: 'env_name'`

![test_03_create_link_append_yes_20260503_093504.png](../../zero_touch_logs/errors/test_03_create_link_append_yes_20260503_093504.png)

**Zero-touch error log:** [`test_03_create_link_append_yes_20260503_093504_logs.txt`](../../zero_touch_logs/errors/test_03_create_link_append_yes_20260503_093504_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_03_create_link_append_yes
Failed at: 20260503_093504
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestURLAppend::test_04_create_link_append_no`

**Error:** `KeyError: 'env_name'`

![test_04_create_link_append_no_20260503_093504.png](../../zero_touch_logs/errors/test_04_create_link_append_no_20260503_093504.png)

**Zero-touch error log:** [`test_04_create_link_append_no_20260503_093504_logs.txt`](../../zero_touch_logs/errors/test_04_create_link_append_no_20260503_093504_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_04_create_link_append_no
Failed at: 20260503_093504
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestURLAppend::test_05_verify_on_homepage`

**Error:** `KeyError: 'env_name'`

![test_05_verify_on_homepage_20260503_093504.png](../../zero_touch_logs/errors/test_05_verify_on_homepage_20260503_093504.png)

**Zero-touch error log:** [`test_05_verify_on_homepage_20260503_093504_logs.txt`](../../zero_touch_logs/errors/test_05_verify_on_homepage_20260503_093504_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_05_verify_on_homepage
Failed at: 20260503_093504
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestXSSLink::test_01_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_01_login_20260503_091735.png](../../zero_touch_logs/errors/test_01_login_20260503_091735.png)

![test_01_login_20260503_091828.png](../../zero_touch_logs/errors/test_01_login_20260503_091828.png)

![test_01_login_20260503_091922.png](../../zero_touch_logs/errors/test_01_login_20260503_091922.png)

![test_01_login_20260503_092016.png](../../zero_touch_logs/errors/test_01_login_20260503_092016.png)

![test_01_login_20260503_092110.png](../../zero_touch_logs/errors/test_01_login_20260503_092110.png)

![test_01_login_20260503_092204.png](../../zero_touch_logs/errors/test_01_login_20260503_092204.png)

![test_01_login_20260503_092257.png](../../zero_touch_logs/errors/test_01_login_20260503_092257.png)

![test_01_login_20260503_092529.png](../../zero_touch_logs/errors/test_01_login_20260503_092529.png)

![test_01_login_20260503_092753.png](../../zero_touch_logs/errors/test_01_login_20260503_092753.png)

![test_01_login_20260503_093011.png](../../zero_touch_logs/errors/test_01_login_20260503_093011.png)

![test_01_login_20260503_093433.png](../../zero_touch_logs/errors/test_01_login_20260503_093433.png)

![test_01_login_20260503_093557.png](../../zero_touch_logs/errors/test_01_login_20260503_093557.png)

**Zero-touch error log:** [`test_01_login_20260503_091735_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091735_logs.txt)

```
Test     : tests/test_admin_grid_controls.py::TestLinksAdminGrid::test_01_login
Failed at: 20260503_091735
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aXpMRUYyQUd4LzFyUlVtWm92UkRJWDVNSWZsSVVoN005M2xtMWpMeGFUVWZwY2pFZ2dTRTM1WFJETHRtcXZMN3Fwc0ovNDZYcUhEOUFTV1loNDV0akE9PTsyMDI2LTA1LTAzVDA5OjE3OjE4LjMyNzY1MzRaO0ZIUmZXeWt1MUJJcFhXeTM3L3doRXc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22063d0c97-be2e-43fe-a237-17dd96ea72b1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799838%2C%22acD%22%3A418%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799840%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799839%2C%22acD%22%3A622%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:17:13.355] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:17:19.084] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded20-b000-764c-9358-94a8b9155b5e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded20-b001-7650-99a6-b28ca9a64f8d&state=eyJpZCI6IjAxOWRlZDIwLWIwMDEtNzM3NC05MDRmLTY5ZGQ4NzcwY2U4MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=PXiZLScgVwP6kOMgNtFjTarAMx94yjl2s2QK-YVXa0g&code_challenge_method=S256:16:0)
[09:17:22.634] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1ODgyODJlMS0xNTBlLTQ3MmUtYTM2Yi03MWQ4ZDY4MzI0NDgifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091828_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091828_logs.txt)

```
Test     : tests/test_cascade.py::TestCascade::test_01_login
Failed at: 20260503_091828
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGV5aDZkMlUvSzY3NlNtSXdvUHF6Z1c0UjdIbHRqa2prMTgzM1pNREJCSFN1WmtTdGd5V0NHY3FRQ25sRm90ck4xTjJmUkg4UGkwN0ZaQ3pObmZxeEE9PTsyMDI2LTA1LTAzVDA5OjE4OjExLjY4NzA2NTZaO2lKT1FHb2g1UDdGRWlzdnh3Yy9GY2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2298c90fd0-ab5e-4f5d-9302-d72301c9fad9%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799891%2C%22acD%22%3A375%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799892%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799893%2C%22acD%22%3A611%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:18:09.131] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:18:12.338] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded21-85fc-7db2-9930-f72f1febb773&response_mode=fragment&client_info=1&clidata=1&nonce=019ded21-85fd-7a49-a76a-1e6a92efc961&state=eyJpZCI6IjAxOWRlZDIxLTg1ZmQtN2YzMC05YTVmLTBlNTJjNGNiNzVkOCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=6CX131Ct9eM8HDSBIDpgQmf7nbBAX1s0DgeP2wQ8vkI&code_challenge_method=S256:16:0)
[09:18:15.568] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjMWYxYTMyYy1jMGRhLTRjZTMtYWM2Ni0yOGY0MDk4NTQ4YmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_091922_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_091922_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestDomainLinkCascade::test_01_login
Failed at: 20260503_091922
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=bzljeEZlVG96MXRaMWxRbExlWG9JdXBUMkQrK0NtWHZYd0srdVlCc0JGYVlPd3V6ZU1VT3lUM3h5K2tkOUJYVnhsZDdXQTlPaWtwSFpheG1BK3JoZGc9PTsyMDI2LTA1LTAzVDA5OjE5OjA1LjMwNDU1ODRaO0p4elhtdk84b0lUSUZUVks3R3FTYlE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229e583314-066f-4541-8e8f-d570dc4b05b4%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799945%2C%22acD%22%3A393%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777799946%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777799947%2C%22acD%22%3A460%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:02.492] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:19:06.210] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded22-5661-7fa3-9fc2-9c97fc19472f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded22-5662-74a6-b77a-7d973b27e496&state=eyJpZCI6IjAxOWRlZDIyLTU2NjItN2Q1ZC1iZjJhLTI4ZTQ2MDAyZTk1ZiIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=rgj4Uy5pFVN-q4rVQFHMPUUj8jFCWtyjaDX_ddVxkNk&code_challenge_method=S256:16:0)
[09:19:10.680] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI1NzhkMGFiZC01YWJhLTQ5NWYtYjliOS04YTRhZDAwNDBiMWYifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092016_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092016_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagLinkCascade::test_01_login
Failed at: 20260503_092016
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=czc5SGRkanQ1blB1M3hsbThUOWJnNTNoc2JYNWQyWm9nTGpuTER3dXYrbEROSlg2ZUZZNStmeUpuNWdReG9sVmFCWFozS0NvQnJYbTRId1RKZVVrcUE9PTsyMDI2LTA1LTAzVDA5OjE5OjU5LjM4MjY4MjRaO3JDaXBSUGJaUTJtV253Si9BcDRVUEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22c3ad10d1-8b55-4bf2-81d0-8fe44b629f7f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777799999%2C%22acD%22%3A374%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800001%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800000%2C%22acD%22%3A742%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:19:56.542] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:00.017] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-2980-7b2f-aa89-a0406a4e9721&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-2981-74dc-bf64-fd70ef2fee33&state=eyJpZCI6IjAxOWRlZDIzLTI5ODEtN2I2Ni1hY2U1LTY3NGE4NjI2MmI1MyIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=3AUDy4WMcDFAnLwR6K-SqV0vcmB7Vrt2xUsh4hFehTc&code_challenge_method=S256:16:0)
[09:20:03.429] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIwOGU3Nzk0Yi01Nzc5LTQ1ZmMtYjc3Yy04ZWIzMzIxZjYzZDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092110_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092110_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestEnvironmentLinkCascade::test_01_login
Failed at: 20260503_092110
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=UjFPMWJ3UWdZbzRHd2h6eUtDQmlmTTRVbHR1cWNaM0tYeEk3NjhCQ2xiSkJXNHpJVTkvZnQ0eTNxWmEzc2I0dzB5VEYrNkZJNm81d2gvb0NrNUkxeEE9PTsyMDI2LTA1LTAzVDA5OjIwOjUzLjY3NTIyODFaO2pBdisvWksxUmF5dG5zMlZKdHJteEE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22abf89930-9fd1-4b1e-aa81-4c559e1ccdaf%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800053%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800054%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800056%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800055%2C%22acD%22%3A873%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:20:50.424] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:20:54.313] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded23-fbda-7ce5-9470-27f495bf8da1&response_mode=fragment&client_info=1&clidata=1&nonce=019ded23-fbdb-71f2-bcce-fde0b0c78a02&state=eyJpZCI6IjAxOWRlZDIzLWZiZGItN2Y5Mi04ZTgxLTQyYzFmY2MyMDNiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=F8dxbmhjJWXYZk0HvA9whPMrL8udSbwmdlzHW1_uoPk&code_challenge_method=S256:16:0)
[09:20:57.718] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTNiN2EwNi03OWE0LTQ2OTctYTM0OS1kNWZmYmUyMjg4MWEifQ&p=B2C_1_Zira-Test:0:0)

==== 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092204_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092204_logs.txt)

```
Test     : tests/test_cascade_expanded.py::TestTagMessageCascade::test_01_login
Failed at: 20260503_092204
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=THhyK3U5K1VsU0JpM2xjR0taaXM2WmNVNHNCTFFKUUVhazBDWDhTVWRzSDdaQmdJTjVET2grWTRuUnVlUml1QjBudXhQYVBVQitxYTczMDJDNmltWXc9PTsyMDI2LTA1LTAzVDA5OjIxOjQ3Ljc1OTUwNTRaO2Qyc25pSWJkcllMcGdaUnEyNENDMkE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2202bd9878-093e-4bd8-9777-36a5f58bdbf1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A372%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800108%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800110%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800109%2C%22acD%22%3A910%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:21:45.065] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:21:48.674] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded24-d12f-7531-999e-fa6b8340147d&response_mode=fragment&client_info=1&clidata=1&nonce=019ded24-d130-7fc3-8d6c-709d539f03c8&state=eyJpZCI6IjAxOWRlZDI0LWQxMzAtNzBmMS04NjViLWY4NjQ2Y2RhNzllOSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=v9EYVd-NbybY4xT1qkQiMU96kp-u6COnbAknrNVjaY0&code_challenge_method=S256:16:0)
[09:21:59.674] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiIxOWE4ZDk0Yi04MjczLTQ1OTAtODNkNC0wZWQ4MWYxODlkMjQifQ&p=B2C_1_Zira-Test:0:0)

==== Conso
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092257_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092257_logs.txt)

```
Test     : tests/test_discard.py::TestDiscard::test_01_login
Failed at: 20260503_092257
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=RVlpTloyZlNaTnExZmVWYkVSUGJ4eGNHVjlpWGZkZGVHSXRqeTNUbmtzQWY2d1g0SjU4bDZnKzJkLyt1L2xwS2FZWVVtVThmVEtSWVRDRnFHUXJ1ZFE9PTsyMDI2LTA1LTAzVDA5OjIyOjQxLjE5NDY1NzhaO3AvaDRKc3FXSm1JMkxyRmFTMDN2Nmc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22ec8b3dc9-f4ee-41de-9f7d-d7ad1e395cc1%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A397%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800161%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800163%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800162%2C%22acD%22%3A670%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:22:38.984] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:22:41.864] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded25-a3c9-704f-b022-cfcad1cb1263&response_mode=fragment&client_info=1&clidata=1&nonce=019ded25-a3ca-7340-9d5c-75cb58fd0095&state=eyJpZCI6IjAxOWRlZDI1LWEzYzktN2Q2Zi1hMjdhLTkwN2QzNDQxNThiNCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=IR8l2MrrOz0sFogyed1hcxelDI1TRP9bPItu7xsToqc&code_challenge_method=S256:16:0)
[09:22:45.007] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI3NWQ2ODFhNC01ODJmLTQwYjQtYjhmOS1lOWI1MGU0ZTU5MmIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ===
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092529_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092529_logs.txt)

```
Test     : tests/test_image_upload.py::TestImageUpload::test_01_login
Failed at: 20260503_092529
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=MjdGR0hxMDdFZnhlMnhqWU9nNGFVUWdoVnRoZW85YVJ3bDRkcjBkbGlPd3B6VFVXRXVwcWZoa0lvejBhWmxqQUMrSjR1NjUvSlp3ODVJTlVSUGsrekE9PTsyMDI2LTA1LTAzVDA5OjI1OjEyLjYyMDYwODhaO1Avak9vN2NHb2x3ZG9sdk9LWXYyV0E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%229d80786b-c842-4d83-ad2c-c8a6537be35f%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800312%2C%22acD%22%3A377%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800313%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800314%2C%22acD%22%3A523%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:25:10.427] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:25:13.285] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded27-f35e-77bb-ad95-3368239c6b7e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded27-f35f-7f45-ae0a-46e022d7ff68&state=eyJpZCI6IjAxOWRlZDI3LWYzNWYtNzRmYS05ZjE4LWY0ZmM2Njc0N2E1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=mbcNdb5bQrXNOMEun8mgpszFIQ5w9oVDkloejxAurG4&code_challenge_method=S256:16:0)
[09:25:16.693] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0ZTkwNTFkOS1mNWE2LTRjY2EtYjFjMS04NDNjMDVlY2E1ZjUifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_092753_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_092753_logs.txt)

```
Test     : tests/test_inactive_link.py::TestInactiveLink::test_01_login
Failed at: 20260503_092753
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=aGVITWl3UmpxV0JDekJ5bmlTK0FZNlh4NzRML0NzM3J6OSt2RHJqaXRINDdvb2pSdERWeWovNUxSLzQrazJpUG9GNDJPN2dJOVpSSFlYTW9yY04rb1E9PTsyMDI2LTA1LTAzVDA5OjI3OjM2LjU5NDI0OTVaO3oydUFNRjgrZE9kdEU3Z3lxaXZ1aWc9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%222e583d5b-1b5d-4857-98ca-27b551fc41c8%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800456%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800457%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800458%2C%22acD%22%3A799%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:27:33.989] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:27:37.268] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2a-2479-77df-8e81-4d96018bc16e&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2a-247a-77ab-a1dd-5fb5f034afae&state=eyJpZCI6IjAxOWRlZDJhLTI0N2EtN2IxZi04OTA2LTlmNDFkNjM5ODRmYSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=Qswp9V6Jc5W2lgcaDzBoaAq8yEvKpzjg3aAXAuy9-04&code_challenge_method=S256:16:0)
[09:27:40.927] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJkNDZjZjI5Mi0zZmM5LTRlYzMtYjA2YS02NzMwMGU3NDIxOWQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warni
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093011_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093011_logs.txt)

```
Test     : tests/test_neg_links.py::TestNegLinks::test_01_login
Failed at: 20260503_093011
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=VUJocUJQUklXSDNFODZHMDNORWoxTmp3Rlg3V3grUU9aRFBhTkNSUXFVUmYxakJhU0o2ZGZ4b2wxb2djUzBPdW9yUlI4TTFzQlA4R3l2TU5JaFprb1E9PTsyMDI2LTA1LTAzVDA5OjI5OjU0Ljk5MjM3NTFaO08zTHdvalVIamlpWnlUTytKK29RT2c9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%224f876603-1053-4e80-8e1c-09c98d876890%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800595%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800597%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800596%2C%22acD%22%3A891%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:29:52.504] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:29:55.912] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded2c-4136-7ba1-b7a6-96d66f690b1c&response_mode=fragment&client_info=1&clidata=1&nonce=019ded2c-4137-7286-9e5b-8d9b0b41117a&state=eyJpZCI6IjAxOWRlZDJjLTQxMzctNzA4NC1hZWRmLTM5MmRkYzQyNDE2ZSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=oOEXIo41r8Ugt1W8EyYqkLifSBlD8NiWrm79w3nKgGo&code_challenge_method=S256:16:0)
[09:30:00.356] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiJjY2FhMjcyNC04ZTYzLTRlYTctOGQ4My1mMzQyYTFiZGNkODIifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) 
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093433_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093433_logs.txt)

```
Test     : tests/test_url_append.py::TestURLAppend::test_01_login
Failed at: 20260503_093433
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=b3ZGOHNwU0RMREJhWHBtRVE2NWxTYTJBWXdWVGNjdDRPK3NHZTZEWEdlL1liRVd4NmVZcGdYbng2dXpwZGFSTEx6UFl1TUErRTU3OW5FWFZNYXhzZWc9PTsyMDI2LTA1LTAzVDA5OjM0OjE3LjEzMzg5MjVaOzdWQ1NWSW42bWYrZFZnL3UvS1M5M1E9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%2277e29157-98a4-4840-a8e2-9c6bce6366e0%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A383%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800857%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800859%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800858%2C%22acD%22%3A577%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:34:14.511] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:34:17.797] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded30-4121-7688-a130-2a0045357632&response_mode=fragment&client_info=1&clidata=1&nonce=019ded30-4122-7d21-82db-015a4cd2c7e0&state=eyJpZCI6IjAxOWRlZDMwLTQxMjEtN2M5OC05ZTQ2LWViZjk3ZDdmMDM5OCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=GvvoLDk4gm2LPXHbOiVKS5fLQ5PCReZw6odmXomVAu0&code_challenge_method=S256:16:0)
[09:34:21.432] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4ZmMxOWUzZS03NDUzLTQ5NzUtYmU1NC1mYmEzYzE2OTFkNDgifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1
... (truncated — open the log file for the full content)
```

**Zero-touch error log:** [`test_01_login_20260503_093557_logs.txt`](../../zero_touch_logs/errors/test_01_login_20260503_093557_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_01_login
Failed at: 20260503_093557
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:35:38.320] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:35:41.792] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded31-8864-77ce-8046-b654fdd98b6f&response_mode=fragment&client_info=1&clidata=1&nonce=019ded31-8865-7ed7-a584-b751aa13209b&state=eyJpZCI6IjAxOWRlZDMxLTg4NjUtNzQ3MS05ZGFjLWYyNWUwMGQyYTI1NSIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=YDTxp1s-6hsModj26eejuGSu5VSRA88qQUorDBvVUdk&code_challenge_method=S256:16:0)
[09:35:45.503] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warning
... (truncated — open the log file for the full content)
```

#### ❌ `TestXSSLink::test_02_create_link_with_xss_in_title`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_02_create_link_with_xss_in_title_20260503_093628.png](../../zero_touch_logs/errors/test_02_create_link_with_xss_in_title_20260503_093628.png)

**Zero-touch error log:** [`test_02_create_link_with_xss_in_title_20260503_093628_logs.txt`](../../zero_touch_logs/errors/test_02_create_link_with_xss_in_title_20260503_093628_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_02_create_link_with_xss_in_title
Failed at: 20260503_093628
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestXSSLink::test_03_verify_title_payload_is_escaped_on_public`

**Error:** `KeyError: 'title_link_name'`

![test_03_verify_title_payload_is_escaped_on_public_20260503_093628.png](../../zero_touch_logs/errors/test_03_verify_title_payload_is_escaped_on_public_20260503_093628.png)

**Zero-touch error log:** [`test_03_verify_title_payload_is_escaped_on_public_20260503_093628_logs.txt`](../../zero_touch_logs/errors/test_03_verify_title_payload_is_escaped_on_public_20260503_093628_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_03_verify_title_payload_is_escaped_on_public
Failed at: 20260503_093628
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestXSSLink::test_04_create_link_with_xss_in_description`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_04_create_link_with_xss_in_description_20260503_093658.png](../../zero_touch_logs/errors/test_04_create_link_with_xss_in_description_20260503_093658.png)

**Zero-touch error log:** [`test_04_create_link_with_xss_in_description_20260503_093658_logs.txt`](../../zero_touch_logs/errors/test_04_create_link_with_xss_in_description_20260503_093658_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_04_create_link_with_xss_in_description
Failed at: 20260503_093658
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestXSSLink::test_05_verify_description_payload_is_escaped_on_public`

**Error:** `KeyError: 'desc_link_name'`

![test_05_verify_description_payload_is_escaped_on_public_20260503_093658.png](../../zero_touch_logs/errors/test_05_verify_description_payload_is_escaped_on_public_20260503_093658.png)

**Zero-touch error log:** [`test_05_verify_description_payload_is_escaped_on_public_20260503_093658_logs.txt`](../../zero_touch_logs/errors/test_05_verify_description_payload_is_escaped_on_public_20260503_093658_logs.txt)

```
Test     : tests/test_xss_sanitization.py::TestXSSLink::test_05_verify_description_payload_is_escaped_on_public
Failed at: 20260503_093658
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=OGRELzV0ZEFiVCtmQ3VYVzdGdXFHRTlxUFZ1d2hHNWdIMjh2T2JTLzM1UGhjWEpqMGgwckljaG9LcEgrWnIyN29Mc284d01ZbmFzTVV1ZCtLMlFlSkE9PTsyMDI2LTA1LTAzVDA5OjM1OjQxLjAxNTU3NzRaOzBMaW5TdFVldW55OW5lTkQrYmRYaFE9PTt7Ik9yY2hlc3RyYXRpb25TdGVwIjoxfQ==&tx=StateProperties=eyJUSUQiOiI0NTc5ZTBkNy05ZmE4LTQwNzYtYjYyMS04OTZlNTg3MDdhYzQifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%22aac2cf90-9cb6-4d34-9a0f-ecd482a2cd43%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A400%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A4%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777800941%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777800943%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777800942%2C%22acD%22%3A722%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_login`

**Error:** `playwright._impl._errors.TimeoutError: Locator.wait_for: Timeout 15000ms exceeded.`

![test_login_20260503_093825.png](../../zero_touch_logs/errors/test_login_20260503_093825.png)

**Zero-touch error log:** [`test_login_20260503_093825_logs.txt`](../../zero_touch_logs/errors/test_login_20260503_093825_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_login
Failed at: 20260503_093825
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (3) ====
[09:38:06.746] [error] SSE connection error: Event  (https://front-zira.dev.orangepeak.net/assets/index-CA-VTr2E.js:743:5734)
[09:38:09.232] [error] The Content Security Policy directive 'frame-ancestors' is ignored when delivered via a <meta> element.  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/b2c_1_zira-test/oauth2/v2.0/authorize?client_id=680c9001-8c8a-4ed1-844a-6aa80a51b8d6&scope=openid%20profile%20offline_access%20https%3A%2F%2Fshob127.onmicrosoft.com%2F8c2e8feb-f658-43c6-b247-3037737d951c%2Faccess_as_user&redirect_uri=https%3A%2F%2Ffront-zira.dev.orangepeak.net%2F&client-request-id=019ded33-cbaa-7390-bcbd-03641ece8fcf&response_mode=fragment&client_info=1&clidata=1&nonce=019ded33-cbab-7609-99c4-4fb566d83ae9&state=eyJpZCI6IjAxOWRlZDMzLWNiYWEtNzcyNi05ZWYwLWIyYTI5ZGFlMWUxMCIsIm1ldGEiOnsiaW50ZXJhY3Rpb25UeXBlIjoicmVkaXJlY3QifX0%3D&x-client-SKU=msal.js.browser&x-client-VER=4.30.0&response_type=code&code_challenge=ZMSnvzoSp0lpGq1xwWIhz8kJo_SGupsx0s9tbe4fUbo&code_challenge_method=S256:16:0)
[09:38:11.901] [error] Failed to load resource: the server responded with a status of 400 (Bad Request)  (https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/client/perftrace?tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test:0:0)

==== Console Warnings (1) ====
[09
... (truncated — open the log file for the full content)
```

#### ❌ `TestPortalClient::test_navigate`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_navigate_20260503_093855.png](../../zero_touch_logs/errors/test_navigate_20260503_093855.png)

**Zero-touch error log:** [`test_navigate_20260503_093855_logs.txt`](../../zero_touch_logs/errors/test_navigate_20260503_093855_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_navigate
Failed at: 20260503_093855
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_create_link`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_create_link_20260503_093926.png](../../zero_touch_logs/errors/test_create_link_20260503_093926.png)

**Zero-touch error log:** [`test_create_link_20260503_093926_logs.txt`](../../zero_touch_logs/errors/test_create_link_20260503_093926_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_create_link
Failed at: 20260503_093926
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_update_link`

**Error:** `AssertionError: Locator expected to be visible`

![test_update_link_20260503_093933.png](../../zero_touch_logs/errors/test_update_link_20260503_093933.png)

**Zero-touch error log:** [`test_update_link_20260503_093933_logs.txt`](../../zero_touch_logs/errors/test_update_link_20260503_093933_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_update_link
Failed at: 20260503_093933
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_delete_link`

**Error:** `AssertionError: Locator expected to be visible`

![test_delete_link_20260503_093940.png](../../zero_touch_logs/errors/test_delete_link_20260503_093940.png)

**Zero-touch error log:** [`test_delete_link_20260503_093940_logs.txt`](../../zero_touch_logs/errors/test_delete_link_20260503_093940_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_delete_link
Failed at: 20260503_093940
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_create_domain`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_create_domain_20260503_094010.png](../../zero_touch_logs/errors/test_create_domain_20260503_094010.png)

**Zero-touch error log:** [`test_create_domain_20260503_094010_logs.txt`](../../zero_touch_logs/errors/test_create_domain_20260503_094010_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_create_domain
Failed at: 20260503_094010
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_update_domain`

**Error:** `AssertionError: Missing domain name`

![test_update_domain_20260503_094010.png](../../zero_touch_logs/errors/test_update_domain_20260503_094010.png)

**Zero-touch error log:** [`test_update_domain_20260503_094010_logs.txt`](../../zero_touch_logs/errors/test_update_domain_20260503_094010_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_update_domain
Failed at: 20260503_094010
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_delete_domain`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_delete_domain_20260503_094040.png](../../zero_touch_logs/errors/test_delete_domain_20260503_094040.png)

**Zero-touch error log:** [`test_delete_domain_20260503_094040_logs.txt`](../../zero_touch_logs/errors/test_delete_domain_20260503_094040_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_delete_domain
Failed at: 20260503_094040
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_create_tag`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_create_tag_20260503_094111.png](../../zero_touch_logs/errors/test_create_tag_20260503_094111.png)

**Zero-touch error log:** [`test_create_tag_20260503_094111_logs.txt`](../../zero_touch_logs/errors/test_create_tag_20260503_094111_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_create_tag
Failed at: 20260503_094111
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_update_tag`

**Error:** `playwright._impl._errors.TimeoutError: Locator.scroll_into_view_if_needed: Timeout 30000ms exceeded.`

![test_update_tag_20260503_094141.png](../../zero_touch_logs/errors/test_update_tag_20260503_094141.png)

**Zero-touch error log:** [`test_update_tag_20260503_094141_logs.txt`](../../zero_touch_logs/errors/test_update_tag_20260503_094141_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_update_tag
Failed at: 20260503_094141
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_delete_tag`

**Error:** `playwright._impl._errors.TimeoutError: Locator.scroll_into_view_if_needed: Timeout 30000ms exceeded.`

![test_delete_tag_20260503_094211.png](../../zero_touch_logs/errors/test_delete_tag_20260503_094211.png)

**Zero-touch error log:** [`test_delete_tag_20260503_094211_logs.txt`](../../zero_touch_logs/errors/test_delete_tag_20260503_094211_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_delete_tag
Failed at: 20260503_094211
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_create_message`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_create_message_20260503_094241.png](../../zero_touch_logs/errors/test_create_message_20260503_094241.png)

**Zero-touch error log:** [`test_create_message_20260503_094241_logs.txt`](../../zero_touch_logs/errors/test_create_message_20260503_094241_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_create_message
Failed at: 20260503_094241
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_update_message`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_update_message_20260503_094312.png](../../zero_touch_logs/errors/test_update_message_20260503_094312.png)

**Zero-touch error log:** [`test_update_message_20260503_094312_logs.txt`](../../zero_touch_logs/errors/test_update_message_20260503_094312_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_update_message
Failed at: 20260503_094312
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_delete_message`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_delete_message_20260503_094342.png](../../zero_touch_logs/errors/test_delete_message_20260503_094342.png)

**Zero-touch error log:** [`test_delete_message_20260503_094342_logs.txt`](../../zero_touch_logs/errors/test_delete_message_20260503_094342_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_delete_message
Failed at: 20260503_094342
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_create_environment`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_create_environment_20260503_094412.png](../../zero_touch_logs/errors/test_create_environment_20260503_094412.png)

**Zero-touch error log:** [`test_create_environment_20260503_094412_logs.txt`](../../zero_touch_logs/errors/test_create_environment_20260503_094412_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_create_environment
Failed at: 20260503_094412
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_update_environment`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_update_environment_20260503_094443.png](../../zero_touch_logs/errors/test_update_environment_20260503_094443.png)

**Zero-touch error log:** [`test_update_environment_20260503_094443_logs.txt`](../../zero_touch_logs/errors/test_update_environment_20260503_094443_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_update_environment
Failed at: 20260503_094443
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```

#### ❌ `TestPortalClient::test_delete_environment`

**Error:** `playwright._impl._errors.TimeoutError: Locator.click: Timeout 30000ms exceeded.`

![test_delete_environment_20260503_094513.png](../../zero_touch_logs/errors/test_delete_environment_20260503_094513.png)

**Zero-touch error log:** [`test_delete_environment_20260503_094513_logs.txt`](../../zero_touch_logs/errors/test_delete_environment_20260503_094513_logs.txt)

```
Test     : tests/test_zira.py::TestPortalClient::test_delete_environment
Failed at: 20260503_094513
URL      : https://shob127.b2clogin.com/shob127.onmicrosoft.com/B2C_1_Zira-Test/api/CombinedSigninAndSignup/confirmed?rememberMe=false&csrf_token=ZmxjS29BMW1ycWhiYjhxRGJHTHp4ejltVGpDZ1FOU2hZSnZmd0RGUVF1QnFJZStkNWlNN1hQNU1ObHp6QUYwcmt3bHI1L013WFJGQkNPK0ZVMkNQNmc9PTsyMDI2LTA1LTAzVDA5OjM4OjA4LjU5Njc1Mlo7Q1dpOWdzOHJudHlpNzRWZkRzOGJzdz09O3siT3JjaGVzdHJhdGlvblN0ZXAiOjF9&tx=StateProperties=eyJUSUQiOiI4MDI3NTJhYS1mMzU4LTQxZGQtOTZjNC1iZDNjYjU4NDZkYzYifQ&p=B2C_1_Zira-Test&diags=%7B%22pageViewId%22%3A%227adc8227-4881-4c79-9eb0-5656c35e7d6b%22%2C%22pageId%22%3A%22CombinedSigninAndSignup%22%2C%22trace%22%3A%5B%7B%22ac%22%3A%22T005%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A1%7D%2C%7B%22ac%22%3A%22T021%20-%20URL%3Ahttps%3A%2F%2Fzira-assets.dev.orangepeak.net%2Fzira-assets%2Fziralogin%2FLoginPage-zira.html%3Fui_locales%3Dhe%22%2C%22acST%22%3A1777801088%2C%22acD%22%3A391%7D%2C%7B%22ac%22%3A%22T019%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A3%7D%2C%7B%22ac%22%3A%22T004%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A2%7D%2C%7B%22ac%22%3A%22T003%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T030Online%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T035%22%2C%22acST%22%3A1777801089%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T002%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A0%7D%2C%7B%22ac%22%3A%22T018T010%22%2C%22acST%22%3A1777801090%2C%22acD%22%3A499%7D%5D%7D
======================================================================

==== Console Errors (0) ====
(none)

==== Console Warnings (0) ====
(none)

==== Page Exceptions (0) ====
(none)

==== Network Failures (HTTP >= 400) (0) ====
(none)

(no console errors/warnings, page exceptions, or HTTP >= 400 captured during this test)
```
