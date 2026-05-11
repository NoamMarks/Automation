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

    def _is_already_logged_in(self, wait_ms=1500):
        """Idempotency guard for storage-state preloaded contexts.

        When `tests/conftest.py`'s session-scoped fixture has populated
        the browser context with admin cookies + localStorage, the page
        renders the post-login welcome text immediately. In that case we
        must NOT click the (now-hidden) 'התחבר' link — we just short-circuit.
        """
        try:
            self.page.get_by_text("שלום מנהלן ראשי").first.wait_for(
                state="visible", timeout=wait_ms
            )
            return True
        except Exception:
            return False

    def fill_credentials(self):
        """Click the login link and fill username + password on the B2C form.
        No-op if the page already shows admin auth (preloaded storage_state)."""
        if self._is_already_logged_in():
            return
        self._login_link.click()

        # Wait for the B2C form to load by waiting for the username input
        self.page.locator("#pretty-username").wait_for(state="visible", timeout=15000)

        self.page.locator("#pretty-username").fill(os.getenv("APP_USERNAME"))
        self.page.locator("#pretty-password").fill(os.getenv("APP_PASSWORD"))

    def click_login(self):
        """Click the login button on the B2C form.
        No-op if already authenticated."""
        if self._is_already_logged_in():
            return
        self.page.locator("button.button-submit").click()

    def wait_for_dashboard(self, timeout=15000, attempts=3):
        """Wait until the dashboard is loaded and click into settings.

        The 'enter admin' transition is a 2-click sequence: click the
        user-profile, then click the menu item that opens. A frontend
        re-render between those clicks (observed when an SSE connection
        drops mid-test, see UI bug "menu auto-closes on SSE error")
        can flicker the menu shut before the second click lands.

        We retry the whole sequence a few times with short per-step
        timeouts. The final post-login wait keeps the full timeout
        budget so success-path latency isn't affected.
        """
        user_profile = self.page.get_by_text("שלום מנהלן ראשי")
        user_profile.wait_for(state="visible", timeout=timeout)

        last_err = None
        for attempt in range(1, attempts + 1):
            try:
                user_profile.click()
                # Wait for the menu to actually open AND stabilize before
                # clicking it — animation + re-render races are the
                # specific failure mode this guards against.
                menu = self.page.get_by_role("menu")
                menu.wait_for(state="visible", timeout=4000)
                # Tiny settle so a mid-animation re-render doesn't swallow
                # the click; cheaper than a stability poll.
                self.page.wait_for_timeout(200)
                menu.click(timeout=4000)
                # Confirm we landed in the admin context
                self._post_login_indicator.wait_for(
                    state="visible", timeout=timeout
                )
                return
            except Exception as e:
                last_err = e
                if attempt == attempts:
                    break
                print(f"[login] wait_for_dashboard attempt {attempt}/{attempts} "
                      f"failed ({type(e).__name__}); retrying after settle")
                # Let any stale menu close and the page re-stabilize
                try:
                    self.page.keyboard.press("Escape")
                except Exception:
                    pass
                self.page.wait_for_timeout(1500)
        # Out of attempts — surface the original error
        raise last_err

    def login(self):
        """Full login flow: navigate, fill credentials, click login, wait for dashboard."""
        self.navigate()
        self.fill_credentials()
        self.click_login()
