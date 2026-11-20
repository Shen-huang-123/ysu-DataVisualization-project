"""Original RF/GB architecture, past-only selection and event-unit refits.

Frozen published hyperparameters; this is not a blind prospective trial or IOC certification.
"""
from pathlib import Path
import hashlib,json,re,time
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor,GradientBoostingRegressor

ROOT=Path(__file__).resolve().parents[2];T4=ROOT/'交付文件/任务四_开放创作';OUT=T4/'05_满分升级/15_原项目模型时序核验';OUT.mkdir(exist_ok=True)
raw=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz';official=raw.parent/'2024官方329小项奖牌表.csv'
secondary=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/Olympedia独立交叉核验/历史555项独立交叉对照.csv'
d=pd.read_csv(raw);d=d[d.include_main.astype(bool)].copy();m=d[d.is_medal.astype(bool)].copy()
row=m[m.Year.ge(2000)].groupby(['Year','NOC','sport_family']).size().rename('records').reset_index()
ev=m[m.Year.between(2000,2016)].drop_duplicates(['Year','Sport','Event','Medal','NOC'])
event=ev.groupby(['Year','NOC','sport_family']).size().rename('records').reset_index()
mapping=m[m.Year.between(2000,2016)][['Year','Sport','Event','sport_family']].drop_duplicates()
assert not mapping.duplicated(['Year','Sport','Event']).any()
family_lookup=mapping.set_index(['Year','Sport','Event']).sport_family.to_dict()
sec=pd.read_csv(secondary).fillna('');keys=set(zip(sec.Year,sec.Sport,sec.Event));assert keys.issubset(family_lookup)
filtered=ev[[tuple(r) not in keys for r in ev[['Year','Sport','Event']].itertuples(index=False,name=None)]]
extra=[dict(Year=int(r.Year),Sport=r.Sport,Event=r.Event,Medal=med,NOC=n,sport_family=family_lookup[(r.Year,r.Sport,r.Event)]) for r in sec.itertuples() for med in ['Gold','Silver','Bronze'] for n in re.findall(r'\b[A-Z]{3}\b',str(getattr(r,med+'_olympedia')))]
rev=pd.concat([filtered,pd.DataFrame(extra)],ignore_index=True).drop_duplicates(['Year','Sport','Event','Medal','NOC'])
revised=rev.groupby(['Year','NOC','sport_family']).size().rename('records').reset_index()

# Structural mapping specified before modelling; never chosen from model scores.
families={'3x3 Basketball':'Basketball','Beach Volleyball':'Volleyball','Artistic Gymnastics':'Gymnastics','Rhythmic Gymnastics':'Gymnastics','Trampoline Gymnastics':'Gymnastics','Canoe Slalom':'Canoeing','Canoe Sprint':'Canoeing','Marathon Swimming':'Swimming','Rugby Sevens':'Rugby'}
official24=pd.read_csv(official).fillna('');slots=[];maprows=[]
known=set(d.sport_family)
for r in official24.itertuples():
    family=families.get(r.discipline,'Cycling' if r.discipline.startswith('Cycling ') else r.discipline)
    assert family in known,r.discipline
    maprows.append(dict(discipline=r.discipline,sport_family=family,规则='预设运动家族结构映射'))
    for medal,field in [('Gold','gold_country_code'),('Silver','silver_country_code'),('Bronze','bronze_country_code')]:
        for n in re.findall(r'\b[A-Z]{3}\b',getattr(r,field)):slots.append(dict(Year=2024,NOC=n,sport_family=family,event_id=r.event_id,Medal=medal))
actual24=pd.DataFrame(slots).groupby(['Year','NOC','sport_family']).size().rename('records').reset_index()
event=pd.concat([event,actual24],ignore_index=True);revised=pd.concat([revised,actual24],ignore_index=True)
pd.DataFrame(maprows).drop_duplicates().to_csv(OUT/'2024运动家族结构映射.csv',index=False,encoding='utf-8-sig')
sources={'运动员行原口径':row,'小项原代理':event,'小项二次来源':revised}
years_by={'运动员行原口径':[2000,2004,2008,2012,2016,2020,2024],'小项原代理':[2000,2004,2008,2012,2016,2024],'小项二次来源':[2000,2004,2008,2012,2016,2024]}
params=dict(RF=dict(n_estimators=280,min_samples_leaf=3,max_features=.65,random_state=28,n_jobs=2),GB=dict(n_estimators=220,max_depth=2,learning_rate=.035,loss='huber',random_state=28))
audits=[];scores=[];predrows=[];selection=[];cellrows=[]

def candidate_pool(target):
    ys=sorted(d.loc[d.Year.lt(target),'Year'].unique())[-3:]
    return sorted(d.loc[d.Year.isin(ys),'NOC'].unique())
