/* Short evidence-led overtures. Read existing local data; never change analytical filters on scroll. */
(()=>{
 const kind=document.body.dataset.narrative,main=document.querySelector('main');
 if(!kind||!main)return;
 const evidence=JSON.parse(document.getElementById('narrative-evidence-data')?.textContent||'{}');
 const el=(tag,cls,text)=>{const n=document.createElement(tag);if(cls)n.className=cls;if(text)n.textContent=text;return n};
 const fmt=n=>Number(n).toLocaleString('zh-CN');
 let audit=null,rows=[];
 try{if(kind==='audit'&&typeof D!=='undefined')audit=D;if(kind==='panorama'&&typeof raw!=='undefined')rows=raw}catch(e){}
 const qc=id=>audit?.qc.find(d=>d['编号']===id)?.['实测结果']||'见下方审计';
 const esp=audit?.compare.find(d=>d.NOC==='ESP');
 const yearly=rows.reduce((acc,r)=>{const y=acc[r.Year]??={year:r.Year,records:0,female:0};y.records+=r.records;if(r.Sex==='F')y.female+=r.records;return acc},{});
 const series=Object.values(yearly).sort((a,b)=>a.year-b.year),last=series.at(-1);
 const stories={
 audit:{title:'先相信数字，还是先检查数字？',unit:'数据体检 · 原始记录与处理决定',source:'来源：本页 QC 审计与2024双口径对照；所有数量均保持原统计单位。',steps:[
 ['表格没有空白，故事就完整了吗？','字段缺失为零，只能说明单元格被填满。它还不能回答标签是否具体、姓名能否识别人。','字段缺失数',qc('QC02').match(/\d+/)?.[0]||'0','形式完整 ≠ 语义完整','#explore-audit-1'],
 ['真正的裂缝，藏在字段的含义里。','扩展风险规则找到上下文依赖的小项记录。处理时降低分析粒度，保留原始字段与决定，而不是替它们补写细节。','小项语义风险',fmt(qc('QC09').match(/\d+/)?.[0]||8515),'运动员行；风险标记不等于已确认错误','#explore-audit-3'],
 ['同一支队伍，换个单位就换个位置。','西班牙的2024金牌榜名次随统计单位改变。团队成员产生的多条记录，不能当成多枚官方小项金牌。','西班牙 · 2024',`${esp?.official??15} → ${esp?.athlete??5}`,'官方小项名次 → 运动员行名次','#explore-audit-5']
 ]},
 panorama:{title:'把时间拉远，再把视线停住。',unit:'百年全景 · 来自本页归一记录',source:'来源：任务一归一数据，1906排除。记录数不是独立人数，也不是官方小项数。',steps:[
 ['拉远，看见赛场的扩展。','先沿真实年份间距阅读参赛记录的变化。规模描绘了历史轮廓，也受到项目设置、团队人数和数据覆盖影响。','观察范围',`${series[0]?.year??1896}—${last?.year??2024}`,'参赛记录 · 逐届汇总','#explore-panorama-2'],
 ['停在一届，看见具体的差异。','把百年趋势切换为单届代表团排名，比较对象才共享同一届赛场。下面的筛选和导出始终使用同一份数据。',`${last?.year??2024} · 全部代表团`,last?fmt(last.records):'见下方图表','参赛记录，不是独立运动员人数','#explore-panorama-1'],
 ['换一个人群，历史又有了新轮廓。','女性参赛记录的份额是参与结构的一面镜子。比例变化需要与项目机会、团队规模一起阅读，不能自动解释为机会完全平等。',`${last?.year??2024} · 女性参赛记录占比`,last?(last.female/last.records*100).toFixed(1)+'%':'见下方筛选','分母：当届全部参赛记录','#explore-panorama-1']
 ]},
 stories:{title:'把一个结论，放到反例面前。',unit:'冠军控制权 · 来源与样本敏感性',source:'来源：冠军来源敏感性复算CSV；研究单位为小项金牌代表团控制权，不是个人寿命。二次来源不是现行IOC全项认证。',steps:[
 ['冠军更难延续，这个判断有多稳？','固定113个小项，前后段延续率下降7.37个百分点。先把结论与它的样本、区间一起放到画面中。','固定队列','113 个小项','95%区间未跨零；差值单位为百分点','#explore-stories-2'],
 ['只更换来源，结果没有改变。','在同一113项队列上替换对应二次来源，下降幅度和区间保持不变。这检验的是来源敏感性，不是给所有历史记录盖上官方认证。','同113项来源替换','−7.37 个百分点','同一个样本，检查另一层来源','#explore-stories-4'],
 ['排除未决系列，判断需要收窄。','样本缩至50项，点估计仍是下降，但95%区间跨零。更严格的筛选并未给出同样确定的下降证据；继续进入十专题，看看每个结论能承受怎样的反例。','排除后子队列','区间跨零','改变了样本，不是来源替换推翻了原113项结果','#explore-stories-4']
 ]},
 future:{title:'先检验预测，再想象未来。',unit:'洛杉矶2028 · 同口径回放与条件情景',source:'来源：原RF/GB严格历史选择评分与2028重训情景榜。小项为代理/二次来源奖牌槽；1120是比较条件，不保证官方规模。',steps:[
 ['模型更复杂，就一定更准吗？','在同一小项二次来源口径下，RF/GB在2012、2024两届未胜过历史基准。先看模型在哪些历史回放中失效，再决定把多少信任交给它。','三折回放','2 届未胜出','全体MAE越小越好；这里只比较同单位','#explore-future-1'],
 ['把基准与情景分开，未来才可讨论。','2028主阅读采用中性历史基准。55%基准加45%项目只保留为情景，不把权重叫作最优；新增运动、主场与资格条件也分别讨论。','2028主阅读','中性基准','以美国为读数示例；总池1120仅作比较条件','#explore-future-2'],
 ['还不知道的部分，也要留在画面里。','完整集成同构回测、真实历史冻结快照和新区间校准仍有缺口。保留可复算的点值与条件，提前确定赛后评价规则，不给新榜套上旧区间。','验证边界','等待现实检验','新基准不附未经校准的区间','#explore-future-4']
 ]}
 };
 const data=stories[kind];if(!data)return;
 const sceneNames={audit:['检查字段','追踪语义','核对名次'],panorama:['拉远时间','停在一届','换个分母'],stories:['提出判断','替换来源','排除样本'],future:['历史检验','条件情景','保留边界']}[kind];
 const root=el('section','story-sequence sequence-'+kind);root.setAttribute('aria-label',data.title);
 const head=el('div','sequence-heading');head.append(el('span','sequence-eyebrow','顺着证据，继续追问'),el('h2','',data.title));
 const body=el('div','sequence-body'),visual=el('figure','sequence-visual'),canvas=el('div','sequence-canvas');
 const caption=el('figcaption','sequence-source',data.source);visual.append(el('small','sequence-unit',data.unit),canvas,caption);
 const sourcePhoto=document.querySelector('.image-stage-photo,.story-photo');
 if(sourcePhoto){const photo=el('img','sequence-scene-photo');photo.src=sourcePhoto.currentSrc||sourcePhoto.src;photo.alt='';photo.loading='lazy';photo.decoding='async';visual.prepend(photo)}
 const proof=el('button','sequence-proof','展开证据');proof.type='button';proof.setAttribute('aria-expanded','false');proof.setAttribute('aria-controls','sequence-proof-'+kind);canvas.id='sequence-proof-'+kind;
 let holdTimer,held=false;const reveal=open=>{root.dataset.proof=String(open);proof.setAttribute('aria-expanded',String(open));proof.textContent=open?'收起证据':'展开证据'};
 proof.addEventListener('pointerdown',()=>{held=false;holdTimer=setTimeout(()=>{held=true;reveal(true)},240)});
 proof.addEventListener('pointerup',()=>clearTimeout(holdTimer));proof.addEventListener('pointercancel',()=>clearTimeout(holdTimer));proof.addEventListener('pointerleave',()=>clearTimeout(holdTimer));
 proof.addEventListener('click',()=>{if(!held)reveal(proof.getAttribute('aria-expanded')!=='true');held=false});visual.append(proof);reveal(false);
 const text=el('div','sequence-text');
 const steps=data.steps.map((s,i)=>{
  const article=el('article','sequence-step');article.id='sequence-'+kind+'-'+i;
  article.append(el('small','sequence-index',String(i+1).padStart(2,'0')),el('h3','',s[0]),el('p','',s[1]));
  const inline=el('div','sequence-inline');inline.append(el('small','',s[2]),el('strong','',s[3]),el('span','',s[4]));article.append(inline);
  const a=el('a','sequence-evidence-link','查看对应证据 ↗');a.href=s[5];article.append(a);text.append(article);return article;
 });
 const controls=el('nav','sequence-controls');controls.setAttribute('aria-label','选择故事画面');
 const buttons=steps.map((s,i)=>{const a=el('a','',sceneNames[i]);a.href='#'+s.id;a.setAttribute('aria-label',data.steps[i][0]);controls.append(a);return a});
 const current=el('p','sequence-current');current.setAttribute('aria-live','off');visual.prepend(current);
 visual.append(controls);body.append(visual,text);root.append(head,body);
 main.querySelector('.narrative-cinema')?.remove();
 (main.querySelector('.narrative-opening')||main.firstElementChild).after(root);
 let active=-1;
 const svg=(content,label)=>`<svg viewBox="0 0 640 350" role="img" aria-label="${label}">${content}</svg>`;
 function diagram(i){
  if(kind==='audit'){
   if(i===0)return svg(['Year','Sport','Event','NOC'].map((t,j)=>`<rect class="sequence-record-cell" x="${20+j*154}" y="65" width="140" height="86" rx="8"/><text x="${90+j*154}" y="100" text-anchor="middle">${t}</text><path class="sequence-series" d="M${65+j*154} 127h50"/>`).join('')+'<text x="320" y="205" text-anchor="middle">字段被填满，还要追问标签的含义</text><path class="sequence-grid" d="M60 238H580"/><text x="320" y="286" text-anchor="middle">结构示意 · 不代表某条运动员记录</text>','Year、Sport、Event、NOC四字段示意，字段非空不保证语义完整');
   if(i===1)return svg('<text x="40" y="78">原始标签</text><path class="sequence-series" d="M40 105H600"/><text x="40" y="164">保留字段与处理决定</text><path class="sequence-grid" d="M40 191H600"/><text x="40" y="250">降低分析粒度，避免补写未知小项</text><text x="40" y="310">处理流程示意 · 风险记录不等于确认错误</text>','语义风险处理：保留原始标签、记录决定、降低分析粒度');
   const a=esp?.official??15,b=esp?.athlete??5,x=v=>50+(v-1)/19*540;
   return svg('<text x="50" y="45">西班牙2024 · 名次越小，排名越靠前</text><path class="sequence-grid" d="M50 110H590M50 230H590"/>'+[1,5,10,15,20].map(v=>`<text x="${x(v)}" y="300" text-anchor="middle">${v}</text>`).join('')+`<circle class="sequence-dot" cx="${x(a)}" cy="110" r="9"/><text x="${x(a)-16}" y="92" text-anchor="end">官方小项 · ${a}</text><circle class="sequence-dot" cx="${x(b)}" cy="230" r="9"/><text x="${x(b)+16}" y="236">运动员行 · ${b}</text><path class="sequence-series" stroke-dasharray="5 5" d="M${x(a)} 122L${x(b)} 218"/>`,'西班牙官方小项第15、运动员行第5；横轴为名次');
  }
  if(kind==='stories'&&evidence.intervals){
   const x=v=>65+(v+20)/25*510,z=x(0);let marks=`<path class="sequence-grid" d="M${z} 42V270" stroke-dasharray="4 4"/><text x="${z}" y="27" text-anchor="middle">零差值</text>`;
   evidence.intervals.forEach((r,j)=>{const y=85+j*75,selected=i===j;marks+=`<g opacity="${selected?1:.72}"><text x="35" y="${y-25}">${r.n}项 · ${j===0?'原代理':j===1?'来源替换':'排除后'}</text><path class="sequence-series" stroke-width="${selected?5:2}" d="M${x(r.low)} ${y}H${x(r.high)}"/><circle class="sequence-dot" cx="${x(r.delta)}" cy="${y}" r="${selected?7:4}"/><text x="${x(r.high)+10}" y="${y+5}">${r.high>0?'+':''}${r.high.toFixed(2)}</text></g>`});
   marks+=[-20,-10,0,5].map(v=>`<text x="${x(v)}" y="302" text-anchor="middle">${v}</text>`).join('')+'<text x="320" y="340" text-anchor="middle">后段 − 早段 · 百分点；横线为成组95%区间</text>';
   return svg(marks,'113项来源替换区间未跨零；排除后50项的区间跨零，样本变化影响判断');
  }
  if(kind==='future'&&evidence.models){
   if(i===0){const max=Math.max(...evidence.models.flatMap(x=>[x.base,x.model]))*1.15,x=v=>130+v/max*390;return svg(evidence.models.map((r,j)=>{const y=65+j*83;return `<text x="25" y="${y+13}">${r.year}</text><path class="sequence-grid" stroke-width="10" d="M130 ${y}H${x(r.base)}"/><path class="sequence-series" stroke-width="10" d="M130 ${y+25}H${x(r.model)}"/><text x="${x(r.base)+12}" y="${y+5}">${r.base.toFixed(3)}</text><text x="${x(r.model)+12}" y="${y+30}">${r.model.toFixed(3)}</text>`}).join('')+'<text x="130" y="325">浅线：基准；实线：RF/GB · 同口径MAE</text>','2012、2016、2024同口径基准与RF/GB的全体MAE，横条从零开始');}
   if(i===1){const r=evidence.us,x=v=>55+v/160*500;return svg(`<text x="55" y="45">美国2028 · 奖牌槽参考量</text><text x="55" y="90">中性基准</text><path class="sequence-series" stroke-width="12" d="M55 120H${x(r.base)}"/><text x="${x(r.base)+14}" y="125">${r.base.toFixed(1)}</text><text x="55" y="200">55/45条件情景</text><path class="sequence-grid" stroke-width="12" d="M55 230H${x(r.mixed)}"/><text x="${x(r.mixed)+14}" y="235">${r.mixed.toFixed(1)}</text><text x="55" y="312">总池1120 · 无额外主场、排名或资格加成</text>`,'美国2028中性基准133.1、55/45条件情景138.4，点值不是官方成绩');}
   return svg(['逐折同口径比较','完整集成同构回测','新基准区间校准'].map((t,j)=>`<text x="55" y="${80+j*90}">${t}</text><text x="580" y="${80+j*90}" text-anchor="end">${j===0?'已提供':'仍有缺口'}</text><path class="sequence-grid" d="M55 ${100+j*90}H580"/>`).join(''),'验证状态：已提供逐折比较，完整集成同构回测与新区间校准仍有缺口');
  }
  if(kind==='panorama'&&series.length){
   if(i===1){
    const totals={};rows.filter(r=>r.Year===last.year).forEach(r=>totals[r.NOC]=(totals[r.NOC]||0)+r.records);
    const top=Object.entries(totals).sort((a,b)=>b[1]-a[1]).slice(0,5),max=top[0]?.[1]||1;
    return svg(top.map(([code,value],j)=>{let name=code;try{if(typeof displayNoc==='function')name=displayNoc(code)}catch(e){}const y=65+j*53,w=value/max*360;return `<text x="120" y="${y+5}" text-anchor="end">${name}</text><path class="sequence-grid" d="M140 ${y+16}H540"/><path class="sequence-series" stroke-width="12" d="M140 ${y}H${140+w}"/><text x="${150+w}" y="${y+5}">${fmt(value)}</text>`}).join('')+`<text x="140" y="340">${last.year} · 参赛记录前五代表团</text>`,`${last.year}参赛记录前五代表团，横条从零开始，直接标注记录数`);
   }
   const vals=series.map(d=>i===2?d.female/d.records*100:d.records),max=Math.max(...vals)*1.14||1;
   const x=j=>48+(series[j].year-series[0].year)/(last.year-series[0].year)*540,y=v=>286-v/max*205;
   const path=vals.map((v,j)=>(j?'L':'M')+x(j).toFixed(1)+','+y(v).toFixed(1)).join(' ');
   const ticks=[0,max/2,max].map(v=>`<path class="sequence-grid" d="M48 ${y(v)}H588"/><text x="48" y="${y(v)-9}">${i===2?v.toFixed(0)+'%':fmt(Math.round(v))}</text>`).join('');
   return svg(ticks+`<path class="sequence-series" d="${path}"/><circle class="sequence-dot" cx="${x(series.length-1)}" cy="${y(vals.at(-1))}" r="${i===1?9:5}"/><text x="48" y="326">${series[0].year}</text><text x="588" y="326" text-anchor="end">${last.year}</text>`,i===2?'逐届女性参赛记录占比':'逐届参赛记录趋势，年份按实际时间间隔排列');
  }
  if(kind==='stories')return svg(`<path class="sequence-grid" d="M90 190H550"/>`+['原判断','反例','修正'].map((t,j)=>`<circle class="${j===i?'sequence-dot':'sequence-node'}" cx="${90+j*230}" cy="190" r="${j===i?11:6}"/><text x="${90+j*230}" y="240" text-anchor="middle">${t}</text>`).join('')+`<text class="sequence-diagram-note" x="320" y="105" text-anchor="middle">${i===1?'反例让解释停下来，再向前走':'阅读路径示意 · 不编码数据大小'}</text>`, '原判断、反例和修正的阅读路径示意，不是数据曲线');
  return svg(['历史','假设','区间','验证'].map((t,j)=>`<circle class="${j<=i||i===2?'sequence-dot':'sequence-node'}" cx="${80+j*160}" cy="185" r="${j===i?10:6}"/><text x="${80+j*160}" y="230" text-anchor="middle">${t}</text>`).join('')+`<path class="sequence-grid" d="M90 185H550"/><text class="sequence-diagram-note" x="320" y="105" text-anchor="middle">预测流程示意 · 不编码预测数值</text>`, '预测从历史、假设、区间走向现实验证的流程示意');
 }
 function show(i){if(i===active)return;active=i;const s=data.steps[i];current.textContent=`${String(i+1).padStart(2,'0')} / ${String(steps.length).padStart(2,'0')} · ${sceneNames[i]}`;canvas.replaceChildren(el('span','sequence-metric-label',s[2]),el('strong','sequence-metric',s[3]),el('p','sequence-metric-note',s[4]));const art=el('div','sequence-diagram');art.innerHTML=diagram(i);canvas.append(art);root.dataset.frame=i;buttons.forEach((a,j)=>j===i?a.setAttribute('aria-current','step'):a.removeAttribute('aria-current'));steps.forEach((a,j)=>a.classList.toggle('is-active',j===i));if(!matchMedia('(prefers-reduced-motion: reduce)').matches){canvas.getAnimations().forEach(a=>a.cancel());canvas.animate([{opacity:.92,transform:'translateY(4px)'},{opacity:1,transform:'none'}],{duration:220,easing:'cubic-bezier(.2,.7,.2,1)'})}}
 // On narrow screens each passage owns its chart: no sticky panel obscures text.
 steps.forEach((article,i)=>{const chart=el('div','sequence-inline-chart');chart.innerHTML=diagram(i);article.querySelector('.sequence-inline').append(chart)});
 const onward=el('div','sequence-onward');onward.append(el('p','',({audit:'现在，检查这些处理决定能否逐条复现。',panorama:'把刚才的观察，放进自己的筛选条件。',stories:'带着这条反例，进入十个专题的不同问题。',future:'先读最新核验，再决定探索哪一种情景。'})[kind]));
 const go=el('a','sequence-evidence-link','继续探索完整证据 →');go.href=data.steps[0][5];onward.append(go);root.append(onward);
 let scheduled=false;
 function measure(){scheduled=false;const focus=innerHeight*.52;let i=0;steps.forEach((s,j)=>{if(s.getBoundingClientRect().top<focus)i=j});const box=root.getBoundingClientRect(),span=Math.max(1,box.height-innerHeight),progress=Math.max(0,Math.min(1,-box.top/span));root.style.setProperty('--scene-depth',String(progress));show(i)}
 function schedule(){if(!scheduled){scheduled=true;requestAnimationFrame(measure)}}
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);addEventListener('pageshow',schedule);show(0);
 // Mobile and reduced-motion readers can explicitly choose a frame without a long pinned sequence.
 controls.addEventListener('click',e=>{const a=e.target.closest('a');if(!a)return;const i=buttons.indexOf(a);if(i<0)return;e.preventDefault();history.replaceState(null,'',a.hash);show(i);steps[i].scrollIntoView({block:'center',behavior:matchMedia('(prefers-reduced-motion: reduce)').matches?'instant':'smooth'})});
 if(location.hash.startsWith('#sequence-'+kind+'-'))requestAnimationFrame(()=>document.getElementById(location.hash.slice(1))?.scrollIntoView({block:'center',behavior:'instant'}));
 // Keep the original aggregation and CSV, but give its main chart explicit units, axes and direct labels.
 if(kind==='panorama'){
  const chart=document.getElementById('chart');
  function drawReadable(){
   const current=window.current;if(!Array.isArray(current)||!chart)return;
   const field=document.getElementById('metric').value,year=document.getElementById('year').value,grouped={};
   current.forEach(r=>{const k=year?r.NOC:r.Year;grouped[k]=(grouped[k]||0)+r[field]});
   let points=Object.entries(grouped);points.sort(year?(a,b)=>b[1]-a[1]:(a,b)=>+a[0]-+b[0]);if(year)points=points.slice(0,15);
   if(!points.length){chart.innerHTML='<text x="60" y="100">当前组合没有记录，请调整筛选。</text>';return}
   const max=Math.max(...points.map(d=>d[1])),ceiling=Math.ceil(max/4)||1,top=ceiling*4,y=v=>325-v/top*255;
   const name=code=>{try{return displayNoc(code)}catch(e){return code}};
   let content=[0,1,2,3,4].map(i=>`<path class="sequence-grid" d="M75 ${y(ceiling*i)}H1065"/><text x="65" y="${y(ceiling*i)+4}" text-anchor="end">${fmt(ceiling*i)}</text>`).join('');
   content+=`<text x="75" y="35">${field==='medals'?'获奖运动员行':'参赛记录'} · ${year?'前15代表团':'按真实年份间距'}</text>`;
   if(year){const band=970/points.length,w=band*.6;content+=points.map(([code,v],i)=>{const x=85+i*band;return `<rect class="sequence-chart-bar" x="${x}" y="${y(v)}" width="${w}" height="${325-y(v)}"><title>${name(code)}：${fmt(v)}</title></rect><text x="${x+w/2}" y="${y(v)-8}" text-anchor="middle">${fmt(v)}</text><text x="${x+w/2}" y="348" transform="rotate(-35 ${x+w/2} 348)" text-anchor="end">${name(code)}</text>`}).join('')}
   else{const first=+points[0][0],span=+points.at(-1)[0]-first||1,x=year=>75+(year-first)/span*990;content+=`<path class="sequence-series" d="${points.map(([year,v],i)=>(i?'L':'M')+x(+year)+','+y(v)).join(' ')}"/>`;content+=points.map(([year,v],i)=>`<circle class="sequence-dot" cx="${x(+year)}" cy="${y(v)}" r="4"><title>${year}：${fmt(v)}</title></circle>`).join('');const tick=points.filter((_,i)=>i===0||i===points.length-1||i%5===0);content+=tick.map(([year])=>`<text x="${x(+year)}" y="352" text-anchor="middle">${year}</text>`).join('')}
   chart.classList.add('sequence-readable-chart');chart.innerHTML=content;
  }
  document.addEventListener('change',e=>{if(e.target.matches('.filters select'))drawReadable()});drawReadable();
 }
})();
