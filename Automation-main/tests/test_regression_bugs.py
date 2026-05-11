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


def _short_id():
    return uuid.uuid4().hex[:6]


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
    # BUG-3: new env missing from the env-switcher dialog until refresh
    # ----------------------------------------------------------
    def test_bug_03_new_env_visible_in_links_without_refresh(self, page):
        """BUG-3: After creating a new env, navigating to the Links page
        (no browser refresh) and opening the 'שינוי סביבה' (Change
        environment) dialog from the header should immediately list the
        new env. The bug is that the frontend caches the env list and
        doesn't include the new env until the user manually reloads.

        Repro:
          1. Navigate to Environments and create a new env
          2. Navigate to Links via the sidebar (no F5)
          3. Click the 'שינוי סביבה' button in the page header to open
             the env-picker dialog
          4. Assert the new env name appears in that dialog
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
        page.wait_for_timeout(2500)

        # Open the env-switcher dialog from the header
        print(f"[reg/bug-03] opening 'שינוי סביבה' dialog")
        page.get_by_role("button", name="שינוי סביבה").click()
        page.wait_for_timeout(1500)

        dialog = page.locator("[role='dialog']").last
        dialog_text = ""
        if dialog.count() > 0 and dialog.is_visible():
            dialog_text = dialog.inner_text()
        new_env_present = env_name in dialog_text
        print(f"[reg/bug-03] {env_name!r} listed in env-switcher dialog: "
              f"{new_env_present}")

        # Cleanup BEFORE assertion so test data is gone even on failure.
        # The env-switcher dialog is modal and its backdrop blocks the
        # sidebar — Escape sometimes doesn't dismiss it cleanly. We do a
        # hard URL navigation to bypass any leftover modal state. This
        # is AFTER `new_env_present` was already captured, so it does not
        # interfere with the bug-3 assertion (which is about NOT having
        # to refresh BEFORE the dialog is read).
        try:
            page.goto(APP_URL.rstrip("/") + "/admin/environments",
                      wait_until="domcontentloaded")
            page.wait_for_timeout(2500)
            envs.click_delete_on_row(env_name)
            envs.click_delete_and_confirm()
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"[reg/bug-03] cleanup raised (non-fatal): "
                  f"{type(e).__name__}: {e}")

        assert new_env_present, (
            f"BUG-3: newly-created env {env_name!r} is missing from the "
            f"env-switcher dialog (opened from the Links page header) "
            f"without a manual browser refresh. The frontend env list "
            f"is stale."
        )

    # ----------------------------------------------------------
    # BUG-4: incomplete link propagation on env create
    # ----------------------------------------------------------
    def test_bug_04_env_create_propagates_to_all_links(self, page):
        """BUG-4: Creating a new env should attach EVERY existing link
        on the admin Links page to it. The backend was reported to drop
        a non-deterministic subset.

        UI-based check (matches what an admin manually verifies):
          1. Create the new env via the admin UI
          2. Hard-refresh the Links page (so we read fresh data and
             isolate this test from BUG-3's caching staleness)
          3. For every visible link row, confirm the new env appears in
             that row's env-chip column — either as a directly-rendered
             chip or inside the '+N' expand tooltip
          4. All visible rows must include the new env → 100% propagation
        """
        suffix = _short_id()
        env_name = f"RegBug4Env{suffix}"
        env_param = f"regbug4{suffix}"

        # Step 1 — create the env via UI
        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        envs_page = EnvironmentsPage(page)
        print(f"\n[reg/bug-04] creating env {env_name!r}")
        envs_page.create_environment(env_name, env_param)
        envs_page.click_save_and_confirm()
        page.wait_for_timeout(2500)
        envs_page.verify_environment_visible(env_name)

        # Step 2 — go to Links page and hard-refresh so we see fresh data.
        # (BUG-3 covers the caching/staleness path; this test is about
        # propagation specifically, so we explicitly reload to remove
        # caching as a confound.)
        NavigationPage(page).go_to_links()
        page.wait_for_timeout(1500)
        page.reload()
        page.wait_for_timeout(3000)

        # Step 3 — for every visible link row, check whether the new env
        # is reflected in its env-chip column. The admin Links page shows
        # one of two things in that column:
        #
        #   (a) the special "כל הסביבות" ("All environments") chip — meaning
        #       the link is attached to every env in the system, including
        #       the one we just created  → propagation OK
        #   (b) a list of specific env-name chips — meaning the link is
        #       attached only to those envs. To pass, the new env name
        #       must appear in this list  → propagation OK
        #
        # If a row shows specific chips that do NOT include the new env,
        # propagation failed for that row.
        ALL_ENVS_LABEL = "כל הסביבות"
        rows = page.locator("[class*='SingleLinkstyled__StyledAdminLink']")
        n_rows = rows.count()
        print(f"\n[reg/bug-04] inspecting {n_rows} admin link rows for "
              f"{env_name!r} or the 'all-envs' marker")

        missing = []
        for i in range(n_rows):
            row = rows.nth(i)
            container = row.locator(
                "[class*='LinkEnvironmentsContainer']"
            )
            if container.count() == 0:
                continue  # header row / non-data row
            try:
                env_text = container.first.inner_text()
            except Exception as e:
                print(f"[reg/bug-04] could not read row {i} env text: "
                      f"{type(e).__name__}: {e}")
                continue
            if ALL_ENVS_LABEL in env_text or env_name in env_text:
                continue  # propagation reflected in UI for this row
            try:
                name = row.locator(
                    "[class*='StyledLinkName']"
                ).first.inner_text().strip()
            except Exception:
                name = f"<row {i}>"
            missing.append(name)

        print(f"[reg/bug-04] propagation reflected in UI for "
              f"{n_rows - len(missing)} of {n_rows} rows; "
              f"missing from {len(missing)} row(s)")

        # Step 4 — cleanup BEFORE assertion (so test data is removed even
        # if the assertion below fails)
        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        try:
            envs_page.click_delete_on_row(env_name)
            envs_page.click_delete_and_confirm()
            page.wait_for_timeout(1500)
        except Exception as e:
            print(f"[reg/bug-04] cleanup raised (non-fatal): "
                  f"{type(e).__name__}: {e}")

        # Assertion: every visible link row must show either the
        # all-envs marker or the new env name in its env-chip column.
        assert not missing, (
            f"BUG-4: env {env_name!r} did not propagate to "
            f"{len(missing)} of {n_rows} visible link rows on the admin "
            f"Links page. Missing from: {missing[:10]}"
        )
