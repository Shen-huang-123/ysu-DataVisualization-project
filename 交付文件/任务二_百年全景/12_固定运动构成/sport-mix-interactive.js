(() => {
  const get = id => document.getElementById(id);
  const {summaries, teams, sports, baseline, team_names} = JSON.parse(get('mix-data').textContent);
  const year = get('mix-year'), mode = get('mix-mode'), sport = get('mix-sport');
  const teamName = code => team_names[code] || code;
  const percent = n => (n * 100).toFixed(2) + '%';
  const signed = n => (n > 0 ? '+' : '') + n.toFixed(2);
  let animation;
  function render() {
    const selectedYear = Number(year.value);
    const selectedMode = mode.value;
    const summary = summaries.find(row => row[0] === selectedYear && row[1] === selectedMode);
    const roster = teams.filter(row => row[0] === selectedYear && row[1] === selectedMode);
    const prior = summaries.find(row => row[0] === 2016 && row[1] === selectedMode);
    get('mix-share').textContent = percent(summary[6]);
    get('mix-effective').textContent = summary[7].toFixed(2);
    get('mix-delta').textContent = signed(100 * (summary[6] - prior[6])) + ' 个百分点';
    const cohort = roster.reduce((sum,row) => sum + (baseline.includes(row[2]) ? row[3] : 0),0);
    get('mix-cohort').textContent = `固定 2016 年标准化榜五队（${baseline.map(teamName).join('、')}）的合计份额为 ${percent(cohort)}。`;
    get('mix-ranks').replaceChildren(...roster.slice(0,5).map(([, ,code,share]) => {
      const row = document.createElement('li');
      row.style.setProperty('--mix-width', share * 100 + '%');
      for (const label of [teamName(code), percent(share)]) {
        const text = document.createElement('span');
        text.textContent = label;
        row.append(text);
      }
      return row;
    }));
    if (!matchMedia('(prefers-reduced-motion: reduce)').matches && get('mix-result').animate) {
      animation?.cancel();
      animation = get('mix-result').animate([{opacity:.62},{opacity:1}], {duration:190,easing:'ease-out'});
    }
  }
  function showSport() {
    const entry = sports.find(row => row[0] === sport.value);
    const [, name, weight, contribution, counts] = entry;
    get('mix-sport-result').textContent = `${name}的固定权重为 ${percent(weight)}。2016／2020／2024 获奖记录分别为 ${counts.join('／')} 条。该运动对固定五队 2016→2024 份额变化的贡献为 ${signed(contribution)} 个百分点。`;
    for (const button of get('mix-sport-examples').children) {
      button.setAttribute('aria-pressed',String(button.dataset.sport === sport.value));
    }
  }
  sport.replaceChildren(...sports.map(([key,name]) => new Option(name,key)));
  for (const key of ['Athletics','Fencing','Gymnastics']) {
    const entry = sports.find(row => row[0] === key);
    if (!entry) continue;
    const button = document.createElement('button');
    button.type = 'button';
    button.dataset.sport = key;
    button.textContent = entry[1];
    button.addEventListener('click', () => { sport.value = key; showSport(); });
    get('mix-sport-examples').append(button);
  }
  for (const select of [year,mode]) select.addEventListener('change',render);
  sport.addEventListener('change',showSport);
  render();
  showSport();
})();
