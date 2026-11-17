"""Bounded sensitivity of historical event proxies to unresolved source evidence.

No source data or forecast targets are overwritten. Scenario C changes the sport
composition and is deliberately not presented as a full Olympic medal table.
"""
from pathlib import Path
import hashlib, json, re
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
T3=ROOT/'交付文件/任务三_专题深挖'
S2=T3/'S2_口径的魔力'
BASE=S2/'08_逐项外部核验'
OUT=BASE/'未决证据三方案敏感性'
OUT.mkdir(exist_ok=True)
inputs=[]
def read(p):
    inputs.append(p)
    return pd.read_csv(p).fillna('')
def save(d,n): d.to_csv(OUT/n,index=False,encoding='utf-8-sig')
original=pd.concat([read(S2/f'02_数据表/S2_{y}历史小项代理表.csv') for y in [2008,2012,2016]],ignore_index=True)
secondary=read(BASE/'Olympedia独立交叉核验/历史555项独立交叉对照.csv')
assert len(original)==910 and len(secondary)==555
assert not original.duplicated(['Year','Event']).any()
assert secondary['配对状态'].eq('自动高可信配对').all()
fixed=original.copy().set_index(['Year','Event'])
changes=[]
for _,r in secondary.iterrows():
    key=(r.Year,r.Event)
    assert key in fixed.index
    for m in ['Gold','Silver','Bronze']:
        old=str(fixed.loc[key,m]); new=str(r[m+'_olympedia'])
        if sorted(re.findall(r'\b[A-Z]{3}\b',old)) != sorted(re.findall(r'\b[A-Z]{3}\b',new)):
            changes.append(dict(Year=r.Year,Sport=r.Sport,Event=r.Event,Medal=m,原代理=old,二次来源=new,逐项链接=r.event_url))
        fixed.loc[key,m]=new
fixed=fixed.reset_index()
keys=set(zip(secondary.Year,secondary.Event))
retained=original[[ (r.Year,r.Event) not in keys for r in original.itertuples() ]].copy()
save(pd.DataFrame(changes),'替代来源差异逐奖牌清单.csv')
assert len(retained)==355
scenarios={'原代理':original,'二次来源替换555项':fixed,'排除555项的剩余子集':retained}
tables=[]; summaries=[]; impacts=[]
def long(frame):
    rows=[]
    for r in frame.itertuples():
        for m in ['Gold','Silver','Bronze']:
            codes=re.findall(r'\b[A-Z]{3}\b',str(getattr(r,m)))
            for code in codes:
                rows.append(dict(Year=r.Year,Event=r.Event,Sport=r.Sport,Medal=m,NOC=code))
    return pd.DataFrame(rows)
base_long=long(original)
for year in [2008,2012,2016]:
    pool=sorted(base_long[base_long.Year.eq(year)].NOC.unique().tolist()+list(set(long(fixed[fixed.Year.eq(year)]).NOC)-set(base_long[base_long.Year.eq(year)].NOC)))
    pool=sorted(set(pool))
    by={}
    for name,frame in scenarios.items():
        sub=frame[frame.Year.eq(year)]; x=long(sub)
        a=pd.crosstab(x.NOC,x.Medal).reindex(index=pool,columns=['Gold','Silver','Bronze'],fill_value=0)
        a['Total']=a.sum(axis=1)
        a['金牌数名次']=a.Gold.rank(method='min',ascending=False).astype(int)
        a['奖牌数名次']=a.Total.rank(method='min',ascending=False).astype(int)
        a['Year']=year;a['方案']=name
        by[name]=a
        tables.append(a.reset_index())
        summaries.append(dict(Year=year,方案=name,小项数=len(sub),保留比例=len(sub)/len(original[original.Year.eq(year)]),运动数=sub.Sport.nunique(),奖牌记录数=len(x),金牌最多代表团='|'.join(a.index[a.Gold.eq(a.Gold.max())]),金牌数最大值=int(a.Gold.max())))
    a=by['原代理']
    for name in ['二次来源替换555项','排除555项的剩余子集']:
        b=by[name]
        shifts=(b['金牌数名次']-a['金牌数名次']).abs()
        impacts.append(dict(Year=year,方案=name,金牌数变动代表团数=int(b.Gold.ne(a.Gold).sum()),金牌数名次变动代表团数=int(shifts.gt(0).sum()),最大金牌名次位移=int(shifts.max()),金牌榜前三集合相同=set(a.index[a['金牌数名次'].le(3)])==set(b.index[b['金牌数名次'].le(3)])))
