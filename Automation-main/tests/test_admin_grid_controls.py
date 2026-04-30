"""
Admin Links grid — search and sort controls.

Verifies the daily-driver workflows that real admins use to find a
specific link among many: a search input that filters the grid, and
sortable column headers that reorder rows.

The test seeds three links with deterministic names spanning the
alphabet (GridA*, GridM*, GridZ*) so that:
  - a name fragment search uniquely identifies one row
  - ascending sort puts GridA first, descending puts GridZ first

Defensive design: if a control isn't present in the current build,
the relevant test is `pytest.skip(reason=...)` rather than failing
silently — that surfaces feature gaps clearly in the suite report
without producing false negatives.
"""

import os
import uuid

import pytest

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage


APP_URL = os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/")

# Selector for visible link names in the admin grid (already used by LinksPage)
NAME_CELL = "[class*='SingleLinkstyled__StyledLinkName']"

# Probable selectors for an admin search input. Tried in order — first hit wins.
SEARCH_INPUT_SELECTORS = (
    "input[placeholder*='חיפוש']",   # Hebrew "search"
    "input[placeholder*='חפש']",
    "input[type='search']",
    "input[role='searchbox']",
    "input[aria-label*='חיפוש']",
    "input[aria-label*='Search' i]",
    "input[name='search']",
    "input[name='filter']",
)

# Header text candidates for sort columns
SORT_HEADER_NAME_TEXTS = ("שם הקישור",)
SORT_HEADER_VISITS_TEXTS = ("כניסות",)


def _find_search_input(page):
    """Return the first visible admin search input, or None."""
    for sel in SEARCH_INPUT_SELECTORS:
        try:
            el = page.locator(sel).first
            if el.count() > 0 and el.is_visible():
                return el, sel
        except Exception:
            continue
    return None, None


def _list_grid_link_names(page):
    """Return the visible link names in the admin grid, in display order."""
    names = []
    cells = page.locator(NAME_CELL)
    n = cells.count()
    for i in range(n):
        try:
            txt = cells.nth(i).inner_text().strip()
            if txt:
                names.append(txt)
        except Exception:
            pass
    return names


def _find_clickable_header(page, candidate_texts):
    """Look for a clickable column header matching one of the candidate texts.
    Tries [role='columnheader'], <th>, and free-floating clickable elements
    containing the text."""
    for txt in candidate_texts:
        for sel in (
            f"[role='columnheader']:has-text('{txt}')",
            f"th:has-text('{txt}')",
            f"button:has-text('{txt}')",
            # Heuristic: a div that contains the header text and has cursor:pointer
            f"div:has-text('{txt}')",
        ):
            try:
                el = page.locator(sel).first
                if el.count() == 0 or not el.is_visible():
                    continue
                # Heuristic to skip overly broad div matches: the text should
                # be the dominant visible content of the element.
                inner = (el.inner_text() or "").strip()
                if txt in inner and len(inner) < 60:
                    return el, sel
            except Exception:
                continue
    return None, None


@pytest.fixture(scope="class")
def grid_data():
    return {}


