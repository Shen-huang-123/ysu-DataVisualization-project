import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import data from './data.json';

const $ = id => document.getElementById(id);
const reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;
const years = data.editions.map(d => d.year);
const state = {index: years.length - 1, noc: 'CHN', sport: 'Skateboarding', timer: null};
const ink = '#adc4cb', grid = '#ffffff19', blue = '#77cee8', gold = '#f1c478';
const echarts = window.echarts;
const charts = {
  scale: echarts.init($('scale-chart')),
  country: echarts.init($('country-chart')),
  sport: echarts.init($('sport-chart')),
};
const fmt = n => Number(n).toLocaleString('zh-CN');

for (const [noc, name] of Object.entries(data.nocNames)) {
  const option = document.createElement('option'); option.value = noc; option.textContent = name; $('country-select').append(option);
}
$('country-select').value = state.noc;
for (const sport of data.sportSeries) {
  const option = document.createElement('option'); option.value = sport.key; option.textContent = sport.name; $('sport-select').append(option);
}
$('sport-select').value = state.sport;

const common = {
  animationDuration: reduced ? 0 : 650,
  textStyle: {fontFamily:'Microsoft YaHei, sans-serif',color:ink},
  tooltip: {trigger:'axis',backgroundColor:'#102c39',borderColor:'#688592',textStyle:{color:'#f4f4ee'},extraCssText:'border-radius:10px;box-shadow:0 15px 35px #0007'},
};
const axisLabel = (max=8) => ({color:ink,interval:Math.max(0,Math.ceil(years.length/(innerWidth<760?4:max))-1)});
const axisLine = {lineStyle:{color:'#48636f'}};
const splitLine = {lineStyle:{color:grid}};
const markerLine = year => ({silent:true,symbol:'none',lineStyle:{color:gold,width:1.5,type:'dashed',opacity:.85},label:{show:false},data:[{xAxis:String(year)}]});

function drawCharts() {
  const selected = data.editions[state.index];
  charts.scale.setOption({...common,grid:{left:54,right:52,top:28,bottom:35,containLabel:true},
    legend:{top:0,right:8,textStyle:{color:ink,fontSize:11}},
    xAxis:{type:'category',data:years.map(String),boundaryGap:false,axisLabel:axisLabel(),axisLine},
    yAxis:[{type:'value',axisLabel:{color:ink,formatter:v=>v>=1000?`${v/1000}千`:v},splitLine},{type:'value',axisLabel:{color:ink},splitLine:{show:false}}],
    series:[{name:'参赛行数',type:'line',smooth:.18,showSymbol:false,lineStyle:{color:blue,width:3},itemStyle:{color:blue},areaStyle:{color:'#77cee814'},markLine:markerLine(selected.year),data:data.editions.map(d=>d.records)},
      {name:'代表团',type:'line',yAxisIndex:1,smooth:.18,showSymbol:false,lineStyle:{color:gold,width:3},itemStyle:{color:gold},data:data.editions.map(d=>d.delegations)}]});
  const series = data.delegationSeries[state.noc];
  const byYear = new Map(series.map(d=>[d.year,d]));
  const values = years.map(y=>byYear.get(y)?.present ? byYear.get(y).medalShare : null);
  charts.country.setOption({...common,grid:{left:54,right:19,top:20,bottom:38,containLabel:true},
    xAxis:{type:'category',data:years.map(String),boundaryGap:false,axisLabel:axisLabel(6),axisLine},
    yAxis:{type:'value',min:0,axisLabel:{color:ink,formatter:'{value}%'},splitLine},
    tooltip:{...common.tooltip,formatter:p=>{const y=+p[0]?.axisValue,v=byYear.get(y);return `${y} 年 · ${data.nocNames[state.noc]}<br>${v?.present?`获奖行份额 <b>${v.medalShare}%</b>`:'未参赛或无可用记录'}`}},
    series:[{type:'line',data:values,connectNulls:false,showSymbol:false,smooth:.12,lineStyle:{color:blue,width:3},itemStyle:{color:blue},areaStyle:{color:'#77cee813'},markLine:markerLine(selected.year)}]});
  const here=byYear.get(selected.year);
  $('country-readout').textContent=`${selected.year} · ${data.nocNames[state.noc]}：${here?.present&&here.medalShare!==null?`获奖行份额 ${here.medalShare}%`:'缺席或无可用记录'}`;
  const sport=data.sportSeries.find(s=>s.key===state.sport);
  charts.sport.setOption({...common,grid:{left:35,right:18,top:21,bottom:38,containLabel:true},
    xAxis:{type:'category',data:years.map(String),axisLabel:axisLabel(6),axisLine},
    yAxis:{type:'value',min:0,max:1,interval:1,axisLabel:{color:ink,formatter:v=>v===1?'出现':'未出现'},splitLine},
    tooltip:{...common.tooltip,formatter:p=>`${p[0].axisValue} 年 · ${sport.name}<br>${p[0].value?'出现于本届项目表':'未出现于本届项目表'}`},
    series:[{type:'bar',barMaxWidth:17,data:sport.present.map((v,i)=>({value:v,itemStyle:{color:i===state.index?gold:'#69bcd5',opacity:v?1:.05,borderRadius:[3,3,0,0]}})),markLine:markerLine(selected.year)}]});
  const presentYears=sport.present.reduce((a,v,i)=>(v&&a.push(years[i]),a),[]);
  $('sport-readout').textContent=`${selected.year} · ${sport.name}：${sport.present[state.index]?'出现':'未出现'}；样本 30 届中出现 ${presentYears.length} 届。`;
}

