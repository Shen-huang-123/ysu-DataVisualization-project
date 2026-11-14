"""Combine IOC bronze reallocations with unchanged original-book gold/silver."""
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验'
P=OUT/'历史910项来源覆盖总表.csv'
u56='https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocations-from-olympic-games-london-2012'
u105='https://www.olympics.com/ioc/news/ioc-executive-board-approves-medal-reallocation-from-olympic-games-london-2012'
book='https://digital.la84.org/digital/api/collection/p17103coll8/id/85164/download'
decisions=[
 ('Weightlifting Men\'s Bantamweight','PRK','CHN','VIE',u56,30,'2012男子56公斤级：IOC明确铜牌VIE；赛时官方册第30页金PRK银CHN'),
 ('Weightlifting Men\'s Super-Heavyweight','IRI','IRI','KOR',u105,37,'2012男子+105公斤级：IOC明确铜牌KOR；赛时官方册第37页金银均IRI'),
]
d=pd.read_csv(P)
rows=[]
for event,g,s,b,ioc,page,note in decisions:
 idx=d.index[(d.Year==2012)&d.Event.eq(event)]
 assert len(idx)==1,event
 d.loc[idx,'来源类型']='IOC单色重分配+官方成绩册其余两色'
 d.loc[idx,'来源等级']=note+'；未读现行IOC完整小项页'
 d.loc[idx,'来源链接']=ioc+' | '+book
 rows.append({'Year':2012,'Event':event,'现行金牌':g,'现行银牌':s,'现行铜牌':b,'IOC决议':ioc,'赛时成绩册':book,'赛时成绩册PDF页码':page,'证据说明':note})
d.to_csv(P,index=False,encoding='utf-8-sig')
pd.DataFrame(rows).to_csv(OUT/'IOC单色重分配加成绩册逐项台账.csv',index=False,encoding='utf-8-sig')
print('IOC partial medal decisions + original book:',len(rows))
