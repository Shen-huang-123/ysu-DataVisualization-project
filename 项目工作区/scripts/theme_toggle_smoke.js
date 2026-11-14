// Runs the shipped inline theme controller against a minimal DOM on every page.
const fs = require('fs');
const path = require('path');
const vm = require('vm');

const root = path.resolve(__dirname, '..', '..', '交付文件');
function* htmlFiles(dir) {
  for (const item of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, item.name);
    if (item.isDirectory()) yield* htmlFiles(full);
    else if (item.name === 'index.html') yield full;
  }
}
function classes() {
  const values = new Set();
  return {
    contains: key => values.has(key),
    add: key => values.add(key),
    toggle(key, force) {
      const on = force === undefined ? !values.has(key) : force;
      if (on) values.add(key); else values.delete(key);
      return on;
    },
  };
}
let checked = 0;
for (const file of htmlFiles(root)) {
  const html = fs.readFileSync(file, 'utf8');
  const match = html.match(/<script id="unified-topbar-script">([\s\S]*?)<\/script>/);
  if (!match) throw new Error(`Missing theme script: ${file}`);
  if (html.includes('id="xz-ui-script"')) throw new Error(`Conflicting legacy theme controller: ${file}`);
  const handlers = {};
  const theme = { setAttribute() {}, addEventListener: (event, fn) => { handlers[event] = fn; } };
  const body = { classList: classes() };
  const documentElement = { classList: classes(), scrollHeight: 1000 };
  const document = {
    body, documentElement,
    querySelector: selector => selector === '#xz-theme' ? theme : null,
  };
  const saved = {};
  vm.runInNewContext(match[1], {
    document,
    localStorage: {
      getItem: key => saved[key] || null,
      setItem: (key, value) => { saved[key] = value; },
    },
    addEventListener() {},
  }, { filename: file });
  if (typeof handlers.click !== 'function') throw new Error(`No click handler: ${file}`);
  handlers.click();
  if (!body.classList.contains('xz-dark') || saved['xz-theme'] !== 'dark') throw new Error(`Dark failed: ${file}`);
  handlers.click();
  if (body.classList.contains('xz-dark') || saved['xz-theme'] !== 'light') throw new Error(`Light failed: ${file}`);
  checked++;
}
console.log(`Theme toggle passed on ${checked} pages.`);
