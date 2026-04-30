"""
Cascade / referential-integrity tests — expanded.

Documents the *contracted* behavior for each parent-child combination
(per business spec):
  - Domain → Link  : silent CASCADE  (no warning about dependent links;
                                       deleting the domain wipes its links)
  - Tag → Link     : NULLIFY         (tag deleted, link survives)
  - Environment → Link : NULLIFY     (env deleted, link survives)
  - Tag → Message  : N/A             (message form does not expose tag
                                       selection; dependency cannot exist)

Outcomes:
    BLOCK   — system refused to delete the parent while a child references it
    NULLIFY — parent deleted, dependent child survived (reference cleared)
    CASCADE — parent and child both deleted
"""

import uuid

import pytest

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage
from pages.domains_page import DomainsPage
from pages.tags_page import TagsPage
from pages.messages_page import MessagesPage
from pages.environments_page import EnvironmentsPage
from utils.image_gen import make_png_bytes


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------

def _attempt_delete_via_modal(page, label):
    """After click_delete_on_row, dump the confirm-dialog text and click the
    מחיקה → אישור buttons (whichever appear). Captures any toasts after."""
    page.wait_for_timeout(1000)

    dialog = page.locator(".MuiDialog-root, .MuiModal-root").first
    try:
        if dialog.count() > 0 and dialog.is_visible():
            txt = dialog.inner_text().strip().replace("\n", " | ")[:240]
            print(f"[{label}] confirm dialog text: {txt!r}")
    except Exception:
        pass

    try:
        page.get_by_role("button", name="מחיקה").first.click(timeout=3000)
        print(f"[{label}] clicked מחיקה")
    except Exception as e:
        print(f"[{label}] could not click מחיקה: {type(e).__name__}: {e}")

    page.wait_for_timeout(800)

    try:
        page.get_by_role("button", name="אישור").first.click(timeout=3000)
        print(f"[{label}] clicked אישור")
    except Exception as e:
        print(f"[{label}] no אישור button (may already have closed): "
              f"{type(e).__name__}: {e}")

    page.wait_for_timeout(2500)


def _capture_toasts(page, label):
    for sel in (".MuiSnackbar-root", ".Toastify__toast", "[role='alert']", ".MuiAlert-root"):
        n = page.locator(sel).count()
        for i in range(n):
            try:
                txt = page.locator(sel).nth(i).inner_text().strip()
                if txt:
                    print(f"[{label}] toast {sel}[{i}]: {txt!r}")
            except Exception:
                pass


# ============================================================
# 0. Domain → Link cascade  (contract: silent CASCADE)
# ============================================================

@pytest.fixture(scope="class")
def domain_link_data():
    return {}


# Hebrew/English keywords that, if present in the delete-confirm dialog,
# would indicate the system warns the user about cascading link deletion.
# A SILENT cascade (the contracted behavior) MUST NOT include any of these.
CASCADE_WARNING_KEYWORDS = (
    "קישור",          # 'link' (Hebrew) — would appear in any dependent-warning text
    "ימחק גם",        # 'will also be deleted' (Hebrew)
    "תלוי",           # 'depends' (Hebrew)
    "links",          # English fallback
    "will also delete",
    "dependent",
)


