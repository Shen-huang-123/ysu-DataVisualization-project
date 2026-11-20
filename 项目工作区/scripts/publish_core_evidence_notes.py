from pathlib import Path
from bs4 import BeautifulSoup
root=Path(__file__).resolve().parents[2]
items=[('S2_口径的魔力/07_口径实验室/index.html','main .scroll table','rule-evidence-caption','2024年同届结果；按金牌分降序，同分并列最小名次。α=0仅代表官方小项金牌计数，不采用银牌、铜牌破同分，不能视为官方完整奖牌榜。'),('S3_冠军的保质期/07_王朝生存图/index.html','#curve','survival-evidence-caption','横轴：连续控制届数；纵轴：观察性生存估计。筛选按王朝首次夺冠年份；2016年仍延续者右删失。该图描述已观察到的代表团小项控制段，不是个人冠军寿命。'),('S3_冠军的保质期/07_王朝生存图/index.html','#dynasty-source-sensitivity','source-sample-caption','与上方生存图区分：本节比较固定113个连续小项在早段1964—1976与后段1996—2016的卫冕率差；排除方案仅余50项。两图的样本及指标不同。')]
for rel,target,ident,text in items:
 p=root/'交付文件/任务三_专题深挖'/rel;s=BeautifulSoup(p.read_text(encoding='utf8'),'html.parser');el=s.select_one(target)
 if not el:continue
 note=s.find(id=ident)
 if not note:
  note=s.new_tag('p',id=ident,attrs={'class':'evidence-reading-note'})
  if el.name=='table':el.parent.insert_before(note)
  elif ident=='source-sample-caption':el.insert(1,note)
  else:el.parent.insert_after(note)
 note.string=text
 style=s.select_one('#evidence-reading-note-style')
 if not style:style=s.new_tag('style',id='evidence-reading-note-style');s.head.append(style)
 style.string='.evidence-reading-note{font:400 14px/1.9 "Microsoft YaHei",sans-serif!important;color:var(--muted,#52666b)!important;margin:16px 0!important;max-width:100%!important}body.xz-dark .evidence-reading-note{color:#c0d0d4!important}'
 p.write_text(str(s),encoding='utf8')
