"""Embed research results into existing task narratives; no network needed at runtime."""
from pathlib import Path
import json
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
D=ROOT/'交付文件'

def table(df):
    return df.rename(columns={'Year':'年份'}).to_html(index=False,border=0,classes='rc-table',float_format=lambda x:f'{x:.4f}')

def section(title,lead,body):
    return f'<section id="research-closure" class="research-closure" aria-labelledby="rc-title"><h2 id="rc-title">{title}</h2><p class="rc-lead">{lead}</p>{body}</section>'

impact=pd.read_csv(D/'任务一_数据体检/05_数据问题影响账本/问题影响实测.csv')
dup=pd.read_csv(D/'任务一_数据体检/05_数据问题影响账本/重复敏感性逐届名次.csv')
t1=section('清洗的决定，改变了多少结论？','先看处理前后，再判断这些问题是否影响解释。数量为记录行，占比变化为百分点。',f'''<label class="rc-control">比较决定 <select data-rc-impact><option>排除1906</option><option>疑似重复超额行剔除敏感性</option></select></label><div class="rc-scroll" tabindex="0" aria-label="处理前后实测表">{table(impact)}</div><p class="rc-note">疑似重复并非已确认错行，剔除只作敏感性。主分析剔除1459行，其中36条获奖行；女性获奖行占比仅增加0.0184个百分点。</p><details><summary>哪些届次的金牌行榜发生了变化？</summary>{table(dup[dup['金牌行榜名次变化代表团数'].gt(0)])}<p>1972年两个代表团、2024年一个代表团移动1位；这里是金牌行榜，不能解释为官方奖牌榜改变。</p></details><details><summary>不改变行数，也会改变能回答的问题</summary><p>项目归一改变组内归属；泛化小项标签不能用来推导正式小项数；身份警报不等于错误人物数量。1956双城合为一届，城市字段保留；历史代表团代码不强行合并。</p></details><a href="05_数据问题影响账本/问题影响实测.csv" download>下载实测表 ↗</a> · <a href="05_数据问题影响账本/数据问题影响账本.html">完整方法与边界 ↗</a>''')

cases=[('口径的魔力','同一场胜利，为何重排榜单？','西班牙官方奖牌榜第15，运动员金牌行榜第5。','固定届次、代表团、奖牌颜色与名次规则，比较小项、团队均分、运动员行，并逐运动剔除。','若统一排名规则或剔除某运动后重排消失，就缩小口径效应的主张。均分也会受成员匹配缺口影响。','统计单位改变了团队成员的权重，不意味着IOC多发奖牌，也不存在脱离问题的唯一公平榜。','../S2_口径的魔力/06_滚动叙事专题/index.html'),('主场效应','自身下降，是否仍有相对优势？','巴西2016自身份额下降0.57个百分点，相对匹配组却为正0.13个百分点。','17个可用合成对照案例；14个高拟合案例平均差值+2.24个百分点，区间约[1.30,3.28]。','预趋势、主办前投入和比较组选择都可能改变解释。区间不能消除主办权选择偏差。','平均主场关联在小项三情景中为正；巴西2016的小项合成对照差值为负，原+0.13仅限运动员行五队匹配。方法不可混写，机制未因果识别。','../S1_东道主效应/index.html'),('冠军延续','王朝变短，只是项目表变了吗？','固定113个连续同名小项后，卫冕率仍由34.51%降至27.14%。','1582次控制权转移；小项成组区间为[-13.20,-1.62]个百分点；逐运动排除未改变下降方向。','同名小项实质规则和历史身份连续性仍可能影响结果；连续举办小项存在选择偏差。','同113项替换二次来源后结果不变；排除未决系列剩50项，差值−7.33个百分点、区间[-16.17,+1.50]跨零。这是代表团控制权，非个人寿命或IOC认证。','../S3_冠军的保质期/06_冠军王朝时间轴/index.html')]
body='<div class="rc-tabs" role="group" aria-label="选择研究专题">'+''.join(f'<button type="button" data-rc-case="{i}" aria-pressed="{str(i==0).lower()}">{c[0]}</button>' for i,c in enumerate(cases))+'</div>'
for i,c in enumerate(cases):
    body+=f'<article data-rc-panel="{i}" {"hidden" if i else ""}><h3>{c[1]}</h3><p class="rc-finding">{c[2]}</p><dl><dt>怎样检验</dt><dd>{c[3]}</dd><dt>什么会推翻它</dt><dd>{c[4]}</dd><dt>修正后的结论</dt><dd>{c[5]}</dd></dl><a href="{c[6]}">进入专题核对证据 ↗</a></article>'