class TestDomainLinkCascade:
    """Asserts the spec'd silent CASCADE behavior: deleting a Domain wipes
    its dependent Links *without* a warning dialog about the cascade.

    Standard 'are you sure?' confirmation is allowed — what is NOT allowed
    is any text alerting the admin that linked entities will also be wiped.
    """

    def test_01_login(self, page):
        print("\n[dom-link] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

    def test_02_create_domain(self, page, domain_link_data):
        domain_name = f"CasDom{uuid.uuid4().hex[:6]}"
        print(f"\n[dom-link] creating domain {domain_name!r}")
        NavigationPage(page).go_to_content_worlds()
        domains = DomainsPage(page)
        domains.create_domain(domain_name)
        domains.click_save_and_confirm()
        domains.verify_domain_visible(domain_name)
        domain_link_data["domain_name"] = domain_name

    def test_03_create_link_with_domain(self, page, domain_link_data):
        domain_name = domain_link_data["domain_name"]
        link_name = f"CasLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[dom-link] creating link {link_name!r} attached to domain {domain_name!r}")

        NavigationPage(page).go_to_links()
        links = LinksPage(page)
        links.open_add_link_dialog()
        links.fill_link_form(link_name, link_url, "domain-link cascade contract test")
        # Combobox 0 = Domains. Pick our specific newly-created domain.
        links.select_option_by_name(domain_name, combobox_index=0)
        print(f"[dom-link] selected domain {domain_name!r} in combobox 0")

        links.click_save_and_confirm()
        links.verify_link_visible(link_name)
        domain_link_data["link_name"] = link_name

    def test_04_delete_domain_asserts_silent_cascade(self, page, domain_link_data):
        domain_name = domain_link_data["domain_name"]
        link_name = domain_link_data["link_name"]
        print(f"\n[dom-link] >>> deleting domain {domain_name!r} — expecting "
              f"silent CASCADE (link {link_name!r} should also be wiped, "
              f"with NO cascade-warning dialog)")

        NavigationPage(page).go_to_content_worlds()
        page.wait_for_timeout(1000)
        domains = DomainsPage(page)
        try:
            domains.click_delete_on_row(domain_name)
        except Exception as e:
            print(f"[dom-link] couldn't click delete on row: {type(e).__name__}: {e}")

        # Capture the confirm dialog text BEFORE clicking through, so we can
        # verify the 'silent' part of the contract.
        page.wait_for_timeout(1000)
        dialog_text = ""
        dialog = page.locator(".MuiDialog-root, .MuiModal-root").first
        try:
            if dialog.count() > 0 and dialog.is_visible():
                dialog_text = dialog.inner_text().strip()
                print(f"[dom-link] confirm dialog text: "
                      f"{dialog_text.replace(chr(10), ' | ')[:240]!r}")
        except Exception:
            pass

        _attempt_delete_via_modal(page, "dom-link")
        _capture_toasts(page, "dom-link")

        # Re-navigate to refresh data and check final state
        NavigationPage(page).go_to_content_worlds()
        page.wait_for_timeout(1500)
        domain_present = page.get_by_text(domain_name, exact=True).count() > 0
        print(f"[dom-link] domain still present: {domain_present}")

        NavigationPage(page).go_to_links()
        page.wait_for_timeout(1500)
        link_present = page.locator(
            "[class*='SingleLinkstyled__StyledLinkName']", has_text=link_name
        ).count() > 0
        print(f"[dom-link] link still present: {link_present}")

        # Classify outcome for the summary
        if domain_present:
            outcome = "BLOCK"
        elif link_present:
            outcome = "NULLIFY"
        else:
            outcome = "CASCADE"
        domain_link_data["outcome"] = outcome
        domain_link_data["dialog_text"] = dialog_text
        print(f"[dom-link] >>> OUTCOME: {outcome}")

        # ----- Assert the spec'd contract -----
        # 1) Both parent and child must be gone (CASCADE).
        assert outcome == "CASCADE", (
            f"Domain → Link contract violated: expected CASCADE "
            f"(both deleted) but got {outcome} "
            f"(domain_present={domain_present}, link_present={link_present})"
        )

        # 2) The confirmation dialog (if any) must NOT mention dependent
        #    links — the cascade must be silent per spec. A standard
        #    'are you sure you want to delete this content world?' dialog
        #    is acceptable; a 'this will also delete N links' warning is not.
        dialog_lower = dialog_text.lower()
        offending = [w for w in CASCADE_WARNING_KEYWORDS if w.lower() in dialog_lower]
        assert not offending, (
            f"Domain → Link contract violated: cascade is supposed to be "
            f"SILENT but the confirm dialog warned about cascading effects "
            f"(matched keywords: {offending}). Dialog text: {dialog_text!r}"
        )
        print(f"[dom-link] >>> CONTRACT PASS: silent CASCADE confirmed "
              f"(no dependent-warning keywords in dialog)")

    def test_05_summary(self, domain_link_data):
        print("\n" + "=" * 60)
        print(f"[dom-link] FINAL OUTCOME: {domain_link_data.get('outcome', 'UNKNOWN')}")
        print(f"[dom-link]   domain      : {domain_link_data.get('domain_name')}")
        print(f"[dom-link]   link        : {domain_link_data.get('link_name')}")
        print(f"[dom-link]   dialog text : {(domain_link_data.get('dialog_text') or '')[:160]!r}")
        print("=" * 60)


# ============================================================
# 1. Tag → Link cascade
# ============================================================

@pytest.fixture(scope="class")
def tag_link_data():
    return {}


