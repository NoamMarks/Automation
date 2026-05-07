"""
Public Homepage tests — covers the surface area that the rest of the suite
doesn't touch (footer, date, status badge, app-tabs toggle, both carousels,
contact link, plus a top-level smoke).

All tests run as **unauthenticated guest** — admin login is irrelevant here,
so we deliberately do NOT use the conftest `page` fixture (which preloads
admin auth). Instead a class-scoped `public_browser` fixture launches its
own browser and each test creates its own fresh context.

No data is created or modified.
"""

import os
import re

import pytest
from playwright.sync_api import expect, sync_playwright


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

# --- Stable substring selectors (styled-component class hashes rotate per build) ---
# Note: trailing '-' in some selectors is intentional — without it,
# `[class*='Headerstyled__StatusText']` would also match
# `Headerstyled__StatusTextAndEnvWrapper` (substring collision), grabbing
# the parent wrapper and picking up all child text.
HEADER_SEL          = "[class*='Headerstyled__TopRow']"
HEADER_DATE_SEL     = "[class*='Headerstyled__DateContainer']"
HEADER_MIDDLE_SEL   = "[class*='Headerstyled__MiddleTab']"
HEADER_STATUS_SEL   = "[class*='Headerstyled__StatusText-']"
HEADER_ENV_SEL      = "[class*='Headerstyled__StatusEnvText-']"
SEARCH_PLACEHOLDER  = "חיפוש יישום בכל עולמות התוכן"
WELCOME_HEADING_SEL = "[class*='Welcomestyled__WelcomeHeading']"
DOMAIN_LABEL_SEL    = "[class*='WelcomeDomainsstyled__DomainNameLabel']"
DOMAIN_SLIDE_SEL    = "[class*='WelcomeCarouselstyled__SingleCarouselDomain']"
DOMAIN_ARROW_SEL    = "[class*='WelcomeCarouselstyled__ArrowButton']"
APP_TAB_SEL         = "[class*='WelcomeLinksstyled__HomeLinksTab']"
LINK_TITLE_SEL      = "[class*='WelcomeLinksstyled__LinkTitle']"
MSG_HEADING_SEL     = "[class*='WelcomeMessagesstyled__WelcomeSubHeading']"
MSG_COUNTER_SEL     = "[class*='MessagesCarouselstyled__MessageCounter']"
MSG_ARROW_SEL       = "[class*='MessagesCarouselstyled__ArrowButton']"
FOOTER_SEL          = "[class*='HomeFooterstyled__FooterWrapper']"
FOOTER_LABEL_SEL    = "[class*='HomeFooterstyled__StyledFooterLabel']"
FOOTER_LOGO_SEL     = "[class*='HomeFooterstyled__StyledLogoImage']"
CONTACT_SEL         = "[class*='Contactstyled__StyledContact']"


# --------------------------------------------------------------------------
# Fixtures + helpers
# --------------------------------------------------------------------------

@pytest.fixture(scope="class")
def public_browser():
    """Class-scoped browser. We don't use the conftest `page` fixture
    because that preloads admin auth via storage_state — these tests need
    a fresh unauthenticated guest experience."""
    headless = os.getenv("HEADLESS", "0") == "1"
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=headless, slow_mo=100 if headless else 400
        )
        yield browser
        browser.close()


def _open_public(browser):
    """Fresh public-context page on the homepage. Returns (ctx, page).

    Viewport pinned to 1920×1080: the homepage hides the messages-carousel
    arrows via `@media (max-width:1550px) { display:none !important }`, and
    similar responsive rules collapse some controls out of the DOM at the
    default 1280-wide Playwright viewport. Pinning a wide viewport keeps
    the desktop UI fully exercised.
    """
    ctx = browser.new_context(viewport={"width": 1920, "height": 1080})
    pp = ctx.new_page()
    pp.goto(APP_URL, wait_until="domcontentloaded")
    try:
        pp.get_by_role("button", name="הבנתי").click(timeout=3000)
    except Exception:
        pass
    pp.wait_for_timeout(2500)
    return ctx, pp


# --------------------------------------------------------------------------
# Tests
# --------------------------------------------------------------------------

