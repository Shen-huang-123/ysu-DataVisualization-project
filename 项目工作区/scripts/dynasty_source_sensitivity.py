"""Recompute S3 transitions and the pre-existing fixed cohort under source alternatives."""
from pathlib import Path
import hashlib,json,re
import numpy as np
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
T3=ROOT/'交付文件/任务三_专题深挖'
BASE=T3/'S3_冠军的保质期'
OUT=BASE/'11_历史来源敏感性';OUT.mkdir(exist_ok=True)
paths=[BASE/'02_数据表/S3_逐小项冠军控制权转移.csv',BASE/'09_固定小项队列检验/固定小项逐届控制权转移.csv',T3/'S2_口径的魔力/08_逐项外部核验/Olympedia独立交叉核验/历史555项独立交叉对照.csv']
t,fixed,sec=[pd.read_csv(p).fillna('') for p in paths]
def codes(v):return '|'.join(sorted(set(re.findall(r'\b[A-Z]{3}\b',str(v)))))
def flag(v):return str(v).lower()=='true'
t['defended']=t.defended.map(flag)
fixed['defended']=fixed.defended.map(flag)
assert len(t)==4511 and len(fixed)==1582 and fixed.event_key.nunique()==113
observed={}
for r in t.itertuples():
    for year,value in [(r.from_year,r.previous),(r.to_year,r.current)]:
        k=(r.event_key,int(year));value=codes(value)
        assert k not in observed or observed[k]==value,k
        observed[k]=value
overlay={};mapping=[]
for r in sec.itertuples():
    k=(r.Sport+'｜'+r.Event,int(r.Year));new=codes(r.Gold_olympedia)
    # Exact original identity only; unmatched labels never guessed from medals.
    overlay[k]=new
    mapping.append(dict(Year=r.Year,Event=r.Event,Sport=r.Sport,event_key=k[0],S3有同名观测=k in observed,原金牌=observed.get(k,''),替代金牌=new,金牌集合改变=k in observed and observed[k]!=new,来源=r.event_url))
mapped=pd.DataFrame(mapping)
corrected=t.copy();changed=[]
for i,r in t.iterrows():
    a=(r.event_key,int(r.from_year));b=(r.event_key,int(r.to_year))
    prev=overlay.get(a,codes(r.previous));cur=overlay.get(b,codes(r.current))
    defended=bool(set(prev.split('|')) & set(cur.split('|')) - {''})
    corrected.loc[i,['previous','current','defended']]=[prev,cur,defended]
    if codes(r.previous)!=prev or codes(r.current)!=cur:
        changed.append(dict(event_key=r.event_key,Sport=r.Sport,Event=r.Event,from_year=r.from_year,to_year=r.to_year,原上届=codes(r.previous),替代上届=prev,原本届=codes(r.current),替代本届=cur,原卫冕=bool(r.defended),替代卫冕=defended))
assert corrected.defended.map(lambda x:isinstance(x,(bool,np.bool_))).all()
fixedkeys=set(fixed.event_key)
correctedfixed=corrected[corrected.event_key.isin(fixedkeys)&corrected.from_year.ge(1960)&corrected.to_year.le(2016)].copy()
assert len(correctedfixed)==1582
blocked={key for key,year in overlay if key in fixedkeys}
retained=fixed[~fixed.event_key.isin(blocked)].copy()
assert len(retained)==retained.event_key.nunique()*14
summary=[];eventrows=[]
def score(name,d):
    early=d[d.to_year.between(1964,1976)].groupby('event_key').defended.mean()
    late=d[d.to_year.between(1996,2016)].groupby('event_key').defended.mean()
    assert early.index.equals(late.index)
    delta=(late-early).to_numpy(dtype=float)
    rng=np.random.default_rng(42)
    ci=np.quantile(rng.choice(delta,size=(10000,len(delta)),replace=True).mean(axis=1),[.025,.975])*100
    for key in early.index:eventrows.append(dict(方案=name,event_key=key,早段卫冕率=float(early[key]),后段卫冕率=float(late[key]),差值百分点=float((late[key]-early[key])*100)))
    summary.append(dict(方案=name,小项数=len(delta),转移数=len(d),早段卫冕率=float(early.mean()),后段卫冕率=float(late.mean()),后减前百分点=float(delta.mean()*100),区间下限=float(ci[0]),区间上限=float(ci[1])))
score('原代理固定队列',fixed)
score('二次来源替换_同113项',correctedfixed)
score('剔除涉及未决项的完整小项队列',retained)
# Same selected events with/without revised sources: selection is not a correction effect.
score('原代理_与排除方案同子队列',fixed[fixed.event_key.isin(retained.event_key.unique())])
era=[]
for name,d in [('原代理',t),('二次来源替换',corrected)]:
    for lo,hi in [(1896,1948),(1952,1988),(1992,2016)]:
        z=d[d.to_year.between(lo,hi)]
        era.append(dict(方案=name,时代=f'{lo}–{hi}',转移数=len(z),卫冕次数=int(z.defended.sum()),卫冕率=float(z.defended.mean())))