class TestTagLinkCascade:

    def test_01_login(self, page):
        print("\n[tag-link] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

    def test_02_create_tag(self, page, tag_link_data):
        tag_name = f"CasTag{uuid.uuid4().hex[:6]}"
        print(f"\n[tag-link] creating tag {tag_name!r}")
        NavigationPage(page).go_to_tags()
        tags = TagsPage(page)
        tags.create_tag(tag_name)
        tags.click_save_and_confirm()
        tags.verify_tag_visible(tag_name)
        tag_link_data["tag_name"] = tag_name

    def test_03_create_link_with_tag(self, page, tag_link_data):
        tag_name = tag_link_data["tag_name"]
        link_name = f"CasLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[tag-link] creating link {link_name!r} attached to tag {tag_name!r}")

        NavigationPage(page).go_to_links()
        links = LinksPage(page)
        links.open_add_link_dialog()
        links.fill_link_form(link_name, link_url, "tag-link cascade test")
        links.select_combobox_options(combobox_index=0, count=3)  # 3 domains
        # Combobox 1 = Tags. Pick our specific newly-created tag.
        links.select_option_by_name(tag_name, combobox_index=1)
        print(f"[tag-link] selected tag {tag_name!r} in combobox 1")

        links.click_save_and_confirm()
        links.verify_link_visible(link_name)
        tag_link_data["link_name"] = link_name
        print("[tag-link] link created with tag attached")

    def test_04_delete_tag_and_observe(self, page, tag_link_data):
        tag_name = tag_link_data["tag_name"]
        link_name = tag_link_data["link_name"]
        print(f"\n[tag-link] >>> attempting to delete tag {tag_name!r} "
              f"(link {link_name!r} depends on it)")

        NavigationPage(page).go_to_tags()
        page.wait_for_timeout(1000)
        tags = TagsPage(page)
        try:
            tags.click_delete_on_row(tag_name)
        except Exception as e:
            print(f"[tag-link] couldn't click delete on row: {type(e).__name__}: {e}")

        _attempt_delete_via_modal(page, "tag-link")
        _capture_toasts(page, "tag-link")

        # Re-navigate to refresh data, then check parent + child presence
        NavigationPage(page).go_to_tags()
        page.wait_for_timeout(1500)
        tag_present = page.locator(f"span[title='{tag_name}']").count() > 0
        print(f"[tag-link] tag {tag_name!r} still present: {tag_present}")

        if tag_present:
            outcome = "BLOCK"
            print("[tag-link] >>> OUTCOME: BLOCK — system refused to delete "
                  "the tag while a link references it")
        else:
            NavigationPage(page).go_to_links()
            page.wait_for_timeout(1500)
            link_present = page.locator(
                "[class*='SingleLinkstyled__StyledLinkName']", has_text=link_name
            ).count() > 0
            print(f"[tag-link] link {link_name!r} still present: {link_present}")
            if link_present:
                outcome = "NULLIFY"
                print("[tag-link] >>> OUTCOME: NULLIFY — tag deleted, "
                      "dependent link survived (reference cleared)")
            else:
                outcome = "CASCADE"
                print("[tag-link] >>> OUTCOME: CASCADE — tag and dependent "
                      "link both deleted")

        tag_link_data["outcome"] = outcome

    def test_05_summary(self, tag_link_data):
        print("\n" + "=" * 60)
        print(f"[tag-link] FINAL OUTCOME: {tag_link_data.get('outcome', 'UNKNOWN')}")
        print(f"[tag-link]   tag : {tag_link_data.get('tag_name')}")
        print(f"[tag-link]   link: {tag_link_data.get('link_name')}")
        print("=" * 60)


# ============================================================
# 2. Environment → Link cascade
# ============================================================

@pytest.fixture(scope="class")
def env_link_data():
    return {}


