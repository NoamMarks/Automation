@echo off
REM ============================================================
REM  Build a FULLY self-contained ZiraQARunner.exe.
REM
REM  Bundles into a single .exe (~310 MB):
REM    - Python interpreter + stdlib (PyInstaller)
REM    - All pip dependencies (pytest, playwright, Pillow, ...)
REM    - Test source (tests\, pages\, utils\, pytest.ini)
REM    - Chromium browser (chromium-XXXX + chromium_headless_shell-XXXX
REM      + ffmpeg + winldd) staged into pw-browsers\ then bundled.
REM      The headless_shell variant is needed because Playwright 1.55
REM      uses it when headless=True (the PDF dashboard generator).
REM
REM  Runtime config + credentials are NOT bundled - first launch
REM  shows a wizard that collects them and saves to
REM    %APPDATA%\ZiraQA\config.json
REM
REM  Prereqs on the BUILD machine (run once):
REM    pip install -r requirements.txt
REM    pip install pyinstaller
REM
REM  Output:
REM    dist\ZiraQARunner.exe   (copy this anywhere, double-click)
REM ============================================================

setlocal

REM ---------- Step 1: ensure pyinstaller is available ----------
REM Always invoke as `python -m PyInstaller` so the user doesn't need
REM the Scripts\ folder on PATH (user-site pip installs land there but
REM it's rarely on PATH by default on Windows).
python -c "import PyInstaller" >nul 2>nul
if errorlevel 1 (
    echo [build] PyInstaller not found. Installing...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo [build] FAILED to install pyinstaller.
        exit /b 1
    )
)

REM ---------- Step 2: stage Chromium variants into pw-browsers\ ----------
REM PLAYWRIGHT_BROWSERS_PATH redirects `playwright install` so the
REM browser binaries land in a build-local folder we can add-data.
REM Always run - `playwright install` is idempotent (only downloads
REM what's missing). Needed to top up any variants someone deleted
REM between builds, including the headless_shell binary required by
REM Playwright 1.55 when headless=True (the PDF dashboard renderer).
set "PW_LOCAL=%CD%\pw-browsers"
set "PLAYWRIGHT_BROWSERS_PATH=%PW_LOCAL%"
echo [build] Ensuring Chromium variants are staged in %PW_LOCAL% ...
python -m playwright install chromium
if errorlevel 1 (
    echo [build] playwright install failed.
    exit /b 1
)

REM ---------- Step 3: kill any running launcher so the .exe isn't locked ----------
taskkill /F /IM ZiraQARunner.exe >nul 2>nul

REM ---------- Step 4: bundle ----------
echo [build] Bundling into dist\ZiraQARunner.exe ...

python -m PyInstaller ^
    --onefile ^
    --noconsole ^
    --name ZiraQARunner ^
    --icon NONE ^
    --clean ^
    --noconfirm ^
    --add-data "tests;tests" ^
    --add-data "pages;pages" ^
    --add-data "utils;utils" ^
    --add-data "pytest.ini;." ^
    --add-data "pw-browsers;pw-browsers" ^
    --collect-all playwright ^
    --collect-all pytest_html ^
    --collect-all pytest_playwright ^
    --collect-all pytest_base_url ^
    --collect-all pytest_metadata ^
    --collect-all pytest_rerunfailures ^
    --collect-all xdist ^
    --copy-metadata pytest ^
    --copy-metadata pytest-html ^
    --copy-metadata pytest-playwright ^
    --copy-metadata pytest-base-url ^
    --copy-metadata pytest-metadata ^
    --copy-metadata pytest-rerunfailures ^
    --copy-metadata pytest-xdist ^
    --hidden-import pytest_html ^
    --hidden-import pytest_playwright ^
    --hidden-import pytest_base_url ^
    --hidden-import pytest_metadata ^
    --hidden-import pytest_rerunfailures ^
    --hidden-import xdist ^
    --hidden-import dotenv ^
    --hidden-import PIL ^
    run_gui.py

if errorlevel 1 (
    echo [build] PyInstaller failed.
    exit /b 1
)

echo.
echo [build] Done. Executable at: %CD%\dist\ZiraQARunner.exe
for %%I in ("dist\ZiraQARunner.exe") do echo [build] Size: %%~zI bytes
echo [build] Copy ZiraQARunner.exe anywhere and double-click. No other files needed.
echo.

endlocal
