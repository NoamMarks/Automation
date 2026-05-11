"""
HTML dashboard with metrics + analytics for a multi-run pytest session.

Self-contained: no external scripts, no CDN requests, just inlined HTML
+ CSS + hand-rendered SVG charts. Open the file in any browser.

Same call shape as the markdown summaries:
    generate_html_dashboard(runs, output_path)

Sections in the output:
    1. Headline metrics (donut chart + KPI tiles)
    2. Per-feature-area pass-rate bars
    3. Per-run trend table
    4. Failure analysis (exception-type buckets)
    5. Stability index (most-failing tests)
    6. Slowest tests (top 15 by avg duration)
    7. Full per-test status grid
"""

import ast
import base64
import html
import math
import os
import re
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime, timedelta


# Translation table for feature-area names — re-uses the same labels as
# the markdown summary so people see consistent vocabulary across both.
try:
    from utils.generate_simple_summary import FEATURE_AREAS, DEFAULT_AREA
except Exception:
    FEATURE_AREAS, DEFAULT_AREA = {}, {"title": "(unrecognized)", "explanation": ""}


# ============================================================
# JUnit parsing
# ============================================================

def _parse_junit(junit_path):
    if not junit_path or not os.path.exists(junit_path):
        return None
    try:
        tree = ET.parse(junit_path)
        root = tree.getroot()
        suite = root.find("testsuite") if root.tag != "testsuite" else root
        cases = []
        for tc in suite.findall("testcase"):
            failure = tc.find("failure")
            error = tc.find("error")
            skipped = tc.find("skipped")
            msg = ""
            if failure is not None:
                msg = failure.attrib.get("message", "")
            elif error is not None:
                msg = error.attrib.get("message", "")
            elif skipped is not None:
                msg = skipped.attrib.get("message", "")
            cases.append({
                "classname": tc.attrib.get("classname", ""),
                "name":      tc.attrib.get("name", ""),
                "time":      float(tc.attrib.get("time", 0)),
                "failed":    (failure is not None) or (error is not None),
                "skipped":   skipped is not None,
                "msg":       msg,
            })
        return {
            "tests":     int(suite.attrib.get("tests", 0)),
            "failures":  int(suite.attrib.get("failures", 0)),
            "errors":    int(suite.attrib.get("errors", 0)),
            "skipped":   int(suite.attrib.get("skipped", 0)),
            "time":      float(suite.attrib.get("time", 0)),
            "testcases": cases,
        }
    except Exception:
        return None


def _short_id(classname, name):
    cls = classname.split(".")[-1] if classname else ""
    return f"{cls}::{name}" if cls else name


# ============================================================
# Test docstring collection (powers the hover tooltips)
# ============================================================

_TESTS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests"
)


# ============================================================
# Zero-touch failure-artifact matching
# ============================================================

# Default location used by conftest's failure-capture hook
_ERRORS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "zero_touch_logs", "errors",
)
_TS_RE = re.compile(r"(\d{8})_(\d{6})")


def _parse_artifact_ts(filename):
    m = _TS_RE.search(filename)
    if not m:
        return None
    try:
        return datetime.strptime(f"{m.group(1)}_{m.group(2)}", "%Y%m%d_%H%M%S")
    except ValueError:
        return None


def _collect_artifacts_for_runs(runs, errors_dir=_ERRORS_DIR, buffer_sec=2):
    """Return {test_name: {"screenshots": [...], "logs": [...]}} across all
    run windows. Uses the same window-matching logic as the master report.
    """
    grouped = defaultdict(lambda: {"screenshots": [], "logs": []})
    if not os.path.isdir(errors_dir):
        return dict(grouped)

    files = sorted(os.listdir(errors_dir))
    for run in runs:
        lower = run["start"]
        upper = run["end"] + timedelta(seconds=buffer_sec)
        for f in files:
            ts = _parse_artifact_ts(f)
            if ts is None or not (lower <= ts <= upper):
                continue
            full = os.path.join(errors_dir, f)
            if f.endswith(".png"):
                test_name = f.rsplit("_", 2)[0]
                grouped[test_name]["screenshots"].append(full)
            elif f.endswith("_logs.txt"):
                test_name = f.rsplit("_", 3)[0]
                grouped[test_name]["logs"].append(full)
    return dict(grouped)


def _img_data_url(path):
    """Read a PNG and return a data: URL so the dashboard stays self-contained."""
    try:
        with open(path, "rb") as f:
            b = base64.b64encode(f.read()).decode("ascii")
        return f"data:image/png;base64,{b}"
    except Exception:
        return ""


def _read_log_file(path, max_chars=8000):
    """Read a logs.txt; truncate to keep the dashboard a reasonable size."""
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            content = f.read().strip()
        if len(content) > max_chars:
            return (content[:max_chars]
                    + f"\n... (truncated — {len(content)-max_chars} more chars in source file)")
        return content
    except Exception as e:
        return f"(could not read log: {type(e).__name__}: {e})"


def _collect_test_docstrings(tests_dir=_TESTS_DIR):
    """Walk tests/test_*.py and return {ClassName::method_name: docstring}.

    Uses ast so we don't have to import the test modules (which would
    trigger their conftest dependencies, fixtures, etc).
    """
    out = {}
    if not os.path.isdir(tests_dir):
        return out
    for fname in sorted(os.listdir(tests_dir)):
        if not (fname.startswith("test_") and fname.endswith(".py")):
            continue
        path = os.path.join(tests_dir, fname)
        try:
            with open(path, encoding="utf-8") as f:
                tree = ast.parse(f.read(), filename=path)
        except Exception:
            continue
        for cls in ast.iter_child_nodes(tree):
            if not isinstance(cls, ast.ClassDef):
                continue
            for fn in cls.body:
                if isinstance(fn, ast.FunctionDef) and fn.name.startswith("test_"):
                    doc = ast.get_docstring(fn) or ""
                    doc = re.sub(r"\s+", " ", doc).strip() if doc else ""
                    out[f"{cls.name}::{fn.name}"] = doc
    return out