let globe = null;
function vector(lat,lon,r=1) {
  const phi=(90-lat)*Math.PI/180, theta=(lon+180)*Math.PI/180;
  return new THREE.Vector3(-r*Math.sin(phi)*Math.cos(theta),r*Math.cos(phi),r*Math.sin(phi)*Math.sin(theta));
}
function createGlobe() {
  const container=$('globe');
  const scene=new THREE.Scene();
  const camera=new THREE.PerspectiveCamera(42,1,.1,100);camera.position.set(0,.2,4.3);
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true,powerPreference:'high-performance'});
  renderer.setPixelRatio(Math.min(devicePixelRatio,1.7));
  renderer.setSize(container.clientWidth,container.clientHeight);
  renderer.outputColorSpace=THREE.SRGBColorSpace;
  container.appendChild(renderer.domElement);
  const controls=new OrbitControls(camera,renderer.domElement);
  controls.enablePan=false;controls.enableDamping=!reduced;controls.dampingFactor=.065;controls.minDistance=2.8;controls.maxDistance=6;controls.rotateSpeed=.65;
  scene.add(new THREE.AmbientLight(0x7199aa,1.1));
  const light=new THREE.DirectionalLight(0xc8e8f0,2.0);light.position.set(3,2,4);scene.add(light);
  const planet=new THREE.Group();scene.add(planet);
  const earth=new THREE.Mesh(new THREE.SphereGeometry(1,64,48),new THREE.MeshPhongMaterial({color:0x123746,emissive:0x05202c,specular:0x41849a,shininess:35}));planet.add(earth);
  const aura=new THREE.Mesh(new THREE.SphereGeometry(1.12,48,32),new THREE.ShaderMaterial({transparent:true,depthWrite:false,side:THREE.BackSide,uniforms:{glowColor:{value:new THREE.Color(0x5ac4de)}},vertexShader:'varying vec3 vNormal;varying vec3 vWorld;void main(){vNormal=normalize(normalMatrix*normal);vec4 world=modelMatrix*vec4(position,1.0);vWorld=world.xyz;gl_Position=projectionMatrix*viewMatrix*world;}',fragmentShader:'varying vec3 vNormal;varying vec3 vWorld;uniform vec3 glowColor;void main(){float a=pow(1.0-abs(dot(normalize(vNormal),normalize(cameraPosition-vWorld))),2.5);gl_FragColor=vec4(glowColor,a*.25);}' }));planet.add(aura);
  const vertices=[];
  for(const ring of data.geography){for(let i=1;i<ring.length;i++){const a=vector(ring[i-1][1],ring[i-1][0],1.009),b=vector(ring[i][1],ring[i][0],1.009);if(a.distanceTo(b)<.17)vertices.push(...a.toArray(),...b.toArray());}}
  const coastGeometry=new THREE.BufferGeometry();coastGeometry.setAttribute('position',new THREE.Float32BufferAttribute(vertices,3));
  planet.add(new THREE.LineSegments(coastGeometry,new THREE.LineBasicMaterial({color:0x72b6bd,transparent:true,opacity:.72})));
  for(let lat=-60;lat<=60;lat+=30){const points=[];for(let lon=-180;lon<=180;lon+=4)points.push(vector(lat,lon,1.005));planet.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(points),new THREE.LineBasicMaterial({color:0x78adbc,transparent:true,opacity:.13})));}
  const markerMeshes=[];
  data.editions.forEach((edition,i)=>{
    const position=vector(edition.lat,edition.lon,1.055);
    const material=new THREE.MeshBasicMaterial({color:i===state.index?0xf2c474:0x78d5e7,transparent:true,opacity:i===state.index?1:.73});
    const mesh=new THREE.Mesh(new THREE.SphereGeometry(i===state.index?.027:.015,12,8),material);
    mesh.position.copy(position);mesh.userData.index=i;planet.add(mesh);markerMeshes.push(mesh);
  });
  const pulse=new THREE.Mesh(new THREE.RingGeometry(.039,.046,48),new THREE.MeshBasicMaterial({color:0xf2c474,transparent:true,opacity:.85,side:THREE.DoubleSide,depthWrite:false}));planet.add(pulse);
  const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();let hovering=-1;
  function pick(e){const rect=container.getBoundingClientRect();pointer.set((e.clientX-rect.left)/rect.width*2-1,-(e.clientY-rect.top)/rect.height*2+1);raycaster.setFromCamera(pointer,camera);const hits=raycaster.intersectObjects([earth,...markerMeshes],false);return hits[0]?.object===earth?-1:(hits[0]?.object?.userData?.index??-1)}
  container.addEventListener('pointermove',e=>{hovering=pick(e);const tip=$('globe-tooltip');if(hovering>=0){const d=data.editions[hovering];tip.textContent=`${d.year} · ${d.city}`;tip.hidden=false;tip.style.left=`${Math.min(container.clientWidth-90,Math.max(90,e.offsetX))}px`;tip.style.top=`${Math.max(25,e.offsetY-47)}px`;}else tip.hidden=true;});
  container.addEventListener('pointerleave',()=>{$('globe-tooltip').hidden=true;hovering=-1});
  let down=null;container.addEventListener('pointerdown',e=>{down=[e.clientX,e.clientY]});
  container.addEventListener('pointerup',e=>{if(down&&Math.hypot(e.clientX-down[0],e.clientY-down[1])<5&&hovering>=0)select(hovering);down=null});
  let targetRotation=0;
  function focus(index){const d=data.editions[index],v=vector(d.lat,d.lon);targetRotation=-Math.atan2(v.x,v.z);const current=planet.rotation.y;while(targetRotation-current>Math.PI)targetRotation-=2*Math.PI;while(targetRotation-current<-Math.PI)targetRotation+=2*Math.PI;
    markerMeshes.forEach((m,i)=>{m.material.color.setHex(i===index?0xf2c474:0x78d5e7);m.material.opacity=i===index?1:.73;m.scale.setScalar(i===index?1.8:1)});
    pulse.position.copy(vector(d.lat,d.lon,1.065));pulse.quaternion.setFromUnitVectors(new THREE.Vector3(0,0,1),vector(d.lat,d.lon).normalize());}
  const resize=()=>{const w=container.clientWidth,h=container.clientHeight;if(w&&h){camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h);}};
  new ResizeObserver(resize).observe(container);resize();focus(state.index);
  const clock=new THREE.Clock();
  function render(){requestAnimationFrame(render);if(document.hidden)return;const t=clock.getElapsedTime();if(!reduced){planet.rotation.y+=(targetRotation-planet.rotation.y)*.055;pulse.scale.setScalar(1+.23*Math.sin(t*2.7));pulse.material.opacity=.55+.35*Math.sin(t*2.7);}else planet.rotation.y=targetRotation;controls.update();renderer.render(scene,camera)}
  render();return {focus,resize};
}
try {globe=createGlobe();}catch(e){console.warn('WebGL unavailable:',e);$('globe-fallback').hidden=false;}

