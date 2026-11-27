"""Apply the final editorial pass to the formal answer DOCX."""
from pathlib import Path
import argparse

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
ANSWER = ROOT / '交付文件/最终提交材料/数说奥运_晓组织_正式答卷.docx'
EDITS = (
    ('巴黎2024提供最直接的口径对照。', '巴黎 2024 的 329 个官方小项与同届运动员记录提供了口径对照。西班牙按官方小项口径排第 15，按运动员获奖行口径排第 5。博茨瓦纳同样升 10 位。两榜同时剔除足球后，两队的名次差分别为 3 位和 10 位。历史 555 项已做独立二次来源对照，现行 IOC 逐项核验仍待完成。主场估计受口径与方法影响。冠军延续分析排除未决系列后保留 50 项，变化区间跨零。'),
    ('三口径延伸：', '进一步比较同样升 10 位的西班牙与博茨瓦纳。西班牙的足球、水球合计贡献 2 枚小项金牌与 35 条运动员金牌记录。博茨瓦纳各运动的金牌计数均无差额。按同样的金、银、铜规则同时剔除足球并重算全榜后，西班牙由两榜相差 10 位缩至 3 位，博茨瓦纳仍相差 10 位。可在奖牌口径实验室并排选队、复算并核对逐项记录。'),
)


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
    doc.save(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path, nargs='?', default=ANSWER)
    polish(parser.parse_args().path)
