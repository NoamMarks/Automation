"""
Page Object for the Environments management section.
"""

from playwright.sync_api import expect


class EnvironmentsPage:
    """Encapsulates CRUD operations for Environments."""

    ROW_SELECTOR = "div.SingleEnvironmentstyled__SingleEnvironmentContainer-sc-vb02hm-0"
    NAME_SELECTOR = "div.SingleEnvironmentstyled__SingleEnvironmentName-sc-vb02hm-1"

    def __init__(self, page):
        self.page = page
        # Locators
        self._add_env_btn = page.get_by_role("button", name="הוספת סביבה")
        self._name_input = page.get_by_role("textbox", name="ניתן להזין עד 50 תווים")
        self._url_param_input = page.locator("input[name='URLParam']")
        self._save_btn = page.get_by_role("button", name="שמירה")
        self._confirm_btn = page.get_by_role("button", name="אישור")
        self._delete_confirm_btn = page.get_by_role("button", name="מחיקה")

    def open_add_environment_dialog(self):
        """Click the 'Add Environment' button."""
        self._add_env_btn.click()

    def fill_environment_form(self, name, url_param):
        """Fill in the environment name and URL param."""
        self._name_input.fill(name)
        self._url_param_input.fill(url_param)

    def click_save_and_confirm(self):
        """Click Save then Confirm."""
        self._save_btn.click()
        self._confirm_btn.click()

    def click_delete_and_confirm(self):
        """Click Delete then Confirm."""
        self._delete_confirm_btn.click()
        self._confirm_btn.click()

    def verify_environment_visible(self, name):
        """Assert that an environment with the given name is visible."""
        expect(
            self.page.locator(self.NAME_SELECTOR, has_text=name)
        ).to_be_visible()

    def verify_environment_not_attached(self, name):
        """Assert that the environment is no longer in the DOM."""
        expect(
            self.page.locator(self.NAME_SELECTOR, has_text=name)
        ).not_to_be_attached()

    def click_edit_on_row(self, name):
        """Find the environment row and click its edit icon."""
        row = self.page.locator(self.ROW_SELECTOR).filter(has_text=name).first
        row.locator("img[src*='editIcon']").first.click()

    def fill_edit_environment_name(self, new_name):
        """Clear and fill the environment name input during editing."""
        self._name_input.click()
        self._name_input.press("Control+A")
        self._name_input.press("Delete")
        self._name_input.fill(new_name)

    def click_delete_on_row(self, name):
        """Find the environment row and click its delete icon."""
        row = self.page.locator(self.ROW_SELECTOR).filter(has_text=name).first
        row.locator("img[src*='deleteIcon']").first.click()

    # --- High-level CRUD methods ---

    def create_environment(self, name, url_param):
        """Full create flow: open dialog, fill form."""
        self.open_add_environment_dialog()
        self.fill_environment_form(name, url_param)

    def update_environment(self, old_name, new_name):
        """Full update flow: click edit, change name."""
        self.click_edit_on_row(old_name)
        self.fill_edit_environment_name(new_name)

    def delete_environment(self, name):
        """Full delete flow: click delete on row."""
        self.click_delete_on_row(name)
