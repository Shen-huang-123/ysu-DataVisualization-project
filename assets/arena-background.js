/* Offline scientific network, powered by Vincent Garreau's MIT particles.js. */
(()=>{
 const stage=document.querySelector('.olympic-model');if(!stage||!window.particlesJS)return;
 const layer=document.createElement('div');layer.id='arena-network';layer.setAttribute('aria-hidden','true');stage.prepend(layer);
 const reduce=matchMedia('(prefers-reduced-motion: reduce)');
 particlesJS(layer.id,{particles:{number:{value:innerWidth<750?24:48,density:{enable:false}},color:{value:['#84bbcb','#c8d9dc','#d6bd89']},shape:{type:'circle'},opacity:{value:.45,random:true,anim:{enable:false}},size:{value:2,random:true,anim:{enable:false}},line_linked:{enable:true,distance:190,color:'#81b6c6',opacity:.24,width:1},move:{enable:false,speed:.24,direction:'none',random:false,straight:false,out_mode:'out',bounce:false}},interactivity:{detect_on:'canvas',events:{onhover:{enable:false},onclick:{enable:false},resize:true}},retina_detect:false});
 const engine=window.pJSDom.find(entry=>entry.pJS.canvas.el.parentNode===layer)?.pJS;if(!engine)return;
 let running=false;
 function sync(){const control=document.getElementById('model-life-toggle');const next=!document.hidden&&!reduce.matches&&control?.getAttribute('aria-pressed')==='true';if(next===running)return;running=next;cancelAnimationFrame(engine.fn.drawAnimFrame);engine.particles.move.enable=next;if(next)engine.fn.vendors.draw();layer.dataset.running=String(next)}
 new MutationObserver(sync).observe(stage,{subtree:true,attributes:true,attributeFilter:['aria-pressed'],childList:true});document.addEventListener('visibilitychange',sync);reduce.addEventListener('change',sync);sync();
})();
