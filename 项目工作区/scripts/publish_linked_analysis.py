"""Build offline linked-analysis datasets and mount them in the three delivery pages."""
from pathlib import Path
from collections import Counter
import json
import os
import re

import pandas as pd
from task2_localization import NOC_ZH, SPORT_ZH

ROOT = Path(__file__).resolve().parents[2] / "交付文件"
HISTORY = ROOT / "任务二_百年全景/05_交互总览"
INTERVAL = ROOT / "任务四_开放创作/05_满分升级/16_预测区间时序核验"
S2 = ROOT / "任务三_专题深挖/S2_口径的魔力"
REPLAY = S2 / "08_逐项外部核验/IOC现行结果补证进度_20261121"
SOURCE = ROOT / "任务一_数据体检/02_交付数据"


def publish(page, kind, data, anchor):
    source = page.read_bytes()
    source = re.sub(rb"<!-- linked-analysis:start -->.*?<!-- linked-analysis:end -->", b"", source, flags=re.S)
    source = re.sub(rb"<!-- linked-entry:start -->.*?<!-- linked-entry:end -->", b"", source, flags=re.S)
    labels = {"history": "比较代表团的两届获奖变化", "interval": "查看逐届、逐队区间对照", "replay": "勾选更正并复算奖牌榜"}
    entry = f'<!-- linked-entry:start --><p><a href="#linked-{kind}">{labels[kind]} ↓</a></p><!-- linked-entry:end -->'
    source = re.sub(rb"<main\b[^>]*>", lambda match: match[0] + entry.encode(), source, count=1)
    target = re.search(anchor, source)
    if not target:
        raise ValueError(f"Missing mount point in {page}")
    shared = Path(os.path.relpath(ROOT / "共享组件", page.parent)).as_posix()
    markup = f"""<!-- linked-analysis:start --><section class="linked-analysis" id="linked-{kind}" data-analysis="{kind}"></section>
<link rel="stylesheet" href="{shared}/linked-analysis.css">
<script defer src="{kind}-analysis-data.js"></script>
<script defer src="{shared}/linked-analysis.js"></script><!-- linked-analysis:end -->"""
    page.write_bytes(source[:target.start()] + markup.encode() + source[target.start():])
    display = {"names": NOC_ZH, "rows": data}
    if kind == "history":
        display["sports"] = SPORT_ZH
    payload = json.dumps(display, ensure_ascii=False, allow_nan=False, separators=(",", ":"))
    page.with_name(f"{kind}-analysis-data.js").write_text(f"window.linkedAnalysisData = {payload};\n", encoding="utf-8")


def history():
    fields = ["source_row", "NOC", "Year", "sport_family", "Event", "Medal", "Name", "include_main", "is_medal"]
    frame = pd.read_csv(SOURCE / "归一数据_保留原始字段.csv.gz", usecols=fields)
    frame = frame.loc[frame.include_main & frame.is_medal, fields[:-2]].fillna("")
    publish(HISTORY / "index.html", "history", frame.values.tolist(), rb'</main>')


def interval():
    fields = ["Year", "校准届次", "区间方法", "NOC", "预测", "实际", "下限", "上限"]
    frame = pd.read_csv(INTERVAL / "逐队区间与覆盖.csv")
    frame = frame.loc[frame["模型"].eq("历史加权基线"), fields]
    by_team = frame.groupby(["Year", "校准届次", "NOC"])
    assert by_team["区间方法"].nunique().eq(2).all()
    assert by_team[["预测", "实际"]].nunique().eq(1).all().all()
    publish(INTERVAL / "index.html", "interval", frame.values.tolist(), rb'<details class="delegation-intervals"')


def standings(totals):
    ordered = sorted(((tuple(counts), code) for code, counts in totals.items() if any(counts)), reverse=True)
    ranks = {}
    previous = None
    for index, (counts, code) in enumerate(ordered, 1):
        if counts != previous:
            rank = index
        ranks[code] = (rank, counts)
        previous = counts
    return ranks


def replay():
    ledger = pd.read_csv(REPLAY / "优先分歧逐项复核.csv", keep_default_na=False)
    colors = ["Gold", "Silver", "Bronze"]
    data = {}
    for year, cases in ledger.groupby("Year"):
        base = pd.read_csv(S2 / "02_数据表" / f"S2_{year}历史小项代理表.csv", keep_default_na=False).set_index("Event")
        assert base.index.is_unique and len(base) == 302
        entries = cases.to_dict("records")
        for case in entries:
            base.loc[case["Event"], colors] = ["" if code == "空" else code for code in case["原金银铜"].split("/")]
        totals = Counter((code, color) for color in colors for value in base[color] for code in value.split("|") if code)
        before = standings({code: [totals[code, color] for color in colors] for code, _ in totals})
        masks = []
        for mask in range(1 << len(entries)):
            current = totals.copy()
            for i, case in enumerate(entries):
                if mask & (1 << i):
                    for color, old, new in zip(colors, case["原金银铜"].split("/"), case["核对金银铜"].split("/")):
                        for code in old.split("|"):
                            if code != "空":
                                current[code, color] -= 1
                        for code in new.split("|"):
                            current[code, color] += 1
            after = standings({code: [current[code, color] for color in colors] for code, _ in current})
            empty = (None, (0, 0, 0))
            masks.append([[code, *before.get(code, empty), *after.get(code, empty)]
                          for code in sorted(before.keys() | after.keys()) if before.get(code) != after.get(code)])
        expected = pd.read_csv(REPLAY / "优先分歧名次复算.csv")
        expected = expected[(expected.Year == year) & (expected["案例"] == "同届全部分歧同时更正")]
        expected_moves = set(expected.loc[expected["原排名"].ne(expected["更新排名"]), "NOC"])
        assert {code for code, old, _, new, _ in masks[-1] if old != new} == expected_moves
        data[str(year)] = [entries, masks]
    publish(REPLAY / "优先分歧复核与复算.html", "replay", data, rb'<h2[^>]*>[^<]*' + "逐项证据与名次复算".encode())


if __name__ == "__main__":
    history()
    interval()
    replay()
