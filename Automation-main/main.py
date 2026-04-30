import sys, os, subprocess, webbrowser
from datetime import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QTextEdit, QProgressBar, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QIcon

# ודא ש־pytest ו־playwright זמינים
user_scripts = os.path.join(os.getenv("APPDATA"), "Python", "Python313", "Scripts")
if os.path.exists(os.path.join(user_scripts, "pytest.exe")):
    os.environ["PATH"] += os.pathsep + user_scripts
pw_browsers = os.path.join(os.getenv("LOCALAPPDATA"), "ms-playwright")
if os.path.exists(pw_browsers):
    os.environ["PLAYWRIGHT_BROWSERS_PATH"] = pw_browsers

class TestRunner(QThread):
    output_signal = pyqtSignal(str)
    finished_signal = pyqtSignal(bool)
    def __init__(self, test_path):
        super().__init__()
        self.test_path = test_path
        self._stop = False
        self.process = None
    def run(self):
        try:
            os.makedirs("reports", exist_ok=True)
            cmd = [
                "pytest", self.test_path,
                "--html=reports/report.html",
                "--self-contained-html",
                "--headed", "--browser=chromium"
            ]
            self.process = subprocess.Popen(
                cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                universal_newlines=True, shell=False
            )
            for line in self.process.stdout:
                if self._stop:
                    self.process.terminate()
                    self.output_signal.emit("🟥 Canceled by user.\n")
                    self.finished_signal.emit(False)
                    return
                self.output_signal.emit(line.rstrip())
            self.process.wait()
            self.finished_signal.emit(self.process.returncode == 0)
        except Exception as e:
            self.output_signal.emit(f"⚠️ Error: {e}")
            self.finished_signal.emit(False)

class PlaywrightUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🧪 Playwright Test Runner v5")
        self.setGeometry(400, 200, 720, 500)
        self.setWindowIcon(QIcon("icons/play.png"))
        self.output = QTextEdit(readOnly=True)
        self.progress = QProgressBar()
        self.progress.setRange(0,0)
        self.progress.hide()
        self.run_btn = QPushButton("▶️ Run Tests")
        self.cancel_btn = QPushButton("⏹️ Cancel", enabled=False)
        self.report_btn = QPushButton("📄 Open Report", enabled=False)
        btns = QHBoxLayout()
        for b in (self.run_btn, self.cancel_btn, self.report_btn): btns.addWidget(b)
        layout = QVBoxLayout(self)
        label = QLabel("Playwright Automated Test Runner", alignment=Qt.AlignCenter)
        layout.addWidget(label); layout.addLayout(btns)
        layout.addWidget(self.progress); layout.addWidget(self.output)
        self.run_btn.clicked.connect(self.run_tests)
        self.cancel_btn.clicked.connect(self.cancel_tests)
        self.report_btn.clicked.connect(lambda: webbrowser.open("reports/report.html"))
        self.thread=None
        self.setStyleSheet("""
            QWidget{background:#1e1e1e;color:#e5e5e5;font-family:Consolas;}
            QPushButton{background:#3b82f6;border:none;padding:8px;border-radius:6px;}
            QPushButton:hover{background:#2563eb;} QPushButton:disabled{background:#555;}
            QTextEdit{background:#0f172a;border:1px solid #334155;padding:6px;}
            QProgressBar{background:#0f172a;border:1px solid #334155;border-radius:6px;}
            QProgressBar::chunk{background:#10b981;width:20px;}
        """)
    def run_tests(self):
        self.output.append(f"[{datetime.now().strftime('%H:%M:%S')}] 🚀 Starting tests...\n")
        self.run_btn.setEnabled(False); self.cancel_btn.setEnabled(True)
        self.report_btn.setEnabled(False); self.progress.show()
        self.thread = TestRunner(r"C:\Users\Admin\amazon_playwright\playwright_pytest_project\tests\test_example.py")
        self.thread.output_signal.connect(self.update_output)
        self.thread.finished_signal.connect(self.on_finished)
        self.thread.start()
    def cancel_tests(self):
        if self.thread: self.thread._stop=True
    def update_output(self,text):
        self.output.append(text)
        self.output.verticalScrollBar().setValue(self.output.verticalScrollBar().maximum())
    def on_finished(self,success):
        self.run_btn.setEnabled(True); self.cancel_btn.setEnabled(False)
        self.report_btn.setEnabled(True); self.progress.hide()
        msg="✅ All tests passed!" if success else "❌ Some tests failed."
        self.output.append(f"\n{msg}\n"); QMessageBox.information(self,"Finished",msg)
        if os.path.exists("reports/report.html"): webbrowser.open("reports/report.html")

if __name__=="__main__":
    app=QApplication(sys.argv); w=PlaywrightUI(); w.show(); sys.exit(app.exec_())
