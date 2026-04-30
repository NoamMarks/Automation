"""
Messages (מודעות) E2E flows — Assertive style.

Verifies:
  1. Create a popup-type message with image upload; appears in the admin grid.
  2. Admin "popup preview" button opens a preview modal.
  3. Active popup appears on the public homepage; toggling status to inactive
     hides it from the public homepage.
  4. Cleanup — delete the message.

Notes:
  - All tests share the class-scoped admin `page` fixture from conftest.
  - Public-side checks open fresh unauthenticated browser contexts so the
    popup-once-per-session behaviour is exercised cleanly each time.
"""

import os
import time
import uuid

import pytest
from playwright.sync_api import expect

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.messages_page import MessagesPage
from utils.image_gen import make_png_bytes


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

MODAL_SEL = "[role='dialog'], .MuiDialog-root, .MuiModal-root"
CARD_NAME_SEL = (
    "[class*='MessagesCardstyled__StyledMessageName'], "
    "[class*='MessagesCardstyled__GalleryObjectWrapper']"
)
ENV_TEXT_SEL = "[class*='Headerstyled__StatusEnvText']"


def _open_public_homepage(browser):
    """Fresh unauthenticated context on the homepage. Returns (context, page)."""
    ctx = browser.new_context()
    pp = ctx.new_page()
    pp.goto(APP_URL, wait_until="domcontentloaded")
    try:
        pp.get_by_role("button", name="הבנתי").click(timeout=3000)
    except Exception:
        pass
    pp.wait_for_timeout(2500)
    return ctx, pp


def _read_active_env(p):
    """Return the env name shown in the page header status, or None."""
    try:
        el = p.locator(ENV_TEXT_SEL).first
        if el.count() > 0:
            txt = el.inner_text().strip()
            return txt or None
    except Exception:
        pass
    return None


def _switch_public_env(public_page, target_env):
    """Click 'שינוי סביבה' on the public homepage and pick target_env.
    Returns True if the active env now matches target_env."""
    try:
        public_page.get_by_role("button", name="שינוי סביבה").click()
        public_page.wait_for_timeout(1500)
        opt = public_page.get_by_text(target_env, exact=True).first
        if opt.count() == 0:
            print(f"[env-switch] env {target_env!r} not in picker")
            return False
        opt.click()
        public_page.wait_for_timeout(800)
        for label in ("אישור", "שמירה", "החלף", "בחר", "אישור בחירה"):
            try:
                btn = public_page.get_by_role("button", name=label).first
                if btn.count() > 0 and btn.is_visible():
                    btn.click(timeout=2000)
                    break
            except Exception:
                continue
        public_page.wait_for_timeout(2500)
        now = _read_active_env(public_page)
        return now == target_env
    except Exception as e:
        print(f"[env-switch] failed: {type(e).__name__}: {e}")
        return False


def _ensure_public_on_env(public_page, target_env):
    """If the public page isn't on target_env, switch and verify."""
    current = _read_active_env(public_page)
    if current == target_env:
        return True
    print(f"[env-switch] {current!r} → {target_env!r}")
    return _switch_public_env(public_page, target_env)


def _find_popup_or_card(public_page, message_name, timeout_ms=15000):
    """Find the message on the public homepage. Returns (locator, kind) where
    kind is 'modal' or 'card', or (None, None) if not found in the timeout.

    'popup'-type messages in this app render as cards in the homepage
    'הודעות' carousel section (verified empirically — they are not always
    modal overlays).
    """
    deadline = time.time() + timeout_ms / 1000
    while time.time() < deadline:
        modal = public_page.locator(MODAL_SEL).filter(has_text=message_name).first
        try:
            if modal.count() > 0 and modal.is_visible():
                return modal, "modal"
        except Exception:
            pass
        card = public_page.locator(CARD_NAME_SEL).filter(has_text=message_name).first
        try:
            if card.count() > 0 and card.is_visible():
                return card, "card"
        except Exception:
            pass
        public_page.wait_for_timeout(400)
    return None, None


def _close_popup(public_page, modal):
    """Close a popup modal by trying common close-button selectors, then Esc."""
    for sel in (
        "[data-testid='CloseIcon']",
        "[aria-label='close']",
        "[aria-label='Close']",
        "[class*='StyledCloseOutlinedIcon']",
        "[class*='CloseOutlinedIcon']",
        "button:has(svg[data-testid='CloseIcon'])",
    ):
        try:
            btn = modal.locator(sel).first
            if btn.count() > 0 and btn.is_visible():
                btn.click(timeout=2000)
                return
        except Exception:
            continue
    public_page.keyboard.press("Escape")


