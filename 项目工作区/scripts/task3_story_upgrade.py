from pathlib import Path
import json
import pandas as pd
from localize_s2_story_rank import localize_story_html

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'
TABLE=TASK/'02_数据表'; STORY=TASK/'06_滚动叙事专题'; STORY.mkdir(parents=True,exist_ok=True)
DATA=ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'归一数据_保留原始字段.csv.gz'
IOC={2008:'https://www.olympics.com/en/olympic-games/beijing-2008/results',2012:'https://www.olympics.com/en/olympic-games/london-2012/results',2016:'https://www.olympics.com/en/olympic-games/rio-2016/results'}
EXPECTED={2008:302,2012:302,2016:306}
d=pd.read_csv(DATA,low_memory=False); d=d[d.Year.isin(IOC)].copy()
d['Medal']=d.Medal.astype(str).str.title(); d=d[d.Medal.isin(['Gold','Silver','Bronze'])]
rows=[]; summary=[]
for year,url in IOC.items():
    y=d[d.Year.eq(year)].copy()
    # 每个NOC–Event–Medal只保留一条，团队成员不会重复制造小项奖牌。
    u=y[['Sport','Event','NOC','Medal']].drop_duplicates()
    wide=(u.groupby(['Sport','Event','Medal']).NOC.apply(lambda s:'|'.join(sorted(set(s.astype(str)))))
          .unstack('Medal').reset_index())
    for col in ['Gold','Silver','Bronze']:
        if col not in wide: wide[col]=''
    wide['Year']=year; wide['official_edition_results_url']=url
    wide['provenance']='主数据运动员记录去重代理；IOC届次链接仅供追溯；逐项证据见来源覆盖总表'
    wide['verification_scope']='完整小项结构与届次总量；历史重分配以IOC最新公告为准'
    wide=wide[['Year','Sport','Event','Gold','Silver','Bronze','official_edition_results_url','provenance','verification_scope']]
    wide.to_csv(TABLE/f'S2_{year}历史小项代理表.csv',index=False,encoding='utf-8-sig')
    summary.append({'Year':year,'event_rows':len(wide),'expected_program_events':EXPECTED[year],
                    'event_count_match':len(wide)==EXPECTED[year],'ioc_results_url':url,
                    'source_grade':'赛程小项总数对照 + 运动员行代理生成；未核现行IOC逐项奖牌'})
    rows.append(wide)
pd.DataFrame(summary).to_csv(TABLE/'S2_历史项目数量对照摘要.csv',index=False,encoding='utf-8-sig')

