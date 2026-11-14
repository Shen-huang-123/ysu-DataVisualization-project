"""Turn the root index into a fixed, scroll-driven seven-scene vortex story."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / 'index.html'
MEDIA = '交付文件/任务三_专题深挖/媒体/'
TASKS = [
    ('数据体检', '交付文件/任务一_数据体检/index.html'),
    ('百年全景', '交付文件/任务二_百年全景/05_交互总览/index.html'),
    ('专题深挖', '交付文件/任务三_专题深挖/统一中文入口/index.html'),
    ('开放创作', '交付文件/任务四_开放创作/index.html'),
]

SCENES = [
    dict(kind='cover', image='host.jpg', tag='1896—2028 · 奥运数据视觉作品', title='百年圣火<br><em>谁被看见？</em>', copy='一枚奖牌、一条记录、一个参赛机会。沿着数据的纹理，重新看见一百多年的奥运。', action='开始深入', href='#voyage-1'),
    dict(kind='rank', image='lens.jpg', tag='第一站 · 统计口径', title='换一种算法，<br><em>换一张榜单。</em>', copy='同一届奥运，同一支代表团。统计单位一变，排名就会改写。', action='查看完整证据', href='交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'),
    dict(kind='task', image='growth.jpg', tag='任务一 · 数据体检', title='一枚奖牌，<br><em>究竟怎么算？</em>', copy='先厘清体育大类、特殊届次与统计单位。每一个处理决定，都可以回到数据里复算。', action='进入数据体检', href=TASKS[0][1]),
    dict(kind='task', image='women.jpg', tag='任务二 · 百年全景', title='谁走进赛场，<br><em>谁留下成绩？</em>', copy='把代表团、性别与运动项目放进同一条时间线，看见规模、机会与成绩如何变化。', action='进入百年全景', href=TASKS[1][1]),
    dict(kind='task', image='dynasty.jpg', tag='任务三 · 专题深挖', title='十个问题，<br><em>十次追问。</em>', copy='从东道主效应到冠军王朝。每个故事都接受反例、替代解释与证据边界的检验。', action='进入专题深挖', href=TASKS[2][1]),
    dict(kind='task', image='la.jpg', tag='任务四 · 开放创作', title='历史能告诉我们<br><em>多少未来？</em>', copy='交互看板、洛杉矶 2028 预测与数据新闻，把已知、假设和不确定性分开呈现。', action='进入开放创作', href=TASKS[3][1]),
    dict(kind='final', image='host.jpg', tag='最后一站 · 正式材料', title='看见故事，<br><em>也看见证据。</em>', copy='从任意任务进入交互作品，或直接阅读统一报告、答卷与海报。', action='', href=''),
]

STYLE = '''<style id="index-vortex-story-style">
html.voyage-live{scroll-behavior:auto}
body.voyage-live{background:#071b21;color:#f6f3ec;overflow-x:hidden}
body.voyage-live :is(.hero,.intro,.chapters,.material,.footer){display:none!important}
body.voyage-live :is(.progress,.ox-stage-line){display:none!important}
body.voyage-live>a[href*="结论稳定性地图"]{display:none!important}
#voyage-stage,#voyage-scrollspace{display:none}
body.voyage-live #voyage-stage{display:block;position:fixed;inset:0;z-index:10;overflow:hidden;background:#071b21;isolation:isolate}
body.voyage-live #voyage-scrollspace{display:block;height:700svh;pointer-events:none}
.voyage-scene{position:absolute;inset:0;display:grid;align-items:center;overflow:hidden;opacity:0;visibility:hidden;pointer-events:none;will-change:transform,opacity}
.voyage-scene[data-scene="0"]{opacity:1;visibility:visible}
.voyage-photo{position:absolute;inset:0;background-position:center;background-size:cover;filter:saturate(.82);transform:scale(1.04)}
.voyage-scene:after{content:"";position:absolute;inset:0;z-index:0;background:linear-gradient(90deg,#071b21fa 0%,#071b21dc 38%,#071b218f 72%,#071b21aa 100%)}
.voyage-tunnel{position:absolute;inset:0;z-index:8;pointer-events:none;overflow:hidden;opacity:0;-webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 48%);mask-image:linear-gradient(90deg,transparent 0%,#000 48%)}.voyage-tunnel:before{content:"";position:absolute;inset:0;background:radial-gradient(circle at 73% 49%,#2a657b55 0%,transparent 43%)}
.voyage-well{position:absolute;left:73%;top:49%;width:88vmin;height:88vmin;transform:translate(-50%,-50%)}
.voyage-warp{position:absolute;inset:0;z-index:7;pointer-events:none;opacity:0;overflow:hidden}.voyage-warp:after{content:"";position:absolute;left:73%;top:49%;width:20vmin;height:20vmin;transform:translate(-50%,-50%);border-radius:50%;background:radial-gradient(circle,#e6d3a79c 0%,#8bbfc079 20%,transparent 68%);filter:blur(12px)}.voyage-streak{position:absolute;left:73%;top:49%;width:78vmin;height:1px;transform-origin:left center;background:linear-gradient(90deg,transparent 0%,var(--ray) 42%,transparent 100%);opacity:0;will-change:transform,opacity}
.voyage-ring{position:absolute;inset:0;border-radius:50%;background:conic-gradient(from 22deg,transparent 0 9%,var(--arc) 17% 29%,transparent 37% 58%,var(--arc) 66% 77%,transparent 84%);-webkit-mask:radial-gradient(transparent 64%,#000 65% 66%,transparent 67%);mask:radial-gradient(transparent 64%,#000 65% 66%,transparent 67%);opacity:0;will-change:transform,opacity}
.voyage-content{position:relative;z-index:2;width:min(1280px,100%);margin:auto;padding:110px clamp(24px,6vw,96px) 125px}
.voyage-tag{display:flex;align-items:center;gap:14px;color:#efc68c;font:700 12px/18px "Microsoft YaHei",system-ui,sans-serif;letter-spacing:.14em}.voyage-tag:before{content:"";width:38px;height:1px;background:currentColor}
.voyage-content h1{max-width:850px;margin:24px 0 24px;font:500 clamp(64px,8.2vw,126px)/1.08 "STSong","SimSun",serif;letter-spacing:-.07em;text-wrap:balance}
.voyage-content h1 em{font-style:normal;color:#f0c58f}
.voyage-scene[data-scene="3"]:after,.voyage-scene[data-scene="4"]:after,.voyage-scene[data-scene="5"]:after{background:linear-gradient(270deg,#071b21fa 0%,#071b21dc 39%,#071b218f 76%,#071b21ad 100%)}
.voyage-scene[data-scene="3"] .voyage-content,.voyage-scene[data-scene="4"] .voyage-content,.voyage-scene[data-scene="5"] .voyage-content{display:flex;flex-direction:column;align-items:flex-end;text-align:right}
.voyage-scene[data-scene="3"] .voyage-tag,.voyage-scene[data-scene="4"] .voyage-tag,.voyage-scene[data-scene="5"] .voyage-tag{flex-direction:row-reverse}
.voyage-copy{max-width:600px;color:#d8e4df;font:400 clamp(16px,1.5vw,20px)/1.75 "Microsoft YaHei",system-ui,sans-serif;text-wrap:pretty}
.voyage-proof{display:flex;align-items:center;gap:12px;width:max-content;max-width:100%;margin:22px 0 0;padding:0;list-style:none;color:#f4e0bf;font:600 12px/20px "Microsoft YaHei",system-ui,sans-serif;letter-spacing:.04em}.voyage-proof li{white-space:nowrap}.voyage-proof li+li:before{content:"·";margin-right:12px;color:#efc58c}
.voyage-task .voyage-content h1,.voyage-rank-layout h1{font-family:"PingFang SC","Microsoft YaHei",system-ui,sans-serif;font-weight:800;letter-spacing:-.065em;line-height:1.12}
.voyage-scene[data-scene="2"]:after{background:linear-gradient(90deg,#f8f5efef 0%,#f8f5efd6 42%,#f8f5ef25 100%)}
.voyage-scene[data-scene="4"]:after{background:linear-gradient(270deg,#f8f5efef 0%,#f8f5efd6 42%,#f8f5ef25 100%)}
.voyage-scene[data-scene="2"] .voyage-content,.voyage-scene[data-scene="4"] .voyage-content{color:#14343d}
.voyage-scene[data-scene="2"] .voyage-content h1 em,.voyage-scene[data-scene="4"] .voyage-content h1 em{color:#14627b}
.voyage-scene[data-scene="2"] .voyage-copy,.voyage-scene[data-scene="4"] .voyage-copy{color:#274c55}
.voyage-scene[data-scene="2"] .voyage-tag,.voyage-scene[data-scene="4"] .voyage-tag,.voyage-scene[data-scene="2"] .voyage-proof,.voyage-scene[data-scene="4"] .voyage-proof{color:#235c6a}
.voyage-scene[data-scene="2"] .voyage-cta,.voyage-scene[data-scene="4"] .voyage-cta{background:#14343d;color:#fff}
.voyage-scene[data-scene="2"] .voyage-cta:hover,.voyage-scene[data-scene="4"] .voyage-cta:hover{background:#235c6a}
.voyage-cta{display:inline-flex;align-items:center;justify-content:space-between;gap:32px;min-height:52px;margin-top:28px;padding:12px 18px 12px 22px;border-radius:999px;background:#e8c494;color:#102d33;text-decoration:none;font:700 14px/20px "Microsoft YaHei",system-ui,sans-serif;transition:transform .5s cubic-bezier(.22,1,.36,1),background .3s}.voyage-cta:hover{transform:translateY(-4px);background:#f4d4aa}.voyage-cta:active{transform:scale(.98)}.voyage-cta:focus-visible{outline:3px solid #fff;outline-offset:4px}
.voyage-rank-layout{display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,.75fr);gap:7vw;align-items:center}.voyage-rank-layout h1{font-size:clamp(56px,6.5vw,96px)}
.voyage-rank{padding:28px 32px;background:#12313bdf;border:1px solid #ffffff54;border-radius:24px;box-shadow:0 25px 70px #0007;backdrop-filter:blur(14px)}
.voyage-rank small{display:block;color:#f0c58f;font:700 12px/18px "Microsoft YaHei",system-ui,sans-serif;letter-spacing:.08em}.voyage-rank strong{display:block;margin:10px 0;font:400 clamp(110px,12vw,174px)/.95 Georgia,serif;color:#f0c58f;font-variant-numeric:tabular-nums}.voyage-rank p{min-height:4.5em;margin:15px 0 0;color:#d8e4df;font:400 15px/1.7 "Microsoft YaHei",system-ui,sans-serif}
.voyage-rank-buttons{display:flex;gap:6px;width:max-content;max-width:100%;padding:5px;border:1px solid #ffffff60;border-radius:999px}.voyage-rank-buttons button{min-height:42px;padding:8px 16px;border:0;border-radius:999px;background:transparent;color:#d8e4df;font:700 13px/20px "Microsoft YaHei",system-ui,sans-serif;cursor:pointer;transition:background .3s,color .3s,transform .5s cubic-bezier(.22,1,.36,1)}.voyage-rank-buttons button:hover{transform:translateY(-2px)}.voyage-rank-buttons button[aria-pressed="true"]{background:#e8c494;color:#102d33}.voyage-rank-buttons button:focus-visible{outline:3px solid #fff;outline-offset:3px}
.voyage-final .voyage-content h1{font-size:clamp(56px,6.7vw,98px)}.voyage-materials{display:flex;flex-wrap:wrap;gap:12px;margin-top:34px}.voyage-materials a{display:grid;gap:8px;min-width:190px;min-height:110px;padding:20px 22px;border:1px solid #ffffff54;border-radius:18px;background:#173943db;color:#f4f3ed;text-decoration:none;transition:transform .5s cubic-bezier(.22,1,.36,1),background .3s}.voyage-materials a:hover{transform:translateY(-5px);background:#24515b}.voyage-materials strong{font:700 18px/28px "Microsoft YaHei",system-ui,sans-serif}.voyage-materials small{color:#c5d7d3;font:400 12px/18px "Microsoft YaHei",system-ui,sans-serif}
.voyage-bottom{position:absolute;left:clamp(24px,6vw,96px);right:clamp(24px,6vw,96px);bottom:25px;z-index:20;display:flex;align-items:center;gap:25px;color:#dce6e2;font:700 12px/18px "Microsoft YaHei",system-ui,sans-serif;letter-spacing:.08em}.voyage-bottom>span{white-space:nowrap}.voyage-bottom .voyage-instruction{margin-left:auto;color:#b9d0cc}
.voyage-stage-light .voyage-bottom{color:#183b45}.voyage-stage-light .voyage-bottom .voyage-instruction{color:#275866}.voyage-stage-light .voyage-steps button:before{background:#1a4d5a66}.voyage-stage-light .voyage-steps button[aria-current="step"]:before{background:#14627b}
.voyage-steps{display:flex;align-items:center;gap:7px;flex:1;max-width:540px}.voyage-steps button{position:relative;flex:1;height:22px;padding:0;border:0;background:transparent;cursor:pointer}.voyage-steps button:before{content:"";position:absolute;left:0;right:0;top:10px;height:2px;background:#ffffff55;transition:background .3s,transform .5s cubic-bezier(.22,1,.36,1)}.voyage-steps button[aria-current="step"]:before{background:#efc58c;transform:scaleY(2)}.voyage-steps button:hover:before{background:#fff}.voyage-steps button:focus-visible{outline:2px solid #fff;outline-offset:3px}
.voyage-direct{position:absolute;right:18px;top:50%;z-index:21;transform:translateY(-50%);display:grid;gap:6px;padding:7px;border:1px solid #ffffff50;border-radius:18px;background:#102b34de;backdrop-filter:blur(14px)}.voyage-direct a{position:relative;display:grid;place-items:center;width:38px;height:38px;border-radius:11px;color:#102b34;text-decoration:none;font:700 12px/1 Georgia,serif;background:#dfbd89;transition:transform .5s cubic-bezier(.22,1,.36,1)}.voyage-direct a:nth-child(2){background:#9bcbd5}.voyage-direct a:nth-child(3){background:#d5a4a7}.voyage-direct a:nth-child(4){background:#a9c99d}.voyage-direct a:hover{transform:scale(1.08)}.voyage-direct a:focus-visible{outline:3px solid #fff;outline-offset:3px}.voyage-direct a span{position:absolute;right:48px;top:50%;transform:translate(8px,-50%);padding:10px 13px;border:1px solid #ffffff48;border-radius:10px;background:#102b34f5;color:#fff;white-space:nowrap;font:600 12px/16px "Microsoft YaHei",system-ui,sans-serif;opacity:0;pointer-events:none;transition:opacity .3s,transform .5s cubic-bezier(.22,1,.36,1)}.voyage-direct a:hover span,.voyage-direct a:focus-visible span{opacity:1;transform:translate(0,-50%)}
.voyage-direct{gap:3px;border-color:#ffffff35;border-radius:20px;background:#102b34e8;box-shadow:0 12px 36px #051a2260}.voyage-direct a,.voyage-direct a:nth-child(n){background:transparent;color:#e6eee9;border-radius:13px;font:700 13px/1 "PingFang SC","Microsoft YaHei",system-ui,sans-serif}.voyage-direct a:hover{background:#ffffff24;transform:none}.voyage-direct a[aria-current="step"]{background:#e9c797;color:#17343b}
@media(max-width:650px){.voyage-photo{background-position:58% center}.voyage-scene:after,.voyage-scene[data-scene="3"]:after,.voyage-scene[data-scene="5"]:after{background:#071b21c4}.voyage-tunnel{-webkit-mask-image:none;mask-image:none}.voyage-well{left:72%;top:43%;width:110vmin;height:110vmin}.voyage-warp:after,.voyage-streak{left:72%;top:43%}.voyage-content{padding:100px 24px 104px}.voyage-scene[data-scene="3"] .voyage-content,.voyage-scene[data-scene="5"] .voyage-content{display:block;text-align:left}.voyage-scene[data-scene="3"] .voyage-tag,.voyage-scene[data-scene="5"] .voyage-tag{flex-direction:row}.voyage-content h1{font-size:clamp(48px,13vw,64px);max-width:100%;line-height:1.12}.voyage-copy{font-size:16px;line-height:1.6;max-width:32ch}.voyage-rank-layout{display:block}.voyage-rank-layout h1{font-size:48px;margin:12px 0}.voyage-rank-layout .voyage-copy{display:none}.voyage-rank{margin-top:22px;padding:18px 20px;border-radius:18px}.voyage-rank strong{font-size:86px;margin:4px 0}.voyage-rank p{font-size:13px;line-height:1.5;min-height:3em;margin-top:10px}.voyage-rank-buttons button{min-height:38px;padding:7px 12px;font-size:12px}.voyage-final .voyage-content h1{font-size:44px}.voyage-final .voyage-copy{display:none}.voyage-materials{margin-top:18px;gap:8px}.voyage-materials a{min-width:0;width:100%;min-height:69px;padding:10px 15px;gap:2px;border-radius:13px}.voyage-materials strong{font-size:14px;line-height:20px}.voyage-materials small{font-size:11px;line-height:16px}.voyage-bottom{left:24px;right:24px;bottom:78px;gap:12px}.voyage-instruction{display:none}.voyage-direct{top:auto;bottom:12px;left:50%;right:auto;transform:translateX(-50%);display:flex;gap:8px;padding:5px}.voyage-direct a{width:42px;height:38px}.voyage-direct a span{display:none}}
@media(max-width:650px){.voyage-scene[data-scene="4"] .voyage-content{display:block;text-align:left}.voyage-scene[data-scene="4"] .voyage-tag{flex-direction:row}}
@media(max-width:650px){.voyage-scene[data-scene="2"]:after,.voyage-scene[data-scene="4"]:after{background:#f8f5efe7}.voyage-task .voyage-content h1{font-size:clamp(44px,11.7vw,58px);line-height:1.13}.voyage-scene[data-scene="2"] .voyage-photo,.voyage-scene[data-scene="4"] .voyage-photo{filter:grayscale(1) contrast(1.08)}}
@media(max-height:720px) and (max-width:650px){.voyage-content{padding-top:78px;padding-bottom:80px}.voyage-content h1{font-size:44px;margin:10px 0}.voyage-copy{font-size:14px}.voyage-cta{margin-top:12px}.voyage-rank strong{font-size:68px}.voyage-bottom{bottom:70px}}
@media(max-width:650px){.voyage-proof{gap:5px;margin-top:13px;font-size:10px;letter-spacing:0}.voyage-proof li+li:before{margin-right:5px}}
@media(prefers-reduced-motion:reduce){.voyage-scene,.voyage-ring,.voyage-cta,.voyage-materials a,.voyage-direct a{transition:none!important;animation:none!important}.voyage-tunnel,.voyage-warp{display:none}}
</style>'''

def scene_html(i, s):
    img = MEDIA + s['image']
    extra = ''
    if s['kind'] == 'rank':
        extra = '''<div class="voyage-rank"><small>2024 · 西班牙代表团 / 金牌榜</small><strong id="voyage-rank-number" aria-live="polite">15</strong><div class="voyage-rank-buttons" role="group" aria-label="切换奖牌统计口径"><button type="button" data-voyage-rank="official" aria-pressed="true">官方小项</button><button type="button" data-voyage-rank="rows" aria-pressed="false">运动员行</button></div><p id="voyage-rank-explain">按官方小项计，西班牙赢得 5 枚金牌，金牌榜位列第 15。团队项目每个小项仍只计一枚。</p></div>'''
    elif s['kind'] == 'final':
        extra = '''<div class="voyage-materials"><a href="交付文件/最终提交材料/报告/百年圣火_正式报告.pdf"><strong>统一报告 ↗</strong><small>贯穿四项任务的分析主线</small></a><a href="交付文件/最终提交材料/数说奥运_晓组织_正式答卷.pdf"><strong>模板答卷 ↗</strong><small>按照竞赛模板填写的正式答卷</small></a><a href="交付文件/最终提交材料/海报/百年圣火_A2海报_正式版.pdf"><strong>A2 海报 ↗</strong><small>作品的宣传视觉</small></a><a href="交付文件/任务三_专题深挖/11_结论稳定性地图/index.html"><strong>结论稳定性地图 ↗</strong><small>十个专题的反例与证据边界</small></a></div>'''
    cta = f'<a class="voyage-cta" href="{s["href"]}">{s["action"]}<span aria-hidden="true">↗</span></a>' if s['action'] else ''
    proof_steps = {2: ('发现异常', '明确口径', '复算结论'), 3: ('时间演进', '群体差异', '结构变化'), 4: ('提出判断', '寻找反例', '重估结论'), 5: ('历史回测', '情景推演', '区间表达')}
    proof = '<ol class="voyage-proof" aria-label="本任务的分析路径">'+''.join(f'<li>{label}</li>' for label in proof_steps[i])+'</ol>' if i in proof_steps else ''
    inner = f'<div class="voyage-tag">{s["tag"]}</div><h1>{s["title"]}</h1><p class="voyage-copy">{s["copy"]}</p>{proof}{cta}'
    if s['kind'] == 'rank': inner = f'<div class="voyage-rank-layout"><div>{inner}</div>{extra}</div>'
    else: inner += extra
    return f'<section class="voyage-scene voyage-{s["kind"]}" data-scene="{i}" aria-label="{s["tag"]}"><div class="voyage-photo" style="background-image:url(\'{img}\')" aria-hidden="true"></div><div class="voyage-content">{inner}</div></section>'

COLORS = ('#8fc9d5','#d9d8c9','#d59b9f','#dfbd89','#a6c8a8')
TUNNEL = '<div class="voyage-tunnel" aria-hidden="true"><div class="voyage-well">'+''.join(f'<i class="voyage-ring" style="--arc:{COLORS[j%5]}"></i>' for j in range(10))+'</div></div>'
WARP = '<div class="voyage-warp" aria-hidden="true">'+''.join(f'<i class="voyage-streak" style="--ray:{COLORS[j%5]}"></i>' for j in range(24))+'</div>'
STAGE = '<div id="voyage-stage" aria-label="百年圣火滚动旅程">'+''.join(scene_html(i,s) for i,s in enumerate(SCENES))+WARP+TUNNEL+'<nav class="voyage-direct" aria-label="任务直达">'+''.join(f'<a href="{href}" aria-label="进入任务{i}：{label}">{i}<span>{label}</span></a>' for i,(label,href) in enumerate(TASKS,1))+'</nav><div class="voyage-bottom"><span id="voyage-counter">01 / 07</span><div class="voyage-steps" role="group" aria-label="选择旅程章节">'+''.join(f'<button type="button" data-voyage-go="{i}" aria-label="前往第{i+1}幕：{s["tag"]}"{(" aria-current="+chr(34)+"step"+chr(34)) if i==0 else ""}></button>' for i,s in enumerate(SCENES))+'</div><span class="voyage-instruction">滚动深入 · 点击刻度跳转</span></div></div><div id="voyage-scrollspace" aria-hidden="true"></div>'

SCRIPT = '''<script src="交付文件/共享组件/gsap/gsap.min.js"></script><script src="交付文件/共享组件/gsap/ScrollTrigger.min.js"></script>
<script id="index-vortex-story-script">(()=>{
const stage=document.querySelector('#voyage-stage'),spacer=document.querySelector('#voyage-scrollspace');
if(!stage||!spacer||!window.gsap||!window.ScrollTrigger)return;
document.body.classList.add('voyage-live');document.documentElement.classList.add('voyage-live');gsap.registerPlugin(ScrollTrigger);
const scenes=[...stage.querySelectorAll('.voyage-scene')],tunnel=stage.querySelector('.voyage-tunnel'),rings=[...stage.querySelectorAll('.voyage-ring')],warp=stage.querySelector('.voyage-warp'),streaks=[...stage.querySelectorAll('.voyage-streak')],steps=[...stage.querySelectorAll('[data-voyage-go]')],counter=stage.querySelector('#voyage-counter'),state={p:0},reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;let last=-1;
const clamp=(v,a,b)=>Math.max(a,Math.min(b,v));
function render(){
 const pos=state.p*(scenes.length-1),nearest=Math.round(pos),phase=pos-Math.floor(pos),transit=Math.sin(Math.PI*phase);
 scenes.forEach((scene,i)=>{
  const d=Math.abs(pos-i),opacity=reduce?(i===nearest?1:0):clamp((.48-d)/.28,0,1),scale=reduce?1:(i<=pos?1+Math.min(d,1)*.16:.84+Math.max(0,1-d)*.16);
  gsap.set(scene,{opacity,scale,visibility:opacity>.005?'visible':'hidden',pointerEvents:i===nearest?'auto':'none'});
  if(!reduce&&opacity>.005)gsap.set(scene.querySelector('.voyage-photo'),{scale:1.04+(1-opacity)*.1});
 });
 if(!reduce){const visibleTransit=clamp((transit-.18)/.82,0,1);gsap.set(tunnel,{opacity:Math.pow(visibleTransit,1.8)*.82});gsap.set(warp,{opacity:Math.pow(visibleTransit,2.3)*.8});rings.forEach((ring,j)=>{const depth=(j/10+state.p*7.4)%1;gsap.set(ring,{scale:.12+3.3*depth*depth,rotation:state.p*980+j*22,opacity:Math.pow(Math.sin(Math.PI*depth),1.35)*.6})});streaks.forEach((ray,j)=>{const depth=(j/24+state.p*4.8)%1;gsap.set(ray,{rotation:j*137.5+state.p*210,scaleX:.1+depth*1.5,opacity:Math.sin(Math.PI*depth)*.55})})}
 if(nearest!==last){const previous=last;last=nearest;stage.classList.toggle('voyage-stage-light',nearest===2||nearest===4);counter.textContent=String(nearest+1).padStart(2,'0')+' / 07';scenes.forEach((scene,i)=>{scene.inert=i!==nearest;scene.setAttribute('aria-hidden',String(i!==nearest))});if(previous>=0&&scenes[previous].contains(document.activeElement)){const heading=scenes[nearest].querySelector('h1');heading.tabIndex=-1;heading.focus({preventScroll:true})}steps.forEach((button,i)=>{if(i===nearest)button.setAttribute('aria-current','step');else button.removeAttribute('aria-current')});stage.querySelectorAll('.voyage-direct a').forEach((a,i)=>{if(nearest===i+2)a.setAttribute('aria-current','step');else a.removeAttribute('aria-current')})}
}
gsap.to(state,{p:1,ease:'none',onUpdate:render,scrollTrigger:{id:'index-vortex-story',trigger:spacer,start:'top top',end:'bottom bottom',scrub:reduce?true:.55,invalidateOnRefresh:true}});render();
function go(index){const max=Math.max(0,spacer.getBoundingClientRect().height-innerHeight);scrollTo({top:clamp(index,0,scenes.length-1)/(scenes.length-1)*max,behavior:reduce?'instant':'smooth'})}
steps.forEach(button=>button.addEventListener('click',()=>go(Number(button.dataset.voyageGo))));
document.querySelectorAll('.topbar a[href^="#"]').forEach(link=>link.addEventListener('click',e=>{const hash=link.getAttribute('href');if(!['#top','#stories','#materials'].includes(hash))return;e.preventDefault();go(hash==='#top'?0:hash==='#stories'?2:6)}));
stage.querySelector('a[href="#voyage-1"]')?.addEventListener('click',e=>{e.preventDefault();go(1)});
const rankData={official:['15','按官方小项计，西班牙赢得 5 枚金牌，金牌榜位列第 15。团队项目每个小项仍只计一枚。'],rows:['05','按运动员获奖行计，西班牙产生 40 条金牌获奖记录，排名升至第 5。多人项目会放大行数。']};
stage.querySelectorAll('[data-voyage-rank]').forEach(button=>button.addEventListener('click',()=>{const key=button.dataset.voyageRank;stage.querySelectorAll('[data-voyage-rank]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));stage.querySelector('#voyage-rank-number').textContent=rankData[key][0];stage.querySelector('#voyage-rank-explain').textContent=rankData[key][1]}));
document.addEventListener('keydown',e=>{if(!document.body.classList.contains('voyage-live')||e.altKey||e.ctrlKey||e.metaKey||e.target.closest('input,textarea,select,button,a,[contenteditable]'))return;if(e.key==='ArrowDown'||e.key==='PageDown'){e.preventDefault();go(Math.min(6,last+1))}else if(e.key==='ArrowUp'||e.key==='PageUp'){e.preventDefault();go(Math.max(0,last-1))}});
})();</script>'''

def main():
    html = PAGE.read_text(encoding='utf-8')
    for style_id in ('vortex-transit-style','index-deep-journey-style','index-vortex-story-style'):
        html = re.sub(r'<style id="'+style_id+r'">.*?</style>', '', html, flags=re.S)
    for script_id in ('vortex-transit-script','index-deep-journey-script','index-vortex-story-script'):
        html = re.sub(r'<script id="'+script_id+r'">.*?</script>', '', html, flags=re.S)
    html = re.sub(r'<script src="交付文件/共享组件/gsap/(?:gsap|ScrollTrigger)\.min\.js"></script>', '', html)
    html = re.sub(r'<div class="vortex-stage".*?<div class="vortex-meta".*?</div>', '', html, count=1, flags=re.S)
    html = re.sub(r'<div class="journey-depth".*?</div></div>', '', html, count=1, flags=re.S)
    html = re.sub(r'<nav class="journey-dock".*?</nav>', '', html, count=1, flags=re.S)
    html = re.sub(r'<div id="voyage-stage".*?<div id="voyage-scrollspace" aria-hidden="true"></div>', '', html, count=1, flags=re.S)
    html = html.replace('<body class="immersive-index">','<body>',1)
    html = html.replace('</head>', STYLE+'</head>', 1)
    html = html.replace('<header class="hero" id="top">', STAGE+'<header class="hero" id="top">', 1)
    html = html.replace('</body>', SCRIPT+'</body>', 1)
    PAGE.write_text(html, encoding='utf-8')
    print('Fixed seven-scene vortex story installed')

if __name__ == '__main__': main()
