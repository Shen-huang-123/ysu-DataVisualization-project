from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
p=root/'交付文件/任务三_专题深挖/S3_冠军的保质期/06_冠军王朝时间轴/index.html'
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
s.body['class']=list(dict.fromkeys(s.body.get('class',[])+['dynasty-topic']))
for ident,href in [('dynasty-topic-style','dynasty-topic.css?v=2'),('unified-selects','unified-selects.css?v=5')]:
 link=s.select_one('#'+ident)
 if not link:link=s.new_tag('link',id=ident,rel='stylesheet');s.head.append(link)
 link['href']='../../../共享组件/'+href
import pandas as pd
data=pd.read_csv(p.parent.parent/'11_历史来源敏感性/固定队列三方案复算.csv')
rows=[]
for label,(_,r) in zip(['原代理 · 固定113项','二次来源替换 · 同113项','排除未决系列 · 剩50项'],data.iterrows()):
 x=lambda v:(v+18)/22*600
 low,high,mean=[float(r[k]) for k in ['区间下限','区间上限','后减前百分点']]
 rows.append(f'<div class="dy-ci-row"><span>{label}</span><svg viewBox="0 0 600 56" role="img" aria-label="差值{mean:.2f}，区间{low:.2f}至{high:.2f}"><line x1="{x(0)}" x2="{x(0)}" y1="0" y2="56" stroke="currentColor" opacity=".35" stroke-dasharray="3 4"/><path d="M{x(low)} 20v16 M{x(low)} 28H{x(high)} M{x(high)} 20v16" fill="none" stroke="var(--金)" stroke-width="2"/><circle cx="{x(mean)}" cy="28" r="4" fill="var(--金)"/></svg><span>{mean:+.2f}<small>95%区间 [{low:+.2f}, {high:+.2f}]</small></span></div>')
markup=BeautifulSoup('<figure class="dy-ci"><figcaption>后段减早段：同队列替换结果不变，排除子队列的区间跨零</figcaption>'+''.join(rows)+'<div class="dy-ci-axis"><span>差值及区间，单位：百分点</span><span>共同横轴 −18 至 +4；虚线为零</span></div></figure>','html.parser')
old=s.select_one('.dy-ci') or s.select_one('#dynasty-source-sensitivity img')
if old:old.replace_with(markup)
for a in s.select('a[href]'):
 if '10_王朝机制与反例' in a.get('href',''):a['class']=list(dict.fromkeys(a.get('class',[])+['dy-research-link']))
p.write_text(str(s),encoding='utf-8')
