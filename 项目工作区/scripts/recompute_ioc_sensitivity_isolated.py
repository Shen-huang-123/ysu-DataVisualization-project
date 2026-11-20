"""Run existing research scripts with OUT redirected; never publish presentation changes."""
import argparse,ast,contextlib,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def run(script,destination):
    source=ROOT/'项目工作区/scripts'/script
    class Isolate(ast.NodeTransformer):
        def visit_Assign(self,node):
            if any(isinstance(t,ast.Name) and t.id=='OUT' for t in node.targets):node.value=ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),args=[ast.Constant(str(destination))],keywords=[])
            if script=='olympedia_secondary_audit.py' and any(isinstance(t,ast.Name) and t.id=='RAW' for t in node.targets):node.value=ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),args=[ast.Constant(str(ROOT/'交付文件/任务三_专题深挖/S2_口径的魔力/08_逐项外部核验/Olympedia独立交叉核验/原始页面'))],keywords=[])
            return self.generic_visit(node)
        def visit_Expr(self,node):
            if isinstance(node.value,ast.Call) and isinstance(node.value.func,ast.Attribute) and isinstance(node.value.func.value,ast.Name) and node.value.func.value.id=='runpy':return None
            return self.generic_visit(node)
    tree=Isolate().visit(ast.parse(source.read_text(encoding='utf-8')));ast.fix_missing_locations(tree)
    destination.mkdir(parents=True,exist_ok=True)
    with (destination/'run.log').open('w',encoding='utf-8') as log,contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):exec(compile(tree,str(source),'exec'),{'__file__':str(source),'__name__':'__main__'})
    print('Completed',script,str(destination))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('script');a=parser.parse_args();run(a.script,ROOT/'项目工作区/outputs/ioc_evidence_repair_recompute'/Path(a.script).stem)
