/* Short, nonblocking chapter cue when arriving from the work homepage. */
(() => {
  const chapter = new URL(location.href).searchParams.get('chapter');
  if (!/^[1-4]$/.test(chapter) || matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  const names = ['数据体检', '百年全景', '专题深挖', '开放创作'];
  const colors = ['#d4ae77', '#8ec2cd', '#d5a2aa', '#a7c79d'];
  const start = () => {
    const style = document.createElement('style');
    style.textContent = `.chapter-handoff{position:fixed;z-index:2147483001;top:84px;left:clamp(16px,5vw,70px);display:flex;align-items:center;gap:20px;max-width:calc(100vw - 32px);padding:13px 15px 13px 20px;border:1px solid #ffffff6b;border-left:4px solid var(--chapter-color);border-radius:15px;background:#102b34ef;color:#f6f3ec;box-shadow:0 18px 45px #061b2366;backdrop-filter:blur(12px);font:700 14px/1.4 'Microsoft YaHei',sans-serif;opacity:0;transform:translate3d(0,-16px,0);transition:opacity .28s ease,transform .35s cubic-bezier(.2,1,.25,1);pointer-events:none}.chapter-handoff.show{opacity:1;transform:translate3d(0,0,0);pointer-events:auto}.chapter-handoff b{color:var(--chapter-color);font-size:12px}.chapter-handoff button{margin-left:auto;padding:5px 8px;border:1px solid #ffffff7a;border-radius:7px;background:transparent;color:inherit;cursor:pointer;font:600 11px 'Microsoft YaHei',sans-serif}@media(max-width:650px){.chapter-handoff{top:68px;left:12px;right:12px;padding:10px 12px;font-size:12px}}`;
    document.head.appendChild(style);
    const cue = document.createElement('div');
    cue.className = 'chapter-handoff';
    cue.style.setProperty('--chapter-color', colors[Number(chapter)-1]);
    cue.innerHTML = `<b>第 0${chapter} 章</b><span>${names[Number(chapter)-1]}</span><button type="button" aria-label="跳过章节提示">跳过</button>`;
    document.body.appendChild(cue);
    const close = () => { cue.classList.remove('show'); setTimeout(() => cue.remove(), 380); };
    cue.querySelector('button').addEventListener('click', close);
    addEventListener('keydown', e => { if (e.key === 'Escape') close(); }, { once: true });
    requestAnimationFrame(() => cue.classList.add('show'));
    setTimeout(close, 1150);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
