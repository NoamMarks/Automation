"""
Render the HTML dashboard to a PRINTABLE, READABLE PDF.

The live dashboard is a dark neon-themed SPA designed for screens. On paper
it's hard to read: low-contrast cyan-on-dark text, decorative gradients
that print muddy, and 6 visually-identical view sections with nothing
telling you which one is which.

This module renders a transformed copy of the dashboard:
  1. A cover page summarising the run set at a glance.
  2. A clear "VIEW: AGGREGATE / RUN N" banner at the top of every view
     section so a reader skimming pages knows exactly where they are.
  3. Light-theme print styles — white background, dark text, semantic
     colors preserved (green/red/yellow for pass/fail/skip).
  4. Hidden screen-only ornaments (tab bars, scroll bars, hover tooltips,
     pulsing live-dots).

Playwright (Chromium) is already a project dependency. WeasyPrint would
work but pulls heavy native deps (GTK on Linux/Mac, fragile on Windows).

Usage:
    from utils.dashboard_to_pdf import dashboard_html_to_pdf
    dashboard_html_to_pdf(html_path, pdf_path)
"""

import os

from playwright.sync_api import sync_playwright


# ============================================================
# Print CSS — light theme, high-contrast, paper-friendly
# ============================================================

_PRINT_CSS = """
@page {
    size: A4;
    margin: 14mm 12mm 14mm 12mm;
}

@media print {
    /* ----- Reveal every view (live page only shows :checked one) ----- */
    .view-switcher > .view-radio { display: none !important; }
    .view-switcher > .view { display: block !important; }
    .view-switcher > .view + .view { page-break-before: always; }
    .view-switcher > .tab-bar { display: none !important; }

    /* ----- Cover page break ----- */
    .pdf-cover + * { page-break-before: always; }

    /* ----- Light-theme background; kill the dot grid + glow ----- */
    html, body {
        background: #ffffff !important;
        background-image: none !important;
        color: #111827 !important;
        padding: 0 !important;
        margin: 0 !important;
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }
    body { padding: 0 !important; }
    .container { max-width: none !important; }

    /* ----- Headings ----- */
    h1 { color: #0f172a !important; font-size: 22px !important; }
    h1 .accent { color: #006da6 !important; }
    h2 {
        color: #0c4a6e !important;
        background: #f1f5f9;
        border-left: 3px solid #006da6;
        padding: 6px 10px;
        margin-bottom: 12px !important;
        font-size: 11px !important;
    }
    h2::before { color: #94a3b8 !important; }

    /* ----- Topbar meta ----- */
    .topbar { border-bottom: 1px solid #cbd5e1 !important; }
    .meta { color: #475569 !important; font-size: 10px !important; }
    .meta .sep { color: #94a3b8 !important; }
    .live-dot { display: none !important; }   /* no animation on paper */

    /* ----- Cards ----- */
    .card {
        background: #ffffff !important;
        backdrop-filter: none !important;
        -webkit-backdrop-filter: none !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: none !important;
        padding: 16px !important;
    }
    .card::before, .card::after { display: none !important; }   /* corner brackets */
    .card:hover { background: #ffffff !important; box-shadow: none !important; }

    /* ----- KPI tiles ----- */
    .kpi .label { color: #64748b !important; }
    .kpi.pass .value { color: #15803d !important; text-shadow: none !important; }
    .kpi.fail .value { color: #b91c1c !important; text-shadow: none !important; }
    .kpi.skip .value { color: #a16207 !important; text-shadow: none !important; }
    .kpi.duration .value { color: #0c4a6e !important; text-shadow: none !important; }
    .kpi .value { font-size: 32px !important; }

    /* ----- Donut card ----- */
    .donut-card { flex-direction: row !important; align-items: center !important; }
    .donut-legend { font-size: 12px !important; color: #334155 !important; }
    .donut-legend .row { color: #334155 !important; }
    .donut-legend strong { color: #0f172a !important; }
    .donut-legend .row[style*='margin-top'] { color: #475569 !important; }
    /* Donut center text is hard-coded fill="#ffffff" in the SVG — invisible
       on the now-white card background. Override via CSS (Chromium respects
       fill rules on SVG text). The pass-rate digits + "PASS RATE" label
       both come through. */
    .donut-card svg text { fill: #0f172a !important; }
    .donut-card svg text tspan { fill: #006da6 !important; }   /* the % sign */
    /* Track ring (the grey background donut) — gets a darker tint so the
       progress arcs stand out clearly. */
    .donut-card svg circle[stroke^='rgba(255,255,255'] {
        stroke: #e2e8f0 !important;
    }
    .donut-card svg circle[stroke^='rgba(0,229,255'] {
        stroke: #cbd5e1 !important;
    }

    /* ----- Status banner ----- */
    .status-banner {
        font-size: 11px !important;
        padding: 12px 16px !important;
    }
    .status-banner.ok {
        background: #ecfdf5 !important;
        color: #166534 !important;
        border: 1px solid #16a34a !important;
        box-shadow: none !important;
    }
    .status-banner.fail {
        background: #fef2f2 !important;
        color: #b91c1c !important;
        border: 1px solid #dc2626 !important;
        box-shadow: none !important;
    }
    .status-banner .secondary { color: #475569 !important; }

    /* ----- H-Bar (per-area pass-rate bars) ----- */
    .hbar-track {
        background: #f1f5f9 !important;
        border: 1px solid #cbd5e1 !important;
    }
    .hbar-track::before { display: none !important; }
    .hbar-fill { box-shadow: none !important; }
    .hbar-label { color: #1e293b !important; }
    .hbar-value { color: #475569 !important; }

    /* ----- Tables ----- */
    table { font-size: 10.5px !important; }
    thead { display: table-header-group; }
    tr { page-break-inside: avoid; break-inside: avoid; }
    th {
        background: #f1f5f9 !important;
        color: #0f172a !important;
        border-bottom: 1px solid #94a3b8 !important;
    }
    td {
        color: #1f2937 !important;
        border-bottom: 1px solid #e2e8f0 !important;
    }
    tbody tr:hover { background: transparent !important; }
    td code {
        background: #f1f5f9 !important;
        border: 1px solid #cbd5e1 !important;
        color: #0c4a6e !important;
    }

    /* ----- Pills ----- */
    .pill.pass {
        background: #ecfdf5 !important;
        color: #166534 !important;
        border-color: #16a34a !important;
    }
    .pill.fail {
        background: #fef2f2 !important;
        color: #b91c1c !important;
        border-color: #dc2626 !important;
    }
    .pill.skip {
        background: #fffbeb !important;
        color: #a16207 !important;
        border-color: #d97706 !important;
    }
    .pill::before { box-shadow: none !important; }

    /* ----- Details/summary collapsed-content: always show in print ----- */
    details { display: block !important; }
    details > summary { color: #006da6 !important; }
    details > *:not(summary) { display: block !important; }

    /* ----- Per-test grid: keep readable ----- */
    .grid-status thead th {
        position: static !important;     /* sticky doesn't work in print */
        box-shadow: none !important;
        background: #f1f5f9 !important;
        backdrop-filter: none !important;
    }

    /* ----- Forensic blocks (failure screenshots + logs) ----- */
    .forensic-block {
        border: 1px solid #dc2626 !important;
        background: #fef2f2 !important;
    }
    .forensic-block .test-id { color: #b91c1c !important; }
    .forensic-block .err-headline { color: #1f2937 !important; }
    .forensic-block .console-log {
        background: #f8fafc !important;
        border: 1px solid #cbd5e1 !important;
        color: #1f2937 !important;
    }
    .forensic-block img {
        border: 1px solid #cbd5e1 !important;
        max-height: 14cm;
        object-fit: contain;
    }

    /* ----- Per-view header banner (injected by JS at PDF time) ----- */
    .pdf-view-header {
        background: #0c4a6e;
        color: #ffffff !important;
        padding: 14px 18px;
        margin: 0 0 18px;
        border-radius: 3px;
        font-family: "JetBrains Mono", ui-monospace, monospace;
        page-break-after: avoid;
        break-after: avoid;
    }
    .pdf-view-header .pvh-label {
        font-size: 10px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        opacity: 0.85;
    }
    .pdf-view-header .pvh-title {
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.01em;
        margin: 2px 0 0;
    }
    .pdf-view-header .pvh-meta {
        font-size: 10px;
        margin-top: 6px;
        opacity: 0.85;
        letter-spacing: 0.04em;
    }

    /* ----- Cover page ----- */
    .pdf-cover {
        text-align: center;
        padding: 60px 20px 20px;
    }
    .pdf-cover .pc-eyebrow {
        color: #006da6;
        font-family: "JetBrains Mono", ui-monospace, monospace;
        font-size: 11px;
        letter-spacing: 0.22em;
        text-transform: uppercase;
    }
    .pdf-cover .pc-title {
        font-size: 32px;
        font-weight: 700;
        margin: 10px 0 8px;
        color: #0f172a;
    }
    .pdf-cover .pc-sub {
        color: #475569;
        font-size: 13px;
        margin-bottom: 36px;
    }
    .pdf-cover .pc-banner {
        display: inline-block;
        padding: 14px 28px;
        border-radius: 4px;
        font-size: 14px;
        font-weight: 700;
        letter-spacing: 0.06em;
        margin-bottom: 28px;
    }
    .pdf-cover .pc-banner.ok {
        background: #ecfdf5; color: #166534; border: 1px solid #16a34a;
    }
    .pdf-cover .pc-banner.fail {
        background: #fef2f2; color: #b91c1c; border: 1px solid #dc2626;
    }
    .pdf-cover .pc-stats {
        display: flex;
        justify-content: center;
        gap: 32px;
        margin: 24px 0 28px;
        flex-wrap: wrap;
    }
    .pdf-cover .pc-stat { text-align: center; }
    .pdf-cover .pc-stat .pc-num {
        font-size: 36px; font-weight: 700;
        font-family: "JetBrains Mono", ui-monospace, monospace;
    }
    .pdf-cover .pc-stat .pc-lab {
        font-size: 10px; color: #64748b;
        letter-spacing: 0.15em; text-transform: uppercase;
    }
    .pdf-cover .pc-stat.pass .pc-num { color: #15803d; }
    .pdf-cover .pc-stat.fail .pc-num { color: #b91c1c; }
    .pdf-cover .pc-stat.skip .pc-num { color: #a16207; }
    .pdf-cover .pc-stat.runs .pc-num { color: #0c4a6e; }
    .pdf-cover .pc-toc {
        margin: 36px auto 0;
        max-width: 480px;
        text-align: left;
        font-size: 12px;
        color: #334155;
        border-top: 1px solid #cbd5e1;
        padding-top: 16px;
    }
    .pdf-cover .pc-toc h3 {
        font-size: 10px;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: #475569;
        margin: 0 0 10px;
    }
    .pdf-cover .pc-toc ul { margin: 0; padding-left: 18px; }
    .pdf-cover .pc-toc li { margin: 3px 0; }
    .pdf-cover .pc-toc strong { color: #0f172a; }

    /* Suppress decorative scrollbars + animations */
    ::-webkit-scrollbar { display: none !important; }

    /* Keep h2 headers with the content that follows */
    h2 { page-break-after: avoid; break-after: avoid; }
    /* And keep cards together where possible */
    .card { page-break-inside: avoid; break-inside: avoid; }
}
"""


