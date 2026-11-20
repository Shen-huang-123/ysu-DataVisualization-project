"""Keep generic light headers from overriding photographic chapter heroes."""
from evidence_guard import presentation_html
from pathlib import Path

root=Path(__file__).resolve().parents[2]
source=root/'项目工作区/scripts/frontends_refresh.py'
pages=[p for p in presentation_html(root/'交付文件') if 'header:not(#xz-nav)' in p.read_text(encoding='utf-8')]
old='header:not(#xz-nav)'
new='header:not(#xz-nav):not(.hero):not(.photo-editorial-hero)'
for p in [source,*pages]:
    text=p.read_text(encoding='utf-8')
    count=text.count(old)
    if count:
        p.write_text(text.replace(old,new),encoding='utf-8')
        print('scoped',p.relative_to(root),count)
