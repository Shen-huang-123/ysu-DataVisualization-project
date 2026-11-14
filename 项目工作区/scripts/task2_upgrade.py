from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.path import Path as MplPath
from matplotlib.patches import PathPatch

ROOT = Path(__file__).resolve().parents[2]
TASK = ROOT / "交付文件" / "任务二_百年全景"
FIG = TASK / "04_核心图表"
TABLE = TASK / "02_数据表"
DASH = TASK / "05_交互总览"
for folder in (FIG, TABLE, DASH):
    folder.mkdir(parents=True, exist_ok=True)

DATA = ROOT / "交付文件" / "任务一_数据体检" / "02_交付数据" / "归一数据_保留原始字段.csv.gz"
HOST = ROOT / "交付文件" / "任务三_专题深挖" / "S1_东道主效应" / "host_summary.csv"
d = pd.read_csv(DATA)
d = d[d.include_main.astype(bool)].copy()
m = d[d.is_medal.astype(bool)].copy()

P = {"navy":"#123742", "teal":"#247487", "cyan":"#65A9B4", "red":"#A64155", "gold":"#C4903D", "paper":"#F7F3EB", "ink":"#172A30", "grey":"#728087", "grid":"#D9DEDC"}
plt.rcParams.update({"font.family":"Microsoft YaHei", "axes.spines.top":False, "axes.spines.right":False,
                     "figure.facecolor":P["paper"], "axes.facecolor":P["paper"], "savefig.facecolor":P["paper"],
                     "axes.labelcolor":P["ink"], "xtick.color":P["ink"], "ytick.color":P["ink"], "savefig.dpi":220})

def save(fig, name, note=""):
    if note:
        fig.text(.04, .014, note, fontsize=8, color=P["grey"])
    fig.savefig(FIG / name, dpi=220, bbox_inches="tight")
    plt.close(fig)

# 1) Cover hero: one visual thesis, four evidence cards.
by_year = d.groupby("Year").agg(records=("source_row","size"), nocs=("NOC","nunique"))
medal_year = m.groupby("Year").size()
noc_med = m.groupby(["Year","NOC"]).size().rename("n").reset_index()
totals = noc_med.groupby("Year").n.sum()
top5 = noc_med.groupby("Year").apply(lambda x: x.nlargest(5,"n").n.sum(), include_groups=False) / totals

fig = plt.figure(figsize=(16,9))
ax = fig.add_axes([.05,.26,.58,.55])
ax.plot(by_year.index, by_year.records, color=P["teal"], lw=3)
ax.fill_between(by_year.index, by_year.records, color=P["teal"], alpha=.12)
ax.set_title("一百二十八年，奥运从精英赛事走向全球制度", fontsize=23, fontweight="bold", loc="left", pad=18)
ax.set_ylabel("运动员参赛记录数"); ax.set_xlabel("届次年份"); ax.grid(axis="y", color=P["grid"])
ax.text(1896, 950, "380", color=P["red"], fontsize=15, fontweight="bold")
ax.text(2024, by_year.loc[2024,"records"]+350, "14,892", ha="right", color=P["teal"], fontsize=15, fontweight="bold")
cards = [("×39.2","参赛记录扩张","380 → 14,892"),("206","2024代表团数","1896年仅12个"),("41.8%","前五强份额","1896年为83.9%"),("49.1%","女性参赛占比","奖牌记录占50.3%")]
for i,(big,title,sub) in enumerate(cards):
    x=.68; y=.70-i*.155
    fig.text(x,y,big,fontsize=28,fontweight="bold",color=[P["teal"],P["gold"],P["red"],P["navy"]][i])
    fig.text(x+.14,y+.012,title,fontsize=13,fontweight="bold",color=P["ink"])
    fig.text(x+.14,y-.027,sub,fontsize=10,color=P["grey"])
fig.text(.05,.91,"百年圣火 · 全景总览",fontsize=15,fontweight="bold",color=P["gold"])
fig.text(.05,.12,"扩张没有制造同等程度的垄断；参与平权也尚未完全转化为项目机会平权。",fontsize=17,fontweight="bold",color=P["ink"])
fig.text(.05,.075,"1896—2024｜运动员记录口径｜排除1906｜2024小项采用官方329项补充表",fontsize=10,color=P["grey"])
save(fig,"00_封面总览英雄图.png")

# 2) Quantitative host attribution and sport contribution.
h = pd.read_csv(HOST)
h["label"] = h.NOC + " " + h.Year.astype(str)
h = h.sort_values("descriptive_gap_pp")
fig, axes = plt.subplots(1,2,figsize=(15,7),gridspec_kw={"width_ratios":[1.05,1.35]})
colors = [P["red"] if x < 0 else P["teal"] for x in h.change_pp]
axes[0].barh(h.label,h.change_pp,color=colors)
axes[0].axvline(0,color=P["ink"],lw=.8); axes[0].grid(axis="x",color=P["grid"])
axes[0].set_xlabel("主办届较前届奖牌记录份额变化（百分点）")
axes[0].set_title("八升一降：主场提升并非必然",loc="left",fontweight="bold",fontsize=15)
for y,v in enumerate(h.change_pp): axes[0].text(v+(.08 if v>=0 else -.08),y,f"{v:+.2f}",va="center",ha="left" if v>=0 else "right",fontsize=8.5)

