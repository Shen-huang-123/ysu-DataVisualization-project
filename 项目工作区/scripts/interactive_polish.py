"""Question-led visual polish for the interactive deliverable pages."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'
PAGES={
 '任务一_数据体检/index.html':('audit','这份数据，哪些地方值得先核对？','从质量决定开始，再看统计口径如何改变结论。'),
 '任务三_专题深挖/S2_口径的魔力/06_交互榜/index.html':('ranking','换一把尺子，榜单会怎样变化？','选择一种奖牌计数口径，再比较同一批代表团的名次。'),
 '任务三_专题深挖/S2_口径的魔力/07_口径实验室/index.html':('lab','把计数规则推到两端','拖动权重，观察换位阈值；中间值是敏感性实验。'),
 '任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html':('dynasty','连续夺冠能维持几届？','先选运动和年代，再读生存曲线与最长王朝。'),
 '任务四_开放创作/01_交互式Dashboard/index.html':('forecast','2028 奖牌预测，换个情景再看','切换新增项目情景，查看代表团点估计与不确定性区间。'),
}
START='<!-- INTERACTIVE_POLISH_START -->';END='<!-- INTERACTIVE_POLISH_END -->'
CSS='''<style id="interactive-polish-style">
body.interactive-polish{--ip:#176d78;--ip-dark:#123b45;--ip-soft:#e7f0ed;--ip-paper:#fffefa}
body.ip-audit{--ip:#9b6339;--ip-dark:#3f342d;--ip-soft:#eee6da}
body.ip-ranking{--ip:#137e84;--ip-dark:#103c45;--ip-soft:#e4f1ec}
body.ip-lab{--ip:#9c4b65;--ip-dark:#443341;--ip-soft:#f4e8ed}
body.ip-dynasty{--ip:#536582;--ip-dark:#26374f;--ip-soft:#e9ecf3}
body.ip-forecast{--ip:#aa663b;--ip-dark:#183c49;--ip-soft:#f3e8dc}
/* Keep content readable without waiting for a scroll observer to reveal it. */
body.interactive-polish .xz-reveal,body.interactive-polish .xz-reveal *{opacity:1!important;visibility:visible!important;transform:none!important}
body.interactive-polish main{position:relative}
body.interactive-polish .ip-context{display:grid;grid-template-columns:minmax(0,1fr) minmax(260px,420px);gap:30px;align-items:end;margin:0 0 28px;padding:0 0 24px;border-bottom:1px solid #b9c9c4}
body.interactive-polish .ip-context small,body.interactive-polish .ip-eyebrow{display:block;color:var(--ip)!important;font-size:12px;font-weight:900;letter-spacing:.15em;margin:0 0 9px}
body.interactive-polish .ip-context h2{margin:0;color:var(--ip-dark);font:600 clamp(31px,3.4vw,52px)/1.1 Georgia,'Songti SC','SimSun',serif;letter-spacing:-.045em}
body.interactive-polish .ip-context p{margin:0;color:#526a6c;font-size:15px;line-height:1.7}
body.interactive-polish :is(.controls,.控制,.xz-toolbar){border:1px solid #cadad5!important;background:var(--ip-soft)!important;border-radius:18px!important;padding:18px 20px!important;box-shadow:none!important}
body.interactive-polish :is(.controls,.控制,.xz-toolbar) :is(label,small){font-weight:700}
body.interactive-polish :is(select,input:not([type=range])){border-color:#b9cbc7!important;background:#fffefa!important;min-height:45px}
body.interactive-polish :is(select,input,button):focus-visible{outline:3px solid #e6a95c!important;outline-offset:2px!important}
body.interactive-polish :is(.card,.卡,.xz-kpis article){border:1px solid #d3dfd9!important;background:var(--ip-paper)!important;border-radius:16px!important;box-shadow:0 10px 28px rgba(24,54,58,.06)!important}
body.interactive-polish :is(.metric,.big,.大数,.xz-kpis strong){color:var(--ip)!important;font-variant-numeric:tabular-nums}
body.interactive-polish table{border-collapse:separate;border-spacing:0;background:#fffefa;border:1px solid #d7e1dc;border-radius:16px;overflow:hidden;box-shadow:0 12px 28px rgba(25,50,57,.06)}
body.interactive-polish thead{background:var(--ip-dark)!important}body.interactive-polish thead th{background:transparent!important;color:#eff8f5!important;border:0!important;font-size:12px!important;letter-spacing:.06em}
body.interactive-polish tbody tr{opacity:1!important;visibility:visible!important;transform:none!important}body.interactive-polish tbody tr:nth-child(even){background:#f2f7f4}body.interactive-polish tbody tr:hover{background:var(--ip-soft)!important}
body.interactive-polish :is(td,th){padding:12px 14px!important}
body.interactive-polish main>section{scroll-margin-top:85px}
body.ip-audit .xz-section{padding-top:62px!important;padding-bottom:68px!important}body.ip-audit .xz-section-top{border-left:3px solid var(--ip);padding-left:18px}body.ip-audit .xz-kpis article:first-child{background:var(--ip-dark)!important}body.ip-audit .xz-kpis article:first-child :is(strong,span){color:#fff!important}
body.ip-ranking main.wrap{max-width:1240px!important;padding-top:72px!important}body.ip-ranking .controls{display:flex;align-items:end;gap:12px;flex-wrap:wrap;margin:0 0 18px!important}body.ip-ranking .ip-field{display:grid;gap:7px;color:#43656b;font-size:12px;font-weight:800}body.ip-ranking .ip-field select{min-width:150px}body.ip-ranking .cards{display:grid!important;grid-template-columns:repeat(3,1fr)!important;gap:12px!important;margin:0 0 24px!important}body.ip-ranking .cards .card{min-height:122px;padding:18px 20px!important}body.ip-ranking .cards .card:first-child{background:var(--ip-dark)!important}body.ip-ranking .cards .card:first-child :is(small,.big){color:#fff!important}body.ip-ranking table{width:100%}body.ip-ranking #xz-extra-controls{margin:0 0 0 auto!important}
body.ip-lab main.wrap,body.ip-dynasty main.wrap{max-width:1180px!important;padding-top:72px!important}body.ip-lab main>section,body.ip-dynasty main>section{margin:0 0 62px!important;padding:0 0 60px!important;border-bottom:1px solid #cbd8d3!important}body.ip-lab main>section:last-child,body.ip-dynasty main>section:last-child{border:0!important}body.ip-lab main>section h2,body.ip-dynasty main>section h2{font-family:Georgia,'Songti SC','SimSun',serif;font-size:clamp(32px,3.4vw,48px)!important;letter-spacing:-.04em;margin:0 0 12px!important;color:var(--ip-dark)}body.ip-lab .grid,body.ip-dynasty .grid{gap:12px!important;margin-top:18px!important}body.ip-lab .grid .card,body.ip-dynasty .grid .card{padding:22px!important}body.ip-lab .grid .card:first-child,body.ip-dynasty .grid .card:first-child{background:var(--ip-dark)!important}body.ip-lab .grid .card:first-child *,body.ip-dynasty .grid .card:first-child *{color:#fff!important}body.ip-lab .scroll,body.ip-dynasty .scroll{border-radius:16px;overflow:auto}body.ip-dynasty .chart{background:#fffefa;border:1px solid #d4dfdb;border-radius:18px;padding:22px;box-shadow:0 12px 32px rgba(25,54,58,.06)}
body.ip-forecast main.包{width:100%!important;max-width:none!important;margin-inline:0!important;padding-inline:clamp(24px,6vw,100px)!important;padding-top:76px!important;min-width:0}body.ip-forecast .卡组{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:12px!important;margin:0 0 28px!important}body.ip-forecast .卡组 .卡{padding:22px!important;min-height:130px!important}body.ip-forecast .卡组 .卡:first-child{background:var(--ip-dark)!important}body.ip-forecast .卡组 .卡:first-child *{color:#fff!important}body.ip-forecast .控制{display:flex!important;gap:10px;flex-wrap:wrap;margin:0 0 24px!important}body.ip-forecast .榜 .行:nth-child(-n+3){background:rgba(212,170,100,.10);border-radius:8px}body.ip-forecast #xz-model-compare{opacity:1!important;visibility:visible!important;transform:none!important;border-top:2px solid var(--ip)!important;margin-top:55px!important;padding-top:55px!important}
@media(max-width:800px){body.interactive-polish .ip-context{grid-template-columns:1fr;gap:8px}body.ip-ranking .cards,body.ip-lab .grid,body.ip-dynasty .grid{grid-template-columns:1fr!important}body.ip-forecast .卡组{grid-template-columns:repeat(2,minmax(0,1fr))!important}body.ip-ranking #xz-extra-controls{margin:0!important}}
@media(max-width:600px){body.interactive-polish .ip-context h2{font-size:32px}body.interactive-polish :is(td,th){padding:9px 8px!important;font-size:12px!important}body.ip-ranking main.wrap,body.ip-lab main.wrap,body.ip-dynasty main.wrap,body.ip-forecast main.包{padding-top:52px!important}body.ip-ranking .controls{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}body.ip-ranking .ip-field select{min-width:0;width:100%}body.ip-ranking #xz-extra-controls{grid-column:1/-1}body.ip-ranking .cards{grid-template-columns:repeat(2,minmax(0,1fr))!important}body.ip-ranking .cards .card:first-child{grid-column:1/-1}body.ip-forecast .卡组 .卡{padding:15px!important;min-height:108px!important}}
</style>'''

for rel,(kind,question,explain) in PAGES.items():
 p=BASE/rel;s=p.read_text(encoding='utf-8')
 s=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',s,flags=re.S)
 def bodyclass(m):
  tag=m.group(0); classes='interactive-polish ip-'+kind
  if 'class="' in tag:return tag.replace('class="','class="'+classes+' ',1) if 'interactive-polish' not in tag else tag
  return tag[:-1]+' class="'+classes+'">'
 s=re.sub(r'<body\b[^>]*>',bodyclass,s,count=1)
 if kind=='ranking':
  if 'class="ip-context"' not in s:
   intro=f'<div class="ip-context"><div><small>INTERACTIVE RANKING / 2024</small><h2>{question}</h2></div><p>{explain}</p></div>'
   s=s.replace('<main class="wrap">','<main class="wrap">'+intro,1)
   for sid,label in [('lens','统计口径'),('sort','排序方式'),('limit','显示数量')]:
    s=re.sub(r'(<select id="'+sid+r'"[^>]*>.*?</select>)',lambda m:'<label class="ip-field"><span>'+label+'</span>'+m.group(1)+'</label>',s,count=1,flags=re.S)
 elif kind=='forecast':
  if 'class="ip-context"' not in s:
   intro=f'<div class="ip-context"><div><small>SCENARIO STUDIO / LA 2028</small><h2>{question}</h2></div><p>{explain}</p></div>'
   s=s.replace('<main class="包">','<main class="包">'+intro,1)
 elif kind in ('lab','dynasty'):
  if 'class="ip-eyebrow"' not in s:
   nums=['01 / 设置观察条件','02 / 阅读结果','03 / 查看构成']
   i=[0]
   def heading(m):
    n=i[0];i[0]+=1;return '<section><span class="ip-eyebrow">'+nums[min(n,2)]+'</span><h2>'
   s=re.sub(r'<section><h2>',heading,s,count=3)
 elif kind=='audit':
  if 'class="ip-context"' not in s:
   intro=f'<div class="ip-context"><div><small>DATA AUDIT / 01</small><h2>{question}</h2></div><p>{explain}</p></div>'
   s=s.replace('<main class="xz-container">','<main class="xz-container">'+intro,1)
 s=s.replace('</head>',START+CSS+END+'</head>',1)
 p.write_text(s,encoding='utf-8')
 print(rel)
