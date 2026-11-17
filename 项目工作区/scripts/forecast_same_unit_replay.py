"""Chronological nested tuning in event-proxy units; no claim of vintage IOC data.

An independent benchmark, not a silent replacement for the published LA28 model.
"""
from pathlib import Path
import json,re,hashlib
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

ROOT=Path(__file__).resolve().parents[2];T4=ROOT/'交付文件/任务四_开放创作'
OUT=T4/'05_满分升级/14_同口径时序重训';OUT.mkdir(exist_ok=True)
raw=ROOT/'交付文件/任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz'
official=raw.parent/'2024官方329小项奖牌表.csv'
secondary=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/Olympedia独立交叉核验/历史555项独立交叉对照.csv'
d=pd.read_csv(raw);d=d[d.include_main.astype(bool)]
m=d[d.is_medal.astype(bool)&d.Year.between(1960,2016)][['Year','Sport','Event','Medal','NOC']].drop_duplicates()
sec=pd.read_csv(secondary).fillna('');keys=set(zip(sec.Year,sec.Sport,sec.Event))
b=m[[tuple(x) not in keys for x in m[['Year','Sport','Event']].itertuples(index=False,name=None)]].copy()
extra=[dict(Year=int(r.Year),Sport=r.Sport,Event=r.Event,Medal=med,NOC=n) for r in sec.itertuples() for med in ['Gold','Silver','Bronze'] for n in re.findall(r'\b[A-Z]{3}\b',str(getattr(r,med+'_olympedia')))]
b=pd.concat([b,pd.DataFrame(extra)],ignore_index=True).drop_duplicates()
o=pd.read_csv(official).fillna('');actual24=[]
for r in o.itertuples():
    for col in ['gold_country_code','silver_country_code','bronze_country_code']:
        actual24.extend(re.findall(r'\b[A-Z]{3}\b',getattr(r,col)))
actual24=pd.Series(actual24).value_counts().astype(float)
years=sorted(m.Year.unique())+[2024]
counts={}
for name,frame in [('A原代理',m),('B二次来源',b)]:
    counts[name]={int(y):g.groupby('NOC').size().astype(float) for y,g in frame.groupby('Year')}
    counts[name][2024]=actual24
def candidates(y):
    # Do not dilute the score with every defunct delegation since 1896.
    # Participation labels remain usable in 2020 even though medal-event labels do not.
    visible=sorted(d.loc[d.Year.lt(y),'Year'].unique())[-3:]
    return sorted(d.loc[d.Year.isin(visible),'NOC'].unique())
def features(source,y):
    past=[a for a in years if a<y];tail=past[-3:]
    if len(tail)<3:return None
    pool=candidates(y);hist=[counts[source][a]/counts[source][a].sum() for a in tail]
    X=np.stack([z.reindex(pool,fill_value=0).to_numpy() for z in hist],axis=1)
    gap=(y-tail[-1])/4
    return pool,np.column_stack([X[:,2],X[:,1],X[:,2]-X[:,1],X.mean(axis=1),X.std(axis=1),np.full(len(pool),gap)])
def training(source,cutoff):
    xs=[];ys=[];used=[]
    for y in years:
        if y>=cutoff:break
        z=features(source,y)
        if z is None:continue
        pool,X=z;t=counts[source][y];xs.append(X);ys.append(t.reindex(pool,fill_value=0).to_numpy()/t.sum());used.append(int(y))
    return np.vstack(xs),np.concatenate(ys),used
def pool_estimate(source,y):
    past=[a for a in years if a<y][-3:];tot=np.array([counts[source][a].sum() for a in past]);annual=np.diff(tot)/np.diff(past)
    return max(1,float(tot[-1]+np.median(annual)*(y-past[-1])))