def baseline(table,years,target,pool):
    past=[y for y in years if y<target][-3:];wide=table[table.Year.isin(past)].groupby(['NOC','Year']).records.sum().unstack(fill_value=0).reindex(index=pool,columns=past,fill_value=0)
    w=np.array([.2,.3,.5]);v=wide.to_numpy()@w+.15*(wide[past[-1]]-wide[past[-2]]).to_numpy();v=np.maximum(0,v);return v/v.sum()
def estimate_pool(table,years,target):
    ys=[y for y in years if y<target][-3:];tot=table.groupby('Year').records.sum();return max(1,float(tot[ys[-1]]+np.median(np.diff(tot.loc[ys].to_numpy())/np.diff(ys))*(target-ys[-1])))

def run(source,target,leaky=False,forecast_pool=None):
    start=time.monotonic();table=sources[source];years=years_by[source];prior=table[table.Year.lt(target)]
    select=table if leaky else prior
    nocs=select.groupby('NOC').records.sum().sort_values(ascending=False,kind='stable').head(100).index.tolist()
    sports=select.groupby('sport_family').records.sum().sort_values(ascending=False,kind='stable').head(45).index.tolist()
    assert leaky or int(select.Year.max())<target
    selected='含目标届选择诊断' if leaky else '仅此前届次'
    for kind,values in [('NOC',nocs),('sport_family',sports)]:selection.extend(dict(来源=source,Year=target,选择规则=selected,类型=kind,值=v) for v in values)
    history=[y for y in years if y<target]
    idx=pd.MultiIndex.from_product([history+[target],nocs,sports],names=['Year','NOC','sport_family'])
    # Target response is deliberately never copied into the feature panel.
    p=prior.set_index(['Year','NOC','sport_family']).records.reindex(idx,fill_value=0).rename('records').reset_index()
    p['lag1']=p.groupby(['NOC','sport_family']).records.shift(1);p['lag2']=p.groupby(['NOC','sport_family']).records.shift(2)
    p['trend']=p.lag1-p.lag2;p['noc_lag']=p.groupby(['NOC','Year']).lag1.transform('sum');p['sport_lag']=p.groupby(['sport_family','Year']).lag1.transform('sum');p=p.dropna().copy()
    X=pd.get_dummies(p[['NOC','sport_family','lag1','lag2','trend','noc_lag','sport_lag']],columns=['NOC','sport_family'],dtype=float)
    train=p.Year.lt(target);test=p.Year.eq(target);assert not train.eq(test).any()
    assert p.loc[test,'records'].eq(0).all()
    rf=RandomForestRegressor(**params['RF']);gb=GradientBoostingRegressor(**params['GB'])
    rf.fit(X.loc[train],p.loc[train,'records']);gb.fit(X.loc[train],p.loc[train,'records'])
    z=p.loc[test,['NOC','sport_family']].copy();z['RF']=np.maximum(0,rf.predict(X.loc[test]));z['GB']=np.maximum(0,gb.predict(X.loc[test]));z['RF60_GB40']=.6*z.RF+.4*z.GB
    # Save cell-level values before normalizing totals; they retain the target unit.
    truth=table[table.Year.eq(target)].set_index(['NOC','sport_family']).records
    for r in z.itertuples():cellrows.append(dict(来源=source,Year=target,选择规则=selected,NOC=r.NOC,sport_family=r.sport_family,RF=float(r.RF),GB=float(r.GB),组合=float(r.RF60_GB40),实际=np.nan if forecast_pool is not None else float(truth.get((r.NOC,r.sport_family),0))))
    pool=candidate_pool(target);total=estimate_pool(table,years,target) if forecast_pool is None else float(forecast_pool)
    outputs={}
    for model in ['RF','GB','RF60_GB40']:
        v=z.groupby('NOC')[model].sum().reindex(pool,fill_value=0);outputs[model]=v/v.sum()*total
    outputs['历史加权基线']=pd.Series(baseline(table,years,target,pool)*total,index=pool)
    outputs['55基线45项目']=.55*outputs['历史加权基线']+.45*outputs['RF60_GB40']
    if forecast_pool is not None:
        forecast=pd.DataFrame(outputs);forecast.index.name='NOC'
        forecast['主阅读基准名次']=forecast['历史加权基线'].rank(method='min',ascending=False).astype(int)
        forecast['混合相对基准变化']=forecast['55基线45项目']-forecast['历史加权基线']
        forecast.sort_values(['主阅读基准名次','NOC']).reset_index().to_csv(OUT/'2028同口径重训情景榜.csv',index=False,encoding='utf-8-sig')
        forecast_cells=pd.DataFrame([r for r in cellrows if r['Year']==target and r['来源']==source and r['选择规则']==selected])
        assert len(forecast_cells)==len(z) and forecast_cells.Year.eq(2028).all()
        forecast_cells.to_csv(OUT/'2028未归一项目格预测.csv',index=False,encoding='utf-8-sig')
        protocol=dict(source=source,train_years=sorted(map(int,p.loc[train,'Year'].unique())),selection_max_year=int(select.Year.max()),latest_medal_year=max(history),prior_medal_year=history[-2],conditional_pool=total,source_of_pool='沿用既有榜单1120单位总池以比较模型，不代表最终官方规模',model_parameters=params,reading_policy='历史加权基准为主阅读，RF/GB与55/45混合作条件比较；不宣称45%最优或区间已校准',unit_limit='历史小项槽代理+2024逐项表，缺2020可比小项；2028资格及新增运动不由本核心决定')
        (OUT/'2028重训协议.json').write_text(json.dumps(protocol,ensure_ascii=False,indent=2),encoding='utf-8')
        print('2028 event-unit core refitted; baseline is main reading, ML is scenario.',flush=True)
        return
    actual=table[table.Year.eq(target)].groupby('NOC').records.sum();scoring=sorted(set(pool)|set(actual.index));a=actual.reindex(scoring,fill_value=0)
    for model,v in outputs.items():
        v=v.reindex(scoring,fill_value=0);err=v-a;strong=a.ge(5)
        scores.append(dict(来源=source,Year=target,选择规则=selected,模型=model,评分代表团数=len(scoring),MAE=float(err.abs().mean()),MAE至少5单位=float(err[strong].abs().mean()),RMSE=float(np.sqrt((err**2).mean())),实际至少5单位队数=int(strong.sum()),前十重合=len(set(v.sort_values(ascending=False,kind='stable').head(10).index)&set(a.sort_values(ascending=False,kind='stable').head(10).index)),预测池=float(v.sum()),实际池=float(a.sum())))
        for n in scoring:predrows.append(dict(来源=source,Year=target,选择规则=selected,模型=model,NOC=n,预测=float(v[n]),实际=float(a[n]),误差=float(err[n]),此前候选=n in pool))
    modeled=float(truth.reindex(pd.MultiIndex.from_product([nocs,sports],names=['NOC','sport_family']),fill_value=0).sum())
    unseen_sports=table[table.Year.eq(target)&~table.sport_family.isin(sports)].groupby('sport_family').records.sum().to_dict()
    audits.append(dict(来源=source,Year=target,选择规则=selected,选择数据最大届=int(select.Year.max()),训练最大届=int(p.loc[train,'Year'].max()),训练届次=','.join(map(str,sorted(p.loc[train,'Year'].unique()))),训练格数=int(train.sum()),目标特征格数=int(test.sum()),候选NOC数=len(nocs),候选家族数=len(sports),最近奖牌届=max(history),间隔年=target-max(history),估计奖牌池=total,实际池_仅评分=float(actual.sum()),目标已建模格覆盖单位=modeled,目标建模格覆盖率=modeled/actual.sum(),未见运动家族=json.dumps(unseen_sports,ensure_ascii=False),特征列数=X.shape[1],特征哈希=hashlib.sha256(pd.util.hash_pandas_object(X,index=True).values.tobytes()).hexdigest(),目标标签未进入特征=True,耗时秒=time.monotonic()-start))
    print(f'{source} {target} {selected}: MAE '+str({q["模型"]:round(q["MAE"],3) for q in scores[-5:]}),flush=True)

