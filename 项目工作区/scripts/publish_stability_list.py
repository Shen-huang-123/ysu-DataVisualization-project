from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import csv
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务三_专题深挖/11_结论稳定性地图'
with (folder/'十专题结论稳定性矩阵.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
p=folder/'index.html';s=BeautifulSoup(p.read_text('utf-8'),'html.parser')
target=s.select_one('.stability-list') or s.select_one('.hero img');assert target
parts=['<section class="stability-list" aria-label="十专题证据分类"><h2>十个直觉，经得起几次换口径？</h2><p>口径敏感：结论随统计单位或纳入规则改变。证据不足：当前数据不足以验证推断。</p><div class="stability-rows">']
for r in rows:
 status=r['状态'];tone='sensitive' if status=='口径敏感' else 'uncertain'
 parts.append(f'<a class="stability-row {tone}" href="../{escape(r["证据入口"],quote=True)}"><span class="stability-code">{escape(r["专题"])}</span><span>{escape(r["未经检验的直觉"])}</span><span class="stability-status">{escape(status)} <span aria-hidden="true">↗</span></span></a>')
parts.append('</div><p class="stability-download"><a href="结论稳定性地图.png" download>下载原始地图 PNG ↓</a> · 分类是证据状态，不是专题质量评分。</p></section>')
target.replace_with(BeautifulSoup(''.join(parts),'html.parser'))
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['stability-map-motion']))
link=s.select_one('#stability-map-motion-style')
if link is None:
 link=s.new_tag('link',id='stability-map-motion-style',rel='stylesheet')
 s.head.append(link)
link['href']='../../共享组件/stability-map-motion.css?v=1'
p.write_text(str(s),'utf-8')
