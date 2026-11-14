"""Give the ten Task-3 stories distinct, offline visual treatments and motion."""
from pathlib import Path
import json, math, html

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT/'交付文件'/'任务三_专题深挖'

ITEMS = [
 ('S1_东道主效应/index.html','lab'),
 ('S2_口径的魔力/06_滚动叙事专题/index.html','press'),
 ('S3_地缘政治的投影/index.html','archive'),
 ('S4_小代表团的大突破/index.html','islands'),
 ('S5_奖牌的通货膨胀/index.html','timeline'),
 ('S6_王者与传奇/index.html','portrait'),
 ('S3_冠军的保质期/06_冠军王朝时间轴/index.html','cinema'),
 ('S8_她们登上领奖台/index.html','editorial'),
 ('S9_消失的赛场/index.html','museum'),
 ('S10_奖牌藏在哪些项目/index.html','atlas'),
]

def plot(kind, rows):
    if not rows:return ''
    vals=[float(x['value']) for x in rows]
    vmax=max(vals) or 1
    n=len(rows)
    pts=[(30+i*740/max(1,n-1),190-150*v/vmax) for i,v in enumerate(vals)]
    def path(points):return ' '.join(('M' if i==0 else 'L')+f'{x:.1f},{y:.1f}' for i,(x,y) in enumerate(points))
    if kind in ('archive','timeline','editorial'):
        poly=path(pts)
        marks=''.join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 if kind!="archive" else 7}"/>' for x,y in pts)
        fill=f'<path class="fill" d="{poly} L770,205 L30,205 Z"/>' if kind=='editorial' else ''
        return f'<svg viewBox="0 0 800 220" role="img" aria-label="{kind}专题数据趋势预览"><path class="gridline" d="M30 205H770 M30 120H770 M30 40H770"/>{fill}<path class="trace" d="{poly}"/>{marks}</svg>'
    if kind=='islands':
        circles=''.join(f'<g class="bubble" style="--i:{i}"><circle cx="{85+(i%4)*205}" cy="{70+(i//4)*95}" r="{13+36*math.sqrt(v/vmax):.1f}"/><text x="{85+(i%4)*205}" y="{76+(i//4)*95}">{html.escape(str(r["label"]))}</text></g>' for i,(r,v) in enumerate(zip(rows,vals)))
        return f'<svg viewBox="0 0 800 230" role="img" aria-label="小代表团获奖记录气泡图">{circles}</svg>'
    if kind=='portrait':
        circles=''.join(f'<g class="medallion" style="--i:{i}"><circle cx="{65+(i%6)*133}" cy="{60+(i//6)*110}" r="{18+24*v/vmax:.1f}"/><text x="{65+(i%6)*133}" y="{67+(i//6)*110}">{int(v)}</text></g>' for i,v in enumerate(vals))
        return f'<svg viewBox="0 0 800 230" role="img" aria-label="姓名记录金牌行数圆章阵列">{circles}</svg>'
    if kind=='museum':
        glyphs=''.join(f'<g class="artifact" style="--i:{i}"><rect x="{20+(i%7)*112}" y="{20+(i//7)*105}" width="94" height="88" rx="3"/><text x="{67+(i%7)*112}" y="{72+(i//7)*105}">{int(v)}</text></g>' for i,v in enumerate(vals))
        return f'<svg viewBox="0 0 800 230" role="img" aria-label="项目出现届数展柜预览">{glyphs}</svg>'
    if kind=='atlas':
        blocks=''.join(f'<rect class="atlas-block" style="--i:{i}" x="{22+(i%8)*97}" y="{25+(i//8)*105}" width="{75+15*v/vmax:.1f}" height="{42+42*v/vmax:.1f}" rx="10"/>' for i,v in enumerate(vals))
        return f'<svg viewBox="0 0 800 230" role="img" aria-label="项目获奖记录矩形图谱">{blocks}</svg>'
    return ''

