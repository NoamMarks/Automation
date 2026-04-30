import pytest
import uuid
import json
import time
from contextlib import contextmanager
from playwright.sync_api import expect, sync_playwright
# חובה: ייבוא הרכיב לכתיבת HTML
from pytest_html import extras as html_extras 

# --- ⏱️ כלי עזר: מודד זמן וכותב בלוקים צבעוניים ל-HTML ---
@contextmanager
def performance_step(step_name, extras, limit_ms=3000):
    """
    מודד זמן, ומזריק קוד HTML צבעוני לדוח התוצאות בהתאם לביצועים.
    """
    start_time = time.time()
    
    try:
        # הרצת הקוד של הטסט
        yield
        
        # --- הצלחה (הפונקציונליות עבדה) ---
        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000
        
        if duration_ms <= limit_ms:
            # ✅ הכל תקין - ירוק
            html_content = f"""
            <div class="perf-block perf-pass">
                <span class="perf-title">✅ STEP PASSED: {step_name}</span>
                <span class="perf-meta">Functionality: OK | Performance: <b>{duration_ms:.2f}ms</b> (Limit: {limit_ms}ms)</span>
            </div>
            """
            extras.append(html_extras.html(html_content))
            print(f"   ✅ PASSED: {step_name} ({duration_ms:.2f}ms)")
            
        else:
            # ⚠️ איטי מדי - כתום
            html_content = f"""
            <div class="perf-block perf-warn">
                <span class="perf-title" style="color: #d35400;">⚠️ PERFORMANCE LAG: {step_name}</span>
                <span class="perf-meta">Functionality: OK | Time: <b>{duration_ms:.2f}ms</b> (Limit: {limit_ms}ms)</span>
            </div>
            """
            extras.append(html_extras.html(html_content))
            # כאן אנחנו בוחרים אם להכשיל או רק להתריע. בקוד הזה - נכשיל.
            pytest.fail(f"Performance threshold exceeded for '{step_name}'! Took {duration_ms:.2f}ms")

    except Exception as e:
        # ❌ כישלון פונקציונלי - אדום
        end_time = time.time()
        duration_ms = (end_time - start_time) * 1000
        
        html_content = f"""
        <div class="perf-block perf-fail">
            <span class="perf-title" style="color: #c0392b;">❌ FUNCTIONAL FAILURE: {step_name}</span>
            <span class="perf-meta">Stopped after: {duration_ms:.2f}ms</span>
        </div>
        """
        extras.append(html_extras.html(html_content))
        print(f"   ❌ FAILED: {step_name}")
        raise e

# --- Fixture לנתונים ---
@pytest.fixture(scope="class")
def test_data():
    return {}

