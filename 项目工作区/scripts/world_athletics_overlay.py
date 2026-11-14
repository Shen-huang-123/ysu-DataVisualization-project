"""Promote independently checked World Athletics rows in 910-source ledger.

Run after beijing2008_official_gap_fill.py and ioc_reallocation_ledger.py.
This is sport-federation current result evidence, never labelled IOC current.
"""
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
base=pd.read_csv(OUT/'历史910项来源覆盖总表.csv',dtype=str).fillna('')
wa=pd.read_csv(OUT/'世界田联现行奥运田径逐项核验.csv',dtype=str).fillna('')
assert len(base)==910 and not base.duplicated(['Year','Event']).any()
assert len(wa)==138 and wa.status.str.startswith('世界田联现行决赛三色已抽取').all()
assert not wa.duplicated(['Year','Event']).any()
for r in wa.itertuples(index=False):
    key=base.Year.eq(r.Year)&base.Event.eq(r.Event)
    assert key.sum()==1,(r.Year,r.Event)
    assert base.loc[key,'来源类型'].iloc[0] in ['Olympics.com第三方2023抓取存档','世界田联现行竞赛结果']
    current=f'{r.Gold_current}/{r.Silver_current or "—"}/{r.Bronze_current or "—"}'
    consistency='与主数据一致' if r.Gold_proxy_match=='True' and r.Silver_proxy_match=='True' and r.Bronze_proxy_match=='True' else '与主数据不同'
    base.loc[key,'status']='世界田联现行名次：'+current+'；'+consistency
    base.loc[key,'来源等级']='2026-11-13世界田联现行奥运决赛页逐项抓取，HTML SHA256及三色见独立核验表'
    base.loc[key,'来源链接']=r.official_url
    base.loc[key,'来源类型']='世界田联现行竞赛结果'
assert base['来源类型'].value_counts().to_dict()=={
    'Olympics.com第三方2023抓取存档':761,
    '世界田联现行竞赛结果':138,
    '官方原始补证':7,
    'IOC现行官方修订':4,
}
base.to_csv(OUT/'历史910项来源覆盖总表.csv',index=False,encoding='utf-8-sig')
print(base['来源类型'].value_counts().to_dict())
