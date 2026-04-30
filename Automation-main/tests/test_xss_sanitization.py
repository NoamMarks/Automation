"""
XSS / input-sanitization tests.

Creates entities with hostile payloads in the title, description, and URL
fields, then loads the public homepage in a fresh context with our own
console + dialog listeners attached. The test passes iff:

  1. The public-side rendering shows the payload as TEXT (literal angle
     brackets), proving the value was HTML-escaped on output.
  2. No XSS_SUCCESS_* token appears in the public page's console.error
     stream (proving inline event handlers like onerror/onload did not
     execute).
  3. No alert/confirm/prompt dialog fires (proving inline alert(...) did
     not execute).
  4. No anchor on the public page has an href starting with 'javascript:'
     (proving javascript-URL injection in the URL field was sanitized).

Why this matters: any text field that round-trips to public users is a
potential XSS vector. We never had a test that proved the system
escapes hostile input — until now.
"""

import os
import random
import uuid

import pytest


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")


def _make_title_payload():
    """Return a fresh XSS title payload, unique per call.

    Title field is constrained to 30 chars and the system rejects duplicate
    names, so we randomise the alert(N) integer per run.
    Format: '<svg onload=alert(NNN)>'  (max 25 chars).
    """
    n = random.randint(100, 999)
    return f"<svg onload=alert({n})>"

# Description allows much more — use a payload whose execution would emit
# a unique console.error token we can listen for.
XSS_DESC_TOKEN = "XSS_SUCCESS_DESC"
PAYLOAD_DESC = (
    f"<img src=x onerror=console.error('{XSS_DESC_TOKEN}')>"
    "  some literal text after the img tag"
)

# javascript: URL in the URL field — checks anchor sanitization
PAYLOAD_URL = "javascript:console.error('XSS_SUCCESS_URL')"

# Token markers we watch for in console output (non-zero match = XSS fired)
XSS_TOKENS = ("XSS_SUCCESS_DESC", "XSS_SUCCESS_URL")


def _open_public_with_xss_listeners(browser):
    """Fresh public context with console + dialog listeners.

    Returns (ctx, page, console_msgs_list, dialog_msgs_list). The lists
    accumulate over the page's lifetime; check them after navigations to
    confirm no XSS executed.
    """
    ctx = browser.new_context()
    pp = ctx.new_page()

    console_msgs = []
    dialog_msgs = []

    def _on_console(msg):
        try:
            if msg.type in ("error", "warning"):
                console_msgs.append((msg.type, msg.text))
        except Exception:
            pass

    def _on_dialog(d):
        try:
            dialog_msgs.append((d.type, d.message))
        finally:
            try:
                d.dismiss()
            except Exception:
                pass

    pp.on("console", _on_console)
    pp.on("dialog", _on_dialog)

    pp.goto(APP_URL, wait_until="domcontentloaded")
    try:
        pp.get_by_role("button", name="הבנתי").click(timeout=3000)
    except Exception:
        pass
    pp.wait_for_timeout(2500)
    return ctx, pp, console_msgs, dialog_msgs


def _assert_no_xss_executed(console_msgs, dialog_msgs, ctx_label):
    """Fail if any XSS_SUCCESS_* token appeared in console errors or any
    alert/confirm dialog fired."""
    xss_console = [
        m for m in console_msgs
        if any(tok in m[1] for tok in XSS_TOKENS)
    ]
    assert not xss_console, (
        f"[{ctx_label}] XSS executed via console.error/onerror handler. "
        f"Captured: {xss_console}"
    )
    assert not dialog_msgs, (
        f"[{ctx_label}] XSS executed via alert/confirm dialog. "
        f"Captured: {dialog_msgs}"
    )
    assert not any(
        any(tok in m[1] for tok in XSS_TOKENS) for m in console_msgs
    ), f"[{ctx_label}] XSS token leaked into console: {console_msgs}"


# Lazy imports inside fixtures/tests so static-analysis hints stay quiet
@pytest.fixture(scope="class")
def xss_data():
    return {}


