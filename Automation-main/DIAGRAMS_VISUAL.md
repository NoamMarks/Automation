# 📐 Visual Diagrams — Better Class & Function Maps

Two complementary views — same data, different angles:

1. **Layered Flowchart** — *structure*: what calls what, grouped by purpose, color-coded
2. **Sequence Diagrams** — *timeline*: what happens first, what next, who talks to whom

Paste either Mermaid block into draw.io via `Arrange → Insert → Advanced → Mermaid`.

---

## 1️⃣ Layered Flowchart (recommended for big-picture)

A single page showing all 5 layers with **methods visible on the key classes**,
**labeled arrows**, and **color-coding by layer**. Far easier on the eyes than
the dense class diagram because related things are grouped into colored
boxes and only the most important methods are shown.

```mermaid
flowchart TB
    classDef entry fill:#1e3a8a,stroke:#60a5fa,color:#fff,stroke-width:2px
    classDef fixture fill:#7c2d12,stroke:#fb923c,color:#fff,stroke-width:2px
    classDef test fill:#14532d,stroke:#4ade80,color:#fff,stroke-width:2px
    classDef pom fill:#581c87,stroke:#c084fc,color:#fff,stroke-width:2px
    classDef report fill:#0c4a6e,stroke:#38bdf8,color:#fff,stroke-width:2px
    classDef output fill:#27272a,stroke:#a1a1aa,color:#fff,stroke-dasharray:5

    USER([🧑 user types:<br>python tests/run_multiple.py]):::entry

    subgraph EXEC["🚀 L1 — EXECUTOR"]
        direction TB
        MAIN["main()<br>• loops N times<br>• calls 4 report gens<br>• sends email"]
        RO["_run_once(idx)<br>• runs pytest in subprocess<br>• returns paths + timing"]
        MAIN --> RO
    end
    MAIN:::entry
    RO:::entry

    subgraph FIX["🔧 L2 — FIXTURES & HOOKS (conftest.py)"]
        direction TB
        AUTH["_auth_state_path<br><i>session-scoped</i><br>━━━━━━━━<br>1 real B2C login<br>Saves storage_state.json"]
        PAGE["page<br><i>class-scoped</i><br>━━━━━━━━<br>Browser context<br>w/ preloaded auth"]
        HOOK["pytest_runtest_makereport<br><i>hook</i><br>━━━━━━━━<br>Stashes rep_xxx<br>on test item"]
        CAP["_capture_on_failure<br><i>autouse</i><br>━━━━━━━━<br>screenshot + log<br>on test failure"]
    end
    AUTH:::fixture
    PAGE:::fixture
    HOOK:::fixture
    CAP:::fixture

    subgraph TST["🧪 L3 — TEST CLASSES (16 files)"]
        direction TB
        TC1["TestPortalClient<br><i>17 tests · CRUD basics</i>"]
        TC2["TestKnownRegressions<br><i>5 bug regressions</i>"]
        TC3["TestDomainLinkCascade<br><i>+ 3 more cascade classes</i>"]
        TCN["...12 more test classes..."]
    end
    TC1:::test
    TC2:::test
    TC3:::test
    TCN:::test

    subgraph POM["📄 L4 — PAGE OBJECT MODEL (pages/)"]
        direction TB
        LP["LoginPage<br>━━━━━━━━<br>+ navigate()<br>+ fill_credentials()<br>+ click_login()<br>+ wait_for_dashboard() ↻3"]
        NP["NavigationPage<br>━━━━━━━━<br>+ go_to_links()<br>+ go_to_environments()<br>+ go_to_messages()<br>+ go_to_tags()<br>+ go_to_content_worlds()"]
        DP["DomainsPage · TagsPage<br>EnvironmentsPage · LinksPage<br>MessagesPage<br>━━━━━━━━<br>+ create_X()<br>+ click_save_and_confirm()<br>+ click_delete_on_row()<br>+ verify_X_visible()"]
    end
    LP:::pom
    NP:::pom
    DP:::pom

    subgraph RPT["📊 L5 — REPORT GENERATORS (utils/)"]
        direction TB
        GSS["generate_simple_summary<br>━━━━━━━━<br>FEATURE_AREAS dict<br>_humanize_error()<br>_humanize_test_name()"]
        GHD["generate_html_dashboard<br>━━━━━━━━<br>_svg_donut()<br>_collect_test_docstrings()<br>_build_view_html()<br>_render_tab_bar()"]
        GMR["generate_master_report<br>━━━━━━━━<br>_build_failure_analysis()<br>_find_artifacts_for_run()"]
        GWA["generate_whatsapp_summary<br>━━━━━━━━<br>HEBREW_AREA_NAMES<br>_build_status_line()"]
        SEM["send_run_email<br>━━━━━━━━<br>_aggregate(runs)<br>_build_html_body()"]
    end
    GSS:::report
    GHD:::report
    GMR:::report
    GWA:::report
    SEM:::report

    OUT1[/Test_Summary.md/]:::output
    OUT2[/Test_Dashboard.html/]:::output
    OUT3[/Master_Report.md/]:::output
    OUT4[/WhatsApp.txt/]:::output
    INBOX[/📧 inbox/]:::output

    USER ==> MAIN
    RO -.spawns pytest.-> AUTH
    AUTH -.uses.-> LP
    PAGE -.depends on.-> AUTH
    TC1 ==> PAGE
    TC2 ==> PAGE
    TC3 ==> PAGE
    TCN ==> PAGE
    HOOK -.feeds.-> CAP

    TC1 ==> LP
    TC1 ==> NP
    TC1 ==> DP
    TC2 ==> LP
    TC2 ==> DP
    TC3 ==> DP
    TCN ==> DP

    MAIN ==> GSS
    MAIN ==> GHD
    MAIN ==> GMR
    MAIN ==> GWA
    MAIN ==> SEM
    GHD -.imports<br>FEATURE_AREAS.-> GSS

    GSS ==> OUT1
    GHD ==> OUT2
    GMR ==> OUT3
    GWA ==> OUT4
    OUT1 -.attach.-> SEM
    OUT2 -.attach.-> SEM
    SEM ==> INBOX
```

