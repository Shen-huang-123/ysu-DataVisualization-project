/* Procedural WebGL tunnel. Geometry and camera are driven by the same scroll progress as the seven chapters. */
(()=>{
 const host=document.querySelector('#voyage-stage .voyage-webgl');
 if(!host||!window.THREE||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
 let renderer;
 try{renderer=new THREE.WebGLRenderer({antialias:true,alpha:false,powerPreference:'low-power'});}catch(e){return}
 renderer.setClearColor(0x030d15,1);
 renderer.outputColorSpace=THREE.SRGBColorSpace;
 host.appendChild(renderer.domElement);
 const fallback=document.querySelector('#voyage-stage .voyage-stars');if(fallback)fallback.style.display='none';
 const scene=new THREE.Scene();scene.background=new THREE.Color(0x030d15);scene.fog=new THREE.FogExp2(0x030d15,.012);
 const camera=new THREE.PerspectiveCamera(72,1,.1,130);
 const group=new THREE.Group();scene.add(group);
 const cyan=new THREE.LineBasicMaterial({color:0x66a9b2,transparent:true,opacity:.53,fog:true});
 const gold=new THREE.LineBasicMaterial({color:0xd4ad73,transparent:true,opacity:.76,fog:true});
 const pale=new THREE.LineBasicMaterial({color:0xb8d0d2,transparent:true,opacity:.24,fog:true});
 function line(points,material){const g=new THREE.BufferGeometry().setFromPoints(points);const obj=new THREE.Line(g,material);group.add(obj);return obj}
 for(let i=0;i<53;i++){
  const z=-8-i*3.25,phase=i*.31;
  const pts=[];
  for(let j=0;j<=80;j++){
   const a=j/80*Math.PI*2;
   const warp=1+.055*Math.sin(a*5+phase)+.035*Math.sin(a*9-phase*1.3);
   pts.push(new THREE.Vector3(Math.cos(a)*4.2*warp+Math.sin(z*.035)*.22,Math.sin(a)*3.25*warp,z));
  }
  line(pts,i%5===0?gold:i%2?cyan:pale);
  if(i%4===0){const curve=new THREE.CatmullRomCurve3(pts.slice(0,-1),true);const tube=new THREE.TubeGeometry(curve,80,i%8===0?.022:.013,4,true);group.add(new THREE.Mesh(tube,new THREE.MeshBasicMaterial({color:i%8===0?0xd4ad73:0x6ab8c4,transparent:true,opacity:i%8===0?.54:.35,fog:true})));}
 }
 const count=680,positions=new Float32Array(count*3),colors=new Float32Array(count*3);
 for(let i=0;i<count;i++){
  const rand=n=>{const x=Math.sin((i+1)*n*12.9898)*43758.5453;return x-Math.floor(x)};
  const a=rand(1)*Math.PI*2,r=2.8+rand(2)*6,z=-rand(3)*178;
  positions[i*3]=Math.cos(a)*r;positions[i*3+1]=Math.sin(a)*r*.85;positions[i*3+2]=z;
  const c=new THREE.Color(rand(4)>.84?0xe7bc80:0xb6d8dd);colors[i*3]=c.r;colors[i*3+1]=c.g;colors[i*3+2]=c.b;
 }
 const stars=new THREE.BufferGeometry();stars.setAttribute('position',new THREE.BufferAttribute(positions,3));stars.setAttribute('color',new THREE.BufferAttribute(colors,3));
 scene.add(new THREE.Points(stars,new THREE.PointsMaterial({size:.085,vertexColors:true,transparent:true,opacity:.86,sizeAttenuation:true,depthWrite:false,fog:true})));
 let width=0,height=0,lastProgress=0;
 function resize(){const w=host.clientWidth,h=host.clientHeight;if(w===width&&h===height)return;width=w;height=h;if(!w||!h)return;renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.5));renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix()}
 function render(p){lastProgress=p;resize();if(!width||!height)return;camera.position.set(Math.sin(p*5)*.22,Math.cos(p*4)*.11,-p*105);camera.lookAt(Math.sin(p*5)*.12,0,camera.position.z-12);renderer.render(scene,camera)}
 renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();host.style.display='none';if(fallback)fallback.style.display='block';window.renderVoyage3D=null;if(window.drawVoyageStars)window.drawVoyageStars(lastProgress)});
 addEventListener('resize',()=>render(lastProgress),{passive:true});
 window.renderVoyage3D=render;render(0);
})();
