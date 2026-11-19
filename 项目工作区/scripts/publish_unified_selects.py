"""Apply shared native dropdown styling to generated HTML; safe to rerun."""
from pathlib import Path
import os,re
root=Path(__file__).resolve().parents[2]
css=root/'交付文件/共享组件/unified-selects.css'
count=0
for p in [root/'index.html',*(root/'交付文件').rglob('*.html')]:
    s=p.read_text(encoding='utf-8')
    if not re.search(r'<select\b',s,re.I):continue
    href=Path(os.path.relpath(css,p.parent)).as_posix()+"?v=3"
    tag=f'<link id="unified-selects" rel="stylesheet" href="{href}">'
    s=re.sub(r'<link\b[^>]*id=["\x27]unified-selects["\x27][^>]*>','',s)
    s=re.sub(r'</head\s*>',lambda m:tag+m.group(),s,flags=re.I)
    if 'id="unified-selects"' not in s:s=tag+s
    p.write_text(s,encoding='utf-8');count+=1
print(f'Updated {count} dropdown pages')
