"""Give the ten Task 3 stories a shared editorial navigation and chapter identity."""
from pathlib import Path
import json
import posixpath
import re
import shutil
from task2_localization import NOC_ZH, SPORT_ZH

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件' / '任务三_专题深挖'
SITE = ROOT / '项目工作区' / 'sites' / 'la28-fullscore' / 'dist' / '任务三_专题深挖'
STORIES = [
    ('S1_东道主效应/index.html', '东道主效应', '#7ab7c3'),
    ('S2_口径的魔力/06_滚动叙事专题/index.html', '口径的魔力', '#dbb978'),
    ('S3_地缘政治的投影/index.html', '缺席的代表团', '#9ca9d0'),
    ('S4_小代表团的大突破/index.html', '小队伍的大突破', '#80c8a4'),
    ('S5_奖牌的通货膨胀/index.html', '奖牌变多了', '#df9c7b'),
    ('S6_王者与传奇/index.html', '名字背后的传奇', '#d9b58b'),
    ('S3_冠军的保质期/06_冠军王朝时间轴/index.html', '冠军的保质期', '#83bdc3'),
    ('S8_她们登上领奖台/index.html', '领奖台上的她们', '#d494b9'),
    ('S9_消失的赛场/index.html', '消失的赛场', '#b0be83'),
    ('S10_奖牌藏在哪些项目/index.html', '奖牌藏在哪些项目', '#8bc8d0'),
]
THEME_MARKS = [
    '<ellipse cx="24" cy="24" rx="19" ry="10"/><ellipse cx="24" cy="24" rx="13" ry="6"/><path d="M5 24h38M24 14v20"/>',
    '<circle cx="18" cy="23" r="12"/><circle cx="30" cy="23" r="12"/><path d="M24 8v30"/>',
    '<path d="M10 7h28v34H10zM16 15h16M16 22h13M16 29h16M16 35h9"/><path d="M30 7v10h8"/>',
    '<path d="M6 29c8-9 11-1 17-10s11-3 19-12M7 38c9-3 12-10 19-7s10-2 15-7"/><circle cx="14" cy="17" r="2"/><circle cx="35" cy="36" r="2"/>',
    '<path d="M7 38V28h7v10M18 38V23h7v15M29 38V15h7v23M7 41h35"/><path d="M7 19l10-5 8 2 13-9"/>',
    '<circle cx="24" cy="18" r="8"/><path d="M11 42c1-11 7-16 13-16s12 5 13 16M18 16h12M24 10v16"/>',
    '<path d="M6 34h36M8 27l9-7 8 5 13-15M17 20v14M25 25v9M38 10v24"/><circle cx="38" cy="10" r="2"/>',
    '<path d="M8 37h32M11 37V26h9v11M20 37V15h9v22M29 37V23h9v14"/><circle cx="24" cy="8" r="3"/>',
    '<path d="M9 12h30M9 24h20M9 36h10" stroke-dasharray="3 4"/><circle cx="34" cy="24" r="8"/><path d="M34 20v5l3 2"/>',
    '<circle cx="24" cy="24" r="17"/><path d="M24 7v34M7 24h34M12 12l24 24M36 12 12 36"/><circle cx="24" cy="24" r="4"/>',
]
HEADER_LABELS = [
    ('任务三 / 专题 S1', '主场观察'), ('数据故事 · 2024巴黎', '口径实验'),
    ('冷战档案 / S3', '历史档案'), ('海岛与新星 / S4', '群岛观察'),
    ('百年刻度 / S5', '年代刻度'), ('人物鉴证室 / S6', '人物鉴证'),
    ('任务三 · 创新专题', '优势寿命'), ('紫色档案 / S8', '她们的时间'),
    ('项目博物馆 / S9', '项目博物馆'), ('运动地图 / S10', '运动图谱'),
]
STYLE = '''<style id="story-experience-style">
body.story-experience{--story-ink:#eaf4ef;--story-accent:#85bac5}
body.story-experience header[data-story-no]{position:relative;isolation:isolate;overflow:hidden;border-top:4px solid var(--story-accent)!important}
body.story-experience:is(.story-03,.story-04,.story-05,.story-06,.story-08,.story-09,.story-10) header[data-story-no]:after{content:none!important;display:none!important}
body.story-experience .ed-rings-scene{display:none!important}
body.story-experience header[data-story-no]>*{position:relative;z-index:1}
.story-theme-icon{width:30px;height:30px;display:inline-block;vertical-align:middle;margin-right:10px;color:var(--story-accent);stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round;fill:none;filter:drop-shadow(0 3px 4px #081b2044)}
body.story-experience header[data-story-no]>.story-hero-rings{position:absolute!important;z-index:0!important;right:clamp(22px,5vw,90px)!important;top:48%!important;width:clamp(170px,22vw,280px)!important;height:clamp(120px,16vw,205px)!important;margin:0!important;padding:0!important;pointer-events:none;perspective:900px;transform:translateY(-50%);opacity:.82;filter:drop-shadow(0 18px 18px #06192155)}
.story-hero-rings .story-rings-plate{position:absolute;inset:0;transform-style:preserve-3d;animation:story-rings-drift 8s ease-in-out infinite;will-change:transform}
.story-hero-rings i{position:absolute;display:block;width:34%;aspect-ratio:1;border:clamp(5px,.65vw,9px) solid var(--ring);border-radius:50%;box-shadow:inset 2px 2px 3px #fff9,inset -3px -3px 4px #05182055,3px 6px 0 color-mix(in srgb,var(--ring) 50%,#10252c),6px 12px 18px #05192055;transform:translateZ(var(--depth))}
.story-hero-rings i:nth-child(1){left:1%;top:3%;--ring:#2587b8;--depth:12px}.story-hero-rings i:nth-child(2){left:33%;top:3%;--ring:#273c45;--depth:6px}.story-hero-rings i:nth-child(3){left:65%;top:3%;--ring:#ca6570;--depth:12px}.story-hero-rings i:nth-child(4){left:17%;top:35%;--ring:#d5ac45;--depth:18px}.story-hero-rings i:nth-child(5){left:49%;top:35%;--ring:#4ca379;--depth:18px}
@keyframes story-rings-drift{0%,100%{transform:rotateX(-10deg) rotateY(-15deg) translateY(0)}50%{transform:rotateX(-5deg) rotateY(-5deg) translateY(-10px)}}
body.story-experience:is(.story-02,.story-07) header[data-story-no]>.story-hero-rings{width:150px!important;height:110px!important;right:2vw!important;top:20%!important;opacity:.5}
body.story-experience.xz-dark header[data-story-no]>.story-hero-rings{opacity:.92;filter:drop-shadow(0 20px 20px #010a0ca8)}
body.story-experience .photo-stage{overflow:hidden;position:relative;border-radius:3px;box-shadow:0 25px 70px -44px #071c2688}
body.story-experience .photo-stage img{transition:transform 1.15s cubic-bezier(.2,1,.2,1),filter 1.15s;will-change:transform}
body.story-experience .photo-stage:hover img{transform:scale(1.035);filter:saturate(1.06)}
body.story-experience .photo-stage:is(.portrait,.women,.museum) img{object-fit:contain!important;object-position:center center!important;transform:none!important;filter:none!important;background:#233139}
body.story-experience .photo-stage:is(.portrait,.women,.museum){background:#233139}
body.story-experience .photo-stage:is(.portrait,.women,.museum):hover img{transform:none!important;filter:none!important}
body.story-experience .photo-stage:is(.host,.islands,.archive,.growth,.dynasty,.lens,.sports) img{object-position:center 25%!important}
body.story-experience .photo-stage:is(.host,.islands,.archive,.growth,.dynasty,.lens,.sports):hover img{transform:scale(1.025)!important}
.story-guide{position:relative!important;inset:auto!important;z-index:5!important;width:100%!important;min-height:116px!important;background:#142d34!important;color:#f2f4ed!important;border:0!important;border-top:3px solid transparent!important;border-image:linear-gradient(90deg,#2587b8 0 20%,#d5ac45 20% 40%,#eef2ee 40% 60%,#4ca379 60% 80%,#ca6570 80% 100%) 1!important;padding:16px clamp(18px,4vw,72px) 17px!important;display:grid!important;grid-template-columns:auto minmax(0,1fr) auto!important;gap:12px 24px!important;align-items:center!important;box-sizing:border-box!important;font:700 12px/1.5 'Microsoft YaHei',system-ui,sans-serif!important;letter-spacing:.04em!important;opacity:1!important;visibility:visible!important;transform:none!important}
.story-guide-label{white-space:nowrap;color:var(--story-accent)!important}.story-guide-link{color:#e8eee8!important;text-decoration:none!important;white-space:nowrap}.story-guide-link:hover{text-decoration:underline!important;text-decoration-color:var(--story-accent)!important;text-underline-offset:5px}
body.unified-topbar-added.story-experience>nav.story-guide:not(#xz-nav){display:grid!important;position:relative!important;visibility:visible!important;opacity:1!important}
.story-guide-track{grid-column:1/-1;display:grid!important;grid-template-columns:repeat(10,minmax(0,1fr));gap:0;position:relative;min-width:0;padding-top:9px}.story-guide-track:before{content:'';position:absolute;left:4%;right:4%;top:27px;height:1px;background:#709097;opacity:.65;pointer-events:none}.story-guide-track a{position:relative;z-index:1;display:grid!important;place-items:center;width:36px;height:36px;margin:auto;border:1px solid #76949b;border-radius:50%;background:#17353d!important;color:#c9d9d4!important;text-decoration:none!important;font:700 11px Georgia,serif;opacity:1!important;transition:transform .25s,background .25s,color .25s,border-color .25s}.story-guide-track a[aria-current="page"]{background:var(--story-accent)!important;color:#102a32!important;border-color:var(--story-accent)!important;transform:scale(1.14)}.story-guide-track a:hover,.story-guide-track a:focus-visible{background:#315b63!important;color:#fff!important;transform:translateY(-3px)}.story-guide-track a:focus-visible{outline:2px solid #fff;outline-offset:4px}.story-guide-track a:after{content:attr(aria-label);position:absolute;left:50%;bottom:43px;transform:translateX(-50%);width:max-content;max-width:190px;padding:6px 10px;border-radius:5px;background:#10252c;color:#fff;opacity:0;pointer-events:none;transition:opacity .2s}.story-guide-track a:hover:after,.story-guide-track a:focus-visible:after{opacity:1}
.story-next{box-sizing:border-box!important;display:block!important;position:relative!important;max-width:none!important;width:100%!important;margin:0!important;padding:clamp(54px,7vw,100px) clamp(22px,7vw,110px)!important;background:#e7eee9!important;color:#18343a!important;border:0!important;border-top:1px solid #a8bfba!important;border-radius:0!important;box-shadow:none!important;font-family:'Microsoft YaHei',system-ui,sans-serif}.story-next:before{content:'';position:absolute;top:0;left:7vw;width:110px;height:3px;background:var(--story-accent)}.story-next small{display:block;color:#60777b;font-weight:800;letter-spacing:.15em;margin-bottom:14px}.story-next a{display:flex;align-items:end;justify-content:space-between;gap:20px;color:inherit;text-decoration:none;font:600 clamp(32px,5vw,72px)/1.12 Georgia,'Songti SC',serif;letter-spacing:-.05em}.story-next a span:last-child{color:#8a6d48;transition:transform .3s}.story-next a:hover span:last-child{transform:translate(6px,-6px)}
body.xz-dark .story-guide{background:#0e252c;color:#f2f6ef}.story-experience.xz-dark .story-next small{color:#a9c7c5}
body.story-experience.xz-dark header[data-story-no]{background:#102c34!important;color:#f2f6ef!important}
body.story-experience.xz-dark header[data-story-no] :is(h1,p,.lead,.导语){color:#f2f6ef!important}
body.story-experience.xz-dark main :is(h1,h2,h3,h4,p,.lead,.note,.说明){color:#edf5ef!important}
body.story-experience.xz-dark main :is(.card,.panel,.卡,.专题,.故事){background:#17343c!important;color:#edf5ef!important;border-color:#4b6b70!important}
body.story-experience.xz-dark main :is(.card,.panel,.卡,.专题,.故事) :is(small,span,label){color:#d4e3dd!important}
body.story-experience.xz-dark main :is(select,input,textarea){background:#102b33!important;color:#f1f7f0!important;border-color:#64878a!important}
body.story-experience.xz-dark main :is(table,tbody tr){color:#eef5ef!important}
body.story-experience.xz-dark main :is(th,td){color:#eef5ef!important;border-color:#49676d!important}
body.story-experience.xz-dark .story-next{background:#102b33!important;color:#eef5ef!important;border:0!important;border-top:1px solid #496b70!important;border-radius:0!important;box-shadow:none!important}
body.story-experience.xz-dark .story-next a{color:#eef5ef!important}
/* Legacy story modules used opaque paper panels; dark mode must change both sides. */
body.story-experience.xz-dark :is(aside:not(#xz-menu):not(.story-next),.evidence article,.s1-facts article,.s1-case,.s1-note,.s1-details article,.lens,.viz,.year,.内容,.控制){background:#18353d!important;color:#edf5ef!important;border-color:#54747a!important;box-shadow:0 15px 38px #051a2244!important}
body.story-experience.xz-dark :is(aside:not(#xz-menu):not(.story-next),.evidence article,.s1-facts article,.s1-case,.s1-note,.s1-details article,.lens,.viz,.year,.内容,.控制) :is(h2,h3,h4,p,small,span,strong,label){color:#e8f2ed!important}
body.story-experience.xz-dark :is(.bar,.islands .bar,.museum .bar){background:#20414a!important;color:#ecf4ee!important;border-color:#57777b!important}
body.story-experience.xz-dark .bar:hover,body.story-experience.xz-dark .bar:focus-visible{background:#31545b!important;color:#fff!important}
body.story-experience.xz-dark :is(.s1-picker button,.s1-links a){background:#20444b!important;color:#eef6ef!important;border-color:#648589!important}
body.story-experience.xz-dark :is(.s1-picker button:hover,.s1-links a:hover){background:#315a60!important;color:#fff!important}
body.story-experience.xz-dark .xz-segment button.active{background:#315a60!important;color:#fff!important}
body.story-experience.xz-dark nav:not(#xz-nav):not(.story-guide){background:#142f37!important;color:#edf5ef!important;border-color:#4f7075!important}
body.story-experience.xz-dark nav:not(#xz-nav):not(.story-guide) a{color:#edf5ef!important}
body.story-experience.xz-dark footer{background:#102a32!important;color:#edf5ef!important;border-color:#45636a!important}
body.story-experience.xz-dark footer :is(h1,h2,h3,p,small,span,a){color:#edf5ef!important}
@media(max-width:700px){.story-guide{min-height:122px!important;grid-template-columns:1fr auto!important;gap:8px!important;padding:12px 18px 16px!important}.story-guide-track{grid-column:1/-1;grid-row:2;overflow-x:auto;grid-template-columns:repeat(10,36px);justify-content:space-between;padding-bottom:4px}.story-guide-track:before{left:18px;right:18px}.story-guide-track a{width:30px;height:30px}.story-next{padding:58px 22px!important}body.story-experience header[data-story-no]>.story-hero-rings{width:120px!important;height:90px!important;right:8px!important;top:15%!important;opacity:.38!important}}
@media(prefers-reduced-motion:reduce){body.story-experience .photo-stage img,.story-guide-track a,.story-next a span:last-child{transition:none!important}.story-hero-rings .story-rings-plate{animation:none!important;will-change:auto}}
</style>'''
SCRIPT = '''<script id="story-experience-script">(()=>{const g=document.querySelector('.story-guide');if(!g)return;const bars=[...g.querySelectorAll('.story-guide-track a')];bars.forEach((a,i)=>{a.addEventListener('pointerenter',()=>g.style.setProperty('--story-hover',i));a.addEventListener('pointerleave',()=>g.style.removeProperty('--story-hover'))});})();</script>'''
UI_ZH = {'Gold':'金牌','Silver':'银牌','Bronze':'铜牌','Medals':'奖牌','Medal':'奖牌','Athletes':'运动员','Events':'小项','Sport':'运动','Sports':'运动','Countries':'代表团','Country':'代表团','Ranking':'排名','Results':'结果','Year':'年份','Men':'男子','Women':'女子','All':'全部','No data':'暂无数据','Public domain':'公有领域'}
LABELS = {**SPORT_ZH, **NOC_ZH, **UI_ZH}
LABEL_SCRIPT = '''(()=>{const labels=__LABELS__;const blocked=new Set(['SCRIPT','STYLE','TEXTAREA','CODE','PRE']);function visit(root){if(!root||blocked.has(root.nodeName))return;const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);let node;while(node=walker.nextNode()){const parent=node.parentElement;if(!parent||blocked.has(parent.tagName))continue;const raw=node.nodeValue.trim(),translated=labels[raw];if(translated&&translated!==raw)node.nodeValue=node.nodeValue.replace(raw,translated)}}visit(document.body);let pending=false;const observer=new MutationObserver(()=>{if(pending)return;pending=true;requestAnimationFrame(()=>{pending=false;visit(document.body)})});observer.observe(document.body,{subtree:true,childList:true,characterData:true})})();'''

