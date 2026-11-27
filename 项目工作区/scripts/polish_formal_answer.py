"""Apply the final editorial pass to the formal answer DOCX."""
from pathlib import Path
import argparse
from io import BytesIO

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
ANSWER = ROOT / '交付文件/最终提交材料/数说奥运_晓组织_正式答卷.docx'
EDITS = (
    ('巴黎2024提供最直接的口径对照。', '巴黎 2024 的 329 个官方小项与同届运动员记录提供了口径对照。西班牙按官方小项口径排第 15，按运动员获奖行口径排第 5。博茨瓦纳同样升 10 位。两榜同时剔除足球后，两队的名次差分别为 3 位和 10 位。历史 555 项已做独立二次来源对照，现行 IOC 逐项核验仍待完成。主场估计受口径与方法影响。冠军延续分析排除未决系列后保留 50 项，变化区间跨零。'),
    ('三口径延伸：', '进一步比较同样升 10 位的西班牙与博茨瓦纳。西班牙的足球、水球合计贡献 2 枚小项金牌与 35 条运动员金牌记录。博茨瓦纳各运动的金牌计数均无差额。按同样的金、银、铜规则同时剔除足球并重算全榜后，西班牙由两榜相差 10 位缩至 3 位，博茨瓦纳仍相差 10 位。可在奖牌口径实验室并排选队、复算并核对逐项记录。'),
)


def style_figure_a1(doc):
    from matplotlib.figure import Figure
    from matplotlib import rc_context
    from matplotlib.ticker import MaxNLocator, StrMethodFormatter
    import pandas as pd

    source = ROOT / '交付文件/任务二_百年全景/02_数据表/A_逐届规模与集中度.csv'
    data = pd.read_csv(source)
    index = next(i for i, paragraph in enumerate(doc.paragraphs)
                 if paragraph.text.strip().startswith(('图 A1', '图A1')))
    image_refs = [ref for paragraph in doc.paragraphs[index-1:index+1]
                  for ref in paragraph._p.xpath('.//a:blip')]
    assert len(image_refs) == 1
    from docx.oxml.ns import qn
    part = doc.part.related_parts[image_refs[0].get(qn('r:embed'))]
    from PIL import Image
    with Image.open(BytesIO(part.blob)) as original:
        width, height = original.size
    ink, muted, grid = '#173b49', '#435760', '#d9e3e6'
    series = (
        ('运动员参赛记录（条）', data.participation_records, '#247487', ',.0f'),
        ('运动员获奖记录（条）', data.medal_records, '#82632d', ',.0f'),
        ('有参赛记录的代表团（个）', data.delegations, '#28576a', ',.0f'),
        ('前五代表团获奖记录份额', data.top5_share * 100, '#91465a', '.1f'),
    )
    with rc_context({'font.family': 'Microsoft YaHei', 'axes.unicode_minus': False}):
        fig = Figure(figsize=(10, 10 * height / width), facecolor='white', dpi=280)
        axes = fig.subplots(2, 2, sharex=True)
        fig.subplots_adjust(left=.092, right=.97, top=.84, bottom=.15, wspace=.29, hspace=.39)
        fig.text(.02, .95, '参赛覆盖扩大，前五代表团份额长期下降', fontsize=17, color=ink, weight='bold', va='top')
        for k, (ax, (label, values, color, fmt)) in enumerate(zip(axes.flat, series)):
            ax.set_title(label, loc='left', color=ink, fontsize=11.5, pad=7, weight='bold')
            ax.plot(data.Year, values, color=color, lw=2.05, zorder=2)
            ax.scatter(data.Year.iloc[-1], values.iloc[-1], s=19, color=color, zorder=3)
            suffix = '%' if k == 3 else ''
            ax.text(.99, 1.035, f'{values.iloc[-1]:{fmt}}{suffix}', transform=ax.transAxes,
                    ha='right', color=color, size=10, weight='bold')
            if k == 0:
                for year in (1916, 1940, 1944):
                    ax.axvline(year, color=grid, linestyle='--', linewidth=.8)
            if k == 3:
                ax.axhline(50, color=muted, linestyle='--', linewidth=.65, alpha=.5)
            ax.set_xlim(1894, 2028)
            ax.set_xticks([1900, 1930, 1960, 1990, 2020])
            ax.tick_params(axis='both', length=0, labelsize=9, colors=muted)
            ax.yaxis.set_major_locator(MaxNLocator(4))
            ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}' + suffix))
            ax.grid(axis='y', color=grid, lw=.65)
            ax.spines[['left','right','top']].set_visible(False)
            ax.spines['bottom'].set_color(grid)
        fig.text(.02, .035, '届次年份 · 运动员记录口径 · 排除 1906 年 · 历史代表团代码分别统计 · 获奖记录含团体成员',
                 color=muted, fontsize=9)
        image = BytesIO()
        fig.savefig(image, format='png', facecolor='white')
    part._blob = image.getvalue()


def style_remaining_figures(doc):
    from PIL import Image

    from docx.oxml.ns import qn

    figure_parts = {doc.part.related_parts[ref.get(qn('r:embed'))]
                    for ref in doc._element.xpath('.//a:blip')}
    for part in figure_parts:
        with Image.open(BytesIO(part.blob)) as original:
            image = original.convert('RGB')
            paper = image.getpixel((0, 0))
            if min(paper) < 230 or max(paper) - min(paper) > 24:
                raise ValueError(f'插图底色超出预期：{part.partname}')
            if paper == (255, 255, 255):
                continue
            # Map each paper channel to white while retaining dark strokes.
            # Treat the full palette consistently, including antialiased edges.
            changed = image.point([min(255, round(value * 255 / channel))
                                   for channel in paper for value in range(256)])
            output = BytesIO()
            changed.save(output, format='PNG', optimize=True)
            part._blob = output.getvalue()


def polish(path):
    doc = Document(path)
    for prefix, revised in EDITS:
        matches = [p for p in doc.paragraphs if p.text.startswith(prefix)]
        if not matches and any(p.text == revised for p in doc.paragraphs):
            continue
        if len(matches) != 1:
            raise ValueError(f'正式答卷段落定位失败：{prefix}')
        paragraph = matches[0]
        if paragraph._p.xpath('.//w:drawing | .//w:hyperlink | .//w:fldSimple'):
            raise ValueError(f'段落包含图形、链接或域：{prefix}')
        paragraph.runs[0].text = revised
        for run in paragraph.runs[1:]:
            run.text = ''
    style_figure_a1(doc)
    style_remaining_figures(doc)
    doc.save(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path, nargs='?', default=ANSWER)
    polish(parser.parse_args().path)
