"""Reproduce the athlete-row host model; separately refit event-unit source scenarios.

Never distribute an event medal to invented athletes. Existing inputs stay untouched.
"""
from pathlib import Path
import hashlib,json,re
import numpy as np
import pandas as pd
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parents[2]
T3=ROOT/'交付文件/任务三_专题深挖'; S2=T3/'S2_口径的魔力'
OUT=T3/'S1_东道主效应/01_来源与口径敏感性';OUT.mkdir(exist_ok=True)
raw=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
secondary=S2/'08_逐项外部核验/Olympedia独立交叉核验/历史555项独立交叉对照.csv'
inputs=[raw,secondary,*[S2/f'02_数据表/S2_{y}历史小项代理表.csv' for y in (2008,2012,2016)]]
d=pd.read_csv(raw);d=d[d.include_main.astype(bool)].copy()
m=d[d.is_medal.astype(bool)].copy();years=sorted(d.Year.unique())
part=d.groupby(['Year','NOC']).size().div(d.groupby('Year').size(),level='Year').mul(100)
athlete=m.groupby(['Year','NOC']).size().div(m.groupby('Year').size(),level='Year').mul(100)
hosts={1948:'GBR',1952:'FIN',1956:'AUS',1960:'ITA',1964:'JPN',1968:'MEX',1972:'FRG',1976:'CAN',1980:'URS',1984:'USA',1988:'KOR',1992:'ESP',1996:'USA',2000:'AUS',2004:'GRE',2008:'CHN',2012:'GBR',2016:'BRA',2020:'JPN',2024:'FRA'}
get=lambda series,y,n:float(series.get((y,n),np.nan))

def fit(year,noc,outcome,donors=None):
    i=years.index(year);pre=years[i-3:i];post=years[i:min(i+3,len(years))]
    if donors is None:
        pool=sorted(set(d.loc[d.Year.isin(pre+[year]),'NOC']))
        donors=[n for n in pool if n!=noc and not any(hosts.get(y)==n for y in post)
                and np.isfinite([get(outcome,y,n) for y in pre+[year]]+[get(part,y,n) for y in pre]).all()]
    if len(donors)<5:return None
    target=np.array([get(outcome,y,noc) for y in pre]+[get(part,y,noc) for y in pre])
    if not np.isfinite(target).all():return None
    X=np.vstack([[get(outcome,y,n) for n in donors] for y in pre]+[[get(part,y,n) for n in donors] for y in pre])
    scale=np.maximum(np.std(X,axis=1),.25);Xs=X/scale[:,None];ts=target/scale
    # Same objective and initialization as task2_causal_upgrade.py.
    fun=lambda w:np.sum((Xs@w-ts)**2)+.002*np.sum(w*w)
    res=minimize(fun,np.repeat(1/len(donors),len(donors)),bounds=[(0,1)]*len(donors),constraints={'type':'eq','fun':lambda w:w.sum()-1},method='SLSQP',options={'maxiter':2000,'ftol':1e-10})
    if not res.success:
        # Same convex objective: analytic derivatives avoid finite-difference stalls.
        res=minimize(lambda w:fun(w)*.01,np.repeat(1/len(donors),len(donors)),jac=lambda w:(2*Xs.T@(Xs@w-ts)+.004*w)*.01,bounds=[(0,1)]*len(donors),constraints={'type':'eq','fun':lambda w:w.sum()-1,'jac':lambda w:np.ones_like(w)},method='SLSQP',options={'maxiter':4000,'ftol':1e-12})
    if not res.success:raise RuntimeError((year,noc,res.message))
    assert abs(res.x.sum()-1)<1e-7 and res.x.min()>-1e-9
    w=res.x;actual=get(outcome,year,noc);syn=np.array([get(outcome,year,n) for n in donors])@w
    rms=np.sqrt(np.mean((np.array([get(outcome,y,noc) for y in pre])-np.array([[get(outcome,y,n) for n in donors] for y in pre])@w)**2))
    return dict(host_year=year,host_NOC=noc,actual=actual,synthetic=float(syn),gap_pp=float(actual-syn),pre_rmspe=float(rms),donors=len(donors)),donors,w

