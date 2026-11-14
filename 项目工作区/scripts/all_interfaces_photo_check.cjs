const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '../..');
const out = path.join(root, '项目工作区', 'outputs', 'all_photo_check');
fs.mkdirSync(out, {recursive:true});
function pages(dir) {
  return fs.readdirSync(dir,{withFileTypes:true}).flatMap(x => x.isDirectory()?pages(path.join(dir,x.name)):(x.name==='index.html'?[path.join(dir,x.name)]:[]));
}
(async()=>{
  const browser=await chromium.launch({headless:true});
  const result=[];
  for(const file of pages(path.join(root,'交付文件'))) {
    const page=await browser.newPage({viewport:{width:390,height:844}});
    const errors=[]; page.on('pageerror',e=>errors.push(String(e)));
    await page.goto('file:///'+file.replace(/\\/g,'/'));
    await page.waitForTimeout(120);
    const data=await page.evaluate(()=>({overflow:document.documentElement.scrollWidth>innerWidth+3,photo:getComputedStyle(document.querySelector('header')).backgroundImage,body:document.body.className,stage:!!document.querySelector('.photo-stage')}));
    const rel=path.relative(root,file).replace(/\\/g,'/');
    result.push({rel,overflow:data.overflow,photo:data.photo.includes('.jpg')||data.stage,errors});
    if(/作品总入口|任务一_数据体检|任务二_百年全景|01_交互式Dashboard/.test(rel)) await page.screenshot({path:path.join(out, rel.replaceAll('/','_')+'.png'),fullPage:false});
    await page.close();
  }
  await browser.close();
  console.log(JSON.stringify(result,null,2));
  if(result.some(x=>x.overflow||x.errors.length||!x.photo)) process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
