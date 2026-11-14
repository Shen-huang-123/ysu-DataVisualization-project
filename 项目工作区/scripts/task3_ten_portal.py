from pathlib import Path
import re

root = Path(__file__).resolve().parents[2]
file = root/'交付文件'/'任务三_专题深挖'/'统一中文入口'/'index.html'
s = file.read_text(encoding='utf-8')
topics = [
 ('S1','东道主效应','主场优势是否超出原有趋势？','../S1_东道主效应/index.html','#126c80'),
 ('S2','口径的魔力','官方小项、均分与运动员行三种奖牌秩序。','../S2_口径的魔力/06_滚动叙事专题/index.html','#b87440'),
 ('S3','缺席的代表团','抵制潮与历史代表团身份。','../S3_地缘政治的投影/index.html','#4d587c'),
 ('S4','小队伍的大突破','把镜头转向小代表团。','../S4_小代表团的大突破/index.html','#237d66'),
 ('S5','奖牌变多了','百年奥运规模与机会扩张。','../S5_奖牌的通货膨胀/index.html','#9b5e63'),
 ('S6','名字背后的传奇','谨慎核验不可靠的运动员姓名。','../S6_王者与传奇/index.html','#846636'),
 ('S7','冠军的保质期','冠军王朝和优势寿命。','../S3_冠军的保质期/06_冠军王朝时间轴/index.html','#618c9b'),
 ('S8','领奖台上的她们','女性获奖记录的百年变化。','../S8_她们登上领奖台/index.html','#b46992'),
 ('S9','消失的赛场','体育大类的出现与退出线索。','../S9_消失的赛场/index.html','#728947'),
 ('S10','奖牌藏在哪些项目','体育大类中的机会结构。','../S10_奖牌藏在哪些项目/index.html','#2c8ba7'),
]
cards=''.join(f'<a class="ten-card" href="{href}" style="--tone:{color}"><span>{code}</span><h3>{name}</h3><p>{summary}</p><b>进入专题 ↗</b></a>' for code,name,summary,href,color in topics)
section='<section class="ten-section"><div class="ten-kicker">六个赛题方向 · 四个自拟专题</div><h2>十个问题，十种读法</h2><p class="ten-intro">每个专题都有独立页面、交互图表和口径说明。第一次看，建议从 S2「口径的魔力」开始，再按兴趣选择其他方向。</p><div class="ten-grid">'+cards+'</div></section>'
css='<style id="ten-style">.ten-section{padding:8vh 7vw;background:#f7f5ef}.ten-kicker{font-weight:800;letter-spacing:.17em;color:#a66b3c}.ten-section h2{font-size:clamp(40px,6vw,80px);margin:.15em 0}.ten-intro{max-width:800px;font-size:19px;line-height:1.8}.ten-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:40px}.ten-card{background:#fff;min-height:240px;padding:28px 32px;text-decoration:none;color:#19343d;border-top:8px solid var(--tone);transition:transform .2s,box-shadow .2s}.ten-card:hover{transform:translateY(-5px);box-shadow:0 20px 40px #16313b22}.ten-card span{font-size:14px;font-weight:900;color:var(--tone);letter-spacing:.15em}.ten-card h3{font-size:29px;margin:15px 0 6px}.ten-card p{line-height:1.7}.ten-card b{color:var(--tone)}@media(max-width:700px){.ten-grid{grid-template-columns:1fr}}</style>'
if 'id="ten-style"' not in s:
    s=s.replace('</head>',css+'</head>')
    s=s.replace('<section class="顺序">',section+'<section class="顺序">',1)
s=re.sub(r'<section class="主体 推荐">.*?</section>','',s,count=1,flags=re.S)
s=re.sub(r'<section class="顺序">.*?</section>','',s,count=1,flags=re.S)
s=re.sub(r'<section class="ten-section">.*?</section>',section,s,count=1,flags=re.S)
s=s.replace('三种视角，回答三个常被忽略的问题：统计口径如何塑造排名？冠军优势能维持多久？主场是否真的带来额外收益？','从六个赛题方向出发，再用四个自拟视角追问：谁缺席、谁突破、机会怎样变化，以及我们究竟能从记录里读出什么。')
s=s.replace('<b>3</b>个专题','<b>10</b>个专题')
s=s.replace('SIX GIVEN · FOUR ORIGINAL','六个赛题方向 · 四个自拟专题')
s=s.replace('全部页面均可离线打开；双击任务三“一键运行”文件可重新生成统计表、图表、专题网页和PDF。','全部专题页面均可离线打开；新增七页可由 task3_ten_topics.py 重新生成。')
file.write_text(s,encoding='utf-8')
print(file)
