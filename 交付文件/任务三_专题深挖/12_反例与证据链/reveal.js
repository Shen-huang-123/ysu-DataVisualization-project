(() => {
  const steps = [...document.querySelectorAll('.reveal-step')];
  const panel = document.querySelector('.reveal-panel');
  if (!steps.length || !panel) return;
  const cases = {
    host: { title: '主场不保证增长', unit: '获奖运动员行占比 · 巴西', rows: [['2012 · 前一届', '3.04%', '100%'], ['2016 · 主办届', '2.47%', '81.3%']], note: '巴西自身下降 0.57 个百分点；相对五个匹配代表团的平均变化仍高约 0.13 个百分点。这是描述性比较，不是因果净效应。', source: 'S1 东道主分析 · 赛题 CSV，运动员行口径' },
    lens: { title: '换统计单位，名次改写', unit: '2024 巴黎 · 西班牙金牌榜名次', rows: [['官方获奖小项', '第 15'], ['运动员获奖行', '第 5']], note: '名次变化来自团队项目的多人获奖行。两种口径回答不同问题，不能把运动员行写成 IOC 官方奖牌数。', source: 'S2 三口径排名 · 2024 官方小项表与赛题运动员行' },
    record: { title: '接口标签经不起原件复核', unit: '伦敦 2012 · 女子 100 米自由泳 · 唐奕', rows: [['世界泳联接口', '银 / 第 2'], ['赛时官方成绩册', '铜 / 第 3']], note: '成绩册第 13 页记载 53.44 秒、第 3 名。此处按赛时原件修正接口标签；现行 IOC 授牌状态仍需另行核对。', source: '伦敦 2012 游泳赛时官方成绩册，第 13 页' }
  };
  const title = panel.querySelector('[data-title]'), unit = panel.querySelector('[data-unit]'), chart = panel.querySelector('.reveal-chart'), note = panel.querySelector('.reveal-note'), source = panel.querySelector('.reveal-source'), dots = panel.querySelector('.reveal-dots');
  let current = -1;
  function activate(index) {
    if (index === current || index < 0) return;
    current = index;
    const step = steps[index], item = cases[step.dataset.case], phase = Number(step.dataset.phase);
    steps.forEach((el, i) => el.classList.toggle('is-active', i === index));
    title.textContent = item.title; unit.textContent = item.unit; note.textContent = item.note; source.textContent = item.source;
    chart.innerHTML = item.rows.map((row, i) => `<div class="reveal-row ${row[2] ? '' : 'reveal-categorical'} ${phase === 2 || i === Math.min(phase, 1) ? 'active' : ''}"><div class="reveal-row-head"><span>${row[0]}</span><strong>${row[1]}</strong></div>${row[2] ? `<div class="reveal-track"><div class="reveal-fill" style="--w:${row[2]}"></div></div>` : ''}</div>`).join('');
    dots.innerHTML = [0,1,2].map(i => `<i class="${i === phase ? 'on' : ''}"></i>`).join('');
  }
  const observer = new IntersectionObserver(entries => {
    const visible = entries.filter(e => e.isIntersecting).sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (visible) activate(steps.indexOf(visible.target));
  }, { rootMargin: '-28% 0px -32% 0px', threshold: [0, .25, .5] });
  steps.forEach(step => observer.observe(step));
  activate(0);
})();

(() => {
  if (!('IntersectionObserver' in window) || !Element.prototype.animate) return;
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  const observer = new IntersectionObserver((entries) => {
    for (const { target, isIntersecting } of entries) {
      if (!isIntersecting) continue;
      observer.unobserve(target);
      if (reduced.matches || target.contains(document.activeElement)) continue;
      const animation = target.animate(
        [{ opacity: 0.78, translate: '0 8px' }, { opacity: 1, translate: '0 0' }],
        { duration: 380, easing: 'cubic-bezier(.22,1,.36,1)' }
      );
      const stop = () => { if (reduced.matches) animation.cancel(); };
      reduced.addEventListener('change', stop);
      animation.finished.catch(() => {}).finally(() => reduced.removeEventListener('change', stop));
    }
  }, { threshold: 0.05 });
  document.querySelectorAll('.evidence-chain main :is(h1, .reveal-story > h2, .evidence-summary, .case-head, .case .step, .matrix > h2, .matrix > table)').forEach(element => observer.observe(element));
})();
