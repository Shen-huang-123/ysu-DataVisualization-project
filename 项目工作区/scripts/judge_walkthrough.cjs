const {chromium}=require('../qa_tools/node_modules/playwright-core');
const path=require('path');
const fs=require('fs');
const root=path.resolve(__dirname,'../..');
const pages=[
  ['首页','index.html'],
  ['任务一','交付文件/任务一_数据体检/index.html'],
  ['任务二','交付文件/任务二_百年全景/05_交互总览/index.html'],
  ['任务三','交付文件/任务三_专题深挖/统一中文入口/index.html'],
  ['反例证据链','交付文件/任务三_专题深挖/12_反例与证据链/index.html'],
  ['S2稳健性','交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'],
  ['任务四','交付文件/任务四_开放创作/index.html'],
  ['预测','交付文件/任务四_开放创作/02_2028洛杉矶预测/index.html'],
  ['正式提交入口','交付文件/最终提交材料/00_先看这里.html']
];
function rgb(x){const m=x.match(/rgba?\(([^)]+)\)/);return m?m[1].split(',').slice(0,3).map(Number):null}
function luminance(c){return c.map(v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)}).reduce((s,v,i)=>s+v*[.2126,.7152,.0722][i],0)}
function ratio(a,b){let x=luminance(a),y=luminance(b);return(Math.max(x,y)+.05)/(Math.min(x,y)+.05)}
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
 const results=[];
 for(const [name,rel] of pages){
  for(const width of [1440,390]){
   const page=await browser.newPage({viewport:{width,height:900}}),errors=[];
   page.on('pageerror',e=>errors.push(e.message));
   await page.goto('file:///'+path.join(root,rel).replace(/\\/g,'/'));
   await page.waitForTimeout(250);
   const audit=await page.evaluate(()=>{
    const imgs=[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src);
    const links=[...document.querySelectorAll('a[href]')].filter(a=>a.getAttribute('href')&&!/^(https?:|#|mailto:|javascript:)/.test(a.getAttribute('href'))).map(a=>a.href);
    const samples=[...document.querySelectorAll('p,li,td,small')].filter(e=>e.getBoundingClientRect().width>0&&getComputedStyle(e).fontSize&&parseFloat(getComputedStyle(e).fontSize)<24).slice(0,250).map(e=>({text:e.textContent.trim().slice(0,28),color:getComputedStyle(e).color,bg:getComputedStyle(e).backgroundColor,ancestor:getComputedStyle(e.parentElement).backgroundColor}));
    return{overflow:document.documentElement.scrollWidth>innerWidth+2,imgs,links,samples};
   });
   const broken=audit.links.filter(u=>u.startsWith('file:///')&&!fs.existsSync(decodeURIComponent(new URL(u).pathname.slice(1))));
   const contrast=[];
   for(const s of audit.samples){const fg=rgb(s.color),bg=rgb(s.bg)||rgb(s.ancestor);if(fg&&bg&&ratio(fg,bg)<4.5)contrast.push({text:s.text,ratio:+ratio(fg,bg).toFixed(2)})}
   results.push({page:name,width,title:await page.title(),errors,overflow:audit.overflow,brokenImages:audit.imgs.length,brokenLocalLinks:broken.length,lowContrastCandidates:contrast.slice(0,8)});
   if(width===1440&&['任务二','任务三','任务四','预测','反例证据链'].includes(name)){
     const btn=page.locator('#xz-theme');if(await btn.count()){await btn.click();results.at(-1).darkMode=await page.evaluate(()=>document.body.classList.contains('xz-dark'));}
   }
   await page.close();
  }
 }
 await browser.close();
 fs.writeFileSync(path.join(root,'项目工作区/评委视角走查结果.json'),JSON.stringify(results,null,2));
 console.log(JSON.stringify(results.map(({page,width,errors,overflow,brokenImages,brokenLocalLinks,lowContrastCandidates,darkMode})=>({page,width,errors:errors.length,overflow,brokenImages,brokenLocalLinks,contrast:lowContrastCandidates.length,darkMode})),null,2));
})().catch(e=>{console.error(e);process.exit(1)});
