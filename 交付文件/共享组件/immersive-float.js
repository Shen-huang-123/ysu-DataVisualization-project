/* Shared Olympic track motif for editorial openings; static and non-interactive. */
(() => {
  const start = () => {
    const candidates = document.querySelectorAll('header.photo-editorial-hero, header.xz-hero, header.hero, section.hero, header.s1-hero, header.m-hero, main > .hero, body > header, section.intro');
    const hero = [...candidates].find(el => {
      const box = el.getBoundingClientRect();
      return box.width >= 300 && box.height >= 220 && !el.closest('#voyage-stage');
    });
    if (!hero || hero.classList.contains('photo-editorial-hero') || hero.querySelector('.immersive-float-layer')) return;
    const css = document.createElement('style');
    css.textContent = `
      .immersive-float-host{position:relative;isolation:isolate}
      .immersive-float-layer{position:absolute;inset:0;z-index:0;overflow:hidden;pointer-events:none}
      .immersive-track-art{position:absolute;right:-3%;top:3%;width:clamp(280px,40vw,620px);height:auto;opacity:.26;mask-image:linear-gradient(90deg,transparent,#000 35%);pointer-events:none}
      @media(max-width:700px){.immersive-track-art{width:85vw;right:-28%;top:0;opacity:.12}}
    `;
    document.head.appendChild(css);
    hero.classList.add('immersive-float-host');
    const layer = document.createElement('div');
    layer.className = 'immersive-float-layer';
    layer.setAttribute('aria-hidden', 'true');
    layer.innerHTML = '<svg class="immersive-track-art" viewBox="0 0 640 210" focusable="false" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke-width="1.2"><path d="M60 210 C220 210 210 25 380 25 H640" stroke="#83b6c8"/><path d="M90 210 C250 210 240 45 400 45 H640" stroke="#d6bd82"/><path d="M120 210 C280 210 270 65 420 65 H640" stroke="#bac9ca"/><path d="M150 210 C310 210 300 85 440 85 H640" stroke="#82ad99"/><path d="M180 210 C340 210 330 105 460 105 H640" stroke="#c894a1"/></g></svg>';
    hero.insertBefore(layer, hero.firstChild);
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