# ============================================================
# JS injected before rendering — adds cover page + per-view banners
# ============================================================

_INJECT_JS = r"""
() => {
    // --------------------------------------------------------------
    // 1. Per-view banner — clear "VIEW: AGGREGATE" / "VIEW: RUN N" so
    // someone flipping pages always knows what they're looking at.
    // --------------------------------------------------------------
    const views = document.querySelectorAll('.view-switcher > .view');
    const totalRuns = views.length - 1;   // exclude aggregate

    function buildBanner(viewKey, stats) {
        const isAgg = (viewKey === 'all');
        const label = isAgg ? 'AGGREGATE' : `RUN ${viewKey}`;
        const title = isAgg
            ? `All ${totalRuns} runs combined`
            : `Single-run snapshot — Run ${viewKey} of ${totalRuns}`;
        const meta = stats
            ? `${stats.passed} passed · ${stats.failed} failed · ${stats.skipped} skipped · ${stats.total} ${isAgg ? 'executions' : 'tests'}`
            : '';
        const wrap = document.createElement('div');
        wrap.className = 'pdf-view-header';
        wrap.innerHTML =
            `<div class="pvh-label">VIEW · ${label}</div>` +
            `<div class="pvh-title">${title}</div>` +
            (meta ? `<div class="pvh-meta">${meta}</div>` : '');
        return wrap;
    }

    // Pull the headline numbers out of each view's status banner
    function statsFor(viewEl) {
        const banner = viewEl.querySelector('.status-banner .secondary');
        if (!banner) return null;
        const txt = banner.textContent || '';
        const passM = txt.match(/(\d+)\s*pass/);
        const failM = txt.match(/(\d+)\s*fail/);
        const skipM = txt.match(/(\d+)\s*skip/);
        const p = passM ? parseInt(passM[1]) : 0;
        const f = failM ? parseInt(failM[1]) : 0;
        const s = skipM ? parseInt(skipM[1]) : 0;
        return { passed: p, failed: f, skipped: s, total: p + f + s };
    }

    let aggStats = null;
    views.forEach(v => {
        const key = v.dataset.view;
        const stats = statsFor(v);
        if (key === 'all') aggStats = stats;
        v.insertBefore(buildBanner(key, stats), v.firstChild);
    });

    // --------------------------------------------------------------
    // 2. Cover page at the very top of the PDF.
    //    Built from the aggregate view's headline numbers (the topbar
    //    meta is left to render inside the document body — we don't
    //    duplicate it on the cover).
    // --------------------------------------------------------------
    const titleTxt = document.title || 'Test Dashboard';

    const failed = aggStats ? aggStats.failed : 0;
    const passed = aggStats ? aggStats.passed : 0;
    const skipped = aggStats ? aggStats.skipped : 0;
    const total   = aggStats ? aggStats.total  : 0;
    const rate    = total ? Math.round(100 * passed / total) : 0;

    const ok = (failed === 0);
    const bannerCls = ok ? 'ok' : 'fail';
    const bannerTxt = ok
        ? `✓ ALL PASSING — ${rate}% pass rate`
        : `✗ ${failed} EXECUTION FAILURES — ${rate}% pass rate`;

    // Per-run mini-summary (read from the trend table)
    const trendRows = document.querySelectorAll('.card table tbody tr');
    const tocItems = [];
    trendRows.forEach(tr => {
        const tds = tr.querySelectorAll('td');
        if (tds.length >= 7) {
            const runIdx = (tds[0].textContent || '').trim();
            const dur    = (tds[2].textContent || '').trim();
            const p      = (tds[4].textContent || '').trim();
            const f      = (tds[5].textContent || '').trim();
            tocItems.push(
                `<li><strong>${runIdx}</strong> — ${dur}, ${p} passed, ${f} failed</li>`
            );
        }
    });

    const cover = document.createElement('div');
    cover.className = 'pdf-cover';
    cover.innerHTML = `
        <div class="pc-eyebrow">Zira QA · Test Pipeline Telemetry</div>
        <h1 class="pc-title">${titleTxt}</h1>

        <div class="pc-banner ${bannerCls}">${bannerTxt}</div>

        <div class="pc-stats">
            <div class="pc-stat pass">
                <div class="pc-num">${passed}</div>
                <div class="pc-lab">Passed</div>
            </div>
            <div class="pc-stat fail">
                <div class="pc-num">${failed}</div>
                <div class="pc-lab">Failed</div>
            </div>
            <div class="pc-stat skip">
                <div class="pc-num">${skipped}</div>
                <div class="pc-lab">Skipped</div>
            </div>
            <div class="pc-stat runs">
                <div class="pc-num">${totalRuns}</div>
                <div class="pc-lab">Runs</div>
            </div>
        </div>

        <div class="pc-toc">
            <h3>What's in this document</h3>
            <ul>
                <li><strong>Page 2 — Trend &amp; aggregate.</strong> Pass rate across all ${totalRuns} runs combined: which areas are flaky, which tests fail most, which are slowest.</li>
                ${tocItems.map(i => i).join('\n                ')}
            </ul>
        </div>
    `;
    document.body.insertBefore(cover, document.body.firstChild);
}
"""


