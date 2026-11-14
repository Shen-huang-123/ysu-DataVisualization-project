from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parents[2]
out=root/'交付文件/任务三_专题深挖/12_反例与证据链/两处协会页面错误_证据链.png'
plt.rcParams['font.family']='Microsoft YaHei'
fig,ax=plt.subplots(figsize=(14,7.4));fig.patch.set_facecolor('#F4F1EA');ax.set_facecolor('#F4F1EA');ax.set_xlim(0,14);ax.set_ylim(0,7.4);ax.axis('off')
ax.text(.5,6.9,'协会页面也可能错：两次原件复核改变了奖牌判断',fontsize=23,fontweight='bold',color='#173139')
ax.text(.5,6.53,'红色＝当前协会页面或接口；深色＝赛时官方成绩册；蓝绿＝研究处理决定',fontsize=10,color='#526A6D')
cases=[('伦敦 2012  女子100米自由泳','协会接口：唐奕并列银牌','官方成绩册第13页：53.44秒第3','赛时铜牌；IOC现行授牌待核'),('北京 2008  跆拳道女子蝇量级','协会页面：肯尼亚选手获铜','官方成绩册第111页：委内瑞拉、古巴获铜','不纳入肯尼亚铜牌；IOC授牌待核')]
for row,(head,wrong,source,decision) in enumerate(cases):
 y=4.38-row*2.3
 ax.text(.5,y+1.26,head,fontsize=15,fontweight='bold',color='#18343B')
 for i,(title,body,face,edge) in enumerate([('01  原判断',wrong,'#F2E0DC','#B56359'),('02  原件复核',source,'#EBEEEA','#526B6D'),('03  修正结论',decision,'#DFEDE9','#3F8991')]):
  x=.5+i*4.52
  box=FancyBboxPatch((x,y-.12),4.05,1.16,boxstyle='round,pad=.03,rounding_size=.12',facecolor=face,edgecolor=edge,lw=1.2)
  ax.add_patch(box);ax.text(x+.22,y+.7,title,fontsize=11,fontweight='bold',color=edge);ax.text(x+.22,y+.28,body,fontsize=10.2,color='#203B42')
  if i<2:ax.annotate('',xy=(x+4.47,y+.46),xytext=(x+4.09,y+.46),arrowprops=dict(arrowstyle='->',color='#546B70',lw=1.8))
ax.plot([.5,13.55],[.45,.45],color='#9AAEAA',lw=1)
ax.text(.5,.16,'来源：伦敦2012游泳官方成绩册 p.13；北京2008跆拳道官方成绩册 p.111。协会页面与原件冲突时，不把协会标签称为 IOC 最终授牌。',fontsize=9,color='#4B6266')
fig.savefig(out,dpi=200,bbox_inches='tight',facecolor=fig.get_facecolor());plt.close(fig)
print(out)
