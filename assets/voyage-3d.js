/* Olympic gallery: world-fixed exhibits and a continuous camera journey. */
(()=>{
 const host=document.querySelector('#voyage-stage .voyage-webgl');
 if(!host||!window.THREE||matchMedia('(prefers-reduced-motion: reduce)').matches)return;
 const T=window.THREE;let renderer;
 try{renderer=new T.WebGLRenderer({antialias:true,powerPreference:'low-power'});}catch(e){return}
 renderer.setPixelRatio(Math.min(devicePixelRatio||1,1.25));renderer.outputColorSpace=T.SRGBColorSpace;renderer.setClearColor(0x203947);host.append(renderer.domElement);
 const fallback=document.querySelector('.voyage-stars');if(fallback)fallback.style.display='none';
 const scene=new T.Scene();scene.background=new T.Color(0x203947);scene.fog=new T.FogExp2(0x203947,.026);
 const camera=new T.PerspectiveCamera(62,1,.1,165),gallery=new T.Group();scene.add(gallery);
 scene.add(new T.HemisphereLight(0xc6e1ee,0x384857,3));
 const key=new T.DirectionalLight(0xe2ebff,3);key.position.set(5,7,4);scene.add(key);
 const warm=new T.PointLight(0xffbb73,28,45,2);warm.position.set(1,2,-12);scene.add(warm);
 const palette=[0x379ac8,0xe2bc60,0xa8bcc9,0x59ad85,0xcb6c79];
 const metal=new T.MeshStandardMaterial({color:0x9caebb,metalness:.86,roughness:.27});
 function tube(points,r,material){const mesh=new T.Mesh(new T.TubeGeometry(new T.CatmullRomCurve3(points),100,r,5,false),material);gallery.add(mesh);return mesh}
 // Five continuous lanes connect exhibits; they are decoration, never data encoding.
 palette.forEach((color,k)=>{let pts=[];for(let j=0;j<100;j++){let z=-j*1.5;pts.push(new T.Vector3(2.6+Math.sin(z*.045+k*.15)*.5+(k-2)*.14,-2.55+Math.cos(z*.06)*.12,z))}tube(pts,.018,new T.MeshBasicMaterial({color,transparent:true,opacity:.55}))});
 const floor=new T.Mesh(new T.PlaneGeometry(80,200),new T.MeshStandardMaterial({color:0x425968,metalness:.25,roughness:.5}));floor.rotation.x=-Math.PI/2;floor.position.set(0,-2.8,-70);scene.add(floor);

 // Architectural depth: illuminated side walls, ceiling ribs and floor seams.
 const wallMat=new T.MeshStandardMaterial({color:0x36576a,metalness:.18,roughness:.65,transparent:true,opacity:.55,side:T.DoubleSide});
 for(const side of [-1,1]){const wall=new T.Mesh(new T.PlaneGeometry(180,24),wallMat);wall.rotation.y=side*Math.PI/2;wall.position.set(side*12,4,-72);scene.add(wall)}
 const ribMat=new T.MeshBasicMaterial({color:0x7fa5b4,transparent:true,opacity:.26});
 const seamMat=new T.LineBasicMaterial({color:0x9dbfca,transparent:true,opacity:.2});
 for(let j=0;j<20;j++){const z=-j*8;
  const rib=new T.Mesh(new T.BoxGeometry(24,.045,.065),ribMat);rib.position.set(0,6,z);scene.add(rib);
  const line=new T.Line(new T.BufferGeometry().setFromPoints([new T.Vector3(-12,-2.78,z),new T.Vector3(12,-2.78,z)]),seamMat);scene.add(line);
 }
 const skyCanvas=document.createElement('canvas');skyCanvas.width=64;skyCanvas.height=256;const ctx=skyCanvas.getContext('2d'),gradient=ctx.createLinearGradient(0,0,0,256);gradient.addColorStop(0,'#3e6277');gradient.addColorStop(.45,'#28495b');gradient.addColorStop(.75,'#6c7885');gradient.addColorStop(1,'#203541');ctx.fillStyle=gradient;ctx.fillRect(0,0,64,256);
 const sky=new T.Mesh(new T.SphereGeometry(150,24,16),new T.MeshBasicMaterial({map:new T.CanvasTexture(skyCanvas),side:T.BackSide,fog:false,depthWrite:false}));sky.renderOrder=-10;scene.add(sky);
 // Sculptural flame ribbons, with a small five-ring emblem at each station.
 for(let station=0;station<7;station++){
  const z=-station*18-12;
  for(let k=0;k<3;k++){let pts=[];for(let j=0;j<=36;j++){let t=j/36,a=t*5+k*2.094,r=(1-t)*.55+.04;pts.push(new T.Vector3(.5+Math.sin(a)*r,-2.55+t*4.8,z+Math.cos(a)*r))}tube(pts,.09,metal)}
  palette.forEach((color,k)=>{const ring=new T.Mesh(new T.TorusGeometry(.19,.014,6,36),new T.MeshBasicMaterial({color,transparent:true,opacity:.8}));ring.position.set(2+(k<3?k*.43:(k-3)*.43+.215),-2.16-(k>=3?.2:0),z+2.3);scene.add(ring)});
 }
 const frames=[],loader=new T.TextureLoader();
 (window.voyageImageData||[]).forEach((src,i)=>loader.load(src,tex=>{
  tex.colorSpace=T.SRGBColorSpace;tex.anisotropy=Math.min(4,renderer.capabilities.getMaxAnisotropy());
  const aspect=tex.image.width/tex.image.height,w=6.3,h=Math.min(4.3,w/aspect),mount=new T.Group();mount.position.set(3.9,.25,-i*18-10.2);mount.rotation.y=-.08;
  const glass=new T.Mesh(new T.BoxGeometry(w+.18,h+.18,.09),new T.MeshStandardMaterial({color:0x7b9cae,metalness:.6,roughness:.24}));mount.add(glass);
  const image=new T.Mesh(new T.PlaneGeometry(w,h),new T.MeshBasicMaterial({map:tex,toneMapped:false}));image.position.z=.055;mount.add(image);
  const edge=new T.EdgesGeometry(glass.geometry),line=new T.LineSegments(edge,new T.LineBasicMaterial({color:0x9cbbc9,transparent:true,opacity:.6}));mount.add(line);
  scene.add(mount);frames[i]=mount;render(progress);
 }));
 const starCount=340,vertices=new Float32Array(starCount*3);for(let i=0;i<starCount;i++){vertices[i*3]=Math.sin(i*29.1)*15;vertices[i*3+1]=Math.cos(i*13.7)*8;vertices[i*3+2]=-(i/starCount)*155}
 const geometry=new T.BufferGeometry();geometry.setAttribute('position',new T.BufferAttribute(vertices,3));const stars=new T.Points(geometry,new T.PointsMaterial({color:0xa1c8db,size:.025,transparent:true,opacity:.55,depthWrite:false}));scene.add(stars);
 let progress=0,width=0,height=0,clock=0,raf=0,last=0;
 const scenes=[...document.querySelectorAll('.voyage-scene')];
 function resize(){width=host.clientWidth;height=host.clientHeight;if(!width||!height)return;renderer.setSize(width,height,false);camera.aspect=width/height;camera.updateProjectionMatrix()}
 function render(p){progress=p;if(!width)resize();if(!width||!height)return;
  const pos=p*6,chapter=Math.floor(pos),phase=pos-chapter,t=Math.max(0,Math.min(1,(phase-.18)/.66)),ease=t*t*(3-2*t),z=-(chapter+ease)*18;
  camera.position.set(Math.sin(clock*.18)*.025,Math.cos(clock*.15)*.018,z);camera.lookAt(.35,0,z-18);
  warm.position.z=z-10;sky.position.z=z;stars.rotation.z=Math.sin(clock*.08)*.006;
  frames.forEach((frame,i)=>{frame.visible=width>650&&Math.abs(i-pos)<1.6;frame.position.y=.25+Math.sin(clock*.4+i)*.035});
  scenes.forEach((el,i)=>el.classList.toggle('memory-in-3d',width>650&&!!frames[i]));
  renderer.render(scene,camera);
 }
 renderer.domElement.addEventListener('webglcontextlost',e=>{e.preventDefault();cancelAnimationFrame(raf);host.style.display='none';scenes.forEach(el=>el.classList.remove('memory-in-3d'));if(fallback)fallback.style.display='block';window.renderVoyage3D=null});
 addEventListener('resize',()=>{resize();render(progress)},{passive:true});window.renderVoyage3D=render;render(0);
 function animate(now){raf=requestAnimationFrame(animate);if(document.hidden||now-last<40)return;last=now;clock=now*.001;render(progress)}raf=requestAnimationFrame(animate);
 document.addEventListener('visibilitychange',()=>{cancelAnimationFrame(raf);if(!document.hidden){last=0;raf=requestAnimationFrame(animate)}});
})();
