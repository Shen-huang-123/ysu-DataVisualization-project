"""Overlay the review comparison on the 20-page exported answer."""

import argparse
from pathlib import Path
from urllib.parse import quote

import pymupdf

TITLE = "任务三关键结论与复核"
TARGETS = (
    ("西班牙排名", "官方小项第15，运动员行第5。剔除足球后仍领先3位。",
     "S2_口径的魔力/09_奖牌口径实验室/index.html", "?ef-lens=rows&ef-noc=ESP&exclude=Football#sport-removal"),
    ("巴西主场", "五队匹配为+0.13个百分点，小项合成对照均为负。",
     "S1_东道主效应/01_来源与口径敏感性/index.html", ""),
    ("冠军延续", "固定113项下降7.37个百分点；排除后50项的区间跨零。",
     "S3_冠军的保质期/09_固定小项队列检验/index.html", "#dynasty-source-sensitivity"),
)


def publish(pdf):
    with pymupdf.open(pdf) as doc:
        if len(doc) != 20:
            raise ValueError("Expected the final 20-page answer PDF")
        page = doc[11]
        text = page.get_text()
        if TITLE in text:
            return
        if "三口径延伸" not in text:
            raise ValueError("Task three content moved. Recheck page placement.")
        panel = pymupdf.Rect(56, 544, 556, 680)
        if any(pymupdf.Rect(block[:4]).intersects(panel) for block in page.get_text("blocks")):
            raise ValueError("The evidence comparison would cover existing page content.")
        prefix = "../任务三_专题深挖/"
        for _, _, target, _ in TARGETS:
            if not (pdf.parent / prefix / target).is_file():
                raise FileNotFoundError(target)
        page.draw_rect(panel, color=(.74,.79,.81), fill=(.96,.97,.97), width=.6)
        def put(x, y, value, size, color=(.12,.23,.27)):
            page.insert_text((x,y), value, fontname="china-s", fontsize=size, color=color)
        put(68, 566, TITLE, 13)
        for index, (label, result, target, suffix) in enumerate(TARGETS):
            y = 593 + index * 31
            page.draw_line((68,y-16),(544,y-16),color=(.80,.84,.85),width=.5)
            put(68,y,label,10)
            put(135,y,result,10)
            put(478,y,"查看依据",10,(.10,.33,.46))
            page.insert_link({"kind":pymupdf.LINK_URI,
                              "from":pymupdf.Rect(476,y-12,539,y+4),
                              "uri":quote(prefix+target)+suffix})
        doc.saveIncr()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    publish(parser.parse_args().pdf)
