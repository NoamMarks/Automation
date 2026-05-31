"""
Desktop launcher for the Zira QA test suite.

Tkinter GUI that wraps `tests/run_multiple.py`. Designed to be built into a
single self-contained Windows .exe via PyInstaller (build_exe.bat) — the
.exe bundles Python, every dependency, the test source, and a Chromium
browser, so it runs on a fresh machine with no setup.

Two distinct modes:

  • Source mode (running this file directly with `py -3.13 run_gui.py`)
      Project root = the folder this file sits in. Reports go to
      <root>/reports/master/. .env loaded from <root>/.env if present.

  • Frozen mode (running the PyInstaller .exe)
      sys._MEIPASS is the runtime unpack dir holding tests/, pages/, utils/,
      and the bundled Chromium under pw-browsers/.
      The .exe has no .env beside it — credentials and the chosen reports
      folder live in %APPDATA%\\ZiraQA\\config.json, populated by a
      first-launch wizard the first time the .exe runs.
"""

import contextlib
import json
import os
import queue
import shutil
import subprocess
import sys
import threading
import traceback
import tkinter as tk
from datetime import datetime
from tkinter import ttk, scrolledtext, messagebox, filedialog

IS_FROZEN = bool(getattr(sys, "frozen", False))


# ----------------------------------------------------------------------
# Path resolution
# ----------------------------------------------------------------------
def _meipass_dir():
    """The PyInstaller runtime unpack directory (contains tests/, pages/,
    utils/, pw-browsers/ when frozen). Returns None in source mode."""
    if IS_FROZEN:
        return getattr(sys, "_MEIPASS", None)
    return None


def _source_root():
    """Project root when running from source. Walks up to find tests/run_multiple.py
    so the launcher works from any reasonable starting directory."""
    start = os.path.dirname(os.path.abspath(__file__))
    candidate = start
    for _ in range(5):
        if os.path.exists(os.path.join(candidate, "tests", "run_multiple.py")):
            return candidate
        parent = os.path.dirname(candidate)
        if parent == candidate:
            break
        candidate = parent
    return start


# The "code root" — where tests/ and pages/ and utils/ live. In frozen mode
# this is the temporary unpack dir; in source mode the project folder.
_CODE_ROOT = _meipass_dir() if IS_FROZEN else _source_root()


# ----------------------------------------------------------------------
# Config (creds + chosen reports folder) — persisted across launches
# ----------------------------------------------------------------------
CONFIG_DIR = os.path.join(os.environ.get("APPDATA",
                          os.path.expanduser("~")), "ZiraQA")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")
_DEBUG_LOG = os.path.join(CONFIG_DIR, "launcher_debug.log")

# Schema of config.json — what the wizard collects on first launch.
# APP_URL has a default so the wizard can pre-fill it; the rest are blank.
DEFAULT_APP_URL = "https://front-zira.dev.orangepeak.net/"

CRED_FIELDS = [
    # (env var name, label, is_secret, default)
    ("APP_URL",      "App URL",         False, DEFAULT_APP_URL),
    ("APP_USERNAME", "App username",    False, ""),
    ("APP_PASSWORD", "App password",    True,  ""),
    ("EMAIL_FROM",   "Sender email",    False, ""),
    ("EMAIL_PASS",   "Sender app pass", True,  ""),
    ("EMAIL_TO",     "Recipient(s)",    False, ""),
]

# Which environments exist and which credentials each one needs.
# PP/PROD are on-prem deployments without email — only the app creds.
# PROD additionally runs only the CRUD synthetic monitor (test_zira.py)
# instead of the full suite.
ENVIRONMENTS = ["TEST", "PP", "PROD"]
ENV_FIELDS = {
    "TEST": ["APP_URL", "APP_USERNAME", "APP_PASSWORD",
             "EMAIL_FROM", "EMAIL_PASS", "EMAIL_TO"],
    "PP":   ["APP_URL", "APP_USERNAME", "APP_PASSWORD"],
    "PROD": ["APP_URL", "APP_USERNAME", "APP_PASSWORD"],
}
# Test-collection target per env. The path is resolved against _CODE_ROOT
# at runtime so it works both in source mode and in the frozen .exe.
ENV_TEST_TARGET = {
    "TEST": "tests",
    "PP":   "tests",
    "PROD": os.path.join("tests", "test_zira.py"),
}