def _error_bucket(msg):
    if not msg:
        return "(no message)"
    line = msg.strip().splitlines()[0]
    m = re.search(r"([A-Z]\w*(?:Error|Exception))", line)
    return m.group(1) if m else line[:50]


def _fmt_duration(seconds):
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    if seconds < 60:
        return f"{seconds:.1f}s"
    m, s = divmod(int(seconds), 60)
    if m < 60:
        return f"{m}m {s:02d}s"
    h, m = divmod(m, 60)
    return f"{h}h {m:02d}m"


# ============================================================
# SVG donut chart
# ============================================================

def _svg_donut(passed, failed, skipped, size=210, stroke=22):
    """Three-segment donut for pass/fail/skip counts (dark-mode neon)."""
    total = max(1, passed + failed + skipped)
    cx = cy = size / 2
    r = (size - stroke) / 2
    circ = 2 * math.pi * r
    p_len = circ * passed / total
    f_len = circ * failed / total
    s_len = circ * skipped / total
    PASS = "#00e676"
    FAIL = "#ff3d6e"
    SKIP = "#ffb300"
    TRACK = "rgba(255,255,255,0.06)"
    parts = []
    parts.append(f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
                 f'xmlns="http://www.w3.org/2000/svg">')
    parts.append('<defs>')
    parts.append('<filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/>'
                 '<feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>')
    parts.append('</defs>')
    # Background ring (subtle)
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                 f'stroke="{TRACK}" stroke-width="{stroke}" />')
    # Outer hairline
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r + stroke/2 + 4}" fill="none" '
                 f'stroke="rgba(0,229,255,0.10)" stroke-width="1" stroke-dasharray="2 4" />')
    offset = 0
    for length, color in ((p_len, PASS), (f_len, FAIL), (s_len, SKIP)):
        if length <= 0:
            continue
        parts.append(
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
            f'stroke="{color}" stroke-width="{stroke}" '
            f'stroke-linecap="round" '
            f'stroke-dasharray="{max(0, length-2):.2f} {circ-(length-2):.2f}" '
            f'stroke-dashoffset="{-(offset+1):.2f}" '
            f'transform="rotate(-90 {cx} {cy})" filter="url(#glow)" />'
        )
        offset += length
    rate = 100 * passed / total
    parts.append(
        f'<text x="{cx}" y="{cy+2}" text-anchor="middle" '
        f'font-family="JetBrains Mono,ui-monospace,monospace" '
        f'font-size="40" font-weight="700" fill="#ffffff">{rate:.0f}<tspan font-size="22" fill="#00e5ff">%</tspan></text>'
    )
    parts.append(
        f'<text x="{cx}" y="{cy+26}" text-anchor="middle" '
        f'font-family="JetBrains Mono,ui-monospace,monospace" '
        f'font-size="9" fill="#6f8aa8" letter-spacing="3">PASS RATE</text>'
    )
    parts.append("</svg>")
    return "".join(parts)


def _hbar(label, value, total, color="#4caf50", width=320):
    """Horizontal bar with label on left, percent on right."""
    pct = 0 if total == 0 else 100 * value / total
    bar_w = int(width * pct / 100)
    return (
        f'<div class="hbar-row">'
        f'<div class="hbar-label">{html.escape(label)}</div>'
        f'<div class="hbar-track" style="width:{width}px;">'
        f'<div class="hbar-fill" style="width:{bar_w}px;background:{color};"></div>'
        f'</div>'
        f'<div class="hbar-value">{value}/{total} ({pct:.0f}%)</div>'
        f'</div>'
    )


# ============================================================
# Main builder
# ============================================================


