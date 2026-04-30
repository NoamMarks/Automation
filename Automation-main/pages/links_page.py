"""
Page Object for the Links management section.
"""

import os
import re

from playwright.sync_api import expect


class LinksPage:
    """Encapsulates CRUD operations for Links."""

    def __init__(self, page):
        self.page = page
        # Locators
        self._add_link_btn = page.get_by_role("button", name="הוספת קישור")
        self._name_input = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים")
        self._url_input = page.locator("input[name='URL']")
        self._description_input = page.locator("textarea[name='description']")
        self._save_btn = page.get_by_role("button", name="שמירה")
        self._confirm_btn = page.get_by_role("button", name="אישור")
        self._delete_confirm_btn = page.get_by_role("button", name="מחיקה")

    def open_add_link_dialog(self):
        """Click the 'Add Link' button to open the creation dialog."""
        self._add_link_btn.click()

    def fill_link_form(self, name, url, description):
        """Fill in the link creation/edit form fields."""
        self._name_input.fill(name)
        self._url_input.fill(url)
        self._description_input.fill(description)

    def select_combobox_options(self, combobox_index=0, count=3):
        """Open a combobox and check the first N checkboxes, then close."""
        self.page.get_by_role("combobox").nth(combobox_index).click()
        for box in self.page.locator("input[type='checkbox']").all()[:count]:
            box.check()
        self.page.locator(".MuiBackdrop-root.MuiBackdrop-invisible").click()

    def set_url_append(self, append: bool):
        """Click the URL-append radio. append=True selects כן, False selects לא (default)."""
        label = "כן" if append else "לא"
        self.page.get_by_role("radio", name=label).check()
        self.page.wait_for_timeout(200)

    def toggle_active_off(self):
        """Toggle the 'קישור פעיל / קישור לא פעיל' switch from active to inactive.
        MUI Switch hides the actual input under styled spans, so we click the root.
        Returns the final checked state.
        """
        switch_root = self.page.locator(".MuiSwitch-root").first
        if switch_root.count() == 0:
            raise RuntimeError("No MUI switch found in dialog — check the Add Link form HTML")
        hidden_input = switch_root.locator("input[type='checkbox']").first
        if hidden_input.is_checked():
            switch_root.click()
            self.page.wait_for_timeout(300)
        return hidden_input.is_checked()

    def select_option_by_name(self, option_name, combobox_index=1):
        """Open the combobox at index and toggle the option matching option_name.

        IMPORTANT: do NOT press Escape — Escape closes the whole drawer.
        After closing a previous combobox (via backdrop click), wait for popovers
        to dismiss before clicking the next combobox.
        """
        for sel in ["[role='listbox']", ".MuiPopover-root", ".MuiMenu-paper"]:
            try:
                self.page.locator(sel).first.wait_for(state="hidden", timeout=2000)
            except Exception:
                pass

        cb = self.page.get_by_role("combobox").nth(combobox_index)
        try:
            cb.scroll_into_view_if_needed(timeout=2000)
        except Exception:
            pass
        try:
            cb.click(timeout=3000)
        except Exception:
            # MUI Select listens for mousedown — bypass actionability via DOM event.
            self.page.evaluate(
                """(idx) => {
                    const cbs = document.querySelectorAll('[role="combobox"]');
                    const el = cbs[idx];
                    if (!el) throw new Error('combobox not found at index ' + idx);
                    el.dispatchEvent(new MouseEvent('mousedown', {bubbles:true, cancelable:true}));
                }""",
                combobox_index,
            )
        # Wait for the listbox to actually appear before searching for the option
        listbox = self.page.locator("[role='listbox']").last
        try:
            listbox.wait_for(state="visible", timeout=3000)
        except Exception:
            options_count = self.page.locator("[role='option']").count()
            print(f"[POM/select_option] listbox not visible. role=option count globally: {options_count}")
            sample_options = []
            for i in range(min(options_count, 10)):
                try:
                    sample_options.append(self.page.locator("[role='option']").nth(i).inner_text().strip()[:40])
                except Exception:
                    pass
            print(f"[POM/select_option] sample options: {sample_options}")
            raise

        # Options' accessible names may include extra text (e.g. "Name\ntype" in env picker),
        # so we filter by has_text instead of exact match.
        listbox.locator("[role='option']").filter(has_text=option_name).first.click()
        try:
            self.page.locator(".MuiBackdrop-root.MuiBackdrop-invisible").last.click(timeout=2000)
        except Exception:
            pass

    def click_save_and_confirm(self):
        """Click Save then Confirm."""
        self._save_btn.click()
        self._confirm_btn.click()

    def click_delete_and_confirm(self):
        """Click Delete then Confirm."""
        self._delete_confirm_btn.click()
        self._confirm_btn.click()

    # Styled-component classes have hash suffixes (e.g. SingleLinkstyled__SingleLinkWrapper-sc-11zofz3-0)
    # that change on every build, so we match by substring.
    _ROW_SELECTOR = "[class*='SingleLinkstyled__SingleLinkWrapper']"
    _NAME_SELECTOR = "[class*='SingleLinkstyled__StyledLinkName']"

    def _get_link_row(self, name):
        """Get the SingleLinkWrapper container for a link by its visible name."""
        return self.page.locator(self._ROW_SELECTOR).filter(
            has=self.page.locator(self._NAME_SELECTOR, has_text=name)
        ).first

    def verify_link_visible(self, name, timeout=7000):
        """Assert that a link with the given name is visible in the list."""
        expect(
            self.page.locator(self._NAME_SELECTOR, has_text=name)
        ).to_be_visible(timeout=timeout)

    def verify_link_not_attached(self, name, timeout=7000):
        """Assert that a link with the given name is no longer in the DOM."""
        expect(
            self.page.locator(self._NAME_SELECTOR, has_text=name)
        ).not_to_be_attached(timeout=timeout)

    def click_edit_on_row(self, name):
        """Find the row for a link by name and click its edit button."""
        row = self._get_link_row(name)
        expect(row).to_be_visible(timeout=7000)
        row.locator("div[title='עריכה']").first.click()

    def click_delete_on_row(self, name):
        """Find the row for a link by name and click its delete button."""
        row = self._get_link_row(name)
        expect(row).to_be_visible(timeout=7000)
        row.locator("div[title='מחיקה']").first.click()

    # --- High-level CRUD methods ---

    def create_link(self, name, url, description):
        """Full create flow: open dialog, fill form, select options, save."""
        self.open_add_link_dialog()
        self.fill_link_form(name, url, description)
        self.select_combobox_options(combobox_index=0, count=3)
        self.select_combobox_options(combobox_index=1, count=3)

    def update_link(self, old_name, new_name):
        """Full update flow: click edit, change name."""
        self.click_edit_on_row(old_name)
        self._name_input.fill(new_name)

    def delete_link(self, name):
        """Full delete flow: click delete on row."""
        self.click_delete_on_row(name)

    # --- Analytics: read the public click count for a link ---

    @staticmethod
    def _parse_visits_text(text):
        """Parse '1.3K כניסות' → 1300, '50 כניסות' → 50, '0 כניסות' → 0."""
        m = re.search(r"(\d+(?:\.\d+)?)\s*([KkMm]?)\s*כניסות", text)
        if not m:
            return 0
        n = float(m.group(1))
        sfx = m.group(2).upper()
        if sfx == "K":
            n *= 1000
        elif sfx == "M":
            n *= 1_000_000
        return int(n)

    def _read_count_from(self, public_page, link_name):
        """Walk both apps tabs on `public_page`, find the link card, return its visits."""
        for tab_label in ("יישומים אחרונים", "יישומים נפוצים"):
            try:
                tab = public_page.locator(
                    "[class*='WelcomeLinksstyled__HomeLinksTab']", has_text=tab_label
                ).first
                if tab.count() > 0:
                    tab.click()
                    public_page.wait_for_timeout(800)
            except Exception:
                pass

            card = public_page.locator(
                "[class*='WelcomeLinksstyled__LinkCard']"
            ).filter(
                has=public_page.locator(
                    "[class*='WelcomeLinksstyled__LinkTitle']", has_text=link_name
                )
            ).first

            if card.count() > 0:
                visits_el = card.locator("[class*='WelcomeLinksstyled__VisitsCount']").first
                if visits_el.count() > 0:
                    return self._parse_visits_text(visits_el.inner_text().strip())
        return -1

    def get_click_count(self, link_name, public_page=None):
        """Read the public-facing click count ('כניסות') for a link.

        The admin Links table doesn't expose visits, so we read from the public
        homepage card. If `public_page` is provided, it's used directly.
        Otherwise a fresh unauthenticated context is spun up for the read.

        Returns:
            int >= 0 — the parsed count.
            -1      — link could not be surfaced on the homepage.
        """
        if public_page is not None:
            return self._read_count_from(public_page, link_name)

        browser = self.page.context.browser
        ctx = browser.new_context()
        try:
            pp = ctx.new_page()
            pp.goto(os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/"))
            try:
                pp.get_by_role("button", name="הבנתי").click(timeout=3000)
            except Exception:
                pass
            pp.wait_for_timeout(2000)
            return self._read_count_from(pp, link_name)
        finally:
            ctx.close()
