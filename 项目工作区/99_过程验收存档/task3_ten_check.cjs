const {chromium}=require('playwright');
const path=require('path');
const root=path.resolve(__dirname,'..');
const base=path.join(root,'交付文件/任务三_专题深挖');
const folders=['统一中文入口','S3_地缘政治的投影','S4_小代表团的大突破','S5_奖牌的通货膨胀','S6_王者与传奇','S8_她们登上领奖台','S9_消失的赛场','S10_奖牌藏在哪些项目'];
(async()=>{const browser=await chromium.launch({headless:true});let bad=false;
for(const folder of folders){for(const width of [1440,390]){const p=await browser.newPage({viewport:{width,height:900}});let errors=[];p.on('pageerror',e=>errors.push(String(e)));await p.goto('file:///'+path.join(base,folder,'index.html').replace(/\\/g,'/'));await p.waitForTimeout(1500);let info=await p.evaluate(()=>({title:document.title,overflow:document.documentElement.scrollWidth>innerWidth+2,bars:document.querySelectorAll('.bar').length,art:document.querySelectorAll('.art-figure svg').length,cards:document.querySelectorAll('.story').length,photos:[...document.querySelectorAll('.photo-stage img,.story-photo')].every(x=>x.complete&&x.naturalWidth>0)}));if(folder!=='统一中文入口'){await p.locator('.bar').last().click();info.clicked=await p.locator('#pick').innerText()}if(width===1440)await p.screenshot({path:path.join(root,'项目工作区/outputs/十专题_'+folder+'.png'),fullPage:true});console.log(JSON.stringify({folder,width,...info,errors}));bad ||= info.overflow||errors.length>0||!info.photos||folder!=='统一中文入口'&&info.bars===0||folder==='统一中文入口'&&info.cards!==10;await p.close()}}
await browser.close();if(bad)process.exit(1)})().catch(e=>{console.error(e);process.exit(1)});
