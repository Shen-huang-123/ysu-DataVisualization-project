"""Fetch credited Wikimedia Commons photographs for the offline Task-3 pages."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from html import unescape
import json, re, io, time
from urllib.error import HTTPError
from PIL import Image

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'交付文件'/'任务三_专题深挖'/'媒体'
OUT.mkdir(parents=True,exist_ok=True)
FILES={
 'host':"Birdsclosing.jpg",
 'lens':"Olympic Games Paris.jpg",
 'archive':"People on opening ceremony on 1980 Summer Olympics.jpg",
 'islands':"Torcida fijiana em partida de rugby sevens nos Jogos Rio 2016.jpg",
 'growth':"Athens 1896-Pan-Athenian stadium.jpg",
 'portrait':"Paavo Nurmi (Paris 1924).jpg",
 'dynasty':"1924 Summer Olympics Cross Country Nurmi.jpg",
 'women':"Tennis women 1900.jpg",
 'museum':"Polo 1900.jpg",
 'sports':"2024 Swimming at the 2024 Summer Olympics - 2024-07-27 - 1.jpg",
 'la':"Olympic Torch Tower of the Los Angeles Coliseum.jpg",
}
def plain(s):return re.sub('<[^>]*>','',unescape(s or '')).strip()
credits=[]
for key,name in FILES.items():
    q=urlencode({'action':'query','titles':'File:'+name,'prop':'imageinfo','iiprop':'url|extmetadata|size','iiurlwidth':1600,'format':'json'})
    req=Request('https://commons.wikimedia.org/w/api.php?'+q,headers={'User-Agent':'OlympicDataStoryStudentProject/1.0 (educational research)'})
    with urlopen(req,timeout=35) as response: data=json.load(response)
    page=next(iter(data['query']['pages'].values()))
    if 'missing' in page:raise ValueError('Commons file missing: '+name)
    info=page['imageinfo'][0];meta=info.get('extmetadata',{})
    lic=plain(meta.get('LicenseShortName',{}).get('value',''))
    author=plain(meta.get('Artist',{}).get('value',''))
    if author=='Unknown authorUnknown author':author='未知'
    if not (lic.startswith('CC ') or lic.startswith('CC0') or 'public domain' in lic.lower() or lic in ('PD','PDM')):
        raise ValueError(f'License not accepted for {name}: {lic}')
    url=info.get('thumburl',info['url'])
    path=OUT/(key+'.jpg')
    if path.exists():
        img=Image.open(path)
    else:
        req=Request(url,headers={'User-Agent':'Mozilla/5.0 (educational research)'})
        for attempt in range(4):
            try:
                with urlopen(req,timeout=50) as response: raw=response.read()
                break
            except HTTPError as exc:
                if exc.code!=429 or attempt==3:raise
                time.sleep(5*(attempt+1))
        img=Image.open(io.BytesIO(raw)).convert('RGB')
        if img.width>1600:
            img.thumbnail((1600,1600),Image.Resampling.LANCZOS)
        img.save(path,'JPEG',quality=88,optimize=True,progressive=True)
    credits.append({'key':key,'file':path.name,'title':name,'author':author,'license':lic,'source':info['descriptionurl'],'width':img.width,'height':img.height})
    print(key,img.size,lic,author[:80])
    time.sleep(2)
(OUT/'图片来源与许可.json').write_text(json.dumps(credits,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 专题照片来源与许可','','适合浏览器阅读的版本：[打开摄影来源画廊](图片来源与许可.html)。本文件是可下载、可检索的原始清单。','','图片均下载自 Wikimedia Commons 并保存在本目录，以便离线打开页面。照片仅作历史与运动场景配图，不作为统计数据的证据。','']
for c in credits:
    lines.append(f"- **{c['file']}**：[{c['title']}]({c['source']})；作者：{c['author'] or '见原页面'}；许可：{c['license']}。")
(OUT/'图片来源与许可.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