class TestEnvironmentLinkCascade:

    def test_01_login(self, page):
        print("\n[env-link] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

    def test_02_create_env(self, page, env_link_data):
        env_name = f"CasEnv{uuid.uuid4().hex[:6]}"
        env_param = f"casparam{uuid.uuid4().hex[:6]}"
        print(f"\n[env-link] creating env {env_name!r} (URLParam={env_param!r})")
        NavigationPage(page).go_to_environments()
        envs = EnvironmentsPage(page)
        envs.create_environment(env_name, env_param)
        envs.click_save_and_confirm()
        envs.verify_environment_visible(env_name)
        env_link_data["env_name"] = env_name

    def test_03_create_link_with_env(self, page, env_link_data):
        env_name = env_link_data["env_name"]
        link_name = f"CasLink{uuid.uuid4().hex[:6]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[env-link] creating link {link_name!r} attached to env {env_name!r}")

        NavigationPage(page).go_to_links()
        links = LinksPage(page)
        links.open_add_link_dialog()
        links.fill_link_form(link_name, link_url, "env-link cascade test")
        links.select_combobox_options(combobox_index=0, count=3)  # 3 domains
        # Combobox 2 = Environments. Pick our specific env.
        links.select_option_by_name(env_name, combobox_index=2)
        print(f"[env-link] selected env {env_name!r} in combobox 2")

        links.click_save_and_confirm()
        links.verify_link_visible(link_name)
        env_link_data["link_name"] = link_name
        print("[env-link] link created with env attached")

    def test_04_delete_env_and_observe(self, page, env_link_data):
        env_name = env_link_data["env_name"]
        link_name = env_link_data["link_name"]
        print(f"\n[env-link] >>> attempting to delete env {env_name!r} "
              f"(link {link_name!r} depends on it)")

        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1000)
        envs = EnvironmentsPage(page)
        try:
            envs.click_delete_on_row(env_name)
        except Exception as e:
            print(f"[env-link] couldn't click delete on row: {type(e).__name__}: {e}")

        _attempt_delete_via_modal(page, "env-link")
        _capture_toasts(page, "env-link")

        NavigationPage(page).go_to_environments()
        page.wait_for_timeout(1500)
        env_present = page.locator(
            EnvironmentsPage.NAME_SELECTOR, has_text=env_name
        ).count() > 0
        print(f"[env-link] env {env_name!r} still present: {env_present}")

        if env_present:
            outcome = "BLOCK"
            print("[env-link] >>> OUTCOME: BLOCK — system refused to delete "
                  "the env while a link references it")
        else:
            NavigationPage(page).go_to_links()
            page.wait_for_timeout(1500)
            link_present = page.locator(
                "[class*='SingleLinkstyled__StyledLinkName']", has_text=link_name
            ).count() > 0
            print(f"[env-link] link {link_name!r} still present: {link_present}")
            if link_present:
                outcome = "NULLIFY"
                print("[env-link] >>> OUTCOME: NULLIFY — env deleted, "
                      "dependent link survived (reference cleared)")
            else:
                outcome = "CASCADE"
                print("[env-link] >>> OUTCOME: CASCADE — env and dependent "
                      "link both deleted")

        env_link_data["outcome"] = outcome

    def test_05_summary(self, env_link_data):
        print("\n" + "=" * 60)
        print(f"[env-link] FINAL OUTCOME: {env_link_data.get('outcome', 'UNKNOWN')}")
        print(f"[env-link]   env : {env_link_data.get('env_name')}")
        print(f"[env-link]   link: {env_link_data.get('link_name')}")
        print("=" * 60)


# ============================================================
# 3. Tag → Message cascade  (best-effort)
# ============================================================

@pytest.fixture(scope="class")
def tag_msg_data():
    return {}


