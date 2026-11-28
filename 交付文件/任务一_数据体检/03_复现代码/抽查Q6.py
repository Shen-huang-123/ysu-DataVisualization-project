"""Recheck Q6 from the competition CSV supplied by the reviewer."""
import argparse
import json
from pathlib import Path

import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("csv", type=Path)
args = parser.parse_args()
data = pd.read_csv(args.csv, usecols=["Year", "Event", "Medal"])
medals = data[data.Medal.isin(["Gold", "Silver", "Bronze"])]
groups = medals.groupby(["Year", "Event"])
example = medals[(medals.Year == 1908) & medals.Event.eq("Athletics Men's 400 metres")]
result = {
    "同届同源小项标签同奖牌多行组": int(groups.Medal.value_counts().gt(1).sum()),
    "同届同源小项标签仅一种奖牌色组": int(groups.Medal.nunique().eq(1).sum()),
    "1908男子400米": example.Medal.value_counts().to_dict(),
}
print(json.dumps(result, ensure_ascii=False, indent=2))