_CSS = """
        :root {
            --pass: #00e676;
            --fail: #ff3d6e;
            --skip: #ffb300;
            --cyan: #00e5ff;
            --violet: #b388ff;
            --bg: #07090f;
            --bg-2: #0c1220;
            --card: rgba(15, 22, 38, 0.85);
            --card-hover: rgba(20, 28, 48, 0.95);
            --border: rgba(0, 229, 255, 0.18);
            --border-strong: rgba(0, 229, 255, 0.55);
            --text: #e6f2ff;
            --text-strong: #ffffff;
            --muted: #6f8aa8;
            --muted-2: #4a5d76;
            --grid-line: rgba(0, 229, 255, 0.06);
        }
        * { box-sizing: border-box; }
        html, body { margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                         Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg);
            background-image:
                radial-gradient(ellipse 80% 50% at 50% -10%, rgba(0, 229, 255, 0.10), transparent 60%),
                radial-gradient(ellipse 60% 40% at 80% 100%, rgba(179, 136, 255, 0.08), transparent 60%),
                linear-gradient(var(--grid-line) 1px, transparent 1px),
                linear-gradient(90deg, var(--grid-line) 1px, transparent 1px);
            background-size: auto, auto, 48px 48px, 48px 48px;
            color: var(--text);
            padding: 32px 20px 80px;
            min-height: 100vh;
            -webkit-font-smoothing: antialiased;
        }
        .mono { font-family: "JetBrains Mono", ui-monospace, "SF Mono",
                              "Cascadia Mono", Consolas, monospace; }
        .container { max-width: 1280px; margin: 0 auto; }
        h1 {
            margin: 0;
            font-size: 30px;
            font-weight: 700;
            letter-spacing: -0.01em;
            color: var(--text-strong);
        }
        h1 .accent { color: var(--cyan); }
        h2 {
            margin: 0 0 16px;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 0.16em;
            text-transform: uppercase;
            color: var(--cyan);
            font-family: "JetBrains Mono", ui-monospace, monospace;
        }
        h2::before { content: "// "; color: var(--muted-2); }
        .topbar {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 8px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border);
        }
        .meta {
            color: var(--muted);
            font-size: 12px;
            letter-spacing: 0.06em;
            text-transform: uppercase;
            font-family: "JetBrains Mono", ui-monospace, monospace;
            margin-top: 8px;
        }
        .meta .sep { color: var(--muted-2); margin: 0 10px; }
        .live-dot {
            display: inline-block;
            width: 8px; height: 8px;
            border-radius: 50%;
            background: var(--cyan);
            box-shadow: 0 0 8px var(--cyan), 0 0 14px var(--cyan);
            margin-right: 8px;
            animation: pulse 1.6s infinite ease-in-out;
        }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.35; }
        }
        .grid { display: grid; gap: 16px; margin-bottom: 20px; }
        .grid.cols-3 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
        .grid.cols-2 { grid-template-columns: repeat(auto-fit, minmax(420px, 1fr)); }
        .card {
            position: relative;
            background: var(--card);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            padding: 24px;
            border-radius: 4px;
            border: 1px solid var(--border);
            transition: border-color .25s, box-shadow .25s, background .25s;
        }
        .card::before {
            content: "";
            position: absolute;
            top: -1px; left: -1px;
            width: 12px; height: 12px;
            border-top: 2px solid var(--cyan);
            border-left: 2px solid var(--cyan);
            opacity: 0.7;
        }
        .card::after {
            content: "";
            position: absolute;
            bottom: -1px; right: -1px;
            width: 12px; height: 12px;
            border-bottom: 2px solid var(--cyan);
            border-right: 2px solid var(--cyan);
            opacity: 0.7;
        }
        .card:hover {
            border-color: var(--border-strong);
            background: var(--card-hover);
            box-shadow: 0 0 24px rgba(0, 229, 255, 0.10);
        }
        .kpi {
            display: flex;
            flex-direction: column;
            justify-content: center;
            text-align: left;
            min-height: 110px;
        }
        .kpi .value {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 42px;
            font-weight: 700;
            line-height: 1;
            letter-spacing: -0.02em;
        }
        .kpi .label {
            font-size: 11px;
            color: var(--muted);
            margin-top: 10px;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            font-family: "JetBrains Mono", ui-monospace, monospace;
        }
        .kpi.pass .value { color: var(--pass); text-shadow: 0 0 12px rgba(0, 230, 118, 0.45); }
        .kpi.fail .value { color: var(--fail); text-shadow: 0 0 12px rgba(255, 61, 110, 0.45); }
        .kpi.skip .value { color: var(--skip); text-shadow: 0 0 10px rgba(255, 179, 0, 0.40); }
        .kpi.duration .value { color: var(--cyan); text-shadow: 0 0 10px rgba(0, 229, 255, 0.40); }
        .donut-card { display: flex; align-items: center; gap: 24px; }
        .donut-card svg { flex-shrink: 0; }
        .donut-legend { font-size: 13px; font-family: "JetBrains Mono", ui-monospace, monospace; }
        .donut-legend .swatch {
            display: inline-block; width: 10px; height: 10px;
            border-radius: 1px; margin-right: 10px; vertical-align: middle;
            box-shadow: 0 0 8px currentColor;
        }
        .donut-legend .row { margin-bottom: 8px; color: var(--text); }
        .donut-legend .row strong { color: var(--text-strong); margin-left: 4px; }
        .status-banner {
            padding: 18px 24px;
            border-radius: 4px;
            font-weight: 700;
            font-size: 13px;
            letter-spacing: 0.18em;
            text-transform: uppercase;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-family: "JetBrains Mono", ui-monospace, monospace;
            position: relative;
            overflow: hidden;
        }
        .status-banner.ok {
            background: linear-gradient(90deg, rgba(0, 230, 118, 0.18), rgba(0, 229, 255, 0.10));
            color: var(--pass);
            border: 1px solid rgba(0, 230, 118, 0.45);
            box-shadow: inset 0 0 24px rgba(0, 230, 118, 0.10);
        }
        .status-banner.fail {
            background: linear-gradient(90deg, rgba(255, 61, 110, 0.18), rgba(255, 179, 0, 0.10));
            color: var(--fail);
            border: 1px solid rgba(255, 61, 110, 0.45);
            box-shadow: inset 0 0 24px rgba(255, 61, 110, 0.10);
        }
        .status-banner .secondary {
            color: var(--text);
            font-weight: 500;
            letter-spacing: 0.08em;
        }
        .hbar-row {
            display: grid;
            grid-template-columns: 1fr 320px 140px;
            align-items: center;
            gap: 16px;
            margin-bottom: 10px;
            font-size: 13px;
        }
        .hbar-label { color: var(--text); }
        .hbar-track {
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.06);
            height: 14px;
            border-radius: 2px;
            overflow: hidden;
            position: relative;
        }
        .hbar-track::before {
            content: "";
            position: absolute;
            inset: 0;
            background-image: repeating-linear-gradient(
                90deg, transparent 0, transparent 19px, rgba(255,255,255,0.04) 19px, rgba(255,255,255,0.04) 20px
            );
            pointer-events: none;
        }
        .hbar-fill {
            height: 100%;
            transition: width .35s ease-out;
            box-shadow: 0 0 10px currentColor;
        }
        .hbar-value {
            color: var(--muted);
            font-variant-numeric: tabular-nums;
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 12px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }
        th, td {
            text-align: left;
            padding: 10px 14px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }
        tbody tr:hover { background: rgba(0, 229, 255, 0.04); }
        th {
            background: transparent;
            font-weight: 700;
            color: var(--muted);
            font-size: 10px;
            text-transform: uppercase;
            letter-spacing: 0.16em;
            font-family: "JetBrains Mono", ui-monospace, monospace;
            border-bottom: 1px solid var(--border);
        }
        td.num {
            text-align: right;
            font-variant-numeric: tabular-nums;
            font-family: "JetBrains Mono", ui-monospace, monospace;
        }
        td code {
            background: rgba(0, 229, 255, 0.06);
            border: 1px solid rgba(0, 229, 255, 0.12);
            color: var(--cyan);
            padding: 2px 6px;
            border-radius: 2px;
            font-size: 12px;
        }
        .pill {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 3px 10px;
            border-radius: 2px;
            font-size: 10px;
            font-weight: 700;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            font-family: "JetBrains Mono", ui-monospace, monospace;
        }
        .pill::before {
            content: "";
            width: 6px; height: 6px;
            border-radius: 50%;
            background: currentColor;
            box-shadow: 0 0 6px currentColor;
        }
        .pill.pass {
            background: rgba(0, 230, 118, 0.10);
            color: var(--pass);
            border: 1px solid rgba(0, 230, 118, 0.35);
        }
        .pill.fail {
            background: rgba(255, 61, 110, 0.10);
            color: var(--fail);
            border: 1px solid rgba(255, 61, 110, 0.35);
        }
        .pill.skip {
            background: rgba(255, 179, 0, 0.10);
            color: var(--skip);
            border: 1px solid rgba(255, 179, 0, 0.35);
        }
        details > summary {
            cursor: pointer;
            padding: 10px 0;
            color: var(--cyan);
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 12px;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            list-style: none;
        }
        details > summary::before { content: "[+] "; color: var(--muted); }
        details[open] > summary::before { content: "[-] "; color: var(--cyan); }
        details[open] > summary { color: var(--text-strong); }
        .grid-status td {
            padding: 8px 12px;
            font-size: 12px;
            border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        }
        .err-msg {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 11px;
            color: var(--fail);
            opacity: 0.85;
            white-space: pre-wrap;
            word-break: break-word;
        }
        ::selection { background: rgba(0, 229, 255, 0.30); color: var(--text-strong); }
        ::-webkit-scrollbar { width: 10px; height: 10px; }
        ::-webkit-scrollbar-track { background: var(--bg); }
        ::-webkit-scrollbar-thumb {
            background: rgba(0, 229, 255, 0.18);
            border-radius: 1px;
        }
        ::-webkit-scrollbar-thumb:hover { background: rgba(0, 229, 255, 0.35); }

        /* View tabs (per-run filter) */
        .tab-bar {
            display: flex;
            gap: 4px;
            margin-bottom: 20px;
            padding: 6px;
            background: rgba(15, 22, 38, 0.65);
            border: 1px solid var(--border);
            border-radius: 4px;
            overflow-x: auto;
        }
        .tab {
            background: transparent;
            border: 1px solid transparent;
            color: var(--muted);
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            padding: 8px 16px;
            border-radius: 3px;
            cursor: pointer;
            transition: background .2s, color .2s, border-color .2s;
            white-space: nowrap;
        }
        .tab:hover {
            color: var(--text);
            background: rgba(0, 229, 255, 0.04);
        }
        .tab.tab-active {
            background: rgba(0, 229, 255, 0.10);
            border-color: rgba(0, 229, 255, 0.35);
            color: var(--cyan);
            box-shadow: 0 0 12px rgba(0, 229, 255, 0.20);
        }
        .tab .pill-mini {
            display: inline-block;
            margin-left: 6px;
            padding: 1px 6px;
            border-radius: 999px;
            font-size: 9px;
            background: rgba(255, 61, 110, 0.20);
            color: var(--fail);
            font-weight: 700;
        }
        .view[hidden] { display: none; }

        /* Hover tooltips for test rows */
        [data-tip] {
            cursor: help;
            position: relative;
        }
        [data-tip]:hover::after {
            content: attr(data-tip);
            position: absolute;
            bottom: calc(100% + 8px);
            left: 0;
            transform: none;
            background: #0a1424;
            border: 1px solid var(--border-strong);
            border-radius: 4px;
            padding: 10px 14px;
            font-family: -apple-system, "Segoe UI", sans-serif;
            font-size: 12px;
            color: var(--text);
            line-height: 1.5;
            min-width: 280px;
            max-width: 520px;
            white-space: normal;
            box-shadow: 0 4px 24px rgba(0,0,0,0.6),
                        0 0 16px rgba(0, 229, 255, 0.15);
            z-index: 50;
            letter-spacing: normal;
            text-transform: none;
            font-weight: 400;
            pointer-events: none;
        }
        [data-tip]:hover::before {
            content: "";
            position: absolute;
            bottom: 100%;
            left: 16px;
            border: 6px solid transparent;
            border-top-color: var(--border-strong);
            z-index: 51;
            pointer-events: none;
        }

        /* Failure forensics — screenshots + console errors */
        .forensic-block {
            border: 1px solid rgba(255, 61, 110, 0.30);
            border-radius: 4px;
            padding: 16px;
            margin-bottom: 16px;
            background: rgba(255, 61, 110, 0.04);
        }
        .forensic-block .test-id {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            color: var(--fail);
            font-size: 13px;
            font-weight: 700;
            margin-bottom: 4px;
        }
        .forensic-block .err-headline {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 11px;
            color: var(--text);
            opacity: 0.85;
            margin-bottom: 12px;
            padding-bottom: 10px;
            border-bottom: 1px dashed rgba(255, 61, 110, 0.20);
            white-space: pre-wrap;
            word-break: break-word;
        }
        .forensic-block img {
            display: block;
            width: 100%;
            max-width: 900px;
            border: 1px solid var(--border);
            border-radius: 4px;
            background: #000;
            margin-bottom: 12px;
            cursor: zoom-in;
            transition: transform .2s;
        }
        .forensic-block img:hover { border-color: var(--border-strong); }
        .forensic-block .console-log {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 11px;
            color: var(--text);
            background: #000814;
            border: 1px solid var(--border);
            border-radius: 4px;
            padding: 12px 14px;
            white-space: pre-wrap;
            word-break: break-word;
            max-height: 400px;
            overflow-y: auto;
            line-height: 1.55;
        }
        .forensic-block .console-log .lvl-error { color: var(--fail); }
        .forensic-block .console-log .lvl-warn { color: var(--skip); }
        .forensic-block .no-artifacts {
            font-family: "JetBrains Mono", ui-monospace, monospace;
            font-size: 11px;
            color: var(--muted);
            font-style: italic;
        }

        /* Sticky thead for the full per-test grid table */
        .grid-status thead th {
            position: sticky;
            top: 0;
            background: var(--bg-2);
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            box-shadow: 0 1px 0 var(--border);
            z-index: 5;
        }
        .grid-status {
            /* Reduce row hover-area cut-off near sticky header */
            border-collapse: separate;
            border-spacing: 0;
        }
"""