# Reproduce, rather than overwrite, all 17 legacy host-edition fits.
oldpath=ROOT/'交付文件/任务二_百年全景/02_数据表/B_20届主办事件研究.csv';inputs.append(oldpath)
old=pd.read_csv(oldpath);old=old[old.k.eq(0)].set_index('host_year')
rep=[]
for year,noc in hosts.items():
    z=fit(year,noc,athlete)
    if z:
        row,_,_=z;row['既有差值']=float(old.loc[year,'gap_pp']);row['绝对复现误差']=abs(row['gap_pp']-row['既有差值']);rep.append(row)
assert len(rep)==len(old)==17 and max(r['绝对复现误差'] for r in rep)<1e-5

# Event units: one NOC/medal/event slot; shared colours for different NOCs retained.
event=m[m.Year.le(2016)][['Year','Sport','Event','Medal','NOC']].drop_duplicates().copy()
for year in (2008,2012,2016):
    table=pd.read_csv(S2/f'02_数据表/S2_{year}历史小项代理表.csv').fillna('')
    expected={(int(r.Year),r.Sport,r.Event,med,n) for r in table.itertuples() for med in ('Gold','Silver','Bronze') for n in re.findall(r'\b[A-Z]{3}\b',str(getattr(r,med)))}
    observed=set(event[event.Year.eq(year)].itertuples(index=False,name=None))
    assert observed==expected,(year,len(observed),len(expected))
sec=pd.read_csv(secondary).fillna('');assert len(sec)==555
keys=set(zip(sec.Year,sec.Sport,sec.Event));blocked=set(zip(sec.Sport,sec.Event))
revised=event[[tuple(r) not in keys for r in event[['Year','Sport','Event']].itertuples(index=False,name=None)]].copy()
added=[dict(Year=int(r.Year),Sport=r.Sport,Event=r.Event,Medal=med,NOC=n) for r in sec.itertuples() for med in ('Gold','Silver','Bronze') for n in re.findall(r'\b[A-Z]{3}\b',str(getattr(r,med+'_olympedia')))]
revised=pd.concat([revised,pd.DataFrame(added)],ignore_index=True).drop_duplicates()
excluded=event[[tuple(r) not in blocked for r in event[['Sport','Event']].itertuples(index=False,name=None)]].copy()
# Remove the entire same-name event series in every year, not only host years.
participation_index=d[d.Year.le(2016)].groupby(['Year','NOC']).size().index
def share(frame):
    return frame.groupby(['Year','NOC']).size().reindex(participation_index,fill_value=0).div(frame.groupby('Year').size(),level='Year').mul(100)
outcomes={'小项原代理':share(event),'小项二次来源替换':share(revised),'排除未决同名系列':share(excluded)}
rows=[];weights=[];coverage=[]
for year,noc in hosts.items():
    if year>2016:continue
    base=fit(year,noc,outcomes['小项原代理'])
    if base is None:continue
    _,donors,_=base
    for name,outcome in outcomes.items():
        row,_,w=fit(year,noc,outcome,donors)
        row['方案']=name;rows.append(row)
        weights.extend(dict(方案=name,host_year=year,host_NOC=noc,donor=n,weight=float(v)) for n,v in zip(donors,w))
for name,frame in [('小项原代理',event),('小项二次来源替换',revised),('排除未决同名系列',excluded)]:
    for y,g in frame.groupby('Year'):coverage.append(dict(方案=name,Year=int(y),小项数=len(g[['Sport','Event']].drop_duplicates()),奖牌槽数=len(g)))
r=pd.DataFrame(rows);summaries=[]
common=set.intersection(*[set(r[r['方案'].eq(name)].host_year) for name in outcomes]);assert common
for name,g in r.groupby('方案',sort=False):
    g=g[g.host_year.isin(common)];v=g.gap_pp.to_numpy();rng=np.random.default_rng(42)
    ci=np.quantile(rng.choice(v,size=(10000,len(v)),replace=True).mean(axis=1),[.025,.975])
    grouped=g.groupby('host_NOC').gap_pp.agg(['sum','size'])
    pick=np.random.default_rng(42).integers(0,len(grouped),size=(10000,len(grouped)))
    cluster=grouped['sum'].to_numpy()[pick].sum(axis=1)/grouped['size'].to_numpy()[pick].sum(axis=1)
    cc=np.quantile(cluster,[.025,.975])
    summaries.append(dict(方案=name,共同主办案例数=len(g),平均差值=float(v.mean()),区间下限=float(ci[0]),区间上限=float(ci[1]),正差值案例数=int((v>0).sum()),代表团簇数=len(grouped),代表团成组下限=float(cc[0]),代表团成组上限=float(cc[1])))
