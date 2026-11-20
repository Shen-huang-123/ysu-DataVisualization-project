"""Bring quieter subpages into the main site's motion language.

Only pages without the existing xz-motion-script receive this layer.
"""
from evidence_guard import presentation_html
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGES = sorted(presentation_html(ROOT/'交付文件'))
if (ROOT/'index.html').exists():
    PAGES.append(ROOT/'index.html')
STYLE = '''<style id="ox-motion-bridge-style">
body.ox-flow{--ox-ease:cubic-bezier(.2,1,.25,1)}
body.ox-flow h1{animation:ox-title-in .95s var(--ox-ease) both}
body.ox-flow :is(header,.hero,main) h1 + p,body.ox-flow :is(header,.hero,main) h1 + .lead,body.ox-flow :is(header,.hero,main) h1 + .导语{animation:ox-copy-in 1s var(--ox-ease) .12s both}
body.ox-flow .ox-reveal{opacity:0;transform:translate3d(0,22px,0);transition:opacity .75s ease,transform .8s var(--ox-ease)}
body.ox-flow .ox-reveal.ox-visible{opacity:1;transform:translate3d(0,0,0)}
body.ox-flow a[href]{text-underline-offset:.22em;transition:color .25s ease,opacity .25s ease,transform .25s var(--ox-ease)}
body.ox-flow a[href]:hover{opacity:.84}
body.ox-flow :is(button,select,input[type=range]){transition:filter .2s ease,box-shadow .2s ease,transform .2s var(--ox-ease)}
body.ox-flow button:not(.ox-trigger):not(.ox-close):active{transform:scale(.98)}
body.ox-flow :is(button,a,select,input):focus-visible{outline:3px solid #e2ae5d;outline-offset:3px}
body.ox-flow .ox-stage-line{position:fixed;top:0;left:0;right:0;height:4px;z-index:2147482999;pointer-events:none;background:linear-gradient(90deg,#4b9bc1 0 20%,#d8dad5 20% 40%,#cb6470 40% 60%,#dcaf58 60% 80%,#6eac84 80%);transform-origin:left;transform:scaleX(var(--ox-scroll-progress,0));transition:transform .16s linear}
body.ox-flow.ox-depart{opacity:.68;transform:translateY(-5px);transition:opacity .22s ease,transform .22s ease}
@keyframes ox-title-in{from{opacity:0;transform:translate3d(0,26px,0)}to{opacity:1;transform:translate3d(0,0,0)}}
@keyframes ox-copy-in{from{opacity:0;transform:translate3d(0,15px,0)}to{opacity:1;transform:translate3d(0,0,0)}}
@media(prefers-reduced-motion:reduce){body.ox-flow h1,body.ox-flow :is(header,.hero,main) h1 + p,body.ox-flow :is(header,.hero,main) h1 + .lead,body.ox-flow :is(header,.hero,main) h1 + .导语,body.ox-flow .ox-stage-line{animation:none!important}body.ox-flow .ox-reveal,body.ox-flow.ox-depart,body.ox-flow a[href],body.ox-flow :is(button,select,input[type=range]){opacity:1!important;transform:none!important;transition:none!important}}
</style>'''
SCRIPT = '''<script id="ox-motion-bridge-script">(()=>{
const body=document.body,reduce=matchMedia('(prefers-reduced-motion: reduce)');
body.classList.add('ox-flow');
const line=document.createElement('div');line.className='ox-stage-line';line.setAttribute('aria-hidden','true');body.appendChild(line);
if(reduce.matches)return;
let progressFrame=0;const updateProgress=()=>{progressFrame=0;const max=Math.max(1,document.documentElement.scrollHeight-innerHeight);line.style.setProperty('--ox-scroll-progress',Math.min(1,Math.max(.035,scrollY/max)).toFixed(3))};
const scheduleProgress=()=>{if(!progressFrame)progressFrame=requestAnimationFrame(updateProgress)};
addEventListener('scroll',scheduleProgress,{passive:true});addEventListener('resize',scheduleProgress,{passive:true});scheduleProgress();
const targets=[...new Set([...document.querySelectorAll('main > section,main > article,.wrap > section,.章,.section-block')])];
if('IntersectionObserver'in window){
 const observer=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){entry.target.classList.add('ox-visible');observer.unobserve(entry.target)}},{rootMargin:'0px 0px -32px 0px',threshold:.04});
 for(const el of targets){if(el.closest('.ox-control')||el.hasAttribute('data-no-reveal'))continue;el.classList.add('ox-reveal');if(el.getBoundingClientRect().top<innerHeight-5)el.classList.add('ox-visible');else observer.observe(el)}
}
addEventListener('pageshow',()=>body.classList.remove('ox-depart'));
document.addEventListener('click',e=>{
 const a=e.target.closest('a[href]');if(!a||e.defaultPrevented||e.button!==0||e.metaKey||e.ctrlKey||e.shiftKey||e.altKey||a.hasAttribute('download')||a.target&&a.target!=='_self')return;
 let url;try{url=new URL(a.href,location.href)}catch{return}
 if(url.protocol!==location.protocol||url.pathname===location.pathname||!url.pathname.toLowerCase().endsWith('.html'))return;
 e.preventDefault();if(body.classList.contains('ox-depart'))return;body.classList.add('ox-depart');setTimeout(()=>location.assign(url.href),210);
});
})();</script>'''


def enhance(path: Path) -> bool:
    text = path.read_text(encoding='utf-8')
    text = re.sub(r'<style id="ox-motion-bridge-style">.*?</style>', '', text, flags=re.S)
    text = re.sub(r'<script id="ox-motion-bridge-script">.*?</script>', '', text, flags=re.S)
    if 'xz-motion-script' in text or '</head>' not in text or '</body>' not in text:
        path.write_text(text, encoding='utf-8')
        return False
    text = text.replace('</head>', STYLE+'</head>', 1).replace('</body>', SCRIPT+'</body>', 1)
    path.write_text(text, encoding='utf-8')
    return True


if __name__ == '__main__':
    result = [path for path in PAGES if enhance(path)]
    print(f'Motion bridge added to {len(result)} pages')
