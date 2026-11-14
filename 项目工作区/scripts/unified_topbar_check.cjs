const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../..');
function files(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(x=>x.isDirectory()?files(path.join(dir,x.name)):(x.name==='index.html'?[path.join(dir,x.name)]:[]))}
(async()=>{
 const browser=await chromium.launch();const failures=[];
 for(const file of files(path.join(root,'交付文件'))){
  const page=await browser.newPage({viewport:{width:390,height:844}}),errors=[];
  page.on('pageerror',e=>errors.push(String(e)));
  await page.goto('file:///'+file.replace(/\\/g,'/'));
  await page.locator('#xz-menu-button').click();
  const data=await page.evaluate(()=>{const nav=document.querySelector('#xz-nav'),menu=document.querySelector('#xz-menu'),r=menu.getBoundingClientRect();return {navHeight:nav.getBoundingClientRect().height,menuLeft:r.left,menuRight:r.right,menuWidth:r.width,menuLinks:[...menu.querySelectorAll('a')].map(a=>a.textContent.trim()),overflow:document.documentElement.scrollWidth>innerWidth+2}});
  if(data.navHeight!==60||data.menuLeft<0||data.menuRight>390||data.menuLinks.length!==5||data.overflow||errors.length) failures.push({file,data,errors});
  await page.close();
 }
 const page=await browser.newPage({viewport:{width:390,height:844}});
 await page.goto('file:///'+path.join(root,'交付文件/任务三_专题深挖/统一中文入口/index.html').replace(/\\/g,'/'));
 await page.locator('#xz-menu-button').click();
 await Promise.all([page.waitForURL(url=>decodeURI(url.href).includes('任务一_数据体检/index.html'),{timeout:5000}),page.locator('#xz-menu a').nth(1).click()]);
 if(!decodeURI(page.url()).includes('任务一_数据体检/index.html')) failures.push({navigation:'wrong destination',url:page.url()});
 await page.waitForTimeout(300);
 if(await page.locator('html').evaluate(e=>e.classList.contains('xz-arriving')||e.classList.contains('xz-leaving'))) failures.push({navigation:'transition did not finish'});
 await browser.close();console.log(JSON.stringify({pages:23,failures},null,2));if(failures.length)process.exit(1)
})().catch(e=>{console.error(e);process.exit(1)});
