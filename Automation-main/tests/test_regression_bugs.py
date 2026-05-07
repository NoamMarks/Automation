"""
Regression tests for known open bugs.

Each test in this file maps 1:1 to a documented bug ticket. The test
asserts the EXPECTED correct behavior, so it FAILS while the bug is open
and PASSES once the bug is fixed. That's exactly how a regression marker
should work — when the test starts passing again, you know the fix
landed.

Bugs covered (as of 2026-05-07):
  BUG-1  Delete env fails (HTTP 500) when initiated immediately after
         creating another env.
  BUG-2  Admin preview popup shows ALL messages including inactive ones
         (should show only active).
  BUG-3  Newly-created env is missing from the Links page env combobox
         until the page is manually refreshed.
  BUG-4  Env-create non-deterministically fails to propagate to all
         existing links (random subset is dropped).

Each test is independent and cleans up its own test data. Names use a
'RegBug<N>' prefix so they're easy to identify and clean up manually if
a test crashes mid-flight.
"""

import os
import uuid

import pytest

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.environments_page import EnvironmentsPage
from pages.messages_page import MessagesPage


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")
BACKEND_HOST = "zira-backend.dev.orangepeak.net"


def _short_id():
    return uuid.uuid4().hex[:6]


def _backend_get_links(page):
    """Fetch all links via the page's authenticated session. Returns list."""
    body = page.evaluate(
        """async (host) => {
            const r = await fetch('https://' + host + '/api/links', {credentials: 'include'});
            return r.json();
        }""",
        BACKEND_HOST,
    )
    if isinstance(body, list):
        return body
    if isinstance(body, dict):
        return body.get("links", [])
    return []


def _backend_get_envs(page):
    body = page.evaluate(
        """async (host) => {
            const r = await fetch('https://' + host + '/api/environments', {credentials: 'include'});
            return r.json();
        }""",
        BACKEND_HOST,
    )
    if isinstance(body, list):
        return body
    if isinstance(body, dict):
        return body.get("environments", [])
    return []


def _link_attached_to(link, env_id):
    for e in (link.get("environments") or []):
        eid = e.get("_id") if isinstance(e, dict) else e
        if eid == env_id:
            return True
    return False


@pytest.fixture(scope="class")
def reg_data():
    return {}