def _build_view_html(runs_subset, tip_for):
    """Render one view's content (status banner through full test grid).

    Called once per view (aggregate + per-run). Returns a list of HTML strings.
    All metrics (donut, KPIs, per-area bars, stability, forensics, etc.) reflect
    only `runs_subset`. `tip_for` is a closure that returns tooltip text for
    a given test ID (precomputed by the caller from test docstrings).
    """
    parsed = [(r, _parse_junit(r.get("junit_path"))) for r in runs_subset]
    valid_runs = [(r, d) for r, d in parsed if d is not None]

    # Aggregate per-test outcomes
    by_id = {}
    classes = defaultdict(lambda: {"passes": 0, "fails": 0, "skips": 0, "ids": set()})
    error_buckets = Counter()
    duration_sum = defaultdict(float)
    duration_count = defaultdict(int)

    for run, data in valid_runs:
        for tc in data["testcases"]:
            tid = _short_id(tc["classname"], tc["name"])
            cls = tc["classname"].split(".")[-1] or "<unknown>"
            classes[cls]["ids"].add(tid)
            entry = by_id.setdefault(tid, {
                "cls": cls, "name": tc["name"],
                "passes": 0, "fails": 0, "skips": 0,
                "last_fail_msg": "",
            })
            duration_sum[tid] += tc["time"]
            duration_count[tid] += 1
            if tc["failed"]:
                entry["fails"] += 1
                classes[cls]["fails"] += 1
                entry["last_fail_msg"] = tc["msg"]
                error_buckets[_error_bucket(tc["msg"])] += 1
            elif tc["skipped"]:
                entry["skips"] += 1
                classes[cls]["skips"] += 1
            else:
                entry["passes"] += 1
                classes[cls]["passes"] += 1

    # Final per-test bucketing
    failed = [(tid, e) for tid, e in by_id.items() if e["fails"] > 0]
    skipped = [(tid, e) for tid, e in by_id.items()
               if e["fails"] == 0 and e["skips"] > 0]
    passed = [(tid, e) for tid, e in by_id.items()
              if e["fails"] == 0 and e["skips"] == 0]

    total_unique = len(by_id)
    n_runs = len(runs_subset)
    valid_run_count = len(valid_runs)
    total_dur = sum((r["end"] - r["start"]).total_seconds() for r in runs_subset)

    # _tip_for is passed in by the caller (computed once per dashboard).
    _tip_for = tip_for

    # Per-area summary
    area_rows = []
    for cls, c in classes.items():
        tests = len(c["ids"])
        # Per-test outcome (over all runs aggregated)
        cls_pass = sum(1 for tid, e in by_id.items()
                       if e["cls"] == cls and e["fails"] == 0 and e["skips"] == 0)
        cls_fail = sum(1 for tid, e in by_id.items()
                       if e["cls"] == cls and e["fails"] > 0)
        cls_skip = sum(1 for tid, e in by_id.items()
                       if e["cls"] == cls and e["fails"] == 0 and e["skips"] > 0)
        title = FEATURE_AREAS.get(cls, DEFAULT_AREA)["title"]
        area_rows.append((title, cls_pass, cls_fail, cls_skip, tests))
    # Sort: most failures first, then by name
    area_rows.sort(key=lambda r: (-r[2], -r[3], r[0]))

    # Per-run trend rows
    run_rows = []
    for run, data in parsed:
        if data is None:
            run_rows.append({
                "idx": run["run_idx"],
                "started": run["start"].strftime("%H:%M:%S"),
                "duration": _fmt_duration((run["end"] - run["start"]).total_seconds()),
                "tests": "—", "passed": "—", "failed": "—", "skipped": "—",
                "status": "no junit",
            })
            continue
        p = data["tests"] - data["failures"] - data["errors"] - data["skipped"]
        f = data["failures"] + data["errors"]
        run_rows.append({
            "idx": run["run_idx"],
            "started": run["start"].strftime("%H:%M:%S"),
            "duration": _fmt_duration(data["time"]),
            "tests": data["tests"],
            "passed": p,
            "failed": f,
            "skipped": data["skipped"],
            "status": "ok" if f == 0 else "fail",
        })

    # Stability — tests with failures sorted by failure rate
    stability = sorted(
        ((tid, e) for tid, e in by_id.items() if e["fails"] > 0),
        key=lambda x: (-x[1]["fails"], x[0]),
    )

    # Failure forensics — screenshots + console logs matched to run windows
    artifacts = _collect_artifacts_for_runs(runs_subset)

    # Slowest tests — by average duration
    slowest = sorted(
        ((tid, duration_sum[tid] / max(1, duration_count[tid]))
         for tid in by_id),
        key=lambda x: -x[1],
    )[:15]

    # ============================================================
    # HTML rendering
    # ============================================================
    pass_rate = 0 if total_unique == 0 else 100 * len(passed) / total_unique
    overall_status_class = "ok" if not failed else "fail"
    overall_status_text = (
        "PIPELINE NOMINAL" if not failed
        else f"DEGRADED — {len(failed)} FAILING"
    )


    # ---------- HTML sections (returned as a list of strings) ----------
    parts = []

    # Status banner
    parts.append(
        f"<div class='status-banner {overall_status_class}'>"
        f"<span>&gt; {overall_status_text}</span>"
        f"<span class='secondary'>"
        f"{len(passed)} pass &middot; {len(failed)} fail &middot; "
        f"{len(skipped)} skip &middot; {pass_rate:.0f}% rate"
        f"</span>"
        f"</div>"
    )

    # KPI tiles + donut
    parts.append("<div class='grid cols-3'>")
    parts.append(
        f"<div class='card donut-card'>"
        f"<div>{_svg_donut(len(passed), len(failed), len(skipped))}</div>"
        f"<div class='donut-legend'>"
        f"<div class='row'><span class='swatch' style='background:var(--pass);'></span>"
        f"Passed: <strong>{len(passed)}</strong></div>"
        f"<div class='row'><span class='swatch' style='background:var(--fail);'></span>"
        f"Failed: <strong>{len(failed)}</strong></div>"
        f"<div class='row'><span class='swatch' style='background:var(--skip);'></span>"
        f"Skipped: <strong>{len(skipped)}</strong></div>"
        f"<div class='row' style='margin-top:10px;color:var(--muted);'>"
        f"Total {total_unique} tests</div>"
        f"</div></div>"
    )
    parts.append(
        f"<div class='card kpi pass'>"
        f"<div class='value'>{len(passed)}</div>"
        f"<div class='label'>tests · pass</div></div>"
    )
    parts.append(
        f"<div class='card kpi fail'>"
        f"<div class='value'>{len(failed)}</div>"
        f"<div class='label'>tests · fail</div></div>"
    )
    parts.append(
        f"<div class='card kpi skip'>"
        f"<div class='value'>{len(skipped)}</div>"
        f"<div class='label'>tests · skip</div></div>"
    )
    parts.append(
        f"<div class='card kpi duration'>"
        f"<div class='value'>{_fmt_duration(total_dur)}</div>"
        f"<div class='label'>wall-clock · total</div></div>"
    )
    avg_run = (total_dur / valid_run_count) if valid_run_count else 0
    parts.append(
        f"<div class='card kpi duration'>"
        f"<div class='value'>{_fmt_duration(avg_run)}</div>"
        f"<div class='label'>wall-clock · avg/run</div></div>"
    )
    parts.append("</div>")

    # Per-feature-area pass-rate bars
    parts.append("<div class='card'>")
    parts.append("<h2>Coverage matrix · per feature area</h2>")
    for title, p, f, s, tests in area_rows:
        # Color the bar by overall area health
        if f > 0:
            color = "var(--fail)"
        elif s > 0:
            color = "var(--skip)"
        else:
            color = "var(--pass)"
        parts.append(_hbar(title, p, p + f + s, color=color))
    parts.append("</div>")

    # (Per-run trend table is rendered by generate_html_dashboard outside
    # all views, since it always shows the full set of runs.)

    # Failure analysis (exception buckets)
    if error_buckets:
        parts.append("<div class='card'>")
        parts.append("<h2>Anomaly classification · by exception type</h2>")
        parts.append("<table><thead><tr>"
                     "<th>Exception</th><th class='num'>Failures</th>"
                     "</tr></thead><tbody>")
        for k, v in error_buckets.most_common():
            parts.append(f"<tr><td><code>{html.escape(k)}</code></td>"
                         f"<td class='num'>{v}</td></tr>")
        parts.append("</tbody></table></div>")

    # Stability index
    if stability:
        parts.append("<div class='card'>")
        parts.append(f"<h2>Stability index · {len(stability)} test(s) flagged</h2>")
        parts.append(
            "<table><thead><tr>"
            "<th>Test</th><th class='num'>Failures</th>"
            "<th class='num'>Failure rate</th><th>Last error</th>"
            "</tr></thead><tbody>"
        )
        for tid, e in stability:
            f_rate = f"{e['fails']}/{n_runs}"
            err = (e["last_fail_msg"] or "").strip().splitlines()
            err_first = err[0][:200] if err else "(no message)"
            parts.append(
                f"<tr><td><code data-tip=\"{html.escape(_tip_for(tid))}\">"
                f"{html.escape(tid)}</code></td>"
                f"<td class='num'>{e['fails']}</td>"
                f"<td class='num'>{f_rate}</td>"
                f"<td class='err-msg'>{html.escape(err_first)}</td></tr>"
            )
        parts.append("</tbody></table></div>")

    # Failure forensics — screenshots + console errors per failed test
    if stability:
        parts.append("<div class='card'>")
        parts.append(f"<h2>Forensics · screenshots &amp; console errors</h2>")
        for tid, e in stability:
            test_method = tid.split("::", 1)[1] if "::" in tid else tid
            arts = artifacts.get(test_method, {"screenshots": [], "logs": []})
            err_lines = (e["last_fail_msg"] or "").strip().splitlines()
            err_headline = err_lines[0][:280] if err_lines else "(no error message)"

            parts.append("<div class='forensic-block'>")
            parts.append(
                f"<div class='test-id' data-tip=\"{html.escape(_tip_for(tid))}\">"
                f"&gt; {html.escape(tid)}</div>"
            )
            parts.append(
                f"<div class='err-headline'>{html.escape(err_headline)}</div>"
            )

            if arts["screenshots"]:
                for shot in arts["screenshots"]:
                    data_url = _img_data_url(shot)
                    if data_url:
                        parts.append(
                            f"<a href='{data_url}' target='_blank' rel='noopener'>"
                            f"<img src='{data_url}' "
                            f"alt='Screenshot at failure: {html.escape(os.path.basename(shot))}' "
                            f"title='Click to open full-size in new tab' />"
                            f"</a>"
                        )
            if arts["logs"]:
                for log_path in arts["logs"]:
                    log_text = _read_log_file(log_path)
                    parts.append(
                        f"<details open><summary>Console log · "
                        f"{html.escape(os.path.basename(log_path))}</summary>"
                        f"<pre class='console-log'>{html.escape(log_text)}</pre>"
                        f"</details>"
                    )
            if not arts["screenshots"] and not arts["logs"]:
                parts.append(
                    "<div class='no-artifacts'>"
                    "(no screenshot or console log was captured for this failure — "
                    "may have failed during fixture setup before the conftest hook ran)"
                    "</div>"
                )
            parts.append("</div>")
        parts.append("</div>")

    # Slowest tests
    if slowest and slowest[0][1] > 0:
        parts.append("<div class='card'>")
        parts.append("<h2>Latency report · top 15 slowest</h2>")
        parts.append("<table><thead><tr>"
                     "<th>Test</th><th class='num'>Avg duration</th>"
                     "</tr></thead><tbody>")
        for tid, d in slowest:
            parts.append(
                f"<tr><td><code data-tip=\"{html.escape(_tip_for(tid))}\">"
                f"{html.escape(tid)}</code></td>"
                f"<td class='num'>{_fmt_duration(d)}</td></tr>"
            )
        parts.append("</tbody></table></div>")

    # Full per-test status grid (collapsible)
    parts.append("<div class='card'>")
    parts.append("<h2>Full test grid</h2>")
    parts.append("<details open><summary>Show every test's verdict — "
                 "hover any test for a description</summary>")
    parts.append("<table class='grid-status' style='margin-top:12px;'>"
                 "<thead><tr><th>Status</th><th>Test</th>"
                 f"<th class='num'>Pass / Fail / Skip "
                 f"(of {n_runs} run{'s' if n_runs != 1 else ''})</th>"
                 "</tr></thead><tbody>")
    for tid in sorted(by_id.keys()):
        e = by_id[tid]
        if e["fails"] > 0:
            pill = "<span class='pill fail'>FAIL</span>"
        elif e["skips"] > 0:
            pill = "<span class='pill skip'>SKIP</span>"
        else:
            pill = "<span class='pill pass'>PASS</span>"
        parts.append(
            f"<tr><td>{pill}</td>"
            f"<td><code data-tip=\"{html.escape(_tip_for(tid))}\">"
            f"{html.escape(tid)}</code></td>"
            f"<td class='num'>{e['passes']} / {e['fails']} / {e['skips']}</td></tr>"
        )
    parts.append("</tbody></table></details></div>")

    return parts


