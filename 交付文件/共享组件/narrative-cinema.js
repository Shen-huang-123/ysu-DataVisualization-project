/* Offline GSAP choreography: no pinning, snapping, opacity-zero content or body transforms. */
(()=>{
 const body=document.body;if(!body.matches('.narrative-module'))return;
 const chapters=[...document.querySelectorAll('.narrative-chapter')],links=[...document.querySelectorAll('.narrative-route a')],scenes=[...document.querySelectorAll('.narrative-cinema')];
 let frame=0;
 function measure(){frame=0;const y=innerHeight*.35;chapters.forEach((c,i)=>{const r=c.getBoundingClientRect();const progress=Math.max(0,Math.min(1,(y-r.top)/Math.max(1,r.height)));links[i]?.style.setProperty('--chapter-progress',progress.toFixed(3));c.classList.toggle('is-reading',r.top<innerHeight*.7&&r.bottom>innerHeight*.25)})}
 function schedule(){if(!frame)frame=requestAnimationFrame(measure)}
 addEventListener('scroll',schedule,{passive:true});addEventListener('resize',schedule);measure();
 const g=window.gsap,ST=window.ScrollTrigger;if(!g||!ST)return;g.registerPlugin(ST);
 const mm=g.matchMedia();
 mm.add('(prefers-reduced-motion: no-preference)',()=>{
  const mobile=matchMedia('(max-width:700px)').matches;
  scenes.forEach(scene=>{
   const image=scene.querySelector('img'),caption=scene.querySelector('figcaption');
   g.fromTo(image,{yPercent:mobile?-2:-5,scale:1.06},{yPercent:mobile?2:5,scale:1.015,ease:'none',scrollTrigger:{trigger:scene,start:'top bottom',end:'bottom top',scrub:.7}});
   g.fromTo(caption,{y:22,opacity:.65},{y:0,opacity:1,ease:'none',scrollTrigger:{trigger:scene,start:'top 80%',end:'center 60%',scrub:.45}});
  });
  chapters.forEach(c=>{
   const title=c.querySelector('h2');if(!title)return;
   g.fromTo(title,{y:16,opacity:.62},{y:0,opacity:1,duration:.7,ease:'power2.out',immediateRender:false,scrollTrigger:{trigger:title,start:'top 92%',toggleActions:'play none none none',once:true}});
  });
 });
 let refreshTimer;function refresh(){clearTimeout(refreshTimer);refreshTimer=setTimeout(()=>ST.refresh(),100)}
 document.querySelector('main').addEventListener('toggle',refresh,true);
 document.querySelector('main').addEventListener('click',e=>{if(e.target.closest('[data-filter]'))refresh()});
 scenes.forEach(s=>{const img=s.querySelector('img');if(!img.complete)img.addEventListener('load',refresh,{once:true})});
 addEventListener('pageshow',refresh);document.fonts?.ready.then(refresh);
})();
