"""
Image upload boundary tests for the Add Link drawer.

Tests three scenarios against the documented "5MB, png/jpeg/jpg only" constraints:
  1. Valid image under limit (~4.5MB PNG) — Save should remain enabled
  2. Image over limit (~5.5MB PNG)         — observe rejection signal (toast / Save disabled)
  3. Invalid format (text mislabeled .png + plain .txt) — observe rejection signal

Test images are generated dynamically via utils/image_gen — no large binary fixtures
in the repo. Each scenario opens a fresh Add Link drawer, fills required fields to
a known "Save enabled" baseline, uploads the file, captures Save state and any
toasts, then closes via the drawer X to discard. The test never actually saves a
link, so no cleanup is required.
"""

import pytest
import uuid

from pages.login_page import LoginPage
from pages.navigation_page import NavigationPage
from pages.links_page import LinksPage
from utils.image_gen import make_png_bytes, make_text_file_bytes


@pytest.fixture(scope="class")
def img_data():
    return {}


def _close_drawer_via_x(page):
    """Close the Add Link drawer via its custom X icon (NewLinkstyled__StyledCloseOutlinedIcon).
    DO NOT press Escape — that closes the drawer too, but inconsistently across MUI states.
    """
    try:
        page.locator("[class*='StyledCloseOutlinedIcon']").first.click(timeout=2000)
    except Exception:
        pass


def _capture_form_state(page, scenario):
    """Print Save button state and any visible toasts/alerts."""
    save = page.get_by_role("button", name="שמירה")
    save_disabled = None
    try:
        if save.count() > 0:
            save_disabled = save.first.is_disabled()
    except Exception:
        pass
    print(f"[img/{scenario}]   save button disabled: {save_disabled}")

    for sel in [".MuiSnackbar-root", ".Toastify__toast", "[role='alert']", ".MuiAlert-root"]:
        try:
            n = page.locator(sel).count()
            for i in range(n):
                txt = page.locator(sel).nth(i).inner_text().strip()
                if txt:
                    print(f"[img/{scenario}]   toast {sel}[{i}]: {txt!r}")
        except Exception:
            pass


def _open_and_fill_required(page, link_name, link_url):
    """Open Add Link drawer and fill required fields (Title, URL, Domain)."""
    links = LinksPage(page)
    links.open_add_link_dialog()
    page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(link_name)
    page.locator("input[name='URL']").fill(link_url)
    links.select_combobox_options(combobox_index=0, count=3)