def dashboard_html_to_pdf(html_path, pdf_path, format_="A4", landscape=False):
    """Render the dashboard HTML at `html_path` to a printable PDF.

    Returns the absolute output path on success. Raises if Chromium
    cannot launch or the input HTML is missing.
    """
    if not os.path.exists(html_path):
        raise FileNotFoundError(f"dashboard HTML not found: {html_path}")

    abs_html = os.path.abspath(html_path)
    file_url = "file:///" + abs_html.replace(os.sep, "/")

    out_dir = os.path.dirname(pdf_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with sync_playwright() as p:
        # PDF generation only works in Chromium (Playwright limitation).
        browser = p.chromium.launch(headless=True)
        try:
            context = browser.new_context()
            page = context.new_page()
            page.goto(file_url, wait_until="load")

            # Inject print stylesheet
            page.add_style_tag(content=_PRINT_CSS)

            # Inject DOM transforms — cover page + per-view banners
            page.evaluate(_INJECT_JS)

            # Force the print media-query so the @media print rules apply
            page.emulate_media(media="print")

            # Let radial-gradient backgrounds + SVG donut paint
            page.wait_for_timeout(400)

            page.pdf(
                path=pdf_path,
                format=format_,
                landscape=landscape,
                print_background=True,
                margin={"top": "12mm", "right": "10mm",
                        "bottom": "14mm", "left": "10mm"},
                prefer_css_page_size=False,
            )
        finally:
            browser.close()

    return os.path.abspath(pdf_path)
