from pathlib import Path
import json, shutil
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务四_开放创作'
PRED=TASK/'02_2028洛杉矶预测'; NEWS=TASK/'03_数据新闻'; UPG=TASK/'05_满分升级'
UPG.mkdir(parents=True,exist_ok=True)

# 1. 项目级机器学习：同一套运动员行代理口径，按代表团×体育大类×届次建模。
cube=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'99_运行生成'/'analysis_cube.csv')
med=cube[cube.Medal.ne('No medal')].groupby(['Year','NOC','sport_family'],as_index=False).records.sum()
years=[2000,2004,2008,2012,2016,2020,2024]
nocs=med[med.Year>=2000].groupby('NOC').records.sum().nlargest(100).index
sports=med[med.Year>=2000].groupby('sport_family').records.sum().nlargest(45).index
idx=pd.MultiIndex.from_product([years,nocs,sports],names=['Year','NOC','sport_family'])
panel=med.set_index(['Year','NOC','sport_family']).reindex(idx,fill_value=0).reset_index()
panel['lag1']=panel.groupby(['NOC','sport_family']).records.shift(1)
panel['lag2']=panel.groupby(['NOC','sport_family']).records.shift(2)
panel['trend']=panel.lag1-panel.lag2
panel['noc_lag']=panel.groupby(['NOC','Year']).lag1.transform('sum')
panel['sport_lag']=panel.groupby(['sport_family','Year']).lag1.transform('sum')
panel=panel.dropna().copy()
X=pd.get_dummies(panel[['NOC','sport_family','lag1','lag2','trend','noc_lag','sport_lag']],columns=['NOC','sport_family'])
y=panel.records
train=panel.Year<2024; test=panel.Year.eq(2024)
rf=RandomForestRegressor(n_estimators=280,min_samples_leaf=3,max_features=.65,random_state=28,n_jobs=-1)
gb=GradientBoostingRegressor(n_estimators=220,max_depth=2,learning_rate=.035,loss='huber',random_state=28)
rf.fit(X[train],y[train]); gb.fit(X[train],y[train])
pred24=.6*rf.predict(X[test])+.4*gb.predict(X[test])
mae_project=float(mean_absolute_error(y[test],pred24))
# 在代表团总奖牌行口径下比较，避免将项目格误差与总量误差直接并列。
check=panel.loc[test,['NOC','sport_family','records','lag1']].copy()
check['ml_pred']=np.maximum(0,pred24)
same=check.groupby('NOC',as_index=False).agg(actual_rows=('records','sum'),ml_pred_rows=('ml_pred','sum'),last_edition_rows=('lag1','sum'))
same['ml_abs_error']=(same.actual_rows-same.ml_pred_rows).abs()
same['last_edition_abs_error']=(same.actual_rows-same.last_edition_rows).abs()
same.to_csv(UPG/'2024同单位逐队回测.csv',index=False,encoding='utf-8-sig')
same_summary={'观察单位':'代表团奖牌运动员行','留出届次':2024,'代表团数':len(same),'项目格MAE':mae_project,
              '机器学习逐队总量MAE':float(same.ml_abs_error.mean()),'上一届持平逐队总量MAE':float(same.last_edition_abs_error.mean()),
              '实际不少于5行的机器学习MAE':float(same.loc[same.actual_rows.ge(5),'ml_abs_error'].mean()),
              '实际不少于5行的上一届持平MAE':float(same.loc[same.actual_rows.ge(5),'last_edition_abs_error'].mean())}
pd.DataFrame([same_summary]).to_csv(UPG/'2024同单位回测摘要.csv',index=False,encoding='utf-8-sig')

# 2028 features use 2024 and 2020 as lags.
p24=panel[panel.Year.eq(2024)].copy(); X28=X.loc[test].copy()
for c in ['lag2','lag1']:
    pass
X28['lag2']=p24.lag1.values; X28['lag1']=p24.records.values
X28['trend']=X28.lag1-X28.lag2
X28['noc_lag']=p24.groupby('NOC').records.transform('sum').values
X28['sport_lag']=p24.groupby('sport_family').records.transform('sum').values
# 留出验证结束后，正式预测使用截至2024年的全部可用训练样本。
rf.fit(X,y); gb.fit(X,y)
p24['ml2028']=np.maximum(0,.6*rf.predict(X28)+.4*gb.predict(X28))
sport_pred=p24.groupby(['NOC','sport_family'],as_index=False).ml2028.sum()
noc_ml=sport_pred.groupby('NOC').ml2028.sum()