summary=pd.DataFrame(summaries)
for name,frame in [('原运动员行模型复现.csv',pd.DataFrame(rep)),('三方案逐主办案例.csv',r),('三方案完整对照权重.csv',pd.DataFrame(weights)),('三方案逐届覆盖.csv',pd.DataFrame(coverage)),('三方案共同案例摘要.csv',summary)]:frame.to_csv(OUT/name,index=False,encoding='utf-8-sig')
check=dict(input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},legacy_cases=17,max_reproduction_error=max(z['绝对复现误差'] for z in rep),secondary_event_keys=len(keys),excluded_same_name_series=len(blocked),common_host_cases=sorted(map(int,common)),bootstrap_seed=42,bootstrap_draws=10000,scope='单位敏感性与二次来源情景；非IOC现行认证、非因果识别；参赛行特征保持原值，对照池在各案例原小项情景确定并固定，权重分别重拟合；不改写运动员归属')
(OUT/'复算检查与输入哈希.json').write_text(json.dumps(check,ensure_ascii=False,indent=2),encoding='utf-8')
text='# 主场关联是否依赖运动员行口径和历史奖牌来源？\n\n'
text+='## 先分清两种问题\n\n既有17个合成对照案例采用运动员奖牌行份额。本次完整复现各案例，数值误差小于0.00001个百分点。555项来源记录只给小项奖牌代表团集合，不能据此重分配个人奖牌，故不伪造“修正后的运动员行”。\n\n'
text+='另建小项代理口径：同届同Sport、Event、Medal、NOC保留一槽，多个代表团同色奖牌保留各槽；这仍可能合并同NOC同色多枚，属于代理而非官方奖牌数。2008/2012/2016与S2代理的奖牌槽逐条一致。只分析至2016，避免2020、2024不同命名结构混入。\n\n'
text+='## 三种情景与共同样本\n\nA原小项代理；B仅替换555项的三色代表团；C在所有年份剔除涉及555项的Sport+Event整条同名系列，保持跨届筛选规则。C改变运动构成，不是消除偏差后的真值。各案例对照池由A确定并固定，B/C重新拟合权重；模型保留既有三期奖牌份额与参赛行份额、约束和正则。份额以当情景全体奖牌槽为分母，不能与原运动员行模型的数值直接等同。\n\n'
text+=summary.to_markdown(index=False)+'\n\n'
text+='95%区间为共同主办案例成组重抽样10000次、种子42；不是随机主办实验的因果置信区间。并不证明投入、观众、资格等机制。\n\n## 三个近期历史主办案例\n\n'
text+='另按主办代表团整簇重抽样，保留同一代表团多次主办的相关性；每次以抽到的案例总数作分母。两种区间都不能消除各国间共同冲击或主办权选择偏差。\n\n'
text+=r[r.host_year.isin([2008,2012,2016])][['方案','host_year','host_NOC','actual','synthetic','gap_pp','pre_rmspe']].to_markdown(index=False)+'\n\n'
text+='各方案的前拟合质量与案例正负变化应逐项阅读，不按每个方案重新挑选高拟合案例来比较均值。原17/14案例结果继续明确为运动员行口径，不能把本轮小项敏感性写成该模型的官方来源认证。历史政体、抵制、非随机主办权、项目规则变化和系列命名断裂仍限制解释。参赛行特征未随奖牌来源改变；本轮未重训2028预测。\n\n复现：`py 项目工作区/scripts/host_source_sensitivity.py`。输入哈希、逐案例值、完整权重、逐届覆盖与原模型复现记录均在本目录，原始文件未覆盖。\n'
(OUT/'主场来源与口径敏感性说明.md').write_text(text,encoding='utf-8')
print(summary.to_string(index=False));print(r[r.host_year.isin([2008,2012,2016])].to_string(index=False));print(json.dumps(check,ensure_ascii=False,indent=2))
