const {chromium}=require('playwright'); const path=require('path');
const root=path.resolve(__dirname,'../..');
const pages=[
 ['任务三统一入口','交付文件/任务三_专题深挖/统一中文入口/index.html'],
 ['冠军王朝时间轴','交付文件/任务三_专题深挖/S3_冠军的保质期/06_冠军王朝时间轴/index.html'],
 ['口径滚动专题','交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'],
 ['任务二交互总览','交付文件/任务二_百年全景/05_交互总览/index.html'],
 ['任务四交互看板','交付文件/任务四_开放创作/交互看板/index.html']];
(async()=>{const b=await chromium.launch({headless:true});let out=[];for(const [name,rel] of pages){const p=await b.newPage({viewport:{width:1440,height:1000}}),errors=[];p.on('pageerror',e=>errors.push(String(e)));await p.goto('file:///'+path.join(root,rel).replace(/\\/g,'/'));await p.waitForTimeout(250);const body=await p.locator('body').innerText();const visibleEnglish=(body.match(/\b(?:Dashboard|Overview|Explore|Download|Reset|Search|Filter|Robustness|Three Lenses|Source and Boundary)\b/gi)||[]);await p.screenshot({path:path.join(root,'项目工作区/outputs/中文界面验收_'+name+'.png'),fullPage:name==='任务三统一入口'});out.push({name,title:await p.title(),bodyChars:body.length,pageErrors:errors.length,visibleEnglish});await p.close()}await b.close();if(out.some(x=>x.pageErrors||x.visibleEnglish.length))throw new Error(JSON.stringify(out));console.log(JSON.stringify({passed:true,pages:out},null,2))})().catch(e=>{console.error(e);process.exit(1)});
