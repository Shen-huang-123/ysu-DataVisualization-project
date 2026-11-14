"""Verify two IOC bronze decisions are paired with the correct London results-book pages."""
import sys
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'项目工作区/.runtime'))
import pymupdf
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
d=pd.read_csv(OUT/'IOC单色重分配加成绩册逐项台账.csv')
b=pd.read_csv(OUT/'历史910项来源覆盖总表.csv')
assert len(d)==2 and len(b)==910
book=pymupdf.open(ROOT/'资料文件/外部核验/官方成绩册索引/北京2008_伦敦2012_原始PDF/2012_Weightlifting_85164.pdf')
for r in d.itertuples(index=False):
 row=b[(b.Year==2012)&(b.Event==r.Event)]
 assert len(row)==1 and row.iloc[0]['来源类型']=='IOC单色重分配+官方成绩册其余两色'
 text=book[r.赛时成绩册PDF页码-1].get_text()
 if 'Bantamweight' in r.Event:
  assert "Men's 56kg" in text and 'OM Yun Chol' in text and 'WU Jingbiao' in text and r.现行铜牌=='VIE'
 else:
  assert "Men's +105kg" in text and 'SALIMIKORDASIABI' in text and 'ANOUSHIRAVANI' in text and r.现行铜牌=='KOR'
print('QA PASS: two IOC bronze decisions mapped to correct official original-book pages')
