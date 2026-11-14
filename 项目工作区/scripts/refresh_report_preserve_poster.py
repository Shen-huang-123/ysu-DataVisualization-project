from pathlib import Path
from tempfile import TemporaryDirectory
from shutil import copy2
import subprocess, sys

root=Path(__file__).resolve().parents[2]
poster=root/'交付文件/最终提交材料/海报/百年圣火_A2海报_正式版.pdf'
mirror=root/'项目工作区/deliverables/百年圣火_A2海报_正式版.pdf'
with TemporaryDirectory(dir=root/'项目工作区') as tmp:
    saved=[]
    for p in (poster,mirror):
        if p.exists():
            b=Path(tmp)/str(len(saved));copy2(p,b);saved.append((p,b))
    try:
        subprocess.run([sys.executable,str(root/'项目工作区/scripts/final_submission.py')],check=True,cwd=root)
    finally:
        for p,b in saved:copy2(b,p)
print('正式报告已刷新；原海报已保留。')
