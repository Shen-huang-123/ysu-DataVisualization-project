(() => {
  const get = id => document.getElementById('dynasty-flow-' + id);
  const {editions, names} = JSON.parse(get('data').textContent);
  const play = get('play');
  let timer;
  const edition = get('edition');
  const kind = get('kind');
  const chart = get('chart');
  const list = get('list');
  let index = editions.length - 1;
  let filter = 'all';
  const motion = matchMedia('(prefers-reduced-motion: reduce)');
  const height = 49 + 22 * Math.max(...editions.flatMap(([, , flows]) =>
    [0, 1].map(side => new Set(flows.map(row => row[side])).size)));
  const buttons = editions.map(([start, end], i) => {
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = end;
    button.setAttribute('aria-label', start + ' 至 ' + end);
    button.onclick = () => { pause(); index = i; render(); };
    edition.append(button);
    return button;
  });
  chart.setAttribute('viewBox', '0 0 720 ' + height);

  function mark(tag, attributes, label) {
    const node = document.createElementNS('http://www.w3.org/2000/svg', tag);
    Object.entries(attributes).forEach(([key, value]) => node.setAttribute(key, value));
    if (label) node.textContent = label;
    return node;
  }

  function render() {
    const [start, end, flows] = editions[index];
    const displayed = flows.filter(([, , defended]) => filter === 'all' || defended === (filter === 'defended'));
    const total = flows.reduce((sum, row) => sum + row[3], 0);
    const retained = flows.reduce((sum, row) => sum + (row[2] ? row[3] : 0), 0);
    const shown = displayed.reduce((sum, row) => sum + row[3], 0);
    get('status').textContent = start + ' → ' + end + '，卫冕 ' + retained +
      ' 项，易主 ' + (total - retained) + ' 项。当前显示 ' + shown + ' 项。';

    const left = [...new Set(displayed.map(row => row[0]))].sort();
    const right = [...new Set(displayed.map(row => row[1]))].sort();
    const coordinates = codes => new Map(codes.map((code, index) =>
      [code, 48 + index * (height - 70) / Math.max(1, codes.length - 1)]));
    const from = coordinates(left);
    const to = coordinates(right);
    buttons.forEach((button, i) => button.setAttribute('aria-pressed', String(i === index)));
    const previous = chart.querySelector('.flow-frame-current');
    const frame = mark('g', {class: 'flow-frame-current'});
    frame.append(mark('text', {x: 18, y: 22}, start + ' 上届'), mark('text', {x: 565, y: 22}, end + ' 本届'));
    const items = [];
    displayed.sort((a,b) => b[3] - a[3]).forEach(([source, target, defended, count]) => {
      const y1 = from.get(source), y2 = to.get(target);
      const label = names[source] + ' → ' + names[target] + ' · ' + (defended ? '卫冕' : '易主') + ' ' + count + ' 项';
      const path = mark('path', {d: 'M 155 ' + y1 + ' C 270 ' + y1 + ', 450 ' + y2 + ', 565 ' + y2,
        class: defended ? 'flow-defended' : 'flow-changed', 'stroke-width': count * 1.6});
      path.append(mark('title', {}, label));
      frame.append(path);
      const li = document.createElement('li');
      li.textContent = label;
      items.push(li);
    });
    for (const [code,y] of from) frame.append(mark('text', {x: 145,y,'text-anchor':'end','dominant-baseline':'central'}, names[code]));
    for (const [code,y] of to) frame.append(mark('text', {x: 575,y,'dominant-baseline':'central'}, names[code]));
    for (const layer of [...chart.children]) {
      if (layer !== previous) layer.remove();
    }
    chart.append(frame);
    if (previous && !motion.matches) {
      previous.classList.remove('flow-frame-current');
      previous.setAttribute('aria-hidden', 'true');
      previous.style.pointerEvents = 'none';
      previous.animate([{opacity:1},{opacity:0}], {duration:380,easing:'ease-out'}).onfinish = () => previous.remove();
      frame.animate([{opacity:.15},{opacity:1}], {duration:380,easing:'ease-out'});
    } else previous?.remove();
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
    if (index === editions.length - 1) index = 0;
    play.textContent = '暂停播放';
    render();
    timer = setInterval(() => {
      index += 1;
      render();
      if (index === editions.length - 1) pause();
    }, 1800);
  });
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) pause();
  });
  kind.addEventListener('click', event => {
    const button = event.target.closest('[data-kind]');
    if (!button) return;
    filter = button.dataset.kind;
    for (const item of kind.querySelectorAll('button')) {
      item.setAttribute('aria-pressed', String(item === button));
    }
    render();
  });
  render();
})();
