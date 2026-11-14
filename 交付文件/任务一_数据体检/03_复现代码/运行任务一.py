from pathlib import Path
import subprocess,sys
r=Path(__file__).resolve().parent
for n in ['audit.py','prepare.py']: subprocess.run([sys.executable,str(r/n)],check=True)
print('任务一审计与归一完成，结果见04_质量检查结果和99_运行生成目录')
