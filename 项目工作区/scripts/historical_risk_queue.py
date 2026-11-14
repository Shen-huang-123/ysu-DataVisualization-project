"""Prioritise unresolved historical event checks without upgrading source claims."""
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
archive=pd.read_csv(OUT/'逐小项三色对照.csv',dtype=str).fillna('')
base=pd.read_csv(OUT/'历史910项来源覆盖总表.csv',dtype=str).fillna('')
old=base[base['来源类型'].eq('Olympics.com第三方2023抓取存档')][['Year','Event']]
assert len(old)>0
z=old.merge(archive,left_on=['Year','Event'],right_on=['Year','Event_proxy'],validate='one_to_one')
assert len(z)==len(old)
def priority(r):
    if r['status']=='匹配待人工复核':
        return 1,'项目配对不确定'
    if r['gold_match']!='True' or r['silver_match']!='True' or r['bronze_match']!='True':
        return 1,'奖牌三色冲突'
    return 2,'旧存档三色一致，仍待现行来源'
z[['优先级','待核原因']]=z.apply(lambda r:pd.Series(priority(r)),axis=1)
z=z.sort_values(['优先级','Year','Sport','Event'])
cols=['优先级','待核原因','Year','Sport','Event','Event_olympics','Gold_proxy','Silver_proxy','Bronze_proxy',
      'Gold_archive','Silver_archive','Bronze_archive','olympics_event_url']
z[cols].to_csv(OUT/f'历史{len(z)}项风险优先核验清单.csv',index=False,encoding='utf-8-sig')
print('Archive-only:',len(z),'priority counts:',z['优先级'].value_counts().sort_index().to_dict())
