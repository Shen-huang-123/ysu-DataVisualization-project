from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务二_百年全景'; FIG=TASK/'04_核心图表'; TAB=TASK/'02_数据表'
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
d=pd.read_csv(DATA); d=d[d.include_main.astype(bool)].copy(); m=d[d.is_medal.astype(bool)].copy()
years=sorted(d.Year.unique()); totals=m.groupby('Year').size(); part_tot=d.groupby('Year').size()
med_share=m.groupby(['Year','NOC']).size().div(totals,level='Year').mul(100)
part_share=d.groupby(['Year','NOC']).size().div(part_tot,level='Year').mul(100)

hosts={1948:'GBR',1952:'FIN',1956:'AUS',1960:'ITA',1964:'JPN',1968:'MEX',1972:'FRG',1976:'CAN',1980:'URS',1984:'USA',1988:'KOR',1992:'ESP',1996:'USA',2000:'AUS',2004:'GRE',2008:'CHN',2012:'GBR',2016:'BRA',2020:'JPN',2024:'FRA'}

def get(series,y,n): return float(series.get((y,n),np.nan))
def synth_case(year,noc,outcome=med_share):
    i=years.index(year); pre=years[i-3:i]; post=years[i:min(i+3,len(years))]
    all_nocs=sorted(set(d.loc[d.Year.isin(pre+[year]),'NOC']))
    donors=[]
    for n in all_nocs:
        if n==noc or any(hosts.get(py)==n for py in post): continue
        vals=[get(outcome,y,n) for y in pre+[year]]
        pvals=[get(part_share,y,n) for y in pre]
        if np.isfinite(vals).all() and np.isfinite(pvals).all(): donors.append(n)
    if len(donors)<5: return None
    target=np.array([get(outcome,y,noc) for y in pre]+[get(part_share,y,noc) for y in pre])
    if not np.isfinite(target).all(): return None
    X=np.vstack([[get(outcome,y,n) for n in donors] for y in pre]+[[get(part_share,y,n) for n in donors] for y in pre])
    scale=np.maximum(np.nanstd(X,axis=1),.25); Xs=X/scale[:,None]; ts=target/scale
    fun=lambda w: np.sum((Xs@w-ts)**2)+.002*np.sum(w*w)
    w0=np.repeat(1/len(donors),len(donors)); res=minimize(fun,w0,bounds=[(0,1)]*len(donors),constraints={'type':'eq','fun':lambda w:w.sum()-1},method='SLSQP',options={'maxiter':2000,'ftol':1e-10})
    if not res.success: return None
    w=res.x; pre_actual=np.array([get(outcome,y,noc) for y in pre]); pre_syn=np.array([[get(outcome,y,n) for n in donors] for y in pre])@w
    rmspe=float(np.sqrt(np.mean((pre_actual-pre_syn)**2)))
    rows=[]
    for k,y in zip(range(0,len(post)),post):
        actual=get(outcome,y,noc); syn=np.nansum(np.array([get(outcome,y,n) for n in donors])*w)
        rows.append({'host_year':year,'host_NOC':noc,'k':k,'Year':y,'actual':actual,'synthetic':syn,'gap_pp':actual-syn,'pre_rmspe':rmspe,'donors':len(donors)})
    top=sorted(zip(donors,w),key=lambda x:x[1],reverse=True)[:6]
    return rows,top

rows=[]; weights=[]
for y,n in hosts.items():
    out=synth_case(y,n)
    if out:
        rr,ww=out; rows+=rr
        for donor,w in ww:
            if w>.001: weights.append({'host_year':y,'host_NOC':n,'donor':donor,'weight':w})
r=pd.DataFrame(rows); w=pd.DataFrame(weights)
cases=r[r.k.eq(0)].copy(); cases['special_1956']=cases.host_year.eq(1956); cases['boycott']=cases.host_year.isin([1980,1984])

rng=np.random.default_rng(20261107)
def boot_ci(x,B=50000):
    x=np.asarray(x); z=np.array([rng.choice(x,len(x),replace=True).mean() for _ in range(B)]); return [float(x.mean()),float(np.quantile(z,.025)),float(np.quantile(z,.975))]