### Reading guide

| Arrow style | Meaning |
|---|---|
| `==>` (thick solid) | "Uses" / "Calls" — strong dependency |
| `-.->` (dotted) | "Configures" / "Imports" / "Triggers" — looser link |
| `[/file/]` (parallelogram) | A file output, not a class |
| `()` round | The entry-point trigger (you) |
| Subgraph color | The layer: blue/orange/green/purple/cyan |

---

## 2️⃣ Sequence Diagram — "What happens during one test"

**Better than a class diagram if you want to understand the runtime flow.**
Reads top-to-bottom like a story. Each vertical line is one object; arrows
between them are messages over time.

```mermaid
sequenceDiagram
    autonumber
    actor User as 🧑 You
    participant Exec as 🚀 run_multiple
    participant PT as pytest
    participant CF as 🔧 conftest
    participant LP as 🔑 LoginPage
    participant POM as 📄 PageObjects
    participant T as 🧪 TestClass

    User->>Exec: python run_multiple.py
    Exec->>PT: subprocess pytest

    rect rgb(40, 60, 90)
        Note over PT,CF: ONCE PER SESSION
        PT->>CF: _auth_state_path()
        CF->>LP: navigate + fill + click + wait
        LP-->>CF: ✓ logged in
        CF-->>PT: storage_state.json
    end

    loop For each TestClass
        rect rgb(60, 40, 30)
            Note over PT,CF: PER CLASS
            PT->>CF: page fixture
            CF-->>PT: browser context w/ auth
        end

        loop For each test method
            PT->>T: test_XX()
            T->>POM: action e.g. create_link
            POM-->>T: ✓ result
            T->>PT: assert
            alt 😱 Test fails
                PT->>CF: _capture_on_failure
                CF->>CF: screenshot + dump logs
            end
        end
    end

    rect rgb(20, 60, 50)
        Note over Exec: AFTER ALL RUNS
        Exec->>Exec: generate 4 reports
        Exec->>Exec: send email
    end
```

