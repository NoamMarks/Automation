"""
Permission-boundary tests via direct URL manipulation.

`test_mod_security` verifies that admin-only buttons are visually hidden
from a moderator. That is UX-level, not authorization-level — a user
with knowledge of the admin URLs could still reach those routes.

This file exercises the real authorization boundary: log in as a
moderator, force-navigate to admin-only URLs (Environments and Domains/
Content-Worlds), and assert that no admin-only edit affordance is
reachable. The acceptable outcomes are:

  REDIRECTED     — the moderator was bounced off the admin URL
  BLOCKED        — explicit '403 / no permission' content was rendered
  EMPTY_SHELL    — the route loaded but no admin controls are present
  ALLOWED_WITH_CONTROLS  — security breach (test FAILS)

The moderator must NOT see the create/add buttons under any circumstance.
"""

import os
import time

import pytest


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

MOD_USERNAME = os.getenv("MOD_USERNAME", "ZiraMod")
MOD_PASSWORD = os.getenv("MOD_PASSWORD", "123123")

# Hebrew/English keywords indicating an explicit "no permission" state
DENIAL_KEYWORDS = (
    "403", "404",
    "אין לך הרשאה",   # 'you don't have permission' (Hebrew)
    "permission",
    "forbidden",
    "unauthorized",
    "not authorized",
    "אין הרשאה",
)


def _login_as_moderator(page):
    """Log in via the standard login flow with moderator credentials."""
    page.goto(APP_URL)
    try:
        page.get_by_role("button", name="הבנתי").click(timeout=3000)
    except Exception:
        pass
    page.get_by_text("התחבר").click()
    # Wait for the B2C form to load
    page.locator("#pretty-username").wait_for(state="visible", timeout=15000)
    page.locator("#pretty-username").fill(MOD_USERNAME)
    page.locator("#pretty-password").fill(MOD_PASSWORD)
    page.locator("button.button-submit").click()
    # Moderator typically lands on /links per existing test_mod_security
    try:
        page.wait_for_url("**/links**", timeout=10000)
    except Exception:
        page.wait_for_timeout(3000)


def _classify_outcome(page, target_url_fragment, admin_create_button_name):
    """Return one of REDIRECTED / BLOCKED / EMPTY_SHELL / ALLOWED_WITH_CONTROLS."""
    final_url = page.url
    body_text = ""
    try:
        body_text = page.locator("body").inner_text()
    except Exception:
        pass
    body_lower = body_text.lower()

    # 1) URL bounced away from the admin route?
    if target_url_fragment not in final_url:
        return "REDIRECTED", final_url, body_text

    # 2) Explicit denial content rendered?
    if any(kw.lower() in body_lower for kw in DENIAL_KEYWORDS):
        return "BLOCKED", final_url, body_text

    # 3) Are admin-only create controls visible?
    btn = page.get_by_role("button", name=admin_create_button_name)
    try:
        if btn.count() > 0 and btn.first.is_visible():
            return "ALLOWED_WITH_CONTROLS", final_url, body_text
    except Exception:
        pass

    return "EMPTY_SHELL", final_url, body_text


@pytest.fixture(scope="class")
def sec_data():
    return {}


class TestSecurityRouting:
    """Direct-URL authorization boundary tests for the moderator role."""

    def test_01_login_as_moderator(self, page, sec_data):
        print("\n[sec] logging in as moderator...")
        _login_as_moderator(page)
        post_login_url = page.url
        print(f"[sec] post-login URL: {post_login_url}")
        sec_data["post_login_url"] = post_login_url

        # Sanity check: the homepage's admin-only sidebar buttons should be
        # invisible to the moderator (the existing test_mod_security
        # assertion). If this fails, our login didn't actually use mod creds.
        for label in ("עולמות תוכן", "סביבות"):
            btn = page.get_by_role("button", name=label)
            visible = btn.count() > 0 and btn.first.is_visible()
            print(f"[sec]   sidebar button {label!r} visible: {visible}")
            assert not visible, (
                f"Sanity-check failed: sidebar button {label!r} is visible "
                f"to the moderator. Either mod creds are wrong or the role "
                f"already grants admin UI."
            )

    def test_02_environments_url_blocked(self, page, sec_data):
        target = "/admin/environments"
        url = APP_URL.rstrip("/") + target
        print(f"\n[sec] >>> moderator force-navigating to {url}")

        page.goto(url, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        outcome, final_url, body = _classify_outcome(
            page, target, "הוספת סביבה"
        )
        sec_data["envs_outcome"] = outcome
        sec_data["envs_final_url"] = final_url
        print(f"[sec]   final URL : {final_url}")
        print(f"[sec]   outcome   : {outcome}")
        # Print a small body snippet for diagnostics
        snippet = body.strip().replace("\n", " | ")[:160]
        print(f"[sec]   body[:160]: {snippet!r}")

        assert outcome != "ALLOWED_WITH_CONTROLS", (
            f"SECURITY BREACH: moderator can see the admin-only "
            f"'הוספת סביבה' button at {final_url}"
        )
        # Any of the three protective outcomes is acceptable
        assert outcome in ("REDIRECTED", "BLOCKED", "EMPTY_SHELL"), (
            f"Unexpected outcome {outcome!r} for {target}"
        )

    def test_03_domains_url_blocked(self, page, sec_data):
        # Try both common path conventions — content-worlds is the spec'd
        # term in the UI but '/admin/domains' is the user-requested target.
        candidates = ["/admin/domains", "/admin/content-worlds"]
        results = []
        for target in candidates:
            url = APP_URL.rstrip("/") + target
            print(f"\n[sec] >>> moderator force-navigating to {url}")
            page.goto(url, wait_until="domcontentloaded")
            page.wait_for_timeout(3000)
            outcome, final_url, body = _classify_outcome(
                page, target, "הוספת עולם תוכן"
            )
            print(f"[sec]   final URL : {final_url}")
            print(f"[sec]   outcome   : {outcome}")
            snippet = body.strip().replace("\n", " | ")[:160]
            print(f"[sec]   body[:160]: {snippet!r}")
            results.append((target, outcome, final_url))

        sec_data["domains_results"] = results
        # CRITICAL: at NO admin-domain URL may the moderator see the create
        # button. (Every candidate path must be safely guarded.)
        breaches = [r for r in results if r[1] == "ALLOWED_WITH_CONTROLS"]
        assert not breaches, (
            f"SECURITY BREACH: moderator can see 'הוספת עולם תוכן' "
            f"at one or more admin-domain URLs: {breaches}"
        )

    def test_04_summary(self, sec_data):
        print("\n" + "=" * 60)
        print("[sec] SECURITY ROUTING SUMMARY")
        print("=" * 60)
        print(f"[sec]   post-login URL    : {sec_data.get('post_login_url')}")
        print(f"[sec]   /admin/environments: {sec_data.get('envs_outcome')} "
              f"@ {sec_data.get('envs_final_url')}")
        for target, outcome, final_url in sec_data.get("domains_results", []):
            print(f"[sec]   {target:<24}: {outcome} @ {final_url}")
        print("=" * 60)
