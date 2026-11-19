(()=>{
 const picker=document.querySelector('.s1-picker'),bars=document.querySelector('.s1-bars');if(!picker||!bars)return;
 picker.querySelectorAll('button').forEach(b=>{const text=b.textContent.trim(),year=text.slice(0,4),name=text.slice(4).trim();b.replaceChildren();const y=document.createElement('span'),n=document.createElement('small');y.textContent=year;n.textContent=name;b.append(y,n)});
 const axis=document.createElement('div');axis.className='s1-chart-axis';axis.innerHTML='<span>获奖运动员记录份额</span><div><span>0%</span><span>5%</span><span>10%</span></div>';bars.before(axis);
 const chart=document.createElement('div');chart.className='s1-chart-group';axis.before(chart);chart.append(axis,bars);
 const announce=document.querySelector('#s1-name');announce.setAttribute('aria-live','polite');
 picker.addEventListener('keydown',e=>{const buttons=[...picker.querySelectorAll('button')],i=buttons.indexOf(document.activeElement);if(i<0)return;let next;if(e.key==='ArrowRight')next=(i+1)%buttons.length;if(e.key==='ArrowLeft')next=(i-1+buttons.length)%buttons.length;if(e.key==='Home')next=0;if(e.key==='End')next=buttons.length-1;if(next!==undefined){e.preventDefault();buttons[next].focus();buttons[next].click()}});
})();