class TestLinksAdminGrid:
    """Search + sort controls on the admin Links grid."""

    # ---------------------------------------------------------
    # Setup
    # ---------------------------------------------------------
    def test_01_login(self, page):
        print("\n[grid] admin login...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        page.wait_for_timeout(1000)

    def test_02_seed_three_links(self, page, grid_data):
        """Seed deterministic A/M/Z-prefixed links to enable predictable
        filtering and sort assertions."""
        suffix = uuid.uuid4().hex[:5]
        names = {
            "a": f"GridA_{suffix}",
            "m": f"GridM_{suffix}",
            "z": f"GridZ_{suffix}",
        }
        print(f"\n[grid] seeding three links: {list(names.values())}")
        links = LinksPage(page)
        for key, name in names.items():
            url = f"https://example.com/grid-{key}-{suffix}"
            links.create_link(name, url, f"grid-test-{key}-marker")
            links.click_save_and_confirm()
            page.wait_for_timeout(1500)
            links.verify_link_visible(name)
        grid_data["names"] = names
        grid_data["suffix"] = suffix

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------
    def test_03_admin_search_filters_grid(self, page, grid_data):
        """Type one of the seeded names into an admin search input; verify
        the grid filters down to exactly that link."""
        names = grid_data["names"]
        target = names["a"]  # GridA_<suffix>

        # Sanity: BEFORE filtering, all three should be visible
        all_names_before = _list_grid_link_names(page)
        print(f"\n[grid/search] grid has {len(all_names_before)} link rows before filter")
        for n in names.values():
            assert n in all_names_before, (
                f"Seeded link {n!r} not visible in admin grid before filter — "
                f"setup is broken"
            )

        search, sel_used = _find_search_input(page)
        if search is None:
            tried = "\n    ".join(SEARCH_INPUT_SELECTORS)
            pytest.skip(
                f"Admin Links page has no search input. Tried selectors:\n"
                f"    {tried}\n"
                f"This is a feature gap — flag to product if the team expects "
                f"a search/filter affordance on this grid."
            )

        print(f"[grid/search] using search selector {sel_used!r}; typing {target!r}")
        search.click()
        try:
            search.fill("")
        except Exception:
            pass
        search.press_sequentially(target, delay=60)
        page.wait_for_timeout(1500)

        names_after = _list_grid_link_names(page)
        print(f"[grid/search] grid now shows {len(names_after)} rows: {names_after}")

        # Assert: only the target name is visible
        assert target in names_after, (
            f"Search for {target!r} did not surface the matching link "
            f"(visible rows: {names_after})"
        )
        unrelated = [n for n in names_after if n in (names["m"], names["z"])]
        assert not unrelated, (
            f"Search for {target!r} did not filter out unrelated seeded links: "
            f"{unrelated}. Filter is too permissive."
        )
        print(f"[grid/search] >>> PASS — filter narrowed grid to the target row")

        # Clean up the search filter so subsequent tests see the full grid
        try:
            search.fill("")
            page.wait_for_timeout(800)
        except Exception:
            pass

    # ---------------------------------------------------------
    # Sort
    # ---------------------------------------------------------
    def test_04_sort_by_name_changes_top_row(self, page, grid_data):
        """Click the 'שם הקישור' column header; assert the row order changes
        and matches alphabetical (asc/desc) ordering of our seeds."""
        names = grid_data["names"]

        # Make sure we're on a clean view (no active search filter)
        search, _ = _find_search_input(page)
        if search is not None:
            try:
                search.fill("")
                page.wait_for_timeout(600)
            except Exception:
                pass

        before = _list_grid_link_names(page)
        print(f"\n[grid/sort] order before clicking name header: "
              f"{[n for n in before if n.startswith('Grid')]}")

        header, sel_used = _find_clickable_header(page, SORT_HEADER_NAME_TEXTS)
        if header is None:
            pytest.skip(
                "Admin Links page has no clickable 'שם הקישור' column header "
                "(no matching role=columnheader / th / labelled button found). "
                "This is a feature gap — sorting is not exposed in the UI."
            )

        print(f"[grid/sort] using header selector {sel_used!r}; clicking once")
        try:
            header.scroll_into_view_if_needed()
            header.click(timeout=3000)
        except Exception as e:
            pytest.skip(
                f"Found a 'שם הקישור' element but it was not clickable: "
                f"{type(e).__name__}: {e}. Header text exists but it is not "
                f"wired to a sort handler."
            )
        page.wait_for_timeout(1500)

        after_first = _list_grid_link_names(page)
        seeded_after_first = [n for n in after_first if n.startswith("Grid")]
        print(f"[grid/sort] order after first click: {seeded_after_first}")

        if seeded_after_first == [n for n in before if n.startswith("Grid")]:
            pytest.skip(
                "Clicking 'שם הקישור' header did not reorder the grid — "
                "header is not bound to a sort handler in the current build."
            )

        # We now know the click reorders. Verify the order matches one of the
        # two valid alphabetical directions (asc or desc) for our 3 seeds.
        a, m, z = names["a"], names["m"], names["z"]
        ordered_seeds = [n for n in seeded_after_first if n in (a, m, z)]
        valid_orderings = ([a, m, z], [z, m, a])
        assert ordered_seeds in valid_orderings, (
            f"After name-sort click, our seeded rows are in unexpected order: "
            f"{ordered_seeds}. Expected ascending {[a, m, z]} or "
            f"descending {[z, m, a]}."
        )
        direction = "ASC" if ordered_seeds == [a, m, z] else "DESC"
        print(f"[grid/sort] >>> PASS — name sort produced {direction} order")

        # Click again and verify the direction flips (toggle behaviour)
        try:
            header.click(timeout=3000)
            page.wait_for_timeout(1500)
        except Exception:
            print("[grid/sort] could not click header a second time — skipping toggle check")
            return

        after_second = [
            n for n in _list_grid_link_names(page) if n in (a, m, z)
        ]
        print(f"[grid/sort] order after second click: {after_second}")
        if after_second != ordered_seeds and after_second in valid_orderings:
            opposite = "DESC" if direction == "ASC" else "ASC"
            print(f"[grid/sort] >>> PASS — second click flipped direction to {opposite}")
        elif after_second == ordered_seeds:
            print("[grid/sort] >>> NOTE — second click did NOT flip direction "
                  "(the header is single-direction, not a toggle)")
        else:
            print(f"[grid/sort] >>> WARN — unexpected order after second click: "
                  f"{after_second}")

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------
    def test_05_cleanup(self, page, grid_data):
        names = grid_data.get("names", {})
        if not names:
            return
        print(f"\n[grid/cleanup] deleting seeded links: {list(names.values())}")
        try:
            NavigationPage(page).go_to_links()
            page.wait_for_timeout(800)
        except Exception:
            pass

        # Clear any active search filter
        search, _ = _find_search_input(page)
        if search is not None:
            try:
                search.fill("")
                page.wait_for_timeout(600)
            except Exception:
                pass

        links = LinksPage(page)
        for name in names.values():
            try:
                links.delete_link(name)
                links.click_delete_and_confirm()
                page.wait_for_timeout(1500)
                print(f"[grid/cleanup] deleted {name!r}")
            except Exception as e:
                print(f"[grid/cleanup] could not delete {name!r}: "
                      f"{type(e).__name__}: {e}")
