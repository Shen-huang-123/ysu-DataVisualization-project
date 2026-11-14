$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"
$base = Split-Path -Parent $MyInvocation.MyCommand.Path
$root = [System.IO.Path]::GetFullPath((Join-Path $base "..\.."))
$script = Join-Path $root "项目工作区\scripts\final_submission.py"
try {
    $py = (Get-Command py -ErrorAction Stop).Source
    $prefix = @("-3")
    $ready = $false
    try {
        & $py @prefix -c "import reportlab,PIL" 2>$null
        $ready = ($LASTEXITCODE -eq 0)
    } catch { $ready = $false }
    if (-not $ready) {
        $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
        if (-not (Test-Path -LiteralPath $bundled)) { throw "请先在项目工作区运行 py -3 -m pip install -r requirements.txt" }
        $py = $bundled
        $prefix = @()
    }
    & $py @prefix $script
    if ($LASTEXITCODE -ne 0) { throw "最终材料生成失败。" }
    $report = Join-Path $base "报告\百年圣火_正式报告.pdf"
    $poster = Join-Path $base "海报\百年圣火_A2海报_正式版.pdf"
    if (-not (Test-Path -LiteralPath $report) -or -not (Test-Path -LiteralPath $poster)) { throw "输出文件缺失。" }
    Write-Host "正式报告与A2海报已重建。" -ForegroundColor Green
    exit 0
} catch {
    Write-Host "生成失败：$($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