body+='<p class="rc-note">三篇承担主论证，其余专题作为扩展探索。历史555项已完成独立二次来源对照，仍不等于现行IOC逐项确认。</p><a href="../三篇旗舰专题_研究闭环.html">阅读完整研究闭环 ↗</a>'
t3=section('结论要经过反例，才值得留下','沿着三个问题，检查原判断如何被证据修正。',body)
t2=section('主场优势，取决于你与谁比较','前后变化和相对比较并不总是给出同一个答案。','''<div class="rc-contrast"><div><h3>巴西2016：比自己</h3><p class="rc-finding">−0.57 个百分点</p><p>主办届获奖行份额较前届下降。</p></div><div><h3>巴西2016：比匹配组</h3><p class="rc-finding">+0.13 个百分点</p><p>相对于前届份额相近的比较组，差值为正。</p></div></div><details><summary>更多比较设计，能把结论推进多远？</summary><p>扩展合成对照含17个可用案例，其中14个高拟合案例平均差值+2.24个百分点，案例自助法95%区间约[1.30,3.28]。不同筛选总体的估计不能混用。主办权选择、赛前投入与资格扩张仍限制因果解释。</p></details><p class="rc-note">统计单位为获奖运动员行份额；不能转称官方奖牌净增量。自身下降与相对优势可以同时成立。</p><a href="../02_数据表/B_匹配DID逐案例.csv" download>下载逐案例比较 ↗</a> · <a href="../../任务三_专题深挖/三篇旗舰专题_研究闭环.html">查看反证条件 ↗</a>''')
scores=pd.read_csv(D/'任务四_开放创作/05_满分升级/13_统一条件消融总表/统一条件消融评分.csv')
short={'透明基线_赛前奖牌池':'透明基线','混合核心_赛前奖牌池':'加入项目模型','混合核心_加主场':'再加入主场','混合核心_资格受限':'资格压力情景'}
rows=''
for _,r in scores.iterrows():
    rows+=f'<tr data-rc-year="{r.Year}"><th scope="row">{short[r.阶段]}</th><td><span class="rc-bar" style="--rc-width:{r.MAE/3.2*100:.2f}%"></span>{r.MAE:.4f}</td><td>{r.相对基线MAE变化:+.4f}</td><td>{r.相对上阶段MAE变化:+.4f}</td></tr>'
t4=section('模型更复杂，预测就更准吗？','把同一届的代表团、实际值和赛前估计奖牌池固定，再逐步加入模型组成。',f'''<label class="rc-control">回放届次 <select data-rc-year-select><option>2012</option><option>2016</option><option selected>2024</option></select></label><p data-rc-verdict aria-live="polite"></p><div class="rc-scroll" tabindex="0" aria-label="模型消融误差表"><table class="rc-table"><thead><tr><th>阶段</th><th>平均绝对误差（枚/队）</th><th>较基线变化</th><th>较上阶段变化</th></tr></thead><tbody>{rows}</tbody></table></div><p>误差越低越好；负的变化表示改善。2012、2016实际为历史小项代理，2024为官方小项奖牌。不同届次不混成同一个总分。</p><details><summary>为什么资格情景和新增排名不能算作稳定预测收益？</summary><p>资格受限是排除预设身份代码的压力模拟，不是当时已知的部署策略。新增排名缺三届统一快照，不能填0冒充验证；独立2016橄榄球类比回放仅使MAE从2.1698降至2.1691。主场率三届均触及18%上限；权重尚未证明最优，基线区间也不是最终集成的已校准区间。</p></details><a href="05_满分升级/13_统一条件消融总表/统一条件消融评分.csv" download>下载12组同条件评分 ↗</a> · <a href="05_满分升级/13_统一条件消融总表/逐队配对误差.csv" download>下载逐队误差 ↗</a>''')

pages={'任务一_数据体检/index.html':t1,'任务二_百年全景/05_交互总览/index.html':t2,'任务三_专题深挖/统一中文入口/index.html':t3,'任务四_开放创作/index.html':t4}
import re,os
for name,markup in pages.items():
    path=D/name;s=path.read_text(encoding='utf-8')
    s=re.sub(r'<!-- RESEARCH_CLOSURE_START -->.*?<!-- RESEARCH_CLOSURE_END -->','',s,flags=re.S)
    # Insert into the existing narrative flow without reserializing the page.
    marker='<div class="narrative-flow">'
    assert marker in s
    s=s.replace(marker,marker+'<!-- RESEARCH_CLOSURE_START -->'+markup+'<!-- RESEARCH_CLOSURE_END -->',1)
    prefix=os.path.relpath(D/'共享组件',path.parent).replace('\\','/')
    if 'research-closure.css' not in s:
        s=s.replace('</head>',f'<link rel="stylesheet" href="{prefix}/research-closure.css?v=1"></head>',1)
        s=s.replace('</body>',f'<script defer src="{prefix}/research-closure.js?v=1"></script></body>',1)
    path.write_text(s,encoding='utf-8')
print('Integrated research into four task pages.')

# Refresh the complete web reading edition after material updates.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_flagship_reading.py")))
