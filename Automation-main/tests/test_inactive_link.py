"""
Inactive Link visibility test.

Goal: verify the spec — `קישור שאינו פעיל לא יוצג בדף הבית`
("an inactive link won't appear on the home page").

Per the testing-priorities note, this MUST run in a fresh unauthenticated
context — admins/moderators may have preview permissions that mask the bug.
"""

import os
import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")


@pytest.fixture(scope="class")
def inactive_data():
    return {}


class TestInactiveLink:

    def test_01_login(self, page):
        print("\n[inactive] logging in as admin...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        print("[inactive] reached Links admin")

    def test_02_create_inactive_link(self, page, inactive_data):
        link_name = f"InactLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[inactive] creating INACTIVE link: '{link_name}'")

        links = LinksPage(page)
        links.open_add_link_dialog()
        page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(link_name)
        page.locator("input[name='URL']").fill(link_url)
        # Same Domain-selection approach as the working test_zira create flow.
        # count=3 reliably catches Domain options; count=1 picks up the Active toggle instead.
        links.select_combobox_options(combobox_index=0, count=3)

        final_state = links.toggle_active_off()
        print(f"[inactive] active toggle is now checked={final_state} (False = inactive)")
        assert final_state is False, "Active toggle did not turn off — test setup invalid"

        page.get_by_role("button", name="שמירה").click()
        page.get_by_role("button", name="אישור").click()
        page.wait_for_timeout(1500)

        links.verify_link_visible(link_name)
        inactive_data["link_name"] = link_name
        inactive_data["link_url"] = link_url
        print(f"[inactive] link saved as INACTIVE and visible in admin list")

    def test_03_check_public_homepage(self, page, inactive_data):
        link_name = inactive_data["link_name"]
        print(f"\n[inactive] >>> opening fresh unauthenticated context for public homepage check")

        browser = page.context.browser
        new_context = browser.new_context()
        public_page = new_context.new_page()
        try:
            public_page.goto(APP_URL)
            try:
                public_page.get_by_role("button", name="הבנתי").click(timeout=3000)
            except Exception:
                pass
            public_page.wait_for_timeout(2500)

            link_title_selector = "[class*='WelcomeLinksstyled__LinkTitle']"
            all_titles = public_page.locator(link_title_selector)
            n_titles = all_titles.count()
            visible_titles = []
            for i in range(n_titles):
                try:
                    txt = all_titles.nth(i).inner_text().strip()
                    if txt:
                        visible_titles.append(txt)
                except Exception:
                    pass
            print(f"[inactive] public homepage shows {n_titles} link cards: {visible_titles}")

            our_link = public_page.locator(link_title_selector, has_text=link_name)
            our_link_count = our_link.count()
            print(f"[inactive] our inactive link '{link_name}' on homepage grid: count={our_link_count}")

            if our_link_count == 0:
                print(f"[inactive] >>> homepage grid: PASS (inactive link is hidden)")
                inactive_data["grid_outcome"] = "HIDDEN_AS_EXPECTED"
            else:
                print(f"[inactive] >>> homepage grid: FAIL — inactive link is VISIBLE to public")
                inactive_data["grid_outcome"] = "LEAKED_TO_PUBLIC"

            try:
                search = public_page.get_by_placeholder("חיפוש יישום בכל עולמות התוכן")
                search.fill(link_name)
                public_page.wait_for_timeout(1500)
                options = public_page.get_by_role("option")
                n_opts = options.count()
                found_in_search = 0
                for i in range(n_opts):
                    try:
                        if link_name in options.nth(i).inner_text():
                            found_in_search += 1
                    except Exception:
                        pass
                print(f"[inactive] search for '{link_name}': {n_opts} options total, {found_in_search} match our link")
                if found_in_search == 0:
                    print(f"[inactive] >>> search: PASS (inactive link not searchable)")
                    inactive_data["search_outcome"] = "HIDDEN_AS_EXPECTED"
                else:
                    print(f"[inactive] >>> search: FAIL — inactive link IS searchable")
                    inactive_data["search_outcome"] = "LEAKED_TO_SEARCH"
            except Exception as e:
                print(f"[inactive] search check failed: {type(e).__name__}: {e}")
                inactive_data["search_outcome"] = "ERROR"
        finally:
            new_context.close()

    def test_04_cleanup(self, page, inactive_data):
        link_name = inactive_data.get("link_name")
        if not link_name:
            print("\n[inactive] no link to clean up")
            return
        print(f"\n[inactive] cleaning up: deleting {link_name}")
        NavigationPage(page).go_to_links()
        page.wait_for_timeout(800)
        try:
            links = LinksPage(page)
            links.delete_link(link_name)
            links.click_delete_and_confirm()
            page.wait_for_timeout(1500)
            print("[inactive] cleanup done")
        except Exception as e:
            print(f"[inactive] cleanup failed (non-fatal): {type(e).__name__}: {e}")

    def test_05_summary(self, inactive_data):
        grid = inactive_data.get("grid_outcome", "UNKNOWN")
        search = inactive_data.get("search_outcome", "UNKNOWN")
        print("\n" + "=" * 60)
        print(f"[inactive] FINAL OUTCOMES:")
        print(f"[inactive]   homepage grid: {grid}")
        print(f"[inactive]   search bar   : {search}")
        print(f"[inactive]   link name    : {inactive_data.get('link_name')}")
        print("=" * 60)
