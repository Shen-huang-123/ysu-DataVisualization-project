# 项目工作区

这里保存完整代码、中间结果和本地依赖。评委先打开上一级 `交付文件/作品总入口/index.html`。

- scripts：审计、清洗、分析、报告、海报和看板生成代码。
- outputs：全部中间数据、图表和质量检查结果。
- docs：分析正文与过程说明。
- deliverables：脚本生成的工作版成品。
- .runtime：本机依赖，不随提交包分发。

输入文件位于上一级 `资料文件/原始资料`。推荐使用 Python 3.11—3.13，在本目录运行 `py -3 -m pip install -r requirements.txt` 安装依赖。随后按任务一、二、三、四目录的一键运行入口依次重建交付物。若不在 Windows 上运行，可查看各任务 `run_task*.ps1` 中的脚本顺序逐个运行 Python 文件。报告和海报使用系统字体 `C:\Windows\Fonts\simhei.ttf`，非 Windows 环境需指定可用的中文字体。

`scripts/run_all.py` 是早期工作版流水线，不生成四项任务的全部最终交付物；正式复现请使用各任务入口。`scripts/final_submission.py` 在四项任务生成后重建总报告与A2海报，也可双击上一级 `交付文件/最终提交材料/一键生成最终材料.cmd`。当前统一报告为19页，主办方模板答卷为20页。需要 `reportlab` 和 `pillow`。`.runtime` 是本机旧依赖副本，不要将其加入 `PYTHONPATH`；安装 `requirements.txt` 即可。

`99_过程验收存档` 收纳早期临时截图、PDF渲染页、浏览器验收脚本和调试日志，仅供过程追溯，不属于提交材料。
