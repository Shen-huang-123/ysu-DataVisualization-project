"""Final Olympic editorial finish for the static competition website."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
SITE = ROOT / '项目工作区' / 'sites' / 'la28-fullscore' / 'dist'

STYLE = '''<style id="olympic-premium-finish">
/* One editorial system: archival imagery, stadium geometry, disciplined spacing. */
:root{--of-paper:#f2f0e9;--of-ink:#132b32;--of-line:#b8c8c3;--of-gold:#c2a36b;--of-aqua:#83c3c3}
html{scroll-padding-top:84px}
body{font-family:'Noto Sans SC','Microsoft YaHei',system-ui,sans-serif;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}
body:not(.xz-dark){--of-ground:#f2f0e9;--of-panel:#fbfaf5;--of-type:#132b32;--of-secondary:#52686b;--of-stroke:#c4d0ca}
body.xz-dark{--of-ground:#0c2028;--of-panel:#17313a;--of-type:#f0f3ec;--of-secondary:#bbd1ca;--of-stroke:#47636a}
/* Venue light and lane geometry give each chapter its own atmosphere. */
body.ed-module-0{--of-glow:#c9b685;--of-glow-2:#8eb8b2}
body.ed-module-1{--of-glow:#d7bd86;--of-glow-2:#b5cec8}
body.ed-module-2{--of-glow:#9cbfc5;--of-glow-2:#d9c6a1}
body.ed-module-3{--of-glow:#b8b5d0;--of-glow-2:#d6b5ac}
body.ed-module-4{--of-glow:#dfb196;--of-glow-2:#9ec4c2}
body.story-experience{--of-glow:var(--story-accent);--of-glow-2:#c8b99f}
body:not(.xz-dark){background-color:#f2f0e9!important;background-image:radial-gradient(ellipse 65vw 48vw at 93% 7%,color-mix(in srgb,var(--of-glow,#c9b685) 25%,transparent),transparent 70%),radial-gradient(ellipse 44vw 40vw at 2% 69%,color-mix(in srgb,var(--of-glow-2,#8eb8b2) 15%,transparent),transparent 72%),repeating-linear-gradient(0deg,transparent 0 119px,#29474c09 120px 121px)!important}
body.xz-dark{background-color:#0c2028!important;background-image:radial-gradient(ellipse 58vw 46vw at 92% 8%,color-mix(in srgb,var(--of-glow,#83c3c3) 12%,transparent),transparent 70%),radial-gradient(ellipse 42vw 38vw at 3% 72%,color-mix(in srgb,var(--of-glow-2,#c8b99f) 8%,transparent),transparent 75%),repeating-linear-gradient(0deg,transparent 0 119px,#b8d9d20a 120px 121px)!important}
body:not(.ed-entry) main{position:relative}
body:not(.ed-entry) main:before{content:'';position:absolute;right:0;top:3%;width:min(26vw,360px);aspect-ratio:1;border:1px solid color-mix(in srgb,var(--of-glow,#83c3c3) 30%,transparent);border-radius:50%;box-shadow:0 0 0 34px color-mix(in srgb,var(--of-glow,#83c3c3) 5%,transparent),0 0 0 70px color-mix(in srgb,var(--of-glow,#83c3c3) 3%,transparent);pointer-events:none;z-index:0}
body :is(h1,h2,h3){text-wrap:balance}
body :is(p,.lead,.lede,.xz-lead){text-wrap:pretty}
body :is(button,a,select,input):focus-visible{outline:2px solid #d9b676!important;outline-offset:4px}
#xz-nav{height:72px!important;padding-inline:clamp(20px,4vw,76px)!important;background:#0d222aeF!important;box-shadow:0 12px 32px #06192026!important}
#xz-nav .xz-brand{letter-spacing:.025em!important;font-weight:650!important}
#xz-nav .xz-mark{border-radius:50%!important;background:#d8bd82!important;color:#132a30!important;box-shadow:0 0 0 1px #f5e4ba66,0 0 0 6px #ffffff0b!important}
#xz-nav .xz-links>a{font-size:12px!important;letter-spacing:.03em!important}
#xz-nav .xz-links>a[aria-current=page]{background:#ffffff17!important;box-shadow:inset 0 -2px 0 #d5b371!important}
body.ed-entry header.photo-editorial-hero,body.ed-entry header.hero{min-height:min(800px,calc(100svh - 72px))!important;padding-top:clamp(110px,15vh,180px)!important;padding-bottom:clamp(90px,12vh,140px)!important;background-position:center!important}
body.ed-entry header.photo-editorial-hero:before,body.ed-entry header.hero:before{height:2px!important;background:linear-gradient(90deg,#4d9bc0 0 20%,#e0b856 20% 40%,#f5f1e6 40% 60%,#66b392 60% 80%,#cc7078 80% 100%)!important}
body.ed-entry header.photo-editorial-hero h1,body.ed-entry header.hero h1{font-family:'Noto Serif SC','Songti SC',Georgia,serif!important;font-weight:650!important;letter-spacing:-.065em!important;line-height:1.12!important;max-width:850px!important;text-shadow:0 5px 30px #04141add!important}
body.ed-entry header.photo-editorial-hero :is(.xz-eyebrow,.eyebrow),body.ed-entry header.hero .eyebrow{font-size:12px!important;letter-spacing:.19em!important;color:#e8cd98!important}
body.ed-entry header.photo-editorial-hero :is(.xz-lead,.lead),body.ed-entry header.hero .hero-copy p{font-size:clamp(16px,1.35vw,20px)!important;line-height:1.72!important;max-width:640px!important;color:#f5f2e9!important;text-shadow:0 3px 17px #061719bb}
body.ed-entry .ed-chapter-rail{min-height:64px!important;background:#112931!important;border-bottom:1px solid #c5a97766!important}
body.ed-entry main{max-width:1480px;margin-inline:auto}
body.ed-entry main .xz-section{padding-block:clamp(90px,10vw,145px)!important}
body.ed-entry main .xz-section-top{display:grid;grid-template-columns:minmax(150px,240px) minmax(0,1fr);align-items:start;gap:clamp(20px,4vw,70px);margin-bottom:42px!important;border-top:1px solid var(--of-stroke)!important;padding-top:22px!important}
body.ed-entry main .xz-section-top>span{font-size:12px!important;font-weight:750!important;letter-spacing:.16em!important;color:#8b704b!important}
body.ed-entry main .xz-section-top h2{font-family:'Noto Serif SC','Songti SC',Georgia,serif!important;font-size:clamp(38px,4.7vw,70px)!important;line-height:1.13!important;margin:0!important;color:var(--of-type)!important}
body.ed-entry main .xz-path{gap:clamp(14px,1.5vw,26px)!important}
body.ed-entry:not(.ed-home) main .xz-path>a{min-height:285px!important;border-radius:13px!important;background:var(--of-panel)!important;border:1px solid var(--of-stroke)!important;box-shadow:0 20px 38px -32px #10293255!important;transition:transform .38s cubic-bezier(.2,.8,.2,1),box-shadow .38s,border-color .38s!important}
body.ed-entry:not(.ed-home) main .xz-path>a:hover{transform:translateY(-4px)!important;box-shadow:0 26px 42px -25px #1029325c!important;border-color:#8aaea6!important}
body.ed-entry:not(.ed-home) main .xz-path h3{font-family:'Noto Serif SC','Songti SC',Georgia,serif!important;font-size:clamp(26px,2.3vw,38px)!important;line-height:1.2!important}
body.ed-entry:not(.ed-home) main .xz-path p{font-size:14px!important;line-height:1.8!important;color:var(--of-secondary)!important}
body.xz-dark.ed-entry{background:#0c2028!important;color:#f0f3ec!important}
body.xz-dark.ed-entry main .xz-section-top h2{color:#f0f3ec!important}
body.xz-dark.ed-entry:not(.ed-home) main .xz-path>a{background:#17333b!important;color:#f0f3ec!important;border-color:#4f6b70!important}
body.xz-dark.ed-entry:not(.ed-home) main .xz-path p{color:#c3d7d0!important}
body.ed-home main .xz-path>a{border-radius:8px!important;box-shadow:0 25px 52px -35px #061c25aa!important;transition:transform .45s cubic-bezier(.2,.8,.2,1),box-shadow .45s!important}
body.ed-home main .xz-path>a:hover{transform:translateY(-5px)!important;box-shadow:0 33px 54px -28px #061c25bb!important}
body.ed-home main .xz-path>a h3{font-size:clamp(28px,2.5vw,43px)!important;line-height:1.13!important}
body.ed-home main .xz-path>a p{color:#f4f1e9!important}
body.ed-home main .xz-section:nth-of-type(2){background:radial-gradient(ellipse at 95% 7%,#d9e4d8aa,transparent 42%),linear-gradient(145deg,#e8ebe2,#eee9dc 70%);border:1px solid #d1d8cb;border-radius:18px;padding-inline:clamp(24px,4vw,65px)!important;margin-bottom:clamp(40px,6vw,90px);box-shadow:0 28px 62px -52px #102a3444}
body.ed-home main .xz-section:nth-of-type(2) .xz-section-top{border-color:#9db5ac!important}
body.xz-dark.ed-home main .xz-section:nth-of-type(2){background:radial-gradient(ellipse at 94% 8%,#36605e55,transparent 48%),linear-gradient(145deg,#18343c,#1c3238 70%);border-color:#49676a}
body.ed-home main .xz-note{background:linear-gradient(105deg,#102c35,#1c4248 72%,#214b50)!important;border-radius:18px!important;position:relative;overflow:hidden}
body.ed-home main .xz-note:after{content:'';position:absolute;width:min(36vw,440px);aspect-ratio:1;border:1px solid #d2b87988;border-radius:50%;right:-10%;top:-40%;box-shadow:0 0 0 45px #d2b87913,0 0 0 91px #d2b8790b;pointer-events:none}
body.ed-home main .xz-note>*{position:relative;z-index:1}
body.ed-home main .xz-note :is(h2,p,a,span){color:#f1f3e9!important}
body.hero-motion-portal main{background:radial-gradient(ellipse at 100% 5%,#bcc8bd6a,transparent 40%),radial-gradient(ellipse at 0 84%,#d4c6ad47,transparent 36%)}
body.xz-dark.hero-motion-portal main{background:radial-gradient(ellipse at 100% 5%,#42636b42,transparent 40%),radial-gradient(ellipse at 0 84%,#7d656230,transparent 36%)}
/* Three specific chapter moments break up long stretches of paper. */
body.ed-module-1.ed-entry main .xz-section:nth-of-type(2){position:relative;background:linear-gradient(120deg,#e3eeeb,#eff1e9 62%,#e7eee5);border:1px solid #bdd0ca;border-radius:16px;padding-inline:clamp(24px,4vw,64px)!important;overflow:hidden}
body.ed-module-1.ed-entry main .xz-section:nth-of-type(2):before{content:'';position:absolute;right:-8%;bottom:-42%;width:min(38vw,500px);aspect-ratio:1;border:1px solid #49859544;border-radius:50%;box-shadow:0 0 0 42px #49859511,0 0 0 89px #49859509;pointer-events:none}
body.ed-module-1.ed-entry main .xz-section:nth-of-type(2)>*{position:relative;z-index:1}
body.xz-dark.ed-module-1.ed-entry main .xz-section:nth-of-type(2){background:linear-gradient(120deg,#15333b,#1b3a40 70%);border-color:#547078}
body.ed-module-4.ed-entry main .xz-section:first-of-type{background:radial-gradient(ellipse at 95% 2%,#eec8a75c,transparent 46%),linear-gradient(145deg,#f2eee4,#f1e8dd);border-radius:18px;padding-inline:clamp(24px,4vw,64px)!important;margin-top:clamp(30px,4vw,58px);border:1px solid #d7cbbb}
body.xz-dark.ed-module-4.ed-entry main .xz-section:first-of-type{background:radial-gradient(ellipse at 95% 2%,#865f5266,transparent 45%),linear-gradient(145deg,#1b333b,#24343b);border-color:#725f5b}
body.ed-module-4.ed-entry main .xz-note{background-image:linear-gradient(90deg,#0b2932f5,#0c2932dd 60%,#0b293288),url('../任务三_专题深挖/媒体/la.jpg')!important;background-size:cover!important;background-position:center!important;border-radius:18px!important;min-height:320px;display:flex;flex-direction:column;justify-content:center}
body.ed-module-4.ed-entry main .xz-note :is(span,h2,p,a){color:#f4f2e8!important;position:relative;z-index:1}
body.ed-module-2:not(.ed-entry) main .t2-chart-panel{background:linear-gradient(160deg,#fbfaf5,#edf3ef 78%)!important;border:1px solid #c9d9d3!important;box-shadow:0 28px 48px -39px #0e424b77!important}
body.ed-module-2.xz-dark:not(.ed-entry) main .t2-chart-panel{background:linear-gradient(160deg,#16323a,#193a40 78%)!important;border-color:#496a70!important}
body.ed-module-3.story-experience .story-next:before{width:150px;background:linear-gradient(90deg,var(--story-accent) 0 50%,#d3b87e 50% 100%)}
/* Data work uses the same surfaces and type rhythm as the entry pages. */
body:not(.ed-entry) main :is(.card,.卡,.panel,.专题,.故事,.s1-case,.m-panel){border-radius:12px!important}
body:not(.ed-entry) main :is(h2,.section-head h2){letter-spacing:-.045em}
body:not(.ed-entry) main :is(select,input:not([type=range])){min-height:42px;border-radius:7px!important}
body:not(.ed-entry) main :is(button,.按钮){border-radius:7px!important;transition:transform .2s,background-color .2s,border-color .2s!important}
body:not(.ed-entry) main :is(button,.按钮):hover{transform:translateY(-2px)}
body:not(.ed-entry) main :is(button,.按钮):active{transform:translateY(0)}
body.xz-dark:not(.ed-entry) main :is(.card,.卡,.panel,.专题,.故事,.s1-case,.m-panel){border-color:var(--of-stroke)!important;color:var(--of-type)!important}
body.xz-dark:not(.ed-entry) main :is(h1,h2,h3,h4){color:#f1f5ed!important}
body.xz-dark:not(.ed-entry) main :is(.lead,.lede,.ip-context p,.section-head p,.t2-section-head p){color:#c8d9d3!important}
body.xz-dark:not(.ed-entry) main :is(.kicker,.eyebrow,.ip-eyebrow,.section-head small){color:#d9bd84!important}
/* The ten-story portal is a photographic index, not a dashboard grid. */
body.hero-motion-portal main{padding:clamp(84px,8vw,130px) clamp(22px,5.5vw,100px) 140px!important}
body.hero-motion-portal .section-head{grid-template-columns:minmax(0,1.2fr) minmax(300px,.8fr)!important;gap:clamp(35px,8vw,150px)!important;padding-bottom:32px!important}
body.hero-motion-portal .section-head small{font-size:12px!important;letter-spacing:.18em!important}
body.hero-motion-portal .section-head h2{font-family:'Noto Serif SC','Songti SC',Georgia,serif!important;font-size:clamp(42px,5.5vw,82px)!important;letter-spacing:-.06em!important;line-height:1.12!important}
body.hero-motion-portal .section-head p{font-size:16px!important;line-height:1.85!important;color:var(--of-secondary)!important}
body.hero-motion-portal .filters{gap:10px!important;padding-block:26px 38px!important}
body.hero-motion-portal .filters button{min-height:38px;padding:7px 17px!important;border-radius:6px!important;border:1px solid var(--of-stroke)!important;color:var(--of-type)!important;background:transparent!important}
body.hero-motion-portal .filters button.active,body.hero-motion-portal .filters button:hover{background:#17333b!important;color:#fff!important;border-color:#17333b!important}
body.xz-dark.hero-motion-portal .filters button.active,body.xz-dark.hero-motion-portal .filters button:hover{background:#77bbb4!important;color:#0d252b!important;border-color:#77bbb4!important}
body.hero-motion-portal .grid{gap:18px!important}
body.hero-motion-portal .story{border-radius:8px!important;min-height:clamp(420px,36vw,580px)!important;padding:clamp(24px,2.7vw,42px)!important;border:1px solid #ffffff44!important;box-shadow:0 16px 35px -30px #082127aa!important;transition:transform .45s cubic-bezier(.2,.8,.2,1),box-shadow .45s!important}
body.hero-motion-portal .story:hover{transform:translateY(-5px)!important;box-shadow:0 30px 45px -28px #082127bb!important}
body.hero-motion-portal .story-photo{opacity:.86!important;transition:transform .7s ease,filter .7s ease!important}
body.hero-motion-portal .story:hover .story-photo{transform:scale(1.035)!important;filter:saturate(1.08)!important}
body.hero-motion-portal .story:after{background:linear-gradient(180deg,#06171b8a 0%,#06171b0b 38%,#06171bf5 100%)!important}
body.hero-motion-portal .story-top{font-size:11px!important;letter-spacing:.12em!important;opacity:1!important;border-color:#fff9!important}
body.hero-motion-portal .story h3{font-family:'Noto Serif SC','Songti SC',Georgia,serif!important;font-size:clamp(30px,3.1vw,54px)!important;line-height:1.13!important;margin-bottom:12px!important}
body.hero-motion-portal .story p{font-size:14px!important;line-height:1.72!important;color:#f3f1e8!important}
body.hero-motion-portal .story .enter{font-size:12px!important;letter-spacing:.08em!important}
body.hero-motion-portal .story:nth-child(10){min-height:420px!important}
/* Story covers stay recognisable without overwhelming charts and prose. */
body.story-experience header[data-story-no]{border-top:2px solid var(--story-accent)!important}
body.story-experience .story-theme-icon{width:28px;height:28px;vertical-align:middle;margin-right:12px;filter:none}
body.story-experience .story-hero-rings{filter:drop-shadow(0 12px 16px #06192166)!important}
body.story-experience .story-guide{border-bottom:1px solid #738f9044!important}
body.story-experience .story-next{transition:background-color .3s!important}
body.story-experience .story-next:hover{background:#dceae4!important}
body.xz-dark.story-experience .story-next:hover{background:#173a42!important}
@media(max-width:800px){body.ed-entry main .xz-section-top{display:block}body.ed-entry main .xz-section-top h2{margin-top:14px!important}body.hero-motion-portal .section-head{grid-template-columns:1fr!important}body.hero-motion-portal .story,body.hero-motion-portal .story:nth-child(10){min-height:420px!important}}
@media(max-width:600px){#xz-nav{height:62px!important}body.ed-entry header.photo-editorial-hero,body.ed-entry header.hero{min-height:560px!important;padding:100px 22px 72px!important}body.ed-entry header.photo-editorial-hero h1,body.ed-entry header.hero h1{font-size:clamp(40px,10vw,64px)!important}body.ed-entry main .xz-section{padding-block:72px!important}body.hero-motion-portal main{padding:66px 18px 90px!important}body.hero-motion-portal .story{border-radius:5px!important}body.ed-entry header.photo-editorial-hero .ed-rings-scene,body.ed-entry header.hero .ed-rings-scene{top:24px!important;right:14px!important;bottom:auto!important;width:90px!important;opacity:.34!important;transform:none!important}body.story-experience header[data-story-no]>.story-hero-rings{top:22px!important;right:18px!important;bottom:auto!important;width:80px!important;height:60px!important;opacity:.48!important;transform:none!important}body.hero-motion-portal .filters{display:grid!important;grid-template-columns:repeat(2,minmax(0,1fr))!important;gap:9px!important}body.hero-motion-portal .filters button{width:100%!important;min-width:0!important;padding-inline:8px!important;white-space:normal!important}body.hero-motion-portal .filters button:last-child:nth-child(odd){grid-column:1/-1}}
@media(max-width:600px){body.story-experience:is(.story-02,.story-07) header[data-story-no]>.story-hero-rings{top:22px!important;right:18px!important;bottom:auto!important;width:80px!important;height:60px!important;opacity:.48!important;transform:none!important}}
@media(prefers-reduced-motion:reduce){body.ed-home main .xz-path>a,body.hero-motion-portal .story,body.hero-motion-portal .story-photo{transition:none!important}}
</style>'''

for path in sorted(DELIVERY.rglob('index.html')):
    html = path.read_text(encoding='utf-8')
    labels = {
        'DATA AUDIT / 01': '数据审计 / 01',
        'DATA ATLAS / 1896—2024': '百年图谱 / 1896—2024',
        'INTERACTIVE RANKING / 2024': '交互排名 / 2024',
        'SCENARIO STUDIO / LA 2028': '预测情景 / 洛杉矶 2028',
        '73 获奖行 原始代码 TPE · 1195 条参赛行': '中国台北：73 条获奖行、1195 条参赛行',
        '选取 HKG、TPE、SGP、FIJ、BER、JOR、KOS': '选取中国香港、中国台北、新加坡、斐济、百慕大、约旦和科索沃',
        '点击年份可同时查看参赛行与 NOC 数': '点击年份可同时查看参赛行与代表团数量',
        '12 个 NOC': '12 个代表团',
        '206 个 NOC': '206 个代表团',
        '唯一 NOC 数；展示完整时间序列': '唯一代表团数量；展示完整时间序列',
    }
    for before, after in labels.items():
        html = html.replace(before, after)
    if path.relative_to(DELIVERY).as_posix() == '任务四_开放创作/交互看板/index.html':
        noc_names = "const nocNames={USA:'美国',FRA:'法国',CHN:'中国',GBR:'英国',AUS:'澳大利亚',NED:'荷兰',GER:'德国',ESP:'西班牙',ITA:'意大利',JPN:'日本',KOR:'韩国',BRA:'巴西',CAN:'加拿大',NZL:'新西兰',UZB:'乌兹别克斯坦',HUN:'匈牙利',SUI:'瑞士',SWE:'瑞典',DEN:'丹麦',GRE:'希腊',AUT:'奥地利',ARG:'阿根廷',ROC:'俄罗斯奥委会',AIN:'个人中立运动员',EOR:'难民代表团'};const nocLabel=n=>nocNames[n]||n;"
        if 'const nocNames=' not in html:
            html = html.replace('function render(){', noc_names + 'function render(){', 1)
        html = html.replace('<strong>${n}</strong>', '<strong>${nocLabel(n)}</strong>')
        html = html.replace('<td>${r.NOC}</td>', '<td>${nocLabel(r.NOC)}</td>')
        html = html.replace(' · Public domain · ', ' · 公共领域 · ')
    if path.relative_to(DELIVERY).as_posix() == '任务三_专题深挖/统一中文入口/index.html':
        html = html.replace('TASK 03 / OLYMPIC DATA STORIES', '第三章 / 奥运数据故事')
    html = re.sub(r'<style id="olympic-premium-finish">.*?</style>', '', html, flags=re.S)
    html = html.replace('</head>', STYLE + '</head>', 1)
    path.write_text(html, encoding='utf-8')
    if SITE.exists():
        out = SITE / path.relative_to(DELIVERY)
        out.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, out)
print('Premium finish applied to', len(list(DELIVERY.rglob('index.html'))), 'pages')
