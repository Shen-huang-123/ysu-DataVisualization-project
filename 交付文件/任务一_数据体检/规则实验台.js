(() => {
  const root = document.querySelector('#audit-lab');
  const {main, dedup, inclusive, excess, medals1906, events, official, names, sports, eventLabels} = window.auditLabData;
  const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const select = (id, values) => '<select id="'+id+'">'+values.map(v=>'<option>'+esc(v)+'</option>').join('')+'</select>';
  const original = (label, raw) => label && label !== raw
    ? '<details><summary>'+esc(label)+'</summary><small>'+esc(raw)+'</small></details>'
    : esc(raw);
  const table = (heads, rows) => '<div class="audit-scroll" role="region" aria-label="核验明细表" tabindex="0"><table><thead><tr>'+heads.map(h=>'<th scope="col">'+esc(h)+'</th>').join('')+
    '</tr></thead><tbody>'+rows.map(row=>'<tr>'+row.map(v=>'<td>'+(Array.isArray(v)?original(...v):esc(v))+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
  const get = id => document.getElementById(id);
  root.innerHTML = `<h2>数据规则实验台</h2>
  <p>切换一条规则，对照任务二的逐届图表，并追查源记录。</p>
  <div class="audit-controls"><label>规则 ${select('audit-mode',['重复候选','1906 届','小项标签泛化'])}</label>
  <label id="audit-setting">方案 <select id="audit-choice"></select></label>
  <label id="audit-year-label">查看届次 <select id="audit-year"></select></label></div>
  <p id="audit-summary" role="status"></p><div id="audit-chart"></div><div id="audit-rows"></div>
  <p><a href="04_质量检查结果/edition_main.csv">主方案 CSV</a> · <a href="04_质量检查结果/edition_exclude_duplicate_excess.csv">扣除重复余量 CSV</a> ·
  <a href="04_质量检查结果/edition_include_1906.csv">纳入 1906 CSV</a> · <a href="04_质量检查结果/event_quality_by_year.csv">小项标签检查 CSV</a></p>`;
  function fill(id, values) {
    get(id).innerHTML=values.map(v=>'<option>'+esc(v)+'</option>').join('');
  }
  const yearMap = rows => new Map(rows);
  const baseline = yearMap(main), reduced = yearMap(dedup), extended = yearMap(inclusive);
  const peakYear = main.reduce((best,[year,n]) => n-reduced.get(year)>baseline.get(best)-reduced.get(best)?year:best,main[0][0]);
  const award = value => ({Gold:'金',Silver:'银',Bronze:'铜'})[value] || value;
  function plot(rows, year, mode) {
    const max = Math.ceil(Math.max(...main.map(row=>row[1]))/500)*500;
    const width = Math.max(250, get('audit-chart').clientWidth);
    const right = width - 20;
    const height = width >= 850 ? 300 : 230;
    const bottom = height - 33;
    const x = year => 48 + (year-1896)/128*(right-48);
    const y = value => bottom-value/max*(bottom-24);
    const points = data => data.map(([yr,n])=>x(yr)+','+y(n)).join(' ');
    const selected=rows.find(row=>row[0]===year);
    const guides=[0,max/2,max].map(n=>`<line x1="48" x2="${right}" y1="${y(n)}" y2="${y(n)}"/><text x="39" y="${y(n)+4}" text-anchor="end">${n}</text>`).join('');
    get('audit-chart').innerHTML=`<svg viewBox="0 0 ${width} ${height}" role="img" aria-label="逐届运动员获奖记录数，灰线为主方案，青线为当前方案">
    <g class="audit-grid">${guides}</g>
    <polyline class="audit-base" points="${points(main)}"/><polyline class="audit-current" points="${points(rows)}"/>
    ${selected?`<line class="audit-selection" x1="${x(year)}" x2="${x(year)}" y1="24" y2="${bottom}"/>
    <circle cx="${x(year)}" cy="${y(selected[1])}" r="5"/>
    <text class="audit-value" x="${x(year)+(year>1990?-9:9)}" y="${Math.max(17,y(selected[1])-11)}" text-anchor="${year>1990?'end':'start'}">${year} · ${selected[1].toLocaleString('zh-CN')} 条</text>`:''}
    <text x="48" y="${height-10}">1896</text><text x="${right}" y="${height-10}" text-anchor="end">2024</text></svg>
    <div class="audit-chart-footer"><p>任务二 A1 · 灰线为主方案，青线为当前方案，金点为所选届次。</p><div id="audit-markers" aria-label="届次快捷选择"></div></div>`;
    const shortcuts=mode===0?[peakYear,1900,2024]:[1906];
    get('audit-markers').innerHTML=[...new Set(shortcuts)].map(yr=>` <button type="button" data-year="${yr}" aria-pressed="${yr===year && (mode===0 || selected!=null)}">${yr===peakYear&&mode===0?'最大减量 · ':''}${yr} 年</button>`).join('');
  }
  function render() {
    const mode=get('audit-mode').selectedIndex, alternate=get('audit-choice').selectedIndex===1;
    const yr=Number(get('audit-year').value);
    const summary=get('audit-summary'), rows=get('audit-rows');
    if(mode===0){
      plot(alternate?dedup:main,yr,mode);
      const diff=baseline.get(yr)-reduced.get(yr);
      summary.textContent=`${yr} 年当前 ${alternate?reduced.get(yr):baseline.get(yr)} 条获奖行；扣除候选余量后 ${baseline.get(yr)} → ${reduced.get(yr)}，减少 ${diff} 条。1900 至 2024 两端仍呈增长。`;
      rows.innerHTML='<h3>被标记的获奖行</h3><p>每组保留首行，其余行作为敏感性情景扣除；这些记录仍是候选。</p>'+
        (diff?table(['扣除源行','保留源行','代表团','小项（可展开原文）','奖牌'],(excess[yr]||[]).map(([id,keep,noc,event,medal])=>[id,keep,[names[noc],noc],[eventLabels[event],event],award(medal)])):'<p>该届没有被扣除的获奖行。</p>');
    } else if(mode===1){
      plot(alternate?inclusive:main,1906,mode);
      summary.textContent=`当前${alternate?'纳入':'排除'} 1906 届。纳入后多一个观测点，增加 ${extended.get(1906)} 条获奖行；1896 和 2024 的数值不变。`;
      rows.innerHTML=`<h3>1906 年获奖源行</h3><p>共${new Set(medals1906.map(row=>row[1])).size} 个有获奖记录的代表团。点击代表团或小项可展开源表值。</p>`+
        table(['源行','代表团','小项（可展开原文）','奖牌'],medals1906.map(([id,noc,event,medal])=>[id,[names[noc],noc],[eventLabels[event],event],award(medal)]));
    } else {
      const {count, examples}=events[yr];
      get('audit-chart').innerHTML=table(['受影响图表','该届展示'],[
        ['按运动大类的分析','可以使用归一后的运动大类'],
        ['任务二 D1 · 逐届小项数量',yr===2020?'留空：缺少可靠的小项口径':official+' 项：来自巴黎官方小项表']]);
      summary.textContent=`${yr} 年有 ${count.toLocaleString('zh-CN')} 行小项标签需要上下文辨别。运动大类和性别可以缩小范围；泛化标签本身不足以识别具体小项。`;
      rows.innerHTML='<h3>源表标签样例</h3>'+table(['源行','运动','小项标签','性别','归一运动大类'],examples.map(([id,sport,event,sex,family])=>[id,[sports[sport],sport],[eventLabels[event],event],({M:'男',F:'女'})[sex]||sex,sports[family]||family]));
    }
  }
  function reset() {
    const mode=get('audit-mode').selectedIndex;
    get('audit-setting').hidden=mode===2;
    get('audit-year-label').hidden=mode===1;
    fill('audit-choice',mode===0?['保留重复候选','扣除重复候选余量']:['排除 1906','纳入 1906']);
    fill('audit-year',mode===0?main.map(row=>row[0]):[2020,2024]);
    if(mode===0)get('audit-year').value=String(peakYear);
    render();
  }
  root.addEventListener('change',event=>event.target.id==='audit-mode'?reset():render());
  root.addEventListener('click',event=>{
    const year=event.target.closest('[data-year]')?.dataset.year;
    if(!year)return;
    if(get('audit-mode').selectedIndex===1)get('audit-choice').selectedIndex=1;
    else get('audit-year').value=year;
    render();
    root.querySelector('[data-year="'+year+'"]')?.focus();
  });
  reset();
  let chartWidth = get('audit-chart').clientWidth;
  new ResizeObserver(([entry]) => {
    const width = Math.round(entry.contentRect.width);
    if (width === chartWidth) return;
    chartWidth = width;
    const mode = get('audit-mode').selectedIndex;
    const alternate = get('audit-choice').selectedIndex === 1;
    if (mode === 0) plot(alternate ? dedup : main, Number(get('audit-year').value), mode);
    if (mode === 1) plot(alternate ? inclusive : main, 1906, mode);
  }).observe(get('audit-chart'));
})();
