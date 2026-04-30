"""
Orphan-data cleanup utility.

Scans admin grids for entities whose names match known test prefixes and
deletes them. Use this to clean up orphaned test data left behind by failed
runs (e.g. 'AppEnvf4325vvv' stuck as the system's default environment).

Usage (standalone CLI):
    py -3.13 utils/cleanup_orphans.py            # delete orphans
    py -3.13 utils/cleanup_orphans.py --dry-run  # list only, no deletions
    py -3.13 utils/cleanup_orphans.py --headless # run without visible browser

Usage (importable):
    from utils.cleanup_orphans import cleanup_orphans
    summary = cleanup_orphans(page, dry_run=False)

Safety:
  - Patterns require a hex suffix (e.g. ^Tag[0-9a-f]{4,}$) so "Tagging" or
    "Environment" do NOT match real production-looking names.
  - The currently active environment shown in the header is never deleted
    (deleting the active env can leave the system in an unstable state).
  - Each deletion is wrapped in try/except so one failure does not block
    the rest of the cleanup.

Order matters — children before parents — to avoid cascade complications.
"""

import argparse
import os
import re
import sys

from playwright.sync_api import sync_playwright

# Make sibling packages importable when run as a script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pages.login_page import LoginPage  # noqa: E402
from pages.navigation_page import NavigationPage  # noqa: E402
from pages.links_page import LinksPage  # noqa: E402
from pages.domains_page import DomainsPage  # noqa: E402
from pages.tags_page import TagsPage  # noqa: E402
from pages.messages_page import MessagesPage  # noqa: E402
from pages.environments_page import EnvironmentsPage  # noqa: E402


# --------------------------------------------------------------------------
# Test name patterns (anchored, hex-suffix-required so we don't match real
# data). Update these whenever a new test introduces a new naming convention.
# --------------------------------------------------------------------------
TEST_PATTERNS = {
    "links": [
        r"^TestLink_[0-9a-f]+(_upd)?$",        # test_zira
        r"^CasLink[0-9a-f]+$",                 # test_cascade / test_cascade_expanded
        r"^DiscardLink[0-9a-f]+$",             # test_discard
        r"^DraftDsc[0-9a-f]+$",                # test_discard (unsaved draft)
        r"^InactLink[0-9a-f]+$",               # test_inactive_link
        r"^AnalyticsLink_[0-9a-f]+$",          # test_end_user_flows
        r"^SearchLink_[0-9a-f]+$",             # test_end_user_flows
        r"^AppendYes[0-9a-f]+$",               # test_url_append
        r"^AppendNo[0-9a-f]+$",                # test_url_append
        r"^NegLink[0-9a-f]+$",                 # test_neg_links
        r"^ImgValid[0-9a-f]+$",                # test_image_upload (rarely saved)
        r"^ImgOver[0-9a-f]+$",
        r"^ImgBad[0-9a-f]+$",
        r"^XssDesc_[0-9a-f]+$",                # test_xss_sanitization
        r"^XssUrl_[0-9a-f]+$",
        r"^Grid[A-Z]_[0-9a-f]+$",              # test_admin_grid_controls
        # Title-XSS link's name IS the payload itself.
        # Per-run randomised: '<svg onload=alert(NNN)>' with NNN ∈ [100,999].
        r"^<svg onload=alert\(\d+\)>$",
    ],
    "domains": [
        r"^TestDomain[0-9a-f]+$",              # test_zira
        r"^CasDom[0-9a-f]+$",                  # test_cascade
    ],
    "tags": [
        r"^Tag[0-9a-f]{4,}(upd)?$",            # test_zira (Tag<5hex>)
        r"^ModTag[0-9a-f]+(Upd)?$",            # test_mod_security
        r"^CasTag[0-9a-f]+$",                  # test_cascade_expanded
    ],
    "messages": [
        r"^Msg_[0-9a-f]+(_upd)?$",             # test_zira
        r"^ModMsg[0-9a-f]+(_Upd)?$",           # test_mod_security
        r"^PopupMsg_[0-9a-f]+$",               # test_messages_flows
        r"^PreviewMsg_[0-9a-f]+$",
        r"^CasMsg[0-9a-f]+$",                  # test_cascade_expanded
    ],
    "environments": [
        r"^Env[0-9a-f]{4,}(upd)?$",            # test_zira
        r"^AppEnv[0-9a-f]+(upd)?$",            # test_url_append
        r"^CasEnv[0-9a-f]+$",                  # test_cascade_expanded
    ],
}

