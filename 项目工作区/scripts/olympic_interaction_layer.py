"""Add a compact Olympic progress and task navigator to delivered HTML pages.

The layer is self-contained, works from file://, and never changes chart data.
"""
from pathlib import Path
from html import escape
import os
import re

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / '交付文件'
PAGES = sorted(path for path in BASE.rglob('*.html') if not path.name.endswith('.template.html') and '原始页面' not in path.parts) + ([ROOT/'index.html'] if (ROOT/'index.html').exists() else [])
DESTINATIONS = [
    ('数据体检', BASE/'任务一_数据体检/index.html'),
    ('百年全景', BASE/'任务二_百年全景/05_交互总览/index.html'),
    ('专题深挖', BASE/'任务三_专题深挖/统一中文入口/index.html'),
    ('开放创作', BASE/'任务四_开放创作/index.html'),
]
DESCRIPTIONS = ('定义可信的统计口径', '看清百年赛场的变化', '追问十个数据结论', '走向洛杉矶 2028')
START = '<!-- OLYMPIC_INTERACTION_START -->'
END = '<!-- OLYMPIC_INTERACTION_END -->'

CSS = '''<style id="ox-interaction-style">
.ox-control{--ox-surface:#112d36;--ox-surface-raised:#20424a;--ox-text:#f2f4ee;--ox-muted:#bfd2d1;--ox-motion:cubic-bezier(.22,1,.36,1);position:fixed;left:clamp(12px,2vw,28px);bottom:clamp(14px,2vw,28px);z-index:2147483000;font-family:"Microsoft YaHei",system-ui,sans-serif;isolation:isolate}
.ox-trigger{position:relative;display:grid;place-items:center;width:60px;height:60px;padding:3px;border:0;border-radius:50%;cursor:pointer;background:conic-gradient(#e3b86c var(--ox-progress,0%),#31535a 0);box-shadow:0 12px 32px #051b2370;transition:transform .5s var(--ox-motion),box-shadow .3s var(--ox-motion)}
.ox-trigger:hover,.ox-trigger:focus-visible{transform:translateY(-5px) scale(1.04);box-shadow:0 19px 40px #051b2399}.ox-trigger:hover .ox-rings,.ox-trigger[aria-expanded="true"] .ox-rings{transform:rotate(-9deg) scale(1.1)}.ox-trigger:focus-visible,.ox-panel a:focus-visible,.ox-close:focus-visible{outline:3px solid #ffd177;outline-offset:3px}
.ox-face{display:grid;place-items:center;width:100%;height:100%;border-radius:50%;background:var(--ox-surface)}.ox-rings{position:relative;display:block;width:33px;height:23px;transition:transform .5s var(--ox-motion)}.ox-rings i{position:absolute;width:12px;height:12px;border:2.5px solid var(--c);border-radius:50%;box-sizing:border-box;left:var(--x);top:var(--y);animation:ox-ring-enter .7s var(--ox-motion) both;animation-delay:calc(var(--ox-i)*70ms)}
.ox-rings i:nth-child(1){--c:#51a9d6;--x:0px;--y:0px}.ox-rings i:nth-child(2){--c:#f1f2ed;--x:10px;--y:0px}.ox-rings i:nth-child(3){--c:#ee7272;--x:20px;--y:0px}.ox-rings i:nth-child(4){--c:#eac364;--x:5px;--y:9px}.ox-rings i:nth-child(5){--c:#7cc393;--x:15px;--y:9px}
.ox-control.ox-pulse .ox-trigger{animation:ox-pulse .55s var(--ox-motion)}.ox-control.ox-pulse .ox-rings{transform:rotate(10deg) scale(1.1)}.ox-panel{position:absolute;left:0;bottom:calc(100% + 16px);width:min(356px,calc(100vw - 28px));padding:24px;background:#112d36ed;color:var(--ox-text);backdrop-filter:blur(22px);border:1px solid #54727a;border-radius:24px;box-shadow:0 24px 65px #051b23a8;transform-origin:bottom left;animation:ox-appear .5s var(--ox-motion) both}.ox-panel[hidden]{display:none!important}.ox-panel:before{content:"";position:absolute;top:0;left:24px;right:24px;height:3px;border-radius:0 0 4px 4px;background:linear-gradient(90deg,#51a9d6 0 20%,#d9ddda 20% 40%,#ee7272 40% 60%,#eac364 60% 80%,#7cc393 80%)}
.ox-control .ox-panel{display:block!important;height:auto!important;min-height:0!important;max-height:min(540px,calc(100dvh - 95px));overflow-y:auto}.ox-control .ox-panel[hidden]{display:none!important}
.ox-panel-head{display:flex;align-items:start;justify-content:space-between;gap:12px}.ox-panel strong{font-size:20px;line-height:28px;letter-spacing:.02em;font-weight:600}.ox-panel p{font-size:14px;line-height:20px;color:var(--ox-muted);margin:8px 0 20px}.ox-close{display:grid;place-items:center;width:44px;height:44px;margin:-8px -8px 0 0;background:transparent;border:0;border-radius:50%;color:#d9ebe7;font-size:24px;cursor:pointer;transition:transform .5s var(--ox-motion),background .3s}.ox-close:hover{transform:rotate(90deg);background:#ffffff18}.ox-links{display:grid;gap:8px}.ox-panel a{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:54px;padding:12px 16px;border-radius:16px;color:#f4f7f2;text-decoration:none;font-size:14px;font-weight:600;background:var(--ox-surface-raised);transition:background .3s,transform .5s var(--ox-motion),box-shadow .3s;animation:ox-link-enter .55s var(--ox-motion) both;animation-delay:calc(var(--ox-i)*60ms)}.ox-panel a:hover{background:#315b61;transform:translateX(6px);box-shadow:0 8px 22px #0003}.ox-panel a:active{transform:scale(.98)}.ox-panel a[aria-current="page"]{background:#665136;color:#fff3d7}.ox-links small{color:#a9c5c2;font-size:12px}.ox-foot{display:flex;justify-content:space-between;border-top:1px solid #44616a;margin-top:20px;padding-top:16px;color:#b9cfce;font-size:12px}
@keyframes ox-appear{from{opacity:0;transform:translateY(24px) scale(.96)}to{opacity:1;transform:translateY(0) scale(1)}}@keyframes ox-link-enter{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}@keyframes ox-ring-enter{from{opacity:0;transform:translateY(8px) scale(.5)}to{opacity:1;transform:translateY(0) scale(1)}}@keyframes ox-pulse{50%{transform:scale(1.11)}}
@media(max-width:640px){.ox-control{left:12px;bottom:12px}.ox-trigger{width:52px;height:52px}.ox-control .ox-panel{position:fixed;left:12px;right:12px;top:12px;bottom:76px;width:auto;height:auto!important;max-height:none;padding:24px;display:flex!important;flex-direction:column;overflow-y:auto}.ox-control .ox-panel[hidden]{display:none!important}.ox-panel p{max-width:27ch}.ox-links{flex:1;align-content:center;gap:12px}.ox-panel a{min-height:72px;padding:16px;font-size:16px}.ox-foot{margin-top:auto}}
@media(prefers-reduced-motion:reduce){.ox-trigger,.ox-panel,.ox-panel a,.ox-rings,.ox-rings i{animation:none!important;transition:none!important;transform:none!important}}
.ox-link-copy{display:grid;gap:3px}.ox-link-copy b{font-size:14px;font-weight:600}.ox-link-copy small{font-size:12px;font-weight:400;color:#a9c5c2}.ox-arrow{font-size:18px;color:#e6c18b;transition:transform .5s var(--ox-motion)}.ox-panel a:hover .ox-arrow{transform:translate(3px,-3px)}
.ox-zoomable{cursor:zoom-in}.ox-viewer{position:fixed;inset:0;z-index:2147483001;display:grid;place-items:center;padding:64px 32px 32px;background:#071b21e8;backdrop-filter:blur(18px);color:#f4f7f2;animation:ox-viewer-in .5s cubic-bezier(.22,1,.36,1) both}.ox-viewer[hidden]{display:none!important}.ox-viewer img{display:block;max-width:min(100%,1400px);max-height:calc(100dvh - 150px);width:auto;height:auto;object-fit:contain;border-radius:8px;box-shadow:0 24px 80px #0009;animation:ox-viewer-image .55s cubic-bezier(.22,1,.36,1) both}.ox-viewer figcaption{max-width:70ch;text-align:center;margin-top:16px;font:400 14px/20px "Microsoft YaHei",system-ui,sans-serif;color:#d7e4e1}.ox-viewer figure{margin:0;display:grid;justify-items:center}.ox-viewer-close{position:absolute;right:24px;top:24px;display:grid;place-items:center;width:44px;height:44px;border:1px solid #b9d1cf;border-radius:50%;background:#14343a;color:#fff;font:400 28px/1 system-ui;cursor:pointer;transition:transform .5s cubic-bezier(.22,1,.36,1),background .3s}.ox-viewer-close:hover{transform:rotate(90deg);background:#315b61}.ox-viewer-close:focus-visible{outline:3px solid #ffd177;outline-offset:3px}@keyframes ox-viewer-in{from{opacity:0}to{opacity:1}}@keyframes ox-viewer-image{from{opacity:0;transform:translateY(24px) scale(.96)}to{opacity:1;transform:translateY(0) scale(1)}}
@media(max-width:640px){.ox-viewer{padding:64px 16px 24px}.ox-viewer img{max-height:calc(100dvh - 130px)}.ox-viewer-close{right:16px;top:16px}}
@media(prefers-reduced-motion:reduce){.ox-viewer,.ox-viewer img,.ox-viewer-close{animation:none!important;transition:none!important}}
@media(max-width:640px){.ox-panel a{min-height:84px}.ox-link-copy b{font-size:16px}}
</style>'''

