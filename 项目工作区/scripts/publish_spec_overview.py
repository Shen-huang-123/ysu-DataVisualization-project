from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
import csv
ROOT=Path(__file__).resolve().parents[2]
folder=ROOT/'交付文件/任务三_专题深挖/11_结论稳定性地图/02_量化口径实验'
p=folder/'index.html';s=BeautifulSoup(p.read_text('utf8'),'html.parser')
s.main['class']=list(dict.fromkeys(s.main.get('class',[])+['spec-fullwidth']))
with (folder/'五个核心结论稳定性摘要.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
parts=['<section class="spec-overview" aria-label="五个核心结论预设变体检验"><h2>结论经得起多少种预设检验？</h2><p>切换统计单位、观察窗口或样本门槛，比较方向仍成立的变体数。</p><div class="spec-bars">']
for r in rows:
 ratio=float(r['仍成立比例']);parts.append(f'<div class="spec-bar-row"><span>{escape(r["结论"])}</span><div class="spec-track"><div class="spec-fill" style="width:{ratio*100:g}%"></div></div><strong>{r["仍成立数"]}/{r["变体数"]}</strong></div>')
parts.append('</div><p>变体相互关联，比例不是“结论为真”的概率。逐项规则和结果见下表。 <a href="核心结论量化稳定性.png" download>下载原图 ↓</a></p></section>')
target=s.select_one('.spec-overview') or s.main.select_one('img');assert target
target.replace_with(BeautifulSoup(''.join(parts),'html.parser'));p.write_text(str(s),'utf8')
