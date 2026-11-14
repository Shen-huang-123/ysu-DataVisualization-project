from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from task2_localization import NOC_ZH, SPORT_ZH

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务二_百年全景'; FIG=TASK/'04_核心图表'; TAB=TASK/'02_数据表'; DASH=TASK/'05_交互总览'
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
HOST_SUM=ROOT/'交付文件'/'任务三_专题深挖'/'S1_东道主效应'/'host_summary.csv'
GROUPS=ROOT/'交付文件'/'任务三_专题深挖'/'S1_东道主效应'/'host_comparison_groups.csv'
d=pd.read_csv(DATA); d=d[d.include_main.astype(bool)].copy(); m=d[d.is_medal.astype(bool)].copy()
P={'navy':'#123742','teal':'#247487','red':'#A64155','gold':'#C4903D','paper':'#F7F3EB','grid':'#D9DEDC','grey':'#6C7A80'}
plt.rcParams.update({'font.family':'Microsoft YaHei','axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':P['paper'],'axes.facecolor':P['paper'],'savefig.facecolor':P['paper'],'savefig.dpi':220})

# Matched difference-in-differences with case bootstrap and within-set randomization inference.
h=pd.read_csv(HOST_SUM); g=pd.read_csv(GROUPS)
h['did_pp']=h.change_pp-h.comparison_mean_pp
years=sorted(m.Year.unique()); totals=m.groupby('Year').size()
share=m.groupby(['Year','NOC']).size().div(totals,level='Year').mul(100)
pretr=[]; profiles=[]
for _,r in h.iterrows():
    y=int(r.Year); noc=r.NOC; idx=years.index(y); controls=g[(g.host_year.eq(y))&(g.host_NOC.eq(noc))].NOC.tolist()
    rel_years={k:years[idx+k] for k in [-2,-1,0,1,2] if 0<=idx+k<len(years)}
    def val(n,yy): return float(share.get((yy,n),np.nan))
    for k,yy in rel_years.items():
        hv=val(noc,yy); cv=np.nanmean([val(c,yy) for c in controls])
        profiles.append({'host_year':y,'host_NOC':noc,'k':k,'Year':yy,'host_share':hv,'control_share':cv})
    if -2 in rel_years and -1 in rel_years:
        hp=val(noc,rel_years[-1])-val(noc,rel_years[-2])
        cp=np.nanmean([val(c,rel_years[-1])-val(c,rel_years[-2]) for c in controls])
        pretr.append({'Year':y,'NOC':noc,'pretrend_gap_pp':hp-cp})
prof=pd.DataFrame(profiles); pre=pd.DataFrame(pretr); h=h.merge(pre,on=['Year','NOC'],how='left')
rng=np.random.default_rng(20261107)
boot=np.array([rng.choice(h.did_pp.to_numpy(),len(h),replace=True).mean() for _ in range(50000)])
ci=np.quantile(boot,[.025,.975]); estimate=h.did_pp.mean()
sets=[]
for _,r in h.iterrows():
    changes=[r.change_pp]+g[(g.host_year.eq(r.Year))&(g.host_NOC.eq(r.NOC))].change_pp.tolist(); sets.append(np.array(changes))
placebo=[]
for _ in range(50000):
    eff=[]
    for arr in sets:
        j=rng.integers(len(arr)); eff.append(arr[j]-np.delete(arr,j).mean())
    placebo.append(np.mean(eff))
placebo=np.array(placebo); extreme=int((np.abs(placebo)>=abs(estimate)).sum()); p=extreme/len(placebo); p_label=f'p < {1/len(placebo):.5f}' if extreme==0 else f'p={p:.3f}'
h.to_csv(TAB/'B_匹配DID逐案例.csv',index=False,encoding='utf-8-sig'); prof.to_csv(TAB/'B_主场事件窗口.csv',index=False,encoding='utf-8-sig')
summary={'matched_did_mean_pp':estimate,'bootstrap_ci95':[float(ci[0]),float(ci[1])],'randomization_extreme_count':extreme,'randomization_draws':len(placebo),'randomization_p_upper_bound':float(1/len(placebo)) if extreme==0 else float(p),'randomization_p_label':p_label,'cases':len(h),'mean_pretrend_gap_pp':float(h.pretrend_gap_pp.mean())}
(TAB/'B_主场准实验摘要.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')