# --- Fixture לוגין ---
@pytest.fixture(scope="class")
def mod_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto(os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/"))
        
        try:
            page.get_by_role("button", name="הבנתי").click(timeout=3000)
        except:
            pass

        print("\n🔑 Logging in as Moderator...")
        page.get_by_text("התחבר").click()
        page.get_by_role("textbox", name="הכנס שם משתמש").fill(os.getenv("MOD_USERNAME", "ZiraMod"))
        page.get_by_role("textbox", name="הכנס סיסמה").fill(os.getenv("MOD_PASSWORD", "123123"))
        page.get_by_role("button", name="התחברות").click()
        
        # אנחנו לא משתמשים ב-extras ב-fixture (זה מורכב יותר), אז כאן רק נמתין
        try:
            page.wait_for_url("**/links", timeout=10000)
            print("   ✅ Landed on Links page successfully")
        except:
            print("   ⚠️ Warning: URL validation skipped or timed out")

        yield page

        context.close()
        browser.close()

# --- מחלקת הטסטים ---
class TestModeratorWorkflow:

    # ---------------------------------------------------------
    # שלב 1: בדיקת עמוד הנחיתה (קישורים)
    # ---------------------------------------------------------
    def test_01_links_read_only(self, mod_page, extras):
        print("\n🔍 Checking Read-Only permissions on Links page...")

        with performance_step("Verify Links Page Permissions", extras, limit_ms=2000):
            expect(mod_page.get_by_role("button", name="הוספת קישור")).not_to_be_visible()

            rows = mod_page.locator("div.SingleLinkstyled__SingleLinkContainer-sc-1")
            if rows.count() > 0:
                first_row = rows.first
                expect(first_row.locator("img[src*='edit']")).not_to_be_visible()
                expect(first_row.locator("img[src*='delete']")).not_to_be_visible()
        
        print("✅ Links page is restricted correctly.")

    # ---------------------------------------------------------
    # שלב 1.5: בדיקת ביצועים (טעינת דף)
    # ---------------------------------------------------------
    def test_01_performance_landing_page(self, mod_page, extras):
        print("\n🚀 Starting Performance Check on Links Page...")

        mod_page.reload()
        
        # מדידת זמן טעינת דף מלאה
        start_time = time.time()
        mod_page.wait_for_load_state("load")
        
        # שליפת נתונים וחישוב
        timing_json = mod_page.evaluate("() => JSON.stringify(window.performance.timing)")
        timing = json.loads(timing_json)
        total_time = timing['domComplete'] - timing['navigationStart']
        limit = 5000

        # כתיבה ידנית ל-extras (כי זה לא performance_step רגיל)
        if total_time <= limit:
            html_content = f"""
            <div class="perf-block perf-pass">
                <span class="perf-title">✅ FULL PAGE LOAD PASSED</span>
                <span class="perf-meta">Time: <b>{total_time}ms</b> (Limit: {limit}ms)</span>
            </div>
            """
            extras.append(html_extras.html(html_content))
            print(f"   ✅ PASSED: Full Page Load ({total_time}ms)")
        else:
            html_content = f"""
            <div class="perf-block perf-warn">
                <span class="perf-title" style="color: #d35400;">⚠️ FULL PAGE LOAD LAG</span>
                <span class="perf-meta">Time: <b>{total_time}ms</b> (Limit: {limit}ms)</span>
            </div>
            """
            extras.append(html_extras.html(html_content))
            pytest.fail(f"Page load too slow! Took {total_time}ms")

    # ---------------------------------------------------------
    # שלב 2: תגיות - CRUD מלא
    # ---------------------------------------------------------
    def test_02_navigate_and_crud_tags(self, mod_page, test_data, extras):
        print("\nMoved to Tags page...")
        mod_page.get_by_role("button", name="תגיות").click()
        
        tag_name = f"ModTag{uuid.uuid4().hex[:5]}"

        # --- יצירה ---
        mod_page.get_by_role("button", name="יצירת תגית").click()
        mod_page.get_by_role("textbox", name="ניתן להזין עד 30 תווים").fill(tag_name)
        
        with performance_step("Create Tag", extras, limit_ms=2000):
            mod_page.get_by_role("button", name="שמירה").click()
            mod_page.get_by_role("button", name="אישור").click()
            expect(mod_page.locator(f"span[title='{tag_name}']")).to_be_visible()
        
        # --- עריכה ---
        row = mod_page.locator("div.SingleTagstyled__SingleTagContainer-sc-1urjs6w-0").filter(has_text=tag_name).first
        row.scroll_into_view_if_needed()
        
        edit_btn = row.locator("img").first 
        edit_btn.hover()
        mod_page.wait_for_timeout(200)
        edit_btn.click(force=True)
        
        new_name = tag_name + "Upd"
        input_box = mod_page.get_by_role("textbox", name="הכנס שם תגית")
        input_box.dblclick()
        input_box.fill(new_name)
        
        with performance_step("Update Tag", extras, limit_ms=2000):
            mod_page.get_by_role("button", name="שמירה").click()
            mod_page.get_by_role("button", name="אישור").click()
            expect(mod_page.locator(f"span[title='{new_name}']")).to_be_visible()
            
        # --- מחיקה ---
        row = mod_page.locator("div.SingleTagstyled__SingleTagContainer-sc-1urjs6w-0").filter(has_text=new_name).first
        del_btn = row.locator("img[src*='deleteIcon']").first
        del_btn.hover()
        mod_page.wait_for_timeout(200)
        del_btn.click(force=True)
        
        with performance_step("Delete Tag", extras, limit_ms=2000):
            mod_page.get_by_role("button", name="מחיקה").click()
            mod_page.get_by_role("button", name="אישור").click()
            expect(mod_page.locator(f"span[title='{new_name}']")).not_to_be_attached()

    # ---------------------------------------------------------
    # שלב 3: מודעות - CRUD מלא
    # ---------------------------------------------------------
    def test_03_navigate_and_crud_messages(self, mod_page, test_data, extras):
        print("\nMoved to Messages page...")
        mod_page.get_by_role("button", name="מודעות").click()
        
        msg_name = f"ModMsg{uuid.uuid4().hex[:5]}"

        # --- יצירה ---
        mod_page.get_by_role("button", name="הוספת מודעה").click()
        mod_page.get_by_role("textbox", name="ניתן להזין עד 50 תווים").fill(msg_name)
        mod_page.locator("textarea[name='description']").fill("Auto test")
        
        with performance_step("Create Message", extras, limit_ms=3000):
            mod_page.get_by_role("button", name="שמירה").click()
            mod_page.get_by_role("button", name="אישור").click()
            expect(mod_page.locator("span", has_text=msg_name)).to_be_visible()

        # --- עריכה ---
        row = mod_page.locator("div.SingleMessagestyled__SingleMessageContainer-sc-hgjxqs-0").filter(has_text=msg_name).first
        edit_btn = row.locator("img[src*='editIcon']").first
        edit_btn.hover()
        mod_page.wait_for_timeout(200)
        edit_btn.click(force=True)
        
        new_name = msg_name + "_Upd"
        input_box = mod_page.get_by_role("textbox", name="ניתן להזין עד 50 תווים")
        input_box.click()
        input_box.press("Control+A")
        input_box.press("Delete")
        input_box.fill(new_name)
        
        with performance_step("Update Message", extras, limit_ms=3000):
            mod_page.get_by_role("button", name="שמירה").click()
            mod_page.get_by_role("button", name="אישור").click()
            
            try:
                mod_page.locator("#loader").wait_for(state="hidden", timeout=3000)
            except:
                pass
            
            expect(mod_page.locator("span", has_text=new_name)).to_be_visible()

        # --- מחיקה ---
        row = mod_page.locator("div.SingleMessagestyled__SingleMessageContainer-sc-hgjxqs-0").filter(has_text=new_name).first
        del_btn = row.locator("img[src*='deleteIcon']").first
        del_btn.hover()
        mod_page.wait_for_timeout(200)
        del_btn.click(force=True)
        
        with performance_step("Delete Message", extras, limit_ms=2000):
            mod_page.get_by_role("button", name="מחיקה").click()
            mod_page.get_by_role("button", name="אישור").click()
            expect(mod_page.locator("span", has_text=new_name)).not_to_be_attached()

    # ---------------------------------------------------------
    # שלב 4: וידוא חסימות אבטחה
    # ---------------------------------------------------------
    def test_04_verify_restricted_pages_hidden(self, mod_page, extras):
        print("\n🔒 Verifying restricted pages are hidden...")

        with performance_step("Security Checks (Elements Hidden)", extras, limit_ms=1000):
            expect(mod_page.get_by_role("button", name="עולמות תוכן")).not_to_be_visible()
            expect(mod_page.get_by_role("button", name="סביבות")).not_to_be_visible()