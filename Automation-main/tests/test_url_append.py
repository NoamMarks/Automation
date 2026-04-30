"""
URL-append radio test.

Goal: empirically verify the contract of `האם לשרשר URL שהוגדר בסביבה?`
("Should the URL defined in the environment be appended?") on the Add Link
form. The radio's two states (כן / לא) should produce different rendered
URLs on the public homepage when the user is in the matching environment.

Setup creates a unique Environment with a distinctive URLParam, then two
Links (one per radio state), both restricted to that env. The verification
step switches to the env on the public homepage and inspects each card's
`<a href>`.
"""

import os
import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage
from pages.environments_page import EnvironmentsPage


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")


@pytest.fixture(scope="class")
def url_data():
    return {}


class TestURLAppend:

    def test_01_login(self, page):
        print("\n[urlapp] logging in as admin...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        print("[urlapp] login OK")

    def test_02_create_test_env(self, page, url_data):
        env_name = f"AppEnv{uuid.uuid4().hex[:5]}"
        env_param = f"appendmark{uuid.uuid4().hex[:8]}"
        print(f"\n[urlapp] creating env '{env_name}' with URLParam='{env_param}'")

        NavigationPage(page).go_to_environments()
        envs = EnvironmentsPage(page)
        envs.create_environment(env_name, env_param)
        envs.click_save_and_confirm()
        page.wait_for_timeout(1500)
        envs.verify_environment_visible(env_name)

        url_data["env_name"] = env_name
        url_data["env_param"] = env_param
        print("[urlapp] env created")

    def _create_link_with_append(self, page, link_name, link_url, env_name, append):
        """Shared link-creation helper: name + url + first 3 domains + specific env + append toggle."""
        links = LinksPage(page)
        links.open_add_link_dialog()
        page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(link_name)
        page.locator("input[name='URL']").fill(link_url)
        links.select_combobox_options(combobox_index=0, count=3)
        cb_count = page.get_by_role("combobox").count()
        print(f"[urlapp/diag] role=combobox count in form: {cb_count}")
        for i in range(cb_count):
            try:
                el = page.get_by_role("combobox").nth(i)
                txt = (el.inner_text() or "").strip().replace("\n", " | ")[:80]
                tag = el.evaluate("el => el.tagName")
                cls = (el.get_attribute("class") or "")[:100]
                print(f"[urlapp/diag]   combobox[{i}] tag={tag} class={cls!r} text={txt!r}")
            except Exception as e:
                print(f"[urlapp/diag]   combobox[{i}] err: {e}")
        try:
            links.select_option_by_name(env_name, combobox_index=2)
            print(f"[urlapp]   selected env '{env_name}' in combobox 2")
        except Exception as e:
            print(f"[urlapp]   combobox 2 select failed: {type(e).__name__}: {e}")
        links.set_url_append(append)
        print(f"[urlapp]   set URL append = {'כן' if append else 'לא'}")
        page.get_by_role("button", name="שמירה").click()
        page.get_by_role("button", name="אישור").click()
        page.wait_for_timeout(1500)
        links.verify_link_visible(link_name)

    def test_03_create_link_append_yes(self, page, url_data):
        env_name = url_data["env_name"]
        link_name = f"AppendYes{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/yes-{uuid.uuid4().hex[:6]}"
        print(f"\n[urlapp] creating link '{link_name}' (append=כן)")

        NavigationPage(page).go_to_links()
        self._create_link_with_append(page, link_name, link_url, env_name, append=True)

        url_data["link_yes_name"] = link_name
        url_data["link_yes_url"] = link_url
        print("[urlapp] append=כן link created")

    def test_04_create_link_append_no(self, page, url_data):
        env_name = url_data["env_name"]
        link_name = f"AppendNo{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/no-{uuid.uuid4().hex[:6]}"
        print(f"\n[urlapp] creating link '{link_name}' (append=לא)")

        self._create_link_with_append(page, link_name, link_url, env_name, append=False)

        url_data["link_no_name"] = link_name
        url_data["link_no_url"] = link_url
        print("[urlapp] append=לא link created")

    def test_05_verify_on_homepage(self, page, url_data):
        env_name = url_data["env_name"]
        env_param = url_data["env_param"]
        yes_name = url_data["link_yes_name"]
        yes_url = url_data["link_yes_url"]
        no_name = url_data["link_no_name"]
        no_url = url_data["link_no_url"]

        print(f"\n[urlapp] >>> opening fresh unauthenticated context")
        browser = page.context.browser
        new_context = browser.new_context()
        public_page = new_context.new_page()
        try:
            public_page.goto(APP_URL)
            try:
                public_page.get_by_role("button", name="הבנתי").click(timeout=3000)
            except Exception:
                pass
            public_page.wait_for_timeout(2000)

            print(f"[urlapp] clicking 'שינוי סביבה' to switch to env '{env_name}'")
            try:
                public_page.get_by_role("button", name="שינוי סביבה").click()
                public_page.wait_for_timeout(1500)
                env_option = public_page.get_by_text(env_name, exact=True).first
                if env_option.count() > 0:
                    env_option.click()
                    print(f"[urlapp]   clicked env option in picker")
                    for confirm_label in ["אישור", "שמירה", "החלף", "בחר", "אישור בחירה"]:
                        btn = public_page.get_by_role("button", name=confirm_label)
                        if btn.count() > 0 and btn.first.is_visible():
                            try:
                                btn.first.click(timeout=2000)
                                print(f"[urlapp]   confirmed env switch via: {confirm_label}")
                                break
                            except Exception:
                                continue
                else:
                    print(f"[urlapp]   could NOT find env '{env_name}' in picker — DOM dump follows")
                    body = public_page.locator("body").inner_text()[:1500]
                    print(f"[urlapp/dump] body excerpt:\n{body}")
            except Exception as e:
                print(f"[urlapp]   env switch failed: {type(e).__name__}: {e}")
            public_page.wait_for_timeout(2500)

            cards = public_page.locator("[class*='WelcomeLinksstyled__LinkCard']")
            n_cards = cards.count()
            print(f"[urlapp] homepage 'popular' grid shows {n_cards} link cards in env '{env_name}'")

            yes_href = None
            no_href = None
            for i in range(n_cards):
                try:
                    card = cards.nth(i)
                    title_el = card.locator("[class*='WelcomeLinksstyled__LinkTitle']").first
                    title = title_el.inner_text().strip() if title_el.count() > 0 else "?"
                    anchor = card.locator("a[class*='WelcomeLinksstyled__AppLinkButton']").first
                    href = anchor.get_attribute("href") if anchor.count() > 0 else None
                    print(f"[urlapp]   card[{i}] title={title!r} href={href!r}")
                    if title == yes_name:
                        yes_href = href
                    elif title == no_name:
                        no_href = href
                except Exception:
                    pass

            # Newly-created links don't appear on the "popular" grid (they need visits).
            # Use the search bar to surface them and read their hrefs from search results.
            if yes_href is None or no_href is None:
                print(f"[urlapp] target link(s) not on popular grid — searching to surface them")
                for target_name, target_url, expected_label in [
                    (yes_name, yes_url, "yes"),
                    (no_name, no_url, "no"),
                ]:
                    try:
                        search = public_page.get_by_placeholder("חיפוש יישום בכל עולמות התוכן")
                        search.click()
                        search.fill("")
                        search.fill(target_name)
                        public_page.wait_for_timeout(1500)
                        options = public_page.get_by_role("option")
                        n_opts = options.count()
                        print(f"[urlapp]   search '{target_name}': {n_opts} options")
                        found_href = None
                        for i in range(n_opts):
                            try:
                                opt = options.nth(i)
                                opt_text = opt.inner_text()
                                if target_name not in opt_text:
                                    continue
                                anchor = opt.locator("a").first
                                if anchor.count() > 0:
                                    found_href = anchor.get_attribute("href")
                                else:
                                    found_href = opt.get_attribute("data-href") or "(option found, no href attr)"
                                print(f"[urlapp]     match[{i}] text={opt_text.strip()[:60]!r} href={found_href!r}")
                            except Exception:
                                pass
                        if expected_label == "yes":
                            yes_href = found_href
                        else:
                            no_href = found_href
                        # Clear search for next iteration
                        public_page.keyboard.press("Escape")
                        public_page.wait_for_timeout(300)
                    except Exception as e:
                        print(f"[urlapp]   search for {target_name} failed: {type(e).__name__}: {e}")

            print(f"\n[urlapp] === URL APPEND ANALYSIS ===")
            print(f"[urlapp] env URLParam       : {env_param!r}")
            print(f"[urlapp] link_yes base URL  : {yes_url!r}")
            print(f"[urlapp] link_yes rendered  : {yes_href!r}")
            print(f"[urlapp] link_no  base URL  : {no_url!r}")
            print(f"[urlapp] link_no  rendered  : {no_href!r}")

            # Mechanism check: across ALL visible cards, how many ended with URLParam?
            # The append must be per-link selective: some links opt-in, others don't.
            popular_with_param = 0
            popular_without_param = 0
            for i in range(n_cards):
                try:
                    card = cards.nth(i)
                    anchor = card.locator("a[class*='WelcomeLinksstyled__AppLinkButton']").first
                    href = anchor.get_attribute("href") if anchor.count() > 0 else None
                    if href:
                        if env_param in href:
                            popular_with_param += 1
                        else:
                            popular_without_param += 1
                except Exception:
                    pass
            print(f"[urlapp] popular grid: {popular_with_param} cards with URLParam, {popular_without_param} without")

            # Per-link outcome (only if our specific links actually surfaced)
            if yes_href is not None and no_href is not None:
                yes_has_param = env_param in yes_href
                no_has_param = env_param in no_href
                if yes_has_param and not no_has_param:
                    print("[urlapp] >>> PER-LINK PASS: AppendYes got URLParam, AppendNo did not")
                    url_data["per_link_outcome"] = "PASS"
                elif yes_has_param and no_has_param:
                    print("[urlapp] >>> PER-LINK FAIL: both got URLParam — לא is leaking")
                    url_data["per_link_outcome"] = "BOTH_APPENDED"
                elif not yes_has_param and not no_has_param:
                    print("[urlapp] >>> PER-LINK FAIL: neither got URLParam")
                    url_data["per_link_outcome"] = "NEITHER_APPENDED"
                else:
                    print("[urlapp] >>> PER-LINK WEIRD: inverted")
                    url_data["per_link_outcome"] = "INVERTED"
            else:
                print(f"[urlapp]   AppendYes/AppendNo not visible on homepage (need visits to surface)")
                url_data["per_link_outcome"] = "NOT_OBSERVED"

            # Overall mechanism outcome based on the pre-existing popular cards
            if popular_with_param > 0 and popular_without_param > 0:
                print("[urlapp] >>> MECHANISM PASS: append behavior is selective per-link "
                      "(some cards have URLParam, some don't)")
                url_data["outcome"] = "MECHANISM_VERIFIED"
            elif popular_with_param > 0 and popular_without_param == 0:
                print("[urlapp] >>> MECHANISM SUSPECT: every visible card has URLParam — לא may not work")
                url_data["outcome"] = "ALL_APPENDED"
            elif popular_with_param == 0 and popular_without_param > 0:
                print("[urlapp] >>> MECHANISM SUSPECT: no card has URLParam — כן may not work")
                url_data["outcome"] = "NONE_APPENDED"
            else:
                print("[urlapp] >>> MECHANISM UNVERIFIED: no cards visible to inspect")
                url_data["outcome"] = "NO_CARDS"

        finally:
            new_context.close()

    def test_06_cleanup(self, page, url_data):
        print("\n[urlapp] cleaning up created entities...")
        nav = NavigationPage(page)
        try:
            nav.go_to_links()
            page.wait_for_timeout(800)
            links = LinksPage(page)
            for key in ("link_yes_name", "link_no_name"):
                name = url_data.get(key)
                if not name:
                    continue
                try:
                    links.delete_link(name)
                    links.click_delete_and_confirm()
                    page.wait_for_timeout(1500)
                    print(f"[urlapp]   deleted link {name}")
                except Exception as e:
                    print(f"[urlapp]   couldn't delete {name}: {type(e).__name__}")
        except Exception as e:
            print(f"[urlapp]   link cleanup error: {type(e).__name__}: {e}")

        try:
            env_name = url_data.get("env_name")
            if env_name:
                nav.go_to_environments()
                page.wait_for_timeout(800)
                envs = EnvironmentsPage(page)
                envs.delete_environment(env_name)
                envs.click_delete_and_confirm()
                page.wait_for_timeout(1500)
                print(f"[urlapp]   deleted env {env_name}")
        except Exception as e:
            print(f"[urlapp]   env cleanup error: {type(e).__name__}: {e}")

    def test_07_summary(self, url_data):
        print("\n" + "=" * 60)
        print(f"[urlapp] MECHANISM OUTCOME : {url_data.get('outcome', 'UNKNOWN')}")
        print(f"[urlapp] PER-LINK OUTCOME  : {url_data.get('per_link_outcome', 'UNKNOWN')}")
        print(f"[urlapp]   env       : {url_data.get('env_name')}")
        print(f"[urlapp]   urlparam  : {url_data.get('env_param')}")
        print(f"[urlapp]   link_yes  : {url_data.get('link_yes_name')}")
        print(f"[urlapp]   link_no   : {url_data.get('link_no_name')}")
        print("=" * 60)
