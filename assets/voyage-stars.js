/* 与首页 GSAP 进度同步的离线星空；不启动常驻动画循环。 */
(()=>{
 const canvas=document.querySelector('#voyage-stage .voyage-stars');
 if(!canvas)return;
 const ctx=canvas.getContext('2d',{alpha:true});
 if(!ctx)return;
 const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const seeds=Array.from({length:170},(_,i)=>{
  const hash=n=>{const v=Math.sin(n*127.1+78.233)*43758.5453;return v-Math.floor(v)};
  const a=hash(i+1)*Math.PI*2,r=Math.sqrt(hash(i+341));
  return {x:Math.cos(a)*r,y:Math.sin(a)*r,z:hash(i+811),size:.65+hash(i+1821)*1.45,hue:hash(i+2211)};
 });
 let w=0,h=0,dpr=1;
 function resize(){
  const nw=canvas.clientWidth,nh=canvas.clientHeight,nd=Math.min(devicePixelRatio||1,1.5);
  if(nw===w&&nh===h&&nd===dpr)return;
  w=nw;h=nh;dpr=nd;canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);
  ctx.setTransform(dpr,0,0,dpr,0,0);
 }
 function draw(progress){
  resize();if(!w||!h)return;
  ctx.clearRect(0,0,w,h);
  const cx=w*(w<650?.62:.52),cy=h*.5,span=Math.max(w,h)*.52;
  const travel=reduce?0:progress*3.2;
  for(let i=0;i<7;i++){
   const z=((i/7-travel*.55)%1+1)%1;
   const rad=26+Math.pow(1-z,2.15)*span;
   const opacity=(1-z)*(.055+.06*Math.sin(Math.PI*z));
   if(opacity<.012)continue;
   ctx.beginPath();ctx.ellipse(cx,cy,rad,rad*.63,-.12,.17*Math.PI,1.83*Math.PI);
   ctx.strokeStyle=`rgba(128,185,190,${opacity})`;ctx.lineWidth=Math.max(.6,(1-z)*1.8);ctx.stroke();
  }
  for(const s of seeds){
   const z=((s.z-travel)%1+1)%1;
   const depth=1/(.2+z*1.55),x=cx+s.x*span*depth,y=cy+s.y*span*.68*depth;
   if(x<-12||x>w+12||y<-12||y>h+12)continue;
   const alpha=Math.min(.9,(1-z)*.84)*(z<.08?z/.08:1);
   const color=s.hue>.84?`rgba(238,194,132,${alpha})`:`rgba(197,222,222,${alpha})`;
   const size=s.size*(.55+(1-z)*1.35);
   ctx.fillStyle=color;ctx.beginPath();ctx.arc(x,y,size,0,Math.PI*2);ctx.fill();
   if(!reduce&&z<.55){
    const trail=5+(1-z)*15;
    const angle=Math.atan2(y-cy,x-cx);
    ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x-Math.cos(angle)*trail,y-Math.sin(angle)*trail);
    ctx.strokeStyle=color;ctx.lineWidth=Math.max(.5,size*.45);ctx.stroke();
   }
  }
 }
 window.drawVoyageStars=draw;
 addEventListener('resize',()=>draw(window.__voyageStarProgress||0),{passive:true});
 const original=window.drawVoyageStars;
 window.drawVoyageStars=p=>{window.__voyageStarProgress=p;original(p)};
 draw(0);
})();
