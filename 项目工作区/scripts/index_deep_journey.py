"""Extend the root page's vortex language through all four task chapters."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'index.html'
TASKS = [
    ('数据体检', '交付文件/任务一_数据体检/index.html'),
    ('百年全景', '交付文件/任务二_百年全景/05_交互总览/index.html'),
    ('专题深挖', '交付文件/任务三_专题深挖/统一中文入口/index.html'),
    ('开放创作', '交付文件/任务四_开放创作/index.html'),
]

STYLE = '''<style id="index-deep-journey-style">
body.immersive-index{background:#071b21;color:#f5f4ef}
.journey-depth{position:fixed;inset:0;z-index:0;overflow:hidden;pointer-events:none;background:#071b21;opacity:0;will-change:opacity}
.journey-depth img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;will-change:opacity,transform}
.journey-depth:before{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,#071b21f2 0%,#071b21c9 46%,#071b21a6 100%)}
.journey-depth .vortex-well{z-index:2;left:76%;top:49%;opacity:.42;filter:drop-shadow(0 0 12px #5bb8d530)}
.journey-depth .vortex-ring{background:conic-gradient(from 35deg,#5bb8d5 0 16%,#d7dfd7 17% 32%,#d66f74 33% 48%,#d9b566 49% 66%,#70b08d 67% 83%,#5bb8d5 84%)}
body.immersive-index :is(.hero,.intro,.chapters,.material,.footer){position:relative;z-index:1}
body.immersive-index .intro{background:transparent;min-height:100svh;display:grid;align-items:center;padding-top:clamp(100px,11vw,150px);padding-bottom:clamp(90px,10vw,140px)}
body.immersive-index .intro-inner{align-items:center}
body.immersive-index :is(.intro h2,.section-head h2,.task-step h3){color:#f5f3ec}
body.immersive-index :is(.intro p,.section-head p,.task-step p){color:#c5d4d3}
body.immersive-index .intro .label,body.immersive-index .chapters .label{color:#e9bd81}
body.immersive-index .rank-scene{padding:32px;border:1px solid #ffffff3d;border-radius:24px;background:#102e37da;backdrop-filter:blur(18px);box-shadow:0 24px 65px #0005}
body.immersive-index .rank-scene:before{display:none}
body.immersive-index .rank-label{color:#ecc18b}
body.immersive-index .rank-number{color:#e8c494}
body.immersive-index .rank-switch{background:#081f26c9;border-color:#668286;box-shadow:none}
body.immersive-index .rank-switch button{color:#d5e0dd}
body.immersive-index .rank-switch button.active{background:#e8c494;color:#102a32}
body.immersive-index .rank-source{color:#f1c68e;border-color:#f1c68e}
body.immersive-index .intro .mini{color:#b5c9c6}
body.immersive-index .chapters{max-width:none;padding:100px clamp(24px,6vw,96px) 130px;background:transparent}
body.immersive-index .section-head{max-width:1320px;margin-left:auto;margin-right:auto;border-color:#ffffff47}
body.immersive-index .task-story{max-width:1320px;margin:auto}
body.immersive-index .task-step{min-height:75svh;border-color:#6b8584;opacity:.44}
body.immersive-index .task-step.active{opacity:1;border-color:#e8b77e}
body.immersive-index .task-step .step-no{color:#e8b77e}
body.immersive-index .task-step a{color:#f2d09d}
body.immersive-index .task-step a:hover{color:#fff}
body.immersive-index .task-viz{border:1px solid #ffffff55;border-radius:24px;box-shadow:0 26px 70px #0008}
body.immersive-index .material{background:#081d25cf;border-top:1px solid #ffffff38;backdrop-filter:blur(14px)}
body.immersive-index .material-grid{gap:16px}
body.immersive-index .material-grid a{min-height:190px;padding:28px;background:#173741b8;border:1px solid #ffffff3d;border-radius:20px;box-shadow:0 18px 42px #0003;transition:transform .5s cubic-bezier(.22,1,.36,1),background .3s,box-shadow .3s}
body.immersive-index .material-grid a:hover{transform:translateY(-7px);background:#214651e3;box-shadow:0 26px 50px #0006}
body.immersive-index .material-grid a:active{transform:scale(.98)}
body.immersive-index .footer{background:#071b21;color:#c9d8d5}
.journey-dock{position:fixed;z-index:80;right:14px;top:50%;width:52px;transform:translateY(-50%);padding:6px;background:#102b34e8;border:1px solid #ffffff49;border-radius:18px;box-shadow:0 16px 45px #0006;backdrop-filter:blur(18px);display:grid;gap:5px;color:#f5f3ed}
.journey-dock>span{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}
.journey-dock a{position:relative;display:flex;align-items:center;justify-content:center;min-height:44px;padding:4px;border-radius:12px;text-decoration:none;color:#e9f1ed;font:600 12px/16px "Microsoft YaHei",system-ui,sans-serif;transition:background .3s,transform .5s cubic-bezier(.22,1,.36,1)}
.journey-dock a:hover,.journey-dock a:focus-visible{background:#315761;transform:translateX(-4px)}.journey-dock a:active{transform:scale(.98)}
.journey-dock i{display:grid;place-items:center;width:28px;height:28px;flex:none;border-radius:50%;font:600 11px/1 Georgia,serif;background:#dfbd89;color:#102b34}.journey-dock a:nth-of-type(2) i{background:#9bcbd5}.journey-dock a:nth-of-type(3) i{background:#d5a4a7}.journey-dock a:nth-of-type(4) i{background:#a9c99d}
.journey-dock a b{position:absolute;right:49px;top:50%;transform:translate(8px,-50%);min-width:92px;padding:10px 12px;border:1px solid #ffffff4d;border-radius:10px;background:#102b34f5;color:#f5f3ed;white-space:nowrap;box-shadow:0 10px 25px #0007;opacity:0;pointer-events:none;transition:opacity .3s,transform .5s cubic-bezier(.22,1,.36,1)}.journey-dock a:hover b,.journey-dock a:focus-visible b{opacity:1;transform:translate(0,-50%)}
@media(max-width:1100px){.journey-dock{right:9px;width:48px}}
@media(max-width:650px){.journey-dock{display:none}body.immersive-index .intro{min-height:auto;padding:100px 22px}body.immersive-index .intro h2{font-size:36px;line-height:1.16}body.immersive-index .rank-scene{padding:24px;margin-top:50px}body.immersive-index .chapters{padding:80px 22px 100px}body.immersive-index .task-step{min-height:42svh}body.immersive-index .task-viz{border-radius:20px}body.immersive-index .material-grid a{min-height:140px;padding:22px}.journey-depth .vortex-well{left:65%;opacity:.25}}
@media(prefers-reduced-motion:reduce){.journey-depth{opacity:1!important}.journey-depth img:first-child{opacity:.2!important}.journey-depth .vortex-well{display:none}.journey-dock a{transition:none!important}}
</style>'''

STAGE = '''<div class="journey-depth" aria-hidden="true"><img src="交付文件/任务三_专题深挖/媒体/growth.jpg" alt=""><img src="交付文件/任务三_专题深挖/媒体/host.jpg" alt=""><img src="交付文件/任务三_专题深挖/媒体/lens.jpg" alt=""><img src="交付文件/任务三_专题深挖/媒体/la.jpg" alt=""><div class="vortex-well">'''+''.join('<i class="vortex-ring"></i>' for _ in range(10))+'''</div></div>'''
DOCK = '<nav class="journey-dock" aria-label="随时进入任务"><span>选择你的赛道</span>'+''.join(f'<a href="{href}" aria-label="进入任务{i}：{label}"><i>{i:02d}</i><b>{label}</b></a>' for i,(label,href) in enumerate(TASKS,1))+'</nav>'

SCRIPT = '''<script id="index-deep-journey-script">(()=>{
const stage=document.querySelector('.journey-depth'),intro=document.querySelector('.intro'),material=document.querySelector('.material');
if(!stage||!intro||!material||!window.gsap||!window.ScrollTrigger||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
gsap.registerPlugin(ScrollTrigger);
const rings=[...stage.querySelectorAll('.vortex-ring')],photos=[...stage.querySelectorAll('img')],steps=[...document.querySelectorAll('.task-step')],state={p:0};
const render=()=>{const p=state.p;gsap.set(stage,{opacity:Math.min(1,p*7+.15)});rings.forEach((ring,i)=>{const depth=(i/10+p*3.2)%1;gsap.set(ring,{scale:.18+2.7*depth*depth,rotation:p*490+i*24,opacity:Math.sin(Math.PI*depth)*.45})});photos.forEach(photo=>gsap.set(photo,{scale:1.04+p*.12}))};
gsap.to(state,{p:1,ease:'none',onUpdate:render,scrollTrigger:{id:'index-deep-journey',trigger:intro,start:'top bottom',endTrigger:material,end:'bottom bottom',scrub:.8,invalidateOnRefresh:true}});
function scene(index){photos.forEach((photo,i)=>gsap.to(photo,{opacity:i===index?.26:0,duration:.8,ease:'power2.out',overwrite:true}))}
scene(0);
for(const [i,step] of steps.entries())ScrollTrigger.create({trigger:step,start:'top 62%',end:'bottom 40%',onEnter:()=>scene(i),onEnterBack:()=>scene(i)});
ScrollTrigger.create({trigger:material,start:'top 60%',onEnter:()=>scene(3),onEnterBack:()=>scene(3)});
render();
})();</script>'''

def main():
    html = PAGE.read_text(encoding='utf-8')
    html = re.sub(r'<style id="index-deep-journey-style">.*?</style>', '', html, flags=re.S)
    html = re.sub(r'<script id="index-deep-journey-script">.*?</script>', '', html, flags=re.S)
    html = re.sub(r'<div class="journey-depth".*?</div></div>', '', html, count=1, flags=re.S)
    html = re.sub(r'<nav class="journey-dock".*?</nav>', '', html, count=1, flags=re.S)
    html = html.replace('</head>', STYLE+'</head>', 1)
    html = html.replace('<header class="hero" id="top">', STAGE+DOCK+'<header class="hero" id="top">', 1)
    html = html.replace('</body>', SCRIPT+'</body>', 1)
    html = html.replace('<body>', '<body class="immersive-index">', 1)
    PAGE.write_text(html, encoding='utf-8')
    print('Root index deep journey installed')

if __name__ == '__main__': main()