save(pd.concat(tables),'三方案逐代表团奖牌与名次.csv')
summary=pd.DataFrame(summaries); impact=pd.DataFrame(impacts)
save(summary,'三方案覆盖与头部.csv');save(impact,'三方案名次敏感性.csv')
coverage=original[['Year','Sport','Event']].copy()
coverage['在未决555项内']=[(r.Year,r.Event) in keys for r in coverage.itertuples()]
sport=coverage.groupby(['Year','Sport']).agg(全部小项=('Event','size'),未决小项=('在未决555项内','sum')).reset_index()
sport['排除后小项']=sport.全部小项-sport.未决小项
save(sport,'未决项目运动构成.csv')
manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
(OUT/'输入哈希与检查.json').write_text(json.dumps({'inputs':manifest,'all_events':910,'secondary_events':555,'remaining_events':355,'changed_medal_cells':len(changes),'changed_events':len(set((r['Year'],r['Event']) for r in changes)),'assertions':'输入键唯一、555项高可信映射、排除后355项；主表未修改','ranking':'同届固定代表团池；仅按金牌数/总奖牌数竞争排名(min)，不是IOC金银铜字典序','scope':'仅S2历史小项代理；未重训预测、未重算主场或冠军生存模型。355项也不等于全部已现行IOC核验。'},ensure_ascii=False,indent=2),encoding='utf-8')
report='# 555项未决证据，会改变哪些结论？\n\n'
report+='本轮直接复算S2的三届历史小项代理，不覆盖原数据。巴黎2024官方小项结论不使用这些输入；主场运动员行模型、冠军延续模型与2028预测未在本轮重新估计，不能据此宣称全作品通过。\n\n'
report+='## 三种方案\n\nA保留原代理；B仅将555项金银铜字段替换为已保存的Olympedia二次来源；C从原代理排除这555项，仅保留355项。B不是IOC修订榜。C是改变了运动构成的子集压力测试，不能冒称全届榜，也不能拿它作为无偏估计。其他355项的既有结果未在B中全面修订。\n\n'
report+=f'二次来源替换改变{len(changes)}个奖牌字段、涉及{len(set((r["Year"],r["Event"]) for r in changes))}个小项。差异多于此前旧抓取与二次来源的7项，因为本轮比较对象是主数据代理，而非2023旧抓取。\n\n'
report+=summary.to_markdown(index=False)+'\n\n'+impact.to_markdown(index=False)+'\n\n'
report+='## 结论处理\n\n- 历史逐队数值和精确名次：必须保留来源版本，引用原代理与二次来源情景的差异，不统一写为官方现行榜。\n- 排除情景：用运动构成表解释名次改变，不把筛选后的结果当作原结论被因果推翻或证实。\n- 巴黎2024口径重排：与这555项输入分离，可继续作为主要证据；并不因此证明其他历史结论。\n- 主场、冠军延续和预测：继续保留各自局限。预测更换历史目标还需要匹配训练、调参与赛前回放，不能只替换评分标签就算全链验证。\n\n排名在每届三方案共同固定的代表团池内按金牌数采用竞争排名；同金牌数同名次，其他颜色不破同分。奖牌字段含多个代表团时逐个计数，同一代码跨多个奖牌槽保留重数。此处不比较运动员行榜。\n\n'
report+='## 复算与下一批核查\n\n运行 `py 项目工作区/scripts/historical_uncertainty_sensitivity.py`。逐队表用于找到具体受影响代表团，逐奖牌差异清单用于继续查官方原件；输入哈希记录供复现。本轮结果是来源情景敏感性，不是所有可能改判的最坏界限。\n'
(OUT/'未决证据影响报告.md').write_text(report,encoding='utf-8')
print(json.dumps({'changed_medal_cells':len(changes),'changed_events':len(set((r['Year'],r['Event']) for r in changes)),'impacts':impacts},ensure_ascii=False,indent=2))
