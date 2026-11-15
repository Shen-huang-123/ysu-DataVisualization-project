/* Background scenography only: no data encodings, overlays or input interception. */
(()=>{
 if(document.querySelector('.oa-world'))return;
 const path=decodeURIComponent(location.pathname),body=document.body;
 const kind=path.includes('任务一')?'archive':path.includes('任务二')?'stadium':path.includes('任务四')?'sunset':path.includes('任务三')?'field':'stadium';
 const layer=document.createElement('div');layer.className='oa-world oa-'+kind;layer.setAttribute('aria-hidden','true');
 layer.innerHTML='<div class="oa-grain"></div><div class="oa-light"></div><div class="oa-landscape"></div>';
 body.classList.add('oa-host');body.prepend(layer);
 if(kind==='field')layer.dataset.field=path.includes('S8_')||path.includes('S2_')?'water':path.includes('S6_')||path.includes('冠军')?'track':'court';
 function theme(){
  const explicit=body.dataset.theme||document.documentElement.dataset.theme;
  let dark=explicit==='dark'||body.classList.contains('xz-dark')||body.classList.contains('dark')||document.documentElement.classList.contains('dark');
  if(!explicit&&!document.getElementById('xz-theme')&&!dark){const rgb=getComputedStyle(body).backgroundColor.match(/[\d.]+/g);dark=rgb&&+rgb[3]!==0&&(+rgb[0]*.2126+ +rgb[1]*.7152+ +rgb[2]*.0722)<90}
  layer.dataset.night=String(!!dark);
 }
 new MutationObserver(theme).observe(body,{attributes:true,attributeFilter:['class','data-theme']});
 new MutationObserver(theme).observe(document.documentElement,{attributes:true,attributeFilter:['class','data-theme']});theme();
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');let queued=false,x=0,y=0;
 function paint(){queued=false;if(reduced.matches)return;layer.style.setProperty('--oa-x',x+'px');layer.style.setProperty('--oa-y',y+'px');layer.style.setProperty('--oa-scroll',Math.min(24,scrollY*.012)+'px')}
 function schedule(){if(!queued){queued=true;requestAnimationFrame(paint)}}
 if(matchMedia('(pointer:fine)').matches)addEventListener('pointermove',e=>{x=(e.clientX/innerWidth-.5)*12;y=(e.clientY/innerHeight-.5)*8;schedule()},{passive:true});
 addEventListener('scroll',schedule,{passive:true});
})();
