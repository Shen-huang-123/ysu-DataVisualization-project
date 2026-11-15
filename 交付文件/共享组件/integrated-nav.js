/* Theme state is authoritative: never sample a color mid-transition. */
(()=>{
 const nav=document.getElementById('xz-nav');if(!nav)return;
 const hero=document.querySelector('header.photo-editorial-hero,header.hero,.image-stage');let pending=false;
 function update(){
  pending=false;const rect=hero?.getBoundingClientRect(),navRect=nav.getBoundingClientRect();
  const sampleY=navRect.top+navRect.height/2,overPhoto=!!rect&&rect.top<=sampleY&&rect.bottom>=sampleY;
  const body=document.body,html=document.documentElement,theme=document.getElementById('xz-theme');
  let dark;
  if(theme)dark=body.classList.contains('xz-dark');
  else{const mode=body.dataset.theme||html.dataset.theme;dark=mode==='dark'||body.classList.contains('dark')||html.classList.contains('dark')||body.classList.contains('xz-dark');}
  const ink=overPhoto||dark?'#f3f4ee':'#16343d';
  nav.style.setProperty('--integrated-nav-ink',ink);
  const menu=document.getElementById('xz-menu');if(menu)menu.style.setProperty('--menu-ink',ink);
  nav.style.setProperty('--integrated-nav-shadow',overPhoto?'0 1px 8px #06151bd9':'none');
 }
 function schedule(){if(!pending){pending=true;requestAnimationFrame(update)}}
 const observer=new MutationObserver(update);
 for(const el of [document.body,document.documentElement])observer.observe(el,{attributes:true,attributeFilter:['class','data-theme']});
 const theme=document.getElementById('xz-theme');if(theme)observer.observe(theme,{attributes:true,attributeFilter:['aria-pressed']});
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);addEventListener('pageshow',schedule);update();
})();