def link(from_rel: str, to_rel: str) -> str:
    return posixpath.relpath(to_rel, posixpath.dirname(from_rel))

for index, (rel, title, accent) in enumerate(STORIES):
    path = BASE / rel
    source = path.read_text(encoding='utf-8')
    source = re.sub(r'<style id="story-experience-style">.*?</style>', '', source, flags=re.S)
    source = re.sub(r'<script id="story-experience-script">.*?</script>', '', source, flags=re.S)
    source = re.sub(r'<!-- STORY_GUIDE_START -->.*?<!-- STORY_GUIDE_END -->', '', source, flags=re.S)
    source = re.sub(r'<!-- STORY_NEXT_START -->.*?<!-- STORY_NEXT_END -->', '', source, flags=re.S)
    source = re.sub(r'<div class="story-hero-number"[^>]*>.*?</div>', '', source, flags=re.S)
    source = re.sub(r'<div class="story-hero-rings"[^>]*>.*?</div></div>', '', source, flags=re.S)
    source = re.sub(r'<svg class="story-theme-icon".*?</svg>', '', source, flags=re.S)
    source = re.sub(r'\bstory-experience\b\s*', '', source)
    source = re.sub(r'\bstory-\d{2}\b\s*', '', source)
    source = re.sub(r' style="--story-accent:[^"]*"', '', source, count=1)
    source = re.sub(r' data-story-no="\d{2}"', '', source, count=1)
    source = re.sub(r'header:after\{content:"S(?:[1-9]|10)";[^}]*\}', '', source)
    source = re.sub(r'<body([^>]*)>', lambda m: '<body' + (m.group(1).replace('class="', f'class="story-experience story-{index+1:02d} ', 1) if 'class="' in m.group(1) else m.group(1) + f' class="story-experience story-{index+1:02d}"') + f' style="--story-accent:{accent}">', source, count=1)
    source = re.sub(r'<header([^>]*)>', lambda m: '<header' + m.group(1) + f' data-story-no="{index+1:02d}">', source, count=1)
    hero_rings = '<div class="story-hero-rings" aria-hidden="true"><div class="story-rings-plate">' + '<i></i>' * 5 + '</div></div>'
    source = source.replace(f'data-story-no="{index+1:02d}">', f'data-story-no="{index+1:02d}">' + hero_rings, 1)
    hstart = source.index('<header')
    hend = source.index('</header>', hstart) + len('</header>')
    header = source[hstart:hend]
    old_label, new_label = HEADER_LABELS[index]
    header = header.replace(old_label, new_label, 1)
    icon = '<svg class="story-theme-icon" viewBox="0 0 48 48" aria-hidden="true">' + THEME_MARKS[index] + '</svg>'
    header, inserted = re.subn(r'(<(?:div|span)[^>]*class="[^"]*(?:s1-kicker|tag|eyebrow|眉题)[^"]*"[^>]*>)', lambda m: m.group(1) + icon, header, count=1)
    if inserted != 1:
        raise ValueError(f'No header theme label: {rel}')
    source = source[:hstart] + header + source[hend:]
    source = re.sub(r'(<title>[^<]*)\bS(?:1|2|3|4|5|6|8|9|10)\s*', r'\1', source, count=1)
    source = re.sub(r'>百年圣火 · S(?:1|2|3|4|5|6|8|9|10)<', f'>百年圣火 · {new_label}<', source)
    source = source.replace('>S2 · 口径的魔力<', '>口径的魔力<')
    track = ''.join(f'<a href="{link(rel, target)}" aria-label="{n+1:02d} {name}"' + (' aria-current="page"' if n == index else '') + f'>{n+1:02d}</a>' for n, (target, name, _) in enumerate(STORIES))
    guide = f'<!-- STORY_GUIDE_START --><nav class="story-guide" aria-label="十个专题导航"><span class="story-guide-label">专题 {index+1:02d} / 10 · {title}</span><span></span><a class="story-guide-link" href="{link(rel,"统一中文入口/index.html")}">十题总览 ↗</a><div class="story-guide-track">{track}</div></nav><!-- STORY_GUIDE_END -->'
    source = source.replace('<header', guide + '<header', 1)
    next_rel, next_title, _ = STORIES[(index + 1) % len(STORIES)]
    next_block = f'<!-- STORY_NEXT_START --><aside class="story-next"><small>继续阅读 / {((index + 1) % 10) + 1:02d}</small><a href="{link(rel,next_rel)}"><span>{next_title}</span><span>↗</span></a></aside><!-- STORY_NEXT_END -->'
    label_src = posixpath.relpath('媒体/story-labels.js', posixpath.dirname(rel))
    source = re.sub(r'<script id="story-labels-loader"[^>]*></script>', '', source)
    footer_pos = source.rfind('<footer')
    if footer_pos >= 0:
        source = source[:footer_pos] + next_block + source[footer_pos:]
    else:
        source = source.replace('</body>', next_block + '</body>', 1)
    source = source.replace('</body>', SCRIPT + f'<script id="story-labels-loader" src="{label_src}"></script></body>', 1)
    source = source.replace('</head>', STYLE + '</head>', 1)
    path.write_text(source, encoding='utf-8')
    target = SITE / rel
    if SITE.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
print('Updated 10 story interfaces.')
label_path = BASE / '媒体' / 'story-labels.js'
label_path.write_text(LABEL_SCRIPT.replace('__LABELS__', json.dumps(LABELS, ensure_ascii=False, separators=(',', ':'))), encoding='utf-8')
if SITE.exists():
    shutil.copy2(label_path, SITE / '媒体' / 'story-labels.js')
