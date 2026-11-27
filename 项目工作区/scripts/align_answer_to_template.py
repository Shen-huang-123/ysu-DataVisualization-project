"""Apply submission-format edits after polish_formal_answer.py."""
from pathlib import Path
import argparse

from docx import Document

ROOT = Path(__file__).resolve().parents[2]
ANSWER = ROOT / '交付文件/最终提交材料/数说奥运_晓组织_正式答卷.docx'

ABSTRACT = (
    '本文审计1896—2024年夏奥252,565条记录，从奖牌、代表团、女性参与和项目演化四个视角分析百年变化，'
    '并用2024年329个官方小项对照运动员获奖行。换成获奖行口径，西班牙由第15名升至第5名，'
    '博茨瓦纳同样上升10位。剔除足球并重算两张全榜后，两队的口径名次差分别为3位和10位。'
    '历史555项完成独立二次来源交叉对照，现行国际奥委会逐项核验仍待完成。'
    '洛杉矶2028以历史加权基准提供有条件的点估计，历史回测检验预测误差与区间覆盖。'
)
SOURCES = (
    '数据来源：Kaggle《Summer Olympics Medals (1896–2024)》（Stefany De Oliveira）；'
    '上游为 Nitish Sharma 的《Olympics 124 years Dataset (till 2020)》和 Petro Ivaniuk 的《Paris 2024 Olympic Summer Games》。'
    '口径与外部来源的字段、获取方式及匹配规则见任务一口径说明书和各专题来源台账。'
)
DIAGNOSTIC = (
    '时间边界诊断：2024运动员行折中，全时期筛选提前带入AIN与霹雳舞；仅用此前资料筛选时纳入KUW且不含霹雳舞。'
    '两种筛选的混合MAE分别为3.961和3.978行/队。早期滚动回放已使用此前资料。'
)


def replace_text(paragraph, text):
    if paragraph._p.xpath('.//w:drawing | .//w:hyperlink | .//w:fldSimple'):
        raise ValueError('目标段落含图形、链接或域')
    if paragraph.runs:
        paragraph.runs[0].text = text
        for run in paragraph.runs[1:]:
            run.text = ''
    else:
        paragraph.add_run(text)


def align(path):
    doc = Document(path)
    assert len(ABSTRACT) <= 300
    paragraphs = doc.paragraphs
    start = next(i for i, p in enumerate(paragraphs) if p.text == '研究摘要与证据边界')
    end = next(i for i, p in enumerate(paragraphs) if p.text.startswith('Ⅰ　数据体检'))
    heading = paragraphs[start]
    replace_text(heading, '摘要')
    replace_text(paragraphs[start + 1], ABSTRACT)
    for paragraph in paragraphs[start + 2:end]:
        paragraph._p.getparent().remove(paragraph._p)
    first_answer = next(p for p in doc.paragraphs if p.text.startswith('核心统计') or p.text.startswith('特殊届次与身份'))
    first_answer.insert_paragraph_before(SOURCES, style=first_answer.style)
    video = next(p for p in doc.paragraphs if p.text.startswith('作品视频链接：'))
    replace_text(video, '作品视频链接（B站）：待填写')
    forecast = next(p for p in doc.paragraphs if p.text.startswith('不确定性：新基准'))
    forecast.insert_paragraph_before(DIAGNOSTIC, style=forecast.style)
    doc.save(path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=Path, nargs='?', default=ANSWER)
    align(parser.parse_args().path)
