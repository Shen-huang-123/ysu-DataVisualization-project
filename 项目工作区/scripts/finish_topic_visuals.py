"""Remove giant chapter codes and keep Olympic ornament clear of S2 data."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[2]/'交付文件/任务三_专题深挖'
for p in root.glob('S*/index.html'):
    s=p.read_text(encoding='utf-8')
    if not re.search(r'header:after\{content:["\']S\d+',s):continue
    style='<style id="topic-visual-finish">header:after{content:""!important;width:clamp(140px,20vw,330px)!important;height:clamp(140px,20vw,330px)!important;right:-4vw!important;top:-5vw!important;border:2px solid currentColor!important;border-radius:50%!important;opacity:.09!important;background:none!important;box-shadow:0 0 0 35px #ffffff09,0 0 0 70px #ffffff06!important;pointer-events:none!important}@media(max-width:700px){header:after{width:160px!important;height:160px!important;right:-70px!important;top:-75px!important;opacity:.08!important}}</style>'
    if 'topic-visual-finish' not in s:
        p.write_text(s.replace('</head>',style+'</head>'),encoding='utf-8')
        print('refined',p.parent.name)

p=root/'S2_口径的魔力/06_滚动叙事专题/index.html'
s=p.read_text(encoding='utf-8')
style='<style id="s2-hero-data-finish">body.xz-dark header.hero .lens{background:#1a363e!important;border-color:#567178!important;color:#eef5f0!important}body.xz-dark header.hero .lens small{color:#c9dcd7!important}header.hero .ed-rings-scene{top:100px!important;right:6vw!important;width:150px!important;transform:none!important;opacity:.55!important}@media(max-width:900px){header.hero .ed-rings-scene{display:none!important}}</style>'
if 's2-hero-data-finish' not in s:
    p.write_text(s.replace('</head>',style+'</head>'),encoding='utf-8')
    print('refined S2 data cards')

# Keep statistic and timeline cards legible in the dark theme.
repairs = {
    'S1_东道主效应/index.html': '<style id="dark-card-finish">body.xz-dark .s1-facts article{background:#19343c!important;border-color:#46646a!important;color:#eaf4ef!important}body.xz-dark .s1-facts strong{color:#8bdcd4!important}body.xz-dark .s1-facts span{color:#d5e3df!important}</style>',
    'S3_冠军的保质期/06_冠军王朝时间轴/index.html': '<style id="dark-card-finish">body.xz-dark .控制{background:#10252bdc!important;border:1px solid #426169!important;border-radius:18px;padding:15px!important}body.xz-dark .内容{background:#1a3840!important;border-color:#4a6870!important;color:#ecf3ee!important}body.xz-dark .年份{color:#bdcecb!important}body.xz-dark .区间{background:#36545b!important}body.xz-dark .控制 select{background:#193841!important;color:#eef5ee!important;border-color:#5c7b7e!important}</style>',
}
for name,css in repairs.items():
    page=root/name
    html=page.read_text(encoding='utf-8')
    if 'dark-card-finish' not in html:
        page.write_text(html.replace('</head>',css+'</head>'),encoding='utf-8')
        print('repaired dark cards',name)
