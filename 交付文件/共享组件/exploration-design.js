/* Page-specific analytical views. Existing chart data and click handlers remain the source. */
(()=>{
 const path=decodeURIComponent(location.pathname),reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const main=document.querySelector('main')||document.body;
 // Keep existing Olympic photography; separate it from layered legacy backgrounds.
 document.querySelectorAll('header.photo-editorial-hero').forEach(hero=>{
  const bg=getComputedStyle(hero).backgroundImage,match=[...bg.matchAll(/url\(["']?(.*?)["']?\)/g)].pop();
  if(!match)return;
  const photo=document.createElement('img');photo.className='image-stage-photo';photo.src=match[1];photo.alt='';photo.setAttribute('aria-hidden','true');photo.setAttribute('data-no-zoom','');photo.decoding='async';
  hero.style.setProperty('--image-stage-position',getComputedStyle(hero).backgroundPosition.split(',').pop().trim());
  hero.prepend(photo);hero.classList.add('image-stage');
  const cinema=element('button','沉浸影像','image-stage-cinema');cinema.type='button';cinema.setAttribute('aria-pressed','false');
  const setCinema=on=>{hero.classList.toggle('image-stage-immersed',on);cinema.setAttribute('aria-pressed',String(on));cinema.textContent=on?'返回专题':'沉浸影像'};
  cinema.onclick=()=>setCinema(cinema.getAttribute('aria-pressed')!=='true');hero.append(cinema);
  hero.addEventListener('keydown',e=>{if(e.key==='Escape'){setCinema(false);cinema.focus()}});
  const rail=element('div',null,'image-stage-lanes');rail.setAttribute('aria-hidden','true');for(let i=0;i<5;i++)rail.append(element('i'));hero.append(rail);
  if(!reduce){let scheduled=false;const update=()=>{scheduled=false;const rect=hero.getBoundingClientRect();if(rect.bottom<0||rect.top>innerHeight)return;const progress=Math.max(0,Math.min(1,-rect.top/Math.max(1,rect.height)));hero.style.setProperty('--cinema-travel',progress.toFixed(4))};const request=()=>{if(!scheduled){scheduled=true;requestAnimationFrame(update)}};addEventListener('scroll',request,{passive:true});addEventListener('resize',request,{passive:true});update()}

 });

 const bars=[...document.querySelectorAll('main .chart button.bar[data-i]')];
 const profiles=[['S5_','growth','届次透镜','沿时间轴拖动，核对每一届的奖牌行变化。'],['S8_','balance','平等的距离','50% 是比较参照，不代表不同小项的夺牌机会完全相同。'],['S3_地缘','gaps','历史断点','用真实年份间距阅读变化；总量缺口不能单独证明抵制原因。'],['S4_小','compare','双案例对照','选择两个代表团，比较原图中的获奖行；这不是效率排名。'],['S6_','identity','身份核验台','按原页面的身份标签检索；未核验记录不能当作真实个人排名。'],['S9_','archive','赛场档案柜','按项目名检索，查看数据中出现的届数；出现次数不等于永久退出。'],['S10_','rank','项目机会谱','点选项目联动原有详情。刻度仍沿用原图的获奖行口径。']];
 const profile=(document.body.classList.contains('vanished-topic')||document.body.classList.contains('legends-topic'))?null:profiles.find(x=>path.includes(x[0]));
 function element(tag,text,cls){const e=document.createElement(tag);if(text)e.textContent=text;if(cls)e.className=cls;return e}
 if(profile&&bars.length){
  const [,mode,title,description]=profile,chart=bars[0].parentElement;
  const data=bars.map(b=>({label:b.querySelector('.label')?.textContent.trim()||'',value:parseFloat(b.querySelector('strong').textContent.replaceAll(',','')),display:b.querySelector('strong').textContent,button:b}));
  const box=element('section',null,'ex-design ex-'+mode),heading=element('h3',title),note=element('p',description),tools=element('div',null,'ex-tools'),stage=element('div',null,'ex-stage');
  box.append(heading,note,tools,stage);chart.before(box);
  const original=element('button','查看原始条形图');original.type='button';original.setAttribute('aria-expanded','false');tools.append(original);chart.classList.add("ex-original-chart");chart.hidden=true;
  original.onclick=()=>{chart.hidden=!chart.hidden;original.textContent=chart.hidden?'查看原始条形图':'收起原始条形图';original.setAttribute('aria-expanded',String(!chart.hidden))};
  const output=element('output',null,'ex-readout');box.append(output);
  let chosen=0;
  function choose(i){chosen=i;data[i].button.click();output.textContent=data[i].label+' · '+data[i].display;stage.querySelectorAll('[data-point]').forEach(e=>e.setAttribute('aria-pressed',String(+e.dataset.point===i)));}
  if(['growth','balance','gaps','rank'].includes(mode)){
   const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');svg.setAttribute('viewBox','0 0 840 330');svg.setAttribute('role','img');svg.setAttribute('aria-label',title+'，精确值可用下方滑块选择');
   const max=mode==='balance'?100:Math.max(...data.map(x=>x.value))*1.08;
   const years=data.map(x=>+x.label),minYear=Math.min(...years),yearSpan=Math.max(...years)-minYear;
   function x(i){return 55+(mode==='rank'?i/Math.max(1,data.length-1):(years[i]-minYear)/Math.max(1,yearSpan))*750}
   function y(v){return 270-v/max*220}
   function shape(tag,attrs){const e=document.createElementNS(ns,tag);for(const [k,v]of Object.entries(attrs))e.setAttribute(k,v);svg.append(e);return e}
   for(const v of [0,max/2,max]){shape('line',{x1:55,x2:805,y1:y(v),y2:y(v),class:'ex-grid'});const t=shape('text',{x:8,y:y(v)+4});t.textContent=mode==='balance'?v+'%':Math.round(v).toLocaleString('zh-CN')}
   if(mode==='balance'){shape('line',{x1:55,x2:805,y1:y(50),y2:y(50),class:'ex-reference'});const t=shape('text',{x:635,y:y(50)-9});t.textContent='50% 比较参照'}
   if(mode!=='rank')shape('path',{d:data.map((d,i)=>(i?'L':'M')+x(i)+','+y(d.value)).join(' '),class:'ex-series',fill:'none'});
   data.forEach((d,i)=>{if(mode==='rank')shape('line',{x1:x(i),x2:x(i),y1:270,y2:y(d.value),class:'ex-stem'});const c=shape('circle',{cx:x(i),cy:y(d.value),r:5,class:'ex-dot','data-point':i});const t=document.createElementNS(ns,'title');t.textContent=d.label+'：'+d.display;c.append(t);c.addEventListener('click',()=>{range.value=i;choose(i)});if(i===0||i===data.length-1||data.length<12){const text=shape('text',{x:x(i),y:301,'text-anchor':'middle'});text.textContent=mode==='rank'?'项目'+(i+1):d.label}});
   stage.append(svg);const range=element('input');range.type='range';range.min=0;range.max=data.length-1;range.value=0;range.setAttribute('aria-label','选择'+(mode==='rank'?'运动项目':'届次'));range.oninput=()=>choose(+range.value);stage.append(range);
  }else if(mode==='compare'){
   const pair=element('div',null,'ex-pair');const selects=[];for(let n=0;n<2;n++){const col=element('div');const select=element('select');select.setAttribute('aria-label','对照代表团'+(n+1));data.forEach((d,i)=>{const o=element('option',d.label);o.value=i;select.append(o)});select.value=n;const value=element('strong'),detail=element('p');col.append(select,value,detail);pair.append(col);selects.push(select);select.onchange=()=>{const d=data[+select.value];d.button.click();value.textContent=d.display;detail.textContent=document.querySelector('#detail')?.textContent||''};select.onchange()}stage.append(pair);
  }else{
   const input=element('input');input.type='search';input.placeholder=mode==='archive'?'检索运动项目':'检索姓名或身份标签';input.setAttribute('aria-label',input.placeholder);tools.append(input);const grid=element('div',null,'ex-archive-grid');data.forEach((d,i)=>{const b=element('button',null,'ex-record');b.type='button';b.dataset.point=i;b.append(element('span',d.label),element('strong',d.display),element('small',mode==='archive'?'出现届数 · 点击查看档案':'原始金牌行 · 点击核验身份'));b.onclick=()=>choose(i);grid.append(b)});stage.append(grid);input.oninput=()=>{[...grid.children].forEach((b,i)=>b.hidden=!data[i].label.includes(input.value.trim()))};
  }
  choose(0);
 }
 // Keep Olympic identity in existing imagery and rings, not repeated heading ornaments.
 main.classList.add('olympic-interaction-surface');
 main.addEventListener('change',e=>{if(reduce||!e.target.matches('select,input'))return;const region=e.target.closest('.ex-design,.controls,.filters,.toolbar');if(!region)return;region.classList.remove('olympic-selection-set');requestAnimationFrame(()=>region.classList.add('olympic-selection-set'))});
 // A route derived from this page's actual sections, not a second site-wide menu.
 const headings=[...main.querySelectorAll('h2')].filter(h=>!h.closest('nav,dialog,[hidden],.xz-explore')&&!h.textContent.includes('探索全部作品'));
 if(headings.length>1&&!document.body.classList.contains('narrative-module')){
  const route=element('details',null,'ex-route'),summary=element('summary','本页探索路线 · '+headings.length+' 站'),list=element('nav');list.setAttribute('aria-label','本页章节');route.append(summary,list);
  const controls=element('div',null,'ex-tools'),save=element('button','记录当前筛选'),restore=element('button','恢复已记视图'),status=element('output');save.type=restore.type='button';controls.append(save,restore,status);route.append(controls);
  const fields=()=>[...main.querySelectorAll('select,input[type="range"],input[type="checkbox"],input[type="radio"]')].filter(e=>!route.contains(e));
  if(!fields().length)controls.remove();
  let snapshot=null;try{snapshot=JSON.parse(sessionStorage.getItem('ex-view:'+path)||'null')}catch(e){}restore.disabled=!snapshot;
  save.onclick=()=>{snapshot=fields().map(e=>({value:e.value,checked:e.checked}));try{sessionStorage.setItem('ex-view:'+path,JSON.stringify(snapshot))}catch(e){}restore.disabled=false;status.textContent='已记录本页 '+snapshot.length+' 个筛选条件'};
  restore.onclick=()=>{if(!snapshot)return;fields().forEach((e,i)=>{if(!snapshot[i])return;e.value=snapshot[i].value;if(e.type==='checkbox'||e.type==='radio')e.checked=snapshot[i].checked;e.dispatchEvent(new Event('input',{bubbles:true}));e.dispatchEvent(new Event('change',{bubbles:true}))});status.textContent='已恢复记录的筛选条件'};

  headings.forEach((h,i)=>{if(!h.id)h.id='ex-section-'+i;const a=element('a',String(i+1).padStart(2,'0')+'  '+h.textContent.trim());a.href='#'+h.id;a.onclick=e=>{e.preventDefault();h.scrollIntoView({behavior:reduce?'instant':'smooth',block:'start'});if(innerWidth<650)route.open=false};list.append(a)});
  const anchor=document.body.classList.contains('medal-lens-topic')?(main.querySelector('.photo-stage')||main.querySelector('header.hero')):(main.querySelector('.insight')||main.firstElementChild);anchor?.after(route);
 }
 if(!reduce&&'IntersectionObserver' in window){const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('ex-entered');io.unobserve(e.target)}}),{threshold:.08});document.querySelectorAll('.ex-design').forEach(e=>{e.classList.add('ex-motion');io.observe(e)})}
})();



