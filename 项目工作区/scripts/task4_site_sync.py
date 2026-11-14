"""Refresh the deployable Task 4 bundle after post-build analysis pages are generated."""
from pathlib import Path
import re
import shutil

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务四_开放创作'
DIST=ROOT/'项目工作区'/'sites'/'la28-fullscore'/'dist'
DIST.mkdir(parents=True,exist_ok=True)
shutil.copytree(TASK,DIST,dirs_exist_ok=True)
# The offline task-three cross-link lives outside this standalone deploy bundle.
page=DIST/'02_2028洛杉矶预测'/'index.html'
if page.exists():
    text=page.read_text(encoding='utf-8')
    text=re.sub(r'<!-- stability-map-entry --><a\b.*?</a>','',text,flags=re.S)
    page.write_text(text,encoding='utf-8')
for name in ['滚动留出验证.html','预测误差图谱.html','2024同单位验证.html']:
    assert (DIST/'05_满分升级'/name).exists(),name
assert (DIST/'05_满分升级'/'07_模型消融与资格情景'/'index.html').exists()
assert (DIST/'05_满分升级'/'08_历史误差归因'/'index.html').exists()
assert (DIST/'05_满分升级'/'09_赛前条件回放'/'index.html').exists()
print(DIST)
