const { chromium } = require('playwright');
const path = require('path');
const { pathToFileURL } = require('url');

(async () => {
  const target = path.resolve(process.argv[2]);
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ acceptDownloads: true });
  const errors = [];
  page.on('pageerror', error => errors.push(String(error)));
  await page.goto(pathToFileURL(target).href, { waitUntil: 'load' });
  await page.waitForFunction(() => document.querySelector('#total')?.textContent.trim().length > 0);

  const initial = await page.locator('#total').textContent();
  await page.selectOption('#year', '2024');
  await page.selectOption('#noc', 'CHN');
  await page.selectOption('#sex', 'F');
  await page.selectOption('#sport', 'Swimming');
  await page.selectOption('#metric', 'medals');
  await page.waitForTimeout(100);
  const filtered = await page.locator('#total').textContent();
  const title = await page.locator('#title').textContent();
  const rows = await page.locator('#body tr').count();
  await page.screenshot({ path: path.join(path.dirname(target), '交互总览预览.png'), fullPage: true });
  const downloadPromise = page.waitForEvent('download');
  await page.click('#download');
  const download = await downloadPromise;

  if (errors.length) throw new Error(`Page errors: ${errors.join(' | ')}`);
  if (!initial || !filtered || title !== '2024年代表团排名' || rows < 1) throw new Error('Filter linkage failed');
  if (!download.suggestedFilename().endsWith('.csv')) throw new Error('CSV download failed');

  console.log(JSON.stringify({ initial, filtered, title, rows, download: download.suggestedFilename(), pageErrors: errors }, null, 2));
  await browser.close();
})().catch(error => { console.error(error); process.exit(1); });
