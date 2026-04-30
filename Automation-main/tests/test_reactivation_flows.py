"""
Inactive ↔ Active round-trip symmetry tests for Messages.

`test_messages_flows` already verifies one direction of the contract:
Active → Inactive correctly hides the message from the public homepage.
What it does NOT verify is the inverse and the round-trip:
  - Inactive at creation actually stays hidden
  - Toggling Inactive → Active brings it back into view
  - Toggling back Active → Inactive hides it again

Toggle bugs commonly manifest as "I set it active but it's still hidden"
(stale client cache, unsaved state, async update lag) — those are
exactly the regressions this round-trip catches.

Strategy:
  - Type 'both' (carousel + modal) so visibility is deterministic via the
    homepage messages section, regardless of per-session popup behavior.
  - Each public-side check uses a fresh unauthenticated context so client
    caching cannot hide a real regression.
"""

import os
import time
import uuid

import pytest

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


# --------------------------------------------------------------------------
# Helpers (mirrored from test_messages_flows so this file stays self-contained
# while the suite hardens; can be promoted to utils/ later if more tests need
# them).
# --------------------------------------------------------------------------

def _open_public_homepage(browser):
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
    try:
        el = p.locator(ENV_TEXT_SEL).first
        if el.count() > 0:
            return (el.inner_text() or "").strip() or None
    except Exception:
        pass
    return None


def _switch_public_env(public_page, target_env):
    try:
        public_page.get_by_role("button", name="שינוי סביבה").click()
        public_page.wait_for_timeout(1500)
        opt = public_page.get_by_text(target_env, exact=True).first
        if opt.count() == 0:
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
        return _read_active_env(public_page) == target_env
    except Exception:
        return False


def _ensure_public_on_env(public_page, target_env):
    if _read_active_env(public_page) == target_env:
        return True
    return _switch_public_env(public_page, target_env)


def _find_message_on_public(public_page, message_name, timeout_ms=12000):
    """Return True if `message_name` is visible on the public homepage
    (modal overlay OR carousel card) within the timeout."""
    deadline = time.time() + timeout_ms / 1000
    while time.time() < deadline:
        modal = public_page.locator(MODAL_SEL).filter(has_text=message_name).first
        try:
            if modal.count() > 0 and modal.is_visible():
                return True
        except Exception:
            pass
        card = public_page.locator(CARD_NAME_SEL).filter(has_text=message_name).first
        try:
            if card.count() > 0 and card.is_visible():
                return True
        except Exception:
            pass
        public_page.wait_for_timeout(400)
    return False


def _is_message_visible_to_public(admin_page, message_name, timeout_ms=12000):
    """Open a fresh public context (matching admin's env), check visibility.
    Returns True / False."""
    browser = admin_page.context.browser
    admin_env = _read_active_env(admin_page)
    ctx, pp = _open_public_homepage(browser)
    try:
        if admin_env and _read_active_env(pp) != admin_env:
            _ensure_public_on_env(pp, admin_env)
        return _find_message_on_public(pp, message_name, timeout_ms)
    finally:
        ctx.close()


@pytest.fixture(scope="class")
def react_data():
    return {}


