"""
Send a post-run email with the summary + dashboard attached.

Configured via environment variables (set in `.env` so credentials
never enter source control):

    EMAIL_FROM   sender address (e.g. yourname@gmail.com)
    EMAIL_PASS   sender password — for Gmail use an APP PASSWORD,
                 not the account password; create at
                 https://myaccount.google.com/apppasswords
    EMAIL_TO     recipient address (or comma-separated list)
    SMTP_HOST    optional; default 'smtp.gmail.com'
    SMTP_PORT    optional; default 587 (STARTTLS)

If any of EMAIL_FROM / EMAIL_PASS / EMAIL_TO are missing, the function
silently no-ops with a single line of stdout — running the suite never
fails because of email config.
"""

import mimetypes
import os
import smtplib
import ssl
import xml.etree.ElementTree as ET
from email.message import EmailMessage
from datetime import datetime


def _parse_junit_summary(junit_path):
    """Return dict with tests/passed/failed/skipped/duration. None if unparseable."""
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
            "failed": failures + errors,
            "skipped": skipped,
            "duration": float(suite.attrib.get("time", 0)),
        }
    except Exception:
        return None


def _fmt_duration(seconds):
    if seconds < 60:
        return f"{seconds:.0f}s"
    m, s = divmod(int(seconds), 60)
    if m < 60:
        return f"{m}m {s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m"


def _aggregate(runs):
    """Sum counts across runs."""
    out = {"tests": 0, "passed": 0, "failed": 0, "skipped": 0, "duration": 0.0}
    for run in runs:
        s = _parse_junit_summary(run.get("junit_path"))
        if s is None:
            continue
        for k in out:
            out[k] += s[k]
    return out


def _build_html_body(runs, agg, summary_path, dashboard_path):
    """Compact HTML email body — headline + KPIs + attachment note."""
    n_runs = len(runs)
    pass_rate = 0 if agg["tests"] == 0 else 100 * agg["passed"] / agg["tests"]
    status_color = "#00c853" if agg["failed"] == 0 else "#e53935"
    status_text = "ALL PASSING" if agg["failed"] == 0 else f"{agg['failed']} FAILING"
    summary_basename = os.path.basename(summary_path) if summary_path else ""
    dashboard_basename = os.path.basename(dashboard_path) if dashboard_path else ""

    return f"""<!DOCTYPE html>
<html>
<body style="font-family:-apple-system,Segoe UI,sans-serif;color:#222;
             background:#f6f7f9;margin:0;padding:24px;">
  <div style="max-width:600px;margin:0 auto;background:#fff;
              border-radius:10px;padding:24px;
              border:1px solid #e3e6ea;">

    <h1 style="margin:0 0 8px;font-size:22px;">Zira QA — run report</h1>
    <div style="color:#666;font-size:13px;margin-bottom:20px;">
      {datetime.now().strftime('%Y-%m-%d %H:%M')} ·
      {n_runs} run{'s' if n_runs != 1 else ''} ·
      total wall-clock {_fmt_duration(agg['duration'])}
    </div>

    <div style="background:{status_color};color:white;padding:12px 16px;
                border-radius:8px;font-weight:600;text-align:center;
                margin-bottom:20px;">
      {status_text} &middot; {pass_rate:.0f}% pass rate
    </div>

    <table style="width:100%;border-collapse:collapse;font-size:14px;
                  margin-bottom:20px;">
      <tr>
        <td style="padding:8px 0;border-bottom:1px solid #eee;">Total tests</td>
        <td style="padding:8px 0;border-bottom:1px solid #eee;
                   text-align:right;font-weight:600;">{agg['tests']}</td>
      </tr>
      <tr>
        <td style="padding:8px 0;border-bottom:1px solid #eee;color:#2e7d32;">Passed</td>
        <td style="padding:8px 0;border-bottom:1px solid #eee;
                   text-align:right;font-weight:600;color:#2e7d32;">{agg['passed']}</td>
      </tr>
      <tr>
        <td style="padding:8px 0;border-bottom:1px solid #eee;color:#c62828;">Failed</td>
        <td style="padding:8px 0;border-bottom:1px solid #eee;
                   text-align:right;font-weight:600;color:#c62828;">{agg['failed']}</td>
      </tr>
      <tr>
        <td style="padding:8px 0;color:#e65100;">Skipped</td>
        <td style="padding:8px 0;text-align:right;
                   font-weight:600;color:#e65100;">{agg['skipped']}</td>
      </tr>
    </table>

    <p style="font-size:13px;color:#444;line-height:1.5;">
      Attached to this email:
      <br>1. <strong>{dashboard_basename}</strong> — open in a browser for the
         visual dashboard (charts, KPIs, hover tooltips on every test)
      <br>2. <strong>{summary_basename}</strong> — plain-English summary
         readable by anyone
    </p>

    <p style="font-size:11px;color:#999;margin-top:24px;">
      Auto-generated by <code>tests/run_multiple.py</code>.
      To stop these emails: unset EMAIL_TO in <code>.env</code>.
    </p>
  </div>
</body>
</html>
"""


