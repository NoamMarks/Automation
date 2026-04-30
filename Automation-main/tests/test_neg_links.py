"""
Negative-path validation tests for the Add Link dialog.

Goal: empirically discover how Zira's Link form responds to invalid input —
blank required fields, over-length text, and silent-disable patterns.

Prior observation: the system uses "Save button stays disabled" as its primary
error UX (no toast, no inline message). These tests CAPTURE the behavior across
several invalid scenarios rather than asserting a presumed outcome.
"""

import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage


@pytest.fixture(scope="class")
def neg_data():
    return {}


def _capture_form_state(page, scenario):
    """Print everything observable about the current form's validation state."""
    print(f"\n[neg/{scenario}] --- form state ---")

    save_btn = page.get_by_role("button", name="שמירה")
    if save_btn.count() == 0:
        print(f"[neg/{scenario}]   save button: NOT FOUND")
    else:
        try:
            print(f"[neg/{scenario}]   save button disabled: {save_btn.first.is_disabled()}")
        except Exception as e:
            print(f"[neg/{scenario}]   save button state error: {e}")

    invalid = page.locator("[aria-invalid='true']")
    n_invalid = invalid.count()
    print(f"[neg/{scenario}]   aria-invalid='true' count: {n_invalid}")
    for i in range(min(n_invalid, 5)):
        try:
            el = invalid.nth(i)
            name = el.get_attribute("name") or el.get_attribute("id") or "?"
            print(f"[neg/{scenario}]     invalid[{i}] name/id={name}")
        except Exception:
            pass

    helpers = page.locator(".MuiFormHelperText-root.Mui-error, .MuiFormHelperText-root[class*='error']")
    n_helpers = helpers.count()
    if n_helpers > 0:
        print(f"[neg/{scenario}]   MuiFormHelperText error count: {n_helpers}")
        for i in range(min(n_helpers, 5)):
            try:
                txt = helpers.nth(i).inner_text().strip()
                if txt:
                    print(f"[neg/{scenario}]     helper[{i}]: {txt!r}")
            except Exception:
                pass

    for sel in [".MuiSnackbar-root", ".Toastify__toast", "[role='alert']", ".MuiAlert-root"]:
        n = page.locator(sel).count()
        for i in range(n):
            try:
                txt = page.locator(sel).nth(i).inner_text().strip()
                if txt:
                    print(f"[neg/{scenario}]   toast ({sel})[{i}]: {txt!r}")
            except Exception:
                pass


def _close_dialog(page):
    """Close the open Add Link drawer. Tries the X close, falls back to Escape."""
    candidates = [
        page.locator("[data-testid='CloseIcon']"),
        page.locator("[aria-label='close']"),
        page.locator("[aria-label='Close']"),
        page.get_by_role("button", name="close"),
    ]
    for c in candidates:
        try:
            if c.count() > 0 and c.first.is_visible():
                c.first.click(timeout=2000)
                page.wait_for_timeout(400)
                return
        except Exception:
            continue
    page.keyboard.press("Escape")
    page.wait_for_timeout(400)


