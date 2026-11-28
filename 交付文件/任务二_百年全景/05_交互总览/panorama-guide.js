(() => {
  const get = id => document.getElementById(id);
  const [metrics] = JSON.parse(get('panorama-lead-data').textContent);
  const years = Object.keys(metrics).map(Number);
  const names = ['获奖代表团数', '前五份额（%）', '有效获奖代表团数'];
  const colors = ['#438c9a', '#b18948', '#9a6585'];
  const charts = [];
  const chart = id => {
    const instance = echarts.init(get(id), null, {renderer: 'svg'});
    charts.push(instance);
    return instance;
  };
  const ink = () => getComputedStyle(get('panorama-lead')).color;
  const option = (label, values, color, selected, markers = []) => ({
    animation: false,
    grid: {left: 48, right: 17, top: 22, bottom: 30},
    tooltip: {trigger: 'axis'},
    xAxis: {type: 'category', data: years.map(String), axisLabel: {interval: 'auto', hideOverlap: true, color: ink()}},
    yAxis: {type: 'value', min: 0, axisLabel: {color: ink()}, splitLine: {lineStyle: {color: '#79939a38'}}},
    textStyle: {color: ink()},
    series: [{name: label, type: 'line', data: values, connectNulls: false, showSymbol: false,
      lineStyle: {color}, itemStyle: {color},
      markPoint: {symbol: 'circle', symbolSize: 8, label: {show: false},
        data: markers.map(i => ({coord: [String(years[i]), values[i]], name: String(years[i])}))},
      markLine: {silent: true, symbol: 'none', label: {show: false},
        data: selected ? [{xAxis: String(selected)}] : []}}],
  });
  const leadYear = get('lead-year');
  const a = names.map((_, i) => chart('lead-trend-' + i));
  function renderA() {
    a.forEach((instance, i) => instance.setOption(option(names[i], years.map(year =>
      Number((metrics[year][i] * (i === 1 ? 100 : 1)).toFixed(1))), colors[i], Number(leadYear.value))));
  }
  for (const instance of a) instance.getZr().on('click', event => {
    const index = instance.convertFromPixel({xAxisIndex: 0}, event.offsetX);
    if (instance.containPixel({gridIndex: 0}, [event.offsetX, event.offsetY]) && years[index]) {
      leadYear.value = String(years[index]);
      leadYear.dispatchEvent(new Event('change'));
    }
  });
  leadYear.addEventListener('change', renderA);
  document.querySelectorAll('[data-lead-year]').forEach(button => button.addEventListener('click', renderA));
  renderA();

  const codes = ['USA','GBR','URS','GDR','FRG','GER','CHN','JPN','KOR','AUS','FRA','NED'];
  const byYear = new Map(years.map(year => [year, {total: 0, teams: new Map()}]));
  for (const row of raw) {
    const edition = byYear.get(row.Year);
    if (!edition) continue;
    edition.total += row.medals;
    edition.teams.set(row.NOC, (edition.teams.get(row.NOC) || 0) + row.medals);
  }
  const team = get('history-team');
  team.replaceChildren(...codes.map(code => new Option(displayNoc(code), code)));
  const b = [chart('history-count-plot'), chart('history-share-plot')];
  function renderB() {
    const counts = years.map(year => byYear.get(year).teams.get(team.value) ?? null);
    const shares = counts.map((n,i) => n === null ? null : 100*n/byYear.get(years[i]).total);
    const opposite = [];
    for (let i = 1; i < years.length; i++) {
      if ([counts[i-1],counts[i],shares[i-1],shares[i]].includes(null)) continue;
      if ((counts[i]-counts[i-1])*(shares[i]-shares[i-1]) < 0) opposite.push(i);
    }
    b[0].setOption(option('获奖记录（条）',counts,colors[0],null,opposite));
    b[1].setOption(option('同届份额（%）',shares.map(n => n === null ? null : Number(n.toFixed(2))),colors[1],null,opposite));
    get('history-opposite').textContent = opposite.length ? opposite.map(i =>
      `${years[i-1]} → ${years[i]}：${counts[i-1]} → ${counts[i]} 条，${shares[i-1].toFixed(2)}% → ${shares[i].toFixed(2)}%`).join('；')
      : '相邻两届均有参赛记录的区间里，两项指标没有出现反向变化。';
  }
  team.addEventListener('change', renderB);
  renderB();

  const teams = new Map();
  for (const row of raw.filter(row => row.Year === 2024)) {
    if (!teams.has(row.NOC)) teams.set(row.NOC, {r: 0, m: 0, fr: 0, fm: 0, sports: new Map()});
    const data = teams.get(row.NOC);
    data.r += row.records;
    data.m += row.medals;
    if (row.Sex !== 'F') continue;
    data.fr += row.records;
    data.fm += row.medals;
    const counts = data.sports.get(row.sport_family) || [0, 0];
    counts[0] += row.records;
    counts[1] += row.medals;
    data.sports.set(row.sport_family, counts);
  }
  const gap = data => 100*(data.fm/data.m-data.fr/data.r);
  const signed = n => (n>0 ? '+' : '')+n.toFixed(2);
  const women = get('women-team');
  const ranked = [...teams].filter(([,d]) => d.r && d.m)
    .sort((a,b) => Math.abs(gap(b[1]))-Math.abs(gap(a[1])));
  women.replaceChildren(...ranked.map(([code,d]) => new Option(`${displayNoc(code)} · ${signed(gap(d))} 个百分点`,code)));
  const examples = get('women-examples');
  for (const code of ['NZL','BRA','FRA','POL']) {
    if (!teams.get(code)?.m) continue;
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = displayNoc(code);
    button.addEventListener('click', () => { women.value = code; renderC(); });
    examples.append(button);
  }
  function renderC() {
    const d = teams.get(women.value);
    for (const button of examples.children) button.setAttribute('aria-pressed', String(button.textContent === displayNoc(women.value)));
    get('women-denominators').textContent = `女性参赛 ${d.fr} / ${d.r} 条，女性获奖 ${d.fm} / ${d.m} 条，差值 ${signed(gap(d))} 个百分点。`;
    const sports = [...d.sports].map(([sport,[r,m]]) => [sport,r,m,100*(m/d.m-r/d.r)])
      .sort((a,b) => Math.abs(b[3])-Math.abs(a[3]));
    if (!sports.length) {
      const row = document.createElement('tr');
      const cell = row.insertCell();
      cell.colSpan = 4;
      cell.textContent = '该代表团没有女性参赛记录。';
      get('women-sport-rows').replaceChildren(row);
      return;
    }
    get('women-sport-rows').replaceChildren(...sports.map(([sport,r,m,value]) => {
      const row = document.createElement('tr');
      for (const cell of [sportZh[sport] || sport,r,m,signed(value)]) {
        row.insertCell().textContent = cell;
      }
      return row;
    }));
  }
  women.addEventListener('change', renderC);
  women.value = 'NZL';
  renderC();
  const resize = new ResizeObserver(() => charts.forEach(instance => instance.resize()));
  charts.forEach(instance => resize.observe(instance.getDom()));
  new MutationObserver(() => { renderA(); renderB(); }).observe(document.body, {attributes:true,attributeFilter:['class','data-theme']});
})();
