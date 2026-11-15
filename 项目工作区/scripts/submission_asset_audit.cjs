const fs = require('fs');
const path = require('path');

const root = path.resolve(__dirname, '../..');
const pages = [
  path.join(root, 'index.html'),
  path.join(root, '交付文件/最终提交材料/00_先看这里.html'),
];

function collect(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) collect(full);
    else if (entry.name === 'index.html') pages.push(full);
  }
}
collect(path.join(root, '交付文件'));

let references = 0;
const broken = [];
for (const page of pages) {
  const html = fs.readFileSync(page, 'utf8');
  const found = html.matchAll(/\b(?:href|src)=["']([^"']+)["']|url\(["']?([^"')]+)["']?\)/g);
  for (const match of found) {
    const raw = (match[1] || match[2]).trim();
    if (!raw || /^(?:#|https?:|mailto:|data:|javascript:|blob:|\/\/)/i.test(raw)) continue;
    let relative = raw.split(/[?#]/)[0];
    if (!relative || relative.startsWith('/')) continue;
    try { relative = decodeURIComponent(relative); } catch {}
    const destination = path.resolve(path.dirname(page), relative);
    references++;
    if (!fs.existsSync(destination)) broken.push({ page: path.relative(root, page), target: raw });
  }
}

const result = { pages: pages.length, localReferences: references, brokenCount: broken.length, broken };
fs.writeFileSync(path.join(root, '项目工作区/提交资源核验结果.json'), JSON.stringify(result, null, 2));
console.log(JSON.stringify({ pages: result.pages, localReferences: references, brokenCount: broken.length }));
if (broken.length) process.exitCode = 1;