SHARED = '''<style id="task3-art-direction">
html{scroll-behavior:smooth}body{overflow-x:hidden}a,button{touch-action:manipulation}button:focus-visible,a:focus-visible{outline:3px solid #e6a847;outline-offset:4px}
.art-progress{position:fixed;top:0;left:0;height:4px;width:0;z-index:99999;background:linear-gradient(90deg,#e9a65e,#79c7cb);box-shadow:0 0 16px #e9a65e66;pointer-events:none}
.art-figure{position:relative;max-width:980px;margin:0 auto 0;padding:2vw 4vw 5vw;z-index:2}.art-figure svg{display:block;width:100%;height:auto;overflow:visible}.art-figure .trace{fill:none;stroke:var(--a,#d8b671);stroke-width:4;stroke-linecap:round;stroke-linejoin:round;stroke-dasharray:1300;stroke-dashoffset:1300;animation:draw-trace 2.3s cubic-bezier(.22,1,.36,1) .25s forwards}.art-figure circle{fill:var(--a,#d8b671)}.art-figure .gridline{fill:none;stroke:currentColor;opacity:.18;stroke-dasharray:4 8}.art-figure .fill{fill:var(--a,#d8b671);opacity:.18}.art-figure text{font:700 16px 'Microsoft YaHei',sans-serif;text-anchor:middle;fill:var(--bg,#172e38)}.art-figure .bubble circle{opacity:.65;stroke:var(--bg);stroke-width:2}.art-figure .medallion circle{fill:none;stroke:var(--a);stroke-width:3}.art-figure .medallion text{font-size:24px}.art-figure .artifact rect{fill:#fff;stroke:var(--a);stroke-width:3}.art-figure .artifact text{font-size:30px}.art-figure .atlas-block{fill:var(--a);opacity:.55;transform-box:fill-box;transform-origin:center;animation:atlas-pop .7s cubic-bezier(.2,1.4,.3,1) both;animation-delay:calc(var(--i)*55ms)}
.art-figure .bubble,.art-figure .medallion,.art-figure .artifact{transform-box:fill-box;transform-origin:center;animation:atlas-pop .7s cubic-bezier(.2,1.4,.3,1) both;animation-delay:calc(var(--i)*80ms)}
.bar{transition:transform .3s ease,background .3s ease,box-shadow .3s ease}.bar:hover{transform:translateX(7px)}.bar .track i{transform-origin:left;animation:grow-bar 1.1s cubic-bezier(.2,.9,.2,1) both;animation-delay:calc(var(--i,0)*35ms)}.bar:nth-child(2n) .track i{filter:brightness(.88)}
header h1{animation:title-rise .85s cubic-bezier(.16,1,.3,1) both}header .lead{animation:title-rise .9s cubic-bezier(.16,1,.3,1) .12s both}aside{transition:transform .35s ease,box-shadow .35s ease}aside:hover{transform:translateY(-5px);box-shadow:0 26px 65px #0002}.evidence article{transition:transform .3s ease,box-shadow .3s ease}.evidence article:hover{transform:translateY(-5px);box-shadow:0 16px 35px #0002}
@keyframes draw-trace{to{stroke-dashoffset:0}}@keyframes grow-bar{from{transform:scaleX(0)}to{transform:scaleX(1)}}@keyframes title-rise{from{opacity:0;transform:translateY(28px)}to{opacity:1;transform:translateY(0)}}@keyframes atlas-pop{from{opacity:0;transform:scale(.4)}to{opacity:1;transform:scale(1)}}
body.archive .art-figure{background:linear-gradient(90deg,transparent 49.8%,#d8b67133 50%,transparent 50.2%)}body.archive .bar .label{font-family:Georgia,'SimSun',serif;font-weight:700}body.archive .evidence article{border-radius:0;background:#f8f5ec;box-shadow:8px 8px 0 #d8b67155}body.archive header:before{content:'ARCHIVE 1980—1984';position:absolute;right:4vw;bottom:4vw;opacity:.18;font:900 35px Georgia;transform:rotate(-9deg)}
body.islands .art-figure{border-radius:50% 50% 0 0;background:radial-gradient(circle at 50% 90%,#91dfc933,transparent 62%)}body.islands .evidence article{border-radius:28px 6px 28px 6px}body.islands header:before{content:'';position:absolute;width:24vw;height:24vw;border:2px dashed #ffffff44;border-radius:50%;right:8vw;top:7vh;animation:orbit 28s linear infinite}
body.timeline .art-figure{background:repeating-linear-gradient(90deg,transparent 0 9%,#9b5e631a 9.1% 9.2%)}body.timeline .bar{border-left:3px solid var(--a)}body.timeline .evidence article{background:#42293b;color:#fff;border-color:#f1a060}body.timeline .evidence span{color:#ffbb7c}
body.portrait .art-figure{background:radial-gradient(circle,#d4a44733,transparent 66%)}body.portrait .evidence article{background:#2e1e28;color:#f7efe7;border:1px solid #d4a447}body.portrait .evidence span{color:#d4a447}body.portrait .bar{border-radius:4px;box-shadow:inset 0 0 0 1px #d4a44733;margin-bottom:5px}
body.editorial .art-figure{border-top:1px solid var(--a);border-bottom:1px solid var(--a)}body.editorial .fill{opacity:.28}body.editorial .bar:hover{background:#e58bb81c}body.editorial .evidence article{background:transparent;border:0;border-top:4px solid var(--a);box-shadow:none}
body.museum .art-figure{background:#eae9d4;border:14px solid #e1dfc3;box-shadow:inset 0 0 0 1px #65724e44}body.museum .bar:hover{transform:translateY(-7px) rotate(-1deg)}body.museum .evidence article{background:#fbfaf1;border:1px solid #99a278}
body.atlas .art-figure{background:radial-gradient(circle at 20% 25%,#75c9d044,transparent 35%),radial-gradient(circle at 75% 80%,#75c9d022,transparent 38%)}body.atlas .bar{border-bottom:1px dotted #2c8ba766}body.atlas .evidence article{border-radius:12px;background:#e1f2f1}
@keyframes orbit{to{transform:rotate(360deg)}}
@media(max-width:800px){.art-figure{padding:20px 4vw}.art-figure text{font-size:12px}body.archive header:before{font-size:16px}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.art-figure *,header h1,header .lead,.bar .track i,body.islands header:before{animation:none!important;transition:none!important;stroke-dashoffset:0!important}.bar:hover,.evidence article:hover,aside:hover{transform:none!important}}
</style>'''

