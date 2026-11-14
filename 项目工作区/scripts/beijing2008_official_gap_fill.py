"""Complete the seven 2008 archive gaps from primary results books.

Book entries are contemporaneous (August 2008); a later IOC sanction is
recorded separately. This does not certify all 910 current IOC result pages.
"""
from pathlib import Path
import hashlib
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'
SRC=ROOT/'资料文件'/'外部核验'/'北京2008官方成绩册'
PROXY=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'02_数据表'/'S2_2008历史小项代理表.csv'
urls={
 '公路自行车.pdf':'https://digital.la84.org/digital/api/collection/p17103coll8/id/65340/download',
 '场地自行车.pdf':'https://digital.la84.org/digital/api/collection/p17103coll8/id/65441/download',
 '山地自行车.pdf':'https://digital.la84.org/digital/api/collection/p17103coll8/id/65366/download',
}
aquatics='https://www.worldaquatics.com/news/1914024/pr-40-30-swimmers-to-confirm-olympic-dream-in-setubal-por'
sanction='https://www.olympics.com/ioc/news/ioc-sanctions-five-athletes-who-competed-in-beijing'
entries=[
 ('Cycling Men\'s Individual Time Trial','SUI','SWE','USA','公路自行车.pdf',31,''),
 ('Cycling Men\'s Madison','ARG','ESP','RUS','场地自行车.pdf',None,''),
 ('Cycling Men\'s Mountainbike, Cross-Country','FRA','FRA','SUI','山地自行车.pdf',17,''),
 ('Cycling Men\'s Points Race','ESP','GER','GBR','场地自行车.pdf',None,''),
 ('Cycling Men\'s Road Race, Individual','ESP','ITA','SUI','公路自行车.pdf',6,'2009年IOC取消意大利银牌；赛时成绩不可作为现行奖牌表'),
 ('Cycling Women\'s Mountainbike, Cross-Country','GER','POL','RUS','山地自行车.pdf',9,''),
 ('Swimming Men\'s 10 kilometres Open Water','NED','GBR','GER',None,None,''),
]
proxy=pd.read_csv(PROXY).set_index('Event')
missing=set(pd.read_csv(OUT/'未匹配小项.csv').Event)
assert set(x[0] for x in entries)==missing
rows=[]
for event,g,s,b,pdf,page,note in entries:
    old=proxy.loc[event]
    score=(str(old.Gold)==g and str(old.Silver)==s and str(old.Bronze)==b)
    if event=="Cycling Men's Road Race, Individual":
        assert (str(old.Gold),str(old.Silver),str(old.Bronze))==('ESP','SUI','RUS')
    else:assert score,event
    source=urls[pdf] if pdf else aquatics
    rows.append({'Year':2008,'Event':event,'赛时金牌':g,'赛时银牌':s,'赛时铜牌':b,
                 '主数据金牌':old.Gold,'主数据银牌':old.Silver,'主数据铜牌':old.Bronze,
                 '三色与赛时一致':score,'原始来源':source,'PDF页码':page or '见决赛成绩表',
                 '原始文件SHA256':hashlib.sha256((SRC/pdf).read_bytes()).hexdigest() if pdf else '',
                 '后续裁决来源':sanction if note else '',
                 '当前结果状态':'IOC已取消赛时银牌；转递结果需现行官网复核' if note else '原始官方成绩与主数据一致',
                 '备注':note})
ledger=pd.DataFrame(rows)
ledger.to_csv(OUT/'2008七项官方原始成绩补证.csv',index=False,encoding='utf-8-sig')
archive=pd.read_csv(OUT/'逐小项三色对照.csv')
archive_view=archive[['Year','Event_proxy','status','source_capture','olympics_event_url']].rename(columns={'Event_proxy':'Event','source_capture':'来源等级','olympics_event_url':'来源链接'})
archive_view['来源类型']='Olympics.com第三方2023抓取存档'
official_view=pd.DataFrame({'Year':ledger.Year,'Event':ledger.Event,'status':ledger['当前结果状态'],
                            '来源等级':'2008赛时官方成绩册或国际单项组织原始记录',
                            '来源链接':ledger['原始来源'],'来源类型':'官方原始补证'})
joined=pd.concat([archive_view,official_view],ignore_index=True).sort_values(['Year','Event'])
assert len(joined)==910 and not joined.duplicated(['Year','Event']).any()
joined.to_csv(OUT/'历史910项来源覆盖总表.csv',index=False,encoding='utf-8-sig')
md='''# 2008存档缺失7项：官方原始结果补证

七项均已找到一手成绩：六项自行车取自北京2008官方成绩册，LA84获IOC许可数字化保存；男子10公里公开水域游泳取自国际单项组织 World Aquatics 的回顾记录。逐项的原始链接、成绩册页码、SHA256、赛时三色奖牌和主数据三色奖牌见 `2008七项官方原始成绩补证.csv`。七项全部补证后，**910/910项都有逐项外部来源记录**，见 `历史910项来源覆盖总表.csv`。其中903项仍是2023年第三方抓取的Olympics.com存档，不能据来源覆盖率推称910项均已通过2026现行官网核验。

公路男子个人赛的赛时成绩册为西班牙金、意大利银、瑞士铜；[IOC在2009年宣布取消意大利Davide Rebellin的银牌](https://www.olympics.com/ioc/news/ioc-sanctions-five-athletes-who-competed-in-beijing)。主数据为西班牙金、瑞士银、俄罗斯铜。此处的**赛时与后续口径不同**，不能把成绩册的银铜直接覆盖主数据；瑞士和俄罗斯最终递补结果还需IOC现行项目页或明确的奖牌重分配决议确认。

场地自行车PDF文本编码异常，但LA84网页提供可检索转录，男子记分赛与麦迪逊决赛前三名已逐名核对：[场地成绩册](https://digital.la84.org/digital/api/collection/p17103coll8/id/65441/page/0/inline/p17103coll8_65441_0)。其余自行车成绩可在对应PDF页重查。World Aquatics同时确认男子10公里的荷兰、英国、德国领奖顺序。

**证据层级**：这一步解决了7项“无外部一手来源”的缺口；并未解决其余存档差异、后续奖牌重分配或910项现行IOC页面实时逐项核验。复算：`python 项目工作区/scripts/beijing2008_official_gap_fill.py`。
'''
(OUT/'2008官方补证说明.md').write_text(md,encoding='utf-8')
print('7 official gap entries, combined coverage',len(joined),'of 910')

