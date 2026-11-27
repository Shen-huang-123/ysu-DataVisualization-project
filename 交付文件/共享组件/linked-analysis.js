(() => {
  const panel = document.querySelector('[data-analysis]');
  const {names, rows} = window.linkedAnalysisData;
  const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const name = code => names[code] || code;
  const get = id => panel.querySelector('#la-' + id);
  const options = values => values.map(value => '<option>' + esc(value) + '</option>').join('');
  const number = value => Number(value).toFixed(2);
  const table = (head, body) => '<div class="la-scroll"><table><thead><tr>' + head.map(x => '<th scope="col">'+x+'</th>').join('') +
    '</tr></thead><tbody>' + body.map(row => '<tr>'+row.map(x => '<td>'+x+'</td>').join('')+'</tr>').join('')+'</tbody></table></div>';
  const source = (url, text) => /^https:\/\//.test(url) ? '<a href="'+esc(url)+'">'+text+'</a>' : '';

  function interval() {
    panel.innerHTML = `<h2>按届次找出区间未覆盖的代表团</h2>
      <p>历史加权基线 · 历史留出样本。圆点为点预测，菱形为实际值。筛选以所选方法为准，每队同时显示两种方法。2028 主榜只发布点估计。</p>
      <div class="la-controls"><label>评估届次 <select id="la-year">${options([2016,2020,2024])}</select></label>
      <label>校准届次 <select id="la-calibration"></select></label>
      <label>样本 <select id="la-sample">${options(['全体','预测至少5槽'])}</select></label>
      <label>筛选依据 <select id="la-method">${options(['统一半宽','按预测量分组'])}</select></label>
      <label>实际值位置 <select id="la-side">${options(['全部','未覆盖','高于上限','低于下限','区间内'])}</select></label></div>
      <p id="la-summary" role="status"></p><div id="la-output"></div><p><a href="逐队区间与覆盖.csv">下载全量核验数据</a></p>`;
    const side = ([,,, , , actual, low, high]) => actual < low ? '低于下限' : actual > high ? '高于上限' : '区间内';
    const width = ([,,,,,,low,high]) => high-low;
    const calibrations = () => {
      get('calibration').innerHTML = options([...new Set(rows.filter(row => row[0] === +get('year').value).map(row => row[1]))]);
    };
    function draw() {
      const cohort = rows.filter(row => row[0] === +get('year').value && row[1] === get('calibration').value &&
        (get('sample').value === '全体' || row[4] >= 5));
      const pairs = new Map();
      for (const row of cohort) {
        if (!pairs.has(row[3])) pairs.set(row[3], []);
        pairs.get(row[3])[Number(row[2] !== '统一半宽')] = row;
      }
      const teams = [...pairs.values()].sort((a,b) => b[0][4] - a[0][4]);
      const method = get('method').selectedIndex;
      const filter = get('side').value;
      const shown = teams.filter(pair => filter === '全部' || (filter === '未覆盖' ? side(pair[method]) !== '区间内' : side(pair[method]) === filter));
      const improved = teams.filter(pair => side(pair[0]) !== '区间内' && side(pair[1]) === '区间内').length;
      const lost = teams.filter(pair => side(pair[0]) === '区间内' && side(pair[1]) !== '区间内').length;
      const average = index => number(teams.reduce((sum, pair) => sum + width(pair[index]), 0) / teams.length);
      const high = teams.filter(pair => side(pair[method]) === '高于上限').length;
      const low = teams.filter(pair => side(pair[method]) === '低于下限').length;
      get('summary').textContent = `共 ${teams.length} 队，显示 ${shown.length} 队。当前方法高于上限 ${high} 队，低于下限 ${low} 队。分组后新增覆盖 ${improved} 队，失去覆盖 ${lost} 队，平均宽度 ${average(0)} → ${average(1)} 槽。`;
      const max = Math.ceil(Math.max(1, ...cohort.flatMap(row => [row[5],row[7]])) / 10) * 10;
      const pos = value => value / max * 100 + '%';
      function cell(row) {
        const [,,methodName,,prediction,actual,low,high] = row;
        const state = side(row);
        const distance = Math.max(low-actual,actual-high,0);
        return `<div class="la-interval" aria-hidden="true" style="--low:${pos(low)};--span:${pos(high-low)};--prediction:${pos(prediction)};--actual:${pos(actual)}"><i></i><b></b><em></em></div>
          <strong>${esc(methodName)} · ${state}${distance ? ' '+number(distance)+' 槽' : ''}</strong>
          <div>预测 ${number(prediction)} · 实际 ${number(actual)} · 区间 ${number(low)}–${number(high)} 槽</div>`;
      }
      get('output').innerHTML = '<p>共同横轴：0–'+max+' 槽</p>' + (shown.length ?
        '<div class="la-rows">'+shown.map(pair => '<section><h3>'+esc(name(pair[0][3]))+
          '</h3><div class="la-pair">'+pair.map(row => '<div>'+cell(row)+'</div>').join('')+'</div></section>').join('')+'</div>' :
        '<p>当前筛选没有匹配的代表团。</p>');
    }
    get('year').value = '2024';
    get('sample').selectedIndex = 1;
    calibrations();
    panel.addEventListener('change', event => {
      if (event.target === get('year')) calibrations();
      draw();
    });
    for (const link of document.querySelectorAll('.coverage-point-row a')) {
      link.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        const row = link.closest('.coverage-point-row');
        get('year').value = row.firstElementChild.textContent.trim();
        get('sample').value = row.closest('section').querySelector('h3').textContent.trim();
        get('method').selectedIndex = 0;
        get('side').selectedIndex = 0;
        calibrations();
        draw();
        panel.scrollIntoView();
        get('year').focus({preventScroll:true});
      });
    }
    draw();
  }

  function history() {
    const codes = [...new Set(rows.map(row => row[1]))].sort();
    const years = [...new Set(rows.map(row => row[2]))].sort((a,b) => a-b);
    panel.innerHTML = `<h2>代表团两届之间的获奖变化来自哪里？</h2>
      <p>按夏奥届次统计纳入主分析的运动员获奖行。团队项目每名获奖运动员计一行，零表示该口径下无获奖记录。小项名称保留源表标签。</p>
      <div class="la-controls"><label>代表团 <select id="la-team">${codes.map(code => '<option value="'+esc(code)+'">'+esc(name(code)+' · '+code)+'</option>').join('')}</select></label>
      <label>起始届次 <select id="la-from">${options(years)}</select></label><label>结束届次 <select id="la-to">${options(years)}</select></label></div>
      <h3>逐届获奖行</h3><p>点两个届次设为比较起止。</p><div class="la-trend" id="la-trend"></div>
      <h3>两届运动构成</h3><p id="la-summary" role="status"></p><div id="la-sports"></div>
      <h3>获奖明细</h3><p id="la-detail-label" role="status"></p><div id="la-output"></div><p><a href="../../任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz">下载带原始字段的数据</a></p>`;
    get('team').value = 'CHN';
    get('from').value = '2016';
    get('to').value = '2024';
    let sport = '';
    let pending = null;
    function draw() {
      const [from,to] = [+get('from').value,+get('to').value].sort((a,b) => a-b);
      const selected = rows.filter(row => row[1] === get('team').value && row[2] >= from && row[2] <= to);
      const totals = new Map();
      const sports = new Map();
      for (const row of selected) {
        const year = row[2];
        totals.set(year,(totals.get(year) || 0) + 1);
        if (year !== from && year !== to) continue;
        if (!sports.has(row[3])) sports.set(row[3],[0,0]);
        if (year === from) sports.get(row[3])[0]++;
        if (year === to) sports.get(row[3])[1]++;
      }
      const peak = Math.max(1,...totals.values());
      get('trend').innerHTML = years.filter(year => year >= from && year <= to).map(year => {
        const count = totals.get(year) || 0;
        return `<button type="button" data-year="${year}" aria-pressed="${year === pending}"><span style="--height:${count / peak * 100}%"><i></i></span><strong>${count}</strong>${year}</button>`;
      }).join('');
      get('summary').textContent = `${name(get('team').value)} · ${from} 年 ${totals.get(from) || 0} 行 → ${to} 年 ${totals.get(to) || 0} 行。` +
        (pending === null ? '' : ' 已选 '+pending+' 年，请选择另一届。');
      const ranked = [...sports].sort((a,b) => Math.abs(b[1][1]-b[1][0])-Math.abs(a[1][1]-a[1][0]));
      get('sports').innerHTML = ranked.length ? table(['运动',String(from),String(to),'变化'], ranked.map(([family,[a,b]]) =>
        [`<button type="button" data-sport="${esc(family)}" aria-pressed="${sport === family}">${esc(family)}</button>`,a,b,b-a])) : '<p>两届均无获奖行。</p>';
      const records = selected.filter(row => (row[2] === from || row[2] === to) && (!sport || row[3] === sport));
      get('detail-label').textContent = (sport || '全部运动') + ' · ' + records.length + ' 行。';
      get('output').innerHTML = records.length ? table(['源行','届次','运动','原始小项','奖牌','运动员'],
        records.map(([id,,year,family,event,medal,athlete]) => [id,year,family,event,({Gold:'金',Silver:'银',Bronze:'铜'})[medal] || medal,athlete].map(esc))) : '<p>当前范围没有明细。</p>';
    }
    panel.addEventListener('change', () => {sport='';pending=null;draw();});
    panel.addEventListener('click', ({target}) => {
      const button = target.closest('button');
      if (!button) return;
      if (button.dataset.sport) {
        sport = sport === button.dataset.sport ? '' : button.dataset.sport;
        draw();
        [...panel.querySelectorAll('[data-sport]')].find(item => item.dataset.sport === button.dataset.sport)?.focus();
      }
      if (button.dataset.year) {
        const year = +button.dataset.year;
        if (pending === null) pending = year;
        else {
          get('from').value = Math.min(pending,year);
          get('to').value = Math.max(pending,year);
          sport='';pending=null;
        }
        draw();
        panel.querySelector('[data-year="'+year+'"]')?.focus();
      }
    });
    draw();
  }

  function replay() {
    panel.innerHTML = `<h2>选几条更正，看看奖牌榜怎样重排</h2>
      <p>同一届的勾选项合并复算。基于 302 项历史小项代理表，按金、银、铜排序，相同奖牌组合并列。证据仅覆盖各条记录标明的范围。</p>
      <div class="la-controls"><label>届次 <select id="la-year">${options(Object.keys(rows))}</select></label>
      <button type="button" id="la-all">应用该届全部更正</button><button type="button" id="la-none">恢复旧存档</button></div>
      <fieldset><legend>选择有证据支持的更正</legend><div id="la-cases"></div></fieldset>
      <p id="la-summary" role="status"></p><div id="la-output"></div>
      <p><a href="优先分歧逐项复核.csv">下载逐项证据</a> · <a href="优先分歧名次复算.csv">下载原复算表</a></p>`;
    function cases() {
      const [items] = rows[get('year').value];
      get('cases').innerHTML = items.map((item,i) => `<section><label><input type="checkbox" value="${i}"> <strong>${esc(item.案例)}</strong> · ${esc(item.原金银铜)} → ${esc(item.核对金银铜)}</label>
        <p>${esc(item.证据范围)}。 ${source(item.来源,'来源')} ${source(item.补充来源,'补充来源')}</p></section>`).join('');
      draw();
    }
    function draw() {
      const [,masks] = rows[get('year').value];
      const checked = [...get('cases').querySelectorAll(':checked')];
      const mask = checked.reduce((sum,input) => sum | (1 << +input.value),0);
      const changed = masks[mask];
      const moved = changed.filter(([,old,,next]) => old !== next).length;
      get('summary').textContent = `已应用 ${checked.length} 条更正 · ${moved} 队名次变化 · ${changed.length-moved} 队奖牌数变化但名次不变。`;
      get('output').innerHTML = changed.length ? table(['代表团','原金／银／铜','复算金／银／铜','旧名次 → 复算'],
        changed.map(([code,old,before,next,after]) => [esc(name(code)),before.join('/'),after.join('/'),(old ?? '未上榜')+' → '+(next ?? '未上榜')])) : '<p>与旧存档基准一致。</p>';
    }
    get('year').addEventListener('change',cases);
    get('cases').addEventListener('change',draw);
    for (const id of ['all','none']) get(id).addEventListener('click',() => {
      for (const input of get('cases').querySelectorAll('input')) input.checked = id === 'all';
      draw();
    });
    cases();
  }

  ({interval, history, replay})[panel.dataset.analysis]();
})();
