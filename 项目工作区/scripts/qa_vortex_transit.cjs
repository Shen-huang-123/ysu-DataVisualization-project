const {chromium}=require('../qa_tools/node_modules/playwright-core');const {pathToFileURL}=require('url');const path=require('path');
(async()=>{const b=await chromium.launch({executablePath:'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',headless:true});const url=pathToFileURL(path.resolve('index.html')).href;const errors=[];
for(const config of [{name:'desktop',width:1440,height:900,reducedMotion:'no-preference'},{name:'mobile',width:390,height:844,reducedMotion:'no-preference'},{name:'reduced',width:1440,height:900,reducedMotion:'reduce'}]){
 const p=await b.newPage({viewport:{width:config.width,height:config.height},reducedMotion:config.reducedMotion});p.on('pageerror',e=>errors.push(`${config.name}: ${e}`));await p.goto(url,{waitUntil:'load'});await p.waitForTimeout(700);
 const initial=await p.evaluate(()=>({stage:+getComputedStyle(document.querySelector('.vortex-stage')).opacity,hero:document.querySelector('.hero').getBoundingClientRect().top,trigger:!!window.ScrollTrigger?.getById('hero-vortex-transit')}));
 if(config.reducedMotion==='reduce'){if(initial.trigger||initial.stage!==0)errors.push('reduced motion should not pin or reveal vortex')}else{
  if(!initial.trigger||initial.stage>.05)errors.push(`${config.name}: initial state`);
  await p.evaluate(()=>scrollTo(0,innerHeight*.65));await p.waitForTimeout(900);
  const mid=await p.evaluate(()=>({stage:+getComputedStyle(document.querySelector('.vortex-stage')).opacity,hero:document.querySelector('.hero').getBoundingClientRect().top,progress:ScrollTrigger.getById('hero-vortex-transit').progress}));
  if(mid.stage<.5||Math.abs(mid.hero)>3||mid.progress<.2)errors.push(`${config.name}: vortex did not scrub or pin ${JSON.stringify(mid)}`);
  await p.screenshot({path:`项目工作区/视觉验收/涡旋_${config.name}_中段.png`});
  await p.evaluate(()=>scrollTo(0,innerHeight*2.8));await p.waitForTimeout(750);
  const next=await p.locator('.intro').evaluate(e=>e.getBoundingClientRect().top);if(next>config.height)errors.push(`${config.name}: next section unreachable`);
 }
 if(await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+2))errors.push(`${config.name}: horizontal overflow`);
 await p.close();}
await b.close();console.log(JSON.stringify({cases:3,errors},null,2));if(errors.length)process.exit(1)})().catch(e=>{console.error(e);process.exit(1)})

