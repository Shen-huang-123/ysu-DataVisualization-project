from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import csv
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务三_专题深挖/11_结论稳定性地图'
with (folder/'十专题结论稳定性矩阵.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
p=folder/'index.html';s=BeautifulSoup(p.read_text('utf-8'),'html.parser')
target=s.select_one('.stability-list') or s.select_one('.hero img');assert target
parts=['<section class="stability-list" aria-label="十专题核验结果"><h2>十个直觉，核验后还能说什么？</h2><p>每条对照原判断、已有发现和推断边界。标签描述原判断的证据状态。</p><div class="stability-rows">']
for r in rows:
 status=r['状态'];tone='sensitive' if status=='口径敏感' else 'uncertain'
 topic=escape(r['专题'])
 entry=escape(r['证据入口'],quote=True)
 parts.append(f'<article class="stability-review {tone}"><div class="stability-review-origin"><span class="stability-code">{topic} · 原判断</span><h3>{escape(r["未经检验的直觉"])}</h3><span class="stability-status">{escape(status)}</span></div><div class="stability-review-result"><p><strong>{escape(r["修正后结论"])}</strong></p><p>{escape(r["最关键的交叉证据"])}</p><p class="stability-review-limit">推断边界 · {escape(r["推断边界"])}</p></div><a class="stability-review-link" href="../{entry}" aria-label="查看 {topic} 的依据">查看依据 ↗</a></article>')
parts.append('</div><p class="stability-download"><a href="十专题结论稳定性矩阵.csv" download>下载核验矩阵 CSV ↓</a> · <a href="结论稳定性地图.png" download>下载原始地图 PNG ↓</a></p></section>')
target.replace_with(BeautifulSoup(''.join(parts),'html.parser'))
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['stability-map-motion']))
link=s.select_one('#stability-map-motion-style')
if link is None:
 link=s.new_tag('link',id='stability-map-motion-style',rel='stylesheet')
 s.head.append(link)
link['href']='../../共享组件/stability-map-motion.css?v=4'
p.write_text(str(s),'utf-8')

from publish_stability_case_map import publish as publish_case_map
publish_case_map()