# ============================================================
# Outer orchestrator — head, header, trend table, tab bar, all views, JS
# ============================================================

_TAB_SWITCHER_JS = """
(function () {
    function activate(viewId) {
        document.querySelectorAll('.tab').forEach(function (t) {
            t.classList.toggle('tab-active', t.dataset.view === viewId);
        });
        document.querySelectorAll('.view').forEach(function (v) {
            v.hidden = (v.dataset.view !== viewId);
        });
    }
    document.querySelectorAll('.tab').forEach(function (t) {
        t.addEventListener('click', function () { activate(t.dataset.view); });
    });
})();
"""


def _render_trend_table(runs):
    """Per-run trend table — always shows ALL runs, sits outside views."""
    parts = ["<div class='card'><h2>Run telemetry · trend</h2><table>"]
    parts.append(
        "<thead><tr><th>Run</th><th>Started</th><th>Duration</th>"
        "<th class='num'>Tests</th><th class='num'>Passed</th>"
        "<th class='num'>Failed</th><th class='num'>Skipped</th>"
        "<th>Status</th></tr></thead><tbody>"
    )
    for run in runs:
        data = _parse_junit(run.get("junit_path"))
        if data is None:
            wall = (run["end"] - run["start"]).total_seconds()
            parts.append(
                f"<tr><td>#{run['run_idx']}</td>"
                f"<td>{run['start'].strftime('%H:%M:%S')}</td>"
                f"<td>{_fmt_duration(wall)}</td>"
                f"<td class='num'>—</td><td class='num'>—</td>"
                f"<td class='num'>—</td><td class='num'>—</td>"
                f"<td><span class='pill fail'>NO JUNIT</span></td></tr>"
            )
            continue
        p = data["tests"] - data["failures"] - data["errors"] - data["skipped"]
        f = data["failures"] + data["errors"]
        pill_cls = "pass" if f == 0 else "fail"
        pill_lbl = "PASS" if f == 0 else "FAIL"
        parts.append(
            f"<tr><td>#{run['run_idx']}</td>"
            f"<td>{run['start'].strftime('%H:%M:%S')}</td>"
            f"<td>{_fmt_duration(data['time'])}</td>"
            f"<td class='num'>{data['tests']}</td>"
            f"<td class='num'>{p}</td>"
            f"<td class='num'>{f}</td>"
            f"<td class='num'>{data['skipped']}</td>"
            f"<td><span class='pill {pill_cls}'>{pill_lbl}</span></td></tr>"
        )
    parts.append("</tbody></table></div>")
    return parts


