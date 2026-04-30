"""
Page Object for the Tags management section.
"""

from playwright.sync_api import expect


class TagsPage:
    """Encapsulates CRUD operations for Tags."""

    def __init__(self, page):
        self.page = page
        # Locators
        self._create_tag_btn = page.get_by_role("button", name="יצירת תגית")
        self._name_input = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים")
        self._edit_name_input = page.get_by_role("textbox", name="הכנס שם תגית")
        self._save_btn = page.get_by_role("button", name="שמירה")
        self._confirm_btn = page.get_by_role("button", name="אישור")
        self._delete_confirm_btn = page.get_by_role("button", name="מחיקה")

    def _get_tag_row(self, tag_name):
        """Get the tag row container by tag name."""
        return self.page.locator(
            "div.SingleTagstyled__SingleTagContainer-sc-1urjs6w-0"
        ).filter(
            has=self.page.locator(f"span[title='{tag_name}']")
        ).first

    def open_create_tag_dialog(self):
        """Click the 'Create Tag' button."""
        self._create_tag_btn.click()

    def fill_tag_name(self, name):
        """Fill the tag name input (create dialog)."""
        self._name_input.fill(name)

    def click_save_and_confirm(self):
        """Click Save then Confirm."""
        self._save_btn.click()
        self._confirm_btn.click()

    def click_delete_and_confirm(self):
        """Click Delete then Confirm."""
        self._delete_confirm_btn.click()
        self._confirm_btn.click()

    def verify_tag_visible(self, tag_name, timeout=7000):
        """Assert that the tag is visible by its styled-component class."""
        expect(
            self.page.locator(
                "span.SingleTagstyled__TagText-sc-1urjs6w-4", has_text=tag_name
            )
        ).to_be_visible(timeout=timeout)

    def verify_tag_not_attached(self, tag_name, timeout=7000):
        """Assert that the tag no longer exists in the DOM."""
        expect(
            self.page.locator(f"span[title='{tag_name}']")
        ).not_to_be_attached(timeout=timeout)

    def click_edit_on_row(self, tag_name):
        """Find the tag row and click its edit icon."""
        tag_row = self._get_tag_row(tag_name)
        tag_row.scroll_into_view_if_needed()
        edit_icon = tag_row.locator(
            ".SingleTagstyled__IconWithTooltip-sc-1urjs6w-7 img"
        ).first
        edit_icon.hover()
        self.page.wait_for_timeout(300)
        edit_icon.click(force=True)

    def fill_edit_tag_name(self, new_name):
        """Clear and fill the edit tag name input."""
        self._edit_name_input.dblclick()
        self._edit_name_input.fill(new_name)

    def click_delete_on_row(self, tag_name):
        """Find the tag row and click its delete icon."""
        tag_row = self._get_tag_row(tag_name)
        tag_row.scroll_into_view_if_needed()
        del_icon = tag_row.locator(
            ".SingleTagstyled__IconWithTooltip-sc-1urjs6w-7 img[src*='deleteIcon']"
        ).first
        del_icon.hover()
        self.page.wait_for_timeout(300)
        del_icon.click(force=True)

    def verify_updated_tag_visible(self, new_name, timeout=7000):
        """Assert that the updated tag is visible by its title attribute."""
        expect(
            self.page.locator(f"span[title='{new_name}']")
        ).to_be_visible(timeout=timeout)

    # --- High-level CRUD methods ---

    def create_tag(self, name):
        """Full create flow: open dialog, fill name."""
        self.open_create_tag_dialog()
        self.fill_tag_name(name)

    def update_tag(self, old_name, new_name):
        """Full update flow: click edit, fill new name."""
        self.click_edit_on_row(old_name)
        self.fill_edit_tag_name(new_name)

    def delete_tag(self, name):
        """Full delete flow: click delete on row."""
        self.click_delete_on_row(name)
