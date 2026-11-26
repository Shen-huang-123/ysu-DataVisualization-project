from pathlib import Path
import shutil,json
R=Path(__file__).resolve().parents[1];T=R.parent/'交付文件'/'任务一_数据体检';T.mkdir(parents=True,exist_ok=True)
for folder in ['01_报告与说明','02_交付数据','03_复现代码','04_质量检查结果','06_附图','99_运行生成']: (T/folder).mkdir(exist_ok=True)
for src,dst in [('olympics_flagged.csv.gz','归一数据_保留原始字段.csv.gz'),('sport_mapping.csv','体育大类归一映射表.csv')]:shutil.copy2(R/'outputs'/src,T/'02_交付数据'/dst)
for name in ['audit.json','preparation_summary.json','duplicate_by_year.csv','event_quality_by_year.csv','edition_main.csv','edition_exclude_duplicate_excess.csv','edition_include_1906.csv']:
 shutil.copy2(R/'outputs'/name,T/'04_质量检查结果'/name)
audit=(R/'scripts/audit.py').read_text(encoding='utf-8').split('with zipfile.ZipFile')[0]
audit=audit.replace("ROOT / 'outputs'","ROOT / '04_质量检查结果'").replace("DATA = ROOT.parent / '资料文件' / '原始资料'","DATA = ROOT")
(T/'03_复现代码/audit.py').write_text(audit,encoding='utf-8')
prep=(R/'scripts/prepare.py').read_text(encoding='utf-8').replace("ROOT/'outputs'","ROOT/'99_运行生成'").replace("DATA=ROOT.parent/'资料文件'/'原始资料'","DATA=ROOT")
(T/'03_复现代码/prepare.py').write_text(prep,encoding='utf-8')
(T/'03_复现代码/运行任务一.py').write_text("from pathlib import Path\nimport subprocess,sys\nr=Path(__file__).resolve().parent\nfor n in ['audit.py','prepare.py']: subprocess.run([sys.executable,str(r/n)],check=True)\nprint('任务一审计与归一完成')\n",encoding='utf-8')
(T/'03_复现代码/requirements.txt').write_text('pandas>=2.2,<4\n',encoding='utf-8')
source=(R/'docs/数据质量与口径方案.md').read_text(encoding='utf-8')
source=source.replace('# 数据质量与口径方案','# 数据质量与口径说明书\n\n参赛队：燕山大学 晓组织；张子涵60%，陈旭40%。')
source=source.replace('当前为第一轮审计，不将候选异常直接视为错误。','候选异常不直接视为错误。完整原始记录保留，另增加归一字段与质量标记。')
source=source.replace('`scripts/audit.py`','`代码/audit.py`')
source=source.split('## 尚待完成')[0]
source+='''## 归一与事件处理的执行结果

76个Sport原值均已映射。Cycling Road, Triathlon两条跨家族记录根据Event分别归入自行车和铁人三项；其余逗号组合归入共同运动家族。映射表的event-level resolution required提示须结合逐行sport_family与sport_resolution读取，不表示归一数据仍未解决。

event_status将8515条上下文依赖记录标为generic_or_context_required，包括Singles、Individual等；这比完全泛化词表更宽，不应与赛题约6700条直接比较。其余为specific_label_unverified，表示标签具体但未外部核验。不生成声称官方的小项去重榜。

## 特殊记录规则

1906原始行保留，include_main=False；1956双城合并至同一Year，City不覆盖；历史政体不自动合并，URS/EUN/RUS/ROC/AIN和FRG/GDR/GER分别统计；EOR独立保留，不归入运动员来源国家；不尝试凭残缺姓名修正难民运动员身份。东京使用2020届次年份。缺席届次不等同于参赛但零奖牌。

## 新增字段与数据使用

source_row为原CSV含表头的行号；sport_family为归一运动家族；sport_resolution记录映射方式；event_status记录事件标签风险；include_main为主分析纳入标记；duplicate_candidate标记同组全部重复候选；duplicate_excess仅标记保留首条后的余量；is_medal表示非No medal。

归一文件252565行全部保留。主分析筛选include_main后为250832行，奖牌记录38360行。重复候选2156行、重复余量1466行；不自动删除，敏感性版本只排除duplicate_excess。清洗不是把不可靠信息猜成正确值，而是统一可统一字段、标记无法恢复的信息并限制推断。

## 检查代码与结果对应

说明书上表中规模、空值、重复、姓名与ID、逗号Sport、1906和双城检查均由代码/audit.py执行，结果键名见检查结果/audit.json。代码/prepare.py执行76项映射、上下文标记、重复分层、主分析行数与奖牌数断言，输出preparation_summary.json及逐届敏感性统计。至少五项检查均有代码、实测值及处理决定，无需依赖答卷模板运行。

## 奖牌口径与来源声明

本任务以运动员行口径作为正式主口径，满足至少一种明确口径要求。不把Year/NOC/Event/Medal去重结果称作官方奖牌数。2024外部小项对照属于专题补充，不作为本任务已还原官方小项的证据；其一手核验仍待完成。

数据来源：Stefany De Oliveira，Kaggle Summer Olympics Medals (1896-2024)；上游Nitish Sharma Olympics 124 years Dataset (till 2020)及Petro Ivaniuk Paris 2024 Olympic Summer Games。来源链接见原赛题2.1。衍生数据许可CC BY-NC-SA 4.0，原始CSV不随包提交。原始文件SHA256见audit.json。
'''
(T/'01_报告与说明/01_数据质量与口径说明书.md').write_text(source,encoding='utf-8')
(T/'00_先看这里.md').write_text('''# 任务一交付目录

先阅读任务一_数据质量与口径说明书_高分版.pdf，再查看01_数据质量与口径说明书.md。其余内容按用途分为三个目录：

- 数据：归一数据（gzip压缩CSV，可用pandas直接读取）和完整体育大类映射表。
- 检查结果：审计实测值、归一汇总、重复分布、Event质量与三种逐届敏感性统计。
- 代码：审计、归一及一键运行代码，依赖只有pandas。

## 评委如何复现

将评委持有的olympics_dataset.csv放在本文件夹根目录；安装代码/requirements.txt后，运行 `python 代码/运行任务一.py`。审计结果写入检查结果，归一产物写入复现输出。无需项目其他文件夹或Word模板。

## 任务要求对应

奖牌定义、Event策略、特殊记录规则、至少五项检查见说明书；映射见数据目录；归一数据与代码分别见对应目录。主口径为运动员行，未声称完整还原官方小项。候选重复保留，1906以标记控制，不直接删去历史记录。

本文件夹是任务一的集中交付版本。原项目文件保留用于后续任务，不必逐个翻找。原始CSV不随提交包提供。
''',encoding='utf-8')
print(T)
