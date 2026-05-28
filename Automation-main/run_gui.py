"""
Desktop launcher for the Zira QA test suite.

Tkinter GUI that wraps `tests/run_multiple.py` so a non-technical user can
configure the number of iterations and press a button instead of typing
commands. Live-streams subprocess stdout to a log pane. When the run
finishes, opens File Explorer at the reports folder so the user can grab
the WhatsApp .txt + dashboard PDF for sharing.

Package to a Windows .exe with the included build_exe.bat (PyInstaller).
"""

import os
import queue
import shutil
import subprocess
import sys
import threading
import traceback
import tkinter as tk
from datetime import datetime
from tkinter import ttk, scrolledtext, messagebox


# ----------------------------------------------------------------------
# Locate the project. We can't assume the .exe sits exactly at the
# project root — PyInstaller writes it to `dist\` by default, and users
# may move it around. Walk up from the executable's directory looking
# for the unambiguous "I'm the project root" marker:
#     <root>/tests/run_multiple.py
# This way the .exe Just Works whether it's at the root, in `dist\`,
# in a desktop shortcut location, etc. Limited to 5 levels so we don't
# wander up the whole filesystem if it really isn't there.
# ----------------------------------------------------------------------
def _find_project_root():
    if getattr(sys, "frozen", False):
        start = os.path.dirname(sys.executable)
    else:
        start = os.path.dirname(os.path.abspath(__file__))

    candidate = start
    for _ in range(5):
        if os.path.exists(os.path.join(candidate, "tests", "run_multiple.py")):
            return candidate
        parent = os.path.dirname(candidate)
        if parent == candidate:        # hit filesystem root
            break
        candidate = parent
    # Fall back to start; the UI will show a helpful error if the file
    # genuinely isn't reachable.
    return start


_PROJECT_ROOT = _find_project_root()
_RUN_MULTIPLE = os.path.join(_PROJECT_ROOT, "tests", "run_multiple.py")
_REPORTS_DIR = os.path.join(_PROJECT_ROOT, "reports", "master")
_DEBUG_LOG = os.path.join(_PROJECT_ROOT, "launcher_debug.log")


def _debug(msg):
    """Append a timestamped line to launcher_debug.log. Cheap insurance:
    without it, anything that goes wrong in a --noconsole .exe is invisible."""
    try:
        with open(_DEBUG_LOG, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().isoformat(timespec='seconds')}] {msg}\n")
    except Exception:
        pass


def _find_python_interpreter():
    """Locate a real Python interpreter to run pytest under.

    The pitfall: when bundled by PyInstaller, `sys.executable` points to the
    .exe itself, NOT to python.exe. Spawning [sys.executable, "run_multiple.py"]
    would just open another copy of the launcher GUI. We have to find an
    actual python.exe on the system.

    Search order:
      1. sys.executable IF we're not frozen (running as a normal script)
      2. python.exe on PATH
      3. py.exe (Python launcher) on PATH — call it with "py -3"
      4. None — caller will surface a clear error to the user
    """
    if not getattr(sys, "frozen", False):
        return [sys.executable]

    py = shutil.which("python.exe") or shutil.which("python")
    if py:
        return [py]
    pylauncher = shutil.which("py.exe") or shutil.which("py")
    if pylauncher:
        return [pylauncher, "-3"]
    return None