class TestTagMessageCascade:
    """Best-effort cascade test for Tag → Message.

    The message form may or may not expose a tag selector. We attempt to
    attach a tag via combobox iteration; if no combobox accepts it, the
    test documents that the dependency cannot be created in the current UI
    and exits with outcome 'N/A_NO_TAG_ON_MESSAGE_FORM' (still tear down
    the orphan tag).
    """

    def test_01_login(self, page):
        print("\n[tag-msg] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

    def test_02_create_tag(self, page, tag_msg_data):
        tag_name = f"CasTag{uuid.uuid4().hex[:6]}"
        print(f"\n[tag-msg] creating tag {tag_name!r}")
        NavigationPage(page).go_to_tags()
        tags = TagsPage(page)
        tags.create_tag(tag_name)
        tags.click_save_and_confirm()
        tags.verify_tag_visible(tag_name)
        tag_msg_data["tag_name"] = tag_name

    def test_03_create_message_attempt_tag(self, page, tag_msg_data):
        tag_name = tag_msg_data["tag_name"]
        msg_name = f"CasMsg{uuid.uuid4().hex[:6]}"
        print(f"\n[tag-msg] creating message {msg_name!r}, attempting to attach tag {tag_name!r}")

        NavigationPage(page).go_to_messages()
        msgs = MessagesPage(page)
        msgs.open_add_message_dialog()
        msgs.fill_message_form(msg_name, "tag-message cascade test")
        msgs.select_type("both")
        msgs.upload_image("cascade.png", make_png_bytes(0.3))

        # Try to attach the tag via combobox iteration. The message form may
        # expose tags as one of several MUI comboboxes — we try each and
        # check whether the dropdown contains our tag option.
        attached = False
        cbs = page.get_by_role("combobox").all()
        print(f"[tag-msg] {len(cbs)} comboboxes on the form")
        for i, cb in enumerate(cbs):
            try:
                cb.scroll_into_view_if_needed(timeout=2000)
                cb.click(timeout=2000)
                page.wait_for_timeout(700)
                opt = page.locator("[role='option']").filter(has_text=tag_name).first
                if opt.count() > 0 and opt.is_visible():
                    opt.click()
                    print(f"[tag-msg] attached tag via combobox[{i}]")
                    attached = True
                    # Dismiss the dropdown without leaving the drawer
                    try:
                        page.locator(".MuiBackdrop-root.MuiBackdrop-invisible").last.click(timeout=2000)
                    except Exception:
                        pass
                    break
                # Close this combobox and try the next
                try:
                    page.locator(".MuiBackdrop-root.MuiBackdrop-invisible").last.click(timeout=1500)
                except Exception:
                    pass
            except Exception as e:
                print(f"[tag-msg] combobox[{i}] interaction failed: {type(e).__name__}: {e}")
                continue

        tag_msg_data["tag_attached_to_message"] = attached
        if not attached:
            print(f"[tag-msg] >>> Could not attach tag to message form. "
                  f"Cascade dependency cannot be created in current UI.")

        msgs.click_save_and_confirm()
        page.wait_for_timeout(2000)
        msgs.verify_message_visible(msg_name)
        tag_msg_data["msg_name"] = msg_name
        print(f"[tag-msg] message {msg_name!r} created (tag_attached={attached})")

    def test_04_delete_tag_and_observe(self, page, tag_msg_data):
        tag_name = tag_msg_data["tag_name"]
        msg_name = tag_msg_data.get("msg_name")

        if not tag_msg_data.get("tag_attached_to_message"):
            print(f"\n[tag-msg] >>> SKIP: no tag→message dependency exists "
                  f"(form did not accept tag attachment)")
            tag_msg_data["outcome"] = "N/A_NO_TAG_ON_MESSAGE_FORM"
            # Still try to delete the orphan tag so cleanup is correct
            try:
                NavigationPage(page).go_to_tags()
                page.wait_for_timeout(1500)
                tags = TagsPage(page)
                tags.delete_tag(tag_name)
                tags.click_delete_and_confirm()
                page.wait_for_timeout(1200)
            except Exception as e:
                print(f"[tag-msg] orphan-tag cleanup failed: {type(e).__name__}: {e}")
            return

        print(f"\n[tag-msg] >>> attempting to delete tag {tag_name!r} "
              f"(message {msg_name!r} depends on it)")

        NavigationPage(page).go_to_tags()
        page.wait_for_timeout(1000)
        tags = TagsPage(page)
        try:
            tags.click_delete_on_row(tag_name)
        except Exception as e:
            print(f"[tag-msg] couldn't click delete on row: {type(e).__name__}: {e}")

        _attempt_delete_via_modal(page, "tag-msg")
        _capture_toasts(page, "tag-msg")

        NavigationPage(page).go_to_tags()
        page.wait_for_timeout(1500)
        tag_present = page.locator(f"span[title='{tag_name}']").count() > 0
        print(f"[tag-msg] tag {tag_name!r} still present: {tag_present}")

        if tag_present:
            outcome = "BLOCK"
            print("[tag-msg] >>> OUTCOME: BLOCK — system refused to delete "
                  "the tag while a message references it")
        else:
            NavigationPage(page).go_to_messages()
            page.wait_for_timeout(1500)
            msg_present = page.locator(
                MessagesPage.TITLE_SELECTOR, has_text=msg_name
            ).count() > 0
            print(f"[tag-msg] message {msg_name!r} still present: {msg_present}")
            if msg_present:
                outcome = "NULLIFY"
                print("[tag-msg] >>> OUTCOME: NULLIFY — tag deleted, "
                      "dependent message survived")
            else:
                outcome = "CASCADE"
                print("[tag-msg] >>> OUTCOME: CASCADE — tag and dependent "
                      "message both deleted")

        tag_msg_data["outcome"] = outcome

    def test_05_summary(self, tag_msg_data):
        print("\n" + "=" * 60)
        print(f"[tag-msg] FINAL OUTCOME: {tag_msg_data.get('outcome', 'UNKNOWN')}")
        print(f"[tag-msg]   tag    : {tag_msg_data.get('tag_name')}")
        print(f"[tag-msg]   message: {tag_msg_data.get('msg_name')}")
        print(f"[tag-msg]   tag attached to msg: "
              f"{tag_msg_data.get('tag_attached_to_message')}")
        print("=" * 60)
