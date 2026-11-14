$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
[Console]::OutputEncoding = New-Object System.Text.UTF8Encoding($false)
$OutputEncoding = [Console]::OutputEncoding

$taskDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$workspace = [System.IO.Path]::GetFullPath((Join-Path $taskDir "..\.."))
$scripts = Join-Path $workspace "项目工作区\scripts"
$standardPython = $null
$pdfPython = $null

function Find-WorkingPython {
    $candidates = @(
        @{ Command = "py"; Prefix = @("-3") },
        @{ Command = "python"; Prefix = @() },
        @{ Command = "python3"; Prefix = @() }
    )
    foreach ($candidate in $candidates) {
        try {
            $cmd = Get-Command $candidate.Command -ErrorAction Stop
            & $cmd.Source @($candidate.Prefix) -c "import pandas,numpy,matplotlib" 2>$null
            if ($LASTEXITCODE -eq 0) { return $candidate }
        } catch { }
    }
    throw "No Python environment with pandas, numpy and matplotlib was found."
}

function Find-PdfPython {
    foreach ($candidate in @(@{ Command = "py"; Prefix = @("-3") }, @{ Command = "python"; Prefix = @() })) {
        try {
            $cmd = Get-Command $candidate.Command -ErrorAction Stop
            & $cmd.Source @($candidate.Prefix) -c "import reportlab,PIL" 2>$null
            if ($LASTEXITCODE -eq 0) { return @{ Command = $cmd.Source; Prefix = @($candidate.Prefix) } }
        } catch { }
    }
    $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
    if (Test-Path -LiteralPath $bundled) {
        & $bundled -c "import reportlab,PIL" 2>$null
        if ($LASTEXITCODE -eq 0) { return @{ Command = $bundled; Prefix = @() } }
    }
    throw "PDF依赖缺失。请在项目工作区运行：py -3 -m pip install -r requirements.txt"
}

function Run-StandardPython([string]$script) {
    Write-Host "Running $([System.IO.Path]::GetFileName($script)) ..." -ForegroundColor Cyan
    $cmd = Get-Command $standardPython.Command -ErrorAction Stop
    & $cmd.Source @($standardPython.Prefix) $script
    if ($LASTEXITCODE -ne 0) { throw "Script failed: $script" }
}

try {
    $standardPython = Find-WorkingPython
    $pdfPython = Find-PdfPython

    Run-StandardPython (Join-Path $scripts "task2_highscore.py")
    Run-StandardPython (Join-Path $scripts "task2_upgrade.py")
    Run-StandardPython (Join-Path $scripts "task2_polish.py")
    Run-StandardPython (Join-Path $scripts "task2_causal_upgrade.py")
    Run-StandardPython (Join-Path $scripts "frontends_refresh.py")
    Run-StandardPython (Join-Path $scripts "all_interfaces_photo_upgrade.py")
    Run-StandardPython (Join-Path $scripts "unified_topbar.py")
    Run-StandardPython (Join-Path $scripts "hero_motion.py")
    Run-StandardPython (Join-Path $scripts "task2_visual_redesign.py")
    Run-StandardPython (Join-Path $scripts "interactive_polish.py")
    Run-StandardPython (Join-Path $scripts "task4_method_repair.py")
    Run-StandardPython (Join-Path $scripts "task3_media_gallery.py")
    Run-StandardPython (Join-Path $scripts "olympic_depth_upgrade.py")

    Write-Host "Generating the formal PDF report and A2 poster ..." -ForegroundColor Cyan
    & $pdfPython.Command @($pdfPython.Prefix) (Join-Path $scripts "task2_pdf.py")
    if ($LASTEXITCODE -ne 0) { throw "PDF generation failed." }

    Run-StandardPython (Join-Path $scripts "task2_audit.py")
    Run-StandardPython (Join-Path $scripts "concentration_stress_test.py")
    Run-StandardPython (Join-Path $scripts "gender_gap_decomposition.py")

    $expected = @(
        (Join-Path $taskDir "01_报告与说明\任务二_百年奥运全景_正式报告.pdf"),
        (Join-Path $taskDir "01_报告与说明\任务二_百年奥运全景_A2海报.pdf"),
        (Join-Path $taskDir "04_核心图表\B_主场效应准实验检验.png"),
        (Join-Path $taskDir "04_核心图表\B_20届合成对照与稳健性.png"),
        (Join-Path $taskDir "05_交互总览\index.html")
        (Join-Path $taskDir "07_结论压力测试\结论压力测试.html")
        (Join-Path $taskDir "08_女性结构分解\女性结构分解.html")
        (Join-Path $taskDir "06_质量验收\任务二自动验收报告.json")
    )
    $missing = @($expected | Where-Object { -not (Test-Path -LiteralPath $_) })
    if ($missing.Count -gt 0) { throw "Expected outputs are missing: $($missing -join ', ')" }

    Write-Host "All Task 2 outputs were rebuilt and verified." -ForegroundColor Green
    exit 0
} catch {
    Write-Host "Task 2 build failed: $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