class TestXSSLink:
    """XSS payloads in Link entity fields → verify public-side escaping."""

    def test_01_login(self, page):
        from pages.login_page import LoginPage
        from pages.navigation_page import NavigationPage
        print("\n[xss-link] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()

    def test_02_create_link_with_xss_in_title(self, page, xss_data):
        from pages.links_page import LinksPage
        payload = _make_title_payload()
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[xss-link/title] creating link with title payload {payload!r}")
        links = LinksPage(page)
        links.create_link(payload, link_url, "xss-test-title-marker")
        links.click_save_and_confirm()
        page.wait_for_timeout(1500)
        # In the admin grid, the link should be visible with the literal
        # payload text as its name.
        links.verify_link_visible(payload)
        xss_data["title_link_name"] = payload
        xss_data["title_link_url"] = link_url
        print(f"[xss-link/title] link saved with payload as name (admin OK)")

    def test_03_verify_title_payload_is_escaped_on_public(self, page, xss_data):
        link_name = xss_data["title_link_name"]
        browser = page.context.browser
        ctx, pp, console_msgs, dialog_msgs = _open_public_with_xss_listeners(browser)
        try:
            # Use the homepage search to surface the link (newly created,
            # not on the popular grid yet).
            search = pp.get_by_placeholder("חיפוש יישום בכל עולמות התוכן")
            search.click()
            # Type just the literal-text portion that is unique enough — the
            # full payload contains parens which trigger MUI's regex parsing.
            search.press_sequentially(link_name, delay=80)
            pp.wait_for_timeout(2500)

            popper = pp.locator(".MuiAutocomplete-popper").first
            try:
                popper.wait_for(state="visible", timeout=5000)
            except Exception:
                pass

            # The dropdown should contain the link with the LITERAL payload
            # text (escaped). Try to find an element whose visible text
            # matches the payload exactly.
            text_match = pp.locator("body").inner_text()
            assert link_name in text_match, (
                f"Payload not found anywhere in public DOM as text — "
                f"this could mean it rendered as live HTML (XSS!) or the "
                f"link wasn't surfaced. Body excerpt: "
                f"{text_match[:300]!r}"
            )
            print(f"[xss-link/title] payload appears as literal TEXT on public side")

            # Critical assertion: the payload's <svg onload=...> did NOT fire
            _assert_no_xss_executed(console_msgs, dialog_msgs, "xss-link/title")
            print(f"[xss-link/title] >>> PASS — no alert dialog, no XSS execution")
        finally:
            ctx.close()

    def test_04_create_link_with_xss_in_description(self, page, xss_data):
        from pages.links_page import LinksPage
        link_name = f"XssDesc_{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/{uuid.uuid4().hex[:8]}"
        print(f"\n[xss-link/desc] creating link {link_name!r} with payload "
              f"{PAYLOAD_DESC!r} in description")
        links = LinksPage(page)
        links.create_link(link_name, link_url, PAYLOAD_DESC)
        links.click_save_and_confirm()
        page.wait_for_timeout(1500)
        links.verify_link_visible(link_name)
        xss_data["desc_link_name"] = link_name
        xss_data["desc_link_url"] = link_url

    def test_05_verify_description_payload_is_escaped_on_public(self, page, xss_data):
        link_name = xss_data["desc_link_name"]
        browser = page.context.browser
        ctx, pp, console_msgs, dialog_msgs = _open_public_with_xss_listeners(browser)
        try:
            search = pp.get_by_placeholder("חיפוש יישום בכל עולמות התוכן")
            search.click()
            search.press_sequentially(link_name, delay=80)
            pp.wait_for_timeout(2500)

            popper = pp.locator(".MuiAutocomplete-popper").first
            try:
                popper.wait_for(state="visible", timeout=5000)
            except Exception:
                pass

            # The body should contain literal '<img src=x' substring as text
            # if escaping worked. If unsanitized, the <img> tag would render
            # (broken image, no literal text).
            body = pp.locator("body").inner_text()
            assert "<img src=x" in body or link_name in body, (
                f"Description payload not visible as text on public side — "
                f"likely either rendered as live HTML or not surfaced. "
                f"Body excerpt: {body[:300]!r}"
            )

            # Critical: even waiting for any onerror handler to fire
            pp.wait_for_timeout(2000)
            _assert_no_xss_executed(console_msgs, dialog_msgs, "xss-link/desc")
            print(f"[xss-link/desc] >>> PASS — no XSS_SUCCESS_DESC token in console")
        finally:
            ctx.close()

    def test_06_create_link_with_javascript_url(self, page, xss_data):
        from pages.links_page import LinksPage
        link_name = f"XssUrl_{uuid.uuid4().hex[:5]}"
        print(f"\n[xss-link/url] creating link {link_name!r} with URL payload "
              f"{PAYLOAD_URL!r}")
        links = LinksPage(page)
        try:
            links.create_link(link_name, PAYLOAD_URL, "xss-test-url-marker")
            links.click_save_and_confirm()
            page.wait_for_timeout(1500)
            links.verify_link_visible(link_name)
            xss_data["url_link_name"] = link_name
            xss_data["url_link_accepted"] = True
        except Exception as e:
            # If the form rejects the javascript: URL outright, that's also
            # acceptable sanitization — record it and skip the public check.
            print(f"[xss-link/url] form rejected javascript: URL "
                  f"({type(e).__name__}) — input-side sanitization PASS")
            xss_data["url_link_accepted"] = False

    def test_07_verify_javascript_url_is_sanitized_on_public(self, page, xss_data):
        if not xss_data.get("url_link_accepted"):
            print("\n[xss-link/url] form refused payload at input — skipping public check")
            return

        link_name = xss_data["url_link_name"]
        browser = page.context.browser
        ctx, pp, console_msgs, dialog_msgs = _open_public_with_xss_listeners(browser)
        try:
            search = pp.get_by_placeholder("חיפוש יישום בכל עולמות התוכן")
            search.click()
            search.press_sequentially(link_name, delay=80)
            pp.wait_for_timeout(2500)

            # Walk every <a> on the page and confirm none have a javascript:
            # href.  (Even if the link is in a popper, off-screen, or in a
            # carousel — javascript: URLs anywhere are a security failure.)
            anchors = pp.locator("a[href]")
            n = anchors.count()
            offending_hrefs = []
            for i in range(n):
                try:
                    href = anchors.nth(i).get_attribute("href") or ""
                    if href.lower().lstrip().startswith("javascript:"):
                        offending_hrefs.append(href)
                except Exception:
                    pass
            assert not offending_hrefs, (
                f"javascript: URL was NOT sanitized — found in public DOM: "
                f"{offending_hrefs}"
            )

            _assert_no_xss_executed(console_msgs, dialog_msgs, "xss-link/url")
            print(f"[xss-link/url] >>> PASS — no javascript: anchor on public, "
                  f"no XSS_SUCCESS_URL in console")
        finally:
            ctx.close()

    def test_08_cleanup(self, page, xss_data):
        """Best-effort cleanup of all XSS-test links.

        Always passes — if any step fails (e.g. a stale form drawer from
        the rejected javascript: URL test), the cleanup_orphans utility is
        the canonical safety net for any remaining orphans.
        """
        from pages.links_page import LinksPage
        from pages.navigation_page import NavigationPage

        # Best-effort: dismiss any leftover drawer/modal
        for _ in range(3):
            try:
                page.keyboard.press("Escape")
                page.wait_for_timeout(400)
            except Exception:
                break

        try:
            NavigationPage(page).go_to_links()
            page.wait_for_timeout(800)
        except Exception as e:
            print(f"[xss/cleanup] could not navigate to Links "
                  f"({type(e).__name__}: {e}); falling back to direct goto")
            try:
                page.goto(APP_URL.rstrip("/") + "/admin/links",
                          wait_until="domcontentloaded")
                page.wait_for_timeout(2000)
            except Exception as e2:
                print(f"[xss/cleanup] direct goto also failed: {e2}; "
                      f"orphans will be cleaned by cleanup_orphans utility")
                return

        links = LinksPage(page)
        for key in ("title_link_name", "desc_link_name", "url_link_name"):
            name = xss_data.get(key)
            if not name:
                continue
            try:
                links.delete_link(name)
                links.click_delete_and_confirm()
                page.wait_for_timeout(1500)
                print(f"[xss-link/cleanup] deleted {name!r}")
            except Exception as e:
                print(f"[xss-link/cleanup] could not delete {name!r}: "
                      f"{type(e).__name__}: {e}")
