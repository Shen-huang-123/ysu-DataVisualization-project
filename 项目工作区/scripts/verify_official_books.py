from pathlib import Path
import sys
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'资料文件'/'外部核验'/'官方成绩册索引'
manifest=pd.read_csv(OUT/'官方成绩册下载校验清单.csv')
sys.path.insert(0,str(ROOT/'项目工作区'/'.runtime'))
import pymupdf

rows=[]
for r in manifest.itertuples(index=False):
    doc=pymupdf.open(ROOT/r.file)
    first=doc[0].get_text()
    sample=''.join(doc[i].get_text() for i in range(min(5,len(doc))))
    rows.append({'Year':r.Year,'Sport':r.Sport,'LA84_id':r.LA84_id,'pages':len(doc),
                 'first_page_text_chars':len(first),'first_five_text_chars':len(sample),
                 'ocog_named':bool('Organising Committee' in sample or 'Beijing' in sample),
                 'sha256':r.sha256,'file':r.file})
z=pd.DataFrame(rows).sort_values(['Year','Sport'])
assert len(z)==74 and z.pages.min()>0
z.to_csv(OUT/'74份PDF可读性检查.csv',index=False,encoding='utf-8-sig')
print('books',len(z),'pages',z.pages.sum(),'first five text chars min',z.first_five_text_chars.min(),'no text books',int(z.first_five_text_chars.eq(0).sum()))
