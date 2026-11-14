from pathlib import Path
import contextlib
import subprocess
import sys

code=Path(__file__).resolve().parent
root=code.parent
log=root/'99_运行生成'/'run_log.txt'
log.parent.mkdir(exist_ok=True)
with log.open('w',encoding='utf-8') as stream, contextlib.redirect_stdout(stream), contextlib.redirect_stderr(stream):
    print(f'Python: {sys.executable}')
    print(f'Task root: {root}')
    for name in ['audit.py','prepare.py']:
        print(f'Running {name}...')
        subprocess.run([sys.executable,str(code/name)],cwd=root,check=True)
    print('Task 1 completed successfully.')
print('Task 1 completed successfully. Details: 99_运行生成/run_log.txt')