@pytest.fixture(scope="class")
def msg_data():
    return {}


class TestMessagesFlows:

    # ---------------------------------------------------------
    # Setup: admin login → Messages page
    # ---------------------------------------------------------
    def test_01_login_admin(self, page):
        print("\n[messages] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_messages()

    # ---------------------------------------------------------
    # Scenario 1 — Create popup with image upload
    # ---------------------------------------------------------
    def test_02_create_popup_with_image(self, page, msg_data):
        """Create a popup message with image upload and verify it lands in
        the admin grid.

        Note on type choice: the app exposes three radio values —
            'popup'    → 'מתפרצת'   (modal-only, fires once per session unpredictably)
            'homepage' → 'מסך הבית' (carousel card on the public homepage)
            'both'     → 'מסך הבית ומתפרצת' (carousel card AND modal)
        We use 'both' so the public-side verification in test_04 has a
        deterministic surface (the carousel) to assert against. Popup-only
        type leaves no DOM trace once the modal closes / before it fires,
        which makes session-driven assertions flaky.
        """
        msg_name = f"PopupMsg_{uuid.uuid4().hex[:5]}"
        print(f"\n[messages/create] creating popup message {msg_name!r}")

        msgs = MessagesPage(page)
        msgs.open_add_message_dialog()
        msgs.fill_message_form(msg_name, "Popup test description")
        msgs.select_type("both")  # carousel + modal — see docstring above

        img_bytes = make_png_bytes(1.0)
        print(f"[messages/create] uploading {len(img_bytes):,} bytes "
              f"(~{len(img_bytes)/1024/1024:.2f} MB)")
        msgs.upload_image("popup_test.png", img_bytes)

        # Ensure the message is ACTIVE so it appears on the public homepage —
        # new messages may default to inactive.
        initial_status = msgs.get_status_checked()
        print(f"[messages/create] status switch initial: {initial_status}")
        if initial_status is False:
            before, after = msgs.toggle_status()
            print(f"[messages/create] toggled status: {before} → {after}")

        msgs.click_save_and_confirm()
        page.wait_for_timeout(1500)

        msgs.verify_message_visible(msg_name)
        msg_data["msg_name"] = msg_name
        print(f"[messages/create] {msg_name!r} visible in admin grid")

    # ---------------------------------------------------------
    # Scenario 2 — Admin popup preview opens a modal
    # ---------------------------------------------------------
    def test_03_admin_popup_preview(self, page):
        """The 'תצוגה מקדימה פופ אפ' button lives on the Messages page header
        (not inside the edit drawer). Click it directly and assert a modal
        appears."""
        print(f"\n[messages/preview] clicking 'תצוגה מקדימה פופ אפ' on messages page header")

        msgs = MessagesPage(page)
        page.wait_for_timeout(500)

        modals_before = page.locator(MODAL_SEL).count()
        msgs.click_preview()
        page.wait_for_timeout(1800)
        modals_after = page.locator(MODAL_SEL).count()
        print(f"[messages/preview] modal count {modals_before} → {modals_after}")

        assert modals_after > modals_before, (
            "Clicking 'תצוגה מקדימה פופ אפ' did not open a new modal"
        )

        preview = page.locator(MODAL_SEL).last
        expect(preview).to_be_visible(timeout=5000)
        print(f"[messages/preview] preview modal is visible")

        # Dismiss preview, then ensure the backdrop is fully cleared before
        # the next test interacts with the page.
        page.keyboard.press("Escape")
        page.wait_for_timeout(500)
        msgs._wait_backdrop_clear()

    # ---------------------------------------------------------
    # Scenario 3 — Public popup, toggle status, popup hidden
    # ---------------------------------------------------------
    def test_04_public_popup_and_status_toggle(self, page, msg_data):
        msg_name = msg_data.get("msg_name")
        assert msg_name, "test_02 must have created a message first"
        browser = page.context.browser

        # The message was created in admin's current env. Public defaults to
        # whatever was last set as 'default env' on the server, which may
        # differ — switch public to admin's env so the message is in scope.
        admin_env = _read_active_env(page)
        print(f"\n[messages/public] admin env: {admin_env!r}")

        # --- Phase A: message IS visible on a fresh public homepage ---
        print(f"[messages/public] expecting message {msg_name!r} on fresh homepage")
        ctx_a, pp_a = _open_public_homepage(browser)
        try:
            public_env = _read_active_env(pp_a)
            print(f"[messages/public] public env (initial): {public_env!r}")
            if admin_env and public_env != admin_env:
                ok = _ensure_public_on_env(pp_a, admin_env)
                print(f"[messages/public] env switch ok: {ok}; "
                      f"public env now: {_read_active_env(pp_a)!r}")

            found, kind = _find_popup_or_card(pp_a, msg_name, timeout_ms=15000)

            if found is None:
                # Diagnose: list every visible modal/card on the page
                print(f"[messages/public/diag] message not found — dumping page state")
                all_modals = pp_a.locator(MODAL_SEL)
                n_m = all_modals.count()
                print(f"[messages/public/diag] modals on page: {n_m}")
                for i in range(min(n_m, 6)):
                    try:
                        m = all_modals.nth(i)
                        if m.is_visible():
                            txt = m.inner_text().strip().replace("\n", " | ")[:160]
                            print(f"[messages/public/diag]   modal[{i}]: {txt!r}")
                    except Exception:
                        pass
                cards = pp_a.locator(CARD_NAME_SEL)
                n_c = cards.count()
                print(f"[messages/public/diag] message cards on page: {n_c}")
                for i in range(min(n_c, 8)):
                    try:
                        c = cards.nth(i)
                        if c.is_visible():
                            txt = c.inner_text().strip().replace("\n", " | ")[:120]
                            print(f"[messages/public/diag]   card[{i}]: {txt!r}")
                    except Exception:
                        pass
                import datetime as _dt
                diag_dir = os.path.join(os.getcwd(), "artifacts", "errors")
                os.makedirs(diag_dir, exist_ok=True)
                diag_path = os.path.join(
                    diag_dir, f"msg_public_diag_{_dt.datetime.now().strftime('%H%M%S')}.png"
                )
                try:
                    pp_a.screenshot(path=diag_path, full_page=True)
                    print(f"[messages/public/diag] public-page screenshot: {diag_path}")
                except Exception as e:
                    print(f"[messages/public/diag] screenshot failed: {e}")

            assert found is not None, (
                f"Active message {msg_name!r} did not appear on the public homepage "
                f"(checked both modal overlays and the messages carousel)"
            )
            print(f"[messages/public] message IS visible (kind={kind})")
            if kind == "modal":
                print(f"[messages/public] closing modal")
                _close_popup(pp_a, found)
                pp_a.wait_for_timeout(800)
        finally:
            ctx_a.close()

        # --- Phase B: in admin, toggle the message to inactive and save ---
        print(f"[messages/public] toggling {msg_name!r} to inactive in admin")
        msgs = MessagesPage(page)
        msgs.click_edit_on_row(msg_name)
        page.wait_for_timeout(800)

        before, after = msgs.toggle_status()
        print(f"[messages/public] status switch: {before} → {after}")
        assert after != before and after is not None, (
            f"Status switch did not change state (before={before}, after={after})"
        )

        msgs.click_save_and_confirm()
        page.wait_for_timeout(2000)

        # --- Phase C: message is NOT visible on a fresh public homepage ---
        print(f"[messages/public] expecting {msg_name!r} to be ABSENT now")
        ctx_c, pp_c = _open_public_homepage(browser)
        try:
            if admin_env:
                _ensure_public_on_env(pp_c, admin_env)
            found_after, kind_after = _find_popup_or_card(pp_c, msg_name, timeout_ms=6000)
            assert found_after is None, (
                f"{msg_name!r} STILL appearing as {kind_after!r} after status "
                f"was toggled to inactive"
            )
            print(f"[messages/public] message is hidden — PASS")
        finally:
            ctx_c.close()

    # ---------------------------------------------------------
    # Scenario 4 — Cleanup
    # ---------------------------------------------------------
    def test_05_cleanup_delete(self, page, msg_data):
        msg_name = msg_data.get("msg_name")
        if not msg_name:
            print("\n[messages/cleanup] nothing to delete")
            return
        print(f"\n[messages/cleanup] deleting {msg_name!r}")

        msgs = MessagesPage(page)
        msgs.delete_message(msg_name)
        msgs.click_delete_and_confirm()
        page.wait_for_timeout(1500)
        msgs.verify_message_not_attached(msg_name)
        print(f"[messages/cleanup] {msg_name!r} removed")
