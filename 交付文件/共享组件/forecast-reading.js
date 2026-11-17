/* Keep anchor links and lazily sized charts usable inside the legacy archive. */
(()=>{
  const archive=document.getElementById('legacy-scenarios');
  if(!archive)return;
  const refresh=()=>requestAnimationFrame(()=>{
    dispatchEvent(new Event('resize'));
    if(window.ScrollTrigger)window.ScrollTrigger.refresh();
  });
  const reveal=hash=>{
    let target;try{target=document.getElementById(decodeURIComponent(hash.replace(/^#/,'')))}catch{return}
    if(!target||!archive.contains(target))return;
    archive.open=true;refresh();
    requestAnimationFrame(()=>target.scrollIntoView({block:'start',behavior:'auto'}));
  };
  archive.addEventListener('toggle',()=>{if(archive.open)refresh()});
  addEventListener('hashchange',()=>reveal(location.hash));
  document.addEventListener('click',e=>{
    const a=e.target.closest('a[href]');if(!a)return;
    const url=new URL(a.href,location.href);
    if(url.pathname===location.pathname&&url.hash)reveal(url.hash);
  });
  if(location.hash)reveal(location.hash);
})();