class TestImageUpload:

    def test_01_login(self, page):
        print("\n[img] logging in...")
        login = LoginPage(page)
        login.navigate()
        login.fill_credentials()
        login.click_login()
        login.wait_for_dashboard()
        NavigationPage(page).go_to_links()
        print("[img] reached Links admin")

    def test_02_probe_file_input(self, page, img_data):
        scenario = "probe"
        print(f"\n[img/{scenario}] open Add Link, find file input")
        LinksPage(page).open_add_link_dialog()
        page.wait_for_timeout(800)

        file_inputs = page.locator("input[type='file']")
        n = file_inputs.count()
        print(f"[img/{scenario}]   input[type='file'] count: {n}")
        for i in range(n):
            try:
                el = file_inputs.nth(i)
                accept = el.get_attribute("accept") or ""
                name = el.get_attribute("name") or ""
                visible = el.is_visible()
                print(f"[img/{scenario}]   [{i}] name={name!r} accept={accept!r} visible={visible}")
            except Exception:
                pass

        img_data["file_input_count"] = n
        _close_drawer_via_x(page)
        page.wait_for_timeout(500)

    def test_03_upload_valid_under_limit(self, page, img_data):
        scenario = "valid_4.5MB"
        print(f"\n[img/{scenario}] upload ~4.5MB PNG (under 5MB limit)")
        link_name = f"ImgValid{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/img-{uuid.uuid4().hex[:6]}"
        _open_and_fill_required(page, link_name, link_url)

        try:
            save_before = page.get_by_role("button", name="שמירה").first.is_disabled()
            print(f"[img/{scenario}]   save state before upload: disabled={save_before}")
        except Exception:
            pass

        img_bytes = make_png_bytes(4.5)
        print(f"[img/{scenario}]   uploading {len(img_bytes):,} bytes ({len(img_bytes)/1024/1024:.2f} MB)")
        try:
            page.set_input_files("input[type='file']", files=[{
                "name": "valid_4_5mb.png",
                "mimeType": "image/png",
                "buffer": img_bytes,
            }])
        except Exception as e:
            print(f"[img/{scenario}]   set_input_files failed: {type(e).__name__}: {e}")
            _close_drawer_via_x(page)
            return
        page.wait_for_timeout(2500)

        _capture_form_state(page, scenario)

        preview_count = page.locator("img[src^='blob:'], img[src^='data:']").count()
        print(f"[img/{scenario}]   image preview count (blob:/data:): {preview_count}")

        _close_drawer_via_x(page)
        page.wait_for_timeout(500)

    def test_04_upload_over_limit(self, page, img_data):
        scenario = "over_5.5MB"
        print(f"\n[img/{scenario}] upload ~5.5MB PNG (over 5MB limit)")
        link_name = f"ImgOver{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/img-{uuid.uuid4().hex[:6]}"
        _open_and_fill_required(page, link_name, link_url)

        try:
            save_before = page.get_by_role("button", name="שמירה").first.is_disabled()
            print(f"[img/{scenario}]   save state before upload: disabled={save_before}")
        except Exception:
            pass

        img_bytes = make_png_bytes(5.5)
        print(f"[img/{scenario}]   uploading {len(img_bytes):,} bytes ({len(img_bytes)/1024/1024:.2f} MB)")
        try:
            page.set_input_files("input[type='file']", files=[{
                "name": "over_5_5mb.png",
                "mimeType": "image/png",
                "buffer": img_bytes,
            }])
        except Exception as e:
            print(f"[img/{scenario}]   set_input_files failed: {type(e).__name__}: {e}")
            _close_drawer_via_x(page)
            return
        page.wait_for_timeout(2500)

        _capture_form_state(page, scenario)

        preview_count = page.locator("img[src^='blob:'], img[src^='data:']").count()
        print(f"[img/{scenario}]   image preview count (blob:/data:): {preview_count}")

        _close_drawer_via_x(page)
        page.wait_for_timeout(500)

    def test_05_upload_invalid_format(self, page, img_data):
        scenario = "invalid_format"
        print(f"\n[img/{scenario}] upload non-image content")
        link_name = f"ImgBad{uuid.uuid4().hex[:5]}"
        link_url = f"https://example.com/img-{uuid.uuid4().hex[:6]}"
        _open_and_fill_required(page, link_name, link_url)

        try:
            save_before = page.get_by_role("button", name="שמירה").first.is_disabled()
            print(f"[img/{scenario}]   save state before upload: disabled={save_before}")
        except Exception:
            pass

        text_bytes = make_text_file_bytes()

        # Variant A: text content with image/png mime + .png extension (lying mime)
        print(f"[img/{scenario}/lying_png]   uploading text content as fake.png (image/png mime)")
        try:
            page.set_input_files("input[type='file']", files=[{
                "name": "fake.png",
                "mimeType": "image/png",
                "buffer": text_bytes,
            }])
            page.wait_for_timeout(2000)
            _capture_form_state(page, scenario + "/lying_png")
            preview_count = page.locator("img[src^='blob:'], img[src^='data:']").count()
            print(f"[img/{scenario}/lying_png]   image preview count: {preview_count}")
        except Exception as e:
            print(f"[img/{scenario}/lying_png]   upload failed: {type(e).__name__}: {e}")

        # Variant B: clean .txt name with text/plain mime — extension/MIME both honest
        print(f"[img/{scenario}/honest_txt]   uploading notes.txt with text/plain mime")
        try:
            page.set_input_files("input[type='file']", files=[{
                "name": "notes.txt",
                "mimeType": "text/plain",
                "buffer": text_bytes,
            }])
            page.wait_for_timeout(2000)
            _capture_form_state(page, scenario + "/honest_txt")
        except Exception as e:
            print(f"[img/{scenario}/honest_txt]   upload failed (expected): {type(e).__name__}: {e}")

        _close_drawer_via_x(page)
        page.wait_for_timeout(500)

    def test_06_summary(self, img_data):
        print("\n" + "=" * 60)
        print("[img] image upload boundary tests complete")
        print(f"[img]   file inputs found in form: {img_data.get('file_input_count', 'unknown')}")
        print("[img]   per-scenario PASS/FAIL signals are inline above")
        print("=" * 60)
