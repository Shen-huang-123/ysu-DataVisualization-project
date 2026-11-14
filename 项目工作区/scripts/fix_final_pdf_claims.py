"""Remove outdated source-status claims from the two current review PDFs."""
from pathlib import Path
import pymupdf

ROOT = Path(__file__).resolve().parents[2]
FONT = r"C:\Windows\Fonts\simhei.ttf"


def replace(path: Path, region, lines, size, start_y, leading, background=(1, 1, 1)):
    doc = pymupdf.open(path)
    page = doc[0]
    page.add_redact_annot(pymupdf.Rect(*region), fill=background)
    page.apply_redactions()
    page.insert_font(fontname="Chinese", fontfile=FONT)
    for index, line in enumerate(lines):
        page.insert_text((region[0], start_y + index * leading), line,
                         fontname="Chinese", fontsize=size, color=(0.20, 0.25, 0.28))
    tmp = path.with_suffix(".updated.pdf")
    doc.save(tmp, garbage=4, deflate=True)
    doc.close()
    tmp.replace(path)


for base in (ROOT / "交付文件/最终提交材料", ROOT / "项目工作区/deliverables"):
    report = base / ("报告/百年圣火_图文评审稿.pdf" if base.name == "最终提交材料" else "百年圣火_图文评审稿.pdf")
    poster = base / ("海报/百年圣火_A2海报_评审稿.pdf" if base.name == "最终提交材料" else "百年圣火_A2海报_评审稿.pdf")
    replace(report, (47, 205, 547, 241), [
        "2024年已接入329个小项的外部逐项结果，并以IOC官方赛事总数核验。",
        "原CSV自2020年起的Event泛化不可逆；视频成片及提交渠道仍待确认。",
    ], 10.2, 218, 17)
    replace(poster, (94, 1495, 750, 1540), [
        "主分析排除1906；参赛占比按记录行；2024小项结果见任务一外部结果层。",
        "衍生数据许可：CC BY-NC-SA 4.0。",
    ], 11.5, 1509, 22, background=(250/255, 249/255, 246/255))