SCRIPT = '''<script id="task3-art-script">(()=>{const d=document,b=d.createElement('div');b.className='art-progress';d.body.append(b);let busy=false;function update(){if(busy)return;busy=true;requestAnimationFrame(()=>{const max=d.documentElement.scrollHeight-innerHeight;b.style.width=(max>0?scrollY/max*100:0)+'%';busy=false})}addEventListener('scroll',update,{passive:true});update();d.querySelectorAll('.bar').forEach((x,i)=>x.style.setProperty('--i',i));})();</script>'''

for rel,kind in ITEMS:
    file=BASE/rel
    if not file.exists():raise FileNotFoundError(file)
    s=file.read_text(encoding='utf-8')
    if 'id="task3-art-direction"' in s:
        start=s.find('<style id="task3-art-direction">');end=s.find('</style>',start)+8;s=s[:start]+s[end:]
    if 'id="task3-art-script"' in s:
        start=s.find('<script id="task3-art-script">');end=s.find('</script>',start)+9;s=s[:start]+s[end:]
    if 'id="task3-legacy-polish"' in s:
        start=s.find('<style id="task3-legacy-polish">');end=s.find('</style>',start)+8;s=s[:start]+s[end:]
    s=s.replace('</head>',SHARED+'</head>',1)
    if kind not in ('lab','press','cinema'):
        rows=json.loads((file.parent/'分析数据.json').read_text(encoding='utf-8'))
        art=plot(kind,rows)
        if 'class="art-figure"' in s:
            start=s.find('<div class="art-figure">');end=s.find('</div>',start)+6;s=s[:start]+s[end:]
        s=s.replace('<main>','<div class="art-figure">'+art+'</div><main>',1)
    else:
        # Established long-form experiences keep their own interaction systems.
        theme={'lab':'#bd723f','press':'#c29b52','cinema':'#6299a6'}[kind]
        extra=f'<style id="task3-legacy-polish">body{{--a:{theme}}}main section{{transition:box-shadow .35s ease}}main section:hover{{box-shadow:inset 0 0 0 1px {theme}33}}a[href]{{transition:color .2s,transform .2s}}a[href]:hover{{color:{theme}}}</style>'
        s=s.replace('</head>',extra+'</head>',1)
    s=s.replace('</body>',SCRIPT+'</body>',1)
    file.write_text(s,encoding='utf-8')

