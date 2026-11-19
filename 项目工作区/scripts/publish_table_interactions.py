from pathlib import Path
from bs4 import BeautifulSoup
import os
ROOT=Path(__file__).resolve().parents[2]
for p in (ROOT/'交付文件').rglob('*.html'):
 text=p.read_text(encoding='utf-8-sig')
 if 'id="host-source-sensitivity"' not in text:continue
 soup=BeautifulSoup(text,'html.parser')
 if not soup.find('script',id='table-interactions'):
  soup.body.append(soup.new_tag('script',id='table-interactions',src=os.path.relpath(ROOT/'交付文件/共享组件/table-interactions.js',p.parent).replace(os.sep,'/')))
  p.write_text(str(soup),encoding='utf-8')
