from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit,unquote
import json
root=Path(__file__).resolve().parents[2];bad=[];count=0
for p in (root/'交付文件/最终提交材料').rglob('*.html'):
 count+=1
 for a in BeautifulSoup(p.read_text(encoding='utf8'),'html.parser').select('a[href]'):
  u=urlsplit(a['href'])
  if not u.scheme and u.path and not (p.parent/unquote(u.path)).exists():bad.append({'page':str(p.relative_to(root)),'href':a['href']})
report={'pages':count,'missing_local_links':bad,'scope':'最终提交材料HTML中的本地a[href]文件存在性；未测试远程链接和压缩包内部'}
(root/'项目工作区/最终材料链接核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report,ensure_ascii=False))
