@echo off
chcp 65001 >nul
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_task2.ps1"
if errorlevel 1 (
  echo.
  echo Task 2 failed. See the error above.
  pause
  exit /b 1
)
echo.
echo Task 2 completed successfully.
pause
