"""Ten-topic conclusion stability map, using audited artefacts and explicit evidence grades."""
from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager

ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件'/'任务三_专题深挖'
OUT=TASK/'11_结论稳定性地图';OUT.mkdir(parents=True,exist_ok=True)
raw=pd.read_csv(ROOT/'项目工作区'/'outputs'/'olympics_flagged.csv.gz',low_memory=False)
med24=raw[raw.Year.eq(2024)&raw.is_medal.eq(True)]
off=pd.read_csv(ROOT/'交付文件'/'任务一_数据体检'/'02_交付数据'/'2024官方329小项奖牌表.csv')
ranks=pd.read_csv(TASK/'S2_口径的魔力'/'02_数据表'/'S2_2024三口径完整排名.csv')
spa=ranks[ranks.NOC.eq('ESP')].set_index('lens')['rank']
female=100*med24.Sex.eq('F').mean();women=100*off.gender.eq('W').mean()
row_top3=100*med24.sport_family.value_counts().head(3).sum()/len(med24)
event_top3=100*off.discipline.value_counts().head(3).sum()/len(off)
old=pd.read_csv(TASK/'S4_小代表团的大突破'/'02_客观样本'/'原七案例与客观门槛对照.csv')
small=pd.read_csv(TASK/'S4_小代表团的大突破'/'02_客观样本'/'客观小代表团清单.csv')
orig=len(old);passing=int(old.selected.sum())
records=[
 ('S1','主场会自动带来净收益','9例中8例份额上升；巴西2016份额下降0.57个百分点','相对比较组、匹配DID与合成对照','描述较稳，因果未识别','主办权选择、项目与投资未完全控制','S1_东道主效应/index.html','证据不足'),
 ('S2','金牌榜只有一种公平排名',f'西班牙官方小项第{int(spa["official"])}，运动员行第{int(spa["rows"])}','官方小项／团队内均分／运动员行','排序随统计单位重排','行数放大团队成员，不等于多枚官方奖牌','S2_口径的魔力/06_滚动叙事专题/index.html','口径敏感'),
 ('S3','参赛代表团总数足以识别抵制','1984数据覆盖140个代表团，高于1980的80个，仍有IOC记载的抵制','代码集合差＋IOC一手史料','总量方向可误导','未出现不等于某个具体政治动机','S3_地缘政治的投影/IOC一手来源核验.html','口径敏感'),
 ('S4','七个故事案例代表所有小队伍',f'原{orig}例中{passing}例符合预设最小四分位门槛；客观筛选得到{len(small)}例','至少三届＋典型参赛规模下四分位＋至少一届获奖','纳入规则改变案例总体','行数受团队人数影响；极小样本不宜算效率','S4_小代表团的大突破/02_客观样本/index.html','口径敏感'),
 ('S5','获奖行增长等于夺牌机会增长','1896—2024获奖运动员行约增16倍；不同分母给出不同叙事','同届参赛行、历史奖牌组代理与官方小项','绝对增长成立，机会解释不成立','早期覆盖与团队人数变化','S5_奖牌的通货膨胀/index.html','口径敏感'),
 ('S6','姓名可直接形成个人历史榜','12,796个编号关联多个姓名；原始人物身份不稳定','姓名跨度＋编号冲突＋权威档案逐人核验','个人榜暂不可验证','候选警报不等于真实错误人数','S6_王者与传奇/index.html','证据不足'),
 ('S7','冠军王朝缩短说明运动员变弱','固定113个1960—2016连续小项，卫冕率从34.5%降至27.1%','长期固定小项／避开抵制转折期／逐运动排除','固定项目后下降仍存在，个人机制未识别','只代表长期存续小项；时间窗与政体变化仍影响幅度','S3_冠军的保质期/09_固定小项队列检验/index.html','证据不足'),
 ('S8','女子获奖行接近一半即机会对称',f'2024女性获奖行{female:.1f}%，女子专属小项{women:.1f}%','参赛行／获奖行／官方小项三种分母','比例接近不等于项目机会相等','混合项目和团队规模改变记录占比','S8_她们登上领奖台/index.html','口径敏感'),
 ('S9','最后一次出现等于永久退出','高尔夫中断后重返；早期夏奥中的冬季项目也改变归属','归一运动家族＋逐届出现序列','最后出现并非正式退出','名称映射与赛程规则须独立核验','S9_消失的赛场/index.html','口径敏感'),
 ('S10','获奖行最多的运动拥有最多比赛机会',f'2024行口径前三运动占{row_top3:.1f}%，官方小项数前三占{event_top3:.1f}%','运动员奖牌行／329个官方小项','项目排序与份额随单位改变','奖牌行、奖牌枚数和比赛机会不同','S10_奖牌藏在哪些项目/index.html','口径敏感'),
]
cols=['专题','未经检验的直觉','最关键的交叉证据','替代口径或核验','修正后结论','推断边界','证据入口','状态']
df=pd.DataFrame(records,columns=cols)
df.to_csv(OUT/'十专题结论稳定性矩阵.csv',index=False,encoding='utf-8-sig')
(OUT/'十专题结论稳定性矩阵.json').write_text(df.to_json(orient='records',force_ascii=False,indent=2),encoding='utf-8')

