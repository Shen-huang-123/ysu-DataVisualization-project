/* Shared by integrated navigation, including regenerated pages. */
(()=>{
 const base=new URL('.',document.currentScript.src);
 const link=document.createElement('link');link.rel='stylesheet';link.href=new URL('hero-image-fade.css',base);document.head.append(link);
 const transparent=c=>!c||c==='transparent'||c==='rgba(0, 0, 0, 0)';
 function surface(el){while(el){const c=getComputedStyle(el).backgroundColor;if(!transparent(c))return c;el=el.parentElement}return '#152129'}
 function update(){document.querySelectorAll('header').forEach(h=>{
  const photo=h.querySelector('.image-stage-photo,.geopolitics-photo,.legends-photo,.women-hero-photo,.vanished-photo');
  if(!photo&&!getComputedStyle(h).backgroundImage.includes('url('))return;
  h.classList.add('hero-image-fade');
  if(!h.querySelector(':scope>.hero-image-fade-layer')){const fade=document.createElement('div');fade.className='hero-image-fade-layer';fade.setAttribute('aria-hidden','true');h.append(fade)}
  let next=h.nextElementSibling;while(next&&getComputedStyle(next).display==='none')next=next.nextElementSibling;const bg=surface(next||document.body),rgb=bg.match(/[\d.]+/g)||[21,33,41];
  h.style.setProperty('--hero-fade-surface',bg);h.style.setProperty('--hero-fade-soft',`rgba(${rgb.slice(0,3).join(',')},.45)`);
  const light=(Number(rgb[0])*.2126+Number(rgb[1])*.7152+Number(rgb[2])*.0722)>150;
  h.style.setProperty('--hero-fade-ink',light?'#243b42':'#e7efec');
  const bounds=h.getBoundingClientRect();
  h.querySelectorAll('h1,.lead,.xz-lead,.tag,.xz-eyebrow,.women-credit,.legends-credit,.geopolitics-credit,.vanished-credit').forEach(c=>{const r=c.getBoundingClientRect();c.classList.toggle('hero-fade-caption',r.top+r.height/2>bounds.top+bounds.height*.80)});
 })}
 let timer;const schedule=()=>{update();clearTimeout(timer);timer=setTimeout(update,450)};
 new MutationObserver(schedule).observe(document.body,{attributes:true,attributeFilter:['class','data-theme']});
 addEventListener('resize',schedule,{passive:true});addEventListener('load',schedule);schedule();
 const stories=document.querySelector('body.narrative-stories>header.hero');
 if(stories&&!stories.querySelector('.image-stage-cinema')){
  const button=document.createElement('button');button.type='button';button.className='image-stage-cinema stories-cinema';button.textContent='沉浸影像';button.setAttribute('aria-pressed','false');
  const set=on=>{stories.classList.toggle('stories-immersed',on);button.setAttribute('aria-pressed',String(on));button.textContent=on?'返回专题':'沉浸影像';for(const el of stories.querySelectorAll('.hero-copy,.hero-foot'))el.inert=on};
  button.addEventListener('click',()=>set(button.getAttribute('aria-pressed')!=='true'));
  stories.addEventListener('keydown',e=>{if(e.key==='Escape'&&button.getAttribute('aria-pressed')==='true'){set(false);button.focus()}});
  stories.append(button);
 }
})();
