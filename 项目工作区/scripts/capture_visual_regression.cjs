const {chromium}=require('../qa_tools/node_modules/playwright-core');
const path=require('path'),fs=require('fs');
const root=path.resolve(__dirname,'../..');
const output=path.join(root,'项目工作区/视觉验收');fs.mkdirSync(output,{recursive:true});
const cases=[
 ['总入口','交付文件/作品总入口/index.html'],
 ['任务一','交付文件/任务一_数据体检/index.html'],
 ['任务二','交付文件/任务二_百年全景/05_交互总览/index.html'],
 ['任务三','交付文件/任务三_专题深挖/统一中文入口/index.html'],
 ['任务四','交付文件/任务四_开放创作/index.html'],
 ['S1','交付文件/任务三_专题深挖/S1_东道主效应/index.html'],
 ['S2','交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'],
 ['S3','交付文件/任务三_专题深挖/S3_地缘政治的投影/index.html'],
 ['S4','交付文件/任务三_专题深挖/S4_小代表团的大突破/index.html'],
 ['S5','交付文件/任务三_专题深挖/S5_奖牌的通货膨胀/index.html'],
 ['S6','交付文件/任务三_专题深挖/S6_王者与传奇/index.html'],
 ['S7','交付文件/任务三_专题深挖/S3_冠军的保质期/06_冠军王朝时间轴/index.html'],
 ['S8','交付文件/任务三_专题深挖/S8_她们登上领奖台/index.html'],
 ['S9','交付文件/任务三_专题深挖/S9_消失的赛场/index.html'],
 ['S10','交付文件/任务三_专题深挖/S10_奖牌藏在哪些项目/index.html']
];
(async()=>{const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'}),results=[];
 for(const [name,rel] of cases){for(const width of [1440,390]){const page=await browser.newPage({viewport:{width,height:width===390?844:900},reducedMotion:'reduce'}),errors=[];page.on('pageerror',e=>errors.push(e.message));await page.goto('file:///'+path.join(root,rel).replace(/\\/g,'/'));await page.waitForTimeout(350);for(const mode of ['light','dark']){const dark=mode==='dark';if(dark){const toggle=page.locator('#xz-theme');if(!(await toggle.count()))continue;await toggle.click();await page.waitForTimeout(150)}for(const screen of [0,1]){await page.evaluate(n=>scrollTo(0,n*innerHeight),screen);await page.waitForTimeout(180);await page.screenshot({path:path.join(output,`${name}_${width}_${mode}_${screen}.png`)});}const state=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth+2,heroBg:(()=>{let h=document.querySelector('header.hero,header.photo-editorial-hero');return h?getComputedStyle(h).backgroundImage.slice(0,90):''})(),theme:document.body.classList.contains('xz-dark')}));results.push({name,width,mode,errors, ...state})}await page.close()}}
 await browser.close();fs.writeFileSync(path.join(output,'检查结果.json'),JSON.stringify(results,null,2));console.log(JSON.stringify({states:results.length,errors:results.filter(x=>x.errors.length),overflow:results.filter(x=>x.overflow),screenshots:fs.readdirSync(output).filter(x=>x.endsWith('.png')).length},null,2));})().catch(e=>{console.error(e);process.exit(1)});
