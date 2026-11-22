/* Published from audited inputs; no network requests or model fitting. */
(()=>{'use strict';
const $=id=>document.getElementById(id), data=$('evidence-feedback-data');if(!data)return;
const D=JSON.parse(data.textContent), query=new URLSearchParams(location.search);
document.querySelectorAll('.evidence-feedback').forEach(el=>el.hidden=false);
const signed=(v,n=2)=>(v>0?'+':v<0?'−':'')+Math.abs(v).toFixed(n);
function state(values){const url=new URL(location.href);Object.entries(values).forEach(([k,v])=>url.searchParams.set(k,v));try{history.replaceState(null,'',url)}catch(_){}}
const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
if(D.kind==='rank'){
 const cases=Object.fromEntries(JSON.parse($('lab-data').textContent).cases.map(x=>[x.noc,x]));
 function render(){const c=cases[$('case-select').value];if(!c)return;const lens=document.querySelector('[data-lens][aria-pressed="true"]').dataset.lens, rank=c[lens].rank, delta=c.official.rank-rank;
 const name={official:'官方小项',fractional:'团队内均分',rows:'运动员行'}[lens];
 $('rank-result').textContent=`${c.name}：第 ${c.official.rank} 名 → 第 ${rank} 名`;
 $('rank-direction').textContent=delta>0?`相对官方小项，上升 ${delta} 位。`:delta<0?`相对官方小项，后移 ${-delta} 位。`:'与官方小项名次相同。';
 $('rank-unit').textContent=`当前：${name}。${c.official.Gold} 个金牌小项，对应 ${c.rows.Gold} 条获金运动员记录；组内均分金牌份额为 ${Number(c.fractional.Gold.toFixed(2))}。`;
 $('rank-meaning').textContent=lens==='rows'?'变化来自计数单位与团体项目结构，不能把获金行数叫作官方金牌数，也不代表实力突然改变。':lens==='fractional'?'每个 NOC–Event–Medal 获奖组总权重为1；其分组不保证与官方小项逐一对应。':'这是小项计数的参照端点。切到运动员行，查看同一结果如何改变排名。';
 state({'ef-lens':lens,'ef-noc':c.noc});
 }
 const focus=query.get('ef-noc'),lens=query.get('ef-lens');if(Object.hasOwn(cases,focus)&&$('case-select').value!==focus){$('case-select').value=focus;$('case-select').dispatchEvent(new Event('change'))}if(['official','fractional','rows'].includes(lens)){
 const button=document.querySelector(`[data-lens="${lens}"]`);
 if(button.getAttribute('aria-pressed')!=='true')button.click();
 }
 // Observe existing chart/select interactions rather than maintaining a second ranking state.
 new MutationObserver(render).observe($('case-shift'),{childList:true});render();
}
if(D.kind==='interval'){
 const select=$('interval-choice');if(D.rows[+query.get('ef-cohort')])select.value=+query.get('ef-cohort');
 function render(){const i=+select.value,r=D.rows[i],cross=r.low<=0&&r.high>=0;
 $('interval-result').textContent=cross?'区间跨零：下降方向尚不确定':'区间未跨零：本情景支持下降';
 $('interval-reading').textContent=`${r.n} 个小项，${r.transitions} 次转移；前后差 ${signed(r.delta)} 个百分点，成组95%区间 [${signed(r.low)}, ${signed(r.high)}]。`;
 $('interval-boundary').textContent=i===2?'排除后样本由113项缩至50项；这是样本选择检验，不能说来源替换推翻了同113项的结果，也不能把这50项称作官方认证样本。':'同113项的原代理与二次来源替换结果相同。二次来源仍不等于现行IOC逐项认证；继续切换排除方案检验样本选择的影响。';
 const x=v=>70+(v+20)/25*520,z=x(0);let svg=`<svg viewBox="0 0 660 180" role="img" aria-label="${esc($('interval-reading').textContent)}"><line x1="${z}" x2="${z}" y1="20" y2="116" stroke="currentColor" stroke-dasharray="4 4"/><text x="${z-8}" y="16" text-anchor="end">零：没有前后变化</text>`;
 [-20,-15,-10,-5,0,5].forEach(v=>svg+=`<line x1="${x(v)}" x2="${x(v)}" y1="112" y2="118" stroke="currentColor"/><text x="${x(v)}" y="140" text-anchor="middle">${v}</text>`);
 svg+=`<line x1="70" x2="590" y1="112" y2="112" stroke="currentColor"/><line x1="${x(r.low)}" x2="${x(r.high)}" y1="70" y2="70" stroke="currentColor" stroke-width="5"/><line x1="${x(r.low)}" x2="${x(r.low)}" y1="59" y2="81" stroke="currentColor"/><line x1="${x(r.high)}" x2="${x(r.high)}" y1="59" y2="81" stroke="currentColor"/><circle cx="${x(r.delta)}" cy="70" r="7" fill="currentColor"/><text x="330" y="172" text-anchor="middle">后段 − 早段（百分点）</text></svg>`;
 $('interval-chart').innerHTML=svg;state({'ef-cohort':i});
 }select.addEventListener('change',render);render();
}
if(D.kind==='model'){
 const source=$('model-source'),model=$('model-choice');let year='2024';
 if(D.sources.includes(query.get('ef-source')))source.value=query.get('ef-source');if(D.models.includes(query.get('ef-model')))model.value=query.get('ef-model');if(D.years.includes(query.get('ef-year')))year=query.get('ef-year');
 function render(){const rows=D.rows.filter(x=>x.source===source.value&&x.model===model.value),r=rows.find(x=>x.year===year),delta=r.mae-r.baseline;
 $('model-result').textContent=`${year}：${delta>0?'误差更大，未胜出':delta<0?'误差更小，本届胜出':'与基准持平'}`;
 $('model-reading').textContent=`${source.value} · ${model.options[model.selectedIndex].text}：MAE ${r.mae.toFixed(3)}；同口径基准 ${r.baseline.toFixed(3)}；差 ${signed(delta,3)} ${source.value==='运动员行原口径'?'行':'奖牌槽'}/代表团。MAE越低越好。`;
 const fails=rows.filter(x=>x.mae>x.baseline).map(x=>x.year);$('model-fails').textContent=fails.length?`当前模型未胜过基准的届次：${fails.join('、')}。点击下方届次查看读数。`:'当前三折均低于基准；这不构成跨口径稳定优势，也不能据此认定45%权重最优。';
 document.querySelectorAll('[data-feedback-year]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.feedbackYear===year)));
 const extent=Math.max(.01,...D.rows.filter(x=>x.source===source.value).map(x=>Math.abs(x.mae-x.baseline)))*1.15,scale=v=>330+v/extent*210;
 let svg='<svg viewBox="0 0 660 190" role="img" aria-label="逐届MAE与基准之差：左侧更小，右侧更大"><line x1="330" x2="330" y1="35" y2="183" stroke="currentColor" stroke-dasharray="4 4"/><text x="320" y="23" text-anchor="end">更小 ←</text><text x="340" y="23">→ 更大</text>';
 rows.forEach((v,i)=>{const d=v.mae-v.baseline,y=65+i*48,end=scale(d);svg+=`<text x="30" y="${y+5}" font-weight="${v.year===year?700:400}">${v.year}${v.year===year?' ◀':''}</text><line x1="${Math.min(330,end)}" x2="${Math.max(330,end)}" y1="${y}" y2="${y}" stroke="currentColor" stroke-width="${v.year===year?8:3}" opacity="${v.year===year?1:.5}"/><circle cx="${end}" cy="${y}" r="4" fill="currentColor"/><text x="640" y="${y+5}" text-anchor="end">${signed(d,3)}</text>`});
 svg+=`</svg>`;$('model-chart').innerHTML=svg;state({'ef-source':source.value,'ef-model':model.value,'ef-year':year});
 }source.addEventListener('change',render);model.addEventListener('change',render);document.querySelectorAll('[data-feedback-year]').forEach(b=>b.addEventListener('click',()=>{year=b.dataset.feedbackYear;render()}));render();
}
})();
