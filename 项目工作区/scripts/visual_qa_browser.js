const { chromium } = require('../qa_tools/node_modules/playwright-core');
const fs = require('fs');
const path = require('path');
const { pathToFileURL } = require('url');

const root = path.resolve(__dirname, '../..');
const delivery = path.join(root, '交付文件');
const out = path.join(root, '项目工作区', 'qa_visual');
const pages = process.argv.slice(2);
const scrollY = Number(process.env.QA_SCROLL_Y || 0);
const onlyMobileDark = process.env.QA_ONLY_MOBILE_DARK === '1';
if (!pages.length) throw new Error('Pass relative index.html paths');
fs.mkdirSync(out, { recursive: true });

(async () => {
  const browser = await chromium.launch({ headless: true, executablePath: process.env.QA_BROWSER || 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  try {
    for (const rel of pages) {
      for (const [width, height] of (onlyMobileDark ? [[390, 844]] : [[1440, 900], [390, 844]])) {
        for (const dark of (onlyMobileDark ? [true] : [false, true])) {
          const context = await browser.newContext({ viewport: { width, height }, reducedMotion: 'reduce', deviceScaleFactor: 1 });
          const page = await context.newPage();
          const errors = [];
          page.on('pageerror', e => errors.push(e.message));
          await page.goto(pathToFileURL(path.join(delivery, rel)).href, { waitUntil: 'load' });
          if (dark) await page.locator('#xz-theme').click();
          await page.waitForTimeout(120);
          if (scrollY) await page.evaluate(y => window.scrollTo(0, y), scrollY);
          const metrics = await page.evaluate(() => ({
            viewport: document.documentElement.clientWidth,
            pageWidth: document.documentElement.scrollWidth,
            dark: document.body.classList.contains('xz-dark'),
            storyGuide: (() => { const el = document.querySelector('.story-guide'); return el ? getComputedStyle(el).display : null; })(),
            mainHeadingColor: (() => { const el = document.querySelector('main h2'); return el ? getComputedStyle(el).color : null; })(),
          }));
          const name = rel.replace(/[/\\]/g, '_').replace(/index\.html$/, '').replace(/_$/, '');
          await page.screenshot({ path: path.join(out, `${name}_${width}_${dark ? 'dark' : 'light'}${scrollY ? `_y${scrollY}` : ''}_pw.png`) });
          process.stdout.write(JSON.stringify({ page: rel, width, dark, ...metrics, errors }) + '\n');
          await context.close();
        }
      }
    }
  } finally { await browser.close(); }
})().catch(e => { console.error(e); process.exitCode = 1; });
