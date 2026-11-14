$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$env:MPLBACKEND = "Agg"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$OutputEncoding = [Console]::OutputEncoding

$taskDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspace = [System.IO.Path]::GetFullPath((Join-Path $taskDir "..\.."))
$script = Join-Path $workspace "项目工作区\scripts\task3_s2_highscore.py"
$upgradeScript = Join-Path $workspace "项目工作区\scripts\task3_s2_upgrade.py"
$storyScript = Join-Path $workspace "项目工作区\scripts\task3_story_upgrade.py"
$s3Script = Join-Path $workspace "项目工作区\scripts\task3_s3_dynasties.py"
$s3Experience = Join-Path $workspace "项目工作区\scripts\task3_s3_experience.py"
$s1Experience = Join-Path $workspace "项目工作区\scripts\task3_s1_experience.py"
$s3Pdf = Join-Path $workspace "项目工作区\scripts\task3_s3_pdf.py"
$portalScript = Join-Path $workspace "项目工作区\scripts\task3_portal.py"
$pdfScript = Join-Path $workspace "项目工作区\scripts\task3_s2_pdf.py"
$auditScript = Join-Path $workspace "项目工作区\scripts\task3_audit.py"
$depthScript = Join-Path $workspace "项目工作区\scripts\task3_depth_extension.py"

