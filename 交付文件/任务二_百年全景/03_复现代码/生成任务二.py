from pathlib import Path
import runpy

workspace = Path(__file__).resolve().parents[3]
scripts = workspace / "项目工作区" / "scripts"
for name in (
    "task2_highscore.py",
    "task2_upgrade.py",
    "task2_polish.py",
    "task2_causal_upgrade.py",
    "task2_audit.py",
):
    runpy.run_path(str(scripts / name), run_name="__main__")

print("任务二分析、图表、交互页和自动验收已完成。PDF与海报请使用根目录的一键运行任务二.cmd。")
