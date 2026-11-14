@echo off
setlocal
cd /d "%~dp0"
set "PYTHONIOENCODING=utf-8"
set "RUNNER="

if exist "%~dp0runtime\python.exe" "%~dp0runtime\python.exe" -c "import pandas" >nul 2>nul && set "RUNNER=%~dp0runtime\python.exe"
if not defined RUNNER py -3 -c "import pandas" >nul 2>nul && set "RUNNER=py -3"
if not defined RUNNER python -c "import pandas" >nul 2>nul && set "RUNNER=python"

if not defined RUNNER (
  echo [ERROR] No Python environment with pandas was found.
  echo Add a portable runtime at runtime\python.exe or install Python 3.10+ and pandas.
  pause
  exit /b 1
)

echo [1/1] Running Task 1 audit and normalization...
for /d %%D in ("%~dp003_*") do set "CODEDIR=%%D"
%RUNNER% "%CODEDIR%\run_task1.py"
if errorlevel 1 (
  echo [ERROR] Task 1 failed. See 99_output\run_log.txt or the numbered output folder.
  pause
  exit /b 3
)
%RUNNER% "%~dp0..\..\项目工作区\scripts\frontends_refresh.py"
if errorlevel 1 (
  echo [ERROR] Frontend refresh failed.
  pause
  exit /b 4
)
%RUNNER% "%~dp0..\..\项目工作区\scripts\unified_topbar.py"
if errorlevel 1 (
  echo [ERROR] Theme and navigation rebuild failed.
  pause
  exit /b 5
)
%RUNNER% "%~dp0..\..\项目工作区\scripts\olympic_depth_upgrade.py"
if errorlevel 1 (
  echo [ERROR] Olympic interface upgrade failed.
  pause
  exit /b 6
)

echo [DONE] Outputs and the run log are ready in the numbered folders.
pause
exit /b 0
