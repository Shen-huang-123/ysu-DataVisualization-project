"""Idempotently connect the two new exhibits to the existing reading path."""
from pathlib import Path

root = Path(__file__).resolve().parents[2]

def replace_once(path, old, new):
    content = path.read_text(encoding='utf-8')
    if new in content:
        return
    if old not in content:
        raise RuntimeError(f'Entry anchor changed: {path}')
    path.write_text(content.replace(old, new, 1), encoding='utf-8')

home = root / 'index.html'
replace_once(home,
    '进入百年全景<span aria-hidden="true">↗</span></a>',
    '进入百年全景<span aria-hidden="true">↗</span></a><a class="voyage-cta" href="交付文件/任务二_百年全景/10_百年项目星系/index.html" style="margin-left:12px;background:transparent;border:1px solid currentColor">探索项目星系<span aria-hidden="true">↗</span></a>')
replace_once(home,
    '进入开放创作<span aria-hidden="true">↗</span></a>',
    '进入开放创作<span aria-hidden="true">↗</span></a><a class="voyage-cta" href="交付文件/任务四_开放创作/09_预测风暴实验室/index.html" style="margin-left:12px;background:transparent;border:1px solid currentColor">拨动预测风暴<span aria-hidden="true">↗</span></a>')

task4 = root / '交付文件/任务四_开放创作/index.html'
replace_once(task4,
    '<a href="06_赛后验收单/index.html" data-no="05">',
    '<a href="09_预测风暴实验室/index.html" data-no="07"><small>假设敏感性</small><h3>预测对哪股风最敏感？</h3><p>拨动主场、新增运动与资格条件，让预测点与参照宽度实时响应。</p><strong>进入预测风暴 ↗</strong></a><a href="06_赛后验收单/index.html" data-no="08">')

task2 = root / '交付文件/任务二_百年全景/05_交互总览/index.html'
replace_once(task2,
    '<!-- CONCENTRATION_START -->',
    '<aside style="max-width:1280px;margin:20px auto;padding:23px clamp(20px,5vw,70px);border:1px solid #788f8a;border-radius:22px;background:#123640;color:#f2f6ee;display:flex;align-items:center;justify-content:space-between;gap:18px;flex-wrap:wrap"><div><small style="color:#e6bf82">新增 · 百年项目星系</small><h2 style="margin:7px 0;font-size:clamp(23px,3vw,36px)">项目如何进入、离开与重返？</h2><p style="margin:0;color:#cfdfdc">拖动 30 届时间轴，点击运动星点，再用逐届记录图读数。</p></div><a href="../10_百年项目星系/index.html" style="color:#f1cb8e;font-weight:800">进入项目星系 ↗</a></aside><!-- CONCENTRATION_START -->')

readme = root / 'README.md'
replace_once(readme,
    '| 正式报告、答卷和海报 |',
    '| 百年运动项目的进退 | [百年项目星系](交付文件/任务二_百年全景/10_百年项目星系/index.html) |\n| 拨动 2028 预测假设 | [预测风暴实验室](交付文件/任务四_开放创作/09_预测风暴实验室/index.html) |\n| 正式报告、答卷和海报 |')
