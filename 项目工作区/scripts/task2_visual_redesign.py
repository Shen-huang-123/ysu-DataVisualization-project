"""Editorial redesign of the century overview without changing its filters/data."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[2]
PAGE=ROOT/'交付文件/任务二_百年全景/05_交互总览/index.html'
START='<!-- TASK2_REDESIGN_START -->'
END='<!-- TASK2_REDESIGN_END -->'

CSS='''<style id="task2-redesign-style">
body.task2-redesign{background:#eeeae2!important;color:#16323a!important}
body.task2-redesign header.photo-editorial-hero{background-image:linear-gradient(90deg,rgba(6,21,27,.90),rgba(8,31,39,.56) 54%,rgba(5,24,30,.13)),url('../../任务三_专题深挖/媒体/sports.jpg')!important;background-position:center,center 48%!important;padding:70px clamp(28px,7vw,110px)!important;justify-content:end!important}
body.task2-redesign header.photo-editorial-hero:after{display:none!important}
body.task2-redesign header.photo-editorial-hero h1{font-family:Georgia,'Songti SC','SimSun',serif!important;font-size:clamp(72px,8.8vw,132px)!important;letter-spacing:-.07em!important;line-height:.95!important;margin:20px 0 24px!important;max-width:800px!important}
body.task2-redesign header.photo-editorial-hero p{font-size:clamp(18px,1.5vw,23px)!important;line-height:1.65!important;max-width:640px!important;color:#e6eeea!important}
body.task2-redesign header.photo-editorial-hero:before{content:'1896  /  2024';position:absolute;right:clamp(25px,5vw,90px);bottom:60px;color:#fff;opacity:.6;font:700 16px/1 Georgia,serif;letter-spacing:.22em;z-index:2}
body.task2-redesign main.wrap{width:min(100% - 64px,1300px)!important;max-width:1300px!important;margin:0 auto!important;padding:84px 0 120px!important;display:block!important}
body.task2-redesign .t2-intro{display:grid;grid-template-columns:150px minmax(0,1fr) 370px;gap:24px;align-items:end;margin-bottom:32px;padding-bottom:24px;border-bottom:1px solid #aebcb9}
body.task2-redesign .t2-kicker{color:#aa723f;font-size:13px;font-weight:900;letter-spacing:.18em}
body.task2-redesign .t2-intro h2{font-family:Georgia,'Songti SC','SimSun',serif;font-size:clamp(38px,4vw,62px);line-height:1.1;letter-spacing:-.06em;margin:0;color:#17353d}
body.task2-redesign .t2-intro p{font-size:15px;line-height:1.65;color:#52676a;margin:0}
body.task2-redesign .cards,body.task2-redesign .cards .card,body.task2-redesign .filters{opacity:1!important;transform:none!important;visibility:visible!important}
body.task2-redesign .cards{display:grid!important;grid-template-columns:repeat(4,minmax(0,1fr))!important;gap:12px!important;margin:0 0 74px!important}
body.task2-redesign .cards .card{min-height:148px!important;display:flex;flex-direction:column;justify-content:space-between;padding:22px 24px!important;background:#fffdf8!important;border:1px solid #d2dad4!important;border-radius:18px!important;box-shadow:0 10px 25px rgba(30,62,64,.06)!important}
body.task2-redesign .cards .card:first-child{background:#123740!important;border-color:#123740!important}
body.task2-redesign .cards .card:first-child small,body.task2-redesign .cards .card:first-child .big{color:#f4f4e8!important}
body.task2-redesign .cards small{font-size:13px!important;color:#5e7071!important;font-weight:700!important;letter-spacing:.06em}
body.task2-redesign .cards .big{font:700 clamp(27px,3vw,48px)/1.05 Georgia,'Songti SC',serif!important;color:#176d78!important;letter-spacing:-.045em!important;word-break:break-word}
body.task2-redesign .t2-section-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin:0 0 20px}
body.task2-redesign .t2-section-head span{display:block;color:#a67543;font-size:12px;font-weight:900;letter-spacing:.2em;margin-bottom:8px}
body.task2-redesign .t2-section-head h2{font:600 clamp(30px,3.4vw,48px)/1.1 Georgia,'Songti SC','SimSun',serif;color:#183a42;letter-spacing:-.05em;margin:0}
body.task2-redesign .t2-section-head p{max-width:460px;margin:0;color:#587075;font-size:14px;line-height:1.6}
body.task2-redesign .filters{display:grid!important;grid-template-columns:repeat(5,minmax(0,1fr))!important;gap:13px!important;margin:0 0 78px!important;padding:27px!important;background:#dfe9e6!important;border:1px solid #cadbd6!important;border-radius:20px!important;box-shadow:none!important}
body.task2-redesign .filters .field{display:flex;flex-direction:column;gap:8px;min-width:0}
body.task2-redesign .filters label{color:#3e5f65!important;font-size:13px!important;font-weight:800!important}
body.task2-redesign .filters select{min-width:0;width:100%;height:48px;padding:0 12px;border:1px solid #afc7c2!important;border-radius:10px!important;background:#fffefa!important;color:#16343a!important}
body.task2-redesign #xz-extra-controls{grid-column:1/-1;display:flex!important;align-items:center;gap:18px;margin:7px 0 0!important;color:#557176}
body.task2-redesign #xz-reset{background:#173f48!important;color:#fff!important;border:0!important;padding:10px 16px!important;border-radius:10px!important}

html body.task2-redesign #explore-panorama-2 .actions {
 align-items:center;flex-wrap:wrap;padding-block:12px;
 border-top:1px solid var(--line);
}
html body.task2-redesign #explore-panorama-2 #title {
 color:#23434b;font:600 clamp(19px,2.1vw,30px)/1.35 'Microsoft YaHei',sans-serif;
}
html body.task2-redesign #explore-panorama-2 #download {
 display:inline-flex;align-items:center;gap:9px;min-height:44px;
 padding:7px 13px!important;border:1px solid #65818a!important;border-radius:6px!important;
 background:transparent!important;box-shadow:none!important;text-shadow:none!important;
 color:#23434b!important;font-size:14px!important;font-weight:600;
}
html body.task2-redesign #explore-panorama-2 #download::before {content:'↓';font-size:18px;line-height:1}
html body.task2-redesign #explore-panorama-2 #download:hover {background:#77939c24!important}
html body.task2-redesign #explore-panorama-2 #download:focus-visible {outline:2px solid currentColor;outline-offset:3px}
html body.task2-redesign.xz-dark #explore-panorama-2 :is(#title,#download) {color:#e8f1ee!important}
body.task2-redesign .actions{display:flex;align-items:end;justify-content:space-between;gap:16px;margin:0 0 18px!important}
body.task2-redesign .actions strong{font:600 clamp(29px,3.3vw,46px)/1.1 Georgia,'Songti SC',serif;color:#183a42}
body.task2-redesign #download{background:#173f48!important;color:white!important;padding:11px 17px!important;border:0!important;border-radius:10px!important}
body.task2-redesign .t2-chart-panel{padding:20px 18px 12px;background:#fffefa;border:1px solid #d4ded9;border-radius:20px;box-shadow:0 16px 34px rgba(25,58,62,.06);margin-bottom:78px}
body.task2-redesign #chart{display:block;width:100%!important;height:410px!important;background:transparent!important;box-shadow:none!important;overflow:visible}
body.task2-redesign .t2-chart-note{display:flex;justify-content:space-between;gap:20px;padding:13px 12px 3px;color:#65777a;font-size:12px;border-top:1px solid #e2e9e5}
body.task2-redesign .t2-table-heading{margin:0 0 20px}
body.task2-redesign .t2-table-wrap{overflow:auto;border:1px solid #d3ddd7;border-radius:18px;background:#fffefa;box-shadow:0 12px 30px rgba(27,55,59,.06)}
body.task2-redesign table{width:100%;min-width:600px;border:0!important;border-radius:0!important;box-shadow:none!important;background:transparent!important}
body.task2-redesign thead{background:#143b44!important}body.task2-redesign thead th{background:transparent!important;color:#eff8f3!important;font-size:12px!important;letter-spacing:.08em!important}
body.task2-redesign td,body.task2-redesign th{padding:14px 18px!important;border-bottom:1px solid #e0e7e2!important}
body.task2-redesign tbody tr{opacity:1!important;transform:none!important;visibility:visible!important}body.task2-redesign tbody tr:nth-child(even){background:#f4f8f4}body.task2-redesign tbody tr:hover{background:#e8f3ef!important}
body.task2-redesign .t2-axis{font:12px 'Microsoft YaHei',sans-serif;fill:#647a7b}body.task2-redesign .t2-grid{stroke:#dce5e0;stroke-width:1;stroke-dasharray:4 5}
@media(max-width:900px){body.task2-redesign .t2-intro{grid-template-columns:1fr;gap:10px}body.task2-redesign .cards{grid-template-columns:repeat(2,minmax(0,1fr))!important}body.task2-redesign .filters{grid-template-columns:repeat(2,minmax(0,1fr))!important}}
@media(max-width:700px){body.task2-redesign header.photo-editorial-hero{padding:38px 22px 54px!important;justify-content:end!important}body.task2-redesign header.photo-editorial-hero h1{font-size:clamp(52px,13vw,72px)!important;margin:14px 0!important}body.task2-redesign header.photo-editorial-hero p{font-size:16px!important;line-height:1.6!important}body.task2-redesign header.photo-editorial-hero:before{right:20px;bottom:18px;font-size:11px}body.task2-redesign main.wrap{width:calc(100% - 32px)!important;padding:54px 0 90px!important}body.task2-redesign .t2-intro h2{font-size:36px}body.task2-redesign .cards{gap:8px!important;margin-bottom:56px!important}body.task2-redesign .cards .card{min-height:120px!important;padding:16px!important}body.task2-redesign .cards .big{font-size:26px!important}body.task2-redesign .filters{gap:12px!important;padding:18px!important;margin-bottom:60px!important}body.task2-redesign .filters .field:nth-child(5){grid-column:1/-1}body.task2-redesign .t2-section-head{display:block}body.task2-redesign .t2-section-head p{margin-top:8px}body.task2-redesign .actions{align-items:center}body.task2-redesign .actions strong{font-size:28px}body.task2-redesign #download{font-size:12px!important;padding:10px!important}body.task2-redesign .t2-chart-panel{padding:8px 5px 10px;margin-bottom:56px}body.task2-redesign #chart{height:300px!important}body.task2-redesign .t2-chart-note{display:block;line-height:1.6}body.task2-redesign table{min-width:0!important;table-layout:fixed;font-size:11px!important}body.task2-redesign th,body.task2-redesign td{padding:9px 5px!important;font-size:11px!important;white-space:nowrap}body.task2-redesign th:first-child,body.task2-redesign td:first-child{width:27%;overflow:hidden;text-overflow:ellipsis}body.task2-redesign th:nth-child(2),body.task2-redesign td:nth-child(2){width:26%}body.task2-redesign th:nth-child(3),body.task2-redesign td:nth-child(3){width:24%}body.task2-redesign th:nth-child(4),body.task2-redesign td:nth-child(4){width:23%}}
</style>'''

JS='''<script id="task2-chart-redesign">(()=>{const axis=(x,y,text,anchor='start')=>`<text class="t2-axis" x="${x}" y="${y}" text-anchor="${anchor}">${text}</text>`;draw=function(a,mode){const svg=document.getElementById('chart');if(!a.length){svg.innerHTML='';return}const max=Math.max(...a.map(x=>x[1]))||1;let grid='<defs><linearGradient id="t2-area" x1="0" y1="0" x2="0" y2="1"><stop stop-color="#208c94" stop-opacity=".30"/><stop offset="1" stop-color="#208c94" stop-opacity=".01"/></linearGradient><linearGradient id="t2-bars"><stop stop-color="#1d6874"/><stop offset="1" stop-color="#48a5a3"/></linearGradient></defs>';for(let i=0;i<4;i++){let y=350-i*90;grid+=`<line class="t2-grid" x1="85" y1="${y}" x2="1040" y2="${y}"/>`+axis(72,y+4,Math.round(max*i/3).toLocaleString(),'end')}grid+='<line x1="85" y1="350" x2="1040" y2="350" stroke="#789494" stroke-width="1.2"/>';if(mode==='line'){const pts=a.map((x,i)=>[85+i*955/Math.max(1,a.length-1),350-x[1]/max*270]);const line=pts.map((p,i)=>(i?'L':'M')+p.join(',')).join(' ');const area=line+` L${pts.at(-1)[0]},350 L${pts[0][0]},350 Z`;let labels='';const step=Math.max(1,Math.ceil(a.length/8));a.forEach((x,i)=>{if(i%step===0||i===a.length-1)labels+=axis(pts[i][0],382,x[0],'middle')});svg.innerHTML=grid+`<path d="${area}" fill="url(#t2-area)"/><path d="${line}" fill="none" stroke="#166d7a" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`+pts.map((p,i)=>`<circle cx="${p[0]}" cy="${p[1]}" r="4.3" fill="#fff" stroke="#b45a62" stroke-width="2.4"><title>${a[i][0]}：${a[i][1].toLocaleString()}</title></circle>`).join('')+labels}else{const slot=955/a.length,bw=slot*.66;svg.innerHTML=grid+a.map((x,i)=>{let h=x[1]/max*270,xx=85+i*slot+slot*.17,yy=350-h;return `<rect x="${xx}" y="${yy}" width="${bw}" height="${h}" rx="4" fill="url(#t2-bars)"><title>${displayNoc(x[0])}：${x[1].toLocaleString()}</title></rect>`+axis(xx+bw/2,380,displayNoc(x[0]),'middle')}).join('')}};render()})();</script>'''
MOBILE_JS='''if(innerWidth<700){svg.setAttribute('viewBox','0 0 360 300');const peak=Math.max(...a.map(x=>x[1]))||1;let g='';for(let i=0;i<4;i++){const y=230-i*57;g+=`<line class="t2-grid" x1="42" y1="${y}" x2="340" y2="${y}"/>`+axis(37,y+4,Math.round(peak*i/3).toLocaleString(),'end')}if(mode==='line'){const pts=a.map((x,i)=>[42+i*298/Math.max(1,a.length-1),230-x[1]/peak*171]);const line=pts.map((p,i)=>(i?'L':'M')+p.join(',')).join(' ');const area=line+` L${pts.at(-1)[0]},230 L42,230 Z`;let labels='';[0,Math.floor((a.length-1)/2),a.length-1].forEach(i=>{labels+=axis(pts[i][0],254,a[i][0],'middle')});svg.innerHTML=g+`<path d="${area}" fill="#dcefeb"/><path d="${line}" fill="none" stroke="#166d7a" stroke-width="2.5" stroke-linecap="round"/>`+pts.map((p,i)=>`<circle cx="${p[0]}" cy="${p[1]}" r="2.5" fill="#ad5360"><title>${a[i][0]}：${a[i][1].toLocaleString()}</title></circle>`).join('')+labels}else{const slot=298/a.length,bw=slot*.67;svg.innerHTML=g+a.map((x,i)=>{const h=x[1]/peak*171,xx=42+i*slot+slot*.16;return `<rect x="${xx}" y="${230-h}" width="${bw}" height="${h}" rx="2" fill="#287f87"><title>${displayNoc(x[0])}：${x[1].toLocaleString()}</title></rect>`+(i%3===0?axis(xx+bw/2,252,x[0],'middle'): '')}).join('')}return}svg.setAttribute('viewBox','0 0 1100 440');'''
JS=JS.replace('const max=Math.max(...a.map(x=>x[1]))||1;let grid=',MOBILE_JS+'const max=Math.max(...a.map(x=>x[1]))||1;let grid=',1)

source=PAGE.read_text(encoding='utf-8')
source=re.sub(re.escape(START)+r'.*?'+re.escape(END),'',source,flags=re.S)
source=re.sub(r'<script id="task2-chart-redesign">.*?</script>','',source,flags=re.S)
source=source.replace('<body class="','<body class="task2-redesign ',1) if 'task2-redesign' not in re.search(r'<body[^>]*>',source).group(0) else source
pattern=r'(<main class="wrap">)(<section class="filters">.*?</section>)(<section class="cards">.*?</section>)'
match=re.search(pattern,source,flags=re.S)
fresh=match is not None
if not fresh and 'class="t2-intro"' not in source: raise RuntimeError('Task 2 sections not found')
intro='<div class="t2-intro"><span class="t2-kicker">DATA ATLAS / 1896—2024</span><h2>从一届赛事，<br>看见一个世纪。</h2><p>先看全局，再按届次、代表团、性别和运动大类缩小范围。每个数字和图形都会随筛选同步更新。</p></div>'
filter_head='<div class="t2-section-head"><div><span>01 / 探索条件</span><h2>把视角交给你</h2></div><p>选择任意维度进行组合筛选；切换指标后，图形与排名会同步变化。</p></div>'
if fresh:
    source=source[:match.start()]+match.group(1)+intro+match.group(3)+filter_head+match.group(2)+source[match.end():]
    source=source.replace('<svg id="chart" viewBox="0 0 1100 440" preserveAspectRatio="none"></svg>','<div class="t2-chart-panel"><svg id="chart" viewBox="0 0 1100 440" role="img" aria-label="筛选结果的历史趋势或代表团排名"></svg><div class="t2-chart-note"><span>图中数值随当前筛选条件变化；悬停节点可查看具体值。</span><span>参赛记录与奖牌记录是不同统计单位。</span></div></div>',1)
    source=source.replace('<table><thead>','<div class="t2-section-head t2-table-heading"><div><span>03 / 代表团切面</span><h2>谁参与，谁留下成绩？</h2></div><p>下表按当前指标排序，展示前 20 个代表团。它跟随上方筛选条件即时更新。</p></div><div class="t2-table-wrap"><table><thead>',1)
    source=source.replace('</tbody></table></main>','</tbody></table></div></main>',1)
    source=source.replace('<div class="actions"><strong id="title"></strong>','<div class="t2-section-head"><div><span>02 / 时间与排名</span><h2>变化从哪一年开始？</h2></div><p>未选届次时看历史趋势；选定某届后，图形切换为代表团排名。</p></div><div class="actions"><strong id="title"></strong>',1)
source=source.replace('</head>',START+CSS+END+'</head>',1)
source=source.replace('</body>',JS+'</body>',1)
PAGE.write_text(source,encoding='utf-8')
print(PAGE)
