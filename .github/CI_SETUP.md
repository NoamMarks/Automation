# GitHub Actions Setup — Zira E2E

## What runs

[`.github/workflows/e2e-tests.yml`](workflows/e2e-tests.yml) runs `tests/run_multiple.py` on a clean Ubuntu runner, generates the consolidated Master Run Report, uploads everything as a workflow artifact, and emails a readable digest with the master report attached.

Triggers:
- **Manual** (`workflow_dispatch`) — you can override `NUM_RUNS` and `TEST_PATH` from the Actions tab.
- **Daily schedule** — every day at 06:00 UTC.
- **Push to `main`/`master`** — every commit.

## Required repository secrets

Go to **Settings → Secrets and variables → Actions → New repository secret** and add each of the following:

### Application credentials
| Secret | Value |
|---|---|
| `APP_URL` | Base URL of the dev environment, e.g. `https://front-zira.dev.orangepeak.net` |
| `APP_USERNAME` | Admin user (matches local `.env`) |
| `APP_PASSWORD` | Admin password |
| `MOD_USERNAME` | Moderator user (currently used by `test_mod_security`, which has a known import bug — kept failing on purpose) |
| `MOD_PASSWORD` | Moderator password |

### Email reporting
| Secret | Value |
|---|---|
| `EMAIL_USERNAME` | Gmail address that will send the digest (e.g. `ci-bot@yourdomain.com`) |
| `EMAIL_PASSWORD` | **Gmail App Password** — NOT the account password. Generate at https://myaccount.google.com/apppasswords (requires 2FA on the account first). |
| `EMAIL_TO` | Comma-separated recipient list, e.g. `qa@team.com,lead@team.com` |

### Optional
- Switch SMTP provider by editing the `server_address` / `server_port` in the workflow (e.g. Outlook: `smtp.office365.com:587`, custom: your SMTP host).

## What you get per run

In your inbox:
- **Subject line** like `[Zira E2E #42] ✅ 106/113 passed (0 failed, 2 skipped, 5 errors)` — at-a-glance status.
- **Body** — markdown digest (rendered as HTML by the action): aggregate pass rate, summary table, stability index of failed tests, list of skipped tests.
- **Attachments**:
  - `Master_Run_Report_<TIMESTAMP>.md` — the full consolidated report.
  - `run_<N>_report.html` — pytest-html visual report (per run, self-contained — opens in any browser).
  - `run_<N>_junit.xml` — machine-readable test results.

In the Actions tab → workflow run → Artifacts:
- `e2e-reports-run-<N>` — full bundle including `reports/master/` AND `zero_touch_logs/` (screenshots + console/network error logs from any failed tests).
- 30-day retention by default; adjust in the workflow's `retention-days` field if needed.

## How to test the workflow without committing

1. Push the workflow file to a branch.
2. Go to **Actions → E2E Tests → Run workflow** (workflow_dispatch).
3. Override `num_runs=1` and `test_path=tests/test_admin_grid_controls.py` for a quick (~2 min) smoke verification.
4. Check the run logs and your inbox. After the first successful run, switch back to defaults.

## Local sanity check (matches what CI runs)

```powershell
$env:NUM_RUNS="1"; .\.venv\Scripts\python.exe tests\run_multiple.py
.\.venv\Scripts\python.exe utils\email_summary.py
```

Inspect `reports/master/email_body.md` — that's exactly what the email will contain.

## Notes on environment

- Runner is `ubuntu-latest`. Browser is **Chromium**, installed by `python -m playwright install --with-deps chromium`.
- `HEADLESS=1` is forced in CI; our custom `page` fixture (in `tests/conftest.py`) honors that env var.
- `pytest.ini` has `--headed` for local development; that flag targets pytest-playwright's own fixtures (which we don't use), so it's a harmless no-op in CI.
- The dev URL must be reachable from GitHub-hosted runners. If the environment is behind a VPN / private network, switch `runs-on` to a self-hosted runner with appropriate access.

## Known signal in CI today

After our local dry-run verification, the CI baseline will show:
- **5 errors** in `test_mod_security.py` — pre-existing missing `import os` in that test file. Intentionally left in place as a "known broken" signal.
- **2 skips** in `test_admin_grid_controls.py` — documented feature gaps (admin search + sort not present in the UI).

Anything beyond those should be treated as a regression worth investigating.
