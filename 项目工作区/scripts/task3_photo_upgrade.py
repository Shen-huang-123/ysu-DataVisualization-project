"""Place credited photography into all ten stories, with restrained scroll motion."""
from pathlib import Path
from html import escape
import json, os

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/'交付文件'/'任务三_专题深挖'
MEDIA=BASE/'媒体'
credits={c['key']:c for c in json.loads((MEDIA/'图片来源与许可.json').read_text(encoding='utf-8'))}
PAGES=[
 ('S1_东道主效应/index.html','host','2008 年北京国家体育场闭幕式现场'),
 ('S2_口径的魔力/06_滚动叙事专题/index.html','lens','2024 年巴黎奥运会击剑比赛'),
 ('S3_地缘政治的投影/index.html','archive','1980 年莫斯科奥运会开幕式现场'),
 ('S4_小代表团的大突破/index.html','islands','2016 年里约奥运会斐济七人制橄榄球球迷'),
 ('S5_奖牌的通货膨胀/index.html','growth','1896 年雅典奥运会帕纳辛纳科体育场'),
 ('S6_王者与传奇/index.html','portrait','1924 年巴黎奥运会的帕沃·努尔米'),
 ('S3_冠军的保质期/06_冠军王朝时间轴/index.html','dynasty','1924 年巴黎奥运会越野赛跑现场'),
 ('S8_她们登上领奖台/index.html','women','1900 年巴黎奥运会女子网球比赛'),
 ('S9_消失的赛场/index.html','museum','1900 年巴黎奥运会马球比赛'),
 ('S10_奖牌藏在哪些项目/index.html','sports','2024 年巴黎奥运会游泳比赛场馆'),
]
CSS='''<style id="task3-photo-style">.photo-stage{position:relative;margin:0;min-height:430px;height:min(50vw,620px);overflow:hidden;background:#142e31;isolation:isolate}.photo-stage:after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,#071b1d14 0%,#071b1d05 35%,#071b1dbb 100%);z-index:1}.photo-stage img{width:100%;height:100%;object-fit:cover;display:block;transform:scale(1.06);will-change:transform;animation:photo-open 1.3s cubic-bezier(.2,1,.3,1) both}.photo-stage figcaption{position:absolute;bottom:0;left:0;right:0;z-index:2;color:#fff;display:flex;align-items:end;justify-content:space-between;gap:25px;padding:35px 6vw;font:13px 'Microsoft YaHei',sans-serif;text-shadow:0 1px 12px #000a}.photo-stage figcaption strong{font-size:clamp(15px,1.6vw,22px);font-weight:600;max-width:700px}.photo-stage figcaption a{color:#fff;text-decoration:none;border-bottom:1px solid #fff8;white-space:nowrap}.photo-stage figcaption a:hover{border-color:#fff}.photo-stage:before{content:'摄影档案  /  1896—2024';position:absolute;left:6vw;top:30px;z-index:2;color:#fff;font:700 12px 'Microsoft YaHei';letter-spacing:.18em;text-shadow:0 2px 10px #0008}.photo-stage.archive img,.photo-stage.growth img,.photo-stage.portrait img,.photo-stage.dynasty img,.photo-stage.women img,.photo-stage.museum img{filter:grayscale(1) contrast(1.04)}.photo-stage.archive{border-top:14px solid #d8b671;border-bottom:14px solid #d8b671}.photo-stage.islands{border-bottom:18px solid #ffb769}.photo-stage.growth img{filter:sepia(.28) contrast(1.08)}.photo-stage.portrait{max-width:1100px;margin:30px auto;box-shadow:25px 25px 0 #d4a44755}.photo-stage.portrait img{object-position:center 32%}.photo-stage.editorial,.photo-stage.women{border-left:18px solid #e58bb8}.photo-stage.museum{border:20px solid #dbd7b9;box-shadow:inset 0 0 0 5px #fff}.photo-stage.sports img{object-position:center 55%}.photo-stage.lens{border-top:10px solid #c29b52}.photo-stage.host{border-top:10px solid #0f7485}@keyframes photo-open{from{opacity:.45;transform:scale(1.17)}to{opacity:1;transform:scale(1.06)}}@media(max-width:700px){.photo-stage{height:330px;min-height:330px}.photo-stage figcaption{display:block;padding:23px 5vw}.photo-stage figcaption a{display:inline-block;margin-top:9px}.photo-stage.portrait{margin:15px}.photo-stage:before{top:20px;left:5vw;font-size:10px}}@media(prefers-reduced-motion:reduce){.photo-stage img{animation:none!important;transform:none!important;will-change:auto}}</style>'''
JS='''<script id="task3-photo-motion">(()=>{if(matchMedia('(prefers-reduced-motion: reduce)').matches)return;const f=document.querySelector('.photo-stage'),img=f?.querySelector('img');if(!f||!img)return;let waiting=false;function move(){if(waiting)return;waiting=true;requestAnimationFrame(()=>{const r=f.getBoundingClientRect(),v=(innerHeight-r.top)/(innerHeight+r.height),offset=(Math.max(0,Math.min(1,v))-.5)*24;img.style.transform=`translate3d(0,${offset}px,0) scale(1.08)`;waiting=false})}addEventListener('scroll',move,{passive:true});move()})();</script>'''
for rel,key,caption in PAGES:
    file=BASE/rel
    s=file.read_text(encoding='utf-8')
    for marker,close in [('<style id="task3-photo-style">','</style>'),('<script id="task3-photo-motion">','</script>'),('<figure class="photo-stage','</figure>')]:
        start=s.find(marker)
        if start>=0:
            end=s.find(close,start)+len(close)
            s=s[:start]+s[end:]
    relative=os.path.relpath(MEDIA/(key+'.jpg'),file.parent).replace('\\','/')
    credit=credits[key]
    photo=f'<figure class="photo-stage {key}"><img src="{escape(relative)}" alt="{escape(caption)}" loading="eager"><figcaption><strong>{escape(caption)} <small>· 场景配图，不作为统计证据</small></strong><a href="{escape(credit["source"])}" target="_blank" rel="noopener">图源与许可：{escape(credit["license"])} ↗</a></figcaption></figure>'
    s=s.replace('</head>',CSS+'</head>',1)
    if '</header>' not in s:raise ValueError('No header: '+str(file))
    s=s.replace('</header>','</header>'+photo,1)
    s=s.replace('</body>',JS+'</body>',1)
    file.write_text(s,encoding='utf-8')
print('Added',len(PAGES),'credited photo scenes')

# Restore S8 task-page presentation after generating content.
import runpy
runpy.run_path(str(Path(__file__).with_name("publish_women_topic_style.py")))

# Restore S9 photo and layout after general photo upgrades.
import runpy
runpy.run_path(str(Path(__file__).with_name('publish_vanished_topic_style.py')))
