/* Five living rings, an understated reading line, and editorial task entries. */
(()=>{const root=document.querySelector('.ox-control');if(!root)return;const trigger=root.querySelector('.ox-trigger');
root.querySelectorAll('.ox-links b').forEach(b=>{const match=b.textContent.match(/^(\d+)\s*[·.、]?\s*(.+)$/);if(!match)return;b.textContent='';const number=document.createElement('span'),title=document.createElement('span');number.className='og-number';title.className='og-title';number.textContent=match[1];title.textContent=match[2];b.append(number,title)});
const head=root.querySelector('.ox-panel-head strong');if(head)head.textContent='探索作品';
let pending=false;function update(){pending=false;const max=Math.max(1,document.documentElement.scrollHeight-innerHeight),p=Math.max(0,Math.min(1,scrollY/max));trigger.style.setProperty('--guide-progress',p);trigger.setAttribute('aria-label',(trigger.getAttribute('aria-expanded')==='true'?'关闭':'打开')+'作品目录，阅读进度 '+Math.round(p*100)+'%')}
addEventListener('scroll',()=>{if(!pending){pending=true;requestAnimationFrame(update)}},{passive:true});addEventListener('resize',update);addEventListener('pageshow',update);update();})();
