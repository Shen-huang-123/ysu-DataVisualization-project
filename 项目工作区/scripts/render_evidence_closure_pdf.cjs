// Print the same published HTML; use an installed Playwright runtime, never commit it.
const path=require('path'),fs=require('fs'),{pathToFileURL}=require('url');
let pw;try{pw=require(process.env.PLAYWRIGHT_MODULE||'playwright-core')}catch(e){pw=require('../qa_tools/node_modules/playwright-core')}
const root=path.resolve(__dirname,'../..');
(async()=>{const browser=await pw.chromium.launch({executablePath:process.env.QA_BROWSER||'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});try{const page=await browser.newPage();const directory=path.join(root,'交付文件/最终提交材料');await page.goto(pathToFileURL(path.join(directory,'关键结论证据与预测验证补充说明.html')).href);await page.pdf({path:path.join(directory,'关键结论证据与预测验证补充说明.pdf'),format:'A4',printBackground:true,preferCSSPageSize:true});}finally{await browser.close()}})().catch(e=>{console.error(e);process.exitCode=1});
