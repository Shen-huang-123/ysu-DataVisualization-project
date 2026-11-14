"""Install the scroll-driven vortex transit on the root entrance page."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'index.html'

STYLE = '''<style id="vortex-transit-style">
.hero>.vortex-stage{position:absolute;inset:0;z-index:0;pointer-events:none;overflow:hidden;opacity:0;will-change:opacity;background:radial-gradient(circle at 70% 48%,#0b34439c 0,#071b21b8 42%,#071b2100 74%);-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 48%);mask-image:linear-gradient(90deg,transparent 0%,#000 48%)}
.hero>.vortex-stage:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 70% 50%,transparent 0 14%,#071b2166 48%,#071b21bc 100%);opacity:.7}
.vortex-well{position:absolute;left:69%;top:48%;width:90vmin;height:90vmin;transform:translate(-50%,-50%);perspective:900px;filter:drop-shadow(0 0 18px #65b5ce45)}
.vortex-ring{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 35deg,#5bb8d5 0 16%,#d7dfd7 17% 32%,#d66f74 33% 48%,#d9b566 49% 66%,#70b08d 67% 83%,#5bb8d5 84%);-webkit-mask:radial-gradient(transparent 64.2%,#000 65.1% 66.1%,transparent 67%);mask:radial-gradient(transparent 64.2%,#000 65.1% 66.1%,transparent 67%);opacity:0;will-change:transform,opacity}
.vortex-ring:nth-child(3n){filter:brightness(.7)}.vortex-ring:nth-child(4n){filter:brightness(1.25)}
.vortex-core{position:absolute;left:50%;top:50%;width:20vmin;height:20vmin;border-radius:50%;transform:translate(-50%,-50%);background:#06171d;box-shadow:0 0 0 1px #e4bd7040,0 0 65px #5bb8d550,inset 0 0 40px #3c9ec547;opacity:0;will-change:transform,opacity}
.vortex-beam{position:absolute;left:50%;top:50%;width:65vmin;height:2px;transform-origin:left center;background:linear-gradient(90deg,#f1d29591,transparent);opacity:0;filter:blur(.5px)}
.vortex-beam:nth-of-type(2){transform:rotate(72deg)}.vortex-beam:nth-of-type(3){transform:rotate(144deg)}.vortex-beam:nth-of-type(4){transform:rotate(216deg)}.vortex-beam:nth-of-type(5){transform:rotate(288deg)}
.vortex-meta{position:absolute;right:clamp(28px,6vw,100px);top:22%;z-index:3;display:grid;gap:8px;text-align:right;color:#f7d89a;opacity:0;transform:translateY(18px);pointer-events:none;letter-spacing:.16em}.vortex-meta strong{font:400 clamp(48px,7vw,105px)/1 Georgia,serif;font-variant-numeric:tabular-nums}.vortex-meta small{font:600 12px/1.5 "Microsoft YaHei",system-ui,sans-serif}
.hero>.hero-content,.hero>.hero-foot{position:relative;z-index:2;will-change:transform,opacity}.hero>.hero-photo{will-change:transform}
@media(max-width:650px){.hero>.vortex-stage{-webkit-mask-image:none;mask-image:none}.vortex-well{left:58%;top:46%;width:105vmin;height:105vmin}.vortex-meta{display:none}}
@media(prefers-reduced-motion:reduce){.hero>.vortex-stage,.vortex-meta{display:none!important}.hero>.hero-content,.hero>.hero-foot,.hero>.hero-photo{will-change:auto}}
</style>'''

STAGE = '''<div class="vortex-stage" aria-hidden="true"><div class="vortex-well"><div class="vortex-core"></div>'''+''.join('<i class="vortex-ring"></i>' for _ in range(12))+''.join('<i class="vortex-beam"></i>' for _ in range(5))+'''</div></div><div class="vortex-meta" aria-hidden="true"><strong id="vortex-year">1896</strong><small>穿越一百余年奥运记忆</small></div>'''

SCRIPTS = '''<script src="交付文件/共享组件/gsap/gsap.min.js"></script>
<script src="交付文件/共享组件/gsap/ScrollTrigger.min.js"></script>
<script id="vortex-transit-script">(()=>{
const hero=document.querySelector('#top.hero'),stage=hero?.querySelector('.vortex-stage');
if(!hero||!stage||!window.gsap||!window.ScrollTrigger||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
gsap.registerPlugin(ScrollTrigger);
const photo=hero.querySelector('.hero-photo'),content=hero.querySelector('.hero-content'),foot=hero.querySelector('.hero-foot'),rings=[...hero.querySelectorAll('.vortex-ring')],beams=[...hero.querySelectorAll('.vortex-beam')],core=hero.querySelector('.vortex-core'),meta=hero.querySelector('.vortex-meta'),year=hero.querySelector('#vortex-year');
const state={p:0},clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
function render(){
 const p=state.p,emerge=clamp((p-.06)/.42,0,1),leave=innerWidth<650?clamp((p-.24)/.24,0,1):clamp((p-.52)/.3,0,1),flight=clamp((p-.18)/.72,0,1);
 gsap.set(stage,{opacity:emerge});
 if(p>.005)gsap.set(photo,{scale:1+p*.26,x:-p*34,y:-p*20});
 gsap.set(content,{opacity:1-leave,y:-leave*70,scale:1-leave*.045});
 content.style.pointerEvents=leave>.96?'none':'';
 gsap.set(foot,{opacity:1-clamp(p/.32,0,1)});
 gsap.set(core,{opacity:emerge*.88,scale:.5+flight*.9});
 gsap.set(meta,{opacity:clamp((p-.35)/.22,0,1)*(1-clamp((p-.84)/.16,0,1)),y:18*(1-emerge)});
 year.textContent=String(Math.round((1896+p*132)/4)*4);
 rings.forEach((ring,i)=>{const depth=(i/12+p*2.05)%1,edge=Math.sin(Math.PI*depth);gsap.set(ring,{scale:.13+3.05*depth*depth,rotation:p*285+i*17,opacity:emerge*Math.pow(edge,1.2)*.78})});
 beams.forEach((beam,i)=>gsap.set(beam,{opacity:emerge*.12*(.5+.5*Math.sin(p*14+i)),rotation:i*72+p*90,scaleX:.7+flight*.9}));
}
gsap.to(state,{p:1,ease:'none',onUpdate:render,scrollTrigger:{id:'hero-vortex-transit',trigger:hero,start:'top top',end:()=>'+='+Math.round(innerHeight*(innerWidth<650?1.05:1.45)),pin:true,scrub:.6,anticipatePin:1,invalidateOnRefresh:true}});
render();
})();</script>'''

def main():
    html = PAGE.read_text(encoding='utf-8')
    html = re.sub(r'<style id="vortex-transit-style">.*?</style>', '', html, flags=re.S)
    html = re.sub(r'<script src="交付文件/共享组件/gsap/gsap.min.js"></script>\s*<script src="交付文件/共享组件/gsap/ScrollTrigger.min.js"></script>\s*<script id="vortex-transit-script">.*?</script>', '', html, flags=re.S)
    html = re.sub(r'<div class="vortex-stage".*?<div class="vortex-meta".*?</div>', '', html, count=1, flags=re.S)
    html = html.replace('</head>', STYLE+'</head>', 1)
    html = html.replace('<div class="hero-photo" aria-hidden="true"></div><div class="hero-content">', '<div class="hero-photo" aria-hidden="true"></div>'+STAGE+'<div class="hero-content">', 1)
    if '<script id="index-deep-journey-script">' in html:
        html = html.replace('<script id="index-deep-journey-script">', SCRIPTS+'<script id="index-deep-journey-script">', 1)
    else:
        html = html.replace('</body>', SCRIPTS+'</body>', 1)
    PAGE.write_text(html, encoding='utf-8')
    print('Root hero vortex installed')

if __name__ == '__main__': main()
