import time
import csv
import os
from datetime import datetime
from playwright.sync_api import Playwright, sync_playwright, expect

# הגדרות
REPORT_FILE = "loader_report.csv"
NUM_ITERATIONS = 10  # מספר הפעמים שרוצים להריץ

def run(playwright: Playwright) -> None:
    # פתיחת דפדפן פעם אחת בלבד בתחילת הריצה
    browser = playwright.chromium.launch(headless=False)
    
    # רשימה לשמירת התוצאות לחישוב ממוצע בסוף
    all_durations = []

    print(f"\n🚀 Starting performance test: {NUM_ITERATIONS} iterations...\n")

    for i in range(NUM_ITERATIONS):
        current_run = i + 1
        print(f"--- Running Test {current_run} of {NUM_ITERATIONS} ---")
        
        # יצירת הקשר חדש (Context) לכל איטרציה - מדמה משתמש חדש ונקי מקוקיז
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(os.getenv("APP_URL", "https://front-zira.dev.orangepeak.net/"))

            loader = page.locator("#loader svg")
            popup_btn = page.get_by_role("button", name="הבנתי")

            # 1. בדיקה שהלואודר הופיע
            try:
                expect(loader).to_be_visible(timeout=5000)
            except:
                print(f"❌ Loader not found in run {current_run}. Skipping...")
                context.close()
                continue # עובר לאיטרציה הבאה

            start_time = time.perf_counter()

            # 2. לולאת הדגימה החכמה
            while loader.is_visible():
                if popup_btn.is_visible():
                    # אופציונלי: הדפסה רק אם רוצים לראות בלייב
                    # print("🔔 Pop-up detected! Clicking...") 
                    popup_btn.click()
                time.sleep(0.05)

            end_time = time.perf_counter()
            duration = end_time - start_time
            
            # הוספה לרשימת התוצאות
            all_durations.append(duration)

            print(f"✅ Run {current_run} finished: {duration:.4f} seconds")

            # 3. שמירה לקובץ CSV
            file_exists = os.path.isfile(REPORT_FILE)
            with open(REPORT_FILE, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                # כתיבת כותרות רק אם הקובץ לא היה קיים לפני תחילת הלולאה
                if not file_exists:
                    writer.writerow(["Date", "Time", "Iteration", "Duration (Seconds)"])
                
                now = datetime.now()
                writer.writerow([
                    now.strftime("%Y-%m-%d"), 
                    now.strftime("%H:%M:%S"), 
                    current_run,
                    f"{duration:.4f}"
                ])

        except Exception as e:
            print(f"⚠️ Error in run {current_run}: {e}")

        finally:
            # סגירת ה-Context כדי לנקות את הסביבה להרצה הבאה
            context.close()
            # השהייה קטנה בין הרצות כדי לתת למערכת "לנוח"
            time.sleep(1)

    # סיכום סופי
    if all_durations:
        avg_duration = sum(all_durations) / len(all_durations)
        print("\n" + "="*40)
        print(f"📊 Final Report for {len(all_durations)} successful runs:")
        print(f"⏱️  Average Time: {avg_duration:.4f}s")
        print(f"🚀 Fastest Time: {min(all_durations):.4f}s")
        print(f"🐢 Slowest Time: {max(all_durations):.4f}s")
        print("="*40)
    
    browser.close()

with sync_playwright() as playwright:
    run(playwright)