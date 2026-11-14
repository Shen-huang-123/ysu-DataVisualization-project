@echo off
chcp 65001 >nul
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0run_task4.ps1"
if errorlevel 1 (echo. & echo 任务四运行失败。 & pause & exit /b 1)
echo. & echo 任务四运行成功。 & pause