host_map = dict(zip(h.Year.astype(int),h.NOC))
rows=[]
for year,noc in host_map.items():
    years=sorted(d.Year.unique())
    idx=years.index(year)
    if idx==0: continue
    pre=years[idx-1]
    for sport in sorted(set(m.loc[m.Year.isin([pre,year]),"sport_family"].dropna())):
        a=len(m[(m.Year.eq(pre)) & (m.NOC.eq(noc)) & (m.sport_family.eq(sport))]) / len(m[m.Year.eq(pre)]) * 100
        b=len(m[(m.Year.eq(year)) & (m.NOC.eq(noc)) & (m.sport_family.eq(sport))]) / len(m[m.Year.eq(year)]) * 100
        rows.append({"Year":year,"NOC":noc,"sport_family":sport,"contribution_pp":b-a})
contrib=pd.DataFrame(rows)
top=(contrib.sort_values(["Year","contribution_pp"],ascending=[True,False]).groupby("Year").head(3))
top.to_csv(TABLE/"B_主办届项目贡献分解.csv",index=False,encoding="utf-8-sig")
sport_order=top.groupby("sport_family").contribution_pp.sum().nlargest(12).index
heat=top[top.sport_family.isin(sport_order)].pivot_table(index="sport_family",columns="Year",values="contribution_pp",fill_value=0).reindex(sport_order)
im=axes[1].imshow(heat.values,aspect="auto",cmap="RdBu_r",vmin=-2.2,vmax=2.2)
体育中文={'Athletics':'田径','Swimming':'游泳','Diving':'跳水','Archery':'射箭','Cycling':'自行车','Fencing':'击剑','Gymnastics':'体操','Shooting':'射击','Wrestling':'摔跤','Rowing':'赛艇','Football':'足球','Judo':'柔道','Sailing':'帆船','Boxing':'拳击','Tennis':'网球','Weightlifting':'举重','Equestrian':'马术','Hockey':'曲棍球','Canoeing':'皮划艇','Table Tennis':'乒乓球','Basketball':'篮球','Volleyball':'排球','Water Polo':'水球','Badminton':'羽毛球','Handball':'手球','Triathlon':'铁人三项'}
axes[1].set_yticks(range(len(heat.index)),[体育中文.get(x,x) for x in heat.index]); axes[1].set_xticks(range(len(heat.columns)),heat.columns,rotation=45)
axes[1].set_title("主场增益来自不同优势项目组合",loc="left",fontweight="bold",fontsize=15)
cb=fig.colorbar(im,ax=axes[1],pad=.02); cb.set_label("对份额变化的贡献（百分点）")
fig.suptitle("B 定量归因：主办身份是信号，项目组合才是路径",fontsize=20,fontweight="bold",x=.04,ha="left")
save(fig,"B_主场效应与项目贡献.png","九个现代主办案例；差值为描述性证据而非因果估计。项目贡献以各运动大类奖牌记录占全届份额的前后变化衡量。")
h.to_csv(TABLE/"B_九个主办案例定量结果.csv",index=False,encoding="utf-8-sig")

# 3) Sport lifecycle: new, returning, exiting and continuity.
presence=(d.groupby(["Year","sport_family"]).size().rename("n").reset_index())
years=sorted(presence.Year.unique())
sets={y:set(presence.loc[presence.Year.eq(y),"sport_family"]) for y in years}
life=[]
seen=set()
for i,y in enumerate(years):
    cur=sets[y]; prev=sets[years[i-1]] if i else set(); nxt=sets[years[i+1]] if i+1<len(years) else set()
    new=cur-seen
    returning=(cur-prev)&seen
    continuing=cur&prev
    exiting=cur-nxt if i+1<len(years) else set()
    life.append({"Year":y,"新增":len(new),"重返":len(returning),"连续保留":len(continuing),"本届后退出":len(exiting)})
    seen |= cur
life=pd.DataFrame(life).set_index("Year")
life.to_csv(TABLE/"D_项目新增退出重返.csv",encoding="utf-8-sig")
fig,axes=plt.subplots(2,1,figsize=(15,8),sharex=True,gridspec_kw={"height_ratios":[1.45,1]})
axes[0].stackplot(life.index,life["连续保留"],life["新增"],life["重返"],labels=["连续保留","新增","重返"],colors=[P["teal"],P["gold"],P["cyan"]],alpha=.92)
axes[0].set_ylabel("当届运动大类数"); axes[0].legend(frameon=False,ncol=3,loc="upper left"); axes[0].grid(axis="y",color=P["grid"])
axes[0].set_title("D 项目体系不是只增不减：扩容与更替同时发生",loc="left",fontsize=19,fontweight="bold")
axes[1].bar(life.index,life["本届后退出"],width=2.8,color=P["red"],alpha=.82,label="本届后退出")
axes[1].plot(life.index,life["重返"],color=P["navy"],marker="o",lw=2,label="重返")
axes[1].set_ylabel("运动大类数"); axes[1].set_xlabel("届次年份"); axes[1].legend(frameon=False,ncol=2); axes[1].grid(axis="y",color=P["grid"])
save(fig,"D_项目新增退出重返流向.png","按归一后的体育大类识别：首次出现=新增；此前出现但上届缺席=重返；下届缺席=本届后退出。2020 Event泛化不影响Sport大类出现判断。")