class TestNegLinks:

    def test_01_login(self, page):
        print("\n[neg] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        print("[neg] reached Links admin")

    def test_02_blank_title(self, page):
        scenario = "blank_title"
        print(f"\n[neg] >>> SCENARIO: {scenario} (URL + Domain filled, Title BLANK)")
        links = LinksPage(page)
        links.open_add_link_dialog()
        page.locator("input[name='URL']").fill(f"https://example.com/{uuid.uuid4().hex[:8]}")
        try:
            links.select_combobox_options(combobox_index=0, count=1)
        except Exception as e:
            print(f"[neg/{scenario}]   couldn't select domain: {type(e).__name__}: {e}")
        try:
            page.get_by_role("button", name="שמירה").click(timeout=2000)
            print(f"[neg/{scenario}]   Save click SUCCEEDED (would mean blank title is allowed)")
        except Exception:
            print(f"[neg/{scenario}]   Save click did not complete (button likely disabled)")
        _capture_form_state(page, scenario)
        _close_dialog(page)

    def test_03_blank_url(self, page):
        scenario = "blank_url"
        print(f"\n[neg] >>> SCENARIO: {scenario} (Title + Domain filled, URL BLANK)")
        links = LinksPage(page)
        links.open_add_link_dialog()
        page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(f"NegLink{uuid.uuid4().hex[:5]}")
        try:
            links.select_combobox_options(combobox_index=0, count=1)
        except Exception as e:
            print(f"[neg/{scenario}]   couldn't select domain: {type(e).__name__}: {e}")
        try:
            page.get_by_role("button", name="שמירה").click(timeout=2000)
            print(f"[neg/{scenario}]   Save click SUCCEEDED (would mean blank URL is allowed)")
        except Exception:
            print(f"[neg/{scenario}]   Save click did not complete (button likely disabled)")
        _capture_form_state(page, scenario)
        _close_dialog(page)

    def test_04_no_domain(self, page):
        scenario = "no_domain"
        print(f"\n[neg] >>> SCENARIO: {scenario} (Title + URL filled, NO Domain)")
        links = LinksPage(page)
        links.open_add_link_dialog()
        page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(f"NegLink{uuid.uuid4().hex[:5]}")
        page.locator("input[name='URL']").fill(f"https://example.com/{uuid.uuid4().hex[:8]}")
        try:
            page.get_by_role("button", name="שמירה").click(timeout=2000)
            print(f"[neg/{scenario}]   Save click SUCCEEDED (would mean no domain required)")
        except Exception:
            print(f"[neg/{scenario}]   Save click did not complete (button likely disabled)")
        _capture_form_state(page, scenario)
        _close_dialog(page)

    def test_05_overlength_title(self, page):
        scenario = "overlength_title"
        print(f"\n[neg] >>> SCENARIO: {scenario} (try to enter 35 chars in Title; max is 30)")
        links = LinksPage(page)
        links.open_add_link_dialog()
        attempted = "A" * 35
        title_input = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים")
        title_input.fill(attempted)
        accepted = title_input.input_value()
        print(f"[neg/{scenario}]   attempted {len(attempted)} chars; accepted {len(accepted)} chars: {accepted!r}")
        if len(accepted) == 30:
            print(f"[neg/{scenario}]   >>> form silently TRUNCATES to maxLength")
        elif len(accepted) == 35:
            print(f"[neg/{scenario}]   >>> form ALLOWS over-length input (validation must happen on save)")
        else:
            print(f"[neg/{scenario}]   >>> unexpected accepted length")
        _capture_form_state(page, scenario)
        _close_dialog(page)

    def test_06_overlength_description(self, page):
        scenario = "overlength_description"
        print(f"\n[neg] >>> SCENARIO: {scenario} (try to enter 250 chars in Description; max is 200)")
        links = LinksPage(page)
        links.open_add_link_dialog()
        desc_input = page.locator("textarea[name='description']")
        attempted = "x" * 250
        desc_input.fill(attempted)
        accepted = desc_input.input_value()
        print(f"[neg/{scenario}]   attempted {len(attempted)} chars; accepted {len(accepted)} chars")
        if len(accepted) == 200:
            print(f"[neg/{scenario}]   >>> description silently TRUNCATES to maxLength")
        elif len(accepted) == 250:
            print(f"[neg/{scenario}]   >>> description ALLOWS over-length input")
        # Look for the live counter (we saw "0/200" in the screenshot)
        counter = page.get_by_text("/200").first
        if counter.count() > 0:
            try:
                print(f"[neg/{scenario}]   live counter text: {counter.inner_text()!r}")
            except Exception:
                pass
        _capture_form_state(page, scenario)
        _close_dialog(page)

    def test_07_summary(self):
        print("\n" + "=" * 60)
        print("[neg] negative-path validation pass complete")
        print("[neg] each scenario above prints: save-button state, aria-invalid, helper-text errors, and toasts")
        print("=" * 60)
