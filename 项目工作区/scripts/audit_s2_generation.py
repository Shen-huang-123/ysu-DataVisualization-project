from pathlib import Path
import sys,contextlib,io,json
import pandas as pd
root=Path(__file__).resolve().parents[2];sys.path.insert(0,str(root/'项目工作区/scripts'))
source=root/'项目工作区/scripts/task3_s2_highscore.py';out=root/'项目工作区/outputs/s2_generation_audit';out.mkdir(parents=True,exist_ok=True)
t=source.read_text(encoding='utf8').replace("TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'",'TASK=Path('+repr(str(out))+')')
with contextlib.redirect_stdout(io.StringIO()):exec(compile(t,str(source),'exec'),{'__file__':str(source),'__name__':'__main__'})
original=root/'交付文件/任务三_专题深挖/S2_口径的魔力';checks=[]
for f in (out/'02_数据表').iterdir():
 ref=original/'02_数据表'/f.name
 if not ref.exists():continue
 if f.suffix=='.csv':pd.testing.assert_frame_equal(pd.read_csv(f),pd.read_csv(ref),check_exact=False,rtol=1e-8,atol=1e-8)
 elif f.suffix=='.json':assert json.loads(f.read_text(encoding='utf8'))==json.loads(ref.read_text(encoding='utf8'))
 else:continue
 checks.append({'file':f.name,'match':True})
report={'generator':'task3_s2_highscore.py','isolated':True,'checks':checks,'limits':['未重跑S2升级脚本、外部核验采集或全部材料打包']}
(root/'项目工作区/S2生成核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
