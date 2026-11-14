from pathlib import Path
import json, re
import numpy as np
import pandas as pd
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务二_百年全景'
OUT=TASK/'06_质量验收'; OUT.mkdir(exist_ok=True)
checks=[]
def add(name,ok,detail=''): checks.append({'check':name,'passed':bool(ok),'detail':str(detail)})

for path in sorted((TASK/'02_数据表').glob('*.csv')):
    try:
        df=pd.read_csv(path)
        numeric=df.select_dtypes(include=[np.number])
        add(f'CSV可读:{path.name}',len(df)>0 and len(df.columns)>0,f'{len(df)}行×{len(df.columns)}列')
        add(f'CSV无无穷值:{path.name}',not np.isinf(numeric.to_numpy()).any() if numeric.size else True)
        add(f'CSV字段名唯一:{path.name}',df.columns.is_unique)
    except Exception as e: add(f'CSV可读:{path.name}',False,e)

for path in sorted((TASK/'02_数据表').glob('*.json')):
    try:
        obj=json.loads(path.read_text(encoding='utf-8'))
        add(f'JSON可读:{path.name}',isinstance(obj,(dict,list)),f'{len(obj)}个顶层条目')
    except Exception as e: add(f'JSON可读:{path.name}',False,e)

for path in sorted((TASK/'04_核心图表').glob('*.png')):
    try:
        with Image.open(path) as im:
            im.verify(); w,h=Image.open(path).size
        add(f'图像完整:{path.name}',w>=1000 and h>=600,f'{w}×{h}')
    except Exception as e: add(f'图像完整:{path.name}',False,e)

for md in [TASK/'00_先看这里.md',TASK/'01_报告与说明'/'01_百年奥运全景分析_高分版.md']:
    text=md.read_text(encoding='utf-8')
    links=re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)',text)
    local=[x for x in links if not re.match(r'^[a-z]+:',x,re.I)]
    missing=[x for x in local if not (md.parent/x).resolve().exists()]
    add(f'Markdown链接:{md.name}',not missing,'缺失: '+', '.join(missing) if missing else f'{len(local)}个本地链接全部存在')

required=[TASK/'01_报告与说明'/'任务二_百年奥运全景_正式报告.pdf',TASK/'01_报告与说明'/'任务二_百年奥运全景_A2海报.pdf',TASK/'05_交互总览'/'index.html',TASK/'一键运行任务二.cmd',TASK/'run_task2.ps1']
for path in required: add(f'关键文件:{path.name}',path.exists() and path.stat().st_size>100,f'{path.stat().st_size if path.exists() else 0} bytes')

report=(TASK/'01_报告与说明'/'01_百年奥运全景分析_高分版.md').read_text(encoding='utf-8')
for token in ['+3.37 个百分点','+2.24 个百分点','[1.30, 3.28]','+2.52 个百分点','2.78至3.60']:
    add(f'报告数字一致:{token}',token in report)

result={'passed':all(x['passed'] for x in checks),'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'items':checks}
(OUT/'任务二自动验收报告.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'passed':result['passed'],'checks':result['checks'],'failed':result['failed']},ensure_ascii=False,indent=2))
if not result['passed']:
    for x in checks:
        if not x['passed']: print('FAILED',x)
    raise SystemExit(1)