class TestKnownRegressions:
    """Regression markers for documented open bugs.

    Tests are expected to FAIL while the corresponding bug is open. Each
    test name encodes the bug ID for easy triage in the run report.
    """

    # ----------------------------------------------------------
    # Setup
    # ----------------------------------------------------------
    def test_00_login(self, page):
        print("\n[reg] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

    # ----------------------------------------------------------
    # BUG-1: delete-after-create returns HTTP 500
    # ----------------------------------------------------------
    def test_bug_01_delete_env_after_create(self, page):
        """BUG-1: Delete env fails (HTTP 500) when triggered immediately
        after creating another env.

        Repro: create env A, then within a fraction of a second click
        Delete on env B and confirm. The bug is that env B's deletion
        fails server-side. This test asserts env B is actually gone after
        the delete-confirm flow completes.
        """
        suffix = _short_id()
        trigger_name = f"RegBug1Trigger{suffix}"
        trigger_param = f"regbug1t{suffix}"
        victim_name = f"RegBug1Victim{suffix}"
        victim_param = f"regbug1v{suffix}"

        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        envs = EnvironmentsPage(page)

        # Pre-step: create the victim env (this one we expect to delete in
        # the bug-repro phase). Use the standard CRUD path.
        print(f"\n[reg/bug-01] pre: create victim env {victim_name!r}")
        envs.create_environment(victim_name, victim_param)
        envs.click_save_and_confirm()
        page.wait_for_timeout(1500)
        envs.verify_environment_visible(victim_name)

        # Trigger: create another env. The bug is that the next mutation
        # within a short window after this returns 500.
        print(f"[reg/bug-01] trigger: create env {trigger_name!r}")
        envs.create_environment(trigger_name, trigger_param)
        envs.click_save_and_confirm()
        # Intentionally do NOT pause here — the bug fires when the next
        # mutation hits the backend immediately.
        print(f"[reg/bug-01] repro: delete victim {victim_name!r} immediately")
        try:
            envs.click_delete_on_row(victim_name)
            envs.click_delete_and_confirm()
        except Exception as e:
            print(f"[reg/bug-01] delete UI step raised: {type(e).__name__}: {e}")
            # Fall through — the assertion below is what fails the test.

        page.wait_for_timeout(2500)

        # Assert: victim is no longer in the env list. If the bug is
        # present, the delete returned 500 and the row is still there.
        envs.verify_environment_not_attached(victim_name)

        # Cleanup: remove the trigger env we created.
        try:
            envs.click_delete_on_row(trigger_name)
            envs.click_delete_and_confirm()
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"[reg/bug-01] cleanup of trigger raised "
                  f"(non-fatal): {type(e).__name__}: {e}")

    # ----------------------------------------------------------
    # BUG-2: preview popup shows inactive messages
    # ----------------------------------------------------------
    def test_bug_02_preview_hides_inactive_messages(self, page):
        """BUG-2: The admin 'תצוגה מקדימה פופ אפ' (preview popup) lists
        inactive messages alongside active ones.

        Repro: create one active and one inactive message; open the
        preview popup; the popup should contain ONLY the active one.
        """
        suffix = _short_id()
        active_name = f"RegBug2Active{suffix}"
        inactive_name = f"RegBug2Inactive{suffix}"

        NavigationPage(page).go_to_messages()
        page.wait_for_timeout(1500)
        msgs = MessagesPage(page)

        print(f"\n[reg/bug-02] creating active message {active_name!r}")
        msgs.create_message(active_name, "regression-test active message")
        # Default status is active — leave the switch alone.
        msgs.click_save_and_confirm()
        page.wait_for_timeout(1500)

        print(f"[reg/bug-02] creating INACTIVE message {inactive_name!r}")
        msgs.create_message(inactive_name, "regression-test inactive message")
        # Toggle status off so it's saved as inactive.
        msgs.toggle_status()
        msgs.click_save_and_confirm()
        page.wait_for_timeout(1500)

        # Open the admin preview popup
        print(f"[reg/bug-02] opening preview popup")
        msgs.click_preview()
        page.wait_for_timeout(2000)

        # Read every visible message-name node inside the open popup. We
        # capture the page's full visible text and check by substring,
        # which sidesteps depending on the popup's exact DOM structure.
        body_text = page.locator("body").inner_text()

        active_present = active_name in body_text
        inactive_present = inactive_name in body_text
        print(f"[reg/bug-02] active visible in popup  : {active_present}")
        print(f"[reg/bug-02] inactive visible in popup: {inactive_present}")

        # Try to close the popup before asserting / cleaning up
        for label in ("הבנתי", "אישור"):
            try:
                btn = page.get_by_role("button", name=label).first
                if btn.count() > 0 and btn.is_visible():
                    btn.click(timeout=2000)
                    page.wait_for_timeout(500)
                    break
            except Exception:
                continue

        # Cleanup BEFORE assertion so test data is removed even on fail
        for name in (active_name, inactive_name):
            try:
                msgs.delete_message(name)
                msgs.click_delete_and_confirm()
                page.wait_for_timeout(1500)
            except Exception as e:
                print(f"[reg/bug-02] cleanup of {name!r} raised "
                      f"(non-fatal): {type(e).__name__}: {e}")

        # Assertions
        assert active_present, (
            f"Active message {active_name!r} should be visible in the "
            f"preview popup but was not."
        )
        assert not inactive_present, (
            f"BUG-2: inactive message {inactive_name!r} appears in the "
            f"preview popup but should be hidden."
        )

    # ----------------------------------------------------------
    # BUG-3: new env missing from Links page env-chip area until refresh
    # ----------------------------------------------------------
    def test_bug_03_new_env_visible_in_links_without_refresh(self, page):
        """BUG-3: After creating a new env on the Environments page,
        navigating to the Links page (no browser refresh) should
        immediately show the new env in each link's env-chip area
        (the visible chips OR the '+N' tooltip that expands the rest).

        The bug is that the Links page renders stale link data and does
        NOT include the new env until the user manually reloads the
        browser. Refresh fetches a fresh link list; sidebar-nav alone
        re-uses the cached one.

        Repro:
          1. Navigate to envs, create new env
          2. Navigate to Links via the sidebar (no F5)
          3. Inspect every link's env-chip column, expanding all '+N'
             tooltips, and assert the new env name appears
        """
        suffix = _short_id()
        env_name = f"RegBug3Env{suffix}"
        env_param = f"regbug3{suffix}"

        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        envs = EnvironmentsPage(page)

        print(f"\n[reg/bug-03] creating env {env_name!r}")
        envs.create_environment(env_name, env_param)
        envs.click_save_and_confirm()
        page.wait_for_timeout(1500)
        envs.verify_environment_visible(env_name)

        # CRITICAL: do NOT page.reload() — that's the workaround we are
        # testing against. The bug is precisely that the user must
        # refresh; the test asserts they shouldn't have to.
        print(f"[reg/bug-03] navigating to Links via sidebar (no refresh)")
        NavigationPage(page).go_to_links()
        page.wait_for_timeout(3000)

        # Collect every env name surfaced by the Links page:
        #   (a) directly-rendered env chips in each link row
        #   (b) tooltips revealed by clicking each '+N' expand button
        seen_text_parts = []

        # (a) Visible chips on each link row. The chip column lives in
        # `LinkEnvironmentsContainer`; each chip is a `SingleLinkEnvironment`.
        try:
            seen_text_parts.append(
                page.locator("[class*='LinkEnvironmentsContainer']")
                    .all_inner_texts()
            )
        except Exception as e:
            print(f"[reg/bug-03] could not read chip containers: "
                  f"{type(e).__name__}: {e}")

        # (b) Click every visible '+N' button and grab its tooltip
        plus_buttons = page.locator(
            "[class*='AdditionalEnvironmentsButton']"
        ).all()
        print(f"[reg/bug-03] found {len(plus_buttons)} '+N' expand buttons")
        for i, btn in enumerate(plus_buttons[:10]):  # cap for speed
            try:
                btn.scroll_into_view_if_needed(timeout=2000)
                btn.click(timeout=2000)
                page.wait_for_timeout(500)
                tip = page.locator("[role='tooltip']").last
                if tip.count() > 0 and tip.is_visible():
                    seen_text_parts.append([tip.inner_text()])
                # Close tooltip — click body away from button
                page.keyboard.press("Escape")
                page.wait_for_timeout(200)
            except Exception as e:
                print(f"[reg/bug-03] +N #{i} click failed (non-fatal): "
                      f"{type(e).__name__}: {e}")

        # Flatten everything to one searchable blob
        seen_text = "\n".join(
            line for chunk in seen_text_parts for line in chunk
        )
        new_env_present = env_name in seen_text
        print(f"[reg/bug-03] {env_name!r} visible in Links page env-chip "
              f"UI (chips + tooltips): {new_env_present}")

        # Cleanup BEFORE assertion so test data is gone even on failure
        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        try:
            envs.click_delete_on_row(env_name)
            envs.click_delete_and_confirm()
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"[reg/bug-03] cleanup raised (non-fatal): "
                  f"{type(e).__name__}: {e}")

        assert new_env_present, (
            f"BUG-3: newly-created env {env_name!r} is missing from the "
            f"Links page env-chip UI (visible chips + '+N' tooltips) "
            f"without a manual browser refresh. The frontend is showing "
            f"stale link data."
        )

    # ----------------------------------------------------------
    # BUG-4: incomplete link propagation on env create
    # ----------------------------------------------------------
    def test_bug_04_env_create_propagates_to_all_links(self, page):
        """BUG-4: Creating a new env should attach every existing link
        to it. The backend non-deterministically drops a subset.

        Repro: snapshot the current link count, create an env, then
        re-fetch links and count how many are attached to the new env.
        The two counts should match.
        """
        suffix = _short_id()
        env_name = f"RegBug4Env{suffix}"
        env_param = f"regbug4{suffix}"

        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        envs_page = EnvironmentsPage(page)

        # Snapshot expected link count BEFORE we trigger
        links_before = _backend_get_links(page)
        expected = len(links_before)
        print(f"\n[reg/bug-04] expected link count to propagate: {expected}")

        print(f"[reg/bug-04] creating env {env_name!r}")
        envs_page.create_environment(env_name, env_param)
        envs_page.click_save_and_confirm()
        page.wait_for_timeout(2500)
        envs_page.verify_environment_visible(env_name)

        # Find the new env's _id by re-querying envs
        all_envs = _backend_get_envs(page)
        new_env = next((e for e in all_envs if e.get("name") == env_name), None)
        assert new_env, f"could not find {env_name!r} in env list after create"
        new_env_id = new_env["_id"]

        # Re-fetch links and count attachments
        links_after = _backend_get_links(page)
        attached = sum(1 for l in links_after if _link_attached_to(l, new_env_id))
        missing_names = [
            l.get("name") for l in links_after
            if not _link_attached_to(l, new_env_id)
        ]
        print(f"[reg/bug-04] links attached to {env_name!r}: "
              f"{attached} / {len(links_after)}")
        if missing_names:
            print(f"[reg/bug-04] sample missing names (first 10): "
                  f"{missing_names[:10]}")

        # Cleanup BEFORE assertion
        try:
            envs_page.click_delete_on_row(env_name)
            envs_page.click_delete_and_confirm()
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"[reg/bug-04] cleanup raised (non-fatal): "
                  f"{type(e).__name__}: {e}")

        # Assertion: every link present at create-time is now attached.
        # We compare against the BEFORE count, since links_after may have
        # additional links if anything else mutated meanwhile (defensive).
        assert attached >= expected, (
            f"BUG-4: env {env_name!r} only got {attached} of {expected} "
            f"existing links propagated. Missing {expected - attached} "
            f"links — sample: {missing_names[:5]}"
        )
