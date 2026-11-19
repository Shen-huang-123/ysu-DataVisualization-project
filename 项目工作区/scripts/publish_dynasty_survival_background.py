from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
st=s.select_one('#dynasty-survival-background')
if not st:st=s.new_tag('style',id='dynasty-survival-background');s.head.append(st)
st.string="""
html body.ip-dynasty{--ds-bg:#f2f3ee;background:var(--ds-bg)!important;background-image:none!important}
html body.ip-dynasty.xz-dark{--ds-bg:#182128;--ink:#edf3f2;--muted:#c0d0d4;background:var(--ds-bg)!important}
html body.ip-dynasty .oa-world{display:none!important}
html body.ip-dynasty::before,html body.ip-dynasty::after{background:none!important;box-shadow:none!important}
html body.ip-dynasty header.photo-editorial-hero.image-stage::before{background:linear-gradient(0deg,var(--ds-bg),transparent 28%),linear-gradient(90deg,#07191fd9, #07191f55 58%,transparent)!important}
html body.ip-dynasty header.photo-editorial-hero:not(.image-stage){background-image:linear-gradient(0deg,var(--ds-bg),transparent 28%),linear-gradient(90deg,#07191fd9,#07191f33),url('../../媒体/dynasty.jpg')!important}
html body.ip-dynasty.xz-dark main :is(h2,h3){color:#edf3f2!important}
html body.ip-dynasty.xz-dark main .ip-eyebrow{color:#d8be89!important}
html body.ip-dynasty .photo-editorial-credit{display:block!important;width:auto!important;max-width:none!important;margin:14px 6vw 0!important;padding:8px 0!important;border:0!important;border-radius:0!important;box-shadow:none!important;background:transparent!important;color:var(--ink)!important;text-align:right;font-size:12px!important}
"""
p.write_text(str(s),encoding='utf-8')
