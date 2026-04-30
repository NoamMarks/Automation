"""
Page Object for the Login page.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class LoginPage:
    """Encapsulates login flow for the portal."""

    URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

    def __init__(self, page):
        self.page = page
        # Locators
        self._login_link = page.get_by_text("התחבר")
        self._username_input = page.get_by_role("textbox", name="הכנס שם משתמש")
        self._password_input = page.get_by_role("textbox", name="הכנס סיסמה")
        self._login_button = page.get_by_role("button", name="התחברות")
        self._post_login_indicator = page.locator("button:has-text('עולמות תוכן')")

    def navigate(self):
        """Navigate to the login page."""
        self.page.goto(self.URL)

    def fill_credentials(self):
        """Click the login link and fill username + password on the B2C form."""
        self._login_link.click()
        
        # Wait for the B2C form to load by waiting for the username input
        self.page.locator("#pretty-username").wait_for(state="visible", timeout=15000)
        
        self.page.locator("#pretty-username").fill(os.getenv("APP_USERNAME"))
        self.page.locator("#pretty-password").fill(os.getenv("APP_PASSWORD"))

    def click_login(self):
        """Click the login button on the B2C form."""
        self.page.locator("button.button-submit").click()

    def wait_for_dashboard(self, timeout=15000):
        """Wait until the dashboard is loaded and click into settings."""
        # Wait for the user profile text to appear to confirm we are logged in
        user_profile = self.page.get_by_text("שלום מנהלן ראשי")
        user_profile.wait_for(state="visible", timeout=timeout)
        
        # Make the two moves to get into settings
        user_profile.click()
        self.page.get_by_role("menu").click()
        
        # Wait for the 'Content Worlds' button to appear to confirm settings loaded
        self._post_login_indicator.wait_for(state="visible", timeout=timeout)

    def login(self):
        """Full login flow: navigate, fill credentials, click login, wait for dashboard."""
        self.navigate()
        self.fill_credentials()
        self.click_login()
