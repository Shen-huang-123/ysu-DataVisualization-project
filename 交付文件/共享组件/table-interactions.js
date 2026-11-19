(()=>{
 if(window.__unifiedTableInteractions)return;window.__unifiedTableInteractions=true;
 function prepare(){document.querySelectorAll('table').forEach(table=>{
 table.classList.add('ut-interactive');
 table.querySelectorAll('tbody tr').forEach(row=>{if(row.querySelector('td')){if(!row.hasAttribute('tabindex'))row.tabIndex=0;if(!row.title)row.title='点击或按 Enter 标记此行，再次操作取消；Esc 清除';}});
 });}
 function toggle(row){if(!row)return;const selected=row.hasAttribute('data-ut-selected');row.closest('table').querySelectorAll('[data-ut-selected]').forEach(r=>r.removeAttribute('data-ut-selected'));if(!selected)row.setAttribute('data-ut-selected','');}
 document.addEventListener('click',e=>{if(e.target.closest('a,button,input,select,textarea,summary,[contenteditable=true]'))return;toggle(e.target.closest('table.ut-interactive tbody tr'));});
 document.addEventListener('keydown',e=>{const row=e.target.closest('table.ut-interactive tbody tr');if(row&&e.target===row&&(e.key==='Enter'||e.key===' ')){e.preventDefault();toggle(row);}if(e.key==='Escape')document.querySelectorAll('[data-ut-selected]').forEach(r=>r.removeAttribute('data-ut-selected'));});
 let pending=false;
 function start(){prepare();new MutationObserver(records=>{if(!records.some(r=>[...r.addedNodes].some(n=>n.nodeType===1&&(n.matches('table,tbody,tr,td')||n.querySelector('table,tbody,tr')))))return;if(!pending){pending=true;requestAnimationFrame(()=>{pending=false;prepare();});}}).observe(document.body,{childList:true,subtree:true});}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',start);else start();
})();