try {
    $pythonExe = $null
    $pythonArgs = @()
    $bundledPython = Join-Path $workspace "项目工作区\qa_clean_env\Scripts\python.exe"
    $launcher = Get-Command py -ErrorAction SilentlyContinue
    if($launcher -and -not (Test-Path -LiteralPath $bundledPython)){
        try {
            & $launcher.Source -3 -c "import pandas,numpy,matplotlib,scipy" 2>$null
            if($LASTEXITCODE -eq 0){$pythonExe=$launcher.Source; $pythonArgs=@("-3")}
        } catch { $pythonExe=$null }
    }
    if(-not $pythonExe){
        $pythonExe=$bundledPython
        if(-not (Test-Path -LiteralPath $pythonExe)){throw "Python dependencies are incomplete."}
        & $pythonExe -c "import pandas,numpy,matplotlib,scipy"
        if($LASTEXITCODE -ne 0){throw "Python dependencies are incomplete."}
    }
    & $pythonExe @pythonArgs $script
    if ($LASTEXITCODE -ne 0) { throw "S2 analysis failed." }
    & $pythonExe @pythonArgs $upgradeScript
    if ($LASTEXITCODE -ne 0) { throw "S2 three-lens upgrade failed." }
    & $pythonExe @pythonArgs $storyScript
    if ($LASTEXITCODE -ne 0) { throw "S2 narrative story upgrade failed." }
    & $pythonExe @pythonArgs $s3Script
    if ($LASTEXITCODE -ne 0) { throw "S3 dynasty analysis failed." }
    & $pythonExe @pythonArgs $s3Experience
    if ($LASTEXITCODE -ne 0) { throw "S3 timeline failed." }
    & $pythonExe @pythonArgs $s1Experience
    if ($LASTEXITCODE -ne 0) { throw "S1 interactive report failed." }
    & $pythonExe @pythonArgs $portalScript
    if ($LASTEXITCODE -ne 0) { throw "Task 3 Chinese portal failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\innovation_lab.py")
    if ($LASTEXITCODE -ne 0) { throw "Innovation labs failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\frontends_refresh.py")
    if ($LASTEXITCODE -ne 0) { throw "Frontend refresh failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_ten_topics.py")
    if ($LASTEXITCODE -ne 0) { throw "Additional Task 3 topics failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_ten_portal.py")
    if ($LASTEXITCODE -ne 0) { throw "Ten-topic portal failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_design_upgrade.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 design upgrade failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_premium_portal.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 photo portal failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_photo_upgrade.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\all_interfaces_photo_upgrade.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\unified_topbar.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\hero_motion.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task2_visual_redesign.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\interactive_polish.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task4_method_repair.py")
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_media_gallery.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 photo scenes failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\olympic_depth_upgrade.py")
    if ($LASTEXITCODE -ne 0) { throw "Olympic 3D interface upgrade failed." }

    $pdfPython = $pythonExe
    $pdfPrefix = $pythonArgs
    $systemPdfReady = $false
    try {
        & $pdfPython @pdfPrefix -c "import reportlab,PIL" 2>$null
        $systemPdfReady = ($LASTEXITCODE -eq 0)
    } catch { $systemPdfReady = $false }
    if (-not $systemPdfReady) {
        $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
        if (-not (Test-Path -LiteralPath $bundled)) { throw "PDF依赖缺失。请在项目工作区运行：py -3 -m pip install -r requirements.txt" }
        & $bundled -c "import reportlab,PIL" 2>$null
        if ($LASTEXITCODE -ne 0) { throw "PDF依赖缺失。请在项目工作区运行：py -3 -m pip install -r requirements.txt" }
        $pdfPython = $bundled
        $pdfPrefix = @()
    }
    & $pdfPython @pdfPrefix $pdfScript
    if ($LASTEXITCODE -ne 0) { throw "S2 PDF generation failed." }
    & $pdfPython @pdfPrefix $s3Pdf
    if ($LASTEXITCODE -ne 0) { throw "S3 PDF generation failed." }

    & $pythonExe @pythonArgs $auditScript
    if ($LASTEXITCODE -ne 0) { throw "S2 automatic audit failed." }
    & $pythonExe @pythonArgs $depthScript
    if ($LASTEXITCODE -ne 0) { throw "Ten-topic depth cross-check failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\task3_evidence_upgrade.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 evidence upgrade failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\dynasty_fixed_panel.py")
    if ($LASTEXITCODE -ne 0) { throw "Fixed-event dynasty validation failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\conclusion_spec_grid.py")
    if ($LASTEXITCODE -ne 0) { throw "Conclusion specification grid failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\topic_evidence_matrix.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 conclusion stability map failed." }
    & $pythonExe @pythonArgs (Join-Path $workspace "项目工作区\scripts\deep_dive_three.py")
    if ($LASTEXITCODE -ne 0) { throw "Task 3 follow-up analyses failed." }

    $expected = @(
        (Join-Path $taskDir "S2_口径的魔力\01_报告与说明\S2_口径的魔力_高分版.md"),
        (Join-Path $taskDir "S2_口径的魔力\02_数据表\S2_2024双口径完整排名.csv"),
        (Join-Path $taskDir "S2_口径的魔力\04_核心图表\S2_双口径排名重排.png"),
        (Join-Path $taskDir "S2_口径的魔力\04_核心图表\S2_多人项目与金牌行膨胀.png"),
        (Join-Path $taskDir "S2_口径的魔力\04_核心图表\00_S2专题英雄图.png"),
        (Join-Path $taskDir "S2_口径的魔力\04_核心图表\S2_三口径排名路径.png"),
        (Join-Path $taskDir "S2_口径的魔力\04_核心图表\S2_跨届机制稳定性.png"),
        (Join-Path $taskDir "S2_口径的魔力\06_交互榜\index.html"),
        (Join-Path $taskDir "S2_口径的魔力\06_滚动叙事专题\index.html"),
        (Join-Path $taskDir "S2_口径的魔力\02_数据表\S2_历史官方核验摘要.csv"),
        (Join-Path $taskDir "S3_冠军的保质期\01_报告与说明\S3_冠军的保质期_分析报告.md"),
        (Join-Path $taskDir "S3_冠军的保质期\04_核心图表\S3_最长冠军王朝.png"),
        (Join-Path $taskDir "S3_冠军的保质期\05_质量验收\S3自动验收报告.json"),
        (Join-Path $taskDir "S3_冠军的保质期\06_冠军王朝时间轴\index.html"),
        (Join-Path $taskDir "S1_东道主效应\index.html"),
        (Join-Path $taskDir "S3_冠军的保质期\01_报告与说明\S3_冠军的保质期_正式报告.pdf"),
        (Join-Path $taskDir "统一中文入口\index.html"),
        (Join-Path $taskDir "媒体\图片来源与许可.md"),
        (Join-Path $taskDir "媒体\host.jpg"),
        (Join-Path $taskDir "媒体\sports.jpg"),
        (Join-Path $taskDir "十专题深度核验.html"),
        (Join-Path $taskDir "十专题深度核验.json"),
        (Join-Path $taskDir "S2_口径的魔力\01_报告与说明\S2_口径的魔力_正式报告.pdf"),
        (Join-Path $taskDir "S2_口径的魔力\05_质量验收\S2自动验收报告.json")
    )
    $missing = @($expected | Where-Object { -not (Test-Path -LiteralPath $_) })
    if ($missing.Count -gt 0) { throw "Expected outputs are missing: $($missing -join ', ')" }
    Write-Host "Task 3 S2 outputs were rebuilt and verified." -ForegroundColor Green
    exit 0
} catch {
    Write-Host "Task 3 build failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}

