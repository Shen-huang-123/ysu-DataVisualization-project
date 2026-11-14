"""One stable topbar across all deliverable HTML pages."""
from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DELIVERY = ROOT / '交付文件'
START = '<!-- UNIFIED_TOPBAR_START -->'
END = '<!-- UNIFIED_TOPBAR_END -->'

CSS = r'''<style id="unified-topbar-style">
html{scrollbar-gutter:stable}
#xz-nav{box-sizing:border-box!important;position:fixed!important;inset:0 0 auto!important;z-index:1000!important;height:68px!important;display:flex!important;align-items:center!important;justify-content:space-between!important;gap:16px!important;padding:0 clamp(18px,4.5vw,72px)!important;background:#102e37!important;color:#f5f7f3!important;border:0!important;border-bottom:1px solid rgba(255,255,255,.18)!important;box-shadow:0 5px 20px rgba(9,31,39,.14)!important;backdrop-filter:none!important;font-family:'Microsoft YaHei',system-ui,sans-serif!important;transition:none!important}
#xz-nav *,#xz-nav *:before,#xz-nav *:after{box-sizing:border-box!important;transition:background-color .15s ease,color .15s ease!important;animation:none!important}
#xz-nav .xz-brand{display:flex!important;align-items:center!important;gap:11px!important;color:#f5f7f3!important;text-decoration:none!important;font-size:16px!important;font-weight:800!important;letter-spacing:0!important;white-space:nowrap!important}
#xz-nav .xz-mark{display:grid!important;place-items:center!important;width:34px!important;height:34px!important;flex:0 0 34px!important;border-radius:50%!important;background:#a2d5c9!important;color:#183f44!important;font-size:17px!important;line-height:1!important;box-shadow:none!important}
#xz-nav .xz-links{display:flex!important;align-items:center!important;gap:4px!important;margin:0!important}
#xz-nav .xz-links>a{display:inline-flex!important;align-items:center!important;min-height:38px!important;padding:7px 12px!important;border-radius:8px!important;color:#d9e7e5!important;text-decoration:none!important;font-size:13px!important;font-weight:700!important;letter-spacing:0!important;white-space:nowrap!important;background:transparent!important;box-shadow:none!important}
#xz-nav .xz-links>a:hover,#xz-nav .xz-links>a[aria-current=page]{background:rgba(255,255,255,.14)!important;color:#fff!important}
#xz-nav .xz-links>a:after{display:none!important}
#xz-nav button{display:inline-flex!important;align-items:center!important;justify-content:center!important;height:38px!important;min-width:38px!important;margin:0 0 0 5px!important;padding:0 11px!important;border:1px solid rgba(255,255,255,.35)!important;border-radius:10px!important;background:transparent!important;color:#f7faf7!important;font-size:14px!important;font-weight:700!important;white-space:nowrap!important;box-shadow:none!important;transform:none!important}
#xz-nav button:hover{background:rgba(255,255,255,.13)!important}
#xz-menu{box-sizing:border-box!important;position:fixed!important;z-index:1002!important;top:76px!important;right:clamp(18px,4.5vw,72px)!important;width:min(360px,calc(100vw - 36px))!important;max-height:calc(100vh - 80px)!important;overflow:auto!important;padding:18px!important;background:#fffefa!important;color:#173039!important;border:1px solid #d6e0dc!important;border-radius:16px!important;box-shadow:0 20px 55px rgba(9,31,39,.25)!important;font-family:'Microsoft YaHei',system-ui,sans-serif!important}
#xz-menu[hidden]{display:none!important}#xz-menu h2{margin:0 0 8px!important;font-size:16px!important}#xz-menu a{display:block!important;padding:9px 10px!important;border-radius:8px!important;color:#173039!important;text-decoration:none!important}#xz-menu a:hover{background:#e8f2ee!important}#xz-menu small{display:block!important;color:#61777a!important;font-size:11px!important}
#xz-progress{top:68px!important;height:2px!important}
#xz-top{position:fixed!important;right:22px!important;bottom:22px!important;z-index:1000!important;width:46px!important;height:46px!important;border:0!important;border-radius:50%!important;background:#102e37!important;color:#fff!important;box-shadow:0 10px 24px rgba(9,31,39,.25)!important;opacity:0!important;pointer-events:none!important;transform:none!important}
#xz-top.visible{opacity:1!important;pointer-events:auto!important}
body{padding-top:68px!important}
body.unified-topbar-added>.topbar,body.unified-topbar-added>nav:not(#xz-nav),body.unified-topbar-added>.progress{display:none!important}
html.xz-dark-preload body{background:#0b1d24!important;color:#edf5ef!important}
@media(max-width:900px){#xz-nav{height:60px!important;padding:0 18px!important}#xz-nav .xz-links>a{display:none!important}#xz-nav .xz-brand{font-size:13px!important}#xz-nav .xz-mark{width:31px!important;height:31px!important;flex-basis:31px!important}#xz-nav button{height:36px!important;padding:0 9px!important;font-size:13px!important}#xz-menu{top:68px!important;right:12px!important}#xz-progress{top:60px!important}body{padding-top:60px!important}}
@media(prefers-reduced-motion:reduce){#xz-nav *{transition:none!important}}
</style>'''

