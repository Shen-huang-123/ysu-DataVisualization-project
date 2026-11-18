from pathlib import Path
import csv
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[2]
TASK=ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力'
def rows(name):
 with (TASK/'02_数据表'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
S=rows('S2_2024逐大类剔除敏感性.csv');T=rows('S2_2024代表团剔除敏感性.csv')
x=lambda v:120+(v-.88)/.07*340
z=lambda v:730+(v+16)/27*330
parts=['<svg viewBox="0 0 1120 460" role="img" aria-label="35次逐大类剔除的Kendall相关与四个代表团名次差范围"><text x="40" y="30">剔除任一运动大类，榜单差异仍在</text><text x="620" y="30">关键代表团的方向均未反转</text>']
for v in [.88,.90,.92,.94,.95]:
 a=x(v);parts.append(f'<path d="M{a} 65V365" stroke="currentColor" opacity=".15"/><text x="{a}" y="395" text-anchor="middle">{v:.2f}</text>')
base=float(next(r for r in S if r['removed_family']=='none')['kendall_tau']);a=x(base)
parts.append(f'<path d="M{a} 65V365" stroke="#c98392" stroke-width="2"/><text x="40" y="430">未剔除：τ = {base:.3f}</text>')
sub=sorted([r for r in S if r['removed_family']!='none'],key=lambda r:float(r['kendall_tau']))
for i,r in enumerate(sub):parts.append(f'<circle cx="{x(float(r["kendall_tau"]))}" cy="{350-i*8}" r="3.5" fill="#7eafbd"><title>{r["removed_family"]}: {float(r["kendall_tau"]):.4f}</title></circle>')
for v in [-15,-10,-5,0,5,10]:
 a=z(v);parts.append(f'<path d="M{a} 65V365" stroke="currentColor" opacity=".15"/><text x="{a}" y="395" text-anchor="middle">{v}</text>')
for i,(noc,name) in enumerate([('ESP','西班牙'),('NED','荷兰'),('JPN','日本'),('UZB','乌兹别克斯坦')]):
 vals=[float(r['rank_shift_rows_minus_official']) for r in T if r['NOC']==noc and r['removed_family']!='none'];base=float(next(r for r in T if r['NOC']==noc and r['removed_family']=='none')['rank_shift_rows_minus_official']);lo,hi=min(vals),max(vals);y=100+i*75;color='#c98392' if base<0 else '#7eafbd'
 parts.append(f'<text x="705" y="{y+5}" text-anchor="end">{name}</text><path d="M{z(lo)} {y}H{z(hi)}" stroke="{color}" stroke-width="9" stroke-linecap="round"/><circle cx="{z(base)}" cy="{y}" r="6" fill="currentColor"/><text x="{z(hi)+12}" y="{y+5}">{lo:+.0f}～{hi:+.0f}</text>')
parts+=['<text x="730" y="430">名次差：运动员行 − 官方小项；负值表示上升</text></svg>']
p=TASK/'06_滚动叙事专题/index.html';s=BeautifulSoup(p.read_text('utf-8'),'html.parser');fig=s.select_one('#robustness2024 figure');img=fig.find('img') or fig.select_one('.s2-robust-chart');assert img
markup='<div class="s2-robust-chart" tabindex="0" role="region" aria-label="稳健性统计图，可横向滚动">'+''.join(parts)+'</div>';img.replace_with(BeautifulSoup(markup,'html.parser'))
p.write_text(str(s),'utf-8')
