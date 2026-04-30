"""
Page Object for the Domains (Content Worlds) management section.
"""

from playwright.sync_api import expect


class DomainsPage:
    """Encapsulates CRUD operations for Domains (Content Worlds)."""

    def __init__(self, page):
        self.page = page
        # Locators
        self._add_domain_btn = page.get_by_role("button", name="הוספת עולם תוכן")
        self._name_input = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים")
        self._save_btn = page.get_by_role("button", name="שמירה")
        self._confirm_btn = page.get_by_role("button", name="אישור")
        self._delete_confirm_btn = page.get_by_role("button", name="מחיקה")
        self._root = page.locator("#root")

    def open_add_domain_dialog(self):
        """Click the 'Add Content World' button."""
        self._add_domain_btn.click()

    def fill_domain_name(self, name):
        """Fill the domain name input."""
        self._name_input.fill(name)

    def select_icons(self, icon_names):
        """Click icon buttons by their accessible names."""
        for icon in icon_names:
            self.page.get_by_role("button", name=icon).click()

    def click_save_and_confirm(self):
        """Click Save then Confirm."""
        self._save_btn.click()
        self._confirm_btn.click()

    def click_delete_and_confirm(self):
        """Click Delete then Confirm."""
        self._delete_confirm_btn.click()
        self._confirm_btn.click()

    def verify_domain_visible(self, name):
        """Assert that a domain with the given name exists in the page."""
        expect(self._root).to_contain_text(name)

    def verify_domain_not_visible(self, name):
        """Assert that a domain with the given name no longer exists."""
        expect(self._root).not_to_contain_text(name)

    def click_edit_on_row(self, name):
        """Find the row for a domain by name and click its edit button."""
        row = self.page.locator("div").filter(has_text=name).filter(has_text="עריכה").last
        row.get_by_text("עריכה", exact=True).click()

    def click_delete_on_row(self, name):
        """Find the row for a domain by name and click its delete button."""
        row = self.page.locator("div").filter(has_text=name).filter(has_text="מחיקה").last
        row.get_by_text("מחיקה", exact=True).click()

    # --- High-level CRUD methods ---

    def create_domain(self, name, icons=None):
        """Full create flow: open dialog, fill name, select icons."""
        if icons is None:
            icons = ["Biohazard", "Broadcast", "Cpu"]
        self.open_add_domain_dialog()
        self.fill_domain_name(name)
        self.select_icons(icons)

    def update_domain(self, old_name, new_name, extra_icon="Heartbeat"):
        """Full update flow: click edit, change name, add an icon."""
        self.click_edit_on_row(old_name)
        self.fill_domain_name(new_name)
        self.page.get_by_role("button", name=extra_icon).click()

    def delete_domain(self, name):
        """Full delete flow: click delete on row."""
        self.click_delete_on_row(name)
