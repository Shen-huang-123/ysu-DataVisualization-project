"""Run key data pipelines in a fresh venv and isolated file tree.

The original CSV stays in 资料文件 and is copied only to a temporary directory.
Run from any working directory with Python 3.11–3.13 and network access for pip.
"""
from pathlib import Path
import json
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parents[2]
SOURCE=Path(os.environ.get('OLYMPICS_CSV',ROOT/'资料文件/原始资料/olympics_dataset.csv'))
if not SOURCE.is_file():raise SystemExit('未找到原始 olympics_dataset.csv；请放在资料文件/原始资料，或设置 OLYMPICS_CSV。')
REQUIREMENTS=ROOT/'项目工作区/requirements.txt'
SCRIPTS=ROOT/'项目工作区/scripts'
TASK1=ROOT/'交付文件/任务一_数据体检'
OUT=ROOT/'交付文件/最终提交材料/异机复现结果.json'

def cp(src,dst):
 dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
def run(cmd,cwd=None,env=None):
 print('运行：',Path(str(cmd[-1])).name,flush=True)
 subprocess.run([str(x) for x in cmd],cwd=cwd,env=env,check=True)
def compare_json(a,b):
 x=json.loads(a.read_text(encoding='utf-8'));y=json.loads(b.read_text(encoding='utf-8'))
 common=set(x)&set(y)
 return {'common_keys':len(common),'equal':bool(common) and all(x[k]==y[k] for k in common),'different_keys':sorted(k for k in common if x[k]!=y[k]),'only_original':sorted(set(x)-set(y)),'only_rebuilt':sorted(set(y)-set(x))}
def compare_file(a,b):
 digest=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
 return {'sha256_equal':digest(a)==digest(b)}

with tempfile.TemporaryDirectory(prefix='olympics-repro-') as tmp:
 q=Path(tmp)
 run([sys.executable,'-m','venv',q/'venv'])
 py=q/'venv/Scripts/python.exe' if os.name=='nt' else q/'venv/bin/python'
 run([py,'-m','pip','install','-r',REQUIREMENTS,'--quiet'])
 for name in ['audit.py','prepare.py','run_task1.py']:
  cp(TASK1/'03_复现代码'/name,q/'交付文件/任务一_数据体检/03_复现代码'/name)
 for name in ['task2_highscore.py','task3_s2_highscore.py','task3_s3_dynasties.py','task4_highscore.py','task4_fullscore_upgrade.py','task2_localization.py','custom_topics_deep_audit.py']:
  cp(SCRIPTS/name,q/'项目工作区/scripts'/name)
 cp(TASK1/'02_交付数据/2024官方329小项奖牌表.csv',q/'交付文件/任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv')
 for name in ['S3_逐小项冠军控制权转移.csv','S3_冠军王朝清单.csv']:
  cp(ROOT/'交付文件/任务三_专题深挖/S3_冠军的保质期/02_数据表'/name,q/'交付文件/任务三_专题深挖/S3_冠军的保质期/02_数据表'/name)
 cp(SOURCE,q/'资料文件/原始资料/olympics_dataset.csv')
 env=os.environ.copy();env['PYTHONUTF8']='1';env['OLYMPICS_CSV']=str(q/'资料文件/原始资料/olympics_dataset.csv')
 run([py,q/'交付文件/任务一_数据体检/03_复现代码/run_task1.py'],env=env)
 cp(q/'交付文件/任务一_数据体检/99_运行生成/olympics_flagged.csv.gz',q/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz')
 for name in ['task2_highscore.py','task3_s2_highscore.py','task3_s3_dynasties.py','task4_highscore.py','task4_fullscore_upgrade.py','custom_topics_deep_audit.py']:
  run([py,q/'项目工作区/scripts'/name],env=env)
 paths=[
  ('任务一审计',TASK1/'04_质量检查结果/audit.json',q/'交付文件/任务一_数据体检/04_质量检查结果/audit.json'),
  ('任务一归一',TASK1/'04_质量检查结果/preparation_summary.json',q/'交付文件/任务一_数据体检/99_运行生成/preparation_summary.json'),
  ('任务二核心',ROOT/'交付文件/任务二_百年全景/02_数据表/任务二关键指标.json',q/'交付文件/任务二_百年全景/02_数据表/任务二关键指标.json'),
  ('任务三S2',ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/02_数据表/S2_关键指标.json',q/'交付文件/任务三_专题深挖/S2_口径的魔力/02_数据表/S2_关键指标.json'),
  ('任务三S7',ROOT/'交付文件/任务三_专题深挖/S3_冠军的保质期/02_数据表/S3_关键指标.json',q/'交付文件/任务三_专题深挖/S3_冠军的保质期/02_数据表/S3_关键指标.json'),
  ('自拟专题',ROOT/'交付文件/任务三_专题深挖/自拟专题深度核验摘要.json',q/'交付文件/任务三_专题深挖/自拟专题深度核验摘要.json'),
 ]
 checks={name:compare_json(a,b) for name,a,b in paths}
 pred=ROOT/'交付文件/任务四_开放创作/02_2028洛杉矶预测'
 isolated_pred=q/'交付文件/任务四_开放创作/02_2028洛杉矶预测'
 file_checks={'模型回测摘要.csv':compare_file(pred/'模型回测摘要.csv',isolated_pred/'模型回测摘要.csv'),'升级模型验证摘要.csv':compare_file(ROOT/'交付文件/任务四_开放创作/05_满分升级/升级模型验证摘要.csv',q/'交付文件/任务四_开放创作/05_满分升级/升级模型验证摘要.csv')}
 result={'passed':all(v['equal'] for v in checks.values()) and all(v['sha256_equal'] for v in file_checks.values()),'python':sys.version,'source_csv':str(SOURCE),'checks':checks,'prediction_file_checks':file_checks,'note':'关键统计流水线复现；未逐页重新生成全部前端和PDF。'}
 OUT.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
 print('核验结果：','全部一致' if result['passed'] else '存在差异',OUT)
 if not result['passed']:raise SystemExit(1)
