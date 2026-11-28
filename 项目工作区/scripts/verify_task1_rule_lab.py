"""Validate the delivered experiment against a clean run from the contest CSV."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

import pandas as pd
from publish_task1_rule_lab import TASK, RESULTS, build_payload

parser = argparse.ArgumentParser()
parser.add_argument("csv", type=Path)
args = parser.parse_args()
env = {**os.environ, "OLYMPICS_CSV": str(args.csv.resolve()), "PYTHONUTF8": "1"}
with TemporaryDirectory() as temp:
    root = Path(temp)
    scripts = root / "code"
    scripts.mkdir()
    for name in ("audit.py", "prepare.py"):
        target = scripts / name
        shutil.copyfile(TASK / "03_复现代码" / name, target)
        subprocess.run([sys.executable, str(target)], cwd=root, env=env, check=True)
    generated = root / "99_运行生成"
    for file in ("edition_main.csv", "edition_exclude_duplicate_excess.csv",
                 "edition_include_1906.csv", "event_quality_by_year.csv"):
        pd.testing.assert_frame_equal(pd.read_csv(generated/file), pd.read_csv(RESULTS/file))
    audit = Path("04_质量检查结果/audit.json")
    assert json.loads((root/audit).read_text(encoding="utf8")) == json.loads((TASK/audit).read_text(encoding="utf8"))
    actual = build_payload(generated / "olympics_flagged.csv.gz", generated)
    embedded = (TASK / "规则实验台数据.js").read_text(encoding="utf8")
    expected = json.loads(embedded.removeprefix("window.auditLabData = ").strip().removesuffix(";"))
    assert json.loads(json.dumps(actual, ensure_ascii=False)) == expected
    print("验收通过：原始 CSV 审计、四张完整数据表与实验台数据一致。")
    print("1900：604 → 591，13 对源行；2024：2281 → 2280；1906：458 条。")
