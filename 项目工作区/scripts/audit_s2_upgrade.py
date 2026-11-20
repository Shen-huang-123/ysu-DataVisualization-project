from pathlib import Path
import sys,contextlib,io,json
import pandas as pd
root=Path(__file__).resolve().parents[2];sys.path.insert(0,str(root/'项目工作区/scripts'))
out=root/'项目工作区/outputs/s2_upgrade_audit'
for part in ['02_数据表','04_核心图表','06_交互榜']:(out/part).mkdir(parents=True,exist_ok=True)
source=root/'项目工作区/scripts/task3_s2_upgrade.py';t=source.read_text(encoding='utf8').replace("TASK=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'",'TASK=Path('+repr(str(out))+')')
with contextlib.redirect_stdout(io.StringIO()):exec(compile(t,str(source),'exec'),{'__file__':str(source),'__name__':'__main__'})
ref=root/'交付文件/任务三_专题深挖/S2_口径的魔力';checks=[]
for f in (out/'02_数据表').glob('*.csv'):
 pd.testing.assert_frame_equal(pd.read_csv(f),pd.read_csv(ref/'02_数据表'/f.name),check_exact=False,rtol=1e-8,atol=1e-8);checks.append({'file':f.name,'match':True})
a=json.loads((out/'02_数据表/S2_升级关键指标.json').read_text(encoding='utf8'));b=json.loads((ref/'02_数据表/S2_升级关键指标.json').read_text(encoding='utf8'));a.pop('dashboard',None);b.pop('dashboard',None);assert a==b
report={'isolated':True,'checks':checks,'metrics_match_excluding_output_path':True,'generated_dashboard':(out/'06_交互榜/index.html').exists(),'archives_present':len(list((root/'交付文件').rglob('*.zip')))+len(list((root/'交付文件').rglob('*.7z'))),'limits':['交互页仅确认生成，未覆盖当前页面','当前无ZIP/7z，未声称打包完成','未重新访问外部历史来源']}
(root/'项目工作区/S2升级生成核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
