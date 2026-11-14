"""Compare IJF current category medals with old archive; update coverage only on valid matches."""
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
a=pd.read_csv(OUT/'国际柔联现行奥运逐级别核验.csv')
o=pd.read_csv(OUT/'逐小项三色对照.csv')
b=pd.read_csv(OUT/'历史910项来源覆盖总表.csv')
d=a.merge(o,left_on=['Year','Event'],right_on=['Year','Event_proxy'],validate='one_to_one')
assert len(d)==42
diff=[]
for _,r in d.iterrows():
 same={k:sorted(r[k].split('|'))==sorted(str(r[f'{k}_archive']).split('|')) for k in ('Gold','Silver','Bronze')}
 if not all(same.values()):diff.append({'Year':r.Year,'Event':r.Event,**{k:r[k] for k in ('Gold','Silver','Bronze')},**{k+'_archive':r[f'{k}_archive'] for k in ('Gold','Silver','Bronze')}})
 idx=b.index[(b.Year==r.Year)&(b.Event==r.Event)]
 assert len(idx)==1
 b.loc[idx,'来源类型']='国际柔联现行逐级别结果'
 b.loc[idx,'来源等级']='国际柔联现行奥运级别排名，逐项读取前四名；不等同于IOC现行授牌结果'
 b.loc[idx,'来源链接']=r.SourceURL
b.to_csv(OUT/'历史910项来源覆盖总表.csv',index=False,encoding='utf-8-sig')
pd.DataFrame(diff,columns=['Year','Event','Gold','Silver','Bronze','Gold_archive','Silver_archive','Bronze_archive']).to_csv(OUT/'国际柔联与旧存档差异.csv',index=False,encoding='utf-8-sig')
print('IJF 42; mismatches',len(diff));print(pd.DataFrame(diff).to_string(index=False) if diff else 'none')
print(b['来源类型'].value_counts().to_string())
