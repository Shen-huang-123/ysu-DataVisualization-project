from pathlib import Path
from bs4 import BeautifulSoup
from docx import Document
from pypdf import PdfReader
import re, csv

root=Path(__file__).resolve().parents[2]
paths=[]
for folder in ['交付文件/任务二_百年全景','交付文件/任务三_专题深挖','交付文件/任务四_开放创作','交付文件/最终提交材料']:
    base=root/folder
    paths.extend(p for p in base.rglob('*') if p.suffix.lower() in {'.html','.md','.docx','.pdf'} and '99_旧版归档' not in p.parts)
patterns=[r'现行.{0,12}(?:官方|IOC).{0,15}(?:小项|结果|授牌|奖牌)',r'(?:协会|世界泳联|世界跆拳道|国际柔联|国际举联).{0,25}(?:IOC|授牌|官方奖牌)',r'(?:2008|2012|2016).{0,35}(?:官方小项|IOC结果|官方奖牌)',r'(?:官方小项|IOC结果|IOC授牌).{0,35}(?:2008|2012|2016)']
hits=[]
for p in paths:
    try:
        if p.suffix=='.docx': text='\n'.join(x.text for x in Document(p).paragraphs)
        elif p.suffix=='.pdf': text='\n'.join(x.extract_text() or '' for x in PdfReader(p).pages)
        else:
            text=p.read_text(encoding='utf-8')
            if p.suffix=='.html': text=BeautifulSoup(text,'html.parser').get_text(' ',strip=True)
        text=re.sub(r'\s+',' ',text)
        for pat in patterns:
            for m in re.finditer(pat,text,re.I):
                hits.append([str(p.relative_to(root)),pat,text[max(0,m.start()-70):m.end()+90]])
    except Exception as e: hits.append([str(p.relative_to(root)),'READ_ERROR',str(e)])
out=root/'项目工作区/证据措辞候选清单.csv'
with out.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['文件','规则','上下文']);w.writerows(hits)
print('files',len(paths),'candidate hits',len(hits),'out',out)
for h in hits[:40]:print(h[0],h[2][:180])