# 2. 新增项目权威信号快照。分数为男女排名的倒数归一化组合；缺少统一国家排名的壁球采用顶尖运动员国家分布代理。
rows=[]
def add(sport, source, date, ranks):
    for noc,rm,rw in ranks: rows.append([sport,noc,rm,rw,(1/(rm or 40)+1/(rw or 40))/2,source,date])
add('板球T20','ICC男女T20I国家队排名','2026-11-01',[('GBR',1,2),('IND',2,3),('AUS',3,1),('NZL',4,4),('RSA',5,5),('USA',13,25)])
add('棒球/垒球','WBSC/KONAMI世界排名与最近世界赛','2026快照',[('JPN',1,2),('USA',4,1),('MEX',3,8),('CAN',8,5),('TPE',2,3),('ITA',14,6)])
add('腰旗橄榄球','IFAF世界排名及2026世界锦标赛','2026-08',[('USA',1,2),('CAN',2,1),('MEX',4,3),('JPN',5,5),('GBR',6,4),('ITA',3,8)])
add('长曲棍球六人制','World Lacrosse Sixes世界排名','2026快照',[('USA',2,1),('CAN',1,2),('JPN',3,4),('GBR',4,5),('AUS',6,3),('CHN',20,8)])
add('壁球','PSA个人排名国家分布代理','2026快照',[('EGY',1,1),('GBR',4,3),('USA',12,5),('NZL',3,15),('BEL',18,2),('MAS',10,8)])
ranking=pd.DataFrame(rows,columns=['新增运动','NOC','男子排名','女子排名','排名信号','一手来源','快照日期'])
ranking.to_csv(UPG/'新增项目权威排名特征.csv',index=False,encoding='utf-8-sig')
bonus=ranking.groupby('NOC')['排名信号'].sum(); bonus=bonus/bonus.sum()*24

# 3. 合成对照式主场估计：以前两届走势匹配非主办国，使用最近邻加权构造反事实。
tot=med.groupby(['Year','NOC']).records.sum().unstack(fill_value=0)
hosts={2000:'AUS',2004:'GRE',2008:'CHN',2012:'GBR',2016:'BRA',2020:'JPN',2024:'FRA'}
effects=[]
for yr,h in hosts.items():
    pos=years.index(yr)
    if pos<2 or h not in tot.columns: continue
    prev=years[pos-2:pos]
    hv=tot.loc[prev,h].values.astype(float)
    donors=[]
    for d in tot.columns:
        if d==h or d in hosts.values(): continue
        dv=tot.loc[prev,d].values.astype(float)
        dist=np.sqrt(np.mean(((dv-hv)/(hv+5))**2))
        donors.append((dist,d))
    near=sorted(donors)[:8]; w=np.array([1/(x[0]+.05) for x in near]); w/=w.sum()
    cf=sum(wi*tot.loc[yr,d] for wi,(_,d) in zip(w,near))
    actual=float(tot.loc[yr,h]); effects.append([yr,h,actual,cf,actual-cf,(actual-cf)/(cf+1)])
host=pd.DataFrame(effects,columns=['Year','Host','Actual','Synthetic','Effect','EffectRate'])
host.to_csv(UPG/'主场效应合成对照.csv',index=False,encoding='utf-8-sig')
host_rate=float(np.clip(host.EffectRate.median(),0,.18))

