"""Discover and preserve Rio 2016 OCOG official result books from Olympic World Library."""
import concurrent.futures as cf
import hashlib,re,urllib.parse
from pathlib import Path
import pandas as pd,requests

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'资料文件/外部核验/官方成绩册索引/里约2016_原始PDF';OUT.mkdir(parents=True,exist_ok=True)
BASE='https://library.olympics.com/digitalCollection/DigitalCollectionAttachmentDownloadHandler.ashx?documentId={}&parentDocumentId=165312&skipCopyright=true&skipWatermark=true'

def fetch(i):
 try:
  s=requests.Session();u=BASE.format(i)
  for _ in range(3):
   r=s.get(u,timeout=35)
   m=re.search("window.location.href='([^']+)'",r.text[:600]) if r.headers.get('content-type','').startswith('text/html') else None
   if not m:break
   u=urllib.parse.urljoin(r.url,m.group(1))
  if not r.content.startswith(b'%PDF'):return None
  p=OUT/f'2016_{i}.pdf';p.write_bytes(r.content)
  return {'documentId':i,'file':str(p.relative_to(ROOT)),'bytes':len(r.content),'sha256':hashlib.sha256(r.content).hexdigest(),'url':BASE.format(i)}
 except Exception as e:return {'documentId':i,'error':str(e)[:120]}

if __name__=='__main__':
 with cf.ThreadPoolExecutor(max_workers=5) as pool:rows=list(pool.map(fetch,range(165313,165381)))
 d=pd.DataFrame([x for x in rows if x and 'file' in x])
 d.to_csv(OUT.parent/'里约2016官方成绩册下载清单.csv',index=False,encoding='utf-8-sig')
 print('PDF',len(d),'MB',round(d.bytes.sum()/1e6,1),'errors',[x for x in rows if x and 'error' in x][:5])
