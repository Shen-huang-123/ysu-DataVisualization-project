"""Run after HTML generation to restore the common table stylesheet last."""
from pathlib import Path
from bs4 import BeautifulSoup
import os
base=Path(__file__).resolve().parents[2]/'交付文件'
for p in base.rglob('*.html'):
 text=p.read_text('utf8')
 if '<table' not in text.lower():continue
 s=BeautifulSoup(text,'html.parser')
 if not s.head:continue
 old=s.select_one('#unified-tables')
 if old:old.extract()
 s.head.append(s.new_tag('link',id='unified-tables',rel='stylesheet',href=Path(os.path.relpath(base/'共享组件/unified-tables.css',p.parent)).as_posix()))
 p.write_text(str(s),'utf8')
