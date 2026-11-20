from evidence_guard import presentation_html
from pathlib import Path
from bs4 import BeautifulSoup
import os
ROOT=Path(__file__).resolve().parents[2]
for path in presentation_html(ROOT/'交付文件'):
    text=path.read_text(encoding='utf-8-sig'); soup=BeautifulSoup(text,'html.parser'); changed=False
    for a in soup.select('a[style]'):
        if a.find('strong') and any(c in a.get('style','').replace(' ','').lower() for c in ['background:#173b58','background:#223b','background:#213b','background:#173e54']):
            a['class']=list(dict.fromkeys(a.get('class',[])+['research-proof-link'])); changed=True
    for panel in soup.select('p[style]'):
        if 'background:#173b58' in panel.get('style','').replace(' ','').lower() and panel.find('a'):
            panel['class']=list(dict.fromkeys(panel.get('class',[])+['research-proof-link'])); changed=True
    controls=soup.find(id='xz-extra-controls')
    year=soup.find(id='year')
    if controls and year:
        section=year.find_parent('section')
        if section and controls.parent!=section: section.append(controls.extract()); changed=True
    if changed:
        css=ROOT/'交付文件/共享组件/research-proof-links.css'
        link=soup.find('link',id='research-proof-links')
        if not link:
            link=soup.new_tag('link',rel='stylesheet',id='research-proof-links',href=os.path.relpath(css,path.parent).replace(os.sep,'/'));soup.head.append(link)
        path.write_text(str(soup),encoding='utf-8')