JS = '''<script id="ox-interaction-script">(()=>{
const root=document.querySelector('.ox-control');if(!root)return;
// Some delivered pages animate the body with transform; a fixed child would
// then be anchored to that transformed body instead of the viewport.
document.documentElement.appendChild(root);
const trigger=root.querySelector('.ox-trigger'),panel=root.querySelector('.ox-panel'),close=root.querySelector('.ox-close'),progress=root.querySelector('.ox-progress-text');
const reduce=matchMedia('(prefers-reduced-motion: reduce)');
function setOpen(open){panel.hidden=!open;trigger.setAttribute('aria-expanded',String(open));if(open)close.focus();else trigger.focus()}
trigger.addEventListener('click',()=>setOpen(panel.hidden));close.addEventListener('click',()=>setOpen(false));
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!panel.hidden)setOpen(false)});
document.addEventListener('pointerdown',e=>{if(!panel.hidden&&!root.contains(e.target)){panel.hidden=true;trigger.setAttribute('aria-expanded','false')}});
let ticking=false;function update(){const max=Math.max(1,document.documentElement.scrollHeight-innerHeight),p=Math.max(0,Math.min(100,Math.round(scrollY/max*100)));trigger.style.setProperty('--ox-progress',p+'%');progress.textContent='阅读进度 '+p+'%';ticking=false}
addEventListener('scroll',()=>{if(!ticking){ticking=true;requestAnimationFrame(update)}},{passive:true});addEventListener('resize',update);update();
function pulse(){if(reduce.matches)return;root.classList.remove('ox-pulse');void root.offsetWidth;root.classList.add('ox-pulse')}
document.addEventListener('change',e=>{if(e.target.matches('select,input[type=range],input[type=checkbox],input[type=radio]'))pulse()});
document.addEventListener('click',e=>{if(e.target.closest('[data-btn],[data-lens],[role="tab"],.tabs button,.controls button,.筛选 button'))pulse()});
const images=[...document.querySelectorAll('figure img,.chart img,.viz img')].filter(img=>!img.closest('a,button,.ox-control')&&img.getAttribute('src'));
if(images.length){
 const viewer=document.createElement('div');viewer.className='ox-viewer';viewer.hidden=true;viewer.setAttribute('role','dialog');viewer.setAttribute('aria-modal','true');viewer.setAttribute('aria-label','查看图表大图');viewer.innerHTML='<button class="ox-viewer-close" type="button" aria-label="关闭大图">×</button><figure><img alt=""><figcaption></figcaption></figure>';
 document.documentElement.appendChild(viewer);const full=viewer.querySelector('img'),caption=viewer.querySelector('figcaption'),vclose=viewer.querySelector('button');let opener=null;
 function hideViewer(){viewer.hidden=true;full.removeAttribute('src');opener?.focus();opener=null}
 for(const img of images){img.classList.add('ox-zoomable');img.tabIndex=0;img.setAttribute('role','button');img.setAttribute('aria-label','放大查看：'+(img.alt||'图表'));const show=()=>{opener=img;full.src=img.currentSrc||img.src;full.alt=img.alt||'图表大图';caption.textContent=img.closest('figure')?.querySelector('figcaption')?.textContent?.trim()||img.alt||'图表详情';viewer.hidden=false;vclose.focus()};img.addEventListener('click',show);img.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();show()}})}
 vclose.addEventListener('click',hideViewer);viewer.addEventListener('click',e=>{if(e.target===viewer)hideViewer()});document.addEventListener('keydown',e=>{if(e.key==='Escape'&&!viewer.hidden)hideViewer()});
}
})();</script>'''