# The portal is a chapter wall, not another copy of a conventional card grid.
portal=BASE/'统一中文入口'/'index.html'
s=portal.read_text(encoding='utf-8')
wall='''<style id="task3-wall-design">.ten-section{background:#efece5!important;position:relative;overflow:hidden;opacity:1!important;transform:none!important}.ten-section:before{content:'10';position:absolute;font-size:clamp(240px,40vw,620px);font-weight:900;line-height:1;color:#d5ded833;right:-4vw;top:-4vw;pointer-events:none}.ten-section>div,.ten-section>h2,.ten-section>p{position:relative}.ten-grid{grid-template-columns:repeat(12,minmax(0,1fr))!important;gap:14px!important;position:relative}.ten-card{grid-column:span 4;min-height:290px!important;border:0!important;border-radius:0 25px 0 25px;background:#fffdf8!important;position:relative;overflow:hidden;box-shadow:0 8px 22px #203a3920;transition:transform .45s cubic-bezier(.2,1,.3,1),box-shadow .45s!important}.ten-card:before{content:'';position:absolute;width:170px;height:170px;right:-70px;top:-70px;border-radius:50%;background:var(--tone);opacity:.16;transition:transform .5s}.ten-card:hover:before{transform:scale(1.75)}.ten-card:hover{transform:translateY(-10px) rotate(-.6deg)!important;box-shadow:0 25px 55px #203a3940}.ten-card:nth-child(1),.ten-card:nth-child(7){grid-column:span 5}.ten-card:nth-child(2),.ten-card:nth-child(8){grid-column:span 7}.ten-card:nth-child(2){background:#283139!important;color:#fff}.ten-card:nth-child(7){background:#1d3940!important;color:#fff}.ten-card:nth-child(3){border-radius:80px 0 0 0}.ten-card:nth-child(4){border-radius:0 80px 0 0}.ten-card:nth-child(5){background:#f4d9c8!important}.ten-card:nth-child(6){background:#e5dccb!important}.ten-card:nth-child(8){background:#f3e5ec!important}.ten-card:nth-child(9){background:#e7eadb!important}.ten-card:nth-child(10){background:#d9edef!important}.ten-card span{font-size:18px!important}.ten-card h3{font-size:clamp(26px,3vw,40px)!important;position:relative}.ten-card b{position:absolute;bottom:30px;left:32px}.ten-card p{max-width:460px;position:relative}.ten-section h2{letter-spacing:-.06em}@media(max-width:850px){.ten-card,.ten-card:nth-child(n){grid-column:span 6}}@media(max-width:600px){.ten-grid{grid-template-columns:1fr!important}.ten-card,.ten-card:nth-child(n){grid-column:auto;min-height:240px!important}}@media(prefers-reduced-motion:reduce){.ten-card,.ten-card:before{transition:none!important}.ten-card:hover{transform:none!important}}</style>'''
if 'id="task3-wall-design"' in s:
    start=s.find('<style id="task3-wall-design">');end=s.find('</style>',start)+8;s=s[:start]+s[end:]
wall=wall.replace('</style>','.ten-card:nth-child(10){grid-column:span 12;min-height:210px!important;background:linear-gradient(115deg,#d9edef,#badde2)!important}.ten-card:nth-child(2) b,.ten-card:nth-child(7) b{color:#ffd393}@media(max-width:600px){.ten-card:nth-child(10){grid-column:auto}}</style>')
s=s.replace('</head>',wall+'</head>',1)
portal.write_text(s,encoding='utf-8')
print('Upgraded',len(ITEMS),'topic designs and portal')
