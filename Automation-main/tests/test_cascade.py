"""
Cascade / referential-integrity exploration test.

Goal: discover how the Zira portal handles deletion of a Domain that is
attached to an active Link. Domains are MANDATORY for Links — attaching one
creates a guaranteed dependency for testing referential integrity.

We do NOT assert a specific outcome — we observe and print whichever behavior
the system exhibits (BLOCK / NULLIFY / CASCADE) so a follow-up test can
encode the real contract.
"""

import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.domains_page import DomainsPage
from pages.links_page import LinksPage


@pytest.fixture(scope="class")
def cascade_data():
    return {}


class TestCascade:

    def test_01_login(self, page):
        print("\n[cascade] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        print("[cascade] login OK")

    def test_02_create_domain(self, page, cascade_data):
        domain_name = f"CasDom{uuid.uuid4().hex[:6]}"
        print(f"\n[cascade] creating domain: {domain_name}")

        nav = NavigationPage(page)
        nav.go_to_content_worlds()

        domains = DomainsPage(page)
        domains.create_domain(domain_name)
        domains.click_save_and_confirm()
        domains.verify_domain_visible(domain_name)

        cascade_data["domain_name"] = domain_name
        print("[cascade] domain created and visible")

    def test_03_create_link_with_domain(self, page, cascade_data):
        domain_name = cascade_data["domain_name"]
        link_name = f"CasLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[cascade] creating link '{link_name}' attached to domain '{domain_name}'")

        nav = NavigationPage(page)
        nav.go_to_links()

        links = LinksPage(page)
        links.open_add_link_dialog()
        links.fill_link_form(link_name, link_url, "cascade test link")

        # Combobox 0 = Domains. Pick our specific newly-created domain.
        links.select_option_by_name(domain_name, combobox_index=0)
        print(f"[cascade] selected domain '{domain_name}' in combobox 0")

        links.click_save_and_confirm()
        links.verify_link_visible(link_name)

        cascade_data["link_name"] = link_name
        print("[cascade] link created with domain attached")

    def test_04_attempt_delete_domain_and_observe(self, page, cascade_data):
        domain_name = cascade_data["domain_name"]
        link_name = cascade_data["link_name"]
        print(f"\n[cascade] >>> attempting to delete domain '{domain_name}' (link '{link_name}' depends on it)")

        nav = NavigationPage(page)
        nav.go_to_content_worlds()
        page.wait_for_timeout(800)

        domains = DomainsPage(page)
        try:
            domains.click_delete_on_row(domain_name)
        except Exception as e:
            print(f"[cascade] couldn't click delete on row: {type(e).__name__}: {e}")

        page.wait_for_timeout(1000)

        # Capture confirmation dialog text — may warn about attached links
        dialog = page.locator(".MuiDialog-root").first
        if dialog.count() > 0 and dialog.is_visible():
            print(f"[cascade] confirmation dialog text:\n--- DIALOG ---\n{dialog.inner_text()}\n--- END ---")
        else:
            print("[cascade] no MuiDialog detected after delete-icon click")

        # Click מחיקה (Delete) in the confirm dialog
        try:
            page.get_by_role("button", name="מחיקה").first.click(timeout=3000)
            print("[cascade] clicked מחיקה")
        except Exception as e:
            print(f"[cascade] could not click מחיקה: {type(e).__name__}: {e}")

        page.wait_for_timeout(800)

        # Click אישור (final confirm) if present
        try:
            page.get_by_role("button", name="אישור").click(timeout=3000)
            print("[cascade] clicked אישור")
        except Exception as e:
            print(f"[cascade] no אישור button: {type(e).__name__}: {e}")

        page.wait_for_timeout(2500)

        # Capture toasts/alerts
        any_toast = False
        for sel in [".MuiSnackbar-root", ".Toastify__toast", "[role='alert']", ".MuiAlert-root"]:
            n = page.locator(sel).count()
            for i in range(n):
                try:
                    txt = page.locator(sel).nth(i).inner_text()
                    if txt.strip():
                        print(f"[cascade] toast/alert ({sel})[{i}]: {txt!r}")
                        any_toast = True
                except Exception:
                    pass
        if not any_toast:
            print("[cascade] no toast/alert detected")

        # Re-navigate to domains to get a clean view, then check
        nav.go_to_content_worlds()
        page.wait_for_timeout(1500)
        domain_still_present = page.get_by_text(domain_name, exact=True).count() > 0
        print(f"[cascade] domain '{domain_name}' still present after attempted delete: {domain_still_present}")

        # Determine outcome
        if domain_still_present:
            print("[cascade] >>> OUTCOME: BLOCK — system refused to delete the domain while a link references it")
            cascade_data["outcome"] = "BLOCK"
        else:
            nav.go_to_links()
            page.wait_for_timeout(1500)
            link_still_present = page.locator("label", has_text=link_name).count() > 0
            print(f"[cascade] link '{link_name}' still present: {link_still_present}")
            if link_still_present:
                print("[cascade] >>> OUTCOME: NULLIFY — domain deleted, dependent link survived (reference cleared)")
                cascade_data["outcome"] = "NULLIFY"
            else:
                print("[cascade] >>> OUTCOME: CASCADE — domain and dependent link both deleted")
                cascade_data["outcome"] = "CASCADE"

    def test_05_summary(self, cascade_data):
        outcome = cascade_data.get("outcome", "UNKNOWN")
        print("\n" + "=" * 60)
        print(f"[cascade] FINAL OUTCOME: {outcome}")
        print(f"[cascade]   domain: {cascade_data.get('domain_name')}")
        print(f"[cascade]   link  : {cascade_data.get('link_name')}")
        print("=" * 60)
