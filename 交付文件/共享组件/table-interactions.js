(()=>{
 function prepare(){document.querySelectorAll('#host-source-sensitivity table').forEach(table=>{
 table.classList.add('ut-interactive');
 table.querySelectorAll('tbody tr').forEach(row=>{row.tabIndex=0;row.title='点击或按 Enter 标记此行，再次操作取消；Esc 清除';});
 });}
 function toggle(row){if(!row)return;const selected=row.hasAttribute('data-ut-selected');row.closest('table').querySelectorAll('[data-ut-selected]').forEach(r=>r.removeAttribute('data-ut-selected'));if(!selected)row.setAttribute('data-ut-selected','');}
 document.addEventListener('click',e=>{if(e.target.closest('a,button,input,select'))return;toggle(e.target.closest('table.ut-interactive tbody tr'));});
 document.addEventListener('keydown',e=>{const row=e.target.closest('table.ut-interactive tbody tr');if(row&&(e.key==='Enter'||e.key===' ')){e.preventDefault();toggle(row);}if(e.key==='Escape')document.querySelectorAll('[data-ut-selected]').forEach(r=>r.removeAttribute('data-ut-selected'));});
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',prepare);else prepare();
})();
