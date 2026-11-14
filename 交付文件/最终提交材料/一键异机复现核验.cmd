@echo off
setlocal
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "异机复现核验.py"
) else (
  python "异机复现核验.py"
)
if errorlevel 1 (
  echo 复现失败；请查看上方错误及异机复现结果.json。
) else (
  echo 复现成功；结果见异机复现结果.json。
)
pause
