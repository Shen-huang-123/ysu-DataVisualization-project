(() => {
  const get = id => document.getElementById(id);
  const [metrics, contributions] = JSON.parse(get('panorama-lead-data').textContent);
  const year = get('lead-year');
  const team = get('lead-team');
  const rank = (records, key) => {
    const totals = new Map();
    for (const row of records) totals.set(row[key], (totals.get(row[key]) || 0) + row.medals);
    return [...totals].filter(([, value]) => value > 0).sort((a, b) => b[1] - a[1]);
  };
  function bar(label, value, number, scale, button = false) {
    const row = document.createElement(button ? 'button' : 'div');
    row.className = 'lead-bar';
    if (button) row.type = 'button';
    row.dataset.direction = value < 0 ? 'negative' : 'positive';
    row.style.setProperty('--fill', 100 * Math.abs(value) / scale + '%');
    row.append(Object.assign(document.createElement('span'), {textContent: label}),
      Object.assign(document.createElement('strong'), {textContent: number}));
    return row;
  }
  function renderTeam() {
    get('lead-sport-title').textContent = displayNoc(team.value) + ' · 运动构成';
    const sports = rank(raw.filter(row => row.Year === Number(year.value) && row.NOC === team.value), 'sport_family');
    get('lead-sports').replaceChildren(...sports.map(([sport, count]) =>
      bar(sportZh[sport] || sport, count, count + ' 条', sports[0][1])));
    for (const button of get('lead-teams').children) {
      button.setAttribute('aria-pressed', String(button.dataset.team === team.value));
    }
  }
  const shortcuts = document.querySelectorAll('[data-lead-year]');
  function renderYear() {
    for (const button of shortcuts) button.setAttribute('aria-pressed', String(button.dataset.leadYear === year.value));
    const [count, share, effective] = metrics[year.value];
    get('lead-count').textContent = count;
    get('lead-share').textContent = (share * 100).toFixed(1) + '%';
    get('lead-effective').textContent = effective.toFixed(1);
    const leaders = rank(raw.filter(row => row.Year === Number(year.value)), 'NOC');
    const selected = team.value;
    team.replaceChildren(...leaders.map(([code]) => new Option(displayNoc(code), code)));
    if (leaders.some(([code]) => code === selected)) team.value = selected;
    get('lead-teams').replaceChildren(...leaders.slice(0, 5).map(([code, count]) => {
      const row = bar(displayNoc(code), count, count + ' 条', leaders[0][1], true);
      row.dataset.team = code;
      row.addEventListener('click', () => {
        team.value = code;
        renderTeam();
      });
      return row;
    }));
    renderTeam();
  }
  year.replaceChildren(...Object.keys(metrics).reverse().map(value => new Option(value + ' 年', value)));
  year.addEventListener('change', renderYear);
  for (const button of shortcuts) button.addEventListener('click', () => {
    year.value = button.dataset.leadYear;
    renderYear();
  });
  team.addEventListener('change', renderTeam);
  renderYear();
  const sorted = [...contributions].sort((a, b) => b[1] - a[1]);
  const scale = Math.max(...sorted.map(([, value]) => Math.abs(value)));
  get('lead-gender-bars').replaceChildren(...[...sorted.slice(0, 3), ...sorted.slice(-3).reverse()].map(([sport, value]) =>
    bar(sport, value, (value > 0 ? '+' : '−') + Math.abs(value).toFixed(2), scale)));
})();