fig,axes=plt.subplots(1,3,figsize=(16,5.7),gridspec_kw={'width_ratios':[1.1,1.15,1]})
hh=h.sort_values('did_pp'); axes[0].barh(hh.NOC+' '+hh.Year.astype(str),hh.did_pp,color=[P['red'] if x<0 else P['teal'] for x in hh.did_pp]); axes[0].axvline(0,color='#263238',lw=.8); axes[0].set_xlabel('匹配DID（百分点）'); axes[0].set_title('逐案例：主办国变化减匹配组变化',loc='left',fontweight='bold')
for i,v in enumerate(hh.did_pp): axes[0].text(v+(.07 if v>=0 else -.07),i,f'{v:+.2f}',va='center',ha='left' if v>=0 else 'right',fontsize=8)
avg=prof.groupby('k')[['host_share','control_share']].mean(); base=avg.loc[-1]
axes[1].plot(avg.index,avg.host_share-base.host_share,marker='o',lw=2.5,color=P['red'],label='主办国'); axes[1].plot(avg.index,avg.control_share-base.control_share,marker='o',lw=2.5,color=P['teal'],label='匹配组'); axes[1].axvline(0,color=P['gold'],ls='--'); axes[1].axhline(0,color=P['grid']); axes[1].set_xticks(avg.index,[f'{x:+d}' for x in avg.index]); axes[1].set_xlabel('相对主办届的届次'); axes[1].set_ylabel('相对前一届的份额变化（百分点）'); axes[1].legend(frameon=False); axes[1].set_title('事件窗口：主办届出现分化',loc='left',fontweight='bold')
axes[2].hist(placebo,bins=45,color=P['teal'],alpha=.75); axes[2].axvline(estimate,color=P['red'],lw=3,label=f'观测均值 {estimate:.2f}pp'); axes[2].axvline(-estimate,color=P['red'],lw=1,ls=':'); axes[2].legend(frameon=False); axes[2].set_xlabel('随机指派下的平均效应'); axes[2].set_title(f'安慰剂检验：{p_label}',loc='left',fontweight='bold')
fig.suptitle('B 准实验升级：匹配DID、前趋势窗口与随机化安慰剂',fontsize=20,fontweight='bold',x=.04,ha='left')
fig.text(.04,.015,f'九个现代案例；平均匹配DID={estimate:.2f}pp，案例自助法95%CI [{ci[0]:.2f}, {ci[1]:.2f}]。主办权并非随机，结果是准实验关联证据，不作无条件因果外推。',fontsize=8.5,color=P['grey'])
fig.savefig(FIG/'B_主场效应准实验检验.png',bbox_inches='tight',dpi=220); plt.close(fig)

