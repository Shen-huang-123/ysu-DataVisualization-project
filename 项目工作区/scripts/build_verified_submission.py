from pathlib import Path
import subprocess,zipfile,hashlib,json,datetime
root=Path(__file__).resolve().parents[2];out=root/'项目工作区/outputs/submission';out.mkdir(parents=True,exist_ok=True)
rev=subprocess.check_output(['git','rev-parse','HEAD'],cwd=root).decode().strip()
files=[Path(x) for x in subprocess.check_output(['git','ls-files','-z'],cwd=root).decode('utf8').split('\0') if x]
files=[p for p in files if not any(x in p.parts for x in ['.git','.codex','.agents','qa_visual','node_modules','outputs']) and p.suffix.lower() not in ['.zip','.7z'] and (root/p).is_file()]
name='百年圣火_完整离线提交包_'+rev[:8];archive=out/(name+'.zip');extract=out/(name+'_解压验收');extract.mkdir(exist_ok=True)
manifest=[]
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=3) as z:
 for rel in files:
  data=(root/rel).read_bytes()
  if rel.suffix.lower()=='.pdf' and data.startswith(b'version https://git-lfs'):raise RuntimeError('LFS pointer: '+str(rel))
  manifest.append({'path':rel.as_posix(),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()});z.writestr(rel.as_posix(),data)
 z.writestr('提交包文件清单.json',json.dumps({'source_commit':rev,'files':manifest},ensure_ascii=False,indent=2))
with zipfile.ZipFile(archive) as z:
 assert z.testzip() is None;z.extractall(extract)
for x in manifest:assert hashlib.sha256((extract/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
report={'source_commit':rev,'archive':str(archive.relative_to(root)),'archive_bytes':archive.stat().st_size,'file_count':len(files),'crc_pass':True,'extracted_hashes_pass':True,'extracted_root':str(extract.relative_to(root)),'limits':['本机独立目录解压验收，不等于第二台设备','视频成片及实际提交渠道仍由团队确认']}
(root/'项目工作区/提交包验收.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8');print(json.dumps(report,ensure_ascii=False))
