"""Refresh the existing styled browser report from its Markdown source."""
from pathlib import Path
from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parents[2]
DIR=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/01_报告与说明'
md=DIR/'S2_口径的魔力_高分版.md'
html=DIR/'S2_口径的魔力_高分版.html'
soup=BeautifulSoup(html.read_text(encoding='utf-8'),'html.parser')
main=soup.find('main',class_='article')
assert main is not None
main.clear()
fragment=BeautifulSoup(MarkdownIt('commonmark').render(md.read_text(encoding='utf-8')),'html.parser')
for child in list(fragment.contents):main.append(child)
html.write_text(str(soup),encoding='utf-8')
print(html)