# Publication chart: one page, a small visual grammar for the evidence status.
font='Microsoft YaHei'
if not any(f.name==font for f in font_manager.fontManager.ttflist):font='SimHei'
plt.rcParams['font.family']=font
fig,ax=plt.subplots(figsize=(13,8.2),facecolor='#f3efe6');ax.set_facecolor('#f3efe6')
colors={'口径敏感':'#ad513c','证据不足':'#23577a'}
for i,r in enumerate(df.itertuples(index=False)):
    y=9-i
    ax.barh(y,1,left=0,color=colors[r.状态],height=.56)
    ax.text(.18,y,r.专题,va='center',ha='left',fontsize=12,fontweight='bold',color='white')
    ax.text(1.4,y,r.未经检验的直觉,va='center',fontsize=13,color='#1b3041')
    ax.text(10.7,y,r.状态,va='center',fontsize=11,color=colors[r.状态],fontweight='bold')
ax.set_xlim(0,12.6);ax.set_ylim(-.7,10.5);ax.axis('off')
fig.text(.085,.92,'十个直觉，经得起几次换口径？',fontsize=25,fontweight='bold',color='#172b42')
fig.text(.085,.875,'红色：结论随统计单位或纳入规则改变    蓝色：当前数据不足以验证推断',fontsize=12,color='#556779')
fig.text(.085,.075,'2024官方小项仅用于该届交叉核验；历史代理和运动员行在图注中分列。',fontsize=10,color='#65747a')
fig.savefig(OUT/'结论稳定性地图.png',dpi=190,bbox_inches='tight',facecolor=fig.get_facecolor());plt.close(fig)

