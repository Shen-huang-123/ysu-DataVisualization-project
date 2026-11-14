"""Classify and hash-check Rio OCOG books; inventory is not medal verification."""
import hashlib,sys
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'项目工作区/.runtime'))
import pymupdf
OUT=ROOT/'资料文件/外部核验/官方成绩册索引'
d=pd.read_csv(OUT/'里约2016官方成绩册下载清单.csv')
assert len(d)==40 and not d.documentId.duplicated().any()
titles=[]
for _,r in d.iterrows():
 p=ROOT/r.file;raw=p.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==r.sha256 and raw.startswith(b'%PDF')
 pdf=pymupdf.open(p)
 head=' '.join(pdf[i].get_text().replace('\n',' ') for i in range(min(2,len(pdf))))
 title=' '.join(head.split())[:220]
 titles.append({'documentId':r.documentId,'pages':len(pdf),'cover_text':title,'file':r.file,'url':r.url,'sha256':r.sha256})
z=pd.DataFrame(titles)
z.to_csv(OUT/'里约2016官方成绩册可读性索引.csv',index=False,encoding='utf-8-sig')
print('QA PASS:',len(z),'official PDFs,',z.pages.sum(),'pages; all SHA256 match and text extractable')