class QARunnerGUI:
    """Single-window launcher. Holds the subprocess + a queue of stdout lines."""

    POLL_MS = 100   # how often we drain the subprocess-output queue into the UI

    def __init__(self, root):
        self.root = root
        self.root.title("Zira QA — Test Runner")
        self.root.geometry("820x600")
        self.root.minsize(640, 480)

        self.process = None
        self.output_queue = queue.Queue()
        self.run_thread = None

        self._build_ui()
        # Periodic poll — copies any pending stdout lines into the log view.
        self.root.after(self.POLL_MS, self._drain_output_queue)

    # ------------------------------------------------------------------
    # UI construction
    # ------------------------------------------------------------------
    def _build_ui(self):
        # Top form
        form = ttk.Frame(self.root, padding=(16, 12, 16, 8))
        form.pack(fill=tk.X)

        ttk.Label(form, text="Zira QA Test Runner",
                  font=("Segoe UI", 16, "bold")).grid(
            row=0, column=0, columnspan=4, sticky="w")
        ttk.Label(form,
                  text="Configure the run, press Start, the suite runs the same way "
                       "it does from the command line. Reports land in "
                       "reports/master/.",
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

        # Status strip
        self.status_var = tk.StringVar(value="Idle.")
        ttk.Separator(self.root, orient=tk.HORIZONTAL).pack(fill=tk.X)
        status_bar = ttk.Frame(self.root, padding=(16, 6))
        status_bar.pack(fill=tk.X)
        ttk.Label(status_bar, textvariable=self.status_var,
                  foreground="#0c4a6e", font=("Segoe UI", 10)).pack(side=tk.LEFT)

        # Log pane (live subprocess output)
        log_frame = ttk.Frame(self.root, padding=(16, 0, 16, 12))
        log_frame.pack(fill=tk.BOTH, expand=True)
        self.log = scrolledtext.ScrolledText(
            log_frame, wrap=tk.WORD, font=("Consolas", 9),
            bg="#0a1424", fg="#e6f2ff",
            insertbackground="#e6f2ff",
        )
        self.log.pack(fill=tk.BOTH, expand=True)
        self.log.configure(state=tk.DISABLED)

    # ------------------------------------------------------------------
    # Run lifecycle
    # ------------------------------------------------------------------
    def _on_start(self):
        if self.process is not None:
            return
        try:
            n_runs = int(self.runs_var.get())
        except (tk.TclError, ValueError):
            messagebox.showerror("Invalid input", "Number of runs must be an integer.")
            return
        if n_runs < 1:
            messagebox.showerror("Invalid input", "Number of runs must be ≥ 1.")
            return
        if not os.path.exists(_RUN_MULTIPLE):
            messagebox.showerror(
                "Project not found",
                f"Can't find tests/run_multiple.py at:\n{_RUN_MULTIPLE}\n\n"
                "The launcher must run from the project root (or the .exe "
                "must sit next to the project files).",
            )
            return

        # Disable inputs while running
        self.start_btn.config(state=tk.DISABLED)
        self.cancel_btn.config(state=tk.NORMAL)
        self.runs_spin.config(state=tk.DISABLED)
        self.headless_check.config(state=tk.DISABLED)
        self._clear_log()
        self._set_status(f"Running {n_runs} iteration(s)…")

        # Spawn pytest in a background thread so the UI stays responsive
        env = os.environ.copy()
        env["NUM_RUNS"] = str(n_runs)
        if self.headless_var.get():
            env["HEADLESS"] = "1"
        env.setdefault("PYTHONIOENCODING", "utf-8")
        env.setdefault("PYTHONUTF8", "1")

        # Find a real Python interpreter. When frozen, sys.executable IS
        # this .exe — running it again would just spawn another launcher,
        # not pytest. Must point at a system python.exe.
        python_cmd = _find_python_interpreter()
        if python_cmd is None:
            _debug("no python interpreter on PATH; aborting")
            messagebox.showerror(
                "Python not found",
                "The launcher couldn't find a Python interpreter on PATH.\n\n"
                "Install Python 3.13 from python.org (tick 'Add to PATH' "
                "during install) and then try again.\n\n"
                "If Python is installed under a different name, run from a "
                "terminal: where python.exe",
            )
            # Re-enable the UI since we never started the run
            self.start_btn.config(state=tk.NORMAL)
            self.cancel_btn.config(state=tk.DISABLED)
            self.runs_spin.config(state=tk.NORMAL)
            self.headless_check.config(state=tk.NORMAL)
            self._set_status("Idle.")
            return
        _debug(f"using python: {python_cmd}; runs={n_runs} headless={self.headless_var.get()}")

        self.run_thread = threading.Thread(
            target=self._run_subprocess,
            args=(python_cmd, env),
            daemon=True,
        )
        self.run_thread.start()

    def _run_subprocess(self, python_cmd, env):
        """Run pytest, stream every stdout line into the queue.

        `python_cmd` is a list — e.g. ["C:\\Python313\\python.exe"]
        or ["py.exe", "-3"]. We append the run_multiple.py path to it.
        """
        cmd = list(python_cmd) + [_RUN_MULTIPLE]
        _debug(f"spawning: {cmd}  cwd={_PROJECT_ROOT}")
        try:
            # creationflags lets us kill the whole process tree on cancel
            # (without it, terminating the python parent leaves Chromium
            # subprocesses orphaned on Windows).
            creationflags = 0
            if sys.platform == "win32":
                creationflags = subprocess.CREATE_NEW_PROCESS_GROUP

            self.process = subprocess.Popen(
                cmd,
                cwd=_PROJECT_ROOT,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                encoding="utf-8",
                errors="replace",
                env=env,
                bufsize=1,
                creationflags=creationflags,
            )
            _debug(f"subprocess started, pid={self.process.pid}")
        except Exception as e:
            _debug(f"failed to start subprocess: {type(e).__name__}: {e}\n{traceback.format_exc()}")
            self.output_queue.put(("error", f"Failed to start: {type(e).__name__}: {e}\n"))
            self.output_queue.put(("done", -1))
            return

        try:
            for line in self.process.stdout:
                self.output_queue.put(("line", line))
        except Exception as e:
            _debug(f"stdout read failed: {e}")
            self.output_queue.put(("error", f"Output stream failed: {e}\n"))

        rc = self.process.wait()
        _debug(f"subprocess exited rc={rc}")
        self.output_queue.put(("done", rc))

    def _on_cancel(self):
        if self.process is None:
            return
        if not messagebox.askyesno(
            "Cancel run?",
            "Cancelling will terminate the test process mid-run. "
            "Already-written report files (if any) are kept. "
            "Continue?",
        ):
            return
        try:
            if sys.platform == "win32":
                # Send CTRL_BREAK to the process group we created
                self.process.send_signal(subprocess.signal.CTRL_BREAK_EVENT)
            else:
                self.process.terminate()
        except Exception as e:
            self.output_queue.put(("error", f"Cancel failed: {e}\n"))
        self._set_status("Cancelling…")

    # ------------------------------------------------------------------
    # Output streaming — pull from queue, append to log widget
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
            self.log.insert(tk.END, text, (tag,))
            self.log.tag_configure("err", foreground="#ff6b8a")
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
        self.process = None
        self.start_btn.config(state=tk.NORMAL)
        self.cancel_btn.config(state=tk.DISABLED)
        self.runs_spin.config(state=tk.NORMAL)
        self.headless_check.config(state=tk.NORMAL)
        if rc == 0:
            self._set_status("✓ Done. Reports written to reports/master/.")
        elif rc == -1:
            self._set_status("✗ Launcher error — see log.")
        else:
            self._set_status(f"⚠ Pytest exited with code {rc}. "
                             "Reports may still be written.")

    # ------------------------------------------------------------------
    def _open_reports_folder(self):
        os.makedirs(_REPORTS_DIR, exist_ok=True)
        if sys.platform == "win32":
            os.startfile(_REPORTS_DIR)
        elif sys.platform == "darwin":
            subprocess.Popen(["open", _REPORTS_DIR])
        else:
            subprocess.Popen(["xdg-open", _REPORTS_DIR])


def main():
    _debug(f"launcher start; frozen={getattr(sys, 'frozen', False)} "
           f"exe={sys.executable} project={_PROJECT_ROOT}")
    root = tk.Tk()
    QARunnerGUI(root)
    root.mainloop()
    _debug("launcher exit")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        _debug(f"FATAL: {type(e).__name__}: {e}\n{traceback.format_exc()}")
        # In --noconsole .exe mode the user wouldn't see the traceback
        # otherwise. Show a dialog as a last resort.
        try:
            messagebox.showerror(
                "Launcher crashed",
                f"{type(e).__name__}: {e}\n\n"
                f"Details written to:\n{_DEBUG_LOG}",
            )
        except Exception:
            pass
        raise