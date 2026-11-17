/* Short evidence-led overtures. Read existing local data; never change analytical filters on scroll. */
(()=>{
 const kind=document.body.dataset.narrative,main=document.querySelector('main');
 if(!kind||!main)return;
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
 stories:{title:'一个好故事，要容得下反例。',unit:'专题深挖 · 原判断、复核、修正',source:'来源：本页十专题深度核验。描述性差异不能自动升级为因果解释。',steps:[
 ['直觉：主场总能带来收益。','如果只挑上升的代表团，主场效应似乎理所当然。先把不符合预期的案例留在画面里。','原判断','主场 → 收益','这是待检验的判断，不是已经识别的因果效应','#explore-stories-2'],
 ['反例：巴西2016没有沿直觉前进。','已纳入的9例中，8例奖牌份额上升；巴西2016却下降0.57个百分点。这个反例要求我们追问比较基准与其他变化。','巴西 · 2016','−0.57','奖牌份额变化 · 百分点','#explore-stories-4'],
 ['修正：看到差异，仍需克制解释。','趋势、项目结构、投资与主办权选择可能同时变化。保留描述性发现，让对照方法、案例规则和证据边界决定解释能走多远。','修正判断','描述 ≠ 因果','在下方展开十个专题的反例与边界','#explore-stories-4']
 ]},
 future:{title:'未来的答案，取决于怎样提问。',unit:'洛杉矶2028 · 预测阅读路径',source:'流程示意，不编码预测数值；实际点估计、区间、回测与来源日期见对应实验室。',steps:[
 ['先把历史放在桌上。','预测从既有参赛与获奖记录出发。先理解历史趋势与口径，再决定哪些经验可以带到2028。','历史基线','已发生','过去的观察，不是未来的保证','#explore-future-1'],
 ['再让假设接受拨动。','主场效应、新增运动与资格条件是不同的假设。去实验室改变条件，同时查看结果如何响应，而不是只读一个名次。','条件与情景','如果……','假设可调整，结论有条件','#explore-future-2'],
 ['最后，把判断交还现实。','把点估计与区间一起读；把评价规则提前确定。等真实结果到来，用同一套规则计算误差，允许预测被证伪。','结果检验','等待验证','不确定性与误差应当留在画面里','#explore-future-4']
 ]}
 };
 const data=stories[kind];if(!data)return;
 const root=el('section','story-sequence sequence-'+kind);root.setAttribute('aria-label',data.title);
 const head=el('div','sequence-heading');head.append(el('span','sequence-eyebrow','从这里读起'),el('h2','',data.title));
 const body=el('div','sequence-body'),visual=el('figure','sequence-visual'),canvas=el('div','sequence-canvas');
 const caption=el('figcaption','sequence-source',data.source);visual.append(el('small','sequence-unit',data.unit),canvas,caption);
 const text=el('div','sequence-text');
 const steps=data.steps.map((s,i)=>{
  const article=el('article','sequence-step');article.id='sequence-'+kind+'-'+i;
  article.append(el('small','sequence-index',String(i+1).padStart(2,'0')),el('h3','',s[0]),el('p','',s[1]));
  const inline=el('div','sequence-inline');inline.append(el('small','',s[2]),el('strong','',s[3]),el('span','',s[4]));article.append(inline);
  const a=el('a','sequence-evidence-link','查看对应证据 ↗');a.href=s[5];article.append(a);text.append(article);return article;
 });
 const controls=el('nav','sequence-controls');controls.setAttribute('aria-label','选择故事画面');
 const buttons=steps.map((s,i)=>{const a=el('a','',String(i+1).padStart(2,'0'));a.href='#'+s.id;a.setAttribute('aria-label',data.steps[i][0]);controls.append(a);return a});
 visual.append(controls);body.append(visual,text);root.append(head,body);
 main.querySelector('.narrative-cinema')?.remove();
 (main.querySelector('.narrative-opening')||main.firstElementChild).after(root);
 let active=-1;
 const svg=(content,label)=>`<svg viewBox="0 0 640 350" role="img" aria-label="${label}">${content}</svg>`;
 function diagram(i){
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
  if(kind==='audit'){
   const labels=i===0?['原始字段','没有空值','语义仍需核对']:i===1?['上下文依赖','降低分析粒度','保留原始标签']:['官方小项','统计单位改变','运动员行'];
   return svg(`<path class="sequence-grid" d="M70 190H570"/>`+labels.map((t,j)=>`<circle class="${j===i?'sequence-dot':'sequence-node'}" cx="${90+j*230}" cy="190" r="${j===i?11:6}"/><text x="${90+j*230}" y="232" text-anchor="middle">${t}</text>`).join('')+`<text class="sequence-diagram-note" x="320" y="112" text-anchor="middle">${i===2?'同一队伍，两种名次':'每一步都要留下处理依据'}</text>`,labels.join('，'));
  }
  if(kind==='stories')return svg(`<path class="sequence-grid" d="M90 190H550"/>`+['原判断','反例','修正'].map((t,j)=>`<circle class="${j===i?'sequence-dot':'sequence-node'}" cx="${90+j*230}" cy="190" r="${j===i?11:6}"/><text x="${90+j*230}" y="240" text-anchor="middle">${t}</text>`).join('')+`<text class="sequence-diagram-note" x="320" y="105" text-anchor="middle">${i===1?'反例让解释停下来，再向前走':'阅读路径示意 · 不编码数据大小'}</text>`, '原判断、反例和修正的阅读路径示意，不是数据曲线');
  return svg(['历史','假设','区间','验证'].map((t,j)=>`<circle class="${j<=i||i===2?'sequence-dot':'sequence-node'}" cx="${80+j*160}" cy="185" r="${j===i?10:6}"/><text x="${80+j*160}" y="230" text-anchor="middle">${t}</text>`).join('')+`<path class="sequence-grid" d="M90 185H550"/><text class="sequence-diagram-note" x="320" y="105" text-anchor="middle">预测流程示意 · 不编码预测数值</text>`, '预测从历史、假设、区间走向现实验证的流程示意');
 }
 function show(i){if(i===active)return;active=i;const s=data.steps[i];canvas.replaceChildren(el('span','sequence-metric-label',s[2]),el('strong','sequence-metric',s[3]),el('p','sequence-metric-note',s[4]));const art=el('div','sequence-diagram');art.innerHTML=diagram(i);canvas.append(art);root.dataset.frame=i;buttons.forEach((a,j)=>j===i?a.setAttribute('aria-current','step'):a.removeAttribute('aria-current'));steps.forEach((a,j)=>a.classList.toggle('is-active',j===i));if(!matchMedia('(prefers-reduced-motion: reduce)').matches){canvas.getAnimations().forEach(a=>a.cancel());canvas.animate([{opacity:.82,transform:'translateY(4px)'},{opacity:1,transform:'none'}],{duration:360,easing:'cubic-bezier(.2,.7,.2,1)'})}}
 let scheduled=false;
 function measure(){scheduled=false;const focus=innerHeight*.52;let i=0;steps.forEach((s,j)=>{if(s.getBoundingClientRect().top<focus)i=j});show(i)}
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
