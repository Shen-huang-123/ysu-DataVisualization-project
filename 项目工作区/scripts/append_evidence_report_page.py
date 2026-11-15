"""Append one evidence-grade page to the rebuilt 19-page unified report."""
from pathlib import Path
from tempfile import TemporaryDirectory

import pymupdf as fitz
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[2]
REPORT = ROOT / '交付文件/最终提交材料/报告/百年圣火_正式报告.pdf'
FIGURE = ROOT / '交付文件/最终提交材料/证据等级与历史反例/证据等级图.png'

def append_page():
    assert REPORT.exists() and FIGURE.exists()
    pdfmetrics.registerFont(TTFont('EvidenceSimHei', r'C:\Windows\Fonts\simhei.ttf'))
    width, height = A4
    with TemporaryDirectory(dir=ROOT / '项目工作区') as tmp:
        temp = Path(tmp)
        page_file = temp / 'evidence-page.pdf'
        c = canvas.Canvas(str(page_file), pagesize=A4)
        c.setFillColor(HexColor('#faf9f6'))
        c.rect(0, 0, width, height, fill=1, stroke=0)
        c.setFont('EvidenceSimHei', 9)
        c.setFillColor(HexColor('#526574'))
        c.drawString(43, 798, '百年圣火  /  晓组织 · 燕山大学')
        c.setStrokeColor(HexColor('#dbe4e8'))
        c.line(43, 787, width - 43, 787)
        c.setFillColor(HexColor('#ad3658'))
        c.drawString(43, 758, '附页  /  证据等级与历史反例')
        c.setFillColor(HexColor('#162b3a'))
        c.setFont('EvidenceSimHei', 20)
        c.drawString(43, 725, '主结论以2024为锚，历史负责挑战它')
        c.setFont('EvidenceSimHei', 10)
        for y, line in [
            (694, '2024逐项结果层给出329个比赛单元；原CSV的运动员行解释获奖成员规模。'),
            (675, '历史三届的555项已有独立二次对照，但仍不能称现行IOC逐项授牌。'),
        ]:
            c.drawString(43, y, line)
        c.drawImage(ImageReader(str(FIGURE)), 42, 325, width=width-84, height=310, preserveAspectRatio=True, anchor='c')
        c.setFont('EvidenceSimHei', 10)
        for y, line in [
            (281, '复算反例：2008现代五项铜牌转授后，代表团名次不变。'),
            (262, '2012皮划艇C1 200米银铜重分配后，立陶宛34→35，挪威35→34；前十不变。'),
            (243, '这只检验已明确的两项事后变化，不能推论全部历史小项现行授牌无误。'),
        ]:
            c.drawString(43, y, line)
        c.setFillColor(HexColor('#526574'))
        c.setFont('EvidenceSimHei', 8.6)
        for y, line in [
            (188, '来源与复算：任务三S2历史555项独立交叉对照、双来源核验报告；'),
            (172, '最终提交材料/证据等级与历史反例/证据等级与历史反例_复算结果.json。'),
            (156, '2012举重69公斤级只确认原铜撤销，继任授牌没有纳入确定性重排。'),
        ]:
            c.drawString(43, y, line)
        c.setStrokeColor(HexColor('#dbe4e8'))
        c.line(43, 52, width-43, 52)
        c.drawString(43, 35, '1896—2024 夏季奥运数据观察  |  官方逐项、历史代理与事后裁决分层使用')
        c.drawString(width-65, 35, '20')
        c.showPage()
        c.save()
        source = fitz.open(REPORT)
        assert len(source) == 19, f'Expected 19-page base report, got {len(source)}'
        extra = fitz.open(page_file)
        source.insert_pdf(extra)
        out = temp / 'unified-report.pdf'
        source.save(out, garbage=4, deflate=True)
        extra.close(); source.close()
        REPORT.write_bytes(out.read_bytes())
    assert len(fitz.open(REPORT)) == 20
    print(REPORT)

if __name__ == '__main__':
    append_page()