class TestMessageReactivation:

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------
    def test_01_login_admin(self, page):
        print("\n[reactivate] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_messages()

    # ---------------------------------------------------------
    # Phase A — create as INACTIVE
    # ---------------------------------------------------------
    def test_02_create_message_as_inactive(self, page, react_data):
        msg_name = f"PopupMsg_{uuid.uuid4().hex[:5]}"
        print(f"\n[reactivate] creating message {msg_name!r} as INACTIVE")

        msgs = MessagesPage(page)
        msgs.open_add_message_dialog()
        msgs.fill_message_form(msg_name, "reactivation cycle test")
        msgs.select_type("both")  # carousel + modal — deterministic visibility
        msgs.upload_image("react.png", make_png_bytes(0.3))

        # Form defaults to ACTIVE — toggle OFF before saving so creation is INACTIVE
        initial_status = msgs.get_status_checked()
        print(f"[reactivate]   status switch initial (active=True): {initial_status}")
        if initial_status is True:
            before, after = msgs.toggle_status()
            print(f"[reactivate]   toggled: {before} → {after}")
            assert after is False, (
                f"Could not flip status to inactive before save (after={after})"
            )
        elif initial_status is False:
            print("[reactivate]   already inactive (no toggle needed)")
        else:
            pytest.fail(f"Could not read status switch state (got {initial_status!r})")

        msgs.click_save_and_confirm()
        page.wait_for_timeout(1500)
        msgs.verify_message_visible(msg_name)
        react_data["msg_name"] = msg_name
        print(f"[reactivate] {msg_name!r} saved as INACTIVE, visible in admin grid")

    def test_03_inactive_is_NOT_visible_on_public(self, page, react_data):
        msg_name = react_data["msg_name"]
        print(f"\n[reactivate] >>> Phase A check: expecting {msg_name!r} HIDDEN on public")
        is_visible = _is_message_visible_to_public(page, msg_name, timeout_ms=10000)
        assert not is_visible, (
            f"INACTIVE message {msg_name!r} should NOT appear on the public homepage "
            f"(but it did)"
        )
        print(f"[reactivate] >>> Phase A PASS: hidden as expected")

    # ---------------------------------------------------------
    # Phase B — toggle to ACTIVE
    # ---------------------------------------------------------
    def test_04_toggle_inactive_to_active(self, page, react_data):
        msg_name = react_data["msg_name"]
        print(f"\n[reactivate] toggling {msg_name!r} INACTIVE → ACTIVE")

        msgs = MessagesPage(page)
        msgs.click_edit_on_row(msg_name)
        page.wait_for_timeout(800)

        before = msgs.get_status_checked()
        assert before is False, (
            f"Edit drawer opened but status switch is not False (got {before!r}). "
            f"The previous save may not have persisted as INACTIVE."
        )
        before, after = msgs.toggle_status()
        print(f"[reactivate]   status: {before} → {after}")
        assert after is True, (
            f"Expected toggle inactive→active but got {before!r}→{after!r}"
        )

        msgs.click_save_and_confirm()
        page.wait_for_timeout(2000)

    def test_05_active_IS_visible_on_public(self, page, react_data):
        msg_name = react_data["msg_name"]
        print(f"\n[reactivate] >>> Phase B check: expecting {msg_name!r} VISIBLE on public")
        is_visible = _is_message_visible_to_public(page, msg_name, timeout_ms=15000)
        assert is_visible, (
            f"After toggling INACTIVE → ACTIVE, message {msg_name!r} should "
            f"appear on the public homepage but it did not"
        )
        print(f"[reactivate] >>> Phase B PASS: visible as expected")

    # ---------------------------------------------------------
    # Phase C — toggle back to INACTIVE (the round-trip)
    # ---------------------------------------------------------
    def test_06_toggle_active_back_to_inactive(self, page, react_data):
        msg_name = react_data["msg_name"]
        print(f"\n[reactivate] toggling {msg_name!r} ACTIVE → INACTIVE (round-trip)")

        msgs = MessagesPage(page)
        msgs.click_edit_on_row(msg_name)
        page.wait_for_timeout(800)

        before = msgs.get_status_checked()
        assert before is True, (
            f"Edit drawer opened but status switch is not True (got {before!r}). "
            f"The previous save may not have persisted as ACTIVE."
        )
        before, after = msgs.toggle_status()
        print(f"[reactivate]   status: {before} → {after}")
        assert after is False, (
            f"Expected toggle active→inactive but got {before!r}→{after!r}"
        )

        msgs.click_save_and_confirm()
        page.wait_for_timeout(2000)

    def test_07_inactive_again_NOT_visible_on_public(self, page, react_data):
        msg_name = react_data["msg_name"]
        print(f"\n[reactivate] >>> Phase C check: expecting {msg_name!r} HIDDEN again")
        is_visible = _is_message_visible_to_public(page, msg_name, timeout_ms=10000)
        assert not is_visible, (
            f"After toggling ACTIVE → INACTIVE, message {msg_name!r} should "
            f"be hidden again, but it is still visible — likely a stale-cache "
            f"or async-update bug in the visibility pipeline"
        )
        print(f"[reactivate] >>> Phase C PASS: hidden again — full round-trip "
              f"symmetry confirmed")

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------
    def test_08_cleanup(self, page, react_data):
        msg_name = react_data.get("msg_name")
        if not msg_name:
            return
        print(f"\n[reactivate/cleanup] deleting {msg_name!r}")
        try:
            NavigationPage(page).go_to_messages()
            page.wait_for_timeout(1000)
            msgs = MessagesPage(page)
            msgs.delete_message(msg_name)
            msgs.click_delete_and_confirm()
            page.wait_for_timeout(1500)
            print(f"[reactivate/cleanup] deleted {msg_name!r}")
        except Exception as e:
            print(f"[reactivate/cleanup] failed (non-fatal — orphan picked up "
                  f"by cleanup_orphans): {type(e).__name__}: {e}")
