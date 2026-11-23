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

  const layer = mark('g', {});
  const labels = mark('g', {});
  const previousYear = mark('text', {x: 18, y: 22});
  const currentYear = mark('text', {x: 565, y: 22});
  chart.append(layer, labels, previousYear, currentYear);
  const marks = new Map();
  let animation;
  let pinned;
  let hovered;
  let focused;

  function highlight() {
    const active = hovered || pinned || focused;
    chart.classList.toggle('flow-tracing', Boolean(active) && Array.from(layer.children)
      .some(path => path.style.pointerEvents !== 'none' && path.dataset[active.side] === active.code));
    for (const path of layer.children) {
      path.classList.toggle('flow-highlight', Boolean(active && path.dataset[active.side] === active.code));
    }
    for (const label of labels.children) {
      const selected = pinned?.side === label.dataset.side && pinned.code === label.dataset.code;
      label.setAttribute('aria-pressed', String(selected));
    }
  }

  function connectLabel(node, side, code) {
    const target = {side: side ? 'target' : 'source', code};
    Object.assign(node.dataset, target);
    node.addEventListener('pointerenter', event => {
      if (event.pointerType !== 'touch') { hovered = target; highlight(); }
    });
    node.addEventListener('pointerleave', () => { hovered = undefined; highlight(); });
    node.addEventListener('focus', () => { if (node.matches(':focus-visible')) focused = target; highlight(); });
    node.addEventListener('blur', () => { focused = undefined; highlight(); });
    node.addEventListener('click', () => {
      pinned = pinned?.side === target.side && pinned.code === code ? undefined : target;
      highlight();
    });
    node.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        node.dispatchEvent(new Event('click'));
      }
    });
  }

  function morph(targets, duration) {
    cancelAnimationFrame(animation);
    for (const [key, target] of targets) {
      if (!marks.has(key)) {
        target.parent.append(target.node);
        marks.set(key, {...target, values: [...target.values.slice(0, -1), 0]});
      }
      const entry = marks.get(key);
      if (target.title) entry.node.firstChild.textContent = target.title;
    }
    const tracks = Array.from(marks, ([key, entry]) => {
      const target = targets.get(key);
      entry.node.style.pointerEvents = target ? '' : 'none';
      if (entry.parent === labels) entry.node.setAttribute('tabindex', target ? '0' : '-1');
      return {key, entry, start: entry.values,
        end: target?.values || [...entry.values.slice(0, -1), 0], exiting: !target};
    });
    const started = performance.now();
    function frame(now) {
      const progress = duration ? Math.min(1, (now - started) / duration) : 1;
      const eased = progress * progress * (3 - 2 * progress);
      for (const {key, entry, start, end, exiting} of tracks) {
        if (progress === 1 && exiting) {
          entry.node.remove();
          marks.delete(key);
          const {side, code} = entry.node.dataset;
          if (hovered && hovered.side === side && hovered.code === code) hovered = undefined;
          if (focused && focused.side === side && focused.code === code) focused = undefined;
          continue;
        }
        const values = entry.values = start.map((value, i) => value + (end[i] - value) * eased);
        const [y1, y2, width] = values;
        if (entry.parent === layer) {
          entry.node.setAttribute('d', 'M 155 ' + y1 + ' C 270 ' + y1 + ', 450 ' + y2 + ', 565 ' + y2);
          entry.node.setAttribute('stroke-width', width);
        } else {
          entry.node.setAttribute('y', y1);
        }
        entry.node.style.opacity = values.at(-1);
      }
      if (progress < 1) animation = requestAnimationFrame(frame);
      else highlight();
    }
    frame(started);
    highlight();
  }

  function render(playing = false) {
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
    previousYear.textContent = start + ' ' + "上届";
    currentYear.textContent = end + ' ' + "本届";
    const targets = new Map();
    const items = [];
    displayed.sort((a,b) => b[3] - a[3]).forEach(([source, target, defended, count]) => {
      const y1 = from.get(source), y2 = to.get(target);
      const label = names[source] + ' → ' + names[target] + ' · ' + (defended ? '卫冕' : '易主') + ' ' + count + ' 项';
      const key = JSON.stringify([source, target, defended]);
      const node = marks.get(key)?.node || mark('path', {class: defended ? 'flow-defended' : 'flow-changed'});
      if (!node.firstChild) {
        Object.assign(node.dataset, {source, target});
        node.append(mark('title', {}, label));
      }
      targets.set(key, {node, parent: layer, title: label, values: [y1, y2, count * 1.6, 1]});
      const li = document.createElement('li');
      li.textContent = label;
      items.push(li);
    });
    for (const [side, positions] of [[0, from], [1, to]]) {
      for (const [code, y] of positions) {
        const key = side + ':' + code;
        const node = marks.get(key)?.node || mark('text', {x: side ? 575 : 145,
          'text-anchor': side ? 'start' : 'end', 'dominant-baseline': 'central', role: 'button'}, names[code]);
        if (!marks.has(key)) connectLabel(node, side, code);
        targets.set(key, {node, parent: labels, values: [y, 1]});
      }
    }
    morph(targets, motion.matches || !marks.size ? 0 : playing ? 1150 : 450);
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
    }, 1500);
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