# 4. 三模型集成：透明基线45% + 项目级RF/GB模型45% + 新增项目排名10%，保持353枚金牌对应的总奖牌池。
base=pd.read_csv(PRED/'LA2028奖牌预测完整榜.csv')
base=base.set_index('NOC'); ml=noc_ml.reindex(base.index).fillna(0)
if ml.sum()>0: ml=ml/ml.sum()*base.forecast_total_programme.sum()
rank_adj=bonus.reindex(base.index).fillna(0)
raw=.45*base.forecast_total_neutral+.45*ml+.10*(base.forecast_total_neutral+rank_adj)
raw.loc['USA']*=1+host_rate*.55  # 因果证据存在分歧，收缩45%。
ens=raw/raw.sum()*base.forecast_total_programme.sum()
out=base.copy(); out['ml_project_forecast']=ml; out['new_sport_ranking_bonus']=rank_adj
out['synthetic_control_host_rate']=host_rate; out['ensemble_total']=ens
out['ensemble_rank']=out.ensemble_total.rank(method='min',ascending=False).astype(int)
out=out.reset_index().sort_values('ensemble_rank')
out.to_csv(PRED/'LA2028机器学习集成预测榜.csv',index=False,encoding='utf-8-sig')
sport_pred.to_csv(PRED/'代表团_项目级预测.csv',index=False,encoding='utf-8-sig')
pd.DataFrame([{'项目级2024回测MAE':mae_project,'2024逐队总量MAE_运动员行':same_summary['机器学习逐队总量MAE'],'2024上一届持平MAE_运动员行':same_summary['上一届持平逐队总量MAE'],'合成对照主场效应中位数':host_rate,'模型':'45%透明基线+45%RF/GB项目模型+10%新增项目排名','验证边界':'最终跨口径集成尚无完整历史回测；预测前项目模型已用截至2024数据重训'}]).to_csv(UPG/'升级模型验证摘要.csv',index=False,encoding='utf-8-sig')

top=out.head(18)[['NOC','ensemble_total','ensemble_rank','lower80','upper80']].round(2).to_dict('records')
rank_top=ranking.sort_values(['新增运动','排名信号'],ascending=[True,False]).to_dict('records')
data=json.dumps({'top':top,'ranking':rank_top,'host':host.round(3).to_dict('records'),'project_mae':round(mae_project,3),'host_rate':round(host_rate,3)},ensure_ascii=False)