# 4) Offline interactive overview, no external libraries.
series=[]
for y in years:
    series.append({"year":int(y),"records":int(by_year.loc[y,"records"]),"nocs":int(by_year.loc[y,"nocs"]),
                   "medals":int(medal_year.get(y,0)),"top5":round(float(top5.get(y,np.nan)*100),2)})
payload=json.dumps(series,ensure_ascii=False)
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>百年圣火 · 交互总览</title><style>
:root{{--paper:#f7f3eb;--ink:#172a30;--teal:#247487;--red:#a64155;--gold:#c4903d;--line:#d9dedc}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font-family:"Microsoft YaHei",sans-serif}}
header{{padding:34px 6vw 18px;border-bottom:1px solid var(--line)}}h1{{font-size:clamp(30px,5vw,68px);margin:0;letter-spacing:-2px}}header p{{max-width:850px;color:#65757b}}
.wrap{{padding:28px 6vw 60px}}.cards{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}.card{{padding:18px;border:1px solid var(--line);border-radius:16px;background:#fff8}}.big{{font-size:32px;font-weight:800;color:var(--teal)}}
.controls{{display:flex;gap:14px;align-items:center;margin:28px 0 12px}}input[type=range]{{flex:1}}#year{{font-size:27px;font-weight:800;color:var(--red)}}
#chart{{width:100%;height:330px;border:1px solid var(--line);border-radius:18px;background:#fff8}}.gallery{{display:grid;grid-template-columns:repeat(2,1fr);gap:18px;margin-top:28px}}.gallery img{{width:100%;border-radius:14px;border:1px solid var(--line)}}
button{{border:0;border-radius:999px;padding:10px 16px;background:var(--ink);color:white;cursor:pointer}}@media(max-width:800px){{.cards,.gallery{{grid-template-columns:1fr}}}}
</style></head><body><header><div style="color:var(--gold);font-weight:800">晓组织 · 燕山大学</div><h1>百年圣火</h1><p>从规模扩张、强国更替、女性平权到项目演化，拖动届次查看同口径数据。所有内容离线运行，不上传任何数据。</p></header>
<main class="wrap"><div class="cards"><div class="card"><small>届次</small><div class="big" id="cYear"></div></div><div class="card"><small>参赛记录</small><div class="big" id="cRec"></div></div><div class="card"><small>代表团</small><div class="big" id="cNoc"></div></div><div class="card"><small>前五强份额</small><div class="big" id="cTop"></div></div></div>
<div class="controls"><button id="play">自动播放</button><input id="slider" type="range" min="0" max="{len(series)-1}" value="{len(series)-1}"><span id="year"></span></div><svg id="chart" viewBox="0 0 1100 330" preserveAspectRatio="none"></svg>
<div class="gallery"><img src="../04_核心图表/00_封面总览英雄图.png"><img src="../04_核心图表/B_主场效应与项目贡献.png"><img src="../04_核心图表/C_女性三层平权曲线.png"><img src="../04_核心图表/D_项目新增退出重返流向.png"></div></main>
<script>const data={payload};const s=document.querySelector('#slider'),svg=document.querySelector('#chart');let timer=null;
function draw(i){{const d=data[i];cYear.textContent=d.year;cRec.textContent=d.records.toLocaleString();cNoc.textContent=d.nocs;cTop.textContent=(isNaN(d.top5)?'—':d.top5+'%');year.textContent=d.year;
const max=Math.max(...data.map(x=>x.records));let pts=data.map((x,j)=>[35+j*(1030/(data.length-1)),295-x.records/max*245]);let p=pts.map((x,j)=>(j?'L':'M')+x[0]+','+x[1]).join(' ');let area=p+' L '+pts.at(-1)[0]+',295 L 35,295 Z';svg.innerHTML=`<path d="${{area}}" fill="#24748722"/><path d="${{p}}" fill="none" stroke="#247487" stroke-width="4"/><line x1="${{pts[i][0]}}" x2="${{pts[i][0]}}" y1="35" y2="295" stroke="#a64155" stroke-width="3"/><circle cx="${{pts[i][0]}}" cy="${{pts[i][1]}}" r="7" fill="#a64155"/>`;}}
s.oninput=()=>draw(+s.value);play.onclick=()=>{{if(timer){{clearInterval(timer);timer=null;play.textContent='自动播放';return}}play.textContent='暂停';timer=setInterval(()=>{{s.value=(+s.value+1)%data.length;draw(+s.value)}},650)}};draw(+s.value);</script></body></html>'''
(DASH/"index.html").write_text(html,encoding="utf-8")
print(json.dumps({"new_figures":4,"dashboard":str(DASH/"index.html"),"host_cases":len(h)},ensure_ascii=False,indent=2))
