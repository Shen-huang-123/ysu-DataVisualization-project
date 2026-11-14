"""Targeted wording corrections; idempotent and deliberately not global."""
from pathlib import Path
root=Path(__file__).resolve().parents[2]
edits={
 '交付文件/任务三_专题深挖/十专题深度核验.md':[
  ('并用 2008、2012、2016 的官方核验表检查机制是否跨届出现。历史相关高说明结构稳定，不意味着任一口径天然更公平。','；2008、2012、2016仅用 NOC–Event–Medal 历史代理做数据内部探索，不能称为现行 IOC 逐项核验或独立机制验证。'),
  ('| 跨届机制相关 | 0.982—0.991 | 2008、2012、2016 三届多人组占比与膨胀倍率的 Spearman 相关 |','| 历史代理内部相关 | 0.982—0.991 | 2008、2012、2016 三届多人组占比与膨胀倍率共享金牌行信息；不构成独立验证 |')],
 '交付文件/任务三_专题深挖/十专题深度核验.html':[
  ('并用 2008、2012、2016 的官方核验表检查机制是否跨届出现。历史相关高说明结构稳定，不意味着任一口径天然更公平。','；2008、2012、2016仅用 NOC–Event–Medal 历史代理做数据内部探索，不能称为现行 IOC 逐项核验或独立机制验证。'),
  ('跨届机制相关','历史代理内部相关')],
 '交付文件/任务三_专题深挖/十专题深度核验.json':[
  ('并用 2008、2012、2016 的官方核验表检查机制是否跨届出现。历史相关高说明结构稳定，不意味着任一口径天然更公平。','；2008、2012、2016仅用 NOC–Event–Medal 历史代理做数据内部探索，不能称为现行 IOC 逐项核验或独立机制验证。')],
 '交付文件/任务三_专题深挖/00_先看这里.md':[
  ('并用2008、2012、2016跨届验证解释重排机制','；2008、2012、2016仅作历史代理内部探索')],
 '交付文件/任务三_专题深挖/00_先看这里.html':[
  ('并用2008、2012、2016跨届验证解释重排机制','；2008、2012、2016仅作历史代理内部探索')],
 '交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html':[
  ('北京2008官方结果','北京2008 IOC 页面入口'),('伦敦2012官方结果','伦敦2012 IOC 页面入口'),('里约2016官方结果','里约2016 IOC 页面入口')]
}
for rel,rules in edits.items():
 p=root/rel;s=p.read_text(encoding='utf-8');before=s
 for old,new in rules:s=s.replace(old,new)
 if s!=before:p.write_text(s,encoding='utf-8');print('updated',rel)
portal=root/'交付文件/任务三_专题深挖/统一中文入口/index.html'
s=portal.read_text(encoding='utf-8')
if '12_反例与证据链/index.html' not in s:
 entry='<a href="../12_反例与证据链/index.html" style="display:block;max-width:1140px;margin:36px auto;padding:26px 30px;border-top:2px solid #bb8d65;border-bottom:1px solid #bb8d65;color:inherit;text-decoration:none"><small style="color:#a46c47">新增研究方法 · 十专题</small><strong style="display:block;font-size:27px;margin:5px 0">反例与证据链 ↗</strong><span>两处协会网页错误，以及十个专题如何从原判断走向修正结论。</span></a>'
 s=s.replace('</body>',entry+'</body>');portal.write_text(s,encoding='utf-8');print('linked',portal)
dashboard=root/'交付文件/任务二_百年全景/05_交互总览/index.html'
s=dashboard.read_text(encoding='utf-8')
old='<span>图中数值随当前筛选条件变化；悬停节点可查看具体值。</span><span>参赛记录与奖牌记录是不同统计单位。</span>'
new='<span>单位随指标切换：参赛记录或获奖运动员行；悬停节点可查看具体值。</span><span>来源：任务一归一数据。1906排除；2020起 Event 泛化，不据此计官方小项。</span>'
if old in s:
 dashboard.write_text(s.replace(old,new),encoding='utf-8');print('updated chart provenance',dashboard)
task4=root/'交付文件/任务四_开放创作/index.html'
s=task4.read_text(encoding='utf-8')
style='<style id="evidence-note-dark-fix">body.xz-dark aside[role="note"]{background:#19383c!important;color:#eef4eb!important;border-color:#6e918e!important}body.xz-dark aside[role="note"] p{color:#dce9e5!important}body.xz-dark aside[role="note"] a{color:#b8e3e3!important}</style>'
if 'evidence-note-dark-fix' not in s:
 task4.write_text(s.replace('</head>',style+'</head>'),encoding='utf-8');print('fixed dark note',task4)
counter=root/'交付文件/任务三_专题深挖/12_反例与证据链/index.html'
s=counter.read_text(encoding='utf-8')
if '两处协会页面错误_证据链.png' not in s:
 img='<img src="两处协会页面错误_证据链.png" alt="伦敦2012游泳和北京2008跆拳道的原判断、官方成绩册复核与修正决定" style="display:block;width:100%;height:auto;margin:40px 0 15px;border:1px solid #c9d0ca;border-radius:12px">'
 s=s.replace('</p><section class="case">','</p>'+img+'<section class="case">',1)
 counter.write_text(s,encoding='utf-8');print('linked evidence chart',counter)
topic_portal=root/'交付文件/任务三_专题深挖/统一中文入口/index.html'
s=topic_portal.read_text(encoding='utf-8')
hero_fix='<style id="topic-hero-contrast-fix">body.hero-motion-portal header.hero{background-image:linear-gradient(90deg,#0b252ae8 0%,#0d2b31d9 53%,#0e30379c 100%),url("../媒体/growth.jpg")!important;background-size:cover!important;background-position:center!important;color:#f8f4ea!important}body.hero-motion-portal header.hero h1,body.hero-motion-portal header.hero p{color:#f8f4ea!important;text-shadow:0 3px 18px #071c20cc!important}body.hero-motion-portal header.hero h1 em{color:#f1c483!important}body.hero-motion-portal header.hero .hero-foot{color:#edf2ee!important}@media(max-width:700px){body.hero-motion-portal header.hero{background-position:57% center!important}body.hero-motion-portal header.hero .hero-graphic,body.hero-motion-portal header.hero .ed-rings-scene{display:none!important}body.hero-motion-portal header.hero .hero-foot{font-size:10px!important;letter-spacing:.02em!important}}</style>'
if 'topic-hero-contrast-fix' not in s:
 topic_portal.write_text(s.replace('</head>',hero_fix+'</head>'),encoding='utf-8');print('fixed portal hero',topic_portal)
elif hero_fix not in s:
 import re
 s=re.sub(r'<style id="topic-hero-contrast-fix">.*?</style>',hero_fix,s,flags=re.S)
 topic_portal.write_text(s,encoding='utf-8');print('updated portal mobile hero',topic_portal)
s=topic_portal.read_text(encoding='utf-8')
if 'TASK 03 / OLYMPIC DATA STORIES' in s:
 topic_portal.write_text(s.replace('TASK 03 / OLYMPIC DATA STORIES','专题深挖 / 十个奥运数据故事'),encoding='utf-8');print('localized portal hero',topic_portal)