def _debug(msg):
    """Append a timestamped line to launcher_debug.log. Cheap insurance:
    without it, anything that goes wrong in a --noconsole .exe is invisible."""
    try:
        os.makedirs(CONFIG_DIR, exist_ok=True)
        with open(_DEBUG_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}\n")
    except Exception:
        pass


def _load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    try:
        with open(CONFIG_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        _debug(f"config load failed: {e}")
        return None


def _save_config(cfg):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(cfg, f, indent=2)


# ----------------------------------------------------------------------
# Shared form builder — populates a top-level window with the same
# reports-folder + environment + credentials UI used by both the
# first-launch wizard and the post-setup Settings dialog.
#
# Expects `instance` to be the wizard / dialog object with these
# attributes already initialised:
#   - instance.top         — the parent window
#   - instance.env_var     — StringVar pre-populated with current env
#   - instance.reports_var — created here if missing
# After the call, the instance also has:
#   - instance.cred_vars   — dict of env_var → StringVar
#   - instance.cred_widgets — dict for show/hide by env
# ----------------------------------------------------------------------
def _build_setup_form(instance, parent_window, title, intro_text,
                       initial_reports="", initial_creds=None):
    initial_creds = initial_creds or {}
    pad = 16
    frame = ttk.Frame(parent_window, padding=(pad, pad, pad, 0))
    frame.pack(fill=tk.BOTH, expand=True)

    ttk.Label(frame, text=title, font=("Segoe UI", 14, "bold")).pack(anchor="w")
    ttk.Label(frame, text=intro_text, foreground="#555",
              justify="left").pack(anchor="w", pady=(2, 12))

    # ---- Reports folder ----
    ttk.Label(frame, text="Reports folder",
              font=("Segoe UI", 10, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text="Where the HTML dashboard, PDF, WhatsApp text and JUnit "
             "files for each run are written. Available for every "
             "environment.",
        foreground="#666", wraplength=520,
    ).pack(anchor="w")
    row = ttk.Frame(frame)
    row.pack(fill=tk.X, pady=(4, 12))
    instance.reports_var = tk.StringVar(
        value=initial_reports or os.path.join(
            os.path.expanduser("~"), "Documents", "ZiraQA-Reports")
    )
    ttk.Entry(row, textvariable=instance.reports_var).pack(
        side=tk.LEFT, fill=tk.X, expand=True)
    ttk.Button(row, text="Browse…", command=instance._browse).pack(
        side=tk.LEFT, padx=(8, 0))

    # ---- Environment ----
    ttk.Label(frame, text="Environment",
              font=("Segoe UI", 10, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text="PROD runs only the CRUD monitor (test_zira.py). "
             "TEST and PP run the full suite. PP and PROD don't collect "
             "email fields (on-prem deployments).",
        foreground="#666", wraplength=520,
    ).pack(anchor="w")
    env_row = ttk.Frame(frame)
    env_row.pack(fill=tk.X, pady=(4, 12))
    for env in ENVIRONMENTS:
        ttk.Radiobutton(
            env_row, text=env, value=env, variable=instance.env_var,
            command=instance._refresh_cred_visibility,
        ).pack(side=tk.LEFT, padx=(0, 18))

    # ---- Credentials (all rows created; visibility driven by env) ----
    ttk.Label(frame, text="Credentials",
              font=("Segoe UI", 10, "bold")).pack(anchor="w")
    ttk.Label(
        frame,
        text="App username/password are required. Email fields are "
             "optional and only shown for TEST.",
        foreground="#666", wraplength=520,
    ).pack(anchor="w", pady=(0, 6))

    instance.cred_vars = {}
    instance.cred_widgets = {}
    grid = ttk.Frame(frame)
    grid.pack(fill=tk.X)
    for r, (key, label, secret, default) in enumerate(CRED_FIELDS):
        lbl = ttk.Label(grid, text=label + ":")
        lbl.grid(row=r, column=0, sticky="w", padx=(0, 8), pady=2)
        var = tk.StringVar(value=initial_creds.get(key, default))
        entry = ttk.Entry(grid, textvariable=var, width=42,
                          show="•" if secret else "")
        entry.grid(row=r, column=1, sticky="ew", pady=2)
        instance.cred_vars[key] = var
        instance.cred_widgets[key] = (lbl, entry)
    grid.columnconfigure(1, weight=1)
    instance._refresh_cred_visibility()


def _refresh_cred_visibility_for(instance):
    """Show/hide credential rows based on the currently selected env."""
    visible = set(ENV_FIELDS.get(instance.env_var.get(), []))
    for key, (lbl, entry) in instance.cred_widgets.items():
        if key in visible:
            lbl.grid()
            entry.grid()
        else:
            lbl.grid_remove()
            entry.grid_remove()


# ----------------------------------------------------------------------
# First-launch wizard
# ----------------------------------------------------------------------
class FirstLaunchWizard:
    """Standalone wizard window collecting reports folder + credentials.

    Implemented as its OWN tk.Tk() root (not a Toplevel) on purpose: on
    Windows, a Toplevel created against a withdrawn root window exists in
    code but is never actually rendered — the process sits forever waiting
    for input on an invisible window. Owning the root removes that whole
    failure mode.
    """

    def __init__(self):
        self.result = None
        self.top = tk.Tk()
        self.top.title("Zira QA — First-launch setup")
        w, h = 560, 640
        self.top.geometry(f"{w}x{h}")
        self.top.resizable(False, False)
        # Center on the primary monitor so the user can't miss it.
        self.top.update_idletasks()
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()
        self.top.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
        # Force to front on first appearance, then drop topmost so the user
        # can put other windows on top normally afterwards.
        self.top.attributes("-topmost", True)
        self.top.after(500, lambda: self.top.attributes("-topmost", False))
        self.top.lift()
        self.top.focus_force()

        self.env_var = tk.StringVar(value="TEST")
        _build_setup_form(
            self, self.top,
            title="Welcome to Zira QA Runner",
            intro_text="This setup runs once. The values are saved to:\n"
                       + CONFIG_PATH,
        )

        # ---- Buttons ----
        btns = ttk.Frame(self.top, padding=(16, 12, 16, 16))
        btns.pack(fill=tk.X, side=tk.BOTTOM)
        ttk.Button(btns, text="Save and continue",
                   command=self._on_save).pack(side=tk.RIGHT)
        ttk.Button(btns, text="Cancel",
                   command=self._on_cancel).pack(side=tk.RIGHT, padx=(0, 8))

        self.top.protocol("WM_DELETE_WINDOW", self._on_cancel)
        self.top.mainloop()

    def _browse(self):
        chosen = filedialog.askdirectory(
            parent=self.top, title="Choose reports folder",
            mustexist=False,
        )
        if chosen:
            self.reports_var.set(chosen)

    def _refresh_cred_visibility(self):
        _refresh_cred_visibility_for(self)

    def _on_save(self):
        reports_dir = self.reports_var.get().strip()
        if not reports_dir:
            messagebox.showerror("Missing", "Please choose a reports folder.",
                                 parent=self.top)
            return
        # Validate required app creds (only those visible for this env).
        env = self.env_var.get()
        active_fields = set(ENV_FIELDS.get(env, []))
        missing = []
        if "APP_USERNAME" in active_fields and not self.cred_vars["APP_USERNAME"].get().strip():
            missing.append("App username")
        if "APP_PASSWORD" in active_fields and not self.cred_vars["APP_PASSWORD"].get().strip():
            missing.append("App password")
        if missing:
            messagebox.showerror(
                "Missing", "Required fields are empty:\n  • " + "\n  • ".join(missing),
                parent=self.top,
            )
            return

        try:
            os.makedirs(reports_dir, exist_ok=True)
        except Exception as e:
            messagebox.showerror(
                "Cannot create folder",
                f"Could not create reports folder:\n{reports_dir}\n\n{e}",
                parent=self.top,
            )
            return

        # Persist only the fields relevant to the selected env so hidden
        # values (e.g. stale email creds when env switched to PP) don't
        # leak into os.environ later.
        creds = {k: (self.cred_vars[k].get() if k in active_fields else "")
                 for k, _, _, _ in CRED_FIELDS}
        self.result = {
            "reports_dir": reports_dir,
            "environment": env,
            "creds": creds,
        }
        # When self.top is a tk.Tk root (the first-launch wizard), the
        # __init__ blocks on mainloop() — must call quit() to break out
        # before destroy(). For the Toplevel reuse in _open_settings_dialog,
        # quit() is harmless (no active mainloop to quit).
        try:
            self.top.quit()
        except Exception:
            pass
        self.top.destroy()

    def _on_cancel(self):
        self.result = None
        try:
            self.top.quit()
        except Exception:
            pass
        self.top.destroy()


# ----------------------------------------------------------------------
# Settings dialog — same fields as the wizard, used post-setup to edit
# ----------------------------------------------------------------------
def _open_settings_dialog(parent, current_cfg):
    """Reuses the wizard's form-builder against an existing root window.
    Returns the updated config dict, or None if the user cancelled."""
    wiz = FirstLaunchWizard.__new__(FirstLaunchWizard)
    wiz.result = None
    wiz.top = tk.Toplevel(parent)
    wiz.top.title("Zira QA — Settings")
    wiz.top.geometry("560x600")
    wiz.top.transient(parent)
    wiz.top.grab_set()
    wiz.top.resizable(False, False)
    wiz.env_var = tk.StringVar(
        value=current_cfg.get("environment", "TEST"))

    _build_setup_form(
        wiz, wiz.top,
        title="Settings",
        intro_text=f"Stored at: {CONFIG_PATH}",
        initial_reports=current_cfg.get("reports_dir", ""),
        initial_creds=current_cfg.get("creds", {}),
    )

    btns = ttk.Frame(wiz.top, padding=(16, 12, 16, 16))
    btns.pack(fill=tk.X, side=tk.BOTTOM)
    ttk.Button(btns, text="Save", command=wiz._on_save).pack(side=tk.RIGHT)
    ttk.Button(btns, text="Cancel", command=wiz._on_cancel).pack(
        side=tk.RIGHT, padx=(0, 8))

    wiz.top.protocol("WM_DELETE_WINDOW", wiz._on_cancel)
    wiz.top.wait_window()
    return wiz.result


# ----------------------------------------------------------------------
# Environment wiring — applies a loaded config to the current process
# before the suite is invoked.
# ----------------------------------------------------------------------
def _apply_config_to_env(cfg):
    """Pump creds + bundled-browser path + sys.path into os.environ so
    everything downstream (conftest, pytest-playwright, send_email) finds
    what it needs without touching disk."""
    for key, value in cfg.get("creds", {}).items():
        if value:
            os.environ[key] = value

    if IS_FROZEN:
        # Point Playwright at the chromium we bundled. Without this it
        # would look in %LOCALAPPDATA%\\ms-playwright which doesn't exist
        # on a fresh machine.
        browsers = os.path.join(_CODE_ROOT, "pw-browsers")
        if os.path.isdir(browsers):
            os.environ["PLAYWRIGHT_BROWSERS_PATH"] = browsers
            _debug(f"PLAYWRIGHT_BROWSERS_PATH = {browsers}")
        else:
            _debug(f"WARNING: bundled browsers dir not found at {browsers}")

        # Make tests/, pages/, utils/ importable in frozen mode.
        if _CODE_ROOT not in sys.path:
            sys.path.insert(0, _CODE_ROOT)


# ----------------------------------------------------------------------
# Stdout/stderr redirect helper — pipes printed output into the GUI queue
# ----------------------------------------------------------------------
class _QueueWriter:
    """File-like object whose .write() pushes lines onto a queue.Queue.
    Lets us redirect stdout/stderr from the worker thread into the UI.

    Implements just enough of the io.TextIOBase protocol that pytest's
    capture / plugin discovery doesn't choke. fileno() raises
    UnsupportedOperation — the right exception for a stream not backed
    by an OS file descriptor (faulthandler / capture handle this and
    skip the fd-level work)."""

    encoding = "utf-8"
    errors = "replace"

    def __init__(self, q, kind="line"):
        self.q = q
        self.kind = kind
        self._buf = ""

    def write(self, s):
        if not s:
            return 0
        self._buf += s
        # Flush complete lines as they arrive — keeps the log responsive
        # while a long pytest command is still printing.
        while "\n" in self._buf:
            line, self._buf = self._buf.split("\n", 1)
            self.q.put((self.kind, line + "\n"))
        return len(s)

    def flush(self):
        if self._buf:
            self.q.put((self.kind, self._buf))
            self._buf = ""

    def fileno(self):
        import io as _io
        raise _io.UnsupportedOperation("queue-backed writer has no fileno")

    def isatty(self):
        return False

    def writable(self):
        return True

    def readable(self):
        return False

    def seekable(self):
        return False


# ----------------------------------------------------------------------
# Main window
# ----------------------------------------------------------------------
class QARunnerGUI:
    """Single-window launcher. Holds the worker thread + queue of stdout lines."""

    POLL_MS = 100   # how often we drain the output queue into the UI

    def __init__(self, root, config):
        self.root = root
        self.config = config
        self.root.title("Zira QA — Test Runner")
        w, h = 820, 620
        self.root.geometry(f"{w}x{h}")
        self.root.minsize(640, 480)
        # Center on the primary monitor + force to front. Otherwise the
        # main window often opens behind whatever the user was looking
        # at and they assume the .exe didn't open.
        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{w}x{h}+{(sw - w) // 2}+{(sh - h) // 2}")
        self.root.attributes("-topmost", True)
        self.root.after(500, lambda: self.root.attributes("-topmost", False))
        self.root.lift()
        self.root.focus_force()

        self.worker = None
        self.cancel_requested = False
        self.output_queue = queue.Queue()

        self._build_ui()
        self.root.after(self.POLL_MS, self._drain_output_queue)

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------
    def _build_ui(self):
        form = ttk.Frame(self.root, padding=(16, 12, 16, 8))
        form.pack(fill=tk.X)

        ttk.Label(form, text="Zira QA Test Runner",
                  font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w")
        ttk.Label(form,
                  text="Choose iteration count, press Start. Reports land in "
                       "the folder configured in Settings.",
                  foreground="#555", wraplength=780).grid(
            row=1, column=0, columnspan=4, sticky="w", pady=(2, 12))

        ttk.Label(form, text="Number of runs:").grid(row=2, column=0, sticky="w")
        self.runs_var = tk.IntVar(value=5)
        self.runs_spin = ttk.Spinbox(
            form, from_=1, to=50, width=6, textvariable=self.runs_var,
        )
        self.runs_spin.grid(row=2, column=1, sticky="w", padx=(8, 24))

        self.headless_var = tk.BooleanVar(value=False)
        self.headless_check = ttk.Checkbutton(
            form, text="Run headless (no visible browser)",
            variable=self.headless_var,
        )
        self.headless_check.grid(row=2, column=2, sticky="w")

        # Environment display (driven by config). PROD runs only test_zira.py;
        # TEST/PP run the full suite.
        ttk.Label(form, text="Environment:").grid(
            row=3, column=0, sticky="w", pady=(8, 0))
        self.env_label_var = tk.StringVar(value=self._env_summary())
        ttk.Label(form, textvariable=self.env_label_var,
                  foreground="#0c4a6e", font=("Segoe UI", 10, "bold")
                  ).grid(row=3, column=1, columnspan=3,
                         sticky="w", pady=(8, 0))

        # Reports-folder display (read-only)
        ttk.Label(form, text="Reports folder:").grid(
            row=4, column=0, sticky="w", pady=(4, 0))
        self.reports_label_var = tk.StringVar(value=self.config["reports_dir"])
        ttk.Label(form, textvariable=self.reports_label_var,
                  foreground="#0c4a6e").grid(
            row=4, column=1, columnspan=3, sticky="w", pady=(4, 0))

        # Action buttons
        btns = ttk.Frame(self.root, padding=(16, 0, 16, 8))
        btns.pack(fill=tk.X)
        self.start_btn = ttk.Button(btns, text="▶  Start", command=self._on_start)
        self.start_btn.pack(side=tk.LEFT)
        self.cancel_btn = ttk.Button(btns, text="✕  Cancel", state=tk.DISABLED,
                                     command=self._on_cancel)
        self.cancel_btn.pack(side=tk.LEFT, padx=(8, 0))
        self.open_btn = ttk.Button(btns, text="📁  Open reports folder",
                                   command=self._open_reports_folder)
        self.open_btn.pack(side=tk.LEFT, padx=(8, 0))
        self.settings_btn = ttk.Button(btns, text="⚙  Settings",
                                       command=self._on_settings)
        self.settings_btn.pack(side=tk.RIGHT)

        # Status strip
        self.status_var = tk.StringVar(value="Idle.")
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X)
        status_bar = ttk.Frame(self.root, padding=(16, 6))
        status_bar.pack(fill=tk.X)
        ttk.Label(status_bar, textvariable=self.status_var,
                  foreground="#0c4a6e", font=("Segoe UI", 10)).pack(side=tk.LEFT)

        # Log pane
        log_frame = ttk.Frame(self.root, padding=(16, 0, 16, 12))
        log_frame.pack(fill=tk.BOTH, expand=True)
        self.log = scrolledtext.ScrolledText(
            log_frame, wrap=tk.WORD, font=("Consolas", 9),
            bg="#0a1424", fg="#e6f2ff", insertbackground="#e6f2ff",
        )
        self.log.pack(fill=tk.BOTH, expand=True)
        self.log.configure(state=tk.DISABLED)

    # ------------------------------------------------------------------
    # Run lifecycle
    # ------------------------------------------------------------------
    def _on_start(self):
        if self.worker is not None:
            return
        try:
            n_runs = int(self.runs_var.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Invalid input", "Number of runs must be an integer.")
            return
        if n_runs < 1:
            messagebox.showerror("Invalid input", "Number of runs must be ≥ 1.")
            return

        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.runs_spin.config(state=tk.DISABLED)
        self.headless_check.config(state=tk.DISABLED)
        self.settings_btn.config(state=tk.DISABLED)
        self._clear_log()
        self._set_status(f"Running {n_runs} iteration(s)…")

        self.cancel_requested = False
        _debug(f"start run; n={n_runs} headless={self.headless_var.get()} "
               f"reports={self.config['reports_dir']}")
        self.worker = threading.Thread(
            target=self._run_in_process,
            args=(n_runs, self.headless_var.get()),
            daemon=True,
        )
        self.worker.start()

    def _env_summary(self):
        env = self.config.get("environment", "TEST")
        scope = ("test_zira.py only (CRUD synthetic monitor)"
                 if env == "PROD" else "full suite")
        return f"{env}  —  {scope}"

    def _env_test_path(self):
        """Resolve the per-env test target against the unpacked source dir.
        Falls back to running all tests if the configured env isn't known."""
        target = ENV_TEST_TARGET.get(
            self.config.get("environment", "TEST"), "tests")
        return os.path.join(_CODE_ROOT, target)

    def _run_in_process(self, n_runs, headless):
        """Invoke the suite in this same process. Redirect stdout/stderr
        to the GUI queue so pytest's live output shows up in the log pane."""
        qw_out = _QueueWriter(self.output_queue, kind="line")
        qw_err = _QueueWriter(self.output_queue, kind="line")
        exit_code = 0
        try:
            with contextlib.redirect_stdout(qw_out), \
                 contextlib.redirect_stderr(qw_err):
                # Import lazily so the GUI shows up before the (slow)
                # pytest+playwright import work happens.
                from tests.run_multiple import run_suite
                run_suite(
                    num_runs=n_runs,
                    headless=headless,
                    reports_dir=os.path.join(self.config["reports_dir"], "master"),
                    test_path=self._env_test_path(),
                )
        except SystemExit as e:
            # pytest.main() raises SystemExit on some paths.
            exit_code = int(getattr(e, "code", 0) or 0)
            _debug(f"SystemExit from suite: {exit_code}")
        except Exception as e:
            tb = traceback.format_exc()
            _debug(f"suite crashed: {type(e).__name__}: {e}\n{tb}")
            self.output_queue.put(("error",
                f"\n[launcher] Suite crashed: {type(e).__name__}: {e}\n{tb}\n"))
            exit_code = -1
        finally:
            qw_out.flush()
            qw_err.flush()
            self.output_queue.put(("done", exit_code))

    def _on_cancel(self):
        # In-process cancellation isn't safe to do cleanly mid-pytest. The
        # only honest option is "let the user know we can't kill it from
        # here, point them at Task Manager". We surface that rather than
        # pretending Cancel works.
        if not messagebox.askyesno(
            "Cancel run?",
            "The suite runs in-process and can't be interrupted cleanly "
            "from the UI. Closing the launcher window will terminate it "
            "abruptly (any partial reports are kept). Close the launcher now?",
        ):
            return
        self.root.destroy()

    # ------------------------------------------------------------------
    # Output streaming
    # ------------------------------------------------------------------
    def _drain_output_queue(self):
        try:
            while True:
                kind, payload = self.output_queue.get_nowait()
                if kind == "line":
                    self._append_log(payload)
                elif kind == "error":
                    self._append_log(payload, tag="err")
                elif kind == "done":
                    self._on_finished(payload)
        except queue.Empty:
            pass
        finally:
            self.root.after(self.POLL_MS, self._drain_output_queue)

    def _append_log(self, text, tag=None):
        self.log.configure(state=tk.NORMAL)
        if tag:
            self.log.tag_configure("err", foreground="#ff6b8a")
            self.log.insert(tk.END, text, (tag,))
        else:
            self.log.insert(tk.END, text)
        self.log.see(tk.END)
        self.log.configure(state=tk.DISABLED)

    def _clear_log(self):
        self.log.configure(state=tk.NORMAL)
        self.log.delete("1.0", tk.END)
        self.log.configure(state=tk.DISABLED)

    def _set_status(self, msg):
        self.status_var.set(msg)

    def _on_finished(self, rc):
        self.worker = None
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        self.runs_spin.config(state=tk.NORMAL)
        self.headless_check.config(state=tk.NORMAL)
        self.settings_btn.config(state=tk.NORMAL)
        if rc == 0:
            self._set_status("✓ Done. Reports written to "
                             f"{self.config['reports_dir']}")
        elif rc == -1:
            self._set_status("✗ Launcher error — see log.")
        else:
            self._set_status(f"⚠ Pytest exited with code {rc}. "
                             "Reports may still be written.")

    # ------------------------------------------------------------------
    def _on_settings(self):
        new_cfg = _open_settings_dialog(self.root, self.config)
        if new_cfg is None:
            return
        self.config = new_cfg
        _save_config(self.config)
        _apply_config_to_env(self.config)
        self.reports_label_var.set(self.config["reports_dir"])
        self.env_label_var.set(self._env_summary())
        self._set_status("Settings saved.")

    def _open_reports_folder(self):
        target = self.config["reports_dir"]
        os.makedirs(target, exist_ok=True)
        if sys.platform == "win32":
            os.startfile(target)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", target])
        else:
            subprocess.Popen(["xdg-open", target])


# ----------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------
def _sweep_stale_mei_dirs():
    """Delete leftover `_MEI*` unpack dirs in %TEMP% from previous launches.

    PyInstaller's onefile bootloader extracts ~340 MB to a fresh
    %TEMP%\\_MEI<random>\\ on EVERY launch and only cleans it up if the
    process exits cleanly. Task-Manager kills, crashes, and OS reboots
    leave the folder behind — they pile up to multiple GB fast.

    Strategy: sweep at startup. Anything we can delete clearly wasn't in
    use; anything currently in use will raise PermissionError and be
    skipped silently (PyInstaller holds open handles inside the dir for
    the duration of the run, so the OS prevents deletion of our own
    in-use dir).
    """
    if not IS_FROZEN:
        return
    our_dir = os.path.realpath(_CODE_ROOT or "")
    # PyInstaller's bootloader writes _MEI* siblings to OUR unpack dir,
    # so the dir holding sibling _MEI dirs is exactly our parent. Using
    # tempfile.gettempdir() here is wrong — the shell's TMP env var can
    # point somewhere else than where the bootloader actually wrote us.
    temp_root = os.path.dirname(our_dir) if our_dir else ""
    if not temp_root or not os.path.isdir(temp_root):
        _debug(f"sweep: cannot resolve temp_root from our_dir={our_dir!r}")
        return
    try:
        candidates = [
            os.path.join(temp_root, name)
            for name in os.listdir(temp_root)
            if name.startswith("_MEI")
        ]
    except Exception as e:
        _debug(f"sweep: listdir({temp_root!r}) failed: "
               f"{type(e).__name__}: {e}")
        return
    swept = 0
    skipped_self = 0
    locked = 0
    freed_mb = 0
    for path in candidates:
        if not os.path.isdir(path):
            continue
        if os.path.realpath(path) == our_dir:
            skipped_self += 1
            continue
        try:
            size = sum(
                os.path.getsize(os.path.join(d, f))
                for d, _, fs in os.walk(path)
                for f in fs
                if os.path.exists(os.path.join(d, f))
            )
        except Exception:
            size = 0
        try:
            shutil.rmtree(path, ignore_errors=False)
            swept += 1
            freed_mb += size / (1024 * 1024)
        except Exception as e:
            # In use by another running launcher, or partial-delete locked.
            # Cheap to ignore — next launch will retry.
            locked += 1
            _debug(f"sweep: could not delete {path}: "
                   f"{type(e).__name__}: {e}")
    _debug(f"sweep: candidates={len(candidates)} swept={swept} "
           f"freed={freed_mb:.0f}MB self={skipped_self} locked={locked}")


def main():
    _debug(f"launcher start; frozen={IS_FROZEN} exe={sys.executable} "
           f"code_root={_CODE_ROOT}")
    _sweep_stale_mei_dirs()

    config = _load_config()
    if config is None:
        _debug("no config — running first-launch wizard")
        wizard = FirstLaunchWizard()       # owns its own tk.Tk() root
        _debug(f"wizard returned; result_is_none={wizard.result is None}")
        if wizard.result is None:
            _debug("wizard cancelled — exiting")
            return
        config = wizard.result
        _save_config(config)

    _apply_config_to_env(config)

    # Fresh tk.Tk() for the main launcher — the wizard's root (if any)
    # has already been destroyed.
    root = tk.Tk()
    QARunnerGUI(root, config)
    root.mainloop()
    _debug("launcher exit")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        tb = traceback.format_exc()
        _debug(f"FATAL: {type(e).__name__}: {e}\n{tb}")
        try:
            messagebox.showerror(
                "Launcher crashed",
                f"{type(e).__name__}: {e}\n\nDetails written to:\n{_DEBUG_LOG}",
            )
        except Exception:
            pass
        raise