COMPILED = {k: [re.compile(p) for p in v] for k, v in TEST_PATTERNS.items()}


def matches_test_pattern(name, entity_type):
    return any(p.match(name) for p in COMPILED.get(entity_type, []))


def find_orphans_on_page(page, entity_type):
    """Tokenize the visible body text and return names matching test patterns.

    Two-pass scan:
      1. Whitespace-tokenized — catches normal names like 'TestLink_abc123'.
      2. Per-line regex search — catches names that contain spaces (e.g.
         XSS payloads like '<svg onload=alert(1)>').
    """
    try:
        text = page.locator("body").inner_text()
    except Exception:
        return []
    found = set()

    # Pass 1: whitespace tokens
    for token in re.split(r"[\s\|·]+", text):
        token = token.strip()
        if token and matches_test_pattern(token, entity_type):
            found.add(token)

    # Pass 2: per-line scan for patterns that may contain whitespace
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for pattern in COMPILED.get(entity_type, []):
            if pattern.match(line):
                found.add(line)
                break

    return sorted(found)


def _read_active_env(page):
    try:
        el = page.locator("[class*='Headerstyled__StatusEnvText']").first
        if el.count() > 0:
            return (el.inner_text() or "").strip() or None
    except Exception:
        pass
    return None


# --------------------------------------------------------------------------
# Per-entity deletion helpers
# --------------------------------------------------------------------------

def _delete_links(page, dry_run):
    NavigationPage(page).go_to_links()
    page.wait_for_timeout(1500)
    names = find_orphans_on_page(page, "links")
    print(f"  found {len(names)} orphan link(s): {names}")
    if dry_run or not names:
        return len(names), 0
    pom = LinksPage(page)
    deleted = 0
    for name in names:
        try:
            pom.delete_link(name)
            pom.click_delete_and_confirm()
            page.wait_for_timeout(1200)
            print(f"  deleted link: {name}")
            deleted += 1
        except Exception as e:
            print(f"  FAILED to delete link {name!r}: {type(e).__name__}: {e}")
    return len(names), deleted


def _delete_messages(page, dry_run):
    NavigationPage(page).go_to_messages()
    page.wait_for_timeout(1500)
    names = find_orphans_on_page(page, "messages")
    print(f"  found {len(names)} orphan message(s): {names}")
    if dry_run or not names:
        return len(names), 0
    pom = MessagesPage(page)
    deleted = 0
    for name in names:
        try:
            pom.delete_message(name)
            pom.click_delete_and_confirm()
            page.wait_for_timeout(1500)
            print(f"  deleted message: {name}")
            deleted += 1
        except Exception as e:
            print(f"  FAILED to delete message {name!r}: {type(e).__name__}: {e}")
    return len(names), deleted


def _delete_tags(page, dry_run):
    NavigationPage(page).go_to_tags()
    page.wait_for_timeout(1500)
    names = find_orphans_on_page(page, "tags")
    print(f"  found {len(names)} orphan tag(s): {names}")
    if dry_run or not names:
        return len(names), 0
    pom = TagsPage(page)
    deleted = 0
    for name in names:
        try:
            pom.delete_tag(name)
            pom.click_delete_and_confirm()
            page.wait_for_timeout(1200)
            print(f"  deleted tag: {name}")
            deleted += 1
        except Exception as e:
            print(f"  FAILED to delete tag {name!r}: {type(e).__name__}: {e}")
    return len(names), deleted