# 5. 滚动叙事、情景动画与地图联动（静态单文件，可离线、可部署）。
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>洛杉矶之前，我们能知道什么｜晓组织</title><style>
:root{{--bg:#f4f0e6;--ink:#10282e;--cyan:#19778a;--gold:#c98c2c;--red:#ad4058;--line:#ccd6d3}}*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:var(--bg);color:var(--ink);font-family:"Microsoft YaHei",sans-serif}}nav{{position:fixed;z-index:8;top:0;width:100%;display:flex;justify-content:space-between;padding:14px 5vw;background:#f4f0e6e8;backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}}nav a{{color:var(--ink);text-decoration:none;margin-left:18px}}header,.章{{min-height:100vh;padding:14vh 7vw 9vh;border-bottom:1px solid var(--line)}}h1{{font-size:clamp(60px,10vw,150px);line-height:.88;letter-spacing:-.07em;margin:.22em 0}}h2{{font-size:clamp(38px,6vw,88px);line-height:1.03;max-width:1100px}}.导语{{font-size:clamp(18px,2vw,28px);line-height:1.8;max-width:900px}}.眉{{color:var(--gold);font-weight:900;letter-spacing:.12em}}.网格{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.卡{{border:1px solid var(--line);border-radius:18px;padding:20px;background:#fff8}}.数{{font-size:52px;font-weight:900;color:var(--cyan)}}.图{{min-height:360px;margin-top:30px}}.条{{display:grid;grid-template-columns:60px 60px 1fr 80px;gap:12px;align-items:center;padding:9px 0}}.轨{{height:14px;background:#dfe6e3;border-radius:8px;overflow:hidden}}.填{{height:100%;background:var(--cyan);transition:width 1s cubic-bezier(.2,.8,.2,1)}}.显现{{opacity:0;transform:translateY(45px);transition:.8s}}.显现.进入{{opacity:1;transform:none}}svg{{width:100%;height:auto}}.点{{fill:var(--cyan);opacity:.78;cursor:pointer;transition:.3s}}.点:hover{{fill:var(--red);opacity:1}}.提示{{font-size:16px;font-weight:800}}table{{width:100%;border-collapse:collapse;background:#fff8}}th,td{{padding:11px;border-bottom:1px solid var(--line);text-align:left}}footer{{padding:60px 7vw}}@media(max-width:800px){{.网格{{grid-template-columns:1fr}}nav span{{display:none}}.条{{grid-template-columns:38px 48px 1fr 55px}}}}
</style></head><body><nav><b>晓组织 · 洛杉矶2028</b><span><a href="#预测">预测</a><a href="#新增">新增项目</a><a href="#主场">主场效应</a><a href="#验证">如何验证</a></span></nav><header><div class="眉">任务四 · 数据新闻升级版</div><h1>未来不是<br>一张确定榜单</h1><p class="导语">我们把历史奖牌、项目级机器学习、五项新增运动的国际排名与主场合成对照放进同一个可检验框架。历史证据可核对，未经核验的新增项目排名另设关闭情景。</p></header>
<section class="章 显现" id="预测"><div class="眉">01 · 三模型集成</div><h2>从代表团总量，下钻到体育项目</h2><div class="网格"><div class="卡"><div class="数">45%</div>透明历史基线</div><div class="卡"><div class="数">45%</div>项目级随机森林与梯度提升</div><div class="卡"><div class="数">10%</div>新增项目排名情景信号</div></div><div id="榜" class="图"></div></section>
<section class="章 显现" id="新增"><div class="眉">02 · 五项新增运动</div><h2>五项运动的排名如何影响预测？</h2><p class="导语">板球、棒垒球、腰旗橄榄球、长曲棍球六人制和壁球以国际单项组织排名方向构建待核情景代理。地图点击代表团，可查看它在新增项目中的信号。</p><div class="图"><svg viewBox="0 0 1000 460" aria-label="新增项目竞争力地图"><path d="M80 155L180 85 300 110 330 210 250 270 145 235ZM430 95L520 70 610 110 655 190 590 245 485 220ZM650 105L795 90 915 160 880 260 740 285 650 215ZM480 285L590 275 630 385 515 420 440 355Z" fill="#dde4df" stroke="#bcc9c5"/></svg><div id="提示" class="卡">将鼠标移到圆点上查看代表团。</div></div></section>
<section class="章 显现" id="主场"><div class="眉">03 · 主场效应</div><h2>用合成对照替代固定加成</h2><p class="导语">对每一届主办国，用赛前两届走势最相近的非主办国加权构造反事实。研究文献提示主场效应在加入社会经济控制后可能减弱，因此模型只采用历史中位数的55%。</p><div id="主场图" class="图"></div></section>
<section class="章 显现" id="验证"><div class="眉">04 · 公开验证协议</div><h2>2028年以后，模型必须接受考试</h2><div class="网格"><div class="卡"><b>总量</b><p>平均绝对误差、均方根误差。</p></div><div class="卡"><b>排序</b><p>斯皮尔曼等级相关与前十命中。</p></div><div class="卡"><b>区间</b><p>80%区间覆盖率是否接近80%。</p></div></div><p class="导语">当前项目级2024留出回测MAE：<b>{mae_project:.2f}</b>（代表团×体育大类的运动员行代理单位）。</p><p><a href="../02_2028洛杉矶预测/预测方法与验证方案.md">查看完整方法</a> · <a href="../01_交互式Dashboard/index.html">进入预测看板</a></p></section><footer>数据快照：2026年11月。团队：晓组织，燕山大学，张子涵60%，陈旭40%。</footer>
<script>const D={data};const榜=document.querySelector('#榜'),mx=Math.max(...D.top.map(x=>x.ensemble_total));榜.innerHTML=D.top.map(x=>`<div class="条"><b>${{x.ensemble_rank}}</b><b>${{x.NOC}}</b><div class="轨"><div class="填" style="width:0" data-w="${{x.ensemble_total/mx*100}}"></div></div><b>${{x.ensemble_total.toFixed(1)}}</b></div>`).join('');
const obs=new IntersectionObserver(es=>es.forEach(e=>{{if(e.isIntersecting){{e.target.classList.add('进入');e.target.querySelectorAll('.填').forEach(x=>x.style.width=x.dataset.w+'%')}}}}),{{threshold:.18}});document.querySelectorAll('.显现').forEach(x=>obs.observe(x));
const pos={{USA:[170,175],CAN:[170,130],MEX:[175,225],GBR:[500,130],EGY:[555,225],IND:[705,215],JPN:[865,185],AUS:[835,355],NZL:[915,390],CHN:[790,185],TPE:[835,210],ITA:[535,160]}};const svg=document.querySelector('svg'),ns='http://www.w3.org/2000/svg';for(const [n,p] of Object.entries(pos)){{let c=document.createElementNS(ns,'circle'),score=D.ranking.filter(x=>x.NOC===n).reduce((s,x)=>s+x['排名信号'],0);c.setAttribute('cx',p[0]);c.setAttribute('cy',p[1]);c.setAttribute('r',Math.min(24,8+Math.sqrt(score)*18));c.setAttribute('class','点');c.onmouseenter=()=>{{let a=D.ranking.filter(x=>x.NOC===n).sort((a,b)=>b['排名信号']-a['排名信号']).slice(0,3);提示.innerHTML='<b>'+n+'</b><br>'+a.map(x=>x['新增运动']+'：男'+x['男子排名']+' / 女'+x['女子排名']).join('<br>')}};svg.appendChild(c)}}
主场图.innerHTML='<table><tr><th>届次</th><th>主办国</th><th>实际</th><th>合成反事实</th><th>差异</th></tr>'+D.host.map(x=>`<tr><td>${{x.Year}}</td><td>${{x.Host}}</td><td>${{x.Actual}}</td><td>${{x.Synthetic}}</td><td>${{x.Effect>0?'+':''}}${{x.Effect}}</td></tr>`).join('')+'</table>';</script></body></html>'''
from task2_localization import NOC_ZH
html=html.replace('../02_2028洛杉矶预测/预测方法与验证方案.md','../02_2028洛杉矶预测/index.html')
assert set(out.NOC) <= NOC_ZH.keys()
assert set(ranking.NOC) <= NOC_ZH.keys()
assert set(host.Host) <= NOC_ZH.keys()
html=html.replace('五项运动的排名如何影响预测？','新增项目的优势，还需验证')
html=html.replace('地图点击代表团，可查看它在新增项目中的信号。','选择运动，比较各代表团的排名信号；当前排名数值为待核情景输入；点击运动可查看假设。')
old='<div class="图"><svg viewBox="0 0 1000 460" aria-label="新增项目竞争力地图"><path d="M80 155L180 85 300 110 330 210 250 270 145 235ZM430 95L520 70 610 110 655 190 590 245 485 220ZM650 105L795 90 915 160 880 260 740 285 650 215ZM480 285L590 275 630 385 515 420 440 355Z" fill="#dde4df" stroke="#bcc9c5"/></svg><div id="提示" class="卡">将鼠标移到圆点上查看代表团。</div></div>'
new='''<div class="sport-explorer"><div class="sport-tabs" id="sport-tabs" role="tablist" aria-label="新增运动"></div><div class="sport-stage"><div class="sport-intro"><span class="sport-overline">新增运动 · 排名信号</span><h3 id="sport-title"></h3><p id="sport-caption"></p><div class="sport-source" id="sport-source"></div></div><div class="sport-ranks" id="sport-ranks" aria-live="polite"></div></div><p class="sport-footnote">条形长度表示本作品使用的归一化排名信号，不是预测奖牌数。点击运动可切换对比。</p></div>'''
assert old in html
html=html.replace(old,new)
old_js="const pos={USA:[170,175]"
start=html.index(old_js)
end=html.index('</script>',start)
new_js='''const nocZh=__NOC_ZH__,nameOf=k=>nocZh[k]||k;
const sports=[...new Set(D.ranking.map(x=>x['新增运动']))],tabs=document.querySelector('#sport-tabs');
tabs.innerHTML=sports.map((x,i)=>`<button type="button" role="tab" data-index="${i}" aria-selected="${i===0}"><small>0${i+1}</small>${x}</button>`).join('');
function showSport(i){const sport=sports[i],rows=D.ranking.filter(x=>x['新增运动']===sport).sort((a,b)=>b['排名信号']-a['排名信号']),max=Math.max(1e-9,...rows.map(x=>x['排名信号']));document.querySelector('#sport-title').textContent=sport;document.querySelector('#sport-caption').textContent=`${rows.length} 个代表团进入此项排名快照。按归一化信号排序，可查看男、女排名依据。`;document.querySelector('#sport-source').textContent=`来源：${rows[0]?.['一手来源']||'单项组织排名'}　快照：${rows[0]?.['快照日期']||'见数据表'}`;document.querySelector('#sport-ranks').innerHTML=rows.map((x,j)=>`<div class="sport-row"><span class="sport-place">${String(j+1).padStart(2,'0')}</span><div class="sport-name"><strong>${nameOf(x.NOC)}</strong><small>男 ${x['男子排名']} · 女 ${x['女子排名']}</small></div><div class="sport-track"><i style="width:${x['排名信号']/max*100}%"></i></div><b>${Number(x['排名信号']).toFixed(2)}</b></div>`).join('');tabs.querySelectorAll('button').forEach((b,j)=>b.setAttribute('aria-selected',String(i===j)))}
tabs.onclick=e=>{const b=e.target.closest('button[data-index]');if(b)showSport(+b.dataset.index)};showSport(0);
document.querySelectorAll('#榜 .条>b:nth-child(2)').forEach((e,i)=>{e.textContent=nameOf(D.top[i].NOC);e.title=D.top[i].NOC});
主场图.innerHTML='<table><tr><th>届次</th><th>主办代表团</th><th>实际奖牌记录</th><th>合成对照</th><th>差异</th></tr>'+D.host.map(x=>`<tr><td>${x.Year}</td><td><strong>${nameOf(x.Host)}</strong></td><td>${x.Actual}</td><td>${x.Synthetic}</td><td>${x.Effect>0?'+':''}${x.Effect}</td></tr>`).join('')+'</table>';'''.replace('__NOC_ZH__',json.dumps(NOC_ZH,ensure_ascii=False,separators=(',',':')))
html=html[:start]+new_js+html[end:]
css='''<style id="sport-explorer-style">.sport-explorer{margin-top:38px}.sport-tabs{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px}.sport-tabs button{border:1px solid var(--line);background:#fff9;color:var(--ink);padding:12px 18px;border-radius:100px;cursor:pointer;font-weight:800}.sport-tabs button small{color:var(--gold);margin-right:9px}.sport-tabs button[aria-selected=true]{background:var(--ink);color:#fff}.sport-stage{display:grid;grid-template-columns:minmax(250px,.75fr) minmax(450px,1.25fr);gap:30px;padding:35px;border:1px solid var(--line);border-radius:26px;background:linear-gradient(125deg,#113139,#173f46);color:#eaf5ef;box-shadow:0 30px 70px -50px #122d39}.sport-overline{color:#e3ad67;font-size:13px;letter-spacing:.14em;font-weight:900}.sport-intro h3{font-size:clamp(46px,5vw,78px);line-height:1.08;margin:26px 0 18px}.sport-intro p{color:#c3dbd7;line-height:1.8;max-width:330px}.sport-source{border-top:1px solid #ffffff38;margin-top:45px;padding-top:17px;color:#bfd4d0;font-size:13px;line-height:1.8}.sport-ranks{display:grid;align-content:center}.sport-row{display:grid;grid-template-columns:34px minmax(115px,160px) 1fr 42px;gap:12px;align-items:center;padding:13px 0;border-bottom:1px solid #ffffff29}.sport-row:last-child{border-bottom:0}.sport-place{color:#e3ad67;font-size:13px;font-weight:800}.sport-name strong{display:block;font-size:16px}.sport-name small{color:#b9d4d1;font-size:11px}.sport-track{height:10px;border-radius:9px;background:#ffffff29;overflow:hidden}.sport-track i{display:block;height:100%;border-radius:9px;background:linear-gradient(90deg,#47aeb8,#a7ded1);transition:width .5s}.sport-row>b{font-size:15px;color:#bde9e0;text-align:right}.sport-footnote{font-size:13px;color:#687d7e;margin-top:14px!important}@media(max-width:850px){.sport-stage{grid-template-columns:1fr}.sport-source{margin-top:22px}}@media(max-width:520px){.sport-stage{padding:22px 15px}.sport-row{grid-template-columns:26px 100px 1fr 35px;gap:6px}.sport-row strong{font-size:13px}.sport-row small{font-size:9px}.sport-tabs button{padding:9px 12px;font-size:12px}}</style>'''
html=html.replace('</head>',css+'</head>',1)
audit_link='''<aside style="max-width:1120px;margin:42px auto;padding:24px;border:1px solid #b2c4bf;border-radius:20px;background:#eaf0e9;color:#173f46"><strong>预测来源复核更新</strong><p>五项新增运动的旧排名输入并非全部通过官方逐队核验。正式阅读请使用来源门控的审慎预测榜；2016新增运动完整公式类比回放也已公开。</p><a href="../05_满分升级/11_官方来源门控预测/index.html">查看审慎预测与来源门槛 ↗</a>　<a href="../05_满分升级/12_新增运动端到端类比回放/index.html">查看历史类比回放 ↗</a></aside>'''
if '预测来源复核更新' not in html:html=html.replace('</body>',audit_link+'</body>')
(NEWS/'index.html').write_text(html,encoding='utf-8')

method=(PRED/'预测方法与验证方案.md').read_text(encoding='utf-8')
method=method.split('\n\n## 满分升级：')[0]
method+='''\n\n## 满分升级：项目级机器学习与合成对照\n\n- 项目级模型以 `代表团×体育大类×届次` 为观察单位，输入包括前两届成绩、趋势、代表团整体强度和项目竞争规模。随机森林与梯度提升按 60%/40% 集成。\n- 2024作为完全留出届次检验，不参与训练。误差记录见 `05_满分升级/升级模型验证摘要.csv`。\n- 五项新增运动不再人工分配固定奖牌，而是把 ICC、WBSC、IFAF、World Lacrosse 与 PSA/WSF 竞技排名转成归一化信号。排名会变化；当前情景值缺少逐条官方榜单链接，不能视作已核验快照。\n- 主场效应采用近邻加权合成对照：用主办国赛前两届轨迹匹配8个非主办代表团，估计主办届实际值与反事实之差。考虑到主办权内生性和文献分歧，只使用历史中位估计的55%。这提高识别质量，但仍不宣称为随机实验因果效应。\n- 最终集成权重为：透明基线45%、项目级机器学习45%、新增项目排名信号10%。赛后固定使用MAE、RMSE、斯皮尔曼相关、前十命中与80%区间覆盖率验证。\n'''
method=method.replace('# 洛杉矶2028奖牌预测：方法、假设与验证\n', '# 洛杉矶2028奖牌预测：方法、假设与验证\n\n> 浏览器直接打开 `.md` 会显示源文本。正式阅读请打开同目录的 [预测方法中文网页](index.html)。本文件作为可复核底稿，分别记录早期历史基线与最终项目级集成模型。\n\n**口径提醒**：前半部分的“美国增加12枚”是早期可关闭的基线情景；最终集成模型采用下文的合成对照收缩调整。2.74枚是代表团总量回测MAE，项目级0.52是“代表团×运动大类”的运动员行代理误差，两者不能直接比较。80%区间来自历史基线回测残差，不应冒充集成模型的独立校准区间。\n',1)
method+='''\n\n### 同单位留出验证：强队反例\n\n将 2024 年项目级预测汇总到代表团的运动员获奖行总量，机器学习逐队 MAE 为 **%.2f 行**，上一届持平基线为 **%.2f 行**。在实际至少 5 行的代表团中，两者分别为 **%.2f 行**和 **%.2f 行**，机器学习没有胜出。详见 [同单位验证网页](../05_满分升级/2024同单位验证.html)。正式 2028 预测前，项目模型已在留出评分后用截至 2024 年的样本重训。最终跨口径集成仍缺端到端历史回测。\n''' % (same_summary['机器学习逐队总量MAE'],same_summary['上一届持平逐队总量MAE'],same_summary['实际不少于5行的机器学习MAE'],same_summary['实际不少于5行的上一届持平MAE'])
(PRED/'预测方法与验证方案.md').write_text(method,encoding='utf-8')

# 留出验证的同单位说明；明确展示强队子集的反例。
validation_md=f'''# 2024 留出验证：同单位比较

以 2024 年为留出届次，把项目级预测汇总到 100 个代表团的运动员获奖行总量，与“上一届持平”基线比较。

| 分组 | 项目级模型 MAE | 上一届持平 MAE |
|---|---:|---:|
| 全体代表团 | {same_summary['机器学习逐队总量MAE']:.2f} 行 | {same_summary['上一届持平逐队总量MAE']:.2f} 行 |
| 2024 实际至少 5 行 | {same_summary['实际不少于5行的机器学习MAE']:.2f} 行 | {same_summary['实际不少于5行的上一届持平MAE']:.2f} 行 |

全体代表团略有改进，但强队子集反而变差。逐队误差见 `2024同单位逐队回测.csv`。

**证据边界**：此处单位为运动员获奖行，不是官方小项奖牌。最终 2028 预测混合了官方小项基线、运动员行项目模型和新增运动排名信号，尚未完成同口径的端到端历史回测；其区间沿用基线历史残差，不能宣称集成模型达到 80% 实际覆盖率。模型在留出评分后用截至 2024 年的数据重训。候选代表团与项目用含 2024 年的数据筛选，留出结果可能有轻微前视偏差。
'''
(UPG/'2024同单位验证.md').write_text(validation_md,encoding='utf-8')
from html import escape
validation_html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>2024 同单位验证</title><style>body{{margin:0;background:#eee9df;color:#17253b;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:920px;margin:auto;padding:64px 24px 90px}}small{{letter-spacing:.2em;color:#9c4d35}}h1{{font-size:clamp(36px,6vw,64px);margin:12px 0 20px}}p{{line-height:1.8}}.grid{{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin:32px 0}}.card{{background:#fffaf2;border:1px solid #d8d0c1;border-radius:20px;padding:25px}}.num{{font:700 clamp(38px,6vw,60px) Georgia;color:#1b4479}}.warn{{background:#193453;color:#fff;padding:28px;border-radius:24px;margin-top:32px}}.warn p{{color:#e9e7dc}}a{{color:#2467a4}}@media(max-width:650px){{.grid{{grid-template-columns:1fr}}}}</style></head><body><main><small>洛杉矶 2028 / 模型证据</small><h1>同一个单位，<br>模型才有可比的成绩。</h1><p>以 2024 年为留出届次，比较项目级机器学习与“上一届持平”基线。两者都汇总到<strong>代表团运动员获奖行总量</strong>，涵盖 {len(same)} 个代表团。</p><div class="grid"><div class="card"><small>全体代表团 · 平均绝对误差</small><div class="num">{same_summary['机器学习逐队总量MAE']:.2f}</div><p>机器学习；上一届持平为 {same_summary['上一届持平逐队总量MAE']:.2f} 行。</p></div><div class="card"><small>实际至少 5 行 · 平均绝对误差</small><div class="num">{same_summary['实际不少于5行的机器学习MAE']:.2f}</div><p>机器学习；上一届持平为 {same_summary['实际不少于5行的上一届持平MAE']:.2f} 行。强队子集没有获得改进。</p></div></div><div class="warn"><h2>证据边界</h2><p>这不是官方小项奖牌数的回测。最终 2028 预测混合了官方小项基线、运动员行项目模型与新增运动信号，尚未完成同口径的端到端历史回测。基线历史残差生成的区间不能解释为最终集成模型已验证的覆盖率。</p><p>项目模型在留出评分后用截至 2024 年的样本重训。候选代表团和项目集合用含 2024 年的数据筛选，结果可能有轻微前视偏差。</p></div><p><a href="2024同单位逐队回测.csv">下载逐队误差表</a>　<a href="2024同单位回测摘要.csv">下载摘要</a>　<a href="../02_2028洛杉矶预测/index.html">返回预测方法</a></p></main></body></html>'''
(UPG/'2024同单位验证.html').write_text(validation_html,encoding='utf-8')

# 同步到可部署静态站点目录。
site=ROOT/'项目工作区'/'sites'/'la28-fullscore'; dist=site/'dist'
if dist.exists(): shutil.rmtree(dist)
shutil.copytree(TASK,dist)
(site/'.openai').mkdir(parents=True,exist_ok=True)
print(json.dumps({'project_mae':mae_project,'host_rate':host_rate,'rows':len(out),'site':str(site)},ensure_ascii=False,indent=2))
