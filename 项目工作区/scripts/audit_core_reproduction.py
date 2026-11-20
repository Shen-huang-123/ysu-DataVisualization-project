from pathlib import Path
import re,json,hashlib,contextlib,io
import pandas as pd
root=Path(__file__).resolve().parents[2]
out=root/'项目工作区/outputs/core_reproduction_audit';out.mkdir(parents=True,exist_ok=True)
report={'hash_checks':[],'recomputed':[],'limits':['未重跑S2全量生成及正式PDF版式检查；本轮复算S1/S3来源敏感性']}
for file in (root/'交付文件/任务三_专题深挖').rglob('复算检查与输入哈希.json'):
 if not any(x in str(file) for x in ['S1_东道主','S3_冠军']):continue
 data=json.loads(file.read_text(encoding='utf8'))
 for name,expected in data['input_sha256'].items():
  actual=hashlib.sha256((root/name).read_bytes()).hexdigest();report['hash_checks'].append({'input':name,'match':actual==expected})
for script,folder,output in [('dynasty_source_sensitivity.py','S3_冠军的保质期/11_历史来源敏感性','固定队列三方案复算.csv'),('host_source_sensitivity.py','S1_东道主效应/01_来源与口径敏感性','三方案共同案例摘要.csv')]:
 target=out/script.removesuffix('.py');target.mkdir(exist_ok=True)
 source=root/'项目工作区/scripts'/script;text=source.read_text(encoding='utf8')
 text=re.sub(r'OUT=.*?;OUT.mkdir\(exist_ok=True\)', lambda _: 'OUT=Path('+repr(str(target))+');OUT.mkdir(exist_ok=True)',text,count=1)
 text=text.split('import runpy')[0]
 with contextlib.redirect_stdout(io.StringIO()):exec(compile(text,str(source),'exec'),{'__file__':str(source),'__name__':'__main__'})
 a=pd.read_csv(root/'交付文件/任务三_专题深挖'/folder/output);b=pd.read_csv(target/output)
 pd.testing.assert_frame_equal(a,b,check_exact=False,rtol=1e-8,atol=1e-8)
 report['recomputed'].append({'script':script,'csv':output,'match':True,'rows':len(a)})
print(json.dumps(report,ensure_ascii=False,indent=2))
(root/'项目工作区/核心专题复算核验.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
