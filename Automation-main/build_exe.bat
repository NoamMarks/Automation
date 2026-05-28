@echo off
REM ============================================================
REM  Build ZiraQARunner.exe from run_gui.py via PyInstaller.
REM
REM  Run this once: pip install pyinstaller
REM  Then:          build_exe.bat
REM
REM  Output: dist\ZiraQARunner.exe (single file, ~30-40 MB)
REM
REM  IMPORTANT — the .exe is a LAUNCHER, not a self-contained
REM  test runner. It needs to sit next to the project files at
REM  runtime because pytest/Playwright load test modules from
REM  disk and Playwright browsers come from
REM  %USERPROFILE%\AppData\Local\ms-playwright\.
REM
REM  Workflow on a fresh machine:
REM    1. Install Python 3.13 + run `pip install -r requirements.txt`
REM       and `playwright install chromium` ONCE.
REM    2. Copy the whole Automation-main\ folder to the machine.
REM    3. Drop ZiraQARunner.exe into the Automation-main\ folder.
REM    4. Double-click to launch.
REM ============================================================

setlocal

where pyinstaller >nul 2>nul
if errorlevel 1 (
    echo [build] PyInstaller not found. Installing it now...
    python -m pip install pyinstaller
    if errorlevel 1 (
        echo [build] FAILED to install pyinstaller.
        exit /b 1
    )
)

echo [build] Bundling run_gui.py into dist\ZiraQARunner.exe ...

pyinstaller ^
    --onefile ^
    --noconsole ^
    --name ZiraQARunner ^
    --icon NONE ^
    --clean ^
    run_gui.py

if errorlevel 1 (
    echo [build] PyInstaller failed.
    exit /b 1
)

echo.
echo [build] Done. Executable at:  dist\ZiraQARunner.exe
echo [build] Copy it next to tests\, pages\, utils\ and double-click.
echo.

endlocal