alphas=[.1,1.,10.,100.];tuning=[];audit=[];predictions={}
for source in counts:
    for target in [2012,2016,2024]:
        validation=[int(y) for y in years if 1996<=y<target]
        scores=[]
        for alpha in alphas:
            per=[]
            for val in validation:
                X,Y,used=training(source,val);pool,V=features(source,val)
                assert max(used)<val<target
                model=make_pipeline(StandardScaler(),Ridge(alpha=alpha));model.fit(X,Y)
                p=np.maximum(0,model.predict(V));p=p/p.sum()*pool_estimate(source,val)
                actual=counts[source][val];universe=sorted(set(pool)|set(actual.index))
                predicted=pd.Series(p,index=pool).reindex(universe,fill_value=0);truth=actual.reindex(universe,fill_value=0)
                per.append(float((predicted-truth).abs().mean()))
                tuning.append(dict(来源=source,目标届=target,内部验证届=val,alpha=alpha,MAE=per[-1],训练最大届=max(used)))
            scores.append((float(np.mean(per)),alpha))
        _,alpha=min(scores)
        X,Y,used=training(source,target);pool,V=features(source,target)
        model=make_pipeline(StandardScaler(),Ridge(alpha=alpha));model.fit(X,Y)
        ridge=np.maximum(0,model.predict(V));ridge=ridge/ridge.sum()
        past=max(a for a in years if a<target);baseline=counts[source][past].reindex(pool,fill_value=0);baseline=baseline/baseline.sum()
        total=pool_estimate(source,target)
        for name,v in [('上一可用届份额',baseline.to_numpy()),('同口径岭回归',ridge),('固定55_45混合',.55*baseline.to_numpy()+.45*ridge)]:predictions[source,target,name]=pd.Series(v*total,index=pool)
        audit.append(dict(来源=source,目标届=target,训练届次=','.join(map(str,used)),训练最大届=max(used),内部验证届次=','.join(map(str,validation)),选中alpha=alpha,最近可用届=past,预测间隔年=target-past,赛前估计池=total,目标实际池_仅评分=float(counts[source][target].sum()),历史候选代表团数=len(pool)))
detail=[];scores=[]
for source,year,model in predictions:
    for target_source in ([source] if source=='B二次来源' else ['A原代理','B二次来源']):
        pred=predictions[source,year,model];truth=counts[target_source][year];idx=sorted(set(pred.index)|set(truth.index));p=pred.reindex(idx,fill_value=0);a=truth.reindex(idx,fill_value=0)
        mae=float((p-a).abs().mean());strong=a.ge(5)
        scores.append(dict(训练来源=source,评分来源=target_source,Year=year,模型=model,评分代表团数=len(idx),MAE=mae,MAE至少5枚=float((p[strong]-a[strong]).abs().mean()),RMSE=float(np.sqrt(((p-a)**2).mean())),预测池=float(p.sum()),实际池=float(a.sum()),未见获奖代表团数=len(set(truth.index)-set(pred.index))))
        for n in idx:detail.append(dict(训练来源=source,评分来源=target_source,Year=year,模型=model,NOC=n,预测=float(p[n]),实际=float(a[n]),误差=float(p[n]-a[n]),赛前候选=n in pred.index))
for name,rows in [('内部时序调参记录.csv',tuning),('逐折数据边界.csv',audit),('三折同口径评分.csv',scores),('三折逐队预测.csv',detail)]:pd.DataFrame(rows).to_csv(OUT/name,index=False,encoding='utf-8-sig')
manifest=dict(input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [raw,official,secondary]},folds=[2012,2016,2024],training_rule='训练与内部验证届次均严格早于外层目标届；候选代表团只由目标前最近三届参赛记录构造，评分补入当届未见获奖代表团且预测为零',version_limit='历史记录含赛后追溯修订，缺少逐届赛前冻结快照，不能宣称严格真实时点回测',excluded_2020='2020小项字段泛化，不用于同口径奖牌特征；2024距最近可用2016为8年，非标准单届预测；2020参赛身份仍可用于候选池',not_validated='已发布2028最终集成、新增运动排名、资格、主场加成和区间覆盖率均非本脚本验证对象',model='代表团总量岭回归独立基准；不是原RF/GB体育项目模型')
(OUT/'复算检查与输入哈希.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(pd.DataFrame(scores).to_string(index=False))
