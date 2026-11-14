from pathlib import Path
import json,re
import numpy as np
import pandas as pd
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]; TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'; OUT=TASK/'05_质量验收'; OUT.mkdir(exist_ok=True)
checks=[]
def add(name,ok,detail=''): checks.append({'check':name,'passed':bool(ok),'detail':str(detail)})
for p in sorted((TASK/'02_数据表').glob('*.csv')):
    try:
        d=pd.read_csv(p); num=d.select_dtypes(include=[np.number]); add('CSV可读:'+p.name,len(d)>0,f'{len(d)}行×{len(d.columns)}列'); add('CSV无无穷值:'+p.name,not np.isinf(num.to_numpy()).any() if num.size else True)
    except Exception as e:add('CSV可读:'+p.name,False,e)
for p in sorted((TASK/'02_数据表').glob('*.json')):
    try:add('JSON可读:'+p.name,isinstance(json.loads(p.read_text(encoding='utf-8')),(dict,list)))
    except Exception as e:add('JSON可读:'+p.name,False,e)
for p in sorted((TASK/'04_核心图表').glob('*.png')):
    try:
        with Image.open(p) as im: im.verify()
        w,h=Image.open(p).size; add('图像完整:'+p.name,w>=1000 and h>=600,f'{w}×{h}')
    except Exception as e:add('图像完整:'+p.name,False,e)
md=TASK/'01_报告与说明'/'S2_口径的魔力_高分版.md'; text=md.read_text(encoding='utf-8'); links=re.findall(r'!?(?:\[[^\]]*\])\(([^)]+)\)',text); missing=[x for x in links if not (md.parent/x).resolve().exists()]; add('报告本地链接',not missing,missing)
rank=pd.read_csv(TASK/'02_数据表'/'S2_2024双口径完整排名.csv').set_index('NOC'); add('美中官方金牌均40',rank.loc['USA','Gold_official']==40 and rank.loc['CHN','Gold_official']==40); add('荷兰排名6到3',rank.loc['NED','official_rank']==6 and rank.loc['NED','row_rank']==3); add('西班牙排名15到5',rank.loc['ESP','official_rank']==15 and rank.loc['ESP','row_rank']==5)
pdf=TASK/'01_报告与说明'/'S2_口径的魔力_正式报告.pdf'; add('正式PDF存在',pdf.exists() and pdf.stat().st_size>100000,pdf.stat().st_size if pdf.exists() else 0)
interactive=TASK/'06_交互榜'/'index.html'; add('三口径交互榜存在',interactive.exists() and interactive.stat().st_size>10000,interactive.stat().st_size if interactive.exists() else 0)
story=TASK/'06_滚动叙事专题'/'index.html'; add('滚动叙事专题存在',story.exists() and story.stat().st_size>15000,story.stat().st_size if story.exists() else 0)
official_hist=pd.read_csv(TASK/'02_数据表'/'S2_历史项目数量对照摘要.csv'); add('三届代理数量对照',len(official_hist)==3 and official_hist['event_count_match'].all(),official_hist[['Year','event_rows']].to_dict('records'))
hist=pd.read_csv(TASK/'02_数据表'/'S2_跨届稳定性摘要.csv'); add('跨届机制稳定',len(hist)==3 and (hist['mechanism_rho']>0.95).all(),hist[['Year','mechanism_rho']].to_dict('records'))
tri=pd.read_csv(TASK/'02_数据表'/'S2_2024三口径完整排名.csv'); add('三口径数据完整',set(tri['lens'])=={'official','fractional','rows'} and len(tri)>200,len(tri))
result={'passed':all(x['passed'] for x in checks),'checks':len(checks),'failed':sum(not x['passed'] for x in checks),'items':checks}; (OUT/'S2自动验收报告.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8'); print(json.dumps({k:result[k] for k in ['passed','checks','failed']},ensure_ascii=False,indent=2)); raise SystemExit(0 if result['passed'] else 1)