rank=pd.read_csv(TABLE/'S2_2024三口径完整排名.csv')
hist=pd.read_csv(TABLE/'S2_跨届稳定性摘要.csv')
payload=json.dumps(rank[['NOC','Gold','Silver','Bronze','rank','lens','lens_label']].to_dict('records'),ensure_ascii=False,separators=(',',':'))
hpayload=json.dumps(hist.to_dict('records'),ensure_ascii=False,separators=(',',':'))
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>口径的魔力｜奥运奖牌榜如何被统计单位重写</title><style>
:root{--paper:#f4f0e7;--ink:#14272d;--gold:#c69036;--red:#ad4058;--cyan:#58a8b4;--teal:#177487;--line:#ccd5d2}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font-family:"Microsoft YaHei",system-ui,sans-serif}nav{position:fixed;z-index:20;top:0;width:100%;display:flex;justify-content:space-between;padding:14px 5vw;background:#f4f0e7e8;backdrop-filter:blur(12px);border-bottom:1px solid #ccd5d288}nav a{color:inherit;text-decoration:none;font-size:13px}.hero{min-height:100vh;padding:15vh 6vw 8vh;display:grid;grid-template-columns:1.15fr .85fr;gap:4vw;align-items:center}.eyebrow{color:var(--gold);font-weight:800;letter-spacing:.18em}.hero h1{font-size:clamp(58px,9vw,132px);line-height:.88;margin:.18em 0}.hero p{font-size:clamp(18px,2vw,29px);max-width:760px}.triptych{display:grid;gap:14px}.lens{padding:22px;border:1px solid var(--line);border-radius:22px;background:#fff6}.lens b{font-size:38px;display:block}.lens:nth-child(1)b{color:var(--gold)}.lens:nth-child(2)b{color:var(--cyan)}.lens:nth-child(3)b{color:var(--red)}section{padding:11vh 7vw;min-height:80vh;border-top:1px solid var(--line)}.kicker{color:var(--gold);font-weight:800}.title{font-size:clamp(34px,5vw,72px);line-height:1.05;max-width:1050px;margin:.25em 0}.lede{font-size:20px;line-height:1.8;max-width:850px}.sticky-grid{display:grid;grid-template-columns:.72fr 1.28fr;gap:5vw;align-items:start}.steps{display:grid;gap:50vh;padding-bottom:40vh}.step{padding:24px;border-left:4px solid var(--line);opacity:.46;transition:.3s}.step.active{border-color:var(--red);opacity:1}.step h3{font-size:28px;margin:0 0 12px}.viz{position:sticky;top:13vh;min-height:68vh;border:1px solid var(--line);border-radius:24px;background:#fff7;padding:25px}.rankrow{display:grid;grid-template-columns:40px 65px 1fr 54px;align-items:center;gap:10px;margin:10px 0}.track{height:15px;background:#e4e8e5;border-radius:8px;overflow:hidden}.fill{height:100%;border-radius:8px;transition:width .65s cubic-bezier(.2,.8,.2,1)}.controls{display:flex;gap:10px;flex-wrap:wrap;margin:18px 0}.controls button{border:1px solid var(--line);background:transparent;border-radius:999px;padding:10px 15px;cursor:pointer}.controls button.active{background:var(--ink);color:white}.history{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:40px}.year{padding:30px;border-radius:22px;background:#fff7;border:1px solid var(--line)}.year strong{font-size:58px;color:var(--teal)}.source{font-size:14px;line-height:1.8}.source a{color:var(--teal)}footer{padding:7vh 7vw;background:var(--ink);color:var(--paper)}@media(max-width:850px){.hero,.sticky-grid{grid-template-columns:1fr}.hero{padding-top:18vh}.viz{position:relative;top:0}.steps{gap:8vh;padding-bottom:8vh}.history{grid-template-columns:1fr}.hero h1{font-size:64px}}
</style></head><body><nav><b>S2 · 口径的魔力</b><div><a href="#story">故事</a>　<a href="#history">跨届验证</a>　<a href="#sources">来源</a></div></nav><header class="hero"><div><div class="eyebrow">DATA STORY · PARIS 2024</div><h1>谁被<br>奖牌榜<br>看见？</h1><p>同一组比赛结果，只需改变统计单位，就会生成三套不同但各自合理的秩序。</p></div><div class="triptych"><div class="lens"><b>329</b>官方金牌单元<br><small>每个获胜小项计1</small></div><div class="lens"><b>1.00</b>团队内均分<br><small>每组成员权重之和</small></div><div class="lens"><b>2,281</b>运动员奖牌记录<br><small>每位获奖者计1</small></div></div></header>
<section id="story"><div class="kicker">01 · THREE LENSES</div><h2 class="title">没有唯一的“公平榜”，只有被问题选择的统计单位</h2><div class="sticky-grid"><div class="steps"><article class="step active" data-lens="official"><h3>官方小项</h3><p>回答“赢下多少竞赛单元”。团队项目与个人项目都只计一枚。</p></article><article class="step" data-lens="fractional"><h3>团队内均分</h3><p>把一枚奖牌平均分给同一获奖组成员。保留个人贡献，但不让团队规模机械放大结果。</p></article><article class="step" data-lens="rows"><h3>运动员行</h3><p>回答“产生多少获奖者记录”。多人项目因此获得更大权重。</p></article></div><div class="viz"><h3 id="viztitle">官方小项 · 前12</h3><div class="controls"><button data-btn="official" class="active">官方小项</button><button data-btn="fractional">团队内均分</button><button data-btn="rows">运动员行</button></div><div id="ranking"></div></div></div></section>
<section id="history"><div class="kicker">02 · ROBUSTNESS</div><h2 class="title">2008、2012、2016：同一机制重复出现</h2><p class="lede">多人获奖组占比越高，运动员行口径的金牌放大越明显。三届相关均超过0.98；榜单总体仍相似，但局部重排稳定存在。</p><div class="history" id="hist"></div></section>
<section id="sources"><div class="kicker">03 · 来源与边界</div><h2 class="title">来源透明，比“看起来精确”更重要</h2><div class="source"><p>2024核心口径使用任务一整理的329小项结果。2008、2012、2016的小项表由运动员记录按 NOC–Event–Medal 去重生成，属于历史代理，仍有待现行逐项核验的记录；下面的IOC链接只是各届结果入口，不代表这些代理已获IOC逐项核实。</p><p><a href="https://www.olympics.com/en/olympic-games/beijing-2008/results">北京2008 IOC 页面入口</a>　·　<a href="https://www.olympics.com/en/olympic-games/london-2012/results">伦敦2012 IOC 页面入口</a>　·　<a href="https://www.olympics.com/en/olympic-games/rio-2016/results">里约2016 IOC 页面入口</a></p><p>伦敦2012存在IOC后续奖牌重分配，本专题以当前主数据版本分析结构机制，并在提交材料中保留版本边界。</p></div></section><footer><h2>口径不是技术脚注，而是结论本身。</h2><p>晓组织｜燕山大学｜张子涵60%｜陈旭40%</p></footer>
<script>const data=__DATA__,hist=__HIST__;let current='official';const colors={official:'#c69036',fractional:'#58a8b4',rows:'#ad4058'},names={official:'官方小项',fractional:'团队内均分',rows:'运动员行'};function draw(lens){current=lens;let a=data.filter(x=>x.lens===lens).sort((a,b)=>a.rank-b.rank).slice(0,12),max=Math.max(...a.map(x=>x.Gold));document.querySelector('#viztitle').textContent=names[lens]+' · 前12';document.querySelector('#ranking').innerHTML=a.map(x=>`<div class="rankrow"><b>${x.rank}</b><b>${x.NOC}</b><div class="track"><div class="fill" style="width:${x.Gold/max*100}%;background:${colors[lens]}"></div></div><span>${x.Gold.toFixed(lens==='fractional'?1:0)}</span></div>`).join('');document.querySelectorAll('[data-btn]').forEach(b=>b.classList.toggle('active',b.dataset.btn===lens))}document.querySelectorAll('[data-btn]').forEach(b=>b.onclick=()=>draw(b.dataset.btn));const obs=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){document.querySelectorAll('.step').forEach(x=>x.classList.remove('active'));e.target.classList.add('active');draw(e.target.dataset.lens)}}),{threshold:.62});document.querySelectorAll('.step').forEach(x=>obs.observe(x));document.querySelector('#hist').innerHTML=hist.map(x=>`<div class="year"><small>${x.Year}</small><strong>${x.mechanism_rho.toFixed(3)}</strong><p>结构相关 ρ</p><hr><p>排名 τ ${x.rank_kendall_tau.toFixed(3)}<br>平均变动 ${x.mean_abs_rank_change.toFixed(1)} 位</p></div>`).join('');draw(current);</script></body></html>'''.replace('__DATA__',payload).replace('__HIST__',hpayload)
# 用户主动切换时停止自动滚动观察，避免观察器与按钮争夺状态。
for a,b in {'DATA STORY · PARIS 2024':'数据故事 · 2024巴黎','01 · THREE LENSES':'01 · 三种统计口径','02 · ROBUSTNESS':'02 · 跨届稳健性','03 · SOURCE & BOUNDARY':'03 · 来源与边界'}.items(): html=html.replace(a,b)
html=html.replace('NOC–Event–Medal 去重','代表团—小项—奖牌类型去重')
html=html.replace('</body>','<script>document.querySelectorAll("[data-btn]").forEach(b=>b.addEventListener("click",()=>obs.disconnect(),{capture:true,once:true}));</script></body>')
(STORY/'index.html').write_text(localize_story_html(html),encoding='utf-8')
print(json.dumps({'official_validation':summary,'story':str(STORY/'index.html')},ensure_ascii=False,indent=2))


# Synchronize evidence scope after story regeneration.
from publish_ioc_evidence_ledger import main as publish_ioc_ledger
publish_ioc_ledger()

# Preserve conclusion-adjacent evidence notes after regeneration.
from publish_evidence_closure import main as publish_closure_notes
publish_closure_notes()
