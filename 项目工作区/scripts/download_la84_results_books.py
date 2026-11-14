"""Download and verify LA84-hosted OCOG results books for 2008/2012.

Idempotent; downloads to .part, validates PDF and moves into place. Books are
contemporaneous results only and must not be labelled current IOC results.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import hashlib
import re
import requests
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'资料文件'/'外部核验'/'官方成绩册索引'
BOOKS=OUT/'北京2008_伦敦2012_原始PDF'
BOOKS.mkdir(parents=True,exist_ok=True)
inventory=pd.read_csv(OUT/'北京2008_伦敦2012_官方分项成绩册索引.csv')
def get(row):
    year=int(row.Year); sport=re.sub(r'[^A-Za-z0-9]+','_',row.Title.split(' Official Results Book')[0]).strip('_')
    name=f'{year}_{sport}_{int(row.LA84_id)}.pdf'
    path=BOOKS/name
    error=''
    for attempt in range(3):
        try:
            if not path.exists():
                r=requests.get(row.pdf_url,timeout=(10,90))
                r.raise_for_status()
                if not r.content.startswith(b'%PDF-') or len(r.content)<1000 or len(r.content)>80_000_000:
                    raise ValueError(f'invalid PDF: {len(r.content)} bytes')
                part=path.with_suffix('.part')
                part.write_bytes(r.content)
                part.replace(path)
            raw=path.read_bytes()
            if not raw.startswith(b'%PDF-'):raise ValueError('existing file is not PDF')
            return {'Year':year,'Sport':sport,'LA84_id':int(row.LA84_id),'file':str(path.relative_to(ROOT)),
                    'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'pdf_url':row.pdf_url,'status':'PDF完整下载'}
        except Exception as e:error=str(e)
    return {'Year':year,'Sport':sport,'LA84_id':int(row.LA84_id),'file':str(path.relative_to(ROOT)),
            'bytes':0,'sha256':'','pdf_url':row.pdf_url,'status':'失败：'+error[:180]}
with ThreadPoolExecutor(max_workers=5) as pool:
    futures=[pool.submit(get,row) for row in inventory.itertuples(index=False)]
    rows=[f.result() for f in as_completed(futures)]
manifest=pd.DataFrame(rows).sort_values(['Year','Sport'])
manifest.to_csv(OUT/'官方成绩册下载校验清单.csv',index=False,encoding='utf-8-sig')
print(manifest.status.value_counts().to_dict(), 'total_MB',round(manifest.bytes.sum()/1e6,1))
