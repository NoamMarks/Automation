"""
Page Object for the sidebar navigation menu.
"""


class NavigationPage:
    """Encapsulates the sidebar navigation buttons."""

    def __init__(self, page):
        self.page = page
        # Locators
        self._content_worlds_btn = page.get_by_role("button", name="עולמות תוכן")
        self._tags_btn = page.get_by_role("button", name="תגיות")
        self._messages_btn = page.get_by_role("button", name="מודעות")
        self._environments_btn = page.get_by_role("button", name="סביבות")
        self._links_btn = page.get_by_role("button", name="קישורים")

    def go_to_content_worlds(self):
        """Navigate to Content Worlds section."""
        self._content_worlds_btn.click()

    def go_to_tags(self):
        """Navigate to Tags section."""
        self._tags_btn.click()

    def go_to_messages(self):
        """Navigate to Messages section."""
        self._messages_btn.click()

    def go_to_environments(self):
        """Navigate to Environments section."""
        self._environments_btn.click()

    def go_to_links(self):
        """Navigate to Links section."""
        self._links_btn.click()
