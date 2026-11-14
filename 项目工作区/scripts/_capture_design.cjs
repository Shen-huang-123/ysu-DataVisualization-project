const {chromium}=require('../qa_tools/node_modules/playwright-core');
const {pathToFileURL}=require('url');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});for(const [name,file] of [['home','index.html'],['task2','交付文件/任务二_百年全景/05_交互总览/index.html'],['topic','交付文件/任务三_专题深挖/统一中文入口/index.html']]){const p=await b.newPage({viewport:{width:1440,height:900},deviceScaleFactor:1});await p.goto(pathToFileURL(path.resolve(file)).href,{waitUntil:'domcontentloaded'});await p.waitForTimeout(1000);await p.screenshot({path:'项目工作区/视觉验收/新设计_'+name+'.png'});await p.locator('.ox-trigger').click();await p.waitForTimeout(650);await p.screenshot({path:'项目工作区/视觉验收/新设计_'+name+'_nav.png'});await p.close()}await b.close()})()


