"""Keep entry points to the medal lens lab in the homepage and S2 story."""
from pathlib import Path

root=Path(__file__).resolve().parents[2]
home=root/'index.html'
s=home.read_text(encoding='utf-8')
url='交付文件/任务三_专题深挖/S2_口径的魔力/09_奖牌口径实验室/index.html'
link=f'<a class="voyage-cta" href="{url}" style="margin-left:12px;background:transparent;border:1px solid currentColor">打开奖牌口径实验室<span aria-hidden="true">↗</span></a>'
if url not in s:
    start=s.index('data-scene="1"')
    end=s.index('</a>',s.index('class="voyage-cta"',start))+4
    s=s[:end]+link+s[end:]
    home.write_text(s,encoding='utf-8')

story=root/'交付文件/任务三_专题深挖/S2_口径的魔力/06_滚动叙事专题/index.html'
s=story.read_text(encoding='utf-8')
url='../09_奖牌口径实验室/index.html'
if url not in s:
    needle='</p></div><div class="triptych">'
    if needle not in s:raise ValueError('S2 story header changed')
    link=f'</p><a href="{url}" style="display:inline-flex;margin-top:18px;padding:11px 18px;border-radius:999px;background:#e7c48c;color:#0b2831;text-decoration:none;font-weight:800">亲手切换三种口径 ↗</a></div><div class="triptych">'
    s=s.replace(needle,link,1)
    story.write_text(s,encoding='utf-8')
