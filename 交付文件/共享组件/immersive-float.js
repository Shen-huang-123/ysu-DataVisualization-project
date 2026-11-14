/* Quiet, scroll-responsive orbit for editorial hero sections. */
(() => {
  const start = () => {
    if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    const candidates = document.querySelectorAll(
      'header.photo-editorial-hero, header.xz-hero, header.hero, section.hero, header.s1-hero, header.m-hero, main > .hero, body > header, section.intro'
    );
    const hero = [...candidates].find(el => {
      const box = el.getBoundingClientRect();
      return box.width >= 300 && box.height >= 220 && !el.closest('#voyage-stage');
    });
    if (!hero || hero.classList.contains('photo-editorial-hero') || hero.querySelector('.immersive-float-layer')) return;

    const css = document.createElement('style');
    css.textContent = `
      .immersive-float-host{position:relative;isolation:isolate}
      .immersive-float-layer{position:absolute;inset:0;z-index:3;overflow:hidden;pointer-events:none;color:#c4a477}
      .immersive-float-orbit{position:absolute;right:9%;top:7%;width:clamp(150px,17vw,240px);aspect-ratio:1;opacity:.3;will-change:transform}
      .immersive-float-orbit i{position:absolute;display:block;border:1px solid currentColor;border-radius:50%}
      .immersive-float-orbit i:first-child{inset:4%;border-style:dashed;opacity:.7}
      .immersive-float-orbit i:nth-child(2){inset:23%;border-width:2px;opacity:.6}
      .immersive-float-orbit i:last-child{width:10px;height:10px;right:8%;top:22%;border:0;background:currentColor;box-shadow:0 0 18px currentColor;opacity:.7}
      @media(max-width:700px),(prefers-reduced-motion:reduce){.immersive-float-layer{display:none}}
    `;
    document.head.appendChild(css);
    hero.classList.add('immersive-float-host');
    const layer = document.createElement('div');
    layer.className = 'immersive-float-layer';
    layer.setAttribute('aria-hidden', 'true');
    layer.innerHTML = '<div class="immersive-float-orbit"><i></i><i></i><i></i></div>';
    hero.insertBefore(layer, hero.firstChild);

    const orbit = layer.firstElementChild;
    let mouseX = 0, mouseY = 0, raf = 0;
    const draw = () => {
      raf = 0;
      const box = hero.getBoundingClientRect();
      if (box.bottom < 0 || box.top > innerHeight || innerWidth <= 700) return;
      const progress = Math.max(-1, Math.min(1, (innerHeight / 2 - box.top - box.height / 2) / innerHeight));
      orbit.style.transform = `translate3d(${(mouseX * 13 + progress * 24).toFixed(1)}px,${(mouseY * 9 - progress * 28).toFixed(1)}px,0) rotate(${(progress * 8).toFixed(1)}deg)`;
    };
    const schedule = () => { if (!raf) raf = requestAnimationFrame(draw); };
    addEventListener('scroll', schedule, { passive: true });
    addEventListener('resize', schedule, { passive: true });
    addEventListener('pointermove', e => {
      if (e.pointerType === 'touch') return;
      mouseX = e.clientX / innerWidth - .5;
      mouseY = e.clientY / innerHeight - .5;
      schedule();
    }, { passive: true });
    schedule();
  };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start, { once: true });
  else start();
})();
