/* A reading path coordinates existing evidence, not a second analytical model. */
(()=>{
 const kind=document.body.dataset.narrative,main=document.querySelector('main'),chapters=[...document.querySelectorAll('.narrative-chapter')],route=[...document.querySelectorAll('.narrative-route a')],context=document.querySelector('.narrative-context-text');
 if(!kind||!chapters.length)return;
 document.querySelectorAll('.ex-route').forEach(e=>e.remove());
 main.addEventListener('click',()=>requestAnimationFrame(updateContext));
 const reduced=matchMedia('(prefers-reduced-motion: reduce)');let active=-1,pending=false;
 const notes={audit:['标签有名字，不等于保留了小项细节。','名称可以归并，原始标签仍须保留。','检查结果与处理决定是一对证据。','保留历史身份，明确样本边界。','同届、同队，统计单位仍会改写名次。'],panorama:['总量先给出轮廓，筛选再把轮廓变成具体问题。','时间趋势与单届排名回答不同的问题。','名次之外，还要看参与结构与记录单位。'],stories:['同一份数据，统计单位决定可以回答的问题。','差异可以描述；机制需要对照、样本规则与反例。','档案留下的是记录，也留下覆盖和身份的边界。','展开一个反例，让原判断接受另一种解释。'],future:['预测的出发点，是历史中实际留下的记录。','假设是可调整的条件，不是已经发生的事实。','点估计与区间需要连同来源日期、条件一起阅读。','评价规则先确定，实际结果到来后再接受检验。']};
 function updateContext(){
  let text=notes[kind]?.[Math.max(0,active)]||'';
  if(kind==='audit'){
   if(active===0){const year=document.querySelector('#year')?.value;const rows=[...document.querySelectorAll('#status-bars .xz-stat-row')];const generic=rows.find(e=>e.textContent.includes('泛化'));if(generic)text=year+' · '+generic.querySelector('b').textContent+' 条记录的小项标签需结合上下文。这里计的是运动员行。';else if(year)text=year+' · 当前显示具体小项标签；标签具体不等于已完成官方逐项核验。'}
   if(active===1){const q=document.querySelector('#sport-search')?.value.trim();if(q)text='正在核对「'+q+'」的原始名称与归一大类；映射规则见右侧表格。'}
   if(active===2){const open=document.querySelector('#qc-list details[open]');if(open)text=open.querySelector('summary').textContent.replace('查看决定 ↗','').trim()+' · 展开的是结果、代码位置与处理决定。'}
   if(active===4&&typeof D!=='undefined'){const q=document.querySelector('#noc-search')?.value.trim();const row=D.compare.find(d=>q&&(d.delegation.includes(q)||d.NOC.toLowerCase()===q.toLowerCase()))||D.compare.find(d=>d.NOC==='ESP');if(row)text='2024 · '+row.delegation+'：小项名次 '+row.official+'，运动员行名次 '+row.athlete+'。两列都是本页已有的统计结果。'}
  }
  if(kind==='panorama'){
   const year=document.querySelector('#year')?.value||'1896—2024';const metric=document.querySelector('#metric')?.value==='medals'?'获奖运动员行':'参赛记录';const total=document.querySelector('#total')?.textContent||'';const sex=document.querySelector('#sex')?.value;const filter=sex==='F'?' · 女性样本':sex==='M'?' · 男性样本':'';text=year+filter+' · '+total+' '+metric+'。'+(active===2?'表格与上方图形使用同一筛选。':'记录数不等于独立运动员人数或官方奖牌数。');
  }
  context.textContent=text;
 }
 function sync(){pending=false;let index=0;const focus=Math.min(300,innerHeight*.34);chapters.forEach((c,i)=>{if(c.getBoundingClientRect().top<=focus)index=i});if(active!==index){active=index;route.forEach((a,i)=>{if(i===index)a.setAttribute('aria-current','location');else a.removeAttribute('aria-current')});}updateContext()}
 function schedule(){if(!pending){pending=true;requestAnimationFrame(sync)}}
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);addEventListener('pageshow',schedule);
 main.addEventListener('input',()=>requestAnimationFrame(updateContext));main.addEventListener('change',()=>requestAnimationFrame(updateContext));
 main.addEventListener('toggle',()=>requestAnimationFrame(updateContext),true);
 main.querySelectorAll('.narrative-route a,.narrative-bridge a').forEach(a=>a.addEventListener('click',e=>{const target=document.getElementById(a.hash.slice(1));if(!target)return;e.preventDefault();history.replaceState(null,'',a.hash);target.scrollIntoView({behavior:reduced.matches?'instant':'smooth',block:'start'});}));
 main.querySelectorAll('[data-rank-lens]').forEach(b=>b.addEventListener('click',()=>{main.querySelectorAll('[data-rank-lens]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));b.closest('.narrative-chapter').dataset.rankFocus=b.dataset.rankLens;updateContext()}));
 if(kind==='audit'){const rankChapter=main.querySelector('[data-rank-lens]')?.closest('.narrative-chapter');if(rankChapter)rankChapter.dataset.rankFocus='official'}
 main.querySelectorAll('[data-panorama]').forEach(b=>b.addEventListener('click',()=>{
  const values={year:'',noc:'',sex:'',sport:'',metric:'records'};if(b.dataset.panorama==='edition')values.year='2024';if(b.dataset.panorama==='women')values.sex='F';
  Object.entries(values).forEach(([id,value])=>{document.getElementById(id).value=value});document.getElementById('metric').dispatchEvent(new Event('change',{bubbles:true}));
  main.querySelectorAll('[data-panorama]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));updateContext();
 }));
 if(kind==='panorama')main.querySelectorAll('.filters select').forEach(s=>s.addEventListener('change',()=>{main.querySelectorAll('[data-panorama]').forEach(b=>b.setAttribute('aria-pressed','false'))}));
 if(kind==='stories'||kind==='future'){
  const links=[...main.querySelectorAll('a.story,.xz-path>a')];let opened=[];try{opened=JSON.parse(sessionStorage.getItem('narrative-opened:'+kind)||'[]')}catch(e){}
  function mark(){links.forEach(a=>{if(opened.includes(a.getAttribute('href')))a.dataset.opened='true'})}mark();
  links.forEach(a=>{const show=()=>{context.textContent=(a.querySelector('h3')?.textContent||'')+' · '+(a.querySelector('p')?.textContent||'')};a.addEventListener('pointerenter',show);a.addEventListener('focus',show);a.addEventListener('pointerleave',updateContext);a.addEventListener('blur',updateContext);a.addEventListener('click',()=>{const href=a.getAttribute('href');if(!opened.includes(href))opened.push(href);try{sessionStorage.setItem('narrative-opened:'+kind,JSON.stringify(opened))}catch(e){}mark()})});
 }
 if(kind==='stories'){
  const cards=[...main.querySelectorAll('a.story')];const refresh=()=>{main.querySelectorAll('.narrative-topic-group').forEach(g=>g.hidden=[...g.querySelectorAll('a.story')].every(a=>getComputedStyle(a).display==='none'))};
  const observer=new MutationObserver(refresh);cards.forEach(a=>observer.observe(a,{attributes:true,attributeFilter:['style','hidden']}));
 }
 sync();
})();
