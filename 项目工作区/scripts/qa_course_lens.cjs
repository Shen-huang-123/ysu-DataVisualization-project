const { chromium } = require('../qa_tools/node_modules/playwright-core');
const files = [
  'index.html',
  '交付文件/任务二_百年全景/05_交互总览/index.html',
  '交付文件/任务二_百年全景/09_课程方法可视分析/index.html'
];
(async () => {
  const browser = await chromium.launch({ executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe' });
  for (const file of files) {
    const page = await browser.newPage();
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    await page.goto('file:///D:/虚拟C盘/数据可视化挑战赛/' + file);
    console.log(file, 'title:', await page.title(), 'errors:', errors.length);
    if (file.includes('05_交互总览')) console.log('entry:', await page.locator('.course-lens-entry a').count());
    if (file.includes('09_课程方法')) {
      console.log('rows:', await page.locator('.row').count());
      await page.locator('#threshold').selectOption('50');
      console.log('rows after filter:', await page.locator('.row').count());
    }
    await page.close();
  }
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
