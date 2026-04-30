"""
Page Object for the Messages (מודעות) management section.

Covers admin CRUD plus popup-specific features:
  - Type radios (popup / homepage / both)
  - Image upload (.jpg / .jpeg / .png)
  - Active/inactive status switch
  - Admin "popup preview" button
"""

import time

from playwright.sync_api import expect


class MessagesPage:
    """Encapsulates CRUD + media + status operations for Messages."""

    ROW_SELECTOR = "div.SingleMessagestyled__SingleMessageContainer-sc-hgjxqs-0"
    TITLE_SELECTOR = "span.SingleMessagestyled__MessageDateTitle-sc-hgjxqs-5"

    def __init__(self, page):
        self.page = page

        # Action buttons
        self._add_message_btn = page.get_by_role("button", name="הוספת מודעה")
        self._save_btn = page.get_by_role("button", name="שמירה")
        self._confirm_btn = page.get_by_role("button", name="אישור")
        self._delete_confirm_btn = page.get_by_role("button", name="מחיקה")
        self._preview_btn = page.get_by_role("button", name="תצוגה מקדימה פופ אפ")

        # Form inputs (drawer)
        self._name_input = page.locator("input[name='name']")
        self._description_input = page.locator("textarea[name='description']")
        self._file_input = page.locator("input[type='file']")

        # Type radios — values 'popup' / 'homepage' / 'both'
        self._type_popup = page.locator("input[value='popup']")
        self._type_homepage = page.locator("input[value='homepage']")
        self._type_both = page.locator("input[value='both']")

        # Status switch (active/inactive). The drawer has the relevant switch;
        # `.first` keeps us on the leading switch in the form.
        self._status_switch_root = page.locator(".MuiSwitch-root").first
        self._status_switch_input = page.locator(".MuiSwitch-input").first

    # ---------- internal helpers ----------

    def _get_message_row(self, name):
        """Return the row container for a message by its title text."""
        return self.page.locator(self.ROW_SELECTOR).filter(
            has=self.page.locator(self.TITLE_SELECTOR, has_text=name)
        ).first

    def _close_drawer_via_x(self):
        """Best-effort close the open drawer without saving."""
        for sel in (
            "[class*='StyledCloseOutlinedIcon']",
            "[class*='CloseOutlinedIcon']",
            "[data-testid='CloseIcon']",
            "[aria-label='close']",
            "[aria-label='Close']",
        ):
            try:
                el = self.page.locator(sel).first
                if el.count() > 0 and el.is_visible():
                    el.click(timeout=2000)
                    self.page.wait_for_timeout(400)
                    return
            except Exception:
                continue
        self.page.keyboard.press("Escape")
        self.page.wait_for_timeout(400)

    # ---------- drawer open / fields ----------

    def open_add_message_dialog(self):
        """Click 'Add Message' and wait for the drawer to be ready."""
        self._add_message_btn.click()
        self._name_input.wait_for(state="visible", timeout=8000)

    def fill_message_form(self, name, description="Test Desc"):
        """Fill name and description fields."""
        self._name_input.fill(name)
        self._description_input.fill(description)

    def select_type(self, type_name):
        """Select the message type. type_name in {'popup', 'homepage', 'both'}."""
        if type_name not in ("popup", "homepage", "both"):
            raise ValueError(f"Invalid message type: {type_name!r}")
        radio = self.page.locator(f"input[value='{type_name}']").first
        radio.check(force=True)
        self.page.wait_for_timeout(250)

    def upload_image(self, file_name, buffer, mime_type="image/png"):
        """Upload an image into the drawer's file input from in-memory bytes."""
        self._file_input.set_input_files(files=[{
            "name": file_name,
            "mimeType": mime_type,
            "buffer": buffer,
        }])
        # Allow the preview thumbnail to render before subsequent actions
        self.page.wait_for_timeout(1500)

    # ---------- status switch ----------

    def get_status_checked(self):
        """Return the current checked state of the active/inactive switch."""
        try:
            return self._status_switch_input.is_checked()
        except Exception:
            return None

    def toggle_status(self):
        """Click the visible switch root so MUI fires its onChange properly.
        Returns the resulting checked state."""
        before = self.get_status_checked()
        self._status_switch_root.click()
        self.page.wait_for_timeout(400)
        after = self.get_status_checked()
        return before, after

    # ---------- save / confirm / preview ----------

    def click_save(self):
        self._save_btn.click()

    def _wait_backdrop_clear(self, max_attempts=10, settle_ms=1200):
        """Wait until any lingering MuiBackdrop is no longer intercepting clicks.

        Two failure modes observed in this app:
          (A) Backdrop is animation-fading: aria-hidden='true' (so
              is_visible()=False) but still has non-zero bounding box and
              pointer-events != 'none', so it intercepts clicks underneath.
          (B) Popup-preview modal is fully open with a 'הבנתי' button but
              MUI ignores Escape on it — the only way out is to click the
              dismiss button itself.

        Strategy per attempt:
          1. If a 'הבנתי' / 'אישור' button is visible, CLICK it (handles B).
          2. Otherwise, press Escape (handles other modals that respect it).
          3. Then check whether any backdrop still has size + interactive
             pointer-events. If clear, settle for `settle_ms` and return.
        """
        for _ in range(max_attempts):
            # Step 1: dismiss any visible confirm/preview button
            dismissed = False
            for label in ("הבנתי", "אישור"):
                try:
                    btn = self.page.get_by_role("button", name=label).first
                    if btn.count() > 0 and btn.is_visible():
                        btn.click(timeout=2000)
                        self.page.wait_for_timeout(600)
                        dismissed = True
                        break
                except Exception:
                    continue

            if not dismissed:
                # Step 2: fall back to Escape
                try:
                    self.page.keyboard.press("Escape")
                    self.page.wait_for_timeout(500)
                except Exception:
                    pass

            # Step 3: check whether backdrops still intercept
            try:
                backdrops = self.page.locator(
                    ".MuiModal-backdrop, .MuiBackdrop-root"
                ).all()
                still_blocking = False
                for bd in backdrops:
                    try:
                        box = bd.bounding_box()
                        if box and box.get("width", 0) > 100 and box.get("height", 0) > 100:
                            pe = bd.evaluate(
                                "el => window.getComputedStyle(el).pointerEvents"
                            )
                            if pe and pe != "none":
                                still_blocking = True
                                break
                    except Exception:
                        pass
                if not still_blocking:
                    self.page.wait_for_timeout(settle_ms)
                    return True
            except Exception:
                return True
        return False

    def click_save_and_confirm(self, max_wait_ms=10000):
        """Click Save and dismiss whichever post-save modal appears.

        Plain messages: a confirmation dialog with 'אישור'.
        Popup messages: an auto-preview of how the popup will look, dismissed
        via 'הבנתי'. Polls for either label so the same call works for both
        flows. After dismissal, ensures any leftover backdrop is cleared.
        """
        self._save_btn.click()
        deadline = time.time() + max_wait_ms / 1000
        clicked = None
        while time.time() < deadline and clicked is None:
            for label in ("אישור", "הבנתי"):
                btn = self.page.get_by_role("button", name=label).first
                try:
                    if btn.count() > 0 and btn.is_visible():
                        btn.click(timeout=2000)
                        self.page.wait_for_timeout(500)
                        clicked = label
                        break
                except Exception:
                    continue
            if clicked is None:
                self.page.wait_for_timeout(200)
        self._wait_backdrop_clear()
        return clicked

    def click_delete_and_confirm(self):
        self._delete_confirm_btn.click()
        self._confirm_btn.click()
        self._wait_backdrop_clear()

    def click_preview(self):
        """Click the admin popup preview button (תצוגה מקדימה פופ אפ)."""
        self._preview_btn.click()

    # ---------- verifications ----------

    def verify_message_visible(self, name, timeout=7000):
        """Assert a message with the given name is visible (loose match)."""
        expect(
            self.page.locator("span, label", has_text=name)
        ).to_be_visible(timeout=timeout)

    def verify_message_updated(self, new_name):
        """Assert the updated message title is visible."""
        expect(
            self.page.locator(self.TITLE_SELECTOR, has_text=new_name)
        ).to_be_visible()

    def verify_message_not_attached(self, name):
        """Assert the message is no longer in the DOM."""
        expect(
            self.page.locator("span, div", has_text=name)
        ).not_to_be_attached()

    # ---------- row actions ----------

    def click_edit_on_row(self, name):
        row = self._get_message_row(name)
        row.locator("img[src*='editIcon']").first.click()
        self._name_input.wait_for(state="visible", timeout=8000)

    def fill_edit_message_name(self, new_name):
        self._name_input.click()
        self._name_input.press("Control+A")
        self._name_input.press("Delete")
        self._name_input.fill(new_name)

    def click_delete_on_row(self, name):
        row = self.page.locator(self.ROW_SELECTOR).filter(has_text=name).first
        row.locator("img[src*='deleteIcon']").first.click()

    # ---------- high-level CRUD ----------

    def create_message(self, name, description="Test Desc"):
        self.open_add_message_dialog()
        self.fill_message_form(name, description)

    def create_popup_message(self, name, description, image_buffer, image_name="msg.png"):
        """Full create flow for a popup message with image upload (no save)."""
        self.open_add_message_dialog()
        self.fill_message_form(name, description)
        self.select_type("popup")
        self.upload_image(image_name, image_buffer)

    def update_message(self, old_name, new_name):
        self.click_edit_on_row(old_name)
        self.fill_edit_message_name(new_name)

    def delete_message(self, name):
        self.click_delete_on_row(name)