# Multi-filter offline dashboard dataset.
agg=d.groupby(['Year','NOC','Sex','sport_family'],dropna=False).agg(records=('source_row','size'),medals=('is_medal','sum')).reset_index()
agg['Year']=agg.Year.astype(int); agg['records']=agg.records.astype(int); agg['medals']=agg.medals.astype(int)
rows=agg.to_dict('records'); payload=json.dumps(rows,ensure_ascii=False,separators=(',',':'))
html=r'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>百年圣火 · 多维交互看板</title><style>
:root{--paper:#f7f3eb;--ink:#172a30;--teal:#247487;--red:#a64155;--gold:#c4903d;--line:#d9dedc}*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Microsoft YaHei",sans-serif}header{padding:28px 5vw 18px;border-bottom:1px solid var(--line)}h1{font-size:clamp(32px,5vw,64px);margin:0;letter-spacing:-2px}.wrap{padding:24px 5vw 60px}.filters{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.field label{display:block;font-size:12px;color:#66777d;margin:0 0 5px}.field select{width:100%;padding:10px;border:1px solid var(--line);border-radius:10px;background:white}.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin:18px 0}.card{padding:16px;border:1px solid var(--line);border-radius:14px;background:#fff9}.big{font-size:28px;font-weight:800;color:var(--teal)}#chart{width:100%;height:390px;border:1px solid var(--line);border-radius:16px;background:#fff9}.actions{display:flex;justify-content:space-between;align-items:center;margin:16px 0}.actions button{border:0;border-radius:999px;background:var(--ink);color:white;padding:10px 16px;cursor:pointer}table{width:100%;border-collapse:collapse;background:#fff7}th,td{padding:9px;border-bottom:1px solid var(--line);text-align:right}th:first-child,td:first-child{text-align:left}@media(max-width:900px){.filters,.cards{grid-template-columns:1fr 1fr}}@media(max-width:600px){.filters,.cards{grid-template-columns:1fr}}</style></head><body><header><div style="color:var(--gold);font-weight:800">晓组织 · 燕山大学</div><h1>百年圣火</h1><p>届次、代表团、性别、运动大类与指标五维联动。数据在本地浏览器内计算，不上传。</p></header><main class="wrap"><section class="filters"><div class="field"><label>届次</label><select id="year"></select></div><div class="field"><label>代表团</label><select id="noc"></select></div><div class="field"><label>性别</label><select id="sex"></select></div><div class="field"><label>运动大类</label><select id="sport"></select></div><div class="field"><label>指标</label><select id="metric"><option value="records">参赛记录</option><option value="medals">奖牌记录</option></select></div></section><section class="cards"><div class="card"><small>筛选后记录</small><div class="big" id="total"></div></div><div class="card"><small>涉及代表团</small><div class="big" id="nocs"></div></div><div class="card"><small>女性占比</small><div class="big" id="female"></div></div><div class="card"><small>领先代表团</small><div class="big" id="leader"></div></div></section><div class="actions"><strong id="title"></strong><button id="download">导出当前结果 CSV</button></div><svg id="chart" viewBox="0 0 1100 390" preserveAspectRatio="none"></svg><table><thead><tr><th>代表团</th><th>参赛记录</th><th>奖牌记录</th><th>女性参赛占比</th></tr></thead><tbody id="body"></tbody></table></main><script>const raw=__DATA__;const $=id=>document.getElementById(id);function opts(id,vals,all='全部'){let e=$(id);e.innerHTML='<option value="">'+all+'</option>'+vals.map(x=>`<option>${x}</option>`).join('')}opts('year',[...new Set(raw.map(x=>x.Year))].sort((a,b)=>a-b),'全部届次');opts('noc',[...new Set(raw.map(x=>x.NOC))].sort(),'全部代表团');opts('sex',[...new Set(raw.map(x=>x.Sex))].sort(),'全部性别');opts('sport',[...new Set(raw.map(x=>x.sport_family))].sort(),'全部运动大类');
function filtered(){return raw.filter(r=>(!year.value||r.Year==year.value)&&(!noc.value||r.NOC==noc.value)&&(!sex.value||r.Sex==sex.value)&&(!sport.value||r.sport_family==sport.value))}function group(a,key){let o={};for(const r of a)o[r[key]]=(o[r[key]]||0)+r[metric.value];return o}function render(){let a=filtered(),val=a.reduce((s,r)=>s+r[metric.value],0),ns=new Set(a.map(r=>r.NOC));total.textContent=val.toLocaleString();nocs.textContent=ns.size;let rec=a.reduce((s,r)=>s+r.records,0),f=a.filter(r=>r.Sex==='F').reduce((s,r)=>s+r.records,0);female.textContent=rec?(f/rec*100).toFixed(1)+'%':'—';let gn=group(a,'NOC'),rank=Object.entries(gn).sort((a,b)=>b[1]-a[1]);leader.textContent=rank[0]?.[0]||'—';let by,mode;if(year.value){by=rank.slice(0,15);mode='bar';title.textContent=year.value+'年代表团排名'}else{by=Object.entries(group(a,'Year')).sort((a,b)=>+a[0]-+b[0]);mode='line';title.textContent='历史趋势'}draw(by,mode);let rows={};for(const r of a){let z=rows[r.NOC]??={records:0,medals:0,f:0};z.records+=r.records;z.medals+=r.medals;if(r.Sex==='F')z.f+=r.records}body.innerHTML=Object.entries(rows).sort((a,b)=>b[1][metric.value]-a[1][metric.value]).slice(0,20).map(([k,v])=>`<tr><td>${k}</td><td>${v.records.toLocaleString()}</td><td>${v.medals.toLocaleString()}</td><td>${v.records?(v.f/v.records*100).toFixed(1)+'%':'—'}</td></tr>`).join('');window.current=a}
const year=$('year'),noc=$('noc'),sex=$('sex'),sport=$('sport'),metric=$('metric'),total=$('total'),nocs=$('nocs'),female=$('female'),leader=$('leader'),title=$('title'),body=$('body'),download=$('download');
function draw(a,mode){const svg=$('chart');if(!a.length){svg.innerHTML='';return}let max=Math.max(...a.map(x=>x[1]))||1;if(mode==='line'){let pts=a.map((x,i)=>[45+i*(1010/Math.max(1,a.length-1)),340-x[1]/max*285]);let p=pts.map((x,i)=>(i?'L':'M')+x.join(',')).join(' ');svg.innerHTML=`<path d="${p}" fill="none" stroke="#247487" stroke-width="4"/>`+pts.map((p,i)=>`<circle cx="${p[0]}" cy="${p[1]}" r="5" fill="#a64155"><title>${a[i][0]}: ${a[i][1]}</title></circle>`).join('')}else{let bw=980/a.length*.7;svg.innerHTML=a.map((x,i)=>{let h=x[1]/max*285,xx=55+i*(980/a.length),yy=340-h;return `<rect x="${xx}" y="${yy}" width="${bw}" height="${h}" fill="#247487"><title>${x[0]}: ${x[1]}</title></rect><text x="${xx+bw/2}" y="365" text-anchor="middle" font-size="12" fill="#172a30">${x[0]}</text>`}).join('')}}
for(const id of ['year','noc','sex','sport','metric'])$(id).onchange=render;download.onclick=()=>{let cols=['Year','NOC','Sex','sport_family','records','medals'],csv=[cols.join(','),...current.map(r=>cols.map(c=>'"'+String(r[c]).replaceAll('"','""')+'"').join(','))].join('\n');let b=new Blob(['\ufeff'+csv],{type:'text/csv'}),u=URL.createObjectURL(b),a=document.createElement('a');a.href=u;a.download='筛选结果.csv';a.click();URL.revokeObjectURL(u)};render();</script></body></html>'''.replace('__DATA__',payload)
assert set(agg.sport_family.dropna()) <= SPORT_ZH.keys(), '发现尚未翻译的运动大类'
assert set(agg.NOC.dropna()) <= NOC_ZH.keys(), '发现尚未翻译的代表团代码'
localization = f"const sportZh={json.dumps(SPORT_ZH,ensure_ascii=False,separators=(',',':'))},nocZh={json.dumps(NOC_ZH,ensure_ascii=False,separators=(',',':'))};const displayNoc=k=>nocZh[k]||k;"
html=html.replace('const $=id=>', localization+'const $=id=>')
html=html.replace('`<option>${x}</option>`','`<option value="${x}">${id===\'noc\'?displayNoc(x):id===\'sport\'?(sportZh[x]||x):id===\'sex\'?(x===\'F\'?\'女性\':\'男性\'):x}</option>`')
html=html.replace("leader.textContent=rank[0]?.[0]||'—'", "leader.textContent=rank[0]?displayNoc(rank[0][0]):'—'")
html=html.replace('<tr><td>${k}</td><td>${v.records.toLocaleString()}', '<tr><td><span title="${k}">${displayNoc(k)}</span></td><td>${v.records.toLocaleString()}')
html=html.replace('<title>${x[0]}: ${x[1]}</title>', '<title>${displayNoc(x[0])}: ${x[1]}</title>')
html=html.replace('<text x="${xx+bw/2}" y="365" text-anchor="middle" font-size="12" fill="#172a30">${x[0]}</text>', '<text x="${xx+bw/2}" y="358" transform="rotate(-35 ${xx+bw/2} 358)" text-anchor="end" font-size="12" fill="#172a30">${displayNoc(x[0])}</text>')
html=html.replace('viewBox="0 0 1100 390"', 'viewBox="0 0 1100 440"')
html=html.replace('#chart{width:100%;height:390px;', '#chart{width:100%;height:440px;')
(DASH/'index.html').write_text(html,encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2)); print('dashboard rows',len(rows))
