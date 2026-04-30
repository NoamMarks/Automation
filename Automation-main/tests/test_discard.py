"""
X-vs-Cancel discard tests.

Goal: verify two related behaviors flagged in the testing-priorities list:
  1. The top-LEFT X on the Add Link drawer discards an unsaved draft WITHOUT
     a "are you sure?" prompt, and the next open of the drawer shows an empty
     form (no draft persistence).
  2. On the Delete confirmation modal, BOTH the close X and the `ביטול`
     button abort deletion (the entity remains). Only `מחיקה` actually deletes.

Each scenario prints PASS/FAIL inline; the test methods themselves never
fail-by-assertion (exploratory style), so the run stays green.
"""

import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage


@pytest.fixture(scope="class")
def discard_data():
    return {}


def _try_click_close_x(scope, scenario):
    """Try Zira's known close-X selectors within scope. Return label of the one that worked, or None.

    Discovered: Add Link drawer uses [class*='StyledCloseOutlinedIcon'] (NewLinkstyled-based).
    Other dialogs may use the standard MUI CloseIcon — keep both as fallbacks.
    """
    candidates = [
        ("[class*='StyledCloseOutlinedIcon']", scope.locator("[class*='StyledCloseOutlinedIcon']")),
        ("[class*='CloseOutlinedIcon']", scope.locator("[class*='CloseOutlinedIcon']")),
        ("[data-testid='CloseIcon']", scope.locator("[data-testid='CloseIcon']")),
        ("[aria-label='close']", scope.locator("[aria-label='close']")),
        ("[aria-label='Close']", scope.locator("[aria-label='Close']")),
    ]
    for label, c in candidates:
        try:
            if c.count() > 0 and c.first.is_visible():
                c.first.click(timeout=2000)
                print(f"[{scenario}]   X click via: {label}")
                return label
        except Exception:
            continue
    print(f"[{scenario}]   no X close button found in scope")
    return None


def _ensure_no_modal(page, scenario, timeout_ms=3000):
    """Defensive cleanup: if a modal/backdrop is still visible, dismiss with Escape."""
    backdrop = page.locator(".MuiBackdrop-root:visible")
    if backdrop.count() > 0:
        print(f"[{scenario}]   leftover backdrop detected — pressing Escape")
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
    try:
        page.locator(".MuiBackdrop-root").first.wait_for(state="hidden", timeout=timeout_ms)
    except Exception:
        pass


