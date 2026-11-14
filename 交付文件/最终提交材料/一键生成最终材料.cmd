@echo off
chcp 65001 >nul
powershell.exe -NoLogo -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_final.ps1"
if errorlevel 1 (
  echo Final materials build failed. See the error above.
  pause
  exit /b 1
)
echo Final report and poster generated successfully.
pause