all_est=boot_ci(cases.gap_pp); clean=boot_ci(cases.loc[~cases.boycott & ~cases.special_1956,'gap_pp']); highfit=boot_ci(cases.loc[cases.pre_rmspe.le(1),'gap_pp'])
loo=[]
for idx,row in cases.iterrows(): loo.append({'excluded':f"{row.host_NOC} {row.host_year}",'mean_gap_pp':float(cases.drop(idx).gap_pp.mean())})
loo=pd.DataFrame(loo)
summary={'candidate_host_editions':len(hosts),'usable_cases':int(len(cases)),'high_fit_cases':int(cases.pre_rmspe.le(1).sum()),'period':'1948-2024','synthetic_control_mean_pp':all_est[0],'bootstrap_ci95':all_est[1:],'high_fit_mean_pp':highfit[0],'high_fit_ci95':highfit[1:],'exclude_1956_and_boycotts_mean_pp':clean[0],'exclude_1956_and_boycotts_ci95':clean[1:],'mean_pre_rmspe':float(cases.pre_rmspe.mean()),'leave_one_out_range':[float(loo.mean_gap_pp.min()),float(loo.mean_gap_pp.max())]}
r.to_csv(TAB/'B_20届主办事件研究.csv',index=False,encoding='utf-8-sig'); w.to_csv(TAB/'B_合成对照权重.csv',index=False,encoding='utf-8-sig'); loo.to_csv(TAB/'B_留一法稳健性.csv',index=False,encoding='utf-8-sig'); (TAB/'B_扩展合成对照摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')

P={'teal':'#247487','red':'#A64155','gold':'#C4903D','paper':'#F7F3EB','grid':'#D9DEDC','ink':'#172A30','grey':'#6C7A80'}
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':P['paper'],'axes.facecolor':P['paper'],'savefig.facecolor':P['paper']})
fig,axes=plt.subplots(1,3,figsize=(16,6),gridspec_kw={'width_ratios':[1.3,1,1]})
cc=cases.sort_values('gap_pp'); axes[0].barh(cc.host_NOC+' '+cc.host_year.astype(str),cc.gap_pp,color=[P['red'] if x<0 else P['teal'] for x in cc.gap_pp]); axes[0].axvline(0,color=P['ink'],lw=.8); axes[0].set_xlabel('主办届 - 合成对照（百分点）'); axes[0].set_title('17个可用案例：多数主办届高于反事实',loc='left',fontweight='bold')
balanced_hosts=set(cases.loc[cases.host_year.le(2016),'host_year']); event=r[r.host_year.isin(balanced_hosts)].groupby('k')[['actual','synthetic']].mean(); base=event.loc[0,'synthetic']
axes[1].plot(event.index,event.actual,marker='o',lw=2.5,color=P['red'],label='主办国'); axes[1].plot(event.index,event.synthetic,marker='o',lw=2.5,color=P['teal'],label='合成对照'); axes[1].set_xticks(event.index,['主办届','下一届','下两届'][:len(event)]); axes[1].set_ylabel('奖牌记录份额（%）'); axes[1].legend(frameon=False); axes[1].set_title(f'平衡事件路径：{len(balanced_hosts)}个完整窗口',loc='left',fontweight='bold'); axes[1].grid(axis='y',color=P['grid'])
labels=['全部可用\n17届','高拟合质量\n14届','剔除1956及\n抵制届']; vals=[all_est[0],highfit[0],clean[0]]; los=[all_est[0]-all_est[1],highfit[0]-highfit[1],clean[0]-clean[1]]; his=[all_est[2]-all_est[0],highfit[2]-highfit[0],clean[2]-clean[0]]
axes[2].errorbar(range(3),vals,yerr=[los,his],fmt='o',ms=9,color=P['red'],capsize=6,lw=2); axes[2].axhline(0,color=P['ink'],lw=.8); axes[2].set_xticks(range(3),labels); axes[2].set_ylabel('平均合成对照差（百分点）'); axes[2].set_title('敏感性分析：更严格样本仍为正',loc='left',fontweight='bold'); axes[2].grid(axis='y',color=P['grid'])
fig.suptitle('B 识别再升级：扩展主办样本 × 合成对照 × 稳健性检验',fontsize=20,fontweight='bold',x=.04,ha='left')
fig.text(.04,.014,f"1948—2024共20个候选主办届，17届满足三期前史，14届前拟合RMSPE≤1。全样本均值 {all_est[0]:.2f}pp；高拟合样本 {highfit[0]:.2f}pp（95%CI {highfit[1]:.2f}—{highfit[2]:.2f}）。主办权仍非随机，结论为高可信准实验关联。",fontsize=8.4,color=P['grey'])
fig.savefig(FIG/'B_20届合成对照与稳健性.png',bbox_inches='tight',dpi=220); plt.close(fig)
print(json.dumps(summary,ensure_ascii=False,indent=2))
