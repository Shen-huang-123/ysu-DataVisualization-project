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
    return_url = '../../../../../index.html'
    html = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{READING_STYLE}
.table-scroll{{overflow:auto}}
table{{border-collapse:collapse;min-width:42rem}}
th,td{{padding:.7rem;text-align:left;vertical-align:top;border-bottom:1px solid #758b8b55}}
code{{overflow-wrap:anywhere}}
</style>
</head>
<body>
<nav aria-label="报告导航">
<a href="{return_url}">← 作品首页</a>
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
