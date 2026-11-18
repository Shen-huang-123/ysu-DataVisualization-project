"""Blend authored statistical chart surfaces with page themes; never alter source assets."""
from pathlib import Path
from urllib.parse import unquote
import json,os
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2];delivery=root/'交付文件';records=[]
exclude=('原始页面','99_旧','媒体','模板')
for page in delivery.rglob('*.html'):
 if any(x in str(page.relative_to(delivery)) for x in exclude):continue
 text=page.read_text(encoding='utf-8');s=BeautifulSoup(text,'html.parser');images=[]
 if not s.head:continue
 for img in s.select('img[src]'):
  f=(page.parent/unquote(img['src'])).resolve()
  # Only local authored PNG charts. Source screenshots and photographic evidence remain exact.
  if f.suffix.lower()!='.png' or not f.exists() or not f.is_relative_to(delivery.resolve()):continue
  if any(x in str(f) for x in ['媒体','海报','证据链','截图','原始页面','99_旧']):continue
  classes=img.get('class',[])
  if 'chart-surface' not in classes:img['class']=classes+['chart-surface']
  images.append(img['src'])
 if not images:continue
 if not s.select_one('#chart-surface-theme'):
  link=s.new_tag('link',id='chart-surface-theme',rel='stylesheet',href=os.path.relpath(delivery/'共享组件/chart-surface.css',page.parent).replace('\\','/'));s.head.append(link)
 updated=str(s)
 if updated!=text:page.write_text(updated,encoding='utf-8')
 records.append({'page':str(page.relative_to(delivery)).replace('\\','/'),'images':images})
(delivery/'最终提交材料/网页统计图主题融合清单.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Themed chart surfaces:',len(records),'pages,',sum(len(x['images']) for x in records),'instances')