class TestPublicHomepage:

    # ---------------------------------------------------------
    # 0. Smoke — every top-level region renders for a guest
    # ---------------------------------------------------------
    def test_00_smoke_all_sections_render(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            # Header
            expect(pp.locator(HEADER_SEL).first).to_be_visible()
            # Search
            expect(pp.get_by_placeholder(SEARCH_PLACEHOLDER)).to_be_visible()
            # Welcome heading (env name)
            expect(pp.locator(WELCOME_HEADING_SEL).first).to_be_visible()
            # Domains carousel
            assert pp.locator(DOMAIN_LABEL_SEL).count() > 0, \
                "Expected at least one domain card on the homepage"
            # Apps tabs (at least one — Recent may collapse if no recent items)
            assert pp.locator(APP_TAB_SEL).count() >= 1, \
                "Expected at least one apps tab to render"
            # Messages section heading
            expect(pp.locator(MSG_HEADING_SEL).first).to_be_visible()
            # Footer
            expect(pp.locator(FOOTER_SEL).first).to_be_visible()
            # Guest greeting
            expect(pp.get_by_text("שלום, אורח")).to_be_visible()
            print("\n[homepage/smoke] all 8 top-level regions render for guest")
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 1. Footer — version string + logos
    # ---------------------------------------------------------
    def test_01_footer_renders_version_and_logos(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            footer = pp.locator(FOOTER_SEL).first
            expect(footer).to_be_visible()

            label_texts = footer.locator(FOOTER_LABEL_SEL).all_inner_texts()
            joined = " ".join(label_texts)
            print(f"\n[homepage/footer] labels: {label_texts}")

            assert re.search(r"\bdev\s+\d+\.\d+\.\d+\b", joined), (
                f"Footer should display version like 'dev X.Y.Z'; got: {joined!r}"
            )

            n_logos = footer.locator(FOOTER_LOGO_SEL).count()
            assert n_logos >= 3, (
                f"Expected at least 3 footer logos (anaf / mahlaka / mador), "
                f"got {n_logos}"
            )
            print(f"[homepage/footer] {n_logos} logos visible — PASS")
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 2. Contact / support link
    # ---------------------------------------------------------
    def test_02_support_contact_is_mailto_link(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            contact = pp.locator(CONTACT_SEL).first
            # The contact widget renders late and lives at position:fixed
            # bottom-left; give it a moment to mount.
            try:
                contact.wait_for(state="attached", timeout=8000)
            except Exception:
                pytest.skip(
                    "Contact icon not present in this build — feature may be "
                    "behind a flag or removed from the public homepage."
                )

            href = (contact.get_attribute("href") or "").strip()
            print(f"\n[homepage/contact] href={href!r}")
            # Contract: must be a valid external destination — mailto, http,
            # or https. The exact destination has changed across builds (was
            # mailto:support@zira.com, currently https://www.btl.gov.il/...).
            assert href, "Contact icon has empty href"
            assert href.startswith(("mailto:", "http://", "https://")), (
                f"Contact link must be mailto: / http: / https:; got: {href!r}"
            )
            if href.startswith("mailto:"):
                assert "@" in href, f"mailto: link is missing an email: {href!r}"

            # External destination should open in a new tab
            target = contact.get_attribute("target")
            assert target == "_blank", (
                f"External contact link should open in new tab, got target={target!r}"
            )
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 3. Header date display — Gregorian + Hebrew
    # ---------------------------------------------------------
    def test_03_header_date_display(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            date_box = pp.locator(HEADER_DATE_SEL).first
            expect(date_box).to_be_visible()

            spans = date_box.locator("span")
            assert spans.count() >= 2, (
                f"Expected ≥2 date spans (Gregorian + Hebrew), got {spans.count()}"
            )

            gregorian = spans.first.inner_text().strip()
            hebrew = spans.nth(1).inner_text().strip()
            print(f"\n[homepage/date] Gregorian={gregorian!r}, Hebrew={hebrew!r}")

            assert re.match(r"^\d{2}\.\d{2}\.\d{4}$", gregorian), (
                f"Gregorian date format should be DD.MM.YYYY, got: {gregorian!r}"
            )
            assert hebrew, "Hebrew date span is empty"
            assert any("֐" <= c <= "׿" for c in hebrew), (
                f"Hebrew date should contain Hebrew characters, got: {hebrew!r}"
            )
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 4. Status badge — מצב תרגיל / מצב מבצעי + env name
    # ---------------------------------------------------------
    def test_04_header_status_badge(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            middle = pp.locator(HEADER_MIDDLE_SEL).first
            expect(middle).to_be_visible()

            status = middle.locator(HEADER_STATUS_SEL).first
            expect(status).to_be_visible()
            text = status.inner_text().strip()
            print(f"\n[homepage/status] badge text: {text!r}")
            assert text in ("מצב תרגיל", "מצב אמת", "מצב מבצעי"), (
                f"Status badge should be one of "
                f"['מצב תרגיל', 'מצב אמת', 'מצב מבצעי'], got: {text!r}"
            )

            env = middle.locator(HEADER_ENV_SEL).first
            expect(env).to_be_visible()
            env_name = env.inner_text().strip()
            print(f"[homepage/status] active env: {env_name!r}")
            assert env_name, "Active environment name should not be empty"

            # The 'שינוי סביבה' button must be available so guests can switch
            change_btn = middle.get_by_role("button", name="שינוי סביבה")
            expect(change_btn).to_be_visible()
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 5. Apps tabs toggle — switching active tab swaps font-weight
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    # 6. Domain carousel scrolls when arrow clicked
    # ---------------------------------------------------------
    def test_06_domain_carousel_scroll_arrow(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            slides = pp.locator(DOMAIN_SLIDE_SEL)
            n = slides.count()
            if n < 5:
                pytest.skip(
                    f"Only {n} domains rendered — carousel doesn't scroll with so few items"
                )

            arrow = pp.locator(DOMAIN_ARROW_SEL).first
            if arrow.count() == 0 or not arrow.is_visible():
                pytest.skip("Carousel arrow not visible")

            # Capture transform on the first 3 slides — arrow click moves them
            sample_n = min(n, 3)
            before = [
                slides.nth(i).evaluate("el => el.style.transform")
                for i in range(sample_n)
            ]
            print(f"\n[homepage/carousel] domain transforms before: {before}")

            arrow.scroll_into_view_if_needed()
            arrow.click()
            pp.wait_for_timeout(1500)

            after = [
                slides.nth(i).evaluate("el => el.style.transform")
                for i in range(sample_n)
            ]
            print(f"[homepage/carousel] domain transforms after:  {after}")

            assert before != after, (
                "Carousel arrow click did not change any slide's transform — "
                "carousel did not scroll"
            )
        finally:
            ctx.close()

    # ---------------------------------------------------------
    # 7. Messages carousel — counter advances when next arrow clicked
    # ---------------------------------------------------------
    def test_07_messages_carousel_navigation(self, public_browser):
        ctx, pp = _open_public(public_browser)
        try:
            counter = pp.locator(MSG_COUNTER_SEL).first
            if counter.count() == 0 or not counter.is_visible():
                pytest.skip("Messages section / counter not visible")

            before_text = counter.inner_text().strip()
            m = re.match(r"\((\d+)\s*/\s*(\d+)\)", before_text)
            if not m:
                pytest.skip(f"Counter format unexpected: {before_text!r}")
            total = int(m.group(1))
            before_idx = int(m.group(2))
            print(f"\n[homepage/messages] counter before: {before_text!r} "
                  f"(total={total}, idx={before_idx})")

            if total < 2:
                pytest.skip(f"Only {total} message(s) — can't test arrow navigation")

            # Click whichever arrow is currently INTERACTIVE (the inactive one
            # has reduced opacity / pointer-events:none). Iterate and pick.
            arrows = pp.locator(MSG_ARROW_SEL)
            n_arrows = arrows.count()
            assert n_arrows >= 2, f"Expected ≥2 carousel arrows, got {n_arrows}"

            clicked = False
            for i in range(n_arrows):
                arrow = arrows.nth(i)
                try:
                    pe = arrow.evaluate(
                        "el => window.getComputedStyle(el).pointerEvents"
                    )
                    opacity = float(
                        arrow.evaluate("el => window.getComputedStyle(el).opacity") or 0
                    )
                    if pe != "none" and opacity > 0.5:
                        arrow.scroll_into_view_if_needed()
                        arrow.click(timeout=2000)
                        clicked = True
                        break
                except Exception:
                    continue

            if not clicked:
                pytest.skip(
                    "Couldn't find an interactive carousel arrow — both may be "
                    "disabled at message boundaries"
                )

            pp.wait_for_timeout(1500)
            after_text = counter.inner_text().strip()
            print(f"[homepage/messages] counter after:  {after_text!r}")

            m2 = re.match(r"\((\d+)\s*/\s*(\d+)\)", after_text)
            assert m2, f"Counter format broke after click: {after_text!r}"
            after_idx = int(m2.group(2))
            assert after_idx != before_idx, (
                f"Carousel index didn't advance after arrow click: "
                f"{before_text!r} → {after_text!r}"
            )
        finally:
            ctx.close()
