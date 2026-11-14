$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:MPLBACKEND = "Agg"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$taskDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspace = [System.IO.Path]::GetFullPath((Join-Path $taskDir "..\.."))
$build = Join-Path $workspace "项目工作区\scripts\task4_highscore.py"
$upgrade = Join-Path $workspace "项目工作区\scripts\task4_fullscore_upgrade.py"
$audit = Join-Path $workspace "项目工作区\scripts\task4_audit.py"
try {
  $pythonExe = $null
  $pythonArgs = @()
  $bundledPython = Join-Path $workspace "项目工作区\qa_clean_env\Scripts\python.exe"
  $launcher = Get-Command py -ErrorAction SilentlyContinue
  if($launcher -and -not (Test-Path -LiteralPath $bundledPython)){
    try {
      & $launcher.Source -3 -c "import pandas,numpy,matplotlib,scipy,PIL,sklearn" 2>$null
      if($LASTEXITCODE -eq 0){$pythonExe=$launcher.Source; $pythonArgs=@("-3")}
    } catch { $pythonExe=$null }
  }
  if(-not $pythonExe){
    $pythonExe=$bundledPython
    if(-not (Test-Path -LiteralPath $pythonExe)){throw "Python依赖不完整。"}
    & $pythonExe -c "import pandas,numpy,matplotlib,scipy,PIL,sklearn"
    if($LASTEXITCODE -ne 0){throw "Python依赖不完整。"}
  }
  & $pythonExe @pythonArgs $build
  if($LASTEXITCODE -ne 0){throw "任务四生成失败。"}
  & $pythonExe @pythonArgs $upgrade
  if($LASTEXITCODE -ne 0){throw "任务四满分升级失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_component_ablation.py")
  if($LASTEXITCODE -ne 0){throw "任务四模型消融失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_rolling_validation.py")
  if($LASTEXITCODE -ne 0){throw "任务四滚动留出验证失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_exante_replay.py")
  if($LASTEXITCODE -ne 0){throw "赛前条件历史回放失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\deep_dive_three.py")
  if($LASTEXITCODE -ne 0){throw "历史逐队误差归因失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\sport_error_probe.py")
  if($LASTEXITCODE -ne 0){throw "历史逐运动误差检验失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_error_atlas.py")
  if($LASTEXITCODE -ne 0){throw "任务四逐队误差分析失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_method_page.py")
  if($LASTEXITCODE -ne 0){throw "预测方法网页生成失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\innovation_lab.py")
  if($LASTEXITCODE -ne 0){throw "创新交互页生成失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\frontends_refresh.py")
  if($LASTEXITCODE -ne 0){throw "统一前端生成失败。"}
  foreach($post in @("all_interfaces_photo_upgrade.py","unified_topbar.py","hero_motion.py","task2_visual_redesign.py","interactive_polish.py","task4_method_repair.py","task3_media_gallery.py","olympic_depth_upgrade.py")){
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\$post")
    if($LASTEXITCODE -ne 0){throw "交互界面样式重建失败：$post"}
  }
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\topic_evidence_matrix.py")
  if($LASTEXITCODE -ne 0){throw "结论稳定性地图生成失败。"}
  & $pythonExe @pythonArgs $audit
  if($LASTEXITCODE -ne 0){throw "任务四验收失败。"}
  & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_site_sync.py")
  if($LASTEXITCODE -ne 0){throw "任务四站点同步失败。"}
  Write-Host "任务四已重建并通过验收。" -ForegroundColor Green
  exit 0
} catch { Write-Host "任务四运行失败：$($_.Exception.Message)" -ForegroundColor Red; exit 1 }

