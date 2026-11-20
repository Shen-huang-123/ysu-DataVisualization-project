from evidence_guard import presentation_html
from pathlib import Path
from bs4 import BeautifulSoup
import os
ROOT=Path(__file__).resolve().parents[2]
for p in presentation_html(ROOT/'交付文件'):
 text=p.read_text(encoding='utf-8-sig')
 if '<table' not in text.lower():continue
 soup=BeautifulSoup(text,'html.parser')
 if not soup.find('script',id='table-interactions'):
  soup.body.append(soup.new_tag('script',id='table-interactions',src=os.path.relpath(ROOT/'交付文件/共享组件/table-interactions.js',p.parent).replace(os.sep,'/')))
  p.write_text(str(soup),encoding='utf-8')

