"""Attach original OCOG results-book provenance to 2008/2012 event keys.

This links each event to its sport book; it does not assert that the medal row
has been individually read or that contemporaneous results are current.
"""
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[2]
INV=ROOT/'资料文件'/'外部核验'/'官方成绩册索引'/'北京2008_伦敦2012_官方分项成绩册索引.csv'
MAN=ROOT/'资料文件'/'外部核验'/'官方成绩册索引'/'官方成绩册下载校验清单.csv'
QUEUE=ROOT/'交付文件'/'任务三_专题深挖'/'S2_口径的魔力'/'08_逐项外部核验'/'历史899项风险优先核验清单.csv'
OUT=QUEUE.parent/'2008_2012小项至官方成绩册索引.csv'
books=pd.read_csv(INV).merge(pd.read_csv(MAN),on=['Year','LA84_id','pdf_url'],validate='one_to_one')
assert books.status.eq('PDF完整下载').all()
books['book_sport']=books.Title.str.split(r' Official Results Book|\. Official Results Book',regex=True).str[0].str.strip()
queue=pd.read_csv(QUEUE).query('Year in [2008,2012]').copy()
def book_name(r):
    s=r.Sport;e=r.Event;y=r.Year
    if s=='Equestrianism':return 'Equestrian'
    if s=='Canoeing':return ('Canoe/Kayak Slalom' if 'Slalom' in e else 'Canoe/Kayak Flatwater Racing') if y==2008 else ('Canoe Slalom' if 'Slalom' in e else 'Canoe Sprint')
    if s=='Cycling':
        if 'BMX' in e:return 'Cycling BMX'
        if 'Mountainbike' in e:return 'Cycling Mountain Bike'
        if 'Road Race' in e or 'Time Trial' in e:return 'Cycling Road'
        return 'Cycling Track'
    if s=='Gymnastics':return 'Artistic Gymnastics' if y==2008 else 'Gymnastics Artistic'
    if s=='Rhythmic Gymnastics':return 'Rhythmic Gymnastics' if y==2008 else 'Gymnastics Rhythmic'
    if s=='Trampolining':return 'Trampoline Gymnastics' if y==2008 else 'Gymnastics Trampoline'
    return s
queue['book_sport']=queue.apply(book_name,axis=1)
z=queue.merge(books[['Year','book_sport','LA84_id','Title','file','sha256','pdf_url']],on=['Year','book_sport'],how='left',validate='many_to_one')
assert z.file.notna().all(),z[z.file.isna()][['Year','Event','book_sport']].to_string(index=False)
z['核验级别']='已定位并保存该运动官方赛时成绩册；小项奖牌尚待逐页确认'
z[['Year','Sport','Event','优先级','待核原因','book_sport','Title','LA84_id','file','sha256','pdf_url','核验级别']].to_csv(OUT,index=False,encoding='utf-8-sig')
print('Event-to-book links:',len(z),'high risk:',int(z['优先级'].eq(1).sum()))
