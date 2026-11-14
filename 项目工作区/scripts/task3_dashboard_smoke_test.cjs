const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const target = path.resolve(__dirname, '../../交付文件/任务三_专题深挖/S2_口径的魔力/06_交互榜/index.html');
  const browser = await chromium.launch({headless:true});
  const page = await browser.newPage({viewport:{width:1440,height:1000}});
  const errors=[]; page.on('pageerror', e=>errors.push(String(e)));
  await page.goto('file:///' + target.replace(/\\/g,'/'));
  await page.waitForSelector('tbody tr');
  const initial = await page.locator('tbody tr').count();
  const selects = page.locator('select');
  if (await selects.count() < 3) throw new Error('Missing dashboard controls');
  for (const value of ['fractional','rows','official']) {
    await selects.nth(0).selectOption(value);
    await page.waitForTimeout(80);
    if (await page.locator('tbody tr').count() < 10) throw new Error('No rows for '+value);
  }
  await selects.nth(1).selectOption('total');
  await selects.nth(2).selectOption('50');
  await page.waitForTimeout(80);
  const expanded = await page.locator('tbody tr').count();
  if (errors.length) throw new Error(errors.join('\n'));
  console.log(JSON.stringify({passed:true, initialRows:initial, expandedRows:expanded, pageErrors:0}));
  await browser.close();
})().catch(e=>{ console.error(e); process.exit(1); });
