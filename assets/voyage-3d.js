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
   pts.push(new THREE.Vector3(Math.cos(a)*4.2*warp+Math.sin(z*.035)*1.1,Math.sin(a)*3.25*warp+Math.cos(z*.03)*.5,z));
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
 const trailPositions=new Float32Array(210*6);
 for(let i=0;i<210;i++){const a=i*2.399963,r=3.4+(i%17)*.22,z=-(i/210)*178;trailPositions.set([Math.cos(a)*r,Math.sin(a)*r*.85,z,Math.cos(a)*r,Math.sin(a)*r*.85,z-.65-(i%7)*.2],i*6)}
 const trailGeometry=new THREE.BufferGeometry();trailGeometry.setAttribute('position',new THREE.BufferAttribute(trailPositions,3));
 const trailMaterial=new THREE.LineBasicMaterial({color:0x7ccbe6,transparent:true,opacity:.25,blending:THREE.AdditiveBlending,depthWrite:false});scene.add(new THREE.LineSegments(trailGeometry,trailMaterial));
 const palette=[0x429ac5,0xd9b45c,0xb3c8d1,0x65ac88,0xc27878];
 for(let k=0;k<5;k++){const pts=[];for(let j=0;j<220;j++){const z=-j*.8,a=k*Math.PI*2/5+.12*Math.sin(z*.04);pts.push(new THREE.Vector3(Math.cos(a)*4.4+Math.sin(z*.035)*1.1,Math.sin(a)*3.4+Math.cos(z*.03)*.5,z))}line(pts,new THREE.LineBasicMaterial({color:palette[k],transparent:true,opacity:.38,fog:true}));}
 const years=['1896','1924','1964','1984','2008','2024','2028'];
 years.forEach((year,i)=>{const c=document.createElement('canvas');c.width=256;c.height=128;const g=c.getContext('2d');g.fillStyle='#c6d5d9';g.font='30px Georgia';g.fillText(year,12,38);g.strokeStyle='#8aaab6';g.lineWidth=3;g.beginPath();g.arc(190,36,6,0,Math.PI*2);g.moveTo(190,45);g.lineTo(180,66);g.lineTo(160,77);g.moveTo(181,65);g.lineTo(204,82);g.moveTo(185,53);g.lineTo(204,55);g.stroke();g.fillStyle='#7296a3';g.fillRect(12,52,85,1);const tex=new THREE.CanvasTexture(c);const sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:tex,transparent:true,opacity:.65,depthWrite:false}));const z=-12-i*17.5;sprite.position.set(Math.sin(z*.035)*1.1+(i%2?2.9:-2.9),1.4,z);sprite.scale.set(1.6,.8,1);scene.add(sprite)});
 const memories=[],loader=new THREE.TextureLoader();
 (window.voyageImageData||[]).forEach((src,i)=>{
  loader.load(src,texture=>{texture.colorSpace=THREE.SRGBColorSpace;texture.anisotropy=Math.min(8,renderer.capabilities.getMaxAnisotropy());const material=new THREE.MeshBasicMaterial({map:texture,transparent:true,opacity:0,fog:false,side:THREE.DoubleSide,depthTest:false,depthWrite:false});material.onBeforeCompile=shader=>{shader.fragmentShader=shader.fragmentShader.replace('#include <clipping_planes_fragment>','#include <clipping_planes_fragment>\n if(length((vMapUv-0.5)*2.0)>1.0) discard;')};const mesh=new THREE.Mesh(new THREE.PlaneGeometry(1,1),material);mesh.renderOrder=5;scene.add(mesh);memories[i]=mesh;render(lastProgress)});
 });
 let ambientTime=0;
 let width=0,height=0,lastProgress=0,quality=1.5,slowFrames=0,sampleFrames=0,totalRenderMs=0;
 const photoRects=[];
 const hover={x:0,y:0,tx:0,ty:0};
 addEventListener('pointermove',e=>{if(e.pointerType!=='mouse')return;const index=Math.round(lastProgress*6),rect=photoRects[index];if(!rect)return;const nx=(e.clientX-rect.x)/(rect.w/2),ny=(e.clientY-rect.y)/(rect.h/2);if(Math.abs(nx)<=1&&Math.abs(ny)<=1){hover.tx=nx;hover.ty=ny}else{hover.tx=0;hover.ty=0}},{passive:true});
 document.documentElement.addEventListener('pointerleave',()=>{hover.tx=hover.ty=0});
 addEventListener('blur',()=>{hover.tx=hover.ty=0});


 function resize(){const w=host.clientWidth,h=host.clientHeight;if(w===width&&h===height)return;width=w;height=h;if(!w||!h)return;renderer.setPixelRatio(Math.min(devicePixelRatio||1,quality));renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix();photoRects.length=0;document.querySelectorAll(".voyage-scene .voyage-photo").forEach(el=>{const r=el.getBoundingClientRect();photoRects.push({x:r.x+r.width/2,y:r.y+r.height/2,w:r.width,h:r.height})})}
 function render(p){lastProgress=p;if(!width||!height)resize();if(!width||!height)return;const step=p*6,chapter=Math.floor(step),phase=step-chapter,t=Math.max(0,Math.min(1,(phase-.18)/.66)),flow=t*t*(3-2*t),z=-(chapter+flow)*17.5,boost=Math.pow(Math.sin(t*Math.PI),2);camera.position.set(Math.sin(z*.035)*1.1+Math.sin(ambientTime*.28)*.035,Math.cos(z*.03)*.5+Math.sin(ambientTime*.23)*.025,z);camera.lookAt(Math.sin((z-12)*.035)*1.1,Math.cos((z-12)*.03)*.5,z-12);camera.fov=72+boost*7;camera.updateProjectionMatrix();trailMaterial.opacity=.15+boost*.45;camera.updateMatrixWorld();
 const pos=p*6;hover.x+=(hover.tx-hover.x)*.085;hover.y+=(hover.ty-hover.y)*.085;
 memories.forEach((mesh,i)=>{const delta=i-pos,rect=photoRects[i];if(!rect)return;const opacity=Math.max(0,1-Math.abs(delta)*2.3);mesh.visible=opacity>.01&&width>650;if(!mesh.visible)return;const depth=8+Math.abs(delta)*18;const v=new THREE.Vector3((rect.x+Math.sin(ambientTime*.45+i)*2+hover.x*4)/width*2-1,1-(rect.y+Math.sin(ambientTime*.55+i)*4+hover.y*3)/height*2,.5).unproject(camera).sub(camera.position).normalize();mesh.position.copy(camera.position).addScaledVector(v,depth/Math.max(.1,-v.clone().applyQuaternion(camera.quaternion.clone().invert()).z));mesh.quaternion.copy(camera.quaternion);mesh.rotateY(delta*.14+hover.x*.035+Math.sin(ambientTime*.32+i)*.007);mesh.rotateX(-hover.y*.025);const worldHeight=2*Math.tan(camera.fov*Math.PI/360)*depth;mesh.scale.set(worldHeight*camera.aspect*rect.w/width,worldHeight*rect.h/height,1);mesh.material.opacity=opacity;});
 const starPositions=stars.attributes.position.array;
 for(let i=0;i<count;i++){const base=-((i*0.61803398875)%1)*178;starPositions[i*3+2]=((base+ambientTime*.42+180)%178)-178;}
 stars.attributes.position.needsUpdate=true;
 group.rotation.z=Math.sin(ambientTime*.12)*.012;
 trailMaterial.opacity+=.035*Math.sin(ambientTime*.9);
 const started=performance.now();renderer.render(scene,camera);const cost=performance.now()-started;
 totalRenderMs+=cost;sampleFrames++;if(cost>22)slowFrames++;
 if(sampleFrames>=75){if(slowFrames>18&&quality>.7){quality=Math.max(.7,quality-.25);stars.setDrawRange(0,Math.floor(count*quality/1.25));trailGeometry.setDrawRange(0,Math.floor(420*quality/1.25));width=0;resize()}host.dataset.quality=quality.toFixed(2);host.dataset.renderMs=(totalRenderMs/sampleFrames).toFixed(1);sampleFrames=0;slowFrames=0;totalRenderMs=0;}
 document.querySelectorAll('.voyage-scene').forEach((el,i)=>el.classList.toggle('memory-in-3d',!!memories[i]&&width>650));
}
 renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();host.style.display='none';if(fallback)fallback.style.display='block';window.renderVoyage3D=null;if(window.drawVoyageStars)window.drawVoyageStars(lastProgress)});
 addEventListener('resize',()=>{resize();render(lastProgress)},{passive:true});
 window.renderVoyage3D=render;render(0);
 let frame=0,lastFrame=0;
 function animate(now){frame=requestAnimationFrame(animate);if(document.hidden||now-lastFrame<40)return;lastFrame=now;ambientTime=now*.001;render(lastProgress)}
 frame=requestAnimationFrame(animate);
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame)}else{lastFrame=0;frame=requestAnimationFrame(animate)}});

})();