function select(index){state.index=Math.max(0,Math.min(years.length-1,index));const d=data.editions[state.index];
  $('year-label').textContent=d.year;$('city-label').textContent=d.city;$('edition-note').textContent=`第 ${state.index+1} 个数据届次 · 夏季奥运`;
  $('records-value').textContent=fmt(d.records);$('delegations-value').textContent=fmt(d.delegations);$('female-value').textContent=d.female.toFixed(1)+'%';
  $('coordinate-label').textContent=`${Math.abs(d.lat).toFixed(2)}° ${d.lat>=0?'N':'S'} · ${Math.abs(d.lon).toFixed(2)}° ${d.lon>=0?'E':'W'}`;
  $('year-slider').value=state.index;$('year-slider').style.setProperty('--pct',`${state.index/(years.length-1)*100}%`);
  $('dock-year').textContent=`${d.year} ${d.city}`;$('progress').textContent=`${state.index+1} / ${years.length}`;
  globe?.focus(state.index);drawCharts();}
$('previous').addEventListener('click',()=>select(state.index-1));$('next').addEventListener('click',()=>select(state.index+1));
$('year-slider').addEventListener('input',e=>select(+e.target.value));
$('country-select').addEventListener('change',e=>{state.noc=e.target.value;drawCharts()});
$('sport-select').addEventListener('change',e=>{state.sport=e.target.value;drawCharts()});
$('play').addEventListener('click',()=>{if(state.timer){clearInterval(state.timer);state.timer=null;$('play').textContent='播放历届 ◉';$('play').setAttribute('aria-pressed','false');return}select(0);$('play').textContent='暂停 Ⅱ';$('play').setAttribute('aria-pressed','true');state.timer=setInterval(()=>{if(state.index===years.length-1){$('play').click();return}select(state.index+1)},1100)});
addEventListener('resize',()=>Object.values(charts).forEach(chart=>chart.resize()));
select(state.index);
