from pathlib import Path
import subprocess,sys
R=Path(__file__).resolve().parents[1]
for name in ['audit','prepare','explore','panorama','compare_2024','plot_comparison','rank_sensitivity','host_analysis','deliver','report_layout','dashboard']:
 print(f'Running {name}',flush=True)
 subprocess.run([sys.executable,str(R/'scripts'/f'{name}.py')],cwd=R,check=True)
print('All outputs generated successfully')
