const {chromium}=require('../qa_tools/node_modules/playwright-core');
const fs=require('fs'),path=require('path');
const {pathToFileURL,fileURLToPath}=require('url');
const base=path.resolve(__dirname,'../../交付文件');
function pages(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?pages(path.join(dir,e.name)):e.name==='index.html'?[path.join(dir,e.name)]:[])}
(async()=>{
  const browser=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});
  const errors=[],files=[...pages(base),path.resolve(__dirname,'../../index.html')];
  for(const file of files){
    const page=await browser.newPage({viewport:{width:1440,height:900}});
    page.on('pageerror',e=>errors.push({file:path.relative(base,file),error:String(e)}));
    try{
      await page.goto(pathToFileURL(file).href,{waitUntil:'domcontentloaded',timeout:15000});
      const button=page.locator('.ox-trigger'),panel=page.locator('.ox-panel');
      if(await button.count()!==1||await panel.count()!==1)throw Error('Missing or duplicate navigator');
      await button.click();
      if(!await panel.isVisible()||await panel.locator('a').count()!==4)throw Error('Navigation did not open with four links');
      const hrefs=await panel.locator('a').evaluateAll(links=>links.map(a=>a.href));
      if(hrefs.some(h=>!h.startsWith('file:///')||!fs.existsSync(fileURLToPath(h))))throw Error('Broken local task link');
      await page.keyboard.press('Escape');if(await panel.isVisible())throw Error('Escape did not close navigation');
      const zoomable=page.locator('.ox-zoomable');
      if(await zoomable.count()){
        await zoomable.first().evaluate(img=>img.click());
        if(!await page.locator('.ox-viewer').isVisible())throw Error('Chart image viewer did not open');
        await page.keyboard.press('Escape');
        if(await page.locator('.ox-viewer').isVisible())throw Error('Chart image viewer did not close');
      }
      const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2);
      if(overflow)throw Error('Desktop horizontal overflow');
      if(['作品总入口','任务一_数据体检','任务二_百年全景','任务三_专题深挖','任务四_开放创作'].some(x=>file.includes(x))){
        await page.setViewportSize({width:390,height:844});
        const mobileOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2);
        if(mobileOverflow)throw Error('Mobile horizontal overflow');
        await button.click();if(!await panel.isVisible())throw Error('Mobile navigation did not open');
        const box=await panel.boundingBox();if(!box||box.height<180||box.y<0||box.y+box.height>844)throw Error('Mobile navigation is clipped');
      }
    }catch(e){errors.push({file:path.relative(base,file),error:String(e)})}
    await page.close();
  }
  await browser.close();
  console.log(JSON.stringify({pages:files.length,errors},null,2));
  if(errors.length)process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});
