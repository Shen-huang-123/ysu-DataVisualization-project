"""Apply the panorama reading layout after generating the Markdown companion."""
from html import escape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / '交付文件/任务二_百年全景/01_报告与说明/01_百年奥运全景分析_高分版.html'
STYLE = """
.panorama-reading .head { background:transparent!important; padding-block:clamp(20px,4vw,48px)!important }
.panorama-reading .head small { color:var(--sr-accent,#88662e) }
.panorama-reading .head h1 { margin-block:8px 14px }
.panorama-reading .layout { align-items:start; padding-top:clamp(16px,3vw,34px) }
.panorama-reading .article { padding:clamp(18px,4vw,52px); box-shadow:none }
.panorama-reading .article h1 { font-size:clamp(24px,3.3vw,44px)!important }
.panorama-reading .article h2 { scroll-margin-top:88px }
.panorama-reading .article h2:target { color:var(--sr-accent,#88662e)!important }
.panorama-reading .article .formal-entry { margin:22px 0!important; padding:14px 0!important }
.panorama-reading .article .formal-entry h2 { margin:4px 0!important; border:0 }
.panorama-reading .chapter-nav { display:flex; flex-wrap:wrap; gap:6px 18px; margin-top:22px; padding-block:10px; border-block:1px solid var(--sr-line,#758b8b55) }
.panorama-reading .chapter-nav a { font-weight:600 }
.panorama-reading .article p { max-width:76ch }
"""

def main():
    raw = PAGE.read_bytes()
    if b'id="panorama-reading-style"' in raw:
        return
    text = raw.decode('utf-8')
    text = re.sub(r'<body([^>]*)class="([^"]*)"',r'<body\1class="\2 panorama-reading"',text,count=1)
    text = text.replace('</head>',f'<style id="panorama-reading-style">{STYLE}</style></head>',1)
    start = text.index('<main class="article">')
    end = text.index('</main>',start)
    article = text[start:end]
    chapters = iter(zip(('method','medals','teams','women','sports','conclusions','reproduce'),
                        ('研究口径','奖牌格局','代表团兴衰','女性参与','项目演化','结论','证据与复现')))
    links = []
    def anchor(match):
        key,label = next(chapters)
        links.append(f'<a href="#{key}">{escape(label)}</a>')
        return f'<h2 id="{key}">'
    article = re.sub(r'<h2>(?=0\.|[A-D]\.|结论|证据边界)',anchor,article)
    assert len(links)==7
    evidence = re.search(r'<!-- CONCENTRATION_HTML_START -->.*?<!-- CONCENTRATION_HTML_END -->',text,re.S)
    if evidence:
        article = article.replace('</h1>','</h1>'+evidence[0],1)
    text = text[:start]+article+text[end:]
    if evidence:
        text = text.replace(evidence[0],'',1)
    nav = '<nav class="chapter-nav" aria-label="报告章节">'+''.join(links)+'</nav>'
    text = text.replace('</header><div class="layout">',nav+'</header><div class="layout">',1)
    text = text.replace('RESEARCH NOTE / 浏览器阅读版','任务二 · 浏览器阅读版',1)
    PAGE.write_text(text,encoding='utf-8')


if __name__ == '__main__':
    main()
