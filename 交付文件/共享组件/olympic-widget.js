(()=>{
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
})();
