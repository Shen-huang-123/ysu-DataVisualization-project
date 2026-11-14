"""Consistent photographic opening frames and restrained motion for all 23 pages."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
START = '<!-- HERO_MOTION_START -->'
END = '<!-- HERO_MOTION_END -->'

CSS = '''<style id="hero-motion-style">
/* Every opening photograph shares a 620 px desktop / 560 px phone frame. */
body.hero-motion header.photo-editorial-hero,
body.hero-motion.hero-motion-portal header.hero,
body.hero-motion figure.photo-stage{box-sizing:border-box!important;height:620px!important;min-height:620px!important;max-height:620px!important;overflow:hidden!important}
body.hero-motion header.photo-editorial-hero{padding:clamp(36px,5vw,72px) clamp(24px,6vw,96px)!important;background-attachment:scroll!important;animation:hero-background-drift 18s ease-in-out infinite alternate}
body.hero-motion.hero-motion-portal header.hero{padding-top:clamp(38px,5vw,70px)!important;padding-bottom:clamp(38px,5vw,70px)!important;animation:hero-background-drift 18s ease-in-out infinite alternate}
body.hero-motion.hero-motion-portal header.hero:after{transform-origin:center;animation:hero-image-breathe 19s ease-in-out infinite alternate}
body.hero-motion.hero-motion-portal header.hero h1{font-size:clamp(66px,6.4vw,100px)!important;line-height:1.02!important;margin:22px 0 18px!important}
body.hero-motion.hero-motion-portal header.hero .hero-copy p{font-size:clamp(17px,1.45vw,21px)!important;line-height:1.55!important}
body.hero-motion figure.photo-stage{position:relative!important;margin-top:0!important;margin-bottom:0!important}
body.hero-motion figure.photo-stage>img{width:100%!important;height:100%!important;object-fit:cover!important;transform:scale(1.035);animation:hero-image-breathe 19s ease-in-out infinite alternate;will-change:transform}
body.hero-motion figure.photo-stage:hover>img{animation-play-state:paused;transform:scale(1.07)!important;transition:transform .8s ease!important}
body.hero-motion figure.photo-stage figcaption{position:absolute!important;left:0;right:0;bottom:0;z-index:2}
@keyframes hero-background-drift{from{background-position:center,48% center}to{background-position:center,54% center}}
@keyframes hero-image-breathe{from{transform:scale(1.035) translate3d(-.5%,0,0)}to{transform:scale(1.085) translate3d(.5%,0,0)}}
@media(max-width:700px){
 body.hero-motion header.photo-editorial-hero,
 body.hero-motion.hero-motion-portal header.hero,
 body.hero-motion figure.photo-stage{height:560px!important;min-height:560px!important;max-height:560px!important}
 body.hero-motion header.photo-editorial-hero{padding:28px 20px!important}
 body.hero-motion header.photo-editorial-hero h1{font-size:clamp(2rem,8.6vw,3.1rem)!important}
 body.hero-motion header.photo-editorial-hero .xz-hero-actions{margin-top:20px!important;gap:8px!important}
 body.hero-motion header.photo-editorial-hero .xz-primary,body.hero-motion header.photo-editorial-hero .xz-secondary{min-height:44px!important;padding:8px 14px!important}
 body.hero-motion.hero-motion-portal header.hero{padding:32px 22px!important}
 body.hero-motion.hero-motion-portal header.hero h1{font-size:clamp(2.7rem,12vw,4.3rem)!important}
 body.hero-motion figure.photo-stage figcaption{padding:18px!important}
}
@media(prefers-reduced-motion:reduce){
 body.hero-motion header.photo-editorial-hero,body.hero-motion.hero-motion-portal header.hero,body.hero-motion.hero-motion-portal header.hero:after,body.hero-motion figure.photo-stage>img{animation:none!important;transition:none!important;transform:none!important}
}
</style>'''

JS = '''<script id="hero-motion-script">(()=>{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const targets=[...document.querySelectorAll('header.photo-editorial-hero,header.hero,figure.photo-stage')];const seen=new WeakSet();const animate=el=>{if(seen.has(el))return;seen.add(el);let text=el.matches('figure')?[...el.querySelectorAll('figcaption strong,figcaption a')]:[...el.querySelectorAll('h1,.xz-eyebrow,.eyebrow,.tag,.lead,.xz-lead,p,.xz-hero-actions')].slice(0,5);text.forEach((item,i)=>{item.animate([{opacity:.45,transform:'translateY(18px)'},{opacity:1,transform:'translateY(0)'}],{duration:620+i*95,delay:i*75,easing:'cubic-bezier(.2,.75,.25,1)',fill:'both'})})};if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){animate(e.target);observer.unobserve(e.target)}})},{threshold:.15});targets.forEach(el=>observer.observe(el))}else targets.forEach(animate)})();</script>'''

for page in DELIVERY.rglob('index.html'):
    source=page.read_text(encoding='utf-8')
    source=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',source,flags=re.S)
    def add_body_class(match):
        tag=match.group(0)
        classes='hero-motion'+(' hero-motion-portal' if '统一中文入口' in str(page) else '')
        if 'class="' in tag:
            return re.sub(r'class="([^"]*)"',lambda m:'class="'+m.group(1).replace('hero-motion-portal','').replace('hero-motion','').strip()+' '+classes+'"',tag,count=1)
        return tag[:-1]+' class="'+classes+'">'
    source=re.sub(r'<body\b[^>]*>',add_body_class,source,count=1)
    source=source.replace('</head>',START+CSS+END+'</head>',1)
    source=source.replace('</body>',JS+'</body>',1) if 'id="hero-motion-script"' not in source else source
    page.write_text(source,encoding='utf-8')
    print(page.relative_to(DELIVERY))