def send_run_email(runs, summary_path=None, dashboard_path=None,
                   master_path=None):
    """Send a post-run email if EMAIL_FROM / EMAIL_PASS / EMAIL_TO are set.

    No-ops cleanly if creds aren't configured. Errors are caught + logged
    but never raised — running the suite never fails because of email.
    """
    sender = os.getenv("EMAIL_FROM", "").strip()
    password = os.getenv("EMAIL_PASS", "").strip()
    recipients = os.getenv("EMAIL_TO", "").strip()
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com").strip()
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    if not (sender and password and recipients):
        print("[email] EMAIL_FROM / EMAIL_PASS / EMAIL_TO not set — "
              "skipping email send (this is a no-op, not a failure).")
        return None

    recipient_list = [r.strip() for r in recipients.split(",") if r.strip()]
    agg = _aggregate(runs)
    n_runs = len(runs)
    pass_rate = 0 if agg["tests"] == 0 else 100 * agg["passed"] / agg["tests"]

    # Subject
    when = datetime.now().strftime("%d-%b %H:%M")
    if agg["failed"]:
        prefix = f"[Zira QA] {agg['failed']} FAIL"
    else:
        prefix = "[Zira QA] all pass"
    subject = (f"{prefix} · {agg['passed']}/{agg['tests']} ({pass_rate:.0f}%) · "
               f"{n_runs} run{'s' if n_runs != 1 else ''} · {when}")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipient_list)

    plain_body = (
        f"Zira QA run report — {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"{n_runs} run(s), wall-clock {_fmt_duration(agg['duration'])}\n\n"
        f"{agg['passed']} passed / {agg['failed']} failed / "
        f"{agg['skipped']} skipped (out of {agg['tests']})\n"
        f"Pass rate: {pass_rate:.0f}%\n\n"
        f"Open the attached HTML dashboard for full details.\n"
    )
    msg.set_content(plain_body)
    msg.add_alternative(
        _build_html_body(runs, agg, summary_path, dashboard_path),
        subtype="html",
    )

    # Attachments — only the two the user asked for
    for path in (dashboard_path, summary_path):
        if not path or not os.path.exists(path):
            continue
        ctype, _ = mimetypes.guess_type(path)
        if ctype is None:
            ctype = "application/octet-stream"
        maintype, subtype = ctype.split("/", 1)
        with open(path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype=maintype, subtype=subtype,
                filename=os.path.basename(path),
            )

    try:
        ctx = ssl.create_default_context()
        with smtplib.SMTP(smtp_host, smtp_port, timeout=30) as smtp:
            smtp.ehlo()
            smtp.starttls(context=ctx)
            smtp.ehlo()
            smtp.login(sender, password)
            smtp.send_message(msg)
        print(f"[email] sent to {len(recipient_list)} recipient(s) "
              f"via {smtp_host}: {subject}")
        return subject
    except Exception as e:
        print(f"[email] FAILED to send via {smtp_host}: "
              f"{type(e).__name__}: {e}")
        return None