---

## 3️⃣ Sequence Diagram — "How a report gets built"

Shows the post-run pipeline: from raw JUnit XMLs to the email landing in
your inbox.

```mermaid
sequenceDiagram
    autonumber
    participant Exec as 🚀 run_multiple.main
    participant JUNIT as 📄 run_N_junit.xml
    participant ZTL as 🚨 zero_touch_logs
    participant GSS as 📝 simple_summary
    participant GHD as 📊 html_dashboard
    participant GMR as 🔬 master_report
    participant GWA as 💬 whatsapp_summary
    participant SEM as ✉️ send_email
    participant INBOX as 📧 inbox

    Note over Exec: All N pytest runs finished

    Exec->>GMR: generate_master_report(runs)
    GMR->>JUNIT: read all N
    GMR->>ZTL: match screenshots+logs by time window
    GMR-->>Exec: Master_Run_Report_<TS>.md

    Exec->>GSS: generate_simple_summary(runs)
    GSS->>JUNIT: read all N
    Note right of GSS: humanize errors,<br>look up FEATURE_AREAS
    GSS-->>Exec: Test_Summary_<TS>.md

    Exec->>GHD: generate_html_dashboard(runs)
    GHD->>JUNIT: read all N
    GHD->>ZTL: base64-embed screenshots
    Note right of GHD: SVG donut, tooltips,<br>tab switcher JS
    GHD-->>Exec: Test_Dashboard_<TS>.html

    Exec->>GWA: generate_whatsapp_summary(runs)
    GWA->>JUNIT: read all N
    Note right of GWA: pick Hebrew status<br>line by failure pattern
    GWA-->>Exec: WhatsApp_Summary_<TS>.txt

    Exec->>SEM: send_run_email(runs, summary, dashboard)
    SEM->>SEM: build subject + body
    SEM->>INBOX: SMTP STARTTLS + attachments
```

---

## 4️⃣ How to paste into draw.io

1. Open https://app.diagrams.net (or the desktop app)
2. Create a blank diagram
3. Go to: `Arrange` → `Insert` → `Advanced` → `Mermaid`
4. Paste any of the three Mermaid blocks above
5. Click **Insert** — draw.io renders it as editable shapes
6. Drag/resize/recolor as needed
7. Export: `File` → `Export as` → PNG / SVG / PDF

## 5️⃣ Tips for making diagrams more readable

| Problem | Fix |
|---|---|
| Too many lines crossing | Group related classes into subgraphs (we do this) |
| Hard to tell "uses" from "imports" | Use different arrow styles (we use `==>` vs `-.->`) |
| Can't see the flow | Set `direction TB` or `LR` to force top-to-bottom or left-right |
| Boxes look the same | Color-code by layer with `classDef` (we do this) |
| Too many methods | Show only the 3–4 most important per class — link to `CALL_GRAPH.md` for the rest |
| Static structure unclear | Use a **sequence diagram** instead — it shows time order |

## 6️⃣ Which diagram for which purpose?

| You want to show... | Use this |
|---|---|
| **The whole codebase at a glance** | Layered Flowchart (#1) |
| **How a test runs step-by-step** | Sequence Diagram (#2) |
| **How reports get built and emailed** | Sequence Diagram (#3) |
| **Just the classes & their methods** (no runtime) | Class Diagram (the original #2 from before) |
| **One specific feature's flow** | Smaller sequence diagram zoomed on that flow |

## 7️⃣ Pro tip — keep diagrams in sync with code

The diagrams here are **derived from `CALL_GRAPH.md`** — if you change
something in the code:

1. Update `CALL_GRAPH.md` first (it's the source of truth)
2. Then update the relevant Mermaid block here
3. Re-paste into draw.io if you have a live diagram

That way the docs stay aligned with reality.