def enhance(path: Path) -> bool:
    html = path.read_bytes().decode('utf-8')
    if re.search(r'''<div\b[^>]*class=["'][^"']*\box-control\b''', html):
        return False
    if re.search(r'''<meta\b[^>]*http-equiv=["']?refresh''', html, re.I):
        return False
    html = re.sub(r'<style id="ox-interaction-style">.*?</style>', '', html, flags=re.S)
    html = re.sub(r'<style id="ox-news-table-fix">.*?</style>', '', html, flags=re.S)
    if START in html:
        html = re.sub(re.escape(START)+r'.*?'+re.escape(END), '', html, flags=re.S)
    links = []
    for i, (label, target) in enumerate(DESTINATIONS, 1):
        href = Path(os.path.relpath(target, path.parent)).as_posix()
        current = ' aria-current="page"' if path == target else ''
        links.append(f'<a href="{escape(href,quote=True)}"{current} style="--ox-i:{i}"><span class="ox-link-copy"><b>{i:02d} · {label}</b><small>{DESCRIPTIONS[i-1]}</small></span><span class="ox-arrow" aria-hidden="true">↗</span></a>')
    widget = '''<div class="ox-control" aria-label="奥运作品导览"><button class="ox-trigger" type="button" aria-label="打开奥运作品导览" aria-haspopup="true" aria-expanded="false" aria-controls="ox-panel"><span class="ox-face"><span class="ox-rings" aria-hidden="true"><i style="--ox-i:1"></i><i style="--ox-i:2"></i><i style="--ox-i:3"></i><i style="--ox-i:4"></i><i style="--ox-i:5"></i></span></span></button><div class="ox-panel" id="ox-panel" role="navigation" aria-label="四项任务" hidden><div class="ox-panel-head"><strong>沿赛道探索作品</strong><button class="ox-close" type="button" aria-label="关闭导览">×</button></div><p>四个任务，一条从数据口径到未来预测的阅读路线。</p><div class="ox-links">'''+''.join(links)+'''</div><div class="ox-foot"><span>奥运数据观察</span><span class="ox-progress-text">阅读进度 0%</span></div></div></div>'''
    shared = Path(os.path.relpath(BASE / '共享组件', path.parent)).as_posix()
    assets = (f'<link rel="stylesheet" href="{shared}/olympic-widget.css">'
              f'<link rel="stylesheet" href="{shared}/olympic-guide.css">')
    scripts = (f'<script defer src="{shared}/olympic-widget.js"></script>'
               f'<script defer src="{shared}/olympic-guide.js"></script>')
    block = START + assets + widget + scripts + END
    closing = re.search(r'</(?:body|html)\s*>', html, re.I)
    index = closing.start() if closing else len(html)
    updated = html[:index] + block + html[index:]
    path.write_bytes(updated.encode('utf-8'))
    return True


if __name__ == '__main__':
    shared = BASE / '共享组件'
    (shared / 'olympic-widget.css').write_text(CSS.split('>', 1)[1].rsplit('</style>', 1)[0], encoding='utf-8')
    controls = JS.split('>', 1)[1].split('function pulse()', 1)[0]
    (shared / 'olympic-widget.js').write_text(controls + '})();\n', encoding='utf-8')
    changed = [str(path.relative_to(ROOT)) for path in PAGES if enhance(path)]
    print(f'Enhanced {len(changed)} delivered pages')