if __name__=='__main__':
    for source in sources:
        for target in [2012,2016,2024]:run(source,target)
    run('运动员行原口径',2024,leaky=True)
    for name,rows in [('原模型五方案评分.csv',scores),('原模型逐队误差.csv',predrows),('逐折选择与训练边界.csv',audits),('逐折代表团和运动选择.csv',selection),('未归一项目格预测.csv',cellrows)]:pd.DataFrame(rows).to_csv(OUT/name,index=False,encoding='utf-8-sig')
    manifest=dict(input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [raw,official,secondary]},parameters=params,ensemble='原RF60%+GB40%；55%基线+45%项目；原正式参数280/220棵；旧滚动回放100/100不直接比较',scope='9个严格时序来源/外层届次，1个明确含目标届的2024筛选诊断；参数冻结不依据本轮评分调优；非独立未见数据测试',unit='运动员行与小项槽分开训练评分，禁止跨单位比较MAE；小项历史为NOC/Sport/Event/Medal代理，2024为既有逐项表',temporal='训练与筛选早于目标，但资料为事后整理修订版，未取得逐届真实赛前版本；小项2024使用2016奖牌特征，间隔8年',not_validated='新增运动排名、资格、主场加成、2028完整最终集成、80%区间覆盖率与IOC逐项认证均未由此完成',mapping='结构映射覆盖2024全部45个discipline，未见历史运动不事后纳入特征')
    (OUT/'输入哈希与模型协议.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print('Saved original-project audit and all cell/delegation predictions.',flush=True)
    # Same comparison pool as the existing conditional table; not an official programme claim.
    run('小项二次来源',2028,forecast_pool=1120)