def save(d,n):pd.DataFrame(d).to_csv(OUT/n,index=False,encoding='utf-8-sig')
save(summary,'固定队列三方案复算.csv');save(eventrows,'逐小项前后段变化.csv');save(changed,'受影响控制权转移.csv');save(mapping,'555项与S3精确映射.csv');save(era,'全样本时代复算.csv')
corrected.to_csv(OUT/'二次来源情景全部控制权转移.csv',index=False,encoding='utf-8-sig')
prior=json.loads((BASE/'09_固定小项队列检验/固定小项检验摘要.json').read_text(encoding='utf-8'))
assert np.isclose(summary[0]['早段卫冕率'],prior['early_rate']) and np.isclose(summary[0]['后段卫冕率'],prior['late_rate'])
info=dict(input_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},original_transitions=len(t),fixed_events=113,secondary_observations_matched=int(mapped['S3有同名观测'].sum()),secondary_observations_unmatched=int((~mapped['S3有同名观测']).sum()),gold_observations_changed=int(mapped['金牌集合改变'].sum()),transition_champion_sets_changed=len(changed),transition_defense_flags_changed=sum(r['原卫冕']!=r['替代卫冕'] for r in changed),excluded_fixed_events=len(blocked),retained_fixed_events=retained.event_key.nunique(),bootstrap_seed=42,bootstrap_draws=10000,scope='二次来源情景；非现行IOC认证、非因果检验；保留原始数据，既有主页面图未静默改写')
(OUT/'复算检查与输入哈希.json').write_text(json.dumps(info,ensure_ascii=False,indent=2),encoding='utf-8')
s=pd.DataFrame(summary)
md='# 历史来源修订后，冠军延续的下降还成立吗？\n\n'
md+='固定既有113个1960—2016连续小项，保持原有早段1964—1976、后段1996—2016及小项成组重抽样。A使用原代理；B仅替换S2队列中与S3的Sport+Event+Year精确匹配的金牌代表团集合；C为避免早晚段组成不一致，剔除任一届涉及555项的小项的**整条1960—2016序列**。另列C的原代理同子队列作选择对照。\n\n'
md+=s.to_markdown(index=False)+'\n\n'
md+=f'555个来源记录中{info["secondary_observations_matched"]}个与S3观测精确对应，{info["secondary_observations_unmatched"]}个未匹配、不猜测映射；{info["gold_observations_changed"]}个金牌集合变化，影响{len(changed)}条转移的冠军集合，其中{info["transition_defense_flags_changed"]}条卫冕判定改变。全4511条转移的三个时代复算见附表。\n\n'
md+='## 可以保留与必须收窄的判断\n\n'
b=summary[1];c=summary[2]
md+=f'同113项二次来源情景差值为{b["后减前百分点"]:.2f}个百分点，成组95%区间[{b["区间下限"]:.2f}, {b["区间上限"]:.2f}]。只对这一固定队列和时间窗判断下降是否保持，不能写成所有运动或所有年代都如此。\n\n'
md+=f'排除后仅剩{c["小项数"]}个小项，差值{c["后减前百分点"]:.2f}个百分点，区间[{c["区间下限"]:.2f}, {c["区间上限"]:.2f}]。区间跨过零，排除子队列尚不足以确认下降；原代理同50项也得到相同结果，不能把变化归因于来源替换。该样本运动结构不同，且剩余项也不等于全部取得现行IOC结果；不能将它称为官方认证样本。\n\n'
md+='研究单位是代表团小项金牌控制权；并列金牌集合存在交集即延续。不是个人冠军寿命，也没有证明竞争加剧这一机制。未更换其他历史年份的记录，未解决小项实质规则变化、政体身份与抵制混杂；二次来源本身仍可能存在误差。本轮不更新主场模型或预测。\n\n'
md+='## 复现\n\n`py 项目工作区/scripts/dynasty_source_sensitivity.py`。输入哈希、精确映射、受影响转移、逐小项变化及全样本时代表均在本目录。旧图和原数据保留原版本；新增结果单列来源情景，避免将二次来源修订伪装为IOC结果。\n'
(OUT/'冠军延续来源敏感性说明.md').write_text(md,encoding='utf-8')
print(json.dumps({'checks':info,'summary':summary},ensure_ascii=False,indent=2))

# A direct interval comparison, with unchanged cohort distinguished from exclusion.
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['Microsoft YaHei','SimHei']
plt.rcParams['axes.unicode_minus']=False
fig,ax=plt.subplots(figsize=(10,4.3),facecolor='#f7f3eb');ax.set_facecolor('#f7f3eb')
for i,r in enumerate(summary[:3]):
    x=r['后减前百分点'];color='#247487' if i<2 else '#a64155'
    ax.errorbar(x,2-i,xerr=[[x-r['区间下限']],[r['区间上限']-x]],fmt='o',color=color,capsize=5,lw=2)
    ax.text(4,2-i,f"{x:.2f}  [{r['区间下限']:.2f}, {r['区间上限']:.2f}]",va='center',fontsize=10)
ax.axvline(0,color='#68777d',ls='--',lw=1)
ax.set_yticks([2,1,0],['原代理 · 固定113项','二次来源替换 · 同113项','排除未决系列 · 剩50项'])
ax.set_xlim(-18,18);ax.set_ylim(-.6,2.8);ax.set_xlabel('后段减早段卫冕率（百分点）；横线为小项成组95%区间')
ax.set_title('同队列替换不改变下降；排除子队列的区间跨零',loc='left',pad=18,fontsize=14)
for sp in ax.spines.values():sp.set_visible(False)
ax.tick_params(length=0);fig.tight_layout();fig.savefig(OUT/'冠军延续来源敏感性.png',dpi=160);plt.close(fig)
