"""Overlay explicitly documented IOC medal reallocations on the 910-event audit.

Only full three-colour decisions enter the verified-count overlay. IOC decisions
covering silver/bronze alone are combined with the current World Athletics final.
This is an exception ledger, not a certification of all remaining event pages.
"""
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
PROXY=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'02_数据表'/'S2_2012历史小项代理表.csv'
u800='https://www.olympics.com/ioc/news/ioc-executive-board-approves-olympic-medal-diploma-and-medallist-pin-reallocation-for-london-2012-olympic-games'
wa800='https://worldathletics.org/competitions/olympic-games/the-xxx-olympic-games-6999193/results/women/800-metres/final/result'
uwalk='https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012-1'
uweight='https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012'
decisions=[
 ('Athletics Women\'s 800 metres','RSA','KEN','USA',u800+' | '+wa800,'2026-06-22','IOC确认银铜；World Athletics现行决赛表确认金牌'),
 ('Athletics Women\'s 20 kilometres Walk','CHN','CHN','CHN',uwalk,'2023','IOC明确三色重分配'),
 ('Athletics Women\'s 400 metres Hurdles','USA','CZE','JAM',uwalk,'2023','IOC明确三色重分配'),
 ('Weightlifting Men\'s Heavyweight','IRI','POL','UZB',uweight,'2020','IOC明确105公斤级三色重分配；主数据以Heavyweight命名'),
]
p=pd.read_csv(PROXY,dtype=str).set_index('Event')
base=pd.read_csv(OUT/'历史910项来源覆盖总表.csv',dtype=str).fillna('')
assert len(base)==910 and not base.duplicated(['Year','Event']).any()
rows=[]
for event,g,s,b,url,date,note in decisions:
    assert event in p.index,event
    old=p.loc[event]
    key=base.Year.eq('2012')&base.Event.eq(event)
    assert key.sum()==1,event
    rows.append({'Year':2012,'Event':event,'现行金牌':g,'现行银牌':s,'现行铜牌':b,
                 '主数据金牌':old.Gold,'主数据银牌':old.Silver,'主数据铜牌':old.Bronze,
                 '三色与主数据一致':(g,s,b)==(old.Gold,old.Silver,old.Bronze),
                 '官方决议或决赛页':url,'官方决议日期':date,'核验日期':'2026-11-12','映射说明':note})
    base.loc[key,'status']='现行IOC重分配：'+g+'/'+s+'/'+b+'；主数据与现行结果不一致'
    base.loc[key,'来源等级']='IOC奖牌重分配决议逐项核验'
    base.loc[key,'来源链接']=url
    base.loc[key,'来源类型']='IOC现行官方修订'
ledger=pd.DataFrame(rows)
assert len(ledger)==4 and not ledger['三色与主数据一致'].any()
ledger.to_csv(OUT/'IOC现行奖牌重分配逐项台账.csv',index=False,encoding='utf-8-sig')
base.to_csv(OUT/'历史910项来源覆盖总表.csv',index=False,encoding='utf-8-sig')
assert base['来源类型'].eq('Olympics.com第三方2023抓取存档').sum()==899
print('4 current IOC revisions; 899 archive-only records remain')

