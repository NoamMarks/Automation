"""
Admin Links grid — link create/delete smoke.

Seeds three links with deterministic names (GridA*, GridM*, GridZ*) and
deletes them, exercising the basic admin create + delete loop end-to-end.
"""

import os
import uuid

import pytest

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")


@pytest.fixture(scope="class")
def grid_data():
    return {}


class TestLinksAdminGrid:
    """Link create/delete smoke on the admin Links grid."""

    def test_01_login(self, page):
        print("\n[grid] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        page.wait_for_timeout(1000)

    def test_02_seed_three_links(self, page, grid_data):
        """Seed deterministic A/M/Z-prefixed links to enable predictable
        filtering and sort assertions."""
        suffix = uuid.uuid4().hex[:5]
        names = {
            "a": f"GridA_{suffix}",
            "m": f"GridM_{suffix}",
            "z": f"GridZ_{suffix}",
        }
        print(f"\n[grid] seeding three links: {list(names.values())}")
        links = LinksPage(page)
        for key, name in names.items():
            url = f"https://example.com/grid-{key}-{suffix}"
            links.create_link(name, url, f"grid-test-{key}-marker")
            links.click_save_and_confirm()
            page.wait_for_timeout(1500)
            links.verify_link_visible(name)
        grid_data["names"] = names
        grid_data["suffix"] = suffix

    def test_05_cleanup(self, page, grid_data):
        names = grid_data.get("names", {})
        if not names:
            return
        print(f"\n[grid/cleanup] deleting seeded links: {list(names.values())}")
        try:
            NavigationPage(page).go_to_links()
            page.wait_for_timeout(800)
        except Exception:
            pass

        links = LinksPage(page)
        for name in names.values():
            try:
                links.delete_link(name)
                links.click_delete_and_confirm()
                page.wait_for_timeout(1500)
                print(f"[grid/cleanup] deleted {name!r}")
            except Exception as e:
                print(f"[grid/cleanup] could not delete {name!r}: "
                      f"{type(e).__name__}: {e}")
