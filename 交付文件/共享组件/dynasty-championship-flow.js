(() => {
  const get = id => document.getElementById('dynasty-flow-' + id);
  const {editions, names} = JSON.parse(get('data').textContent);
  const play = get('play');
  let timer;
  const edition = get('edition');
  const kind = get('kind');
  const chart = get('chart');
  const list = get('list');
  editions.forEach(([start, end], index) => edition.add(new Option(start + ' → ' + end, index)));
  edition.selectedIndex = editions.length - 1;

  function mark(tag, attributes, label) {
    const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
    Object.entries(attributes).forEach(([key, value]) => node.setAttribute(key, value));
    if (label) node.textContent = label;
    return node;
  }

  function render() {
    const [start, end, flows] = editions[edition.selectedIndex];
    const displayed = flows.filter(([, , defended]) => kind.value === 'all' || defended === (kind.value === 'defended'));
    const total = flows.reduce((sum, row) => sum + row[3], 0);
    const retained = flows.reduce((sum, row) => sum + (row[2] ? row[3] : 0), 0);
    const shown = displayed.reduce((sum, row) => sum + row[3], 0);
    get('status').textContent = start + ' → ' + end + '，卫冕 ' + retained +
      ' 项，易主 ' + (total - retained) + ' 项。当前显示 ' + shown + ' 项。';

    const left = [...new Set(displayed.map(row => row[0]))].sort();
    const right = [...new Set(displayed.map(row => row[1]))].sort();
    const height = Math.max(160, 49 + Math.max(left.length, right.length) * 22);
    const coordinates = codes => new Map(codes.map((code, index) =>
      [code, 48 + index * (height - 70) / Math.max(1, codes.length - 1)]));
    const from = coordinates(left);
    const to = coordinates(right);
    chart.setAttribute('viewBox', '0 0 720 ' + height);
    chart.replaceChildren(mark('text', {x: 18, y: 22}, start + ' 上届'), mark('text', {x: 565, y: 22}, end + ' 本届'));
    const items = [];
    displayed.sort((a,b) => b[3] - a[3]).forEach(([source, target, defended, count]) => {
      const y1 = from.get(source), y2 = to.get(target);
      const label = names[source] + ' → ' + names[target] + ' · ' + (defended ? '卫冕' : '易主') + ' ' + count + ' 项';
      const path = mark('path', {d: 'M 155 ' + y1 + ' C 270 ' + y1 + ', 450 ' + y2 + ', 565 ' + y2,
        class: defended ? 'flow-defended' : 'flow-changed', 'stroke-width': count * 1.6});
      path.append(mark('title', {}, label));
      chart.append(path);
      const li = document.createElement('li');
      li.textContent = label;
      items.push(li);
    });
    for (const [code,y] of from) chart.append(mark('text', {x: 145,y,'text-anchor':'end','dominant-baseline':'central'}, names[code]));
    for (const [code,y] of to) chart.append(mark('text', {x: 575,y,'dominant-baseline':'central'}, names[code]));
    list.replaceChildren(...items);
  }

  function pause() {
    clearInterval(timer);
    timer = undefined;
    play.textContent = '播放历届';
  }

  play.addEventListener('click', () => {
    if (timer !== undefined) {
      pause();
      return;
    }
    if (edition.selectedIndex === editions.length - 1) edition.selectedIndex = 0;
    play.textContent = '暂停播放';
    render();
    timer = setInterval(() => {
      edition.selectedIndex += 1;
      render();
      if (edition.selectedIndex === editions.length - 1) pause();
    }, 1800);
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });
  edition.addEventListener('change', () => {
    pause();
    render();
  });
  kind.addEventListener('change', render);
  render();
})();