def _delete_domains(page, dry_run):
    NavigationPage(page).go_to_content_worlds()
    page.wait_for_timeout(1500)
    names = find_orphans_on_page(page, "domains")
    print(f"  found {len(names)} orphan domain(s): {names}")
    if dry_run or not names:
        return len(names), 0
    pom = DomainsPage(page)
    deleted = 0
    for name in names:
        try:
            pom.delete_domain(name)
            pom.click_delete_and_confirm()
            page.wait_for_timeout(1200)
            print(f"  deleted domain: {name}")
            deleted += 1
        except Exception as e:
            print(f"  FAILED to delete domain {name!r}: {type(e).__name__}: {e}")
    return len(names), deleted


def _delete_environments(page, dry_run):
    NavigationPage(page).go_to_environments()
    page.wait_for_timeout(1500)
    names = find_orphans_on_page(page, "environments")
    print(f"  found {len(names)} orphan environment(s): {names}")
    if dry_run or not names:
        return len(names), 0

    # Safety: skip the currently active env to avoid breaking the system default
    active = _read_active_env(page)
    if active and active in names:
        print(f"  SKIP {active!r} — currently active default env "
              f"(would destabilise the system if deleted)")
        names = [n for n in names if n != active]

    pom = EnvironmentsPage(page)
    deleted = 0
    for name in names:
        try:
            pom.delete_environment(name)
            pom.click_delete_and_confirm()
            page.wait_for_timeout(1200)
            print(f"  deleted env: {name}")
            deleted += 1
        except Exception as e:
            print(f"  FAILED to delete env {name!r}: {type(e).__name__}: {e}")
    return len(names), deleted


def cleanup_orphans(page, dry_run=False):
    """Run cleanup across all entity types. Returns dict of {entity: {found, deleted}}.

    Children-first order avoids cascade complications:
        Links → Messages → Tags → Domains → Environments
    """
    summary = {}
    for label, fn in (
        ("links",        _delete_links),
        ("messages",     _delete_messages),
        ("tags",         _delete_tags),
        ("domains",      _delete_domains),
        ("environments", _delete_environments),
    ):
        print(f"\n--- {label} ---")
        try:
            found, deleted = fn(page, dry_run)
            summary[label] = {"found": found, "deleted": deleted}
        except Exception as e:
            print(f"  cleanup phase failed for {label}: {type(e).__name__}: {e}")
            summary[label] = {"found": 0, "deleted": 0, "error": str(e)}
    return summary


def _print_summary(summary, dry_run):
    print("\n" + "=" * 60)
    print("CLEANUP SUMMARY" + (" (DRY-RUN)" if dry_run else ""))
    print("=" * 60)
    total_found = sum(s.get("found", 0) for s in summary.values())
    total_deleted = sum(s.get("deleted", 0) for s in summary.values())
    for label, info in summary.items():
        err = f" [error: {info['error']}]" if "error" in info else ""
        print(f"  {label:<14}  found={info.get('found', 0):3}  "
              f"deleted={info.get('deleted', 0):3}{err}")
    print(f"  {'TOTAL':<14}  found={total_found:3}  deleted={total_deleted:3}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Scan admin grids and delete orphan test entities."
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="list orphans without deleting")
    parser.add_argument("--headless", action="store_true",
                        help="run browser headless (default: visible)")
    args = parser.parse_args()

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=args.headless,
            slow_mo=0 if args.headless else 250,
        )
        context = browser.new_context()
        page = context.new_page()
        page.goto(os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/"))
        try:
            page.get_by_role("button", name="הבנתי").click(timeout=3000)
        except Exception:
            pass

        print("\n=== Logging in as admin ===")
        login = LoginPage(page)
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()

        mode = "DRY-RUN (no deletions)" if args.dry_run else "LIVE (will delete)"
        print(f"\n=== Cleanup mode: {mode} ===")
        summary = cleanup_orphans(page, dry_run=args.dry_run)
        _print_summary(summary, args.dry_run)

        context.close()
        browser.close()


if __name__ == "__main__":
    main()