def _render_tab_bar(runs):
    """Tab bar — one tab for 'All runs (aggregate)' + one tab per run.

    Each tab has a `data-view` attribute that the JS uses to swap views.
    Per-run tabs include a small red pill if that run had any failures.
    """
    parts = ["<div class='tab-bar'>"]
    parts.append(
        "<button class='tab tab-active' data-view='all'>All runs (aggregate)</button>"
    )
    for run in runs:
        data = _parse_junit(run.get("junit_path"))
        n_fail = (data["failures"] + data["errors"]) if data else 0
        pill = (f"<span class='pill-mini'>{n_fail}</span>"
                if n_fail > 0 else "")
        parts.append(
            f"<button class='tab' data-view='{run['run_idx']}'>"
            f"Run {run['run_idx']}{pill}</button>"
        )
    parts.append("</div>")
    return parts


def generate_html_dashboard(runs, output_path):
    """Build the full self-contained HTML dashboard.

    Layout:
        Header
        Per-run trend table  (always full)
        Tab bar              (All / Run 1 / Run 2 / …)
        Aggregate view       (all runs)
        Per-run views        (one per run, hidden by default)
        Tab-switcher JS
    """
    # Compute docstrings + tooltip-text closure ONCE; share across views.
    docstrings = _collect_test_docstrings()

    def tip_for(tid):
        doc = docstrings.get(tid, "")
        cls = tid.split("::")[0]
        area = FEATURE_AREAS.get(cls, DEFAULT_AREA)
        if doc:
            return f"{doc}  ·  Area: {area['title']}"
        return f"{area['title']}  ·  {area['explanation']}"

    # Header-strip metrics — always reflect the FULL set of runs
    n_runs_total = len(runs)
    total_dur_all = sum((r["end"] - r["start"]).total_seconds() for r in runs)
    total_unique_all = set()
    for run in runs:
        data = _parse_junit(run.get("junit_path"))
        if data is None:
            continue
        for tc in data["testcases"]:
            total_unique_all.add(_short_id(tc["classname"], tc["name"]))

    parts = []
    parts.append("<!DOCTYPE html>")
    parts.append("<html lang='en'><head>")
    parts.append("<meta charset='utf-8'>")
    parts.append("<meta name='viewport' content='width=device-width,initial-scale=1'>")
    parts.append(
        f"<title>Test Dashboard — {datetime.now().strftime('%Y-%m-%d %H:%M')}</title>"
    )
    parts.append(f"<style>{_CSS}</style>")
    parts.append("</head><body><div class='container'>")

    # Header
    parts.append("<div class='topbar'><div>")
    parts.append("<h1><span class='accent'>QA</span> · Test Pipeline Telemetry</h1>")
    parts.append(
        f"<div class='meta'>"
        f"<span class='live-dot'></span>"
        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        f"<span class='sep'>|</span>"
        f"{n_runs_total} RUN{'S' if n_runs_total != 1 else ''}"
        f"<span class='sep'>|</span>"
        f"WALL-CLOCK {_fmt_duration(total_dur_all).upper()}"
        f"<span class='sep'>|</span>"
        f"{len(total_unique_all)} TESTS"
        f"</div></div></div>"
    )

    # Per-run trend table (always shows ALL runs)
    parts.extend(_render_trend_table(runs))

    # Tab bar (only render if there's more than 1 run; otherwise just the
    # aggregate view since 'aggregate' == 'run 1' anyway)
    if n_runs_total > 1:
        parts.extend(_render_tab_bar(runs))

    # Aggregate view ("all")
    parts.append("<div class='view' data-view='all'>")
    parts.extend(_build_view_html(runs, tip_for))
    parts.append("</div>")

    # Per-run views
    if n_runs_total > 1:
        for run in runs:
            parts.append(
                f"<div class='view' data-view='{run['run_idx']}' hidden>"
            )
            parts.extend(_build_view_html([run], tip_for))
            parts.append("</div>")

    # Tab-switcher JS
    if n_runs_total > 1:
        parts.append(f"<script>{_TAB_SWITCHER_JS}</script>")

    parts.append("</div></body></html>")

    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    return output_path