EARLY = '''<script id="unified-theme-preload">try{if(localStorage.getItem('xz-theme')==='dark')document.documentElement.classList.add('xz-dark-preload');sessionStorage.removeItem('xz-nav-pending')}catch(e){}document.documentElement.classList.remove('xz-leaving','xz-arriving','xz-reveal')</script>'''

def rel_from(page: Path, target: str) -> str:
    return os.path.relpath(DELIVERY / target, page.parent).replace('\\', '/')

def nav_markup(page: Path) -> str:
    hrefs = [rel_from(page, p) for p in [
        '作品总入口/index.html', '任务一_数据体检/index.html',
        '任务二_百年全景/05_交互总览/index.html',
        '任务三_专题深挖/统一中文入口/index.html',
        '任务四_开放创作/index.html']]
    labels = ['01 数据体检','02 百年全景','03 专题深挖','04 洛杉矶2028']
    rel = page.relative_to(DELIVERY).as_posix()
    current = 2 if rel.startswith('任务三_') else -1
    links = ''.join(f'<a href="{hrefs[i+1]}"' + (' aria-current="page"' if i == current else '') + f'>{labels[i]}</a>' for i in range(4))
    menu = menu_markup(page)
    return f'''<nav id="xz-nav" aria-label="作品导航"><a class="xz-brand" href="{hrefs[0]}"><span class="xz-mark">晓</span><span>奥运数据观察</span></a><div class="xz-links">{links}<button type="button" id="xz-theme" aria-label="切换深色模式" title="切换深色模式">◐</button><button type="button" id="xz-menu-button" aria-expanded="false" aria-controls="xz-menu">目录 ☰</button></div></nav><div id="xz-progress"></div><aside id="xz-menu" hidden><h2>探索全部作品</h2>{menu}</aside><button type="button" id="xz-top" aria-label="返回顶部" title="返回顶部">↑</button>'''

def menu_markup(page: Path) -> str:
    targets = ['作品总入口/index.html','任务一_数据体检/index.html','任务二_百年全景/05_交互总览/index.html','任务三_专题深挖/统一中文入口/index.html','任务四_开放创作/index.html']
    labels = ['作品总入口','数据体检室','百年全景','专题深挖','洛杉矶2028']
    notes = ['四个章节，一条证据链','质量检查与统计口径','届次、性别、项目联动','口径、王朝与主场','预测与数据新闻']
    return ''.join(f'<a href="{rel_from(page,target)}">{label}<small>{note}</small></a>' for target,label,note in zip(targets,labels,notes))

