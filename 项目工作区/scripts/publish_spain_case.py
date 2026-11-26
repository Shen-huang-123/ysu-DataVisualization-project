from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2] / '交付文件'
TASK = ROOT / '任务三_专题深挖/S2_口径的魔力'
DATA = ROOT / '任务一_数据体检/02_交付数据'
OUT = TASK / '02_数据表'

official = pd.read_csv(DATA / '2024官方329小项奖牌表.csv')
assert len(official) == 329 and official.event_id.is_unique
gold = official[official.gold_country_code.fillna('').str.split('|').map(lambda codes: 'ESP' in codes)]
raw = pd.read_csv(DATA / '归一数据_保留原始字段.csv.gz', usecols=['Year','NOC','Medal','sport_family','include_main'])
rows = raw.query("Year == 2024 and NOC == 'ESP' and Medal == 'Gold' and include_main")
labels = {'Football':'足球', 'Water Polo':'水球', 'Athletics':'田径', 'Sailing':'帆船'}
result = pd.DataFrame({'小项金牌':gold.groupby('discipline').size(), '金牌记录':rows.groupby('sport_family').size()})
assert set(result.index) == set(labels) and result.notna().all().all()
rank = pd.read_csv(OUT / 'S2_2024双口径完整排名.csv').set_index('NOC').loc['ESP']
assert list(result.sum()) == [rank.Gold_official, rank.Gold_rows]
result = result.rename(index=labels).sort_values('金牌记录', ascending=False)
result.index.name = '运动'
result['增加记录'] = result['金牌记录'] - result['小项金牌']
result.to_csv(OUT / 'S2_西班牙金牌构成.csv', encoding='utf-8-sig')
team = result.loc[['足球','水球']].sum()
rows_html = ''.join(f'<tr><th scope="row">{name}</th><td>{official_count}</td><td>{athlete_count}</td><td>+{extra}</td></tr>' for name,(official_count,athlete_count,extra) in result.iterrows())
page = f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>巴黎2024西班牙的两种金牌榜</title><style>
:root{{color-scheme:light dark}}body{{font:16px/1.8 system-ui;margin:auto;max-width:64rem;padding:clamp(16px,5vw,72px)}}h1{{font-size:clamp(28px,4vw,50px);line-height:1.2}}table{{width:100%;border-collapse:collapse}}td,th{{padding:10px 6px;border-bottom:1px solid #85928d66}}th:first-child{{text-align:left}}td,thead th:not(:first-child){{text-align:right;font-variant-numeric:tabular-nums}}a{{text-underline-offset:4px}}
</style><main><a href="../../最终提交材料/00_先看这里.html">← 返回提交材料</a>
<h1>西班牙为什么从第{rank.official_rank:.0f}升到第{rank.row_rank:.0f}？</h1>
<p>巴黎2024按金、银、铜依次比较。西班牙有{rank.Gold_official:.0f}枚小项金牌，对应{rank.Gold_rows:.0f}条运动员金牌记录。足球和水球两枚小项金牌对应{team['金牌记录']}条记录，占全部金牌记录的{team['金牌记录']/rank.Gold_rows:.1%}。</p>
<table><caption>西班牙金牌按运动拆解</caption><thead><tr><th scope="col">运动</th><th scope="col">小项金牌</th><th scope="col">金牌记录</th><th scope="col">增加记录</th></tr></thead><tbody>{rows_html}</tbody></table>
<p>表中分解的是西班牙的金牌记录差额。第{rank.official_rank:.0f}到第{rank.row_rank:.0f}来自全部代表团重新排序，无法把十个名次按运动直接相加。</p>
<p>逐一移除35个运动大类中的任意一个，西班牙在运动员行口径下仍相对上升。该检验每次从两张榜同时移除同一大类并重新排序。</p>
<p><a href="02_数据表/S2_西班牙金牌构成.csv" download>下载构成表</a> · <a href="02_数据表/S2_2024双口径完整排名.csv" download>下载完整双口径排名</a> · <a href="02_数据表/S2_2024代表团剔除敏感性.csv" download>下载剔除检验</a></p>
<p><a href="../../任务一_数据体检/02_交付数据/2024官方329小项奖牌表.csv" download>329项结果</a> · <a href="../../任务一_数据体检/02_交付数据/归一数据_保留原始字段.csv.gz" download>归一运动员记录</a></p></main></html>'''
(TASK / '西班牙双口径案例.html').write_text(page, encoding='utf-8')
entry = ROOT / '最终提交材料/00_先看这里.html'
text = entry.read_text(encoding='utf-8')
link = '<p><a href="../任务三_专题深挖/S2_口径的魔力/西班牙双口径案例.html">看西班牙第15到第5的运动拆解与复算 ↗</a></p>'
text = text.replace(link, '')
marker = '</main>'
assert marker in text
entry.write_text(text.replace(marker, link + marker, 1), encoding='utf-8')
