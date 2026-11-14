const {chromium}=require('playwright');
const path=require('path');
const root=path.resolve(__dirname,'../..');
const pages=[
 ['任务一','交付文件/任务一_数据体检/index.html'],
 ['任务二','交付文件/任务二_百年全景/05_交互总览/index.html'],
 ['任务三入口','交付文件/任务三_专题深挖/统一中文入口/index.html'],
 ['任务三交互榜','交付文件/任务三_专题深挖/S2_口径的魔力/06_交互榜/index.html'],
 ['任务三故事','交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'],
 ['任务三时间轴','交付文件/任务三_专题深挖/S3_冠军的保质期/06_冠军王朝时间轴/index.html'],
 ['任务四入口','交付文件/任务四_开放创作/index.html'],
 ['任务四预测','交付文件/任务四_开放创作/01_交互式Dashboard/index.html'],
 ['任务四新闻','交付文件/任务四_开放创作/03_数据新闻/index.html'],
 ['任务四历史','交付文件/任务四_开放创作/交互看板/index.html'],
];
(async()=>{const b=await chromium.launch({headless:true});const report=[];
for(const [name,rel] of pages){const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1}),errors=[];p.on('pageerror',e=>errors.push(String(e)));await p.goto('file:///'+path.join(root,rel).replace(/\\/g,'/'));await p.waitForTimeout(350);const data={name,title:await p.title(),errors,nav:await p.locator('#xz-nav').count(),overflow:await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)};await p.screenshot({path:path.join(root,'项目工作区/outputs/ui_'+name+'.png')});report.push(data);await p.close()}
const m=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:1});await m.goto('file:///'+path.join(root,pages[1][1]).replace(/\\/g,'/'));report.push({name:'任务二移动端',overflow:await m.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2)});await m.screenshot({path:path.join(root,'项目工作区/outputs/ui_任务二移动端.png')});await m.close();await b.close();console.log(JSON.stringify(report,null,2));if(report.some(x=>x.errors?.length||x.overflow))process.exit(1)})().catch(e=>{console.error(e);process.exit(1)});