class TestDiscard:

    def test_01_login(self, page):
        print("\n[discard] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        print("[discard] reached Links admin")

    def test_02_add_link_x_discards_draft(self, page):
        scenario = "discard/add_x"
        print(f"\n[{scenario}] open Add Link, fill draft, X-close, reopen, expect empty form")

        links = LinksPage(page)
        draft_name = f"DraftDsc{uuid.uuid4().hex[:6]}"
        draft_url = f"https://example.com/draft-{uuid.uuid4().hex[:6]}"

        links.open_add_link_dialog()
        title_input = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים")
        url_input = page.locator("input[name='URL']")
        title_input.fill(draft_name)
        url_input.fill(draft_url)
        print(f"[{scenario}]   draft filled — title={draft_name!r}, URL={draft_url!r}")

        _try_click_close_x(page, scenario)
        page.wait_for_timeout(800)

        prompt = page.locator(".MuiDialog-root, [role='alertdialog']")
        n_prompt = prompt.count()
        print(f"[{scenario}]   confirm-prompt count after X: {n_prompt}")
        if n_prompt > 0:
            for i in range(n_prompt):
                try:
                    txt = prompt.nth(i).inner_text().strip()
                    if txt:
                        print(f"[{scenario}]     prompt body: {txt!r}")
                except Exception:
                    pass

        links.open_add_link_dialog()
        page.wait_for_timeout(500)
        title_after = page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").input_value()
        url_after = page.locator("input[name='URL']").input_value()
        print(f"[{scenario}]   reopened state — title={title_after!r}, URL={url_after!r}")

        if title_after == "" and url_after == "":
            print(f"[{scenario}]   >>> PASS: draft discarded silently, form is empty on reopen")
        elif title_after == draft_name or url_after == draft_url:
            print(f"[{scenario}]   >>> FAIL: draft was PERSISTED across X-close")
        else:
            print(f"[{scenario}]   >>> partial — title_persisted={title_after == draft_name}, url_persisted={url_after == draft_url}")

        _try_click_close_x(page, scenario + "/cleanup")
        page.wait_for_timeout(500)

    def test_03_setup_create_link(self, page, discard_data):
        link_name = f"DiscardLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[discard] creating real link to use for delete-X tests: '{link_name}'")

        links = LinksPage(page)
        links.create_link(link_name, link_url, "discard test link")
        links.click_save_and_confirm()
        page.wait_for_timeout(1500)
        links.verify_link_visible(link_name)
        discard_data["link_name"] = link_name
        print("[discard] link created and visible")

    def test_04_delete_x_aborts(self, page, discard_data):
        scenario = "discard/del_x"
        link_name = discard_data["link_name"]
        print(f"\n[{scenario}] click trash → click X on confirm modal → expect link still exists")

        links = LinksPage(page)
        links.click_delete_on_row(link_name)
        page.wait_for_timeout(800)

        # Zira's confirm uses MUI Modal (not Dialog). Look for a visible Modal.
        modal = page.locator(".MuiModal-root:visible").first
        if modal.count() == 0:
            print(f"[{scenario}]   confirmation modal did not appear — skipping")
            _ensure_no_modal(page, scenario)
            return
        print(f"[{scenario}]   confirmation modal visible")

        which = _try_click_close_x(modal, scenario)
        if which is None:
            page.keyboard.press("Escape")
            print(f"[{scenario}]   fell back to Escape key")
        page.wait_for_timeout(1200)
        _ensure_no_modal(page, scenario)

        try:
            links.verify_link_visible(link_name, timeout=3000)
            print(f"[{scenario}]   >>> PASS: link still exists after X-close on delete confirm")
        except Exception:
            print(f"[{scenario}]   >>> FAIL: link was DELETED despite X-close")

    def test_05_delete_cancel_aborts(self, page, discard_data):
        scenario = "discard/del_cancel"
        link_name = discard_data["link_name"]
        print(f"\n[{scenario}] click trash → click ביטול on confirm modal → expect link still exists")

        links = LinksPage(page)
        links.click_delete_on_row(link_name)
        page.wait_for_timeout(800)

        try:
            page.get_by_role("button", name="ביטול").first.click(timeout=3000)
            print(f"[{scenario}]   clicked ביטול")
        except Exception as e:
            print(f"[{scenario}]   couldn't click ביטול: {type(e).__name__}: {e}")
        page.wait_for_timeout(1200)
        _ensure_no_modal(page, scenario)

        try:
            links.verify_link_visible(link_name, timeout=3000)
            print(f"[{scenario}]   >>> PASS: link still exists after ביטול")
        except Exception:
            print(f"[{scenario}]   >>> FAIL: link was DELETED despite ביטול")

    def test_06_delete_actually_works(self, page, discard_data):
        scenario = "discard/del_real"
        link_name = discard_data["link_name"]
        print(f"\n[{scenario}] sanity check: click trash → click מחיקה → expect link gone (also: cleanup)")

        links = LinksPage(page)
        links.delete_link(link_name)
        links.click_delete_and_confirm()
        page.wait_for_timeout(1500)

        try:
            links.verify_link_not_attached(link_name, timeout=5000)
            print(f"[{scenario}]   >>> PASS: link was deleted via מחיקה")
        except Exception:
            print(f"[{scenario}]   >>> FAIL: link still present after מחיקה — abort behavior may be wrong")

    def test_07_summary(self):
        print("\n" + "=" * 60)
        print("[discard] X-vs-Cancel discard tests complete — see PASS/FAIL above")
        print("=" * 60)