JS = '''<script id="unified-topbar-script">(()=>{const d=document,menu=d.querySelector('#xz-menu'),button=d.querySelector('#xz-menu-button'),theme=d.querySelector('#xz-theme'),top=d.querySelector('#xz-top'),bar=d.querySelector('#xz-progress');if(!theme)return;const apply=dark=>{d.body.classList.toggle('xz-dark',dark);d.documentElement.classList.toggle('xz-dark-preload',dark);theme.textContent=dark?'☀':'☾';theme.setAttribute('aria-label',dark?'切换浅色模式':'切换深色模式');theme.setAttribute('title',dark?'切换浅色模式':'切换深色模式');theme.setAttribute('aria-pressed',String(dark))};let saved=false;try{saved=localStorage.getItem('xz-theme')==='dark'}catch(e){}apply(saved);theme.addEventListener('click',()=>{const dark=!d.body.classList.contains('xz-dark');apply(dark);try{localStorage.setItem('xz-theme',dark?'dark':'light')}catch(e){}});if(button&&menu){button.addEventListener('click',()=>{menu.hidden=!menu.hidden;button.setAttribute('aria-expanded',String(!menu.hidden))});d.addEventListener('keydown',e=>{if(e.key==='Escape'){menu.hidden=true;button.setAttribute('aria-expanded','false')}});d.addEventListener('click',e=>{if(!menu.hidden&&!menu.contains(e.target)&&!button.contains(e.target)){menu.hidden=true;button.setAttribute('aria-expanded','false')}})}if(top)top.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));if(bar&&top){let ticking=false;addEventListener('scroll',()=>{if(ticking)return;ticking=true;requestAnimationFrame(()=>{const max=d.documentElement.scrollHeight-innerHeight;bar.style.width=(max>0?scrollY/max*100:0)+'%';top.classList.toggle('visible',scrollY>420);ticking=false})},{passive:true})}})();</script>'''

for page in DELIVERY.rglob('index.html'):
    source = page.read_text(encoding='utf-8')
    source = re.sub(re.escape(START) + r'.*?' + re.escape(END), '', source, flags=re.S)
    source = re.sub(r'<script id="unified-topbar-script">.*?</script>', '', source, flags=re.S)
    # frontends_refresh also emits an older nav controller. Keeping both makes
    # the theme click toggle twice and cancel itself, including on Task 4.
    source = re.sub(r'<script id="xz-ui-script">.*?</script>', '', source, flags=re.S)
    missing = 'id="xz-nav"' not in source
    source = re.sub(r'(<aside id="xz-menu"[^>]*>).*?(</aside>)', lambda m: m.group(1) + '<h2>探索全部作品</h2>' + menu_markup(page) + m.group(2), source, count=1, flags=re.S)
    if missing:
        source = re.sub(r'<body\b([^>]*)>', lambda m: '<body' + m.group(1).rstrip() + ' class="' + (re.search(r'class="([^"]*)"', m.group(1)).group(1) + ' ' if re.search(r'class="([^"]*)"', m.group(1)) else '') + 'unified-topbar-added">' if 'class=' not in m.group(1) else m.group(0).replace('class="', 'class="unified-topbar-added ', 1), source, count=1)
        source = re.sub(r'(<body\b[^>]*>)', lambda m: m.group(1) + nav_markup(page), source, count=1)
    source = source.replace('</body>', JS + '</body>', 1)
    # Preload locally stored hero photography before the page's full stylesheet parses.
    photo = re.search(r'url\([\"\']?([^\)\"\']+\.jpg)', source)
    preload = f'<link rel="preload" as="image" href="{photo.group(1)}">' if photo and not photo.group(1).startswith('data:') else ''
    bundle = START + EARLY + preload + CSS + END
    source = source.replace('</head>', bundle + '</head>', 1)
    page.write_text(source, encoding='utf-8')
    print(page.relative_to(DELIVERY), 'added' if missing else 'styled')