cards=''.join(f'''<article class="card" id="{r.专题}" data-status="{r.状态}"><div class="tag"><span>{r.专题}</span><b>{r.状态}</b></div><h2>{r.未经检验的直觉}</h2><p class="evidence">{r.最关键的交叉证据}</p><dl><dt>替代口径</dt><dd>{r.替代口径或核验}</dd><dt>修正结论</dt><dd>{r.修正后结论}</dd><dt>证据边界</dt><dd>{r.推断边界}</dd></dl><a href="../{r.证据入口}">进入专题证据 ↗</a></article>''' for r in df.itertuples(index=False))
html=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>结论稳定性地图｜百年圣火</title><style>*{{box-sizing:border-box}}html{{scroll-behavior:smooth}}body{{margin:0;background:#f2eee5;color:#142d43;font-family:"Microsoft YaHei",sans-serif}}main{{max-width:1300px;margin:auto;padding:68px 26px 110px}}.eyebrow{{color:#aa4c37;letter-spacing:.16em}}h1{{font-size:clamp(44px,7vw,92px);line-height:1.1;max-width:990px;margin:20px 0}}.lead{{font-size:20px;line-height:1.8;max-width:790px}}.hero img{{display:block;width:100%;border-radius:22px;margin:32px 0;box-shadow:0 22px 50px #1c324021}}.filters{{display:flex;gap:10px;flex-wrap:wrap;margin:35px 0}}button{{border:1px solid #c8c6bc;background:#fffaf1;border-radius:999px;padding:11px 20px;color:#233b4b;cursor:pointer;font-size:15px}}button[aria-pressed=true]{{background:#173b58;color:#fff}}.grid{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}}.card{{background:#fffaf2;border:1px solid #d9d3c7;border-radius:24px;padding:28px;box-shadow:0 10px 30px #1c32400c;transition:transform .35s,box-shadow .35s}}.card:hover{{transform:translateY(-5px);box-shadow:0 20px 40px #1c32401b}}.tag{{display:flex;justify-content:space-between;color:#a0523e}}.tag span{{font:700 34px Georgia}}.tag b{{font-size:13px}}h2{{font-size:24px;line-height:1.4}}.evidence{{font-size:18px;font-weight:700;color:#1d537a;line-height:1.6}}dl{{display:grid;grid-template-columns:86px 1fr;gap:10px 14px;line-height:1.7;color:#374d5e}}dt{{font-weight:700}}dd{{margin:0}}a{{color:#24669b}}.card a{{display:inline-block;margin-top:15px;font-weight:700}}.note{{background:#173b58;color:#edf5f7;border-radius:24px;padding:30px;margin:28px 0;line-height:1.8}}@media(max-width:760px){{.grid{{grid-template-columns:1fr}}main{{padding:42px 17px 80px}}.card{{padding:22px}}}}</style></head><body><main><div class="hero"><div class="eyebrow">百年圣火 / 研究方法</div><h1>结论不是一句话。<br>它要经得起换分母。</h1><p class="lead">十个专题各从一个常见直觉出发，换统计单位、寻找反例，并给结论划出证据边界。点击专题卡片查看完整计算与来源。</p><img src="结论稳定性地图.png" alt="十专题结论稳定性地图"></div><div class="filters" role="group" aria-label="按结论状态筛选"><button aria-pressed="true" data-filter="全部">全部十题</button><button aria-pressed="false" data-filter="口径敏感">口径敏感</button><button aria-pressed="false" data-filter="证据不足">证据不足</button></div><div class="grid">{cards}</div><div class="note">状态是证据分类，不是专题质量评分。“口径敏感”意味着原直觉需改写；“证据不足”意味着现有数据不能支撑更强的因果或人物判断。2024 官方小项与历史代理分开呈现。</div><p><a href="十专题结论稳定性矩阵.csv">下载十专题矩阵</a>　<a href="../十专题深度核验.html">查看原始深度核验</a></p></main><script>document.querySelector('.filters').addEventListener('click',e=>{{const b=e.target.closest('button[data-filter]');if(!b)return;document.querySelectorAll('.filters button').forEach(x=>x.setAttribute('aria-pressed',x===b?'true':'false'));document.querySelectorAll('.card').forEach(x=>x.hidden=b.dataset.filter!=='全部'&&x.dataset.status!==b.dataset.filter)}})</script></body></html>'''
(OUT/'index.html').write_text(html,encoding='utf-8')
map_page=OUT/'index.html'
map_text=map_page.read_text(encoding='utf-8')
map_text=map_text.replace('<div class="filters"', '<p><a href="02_量化口径实验/index.html" class="stability-experiment">查看五个核心结论的量化口径实验<span aria-hidden="true">↗</span></a></p><div class="filters"',1)
map_page.write_text(map_text,encoding='utf-8')
import os
portal=TASK/'统一中文入口'/'index.html'
if portal.exists():
    body=portal.read_text(encoding='utf-8')
    old_start,old_end='<!-- DEPTH_PORTAL_START -->','<!-- DEPTH_PORTAL_END -->'
    if old_start in body and old_end in body:
        body=body[:body.index(old_start)]+body[body.index(old_end)+len(old_end):]
    start,end='<!-- INLINE_EVIDENCE_START -->','<!-- INLINE_EVIDENCE_END -->'
    if start in body and end in body:
        body=body[:body.index(start)]+body[body.index(end)+len(end):]
    item_html=''.join(f'''<details class="inline-evidence-item" id="evidence-{r.专题}"><summary><span class="inline-evidence-no">{r.专题}</span><strong>{r.未经检验的直觉}</strong><span class="inline-evidence-status">{r.状态}</span><i aria-hidden="true">＋</i></summary><div class="inline-evidence-body"><p class="inline-evidence-finding">{r.最关键的交叉证据}</p><dl><dt>换个角度</dt><dd>{r.替代口径或核验}</dd><dt>修正结论</dt><dd>{r.修正后结论}</dd><dt>证据边界</dt><dd>{r.推断边界}</dd></dl><a href="../{r.证据入口}">进入{r.专题}完整专题 <span aria-hidden="true">↗</span></a></div></details>''' for r in df.itertuples(index=False))
    inline=f'''{start}<section class="inline-evidence" aria-labelledby="inline-evidence-title"><div class="section-head"><div><small>十专题 / 交叉核验</small><h2 id="inline-evidence-title">换一个分母，<br>结论还站得住吗？</h2></div><p>十个专题的关键反例直接放在这里。展开每一条，查看替代口径、修正后的判断与证据边界；再按需进入完整专题。</p></div><div class="inline-evidence-list">{item_html}</div><p class="inline-evidence-foot">这是一张阅读索引。红色表示原直觉对口径或选例敏感；蓝色表示当前数据不足以验证更强的推断。<a href="../11_结论稳定性地图/十专题结论稳定性矩阵.csv">下载完整核验矩阵 ↗</a></p></section>{end}'''
    inline=inline.replace('下载完整核验矩阵 ↗</a>','下载完整核验矩阵 ↗</a>　<a href="../11_结论稳定性地图/02_量化口径实验/index.html">五个核心结论的量化检验 ↗</a>')
    anchor='<section class="deep-evidence"'
    if anchor in body:body=body.replace(anchor,inline+anchor,1)
    else:body=body.replace('</main>',inline+'</main>',1)
    css='''<style id="inline-evidence-style">.inline-evidence{margin:clamp(90px,12vw,170px) 0 80px;color:inherit}.inline-evidence .section-head{margin-bottom:24px}.inline-evidence-list{border-top:1px solid currentColor}.inline-evidence-item{border-bottom:1px solid currentColor;border-color:color-mix(in srgb,currentColor 22%,transparent)}.inline-evidence-item summary{list-style:none;display:grid;grid-template-columns:75px minmax(0,1fr) 130px 28px;align-items:center;gap:22px;cursor:pointer;padding:25px 4px;transition:padding .3s,color .3s}.inline-evidence-item summary::-webkit-details-marker{display:none}.inline-evidence-item summary:hover{padding-left:14px;color:#b46140}.inline-evidence-no{font:700 24px Georgia,serif;color:#a3573d}.inline-evidence-item summary strong{font-size:clamp(19px,2.1vw,29px);font-weight:600;line-height:1.4}.inline-evidence-status{font-size:13px;letter-spacing:.05em;color:#a3573d}.inline-evidence-item:nth-child(1) .inline-evidence-status,.inline-evidence-item:nth-child(6) .inline-evidence-status,.inline-evidence-item:nth-child(7) .inline-evidence-status{color:#39779a}.inline-evidence-item summary i{font-style:normal;font-size:27px;transition:transform .3s}.inline-evidence-item[open] summary i{transform:rotate(45deg)}.inline-evidence-body{padding:0 5% 30px 97px;max-width:1050px;animation:ie-open .45s ease both}.inline-evidence-finding{font-size:18px;font-weight:700;line-height:1.7;color:#2b6a85}.inline-evidence-body dl{display:grid;grid-template-columns:90px 1fr;gap:11px 22px;line-height:1.75}.inline-evidence-body dt{font-weight:700}.inline-evidence-body dd{margin:0}.inline-evidence-body>a{display:inline-block;margin-top:10px;border-bottom:1px solid currentColor;padding-bottom:5px;font-weight:700}.inline-evidence-foot{margin:32px 0 0;font-size:14px;line-height:1.8;opacity:.82}.inline-evidence-foot a{text-decoration:underline;text-underline-offset:5px}@keyframes ie-open{from{opacity:0;transform:translateY(-8px)}to{opacity:1;transform:translateY(0)}}body.xz-dark .inline-evidence-finding{color:#9bcbe2}body.xz-dark .inline-evidence-no,body.xz-dark .inline-evidence-status{color:#efad84}@media(max-width:700px){.inline-evidence-item summary{grid-template-columns:48px minmax(0,1fr) 22px;gap:11px;padding:22px 0}.inline-evidence-status{grid-column:2;grid-row:2}.inline-evidence-item summary i{grid-column:3;grid-row:1}.inline-evidence-no{font-size:19px}.inline-evidence-body{padding:0 0 25px 0}.inline-evidence-body dl{grid-template-columns:70px 1fr;gap:10px}.inline-evidence .section-head{margin-bottom:14px}}</style>'''
    if 'id="inline-evidence-style"' not in body:body=body.replace('</head>',css+'</head>',1)
    portal.write_text(body,encoding='utf-8')
for r in df.itertuples(index=False):
    topic_page=TASK/r.证据入口
    if topic_page.exists():
        body=topic_page.read_text(encoding='utf-8')
        marker=f'<!-- stability-backlink-{r.专题} -->'
        if marker not in body:
            href=Path(os.path.relpath(OUT/'index.html',topic_page.parent)).as_posix()+'#'+r.专题
            block=f'''{marker}<a href="{href}" style="display:block;max-width:1020px;margin:32px auto;padding:20px 26px;border-radius:19px;background:#173b58;color:#fff;text-decoration:none;font-family:'Microsoft YaHei',sans-serif"><small style="color:#acd9ec">交叉核验 · {r.专题}</small><strong style="display:block;font-size:22px;margin:5px 0">这个结论换口径后还成立吗？ ↗</strong><span style="color:#dceaf1">查看反例、替代分母与证据边界</span></a>'''
            topic_page.write_text(body.replace('</body>',block+'</body>',1),encoding='utf-8')
for target,href in [
    (TASK/'统一中文入口'/'index.html','../11_结论稳定性地图/index.html'),
    (ROOT/'index.html','交付文件/任务三_专题深挖/11_结论稳定性地图/index.html'),
    (ROOT/'交付文件'/'任务二_百年全景'/'05_交互总览'/'index.html','../../任务三_专题深挖/11_结论稳定性地图/index.html'),
    (ROOT/'交付文件'/'任务四_开放创作'/'02_2028洛杉矶预测'/'index.html','../../任务三_专题深挖/11_结论稳定性地图/index.html')]:
    if target.exists():
        text=target.read_text(encoding='utf-8')
        marker='<!-- stability-map-entry -->'
        if marker not in text:
            link=f'''{marker}<a href="{href}" style="display:block;max-width:1100px;margin:34px auto;padding:24px 28px;border-radius:22px;background:#173b58;color:#fff;text-decoration:none;font-family:'Microsoft YaHei',sans-serif"><small style="color:#a9d5ee">新研究入口 · 十专题</small><strong style="display:block;font-size:25px;margin:7px 0">结论稳定性地图 ↗</strong><span style="color:#dceaf1">换口径、找反例、划证据边界：看十个故事哪些结论真正站得住。</span></a>'''
            target.write_text(text.replace('</body>',link+'</body>',1),encoding='utf-8')
depth=TASK/'十专题深度核验.html'
if depth.exists():
    text=depth.read_text(encoding='utf-8')
    if 'href="11_结论稳定性地图/index.html"' not in text:
        text=text.replace('</body>','<p style="max-width:1050px;margin:32px auto;padding:22px;border-radius:18px;background:#173b58"><a href="11_结论稳定性地图/index.html" style="color:#fff;font-size:20px">十专题结论稳定性地图</a></p></body>',1)
    text=text.replace('下一步应按代码逐个查 IOC 与各国奥委会档案。','IOC 一手文献已核对抵制背景与特殊身份制度；单个缺席代码的动机仍不能由数据推断。')
    text=text.replace('本页只挑选七个分析案例，不构成全部小代表团的公平排行榜。','原七个故事案例均不在预设最小四分位样本内；客观筛选的完整候选与排除理由见 S4 专题。')
    depth.write_text(text,encoding='utf-8')
print(df[['专题','状态']].to_string(index=False))

import runpy
runpy.run_path(str(Path(__file__).with_name("publish_stability_list.py")))

# Apply the shared transparent evidence links after inserting legacy entries.
import runpy
runpy.run_path(str(Path(__file__).with_name('publish_research_proof_links.py')))
