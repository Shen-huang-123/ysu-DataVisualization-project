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
  const option = (label, values, color, selected, markers = [], comparison = null) => ({
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
        data: selected ? [{xAxis: String(selected)}, ...(comparison && comparison !== selected ? [{xAxis: String(comparison), lineStyle:{type:'dotted'}}] : [])] : []}}],
  });
  const leadYear = get('lead-year');
  const baseline = get('lead-baseline');
  const leadTeam = get('lead-team');
  baseline.replaceChildren(...years.map(year => new Option(String(year), String(year))));
  baseline.value = '2016';
  const params = new URLSearchParams(location.search);
  const selectValue = (select, value) => {
    if ([...select.options].some(option => option.value === value)) select.value = value;
  };
  selectValue(leadYear, params.get('year'));
  leadYear.dispatchEvent(new Event('change'));
  selectValue(leadTeam, params.get('team'));
  leadTeam.dispatchEvent(new Event('change'));
  selectValue(baseline, params.get('base'));
  const format = (n,i) => i === 0 ? String(n) : n.toFixed(1) + (i === 1 ? '%' : '');
  function compareA() {
    const summary = document.createElement('dl');
    names.forEach((name,i) => {
      const factor = i === 1 ? 100 : 1;
      const before = metrics[baseline.value][i]*factor;
      const after = metrics[leadYear.value][i]*factor;
      const delta = after-before;
      const item = document.createElement('div');
      const label = document.createElement('dt');
      const value = document.createElement('dd');
      label.textContent = name;
      value.textContent = `${baseline.value}：${format(before,i)} → ${leadYear.value}：${format(after,i)}（${delta>0?'+':''}${delta.toFixed(i===0?0:1)}${i===1?' 个百分点':''}）`;
      item.append(label,value);
      summary.append(item);
    });
    get('lead-comparison').replaceChildren(summary);
  }
  baseline.addEventListener('change', renderA);
  const a = names.map((_, i) => chart('lead-trend-' + i));
  function renderA() {
    compareA();
    a.forEach((instance, i) => instance.setOption(option(names[i], years.map(year =>
      Number((metrics[year][i] * (i === 1 ? 100 : 1)).toFixed(1))), colors[i], Number(leadYear.value), [], Number(baseline.value))));
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
  selectValue(team, params.get('history'));
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
  const peer = get('women-compare');
  peer.replaceChildren(...Array.from(women.options, option => option.cloneNode(true)));
  const examples = get('women-examples');
  for (const code of ['NZL','BRA','FRA','POL']) {
    if (!teams.get(code)?.m) continue;
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = displayNoc(code);
    button.addEventListener('click', () => { women.value = code; renderC(); });
    examples.append(button);
  }
  function contributions(d, sport) {
    const [r,m] = d.sports.get(sport) || [0,0];
    return [r,m,100*(m/d.m-r/d.r)];
  }
  function renderC() {
    const choices = [women.value,peer.value];
    const data = choices.map(code => teams.get(code));
    for (const button of examples.children) button.setAttribute('aria-pressed', String(button.textContent === displayNoc(women.value)));
    get('women-primary-title').textContent = displayNoc(choices[0]);
    get('women-compare-title').textContent = displayNoc(choices[1]);
    get('women-denominators').replaceChildren(...data.map((d,i) => {
      const box = document.createElement('div');
      box.textContent = `${displayNoc(choices[i])} · 女性参赛 ${d.fr} / ${d.r} 条，女性获奖 ${d.fm} / ${d.m} 条，差值 ${signed(gap(d))} 个百分点。`;
      return box;
    }));
    const sports = [...new Set(data.flatMap(d => [...d.sports.keys()]))].map(sport => {
      const values = data.map(d => contributions(d,sport));
      return {sport,values, magnitude: Math.max(...values.map(v => Math.abs(v[2])))};
    }).sort((a,b) => b.magnitude-a.magnitude);
    const scale = sports[0]?.magnitude || 1;
    get('women-sport-rows').replaceChildren(...sports.map(({sport,values}) => {
      const row = document.createElement('tr');
      row.insertCell().textContent = sportZh[sport] || sport;
      for (const [r,m,value] of values) {
        const cell = row.insertCell();
        cell.textContent = `${signed(value)} 个百分点 · ${r} 参赛 / ${m} 获奖`;
        cell.dataset.contribution = '';
        cell.style.setProperty('--contribution-color', value < 0 ? '#b6775438' : '#57948f38');
        cell.style.setProperty('--contribution-width', (100*Math.abs(value)/scale)+'%');
      }
      return row;
    }));
  }
  women.addEventListener('change', renderC);
  peer.addEventListener('change', renderC);
  women.value = 'BRA';
  peer.value = 'FRA';
  selectValue(women,params.get('women'));
  selectValue(peer,params.get('peer'));
  renderC();

  const anchors = {a:'panorama-lead', b:'team-share-case', c:'panorama-gender'};
  const state = () => ({
    year:leadYear.value, base:baseline.value, team:leadTeam.value, history:team.value,
    women:women.value, peer:peer.value,
  });
  function exportRows(view) {
    const scope = '运动员记录行；排除1906';
    if (view === 'a') {
      const selected = raw.filter(r => String(r.Year) === leadYear.value && r.NOC === leadTeam.value);
      const sportCounts = new Map();
      for (const row of selected) sportCounts.set(row.sport_family,(sportCounts.get(row.sport_family) || 0)+row.medals);
      return [['类型','届次','代表团','运动','获奖行','获奖代表团数','前五份额','有效获奖代表团数','统计口径'],
        ...[baseline.value,leadYear.value].map(year => ['全榜',year,'','','',...metrics[year],scope]),
        ...[...sportCounts].filter(([,n])=>n>0).map(([sport,n])=>['运动构成',leadYear.value,leadTeam.value,sport,n,'','','',scope])];
    }
    if (view === 'b') return [['届次','代表团','有参赛记录','获奖记录','全场获奖记录（分母）','同届份额','统计口径'],
      ...years.map(year => {
        const edition = byYear.get(year);
        const count = edition.teams.get(team.value);
        return [year,team.value,count !== undefined,count ?? '',edition.total,count === undefined ? '' : count/edition.total,scope];
      })];
    const selected = [women.value,peer.value];
    const sports = [...new Set(selected.flatMap(code => [...teams.get(code).sports.keys()]))];
    return [['届次','代表团','运动','女性参赛记录','女性获奖记录','全队参赛记录（分母）','全队获奖记录（分母）','贡献（百分点）','统计口径'],
      ...selected.flatMap(code => {
        const d = teams.get(code);
        return [[2024,code,'全队',d.fr,d.fm,d.r,d.m,gap(d),scope],
          ...sports.map(sport => [2024,code,sport,...contributions(d,sport).slice(0,2),d.r,d.m,contributions(d,sport)[2],scope])];
      })];
  }
  for (const controls of document.querySelectorAll('.analysis-actions')) {
    const view = controls.dataset.analysis;
    const status = controls.querySelector('[role=status]');
    controls.querySelector('[data-copy]').addEventListener('click', async () => {
      const url = new URL(location.href);
      url.search = new URLSearchParams(state());
      url.hash = anchors[view];
      try {
        await navigator.clipboard.writeText(url.href);
        status.textContent = '已复制当前分析链接。';
      } catch {
        window.prompt('复制当前分析链接',url.href);
      }
    });
    controls.querySelector('[data-export]').addEventListener('click', () => {
      const csv = exportRows(view).map(row => row.map(cell => '"' + String(cell).replaceAll('"','""') + '"').join(',')).join('\r\n');
      const url = URL.createObjectURL(new Blob(['\ufeff',csv],{type:'text/csv;charset=utf-8'}));
      const download = document.createElement('a');
      download.href = url;
      download.download = `百年全景-${view.toUpperCase()}-当前对照.csv`;
      download.click();
      setTimeout(() => URL.revokeObjectURL(url),1000);
      status.textContent = '已生成当前对照 CSV。';
    });
  }
  const resize = new ResizeObserver(() => charts.forEach(instance => instance.resize()));
  charts.forEach(instance => resize.observe(instance.getDom()));
  new MutationObserver(() => { renderA(); renderB(); }).observe(document.body, {attributes:true,attributeFilter:['class','data-theme']});
})();
