from pathlib import Path
import markdown
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / '交付文件/最终提交材料/证据等级与历史反例'
SOURCE = '../../任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/'
REPORT = SOURCE + 'Olympedia独立交叉核验/双来源核验报告.md'
CASES = {
    'k1': '皮划艇男子 K1 1000 米',
    'fencing': '击剑男子个人佩剑',
    'pentathlon': '现代五项女子个人',
    'shooting': '射击女子飞碟多向',
    'triathlon': '铁人三项男子奥运距离',
    'c1': '皮划艇男子 C1 200 米',
    'lifting': '举重男子 69 公斤级',
}

READING_STYLE = '''
:root{color-scheme:light dark}body{background:#f7f5ef;color:#17333a;font:16px/1.8 system-ui,sans-serif;margin:auto;max-width:56rem;padding:24px}a{color:#17656f;text-underline-offset:4px}section{border-top:1px solid #758b8b55;padding:1rem 0;scroll-margin-top:1rem}h2{font-size:1.25rem}section:target h2{color:#866124}nav{display:flex;flex-wrap:wrap;gap:8px 20px}@media(prefers-color-scheme:dark){body{background:#152129;color:#e8efec}a{color:#b8dedb}section:target h2{color:#ddc393}}
'''

def publish_full_report():
    source = PAGE / REPORT
    body = markdown.markdown(source.read_text(encoding='utf-8'), extensions=['tables'])
    document = BeautifulSoup(body, 'html.parser')
    title = document.h1.get_text()
    for table in document.find_all('table'):
        wrapper = document.new_tag('div', attrs={'class': 'table-scroll', 'tabindex': '0',
                                                  'role': 'region', 'aria-label': '七处差异及裁定表'})
        table.wrap(wrapper)
    delivery = '../../../../'
    shared = delivery + '共享组件/'
    tasks = (
        ('数据体检', '任务一_数据体检/index.html'),
        ('百年全景', '任务二_百年全景/05_交互总览/index.html'),
        ('专题深挖', '任务三_专题深挖/统一中文入口/index.html'),
        ('洛杉矶2028', '任务四_开放创作/index.html'),
    )
    task_links = []
    menu_links = []
    for number, (label, path) in enumerate(tasks, 1):
        current = ' aria-current="page"' if number == 3 else ''
        href = delivery + path
        task_links.append(f'<a href="{href}"{current}>{number:02} {label}</a>')
        menu_links.append(f'<a href="{href}">{label}</a>')
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{shared}supplement-reading.css?v=1">
<link rel="stylesheet" href="{shared}integrated-nav.css?v=9">
<script>try{{document.documentElement.dataset.suppTheme=localStorage.getItem('xz-theme')==='dark'?'dark':'light'}}catch(e){{}}</script>
<script defer src="{shared}supplement-reading.js"></script>
<script defer src="{shared}integrated-nav.js"></script>
<style>{READING_STYLE}
body.supplement-reading{{margin-inline:auto}}
#xz-nav{{flex-wrap:nowrap}}
.table-scroll{{overflow:auto}}
table{{border-collapse:collapse;min-width:42rem}}
th,td{{padding:.7rem;text-align:left;vertical-align:top;border-bottom:1px solid #758b8b55}}
code{{overflow-wrap:anywhere}}
</style>
</head>
<body class="supplement-reading supp-existing-nav">
<nav id="xz-nav" aria-label="作品导航">
<a class="xz-brand" href="{delivery}../index.html"><span class="xz-mark">晓</span><span>奥运数据观察</span></a>
<div class="xz-links">
{''.join(task_links)}
<button id="xz-theme" type="button" data-supp-theme aria-pressed="false" aria-label="切换深浅主题">◐</button>
<button id="xz-menu-button" type="button" aria-controls="xz-menu" aria-expanded="false">目录 ☰</button>
</div>
</nav>
<aside id="xz-menu" aria-label="作品目录" hidden><h2>探索全部作品</h2>{''.join(menu_links)}</aside>
<nav aria-label="报告下载">
<a href="双来源核验报告.md" download>下载 Markdown 原件</a>
<a href="历史555项独立交叉对照.csv" download>下载 555 项对照表</a>
</nav>
<main>{document}</main>
</body>
</html>
"""
    source.with_suffix('.html').write_text(html, encoding='utf-8')


def main():
    publish_full_report()
    source = (PAGE / REPORT).read_text(encoding='utf-8')
    table = source.split('## 七处差异及裁定', 1)[1].split('## 证据边界', 1)[0]
    rendered = BeautifulSoup(markdown.markdown(table.strip(), extensions=['tables']), 'html.parser')
    sections = {}
    for row in rendered.select('tbody tr'):
        name, difference, evidence = row.select('td')
        key = next(key for key, label in CASES.items() if label in name.get_text())
        heading = str(name.get_text())
        sections[key] = f'<section id="{key}"><h2>{heading}</h2><p>{difference.decode_contents()}</p><p>{evidence.decode_contents()}</p></section>'
    assert sections.keys() == CASES.keys()
    source_links = f'<a href="{REPORT}" download>下载 Markdown 原文</a> · <a href="{SOURCE}证据链修复_20261120/index.html">当前证据台账</a>'
    overview = BeautifulSoup((PAGE / 'index.html').read_text(encoding='utf-8'), 'html.parser')
    cards = {card.h3.get_text(strip=True): card.a for card in overview.select('.cases .case')}
    assert cards.keys() == set(CASES.values())
    replication = (overview.select_one('.caption a[href$=".json"]')['href'])
    sections['c1'] = sections['c1'].replace('</section>', f'<p><a href="{replication}" download>下载名次复算结果</a></p></section>')
    sections['pentathlon'] = sections['pentathlon'].replace('</section>', f'<p><a href="{replication}" download>下载名次复算结果</a></p></section>')
    toc = ''.join(f'<a href="#{key}">{label}</a>' for key, label in CASES.items())
    page = f'<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>七处历史差异的证据</title><style>{READING_STYLE}</style><main><a href="index.html#cases-title">← 返回历史反例</a><h1>七处历史差异的证据</h1><p>{source_links}</p><nav aria-label="逐项证据">{toc}</nav>{"".join(sections.values())}</main></html>'
    (PAGE / '七处历史差异.html').write_text(page, encoding='utf-8')
    for key, label in CASES.items():
        cards[label]['href'] = f'七处历史差异.html#{key}'
    for a in overview.select('.caption a[href$="双来源核验报告.md"]'):
        a['href'] = '七处历史差异.html'
    (PAGE / 'index.html').write_text(str(overview), encoding='utf-8')

if __name__ == '__main__':
    main()
