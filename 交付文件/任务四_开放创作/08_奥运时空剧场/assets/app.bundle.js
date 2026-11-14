(()=>{var $n={LEFT:0,MIDDLE:1,RIGHT:2,ROTATE:0,DOLLY:1,PAN:2},Kn={ROTATE:0,PAN:1,DOLLY_PAN:2,DOLLY_ROTATE:3},mc=0,Eo=1,gc=2;var Ps=1,_c=2,Wi=3,jn=0,Tt=1,nn=2,ui=0,Xi=1,To=2,Ao=3,wo=4,xc=5;var di=100,yc=101,vc=102,Sc=103,Mc=104,bc=200,Ec=201,Tc=202,Ac=203,Ro=204,Co=205,wc=206,Rc=207,Cc=208,Pc=209,Ic=210,Lc=211,Dc=212,Nc=213,Uc=214,mr=0,gr=1,_r=2,Di=3,xr=4,yr=5,vr=6,Sr=7,Zr=0,Fc=1,Oc=2,xn=0,Po=1,Io=2,Lo=3,Do=4,No=5,Uo=6,Fo=7;var Oo=300,fi=301,qi=302,Jr=303,$r=304,Mr=1e3,gn=1001,br=1002,Mt=1003,Bc=1004;var Is=1005;var Ft=1006,Kr=1007;var Dn=1008;var Gt=1009,Bo=1010,zo=1011,Yi=1012,jr=1013,cn=1014,hn=1015,un=1016,Qr=1017,ea=1018,pi=1020,ko=35902,Go=35899,Vo=1021,Ho=1022,dn=1023,Cn=1026,Nn=1027,Wo=1028,ta=1029,Qn=1030,na=1031;var ia=1033,Ls=33776,Ds=33777,Ns=33778,Us=33779,sa=35840,ra=35841,aa=35842,oa=35843,la=36196,ca=37492,ha=37496,ua=37488,da=37489,Fs=37490,fa=37491,pa=37808,ma=37809,ga=37810,_a=37811,xa=37812,ya=37813,va=37814,Sa=37815,Ma=37816,ba=37817,Ea=37818,Ta=37819,Aa=37820,wa=37821,Ra=36492,Ca=36494,Pa=36495,Ia=36283,La=36284,Os=36285,Da=36286;var as=2300,Er=2301,fr=2302,go=2303,_o=2400,xo=2401,yo=2402;var zc=3200;var Na=0,kc=1,Un="",Nt="srgb",os="srgb-linear",ls="linear",$e="srgb";var pr=7680;var Gc=519,Vc=512,Hc=513,Wc=514,Xo=515,Xc=516,qc=517,qo=518,Yo=519,Yc=35044;var Zo="300 es",en=2e3,Ni=2001;function qh(i){for(let e=i.length-1;e>=0;--e)if(i[e]>=65535)return!0;return!1}function Yh(i){return ArrayBuffer.isView(i)&&!(i instanceof DataView)}function cs(i){return document.createElementNS("http://www.w3.org/1999/xhtml",i)}function Zc(){let i=cs("canvas");return i.style.display="block",i}var zl={},Ui=null;function Jo(...i){let e="THREE."+i.shift();Ui?Ui("log",e,...i):console.log(e,...i)}function Jc(i){let e=i[0];if(typeof e=="string"&&e.startsWith("TSL:")){let t=i[1];t&&t.isStackTrace?i[0]+=" "+t.getLocation():i[1]='Stack trace not available. Enable "THREE.Node.captureStackTrace" to capture stack traces.'}return i}function Te(...i){i=Jc(i);let e="THREE."+i.shift();if(Ui)Ui("warn",e,...i);else{let t=i[0];t&&t.isStackTrace?console.warn(t.getError(e)):console.warn(e,...i)}}function Pe(...i){i=Jc(i);let e="THREE."+i.shift();if(Ui)Ui("error",e,...i);else{let t=i[0];t&&t.isStackTrace?console.error(t.getError(e)):console.error(e,...i)}}function is(...i){let e=i.join(" ");e in zl||(zl[e]=!0,Te(...i))}function $c(i,e,t){return new Promise(function(n,s){function r(){switch(i.clientWaitSync(e,i.SYNC_FLUSH_COMMANDS_BIT,0)){case i.WAIT_FAILED:s();break;case i.TIMEOUT_EXPIRED:setTimeout(r,t);break;default:n()}}setTimeout(r,t)})}var Kc={[mr]:mr,[_r]:vr,[xr]:xr,[Di]:yr,[gr]:gr,[vr]:_r,[Sr]:Sr,[yr]:Di},ln=class{addEventListener(e,t){this._listeners===void 0&&(this._listeners={});let n=this._listeners;n[e]===void 0&&(n[e]=[]),n[e].indexOf(t)===-1&&n[e].push(t)}hasEventListener(e,t){let n=this._listeners;return n===void 0?!1:n[e]!==void 0&&n[e].indexOf(t)!==-1}removeEventListener(e,t){let n=this._listeners;if(n===void 0)return;let s=n[e];if(s!==void 0){let r=s.indexOf(t);r!==-1&&s.splice(r,1)}}dispatchEvent(e){let t=this._listeners;if(t===void 0)return;let n=t[e.type];if(n!==void 0){e.target=this;let s=n.slice(0);for(let r=0,a=s.length;r<a;r++)s[r].call(this,e);e.target=null}}},Rt=["00","01","02","03","04","05","06","07","08","09","0a","0b","0c","0d","0e","0f","10","11","12","13","14","15","16","17","18","19","1a","1b","1c","1d","1e","1f","20","21","22","23","24","25","26","27","28","29","2a","2b","2c","2d","2e","2f","30","31","32","33","34","35","36","37","38","39","3a","3b","3c","3d","3e","3f","40","41","42","43","44","45","46","47","48","49","4a","4b","4c","4d","4e","4f","50","51","52","53","54","55","56","57","58","59","5a","5b","5c","5d","5e","5f","60","61","62","63","64","65","66","67","68","69","6a","6b","6c","6d","6e","6f","70","71","72","73","74","75","76","77","78","79","7a","7b","7c","7d","7e","7f","80","81","82","83","84","85","86","87","88","89","8a","8b","8c","8d","8e","8f","90","91","92","93","94","95","96","97","98","99","9a","9b","9c","9d","9e","9f","a0","a1","a2","a3","a4","a5","a6","a7","a8","a9","aa","ab","ac","ad","ae","af","b0","b1","b2","b3","b4","b5","b6","b7","b8","b9","ba","bb","bc","bd","be","bf","c0","c1","c2","c3","c4","c5","c6","c7","c8","c9","ca","cb","cc","cd","ce","cf","d0","d1","d2","d3","d4","d5","d6","d7","d8","d9","da","db","dc","dd","de","df","e0","e1","e2","e3","e4","e5","e6","e7","e8","e9","ea","eb","ec","ed","ee","ef","f0","f1","f2","f3","f4","f5","f6","f7","f8","f9","fa","fb","fc","fd","fe","ff"],kl=1234567,ss=Math.PI/180,Fi=180/Math.PI;function Zi(){let i=Math.random()*4294967295|0,e=Math.random()*4294967295|0,t=Math.random()*4294967295|0,n=Math.random()*4294967295|0;return(Rt[i&255]+Rt[i>>8&255]+Rt[i>>16&255]+Rt[i>>24&255]+"-"+Rt[e&255]+Rt[e>>8&255]+"-"+Rt[e>>16&15|64]+Rt[e>>24&255]+"-"+Rt[t&63|128]+Rt[t>>8&255]+"-"+Rt[t>>16&255]+Rt[t>>24&255]+Rt[n&255]+Rt[n>>8&255]+Rt[n>>16&255]+Rt[n>>24&255]).toLowerCase()}function ke(i,e,t){return Math.max(e,Math.min(t,i))}function $o(i,e){return(i%e+e)%e}function Zh(i,e,t,n,s){return n+(i-e)*(s-n)/(t-e)}function Jh(i,e,t){return i!==e?(t-i)/(e-i):0}function rs(i,e,t){return(1-t)*i+t*e}function $h(i,e,t,n){return rs(i,e,1-Math.exp(-t*n))}function Kh(i,e=1){return e-Math.abs($o(i,e*2)-e)}function jh(i,e,t){return i<=e?0:i>=t?1:(i=(i-e)/(t-e),i*i*(3-2*i))}function Qh(i,e,t){return i<=e?0:i>=t?1:(i=(i-e)/(t-e),i*i*i*(i*(i*6-15)+10))}function e1(i,e){return i+Math.floor(Math.random()*(e-i+1))}function t1(i,e){return i+Math.random()*(e-i)}function n1(i){return i*(.5-Math.random())}function i1(i){i!==void 0&&(kl=i);let e=kl+=1831565813;return e=Math.imul(e^e>>>15,e|1),e^=e+Math.imul(e^e>>>7,e|61),((e^e>>>14)>>>0)/4294967296}function s1(i){return i*ss}function r1(i){return i*Fi}function a1(i){return i>0&&Number.isInteger(i)&&2**Math.round(Math.log2(i))===i}function o1(i){return Math.pow(2,Math.ceil(Math.log(i)/Math.LN2))}function Ko(i){return Math.pow(2,Math.floor(Math.log(i)/Math.LN2))}function l1(i,e,t,n,s){let r=Math.cos,a=Math.sin,o=r(t/2),l=a(t/2),c=r((e+n)/2),h=a((e+n)/2),g=r((e-n)/2),d=a((e-n)/2),m=r((n-e)/2),_=a((n-e)/2);switch(s){case"XYX":i.set(o*h,l*g,l*d,o*c);break;case"YZY":i.set(l*d,o*h,l*g,o*c);break;case"ZXZ":i.set(l*g,l*d,o*h,o*c);break;case"XZX":i.set(o*h,l*_,l*m,o*c);break;case"YXY":i.set(l*m,o*h,l*_,o*c);break;case"ZYZ":i.set(l*_,l*m,o*h,o*c);break;default:Te("MathUtils: .setQuaternionFromProperEuler() encountered an unknown order: "+s)}}function jo(i){switch(i.constructor){case Uint32Array:return 4294967295;case Uint16Array:return 65535;case Uint8Array:case Uint8ClampedArray:return 255;case Int32Array:return 2147483647;case Int16Array:return 32767;case Int8Array:return 127;default:return}}function jc(i,e){if(e.constructor===Float32Array)return i;let t=jo(e);if(t===void 0)throw new Error("THREE.MathUtils: Invalid component type.");return Math.max(i/t,-1)}function Qc(i,e){if(e.constructor===Float32Array)return i;let t=jo(e);if(t===void 0)throw new Error("THREE.MathUtils: Invalid component type.");return Math.round(i*t)}var Qo={DEG2RAD:ss,RAD2DEG:Fi,generateUUID:Zi,clamp:ke,euclideanModulo:$o,mapLinear:Zh,inverseLerp:Jh,lerp:rs,damp:$h,pingpong:Kh,smoothstep:jh,smootherstep:Qh,randInt:e1,randFloat:t1,randFloatSpread:n1,seededRandom:i1,degToRad:s1,radToDeg:r1,isPowerOfTwo:a1,ceilPowerOfTwo:o1,floorPowerOfTwo:Ko,setQuaternionFromProperEuler:l1,normalize:Qc,denormalize:jc},sl=class sl{constructor(e=0,t=0){this.x=e,this.y=t}get width(){return this.x}set width(e){this.x=e}get height(){return this.y}set height(e){this.y=e}set(e,t){return this.x=e,this.y=t,this}setScalar(e){return this.x=e,this.y=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;default:throw new Error("THREE.Vector2: index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;default:throw new Error("THREE.Vector2: index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y)}copy(e){return this.x=e.x,this.y=e.y,this}add(e){return this.x+=e.x,this.y+=e.y,this}addScalar(e){return this.x+=e,this.y+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this}subScalar(e){return this.x-=e,this.y-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this}multiply(e){return this.x*=e.x,this.y*=e.y,this}multiplyScalar(e){return this.x*=e,this.y*=e,this}divide(e){return this.x/=e.x,this.y/=e.y,this}divideScalar(e){return this.multiplyScalar(1/e)}applyMatrix3(e){let t=this.x,n=this.y,s=e.elements;return this.x=s[0]*t+s[3]*n+s[6],this.y=s[1]*t+s[4]*n+s[7],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this}clamp(e,t){return this.x=ke(this.x,e.x,t.x),this.y=ke(this.y,e.y,t.y),this}clampScalar(e,t){return this.x=ke(this.x,e,t),this.y=ke(this.y,e,t),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ke(n,e,t))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this}negate(){return this.x=-this.x,this.y=-this.y,this}dot(e){return this.x*e.x+this.y*e.y}cross(e){return this.x*e.y-this.y*e.x}lengthSq(){return this.x*this.x+this.y*this.y}length(){return Math.sqrt(this.x*this.x+this.y*this.y)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)}normalize(){return this.divideScalar(this.length()||1)}angle(){return Math.atan2(-this.y,-this.x)+Math.PI}angleTo(e){let t=Math.sqrt(this.lengthSq()*e.lengthSq());if(t===0)return Math.PI/2;let n=this.dot(e)/t;return Math.acos(ke(n,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){let t=this.x-e.x,n=this.y-e.y;return t*t+n*n}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this}equals(e){return e.x===this.x&&e.y===this.y}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this}rotateAround(e,t){let n=Math.cos(t),s=Math.sin(t),r=this.x-e.x,a=this.y-e.y;return this.x=r*n-a*s+e.x,this.y=r*s+a*n+e.y,this}random(){return this.x=Math.random(),this.y=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y}};sl.prototype.isVector2=!0;var Re=sl,qt=class{constructor(e=0,t=0,n=0,s=1){this.isQuaternion=!0,this._x=e,this._y=t,this._z=n,this._w=s}static slerpFlat(e,t,n,s,r,a,o){let l=n[s+0],c=n[s+1],h=n[s+2],g=n[s+3],d=r[a+0],m=r[a+1],_=r[a+2],S=r[a+3];if(g!==S||l!==d||c!==m||h!==_){let p=l*d+c*m+h*_+g*S;p<0&&(d=-d,m=-m,_=-_,S=-S,p=-p);let u=1-o;if(p<.9995){let M=Math.acos(p),w=Math.sin(M);u=Math.sin(u*M)/w,o=Math.sin(o*M)/w,l=l*u+d*o,c=c*u+m*o,h=h*u+_*o,g=g*u+S*o}else{l=l*u+d*o,c=c*u+m*o,h=h*u+_*o,g=g*u+S*o;let M=1/Math.sqrt(l*l+c*c+h*h+g*g);l*=M,c*=M,h*=M,g*=M}}e[t]=l,e[t+1]=c,e[t+2]=h,e[t+3]=g}static multiplyQuaternionsFlat(e,t,n,s,r,a){let o=n[s],l=n[s+1],c=n[s+2],h=n[s+3],g=r[a],d=r[a+1],m=r[a+2],_=r[a+3];return e[t]=o*_+h*g+l*m-c*d,e[t+1]=l*_+h*d+c*g-o*m,e[t+2]=c*_+h*m+o*d-l*g,e[t+3]=h*_-o*g-l*d-c*m,e}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get w(){return this._w}set w(e){this._w=e,this._onChangeCallback()}set(e,t,n,s){return this._x=e,this._y=t,this._z=n,this._w=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._w)}copy(e){return this._x=e.x,this._y=e.y,this._z=e.z,this._w=e.w,this._onChangeCallback(),this}setFromEuler(e,t=!0){let n=e._x,s=e._y,r=e._z,a=e._order,o=Math.cos,l=Math.sin,c=o(n/2),h=o(s/2),g=o(r/2),d=l(n/2),m=l(s/2),_=l(r/2);switch(a){case"XYZ":this._x=d*h*g+c*m*_,this._y=c*m*g-d*h*_,this._z=c*h*_+d*m*g,this._w=c*h*g-d*m*_;break;case"YXZ":this._x=d*h*g+c*m*_,this._y=c*m*g-d*h*_,this._z=c*h*_-d*m*g,this._w=c*h*g+d*m*_;break;case"ZXY":this._x=d*h*g-c*m*_,this._y=c*m*g+d*h*_,this._z=c*h*_+d*m*g,this._w=c*h*g-d*m*_;break;case"ZYX":this._x=d*h*g-c*m*_,this._y=c*m*g+d*h*_,this._z=c*h*_-d*m*g,this._w=c*h*g+d*m*_;break;case"YZX":this._x=d*h*g+c*m*_,this._y=c*m*g+d*h*_,this._z=c*h*_-d*m*g,this._w=c*h*g-d*m*_;break;case"XZY":this._x=d*h*g-c*m*_,this._y=c*m*g-d*h*_,this._z=c*h*_+d*m*g,this._w=c*h*g+d*m*_;break;default:Te("Quaternion: .setFromEuler() encountered an unknown order: "+a)}return t===!0&&this._onChangeCallback(),this}setFromAxisAngle(e,t){let n=t/2,s=Math.sin(n);return this._x=e.x*s,this._y=e.y*s,this._z=e.z*s,this._w=Math.cos(n),this._onChangeCallback(),this}setFromRotationMatrix(e){let t=e.elements,n=t[0],s=t[4],r=t[8],a=t[1],o=t[5],l=t[9],c=t[2],h=t[6],g=t[10],d=n+o+g;if(d>0){let m=.5/Math.sqrt(d+1);this._w=.25/m,this._x=(h-l)*m,this._y=(r-c)*m,this._z=(a-s)*m}else if(n>o&&n>g){let m=2*Math.sqrt(1+n-o-g);this._w=(h-l)/m,this._x=.25*m,this._y=(s+a)/m,this._z=(r+c)/m}else if(o>g){let m=2*Math.sqrt(1+o-n-g);this._w=(r-c)/m,this._x=(s+a)/m,this._y=.25*m,this._z=(l+h)/m}else{let m=2*Math.sqrt(1+g-n-o);this._w=(a-s)/m,this._x=(r+c)/m,this._y=(l+h)/m,this._z=.25*m}return this._onChangeCallback(),this}setFromUnitVectors(e,t){let n=e.dot(t)+1;return n<1e-8?(n=0,Math.abs(e.x)>Math.abs(e.z)?(this._x=-e.y,this._y=e.x,this._z=0,this._w=n):(this._x=0,this._y=-e.z,this._z=e.y,this._w=n)):(this._x=e.y*t.z-e.z*t.y,this._y=e.z*t.x-e.x*t.z,this._z=e.x*t.y-e.y*t.x,this._w=n),this.normalize()}angleTo(e){return 2*Math.acos(Math.abs(ke(this.dot(e),-1,1)))}rotateTowards(e,t){let n=this.angleTo(e);if(n===0)return this;let s=Math.min(1,t/n);return this.slerp(e,s),this}identity(){return this.set(0,0,0,1)}invert(){return this.conjugate()}conjugate(){return this._x*=-1,this._y*=-1,this._z*=-1,this._onChangeCallback(),this}dot(e){return this._x*e._x+this._y*e._y+this._z*e._z+this._w*e._w}lengthSq(){return this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w}length(){return Math.sqrt(this._x*this._x+this._y*this._y+this._z*this._z+this._w*this._w)}normalize(){let e=this.length();return e===0?(this._x=0,this._y=0,this._z=0,this._w=1):(e=1/e,this._x=this._x*e,this._y=this._y*e,this._z=this._z*e,this._w=this._w*e),this._onChangeCallback(),this}multiply(e){return this.multiplyQuaternions(this,e)}premultiply(e){return this.multiplyQuaternions(e,this)}multiplyQuaternions(e,t){let n=e._x,s=e._y,r=e._z,a=e._w,o=t._x,l=t._y,c=t._z,h=t._w;return this._x=n*h+a*o+s*c-r*l,this._y=s*h+a*l+r*o-n*c,this._z=r*h+a*c+n*l-s*o,this._w=a*h-n*o-s*l-r*c,this._onChangeCallback(),this}slerp(e,t){let n=e._x,s=e._y,r=e._z,a=e._w,o=this.dot(e);o<0&&(n=-n,s=-s,r=-r,a=-a,o=-o);let l=1-t;if(o<.9995){let c=Math.acos(o),h=Math.sin(c);l=Math.sin(l*c)/h,t=Math.sin(t*c)/h,this._x=this._x*l+n*t,this._y=this._y*l+s*t,this._z=this._z*l+r*t,this._w=this._w*l+a*t,this._onChangeCallback()}else this._x=this._x*l+n*t,this._y=this._y*l+s*t,this._z=this._z*l+r*t,this._w=this._w*l+a*t,this.normalize();return this}slerpQuaternions(e,t,n){return this.copy(e).slerp(t,n)}random(){let e=2*Math.PI*Math.random(),t=2*Math.PI*Math.random(),n=Math.random(),s=Math.sqrt(1-n),r=Math.sqrt(n);return this.set(s*Math.sin(e),s*Math.cos(e),r*Math.sin(t),r*Math.cos(t))}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._w===this._w}fromArray(e,t=0){return this._x=e[t],this._y=e[t+1],this._z=e[t+2],this._w=e[t+3],this._onChangeCallback(),this}toArray(e=[],t=0){return e[t]=this._x,e[t+1]=this._y,e[t+2]=this._z,e[t+3]=this._w,e}fromBufferAttribute(e,t){return this._x=e.getX(t),this._y=e.getY(t),this._z=e.getZ(t),this._w=e.getW(t),this._onChangeCallback(),this}toJSON(){return this.toArray()}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._w}},rl=class rl{constructor(e=0,t=0,n=0){this.x=e,this.y=t,this.z=n}set(e,t,n){return n===void 0&&(n=this.z),this.x=e,this.y=t,this.z=n,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;case 2:this.z=t;break;default:throw new Error("THREE.Vector3: index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;default:throw new Error("THREE.Vector3: index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this.z=e.z+t.z,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this.z+=e.z*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this.z=e.z-t.z,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this}multiplyVectors(e,t){return this.x=e.x*t.x,this.y=e.y*t.y,this.z=e.z*t.z,this}applyEuler(e){return this.applyQuaternion(Gl.setFromEuler(e))}applyAxisAngle(e,t){return this.applyQuaternion(Gl.setFromAxisAngle(e,t))}applyMatrix3(e){let t=this.x,n=this.y,s=this.z,r=e.elements;return this.x=r[0]*t+r[3]*n+r[6]*s,this.y=r[1]*t+r[4]*n+r[7]*s,this.z=r[2]*t+r[5]*n+r[8]*s,this}applyNormalMatrix(e){return this.applyMatrix3(e).normalize()}applyMatrix4(e){let t=this.x,n=this.y,s=this.z,r=e.elements,a=1/(r[3]*t+r[7]*n+r[11]*s+r[15]);return this.x=(r[0]*t+r[4]*n+r[8]*s+r[12])*a,this.y=(r[1]*t+r[5]*n+r[9]*s+r[13])*a,this.z=(r[2]*t+r[6]*n+r[10]*s+r[14])*a,this}applyQuaternion(e){let t=this.x,n=this.y,s=this.z,r=e.x,a=e.y,o=e.z,l=e.w,c=2*(a*s-o*n),h=2*(o*t-r*s),g=2*(r*n-a*t);return this.x=t+l*c+a*g-o*h,this.y=n+l*h+o*c-r*g,this.z=s+l*g+r*h-a*c,this}project(e){return this.applyMatrix4(e.matrixWorldInverse).applyMatrix4(e.projectionMatrix)}unproject(e){return this.applyMatrix4(e.projectionMatrixInverse).applyMatrix4(e.matrixWorld)}transformDirection(e){let t=this.x,n=this.y,s=this.z,r=e.elements;return this.x=r[0]*t+r[4]*n+r[8]*s,this.y=r[1]*t+r[5]*n+r[9]*s,this.z=r[2]*t+r[6]*n+r[10]*s,this.normalize()}divide(e){return this.x/=e.x,this.y/=e.y,this.z/=e.z,this}divideScalar(e){return this.multiplyScalar(1/e)}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this}clamp(e,t){return this.x=ke(this.x,e.x,t.x),this.y=ke(this.y,e.y,t.y),this.z=ke(this.z,e.z,t.z),this}clampScalar(e,t){return this.x=ke(this.x,e,t),this.y=ke(this.y,e,t),this.z=ke(this.z,e,t),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ke(n,e,t))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this.z+=(e.z-this.z)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this.z=e.z+(t.z-e.z)*n,this}cross(e){return this.crossVectors(this,e)}crossVectors(e,t){let n=e.x,s=e.y,r=e.z,a=t.x,o=t.y,l=t.z;return this.x=s*l-r*o,this.y=r*a-n*l,this.z=n*o-s*a,this}projectOnVector(e){let t=e.lengthSq();if(t===0)return this.set(0,0,0);let n=e.dot(this)/t;return this.copy(e).multiplyScalar(n)}projectOnPlane(e){return Za.copy(this).projectOnVector(e),this.sub(Za)}reflect(e){return this.sub(Za.copy(e).multiplyScalar(2*this.dot(e)))}angleTo(e){let t=Math.sqrt(this.lengthSq()*e.lengthSq());if(t===0)return Math.PI/2;let n=this.dot(e)/t;return Math.acos(ke(n,-1,1))}distanceTo(e){return Math.sqrt(this.distanceToSquared(e))}distanceToSquared(e){let t=this.x-e.x,n=this.y-e.y,s=this.z-e.z;return t*t+n*n+s*s}manhattanDistanceTo(e){return Math.abs(this.x-e.x)+Math.abs(this.y-e.y)+Math.abs(this.z-e.z)}setFromSpherical(e){return this.setFromSphericalCoords(e.radius,e.phi,e.theta)}setFromSphericalCoords(e,t,n){let s=Math.sin(t)*e;return this.x=s*Math.sin(n),this.y=Math.cos(t)*e,this.z=s*Math.cos(n),this}setFromCylindrical(e){return this.setFromCylindricalCoords(e.radius,e.theta,e.y)}setFromCylindricalCoords(e,t,n){return this.x=e*Math.sin(t),this.y=n,this.z=e*Math.cos(t),this}setFromMatrixPosition(e){let t=e.elements;return this.x=t[12],this.y=t[13],this.z=t[14],this}setFromMatrixScale(e){let t=this.setFromMatrixColumn(e,0).length(),n=this.setFromMatrixColumn(e,1).length(),s=this.setFromMatrixColumn(e,2).length();return this.x=t,this.y=n,this.z=s,this}setFromMatrixColumn(e,t){return this.fromArray(e.elements,t*4)}setFromMatrix3Column(e,t){return this.fromArray(e.elements,t*3)}setFromEuler(e){return this.x=e._x,this.y=e._y,this.z=e._z,this}setFromColor(e){return this.x=e.r,this.y=e.g,this.z=e.b,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this.z=e[t+2],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e[t+2]=this.z,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this.z=e.getZ(t),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this}randomDirection(){let e=Math.random()*Math.PI*2,t=Math.random()*2-1,n=Math.sqrt(1-t*t);return this.x=n*Math.cos(e),this.y=t,this.z=n*Math.sin(e),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z}};rl.prototype.isVector3=!0;var U=rl,Za=new U,Gl=new qt,al=class al{constructor(e,t,n,s,r,a,o,l,c){this.elements=[1,0,0,0,1,0,0,0,1],e!==void 0&&this.set(e,t,n,s,r,a,o,l,c)}set(e,t,n,s,r,a,o,l,c){let h=this.elements;return h[0]=e,h[1]=s,h[2]=o,h[3]=t,h[4]=r,h[5]=l,h[6]=n,h[7]=a,h[8]=c,this}identity(){return this.set(1,0,0,0,1,0,0,0,1),this}copy(e){let t=this.elements,n=e.elements;return t[0]=n[0],t[1]=n[1],t[2]=n[2],t[3]=n[3],t[4]=n[4],t[5]=n[5],t[6]=n[6],t[7]=n[7],t[8]=n[8],this}extractBasis(e,t,n){return e.setFromMatrix3Column(this,0),t.setFromMatrix3Column(this,1),n.setFromMatrix3Column(this,2),this}setFromMatrix4(e){let t=e.elements;return this.set(t[0],t[4],t[8],t[1],t[5],t[9],t[2],t[6],t[10]),this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,t){let n=e.elements,s=t.elements,r=this.elements,a=n[0],o=n[3],l=n[6],c=n[1],h=n[4],g=n[7],d=n[2],m=n[5],_=n[8],S=s[0],p=s[3],u=s[6],M=s[1],w=s[4],E=s[7],A=s[2],T=s[5],f=s[8];return r[0]=a*S+o*M+l*A,r[3]=a*p+o*w+l*T,r[6]=a*u+o*E+l*f,r[1]=c*S+h*M+g*A,r[4]=c*p+h*w+g*T,r[7]=c*u+h*E+g*f,r[2]=d*S+m*M+_*A,r[5]=d*p+m*w+_*T,r[8]=d*u+m*E+_*f,this}multiplyScalar(e){let t=this.elements;return t[0]*=e,t[3]*=e,t[6]*=e,t[1]*=e,t[4]*=e,t[7]*=e,t[2]*=e,t[5]*=e,t[8]*=e,this}determinant(){let e=this.elements,t=e[0],n=e[1],s=e[2],r=e[3],a=e[4],o=e[5],l=e[6],c=e[7],h=e[8];return t*a*h-t*o*c-n*r*h+n*o*l+s*r*c-s*a*l}invert(){let e=this.elements,t=e[0],n=e[1],s=e[2],r=e[3],a=e[4],o=e[5],l=e[6],c=e[7],h=e[8],g=h*a-o*c,d=o*l-h*r,m=c*r-a*l,_=t*g+n*d+s*m;if(_===0)return this.set(0,0,0,0,0,0,0,0,0);let S=1/_;return e[0]=g*S,e[1]=(s*c-h*n)*S,e[2]=(o*n-s*a)*S,e[3]=d*S,e[4]=(h*t-s*l)*S,e[5]=(s*r-o*t)*S,e[6]=m*S,e[7]=(n*l-c*t)*S,e[8]=(a*t-n*r)*S,this}transpose(){let e,t=this.elements;return e=t[1],t[1]=t[3],t[3]=e,e=t[2],t[2]=t[6],t[6]=e,e=t[5],t[5]=t[7],t[7]=e,this}getNormalMatrix(e){return this.setFromMatrix4(e).invert().transpose()}transposeIntoArray(e){let t=this.elements;return e[0]=t[0],e[1]=t[3],e[2]=t[6],e[3]=t[1],e[4]=t[4],e[5]=t[7],e[6]=t[2],e[7]=t[5],e[8]=t[8],this}setUvTransform(e,t,n,s,r,a,o){let l=Math.cos(r),c=Math.sin(r);return this.set(n*l,n*c,-n*(l*a+c*o)+a+e,-s*c,s*l,-s*(-c*a+l*o)+o+t,0,0,1),this}scale(e,t){return is("Matrix3: .scale() is deprecated. Use .makeScale() instead."),this.premultiply(Ja.makeScale(e,t)),this}rotate(e){return is("Matrix3: .rotate() is deprecated. Use .makeRotation() instead."),this.premultiply(Ja.makeRotation(-e)),this}translate(e,t){return is("Matrix3: .translate() is deprecated. Use .makeTranslation() instead."),this.premultiply(Ja.makeTranslation(e,t)),this}makeTranslation(e,t){return e.isVector2?this.set(1,0,e.x,0,1,e.y,0,0,1):this.set(1,0,e,0,1,t,0,0,1),this}makeRotation(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,-n,0,n,t,0,0,0,1),this}makeScale(e,t){return this.set(e,0,0,0,t,0,0,0,1),this}equals(e){let t=this.elements,n=e.elements;for(let s=0;s<9;s++)if(t[s]!==n[s])return!1;return!0}fromArray(e,t=0){for(let n=0;n<9;n++)this.elements[n]=e[n+t];return this}toArray(e=[],t=0){let n=this.elements;return e[t]=n[0],e[t+1]=n[1],e[t+2]=n[2],e[t+3]=n[3],e[t+4]=n[4],e[t+5]=n[5],e[t+6]=n[6],e[t+7]=n[7],e[t+8]=n[8],e}clone(){return new this.constructor().fromArray(this.elements)}};al.prototype.isMatrix3=!0;var Ie=al,Ja=new Ie,Vl=new Ie().set(.4123908,.3575843,.1804808,.212639,.7151687,.0721923,.0193308,.1191948,.9505322),Hl=new Ie().set(3.2409699,-1.5373832,-.4986108,-.9692436,1.8759675,.0415551,.0556301,-.203977,1.0569715);function c1(){let i={enabled:!0,workingColorSpace:os,spaces:{},convert:function(s,r,a){return this.enabled===!1||r===a||!r||!a||(this.spaces[r].transfer===$e&&(s.r=Rn(s.r),s.g=Rn(s.g),s.b=Rn(s.b)),this.spaces[r].primaries!==this.spaces[a].primaries&&(s.applyMatrix3(this.spaces[r].toXYZ),s.applyMatrix3(this.spaces[a].fromXYZ)),this.spaces[a].transfer===$e&&(s.r=Li(s.r),s.g=Li(s.g),s.b=Li(s.b))),s},workingToColorSpace:function(s,r){return this.convert(s,this.workingColorSpace,r)},colorSpaceToWorking:function(s,r){return this.convert(s,r,this.workingColorSpace)},getPrimaries:function(s){return this.spaces[s].primaries},getTransfer:function(s){return s===Un?ls:this.spaces[s].transfer},getToneMappingMode:function(s){return this.spaces[s].outputColorSpaceConfig.toneMappingMode||"standard"},getLuminanceCoefficients:function(s,r=this.workingColorSpace){return s.fromArray(this.spaces[r].luminanceCoefficients)},define:function(s){Object.assign(this.spaces,s)},_getMatrix:function(s,r,a){return s.copy(this.spaces[a].fromXYZ).multiply(this.spaces[r].toXYZ)},_getDrawingBufferColorSpace:function(s){return this.spaces[s].outputColorSpaceConfig.drawingBufferColorSpace},_getUnpackColorSpace:function(s=this.workingColorSpace){return this.spaces[s].workingColorSpaceConfig.unpackColorSpace}},e=[.64,.33,.3,.6,.15,.06],t=[.2126,.7152,.0722],n=[.3127,.329];return i.define({[os]:{primaries:e,whitePoint:n,transfer:ls,toXYZ:Vl,fromXYZ:Hl,luminanceCoefficients:t,workingColorSpaceConfig:{unpackColorSpace:Nt},outputColorSpaceConfig:{drawingBufferColorSpace:Nt}},[Nt]:{primaries:e,whitePoint:n,transfer:$e,toXYZ:Vl,fromXYZ:Hl,luminanceCoefficients:t,outputColorSpaceConfig:{drawingBufferColorSpace:Nt}}}),i}var We=c1();function Rn(i){return i<.04045?i*.0773993808:Math.pow(i*.9478672986+.0521327014,2.4)}function Li(i){return i<.0031308?i*12.92:1.055*Math.pow(i,.41666)-.055}var yi,Tr=class{static getDataURL(e,t="image/png"){if(/^data:/i.test(e.src)||typeof HTMLCanvasElement>"u")return e.src;let n;if(e instanceof HTMLCanvasElement)n=e;else{yi===void 0&&(yi=cs("canvas")),yi.width=e.width,yi.height=e.height;let s=yi.getContext("2d");e instanceof ImageData?s.putImageData(e,0,0):s.drawImage(e,0,0,e.width,e.height),n=yi}return n.toDataURL(t)}static sRGBToLinear(e){if(typeof HTMLImageElement<"u"&&e instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&e instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&e instanceof ImageBitmap){let t=cs("canvas");t.width=e.width,t.height=e.height;let n=t.getContext("2d");n.drawImage(e,0,0,e.width,e.height);let s=n.getImageData(0,0,e.width,e.height),r=s.data;for(let a=0;a<r.length;a++)r[a]=Rn(r[a]/255)*255;return n.putImageData(s,0,0),t}else if(e.data){let t=e.data.slice(0);for(let n=0;n<t.length;n++)t instanceof Uint8Array||t instanceof Uint8ClampedArray?t[n]=Math.floor(Rn(t[n]/255)*255):t[n]=Rn(t[n]);return{data:t,width:e.width,height:e.height}}else return Te("ImageUtils.sRGBToLinear(): Unsupported image type. No color space conversion applied."),e}},h1=0,Oi=class{constructor(e=null){this.isTextureSource=!0,Object.defineProperty(this,"id",{value:h1++}),this.uuid=Zi(),this.data=e,this.dataReady=!0,this.version=0}getSize(e){let t=this.data;return typeof HTMLVideoElement<"u"&&t instanceof HTMLVideoElement?e.set(t.videoWidth,t.videoHeight,0):typeof VideoFrame<"u"&&t instanceof VideoFrame?e.set(t.displayWidth,t.displayHeight,0):t!==null?e.set(t.width||0,t.height||0,t.depth||0):e.set(0,0,0),e}set needsUpdate(e){e===!0&&this.version++}toJSON(e){let t=e===void 0||typeof e=="string";if(!t&&e.images[this.uuid]!==void 0)return e.images[this.uuid];let n={uuid:this.uuid,url:""},s=this.data;if(s!==null){let r;if(Array.isArray(s)){r=[];for(let a=0,o=s.length;a<o;a++)s[a].isDataTexture?r.push($a(s[a].image)):r.push($a(s[a]))}else r=$a(s);n.url=r}return t||(e.images[this.uuid]=n),n}};function $a(i){return typeof HTMLImageElement<"u"&&i instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&i instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&i instanceof ImageBitmap?Tr.getDataURL(i):i.data?{data:Array.from(i.data),width:i.width,height:i.height,type:i.data.constructor.name}:(Te("Texture: Unable to serialize Texture."),{})}var u1=0,Ka=new U,zt=class i extends ln{constructor(e=i.DEFAULT_IMAGE,t=i.DEFAULT_MAPPING,n=gn,s=gn,r=Ft,a=Dn,o=dn,l=Gt,c=i.DEFAULT_ANISOTROPY,h=Un){super(),this.isTexture=!0,Object.defineProperty(this,"id",{value:u1++}),this.uuid=Zi(),this.name="",this.source=new Oi(e),this.mipmaps=[],this.mapping=t,this.channel=0,this.wrapS=n,this.wrapT=s,this.magFilter=r,this.minFilter=a,this.anisotropy=c,this.format=o,this.internalFormat=null,this.type=l,this.offset=new Re(0,0),this.repeat=new Re(1,1),this.center=new Re(0,0),this.rotation=0,this.matrixAutoUpdate=!0,this.matrix=new Ie,this.generateMipmaps=!0,this.mipmapsAutoUpdate=!0,this.premultiplyAlpha=!1,this.flipY=!0,this.unpackAlignment=4,this.colorSpace=h,this.userData={},this.updateRanges=[],this.version=0,this.onUpdate=null,this.renderTarget=null,this.isRenderTargetTexture=!1,this.isArrayTexture=!!(e&&e.depth&&e.depth>1),this.pmremVersion=0,this.isPMREMTexture=!1,this.normalized=!1}get width(){return this.source.getSize(Ka).x}get height(){return this.source.getSize(Ka).y}get depth(){return this.source.getSize(Ka).z}get image(){return this.source.data}set image(e){this.source.data=e}updateMatrix(){this.matrix.setUvTransform(this.offset.x,this.offset.y,this.repeat.x,this.repeat.y,this.rotation,this.center.x,this.center.y)}addUpdateRange(e,t){this.updateRanges.push({start:e,count:t})}clearUpdateRanges(){this.updateRanges.length=0}clone(){return new this.constructor().copy(this)}copy(e){return this.name=e.name,this.source=e.source,this.mipmaps=e.mipmaps.slice(0),this.mapping=e.mapping,this.channel=e.channel,this.wrapS=e.wrapS,this.wrapT=e.wrapT,this.magFilter=e.magFilter,this.minFilter=e.minFilter,this.anisotropy=e.anisotropy,this.format=e.format,this.internalFormat=e.internalFormat,this.type=e.type,this.normalized=e.normalized,this.offset.copy(e.offset),this.repeat.copy(e.repeat),this.center.copy(e.center),this.rotation=e.rotation,this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrix.copy(e.matrix),this.generateMipmaps=e.generateMipmaps,this.mipmapsAutoUpdate=e.mipmapsAutoUpdate,this.premultiplyAlpha=e.premultiplyAlpha,this.flipY=e.flipY,this.unpackAlignment=e.unpackAlignment,this.colorSpace=e.colorSpace,this.renderTarget=e.renderTarget,this.isRenderTargetTexture=e.isRenderTargetTexture,this.isPMREMTexture=e.isPMREMTexture,this.isArrayTexture=e.isArrayTexture,this.userData=JSON.parse(JSON.stringify(e.userData)),this.needsUpdate=!0,this}setValues(e){for(let t in e){let n=e[t];if(n===void 0){Te(`Texture.setValues(): parameter '${t}' has value of undefined.`);continue}let s=this[t];if(s===void 0){Te(`Texture.setValues(): property '${t}' does not exist.`);continue}s&&n&&s.isVector2&&n.isVector2||s&&n&&s.isVector3&&n.isVector3||s&&n&&s.isMatrix3&&n.isMatrix3?s.copy(n):this[t]=n}}toJSON(e){let t=e===void 0||typeof e=="string";if(!t&&e.textures[this.uuid]!==void 0)return e.textures[this.uuid];let n={metadata:{version:4.7,type:"Texture",generator:"Texture.toJSON"},uuid:this.uuid,name:this.name,image:this.source.toJSON(e).uuid,mapping:this.mapping,channel:this.channel,repeat:[this.repeat.x,this.repeat.y],offset:[this.offset.x,this.offset.y],center:[this.center.x,this.center.y],rotation:this.rotation,wrap:[this.wrapS,this.wrapT],format:this.format,internalFormat:this.internalFormat,type:this.type,normalized:this.normalized,colorSpace:this.colorSpace,minFilter:this.minFilter,magFilter:this.magFilter,anisotropy:this.anisotropy,flipY:this.flipY,generateMipmaps:this.generateMipmaps,mipmapsAutoUpdate:this.mipmapsAutoUpdate,premultiplyAlpha:this.premultiplyAlpha,unpackAlignment:this.unpackAlignment};return Object.keys(this.userData).length>0&&(n.userData=this.userData),t||(e.textures[this.uuid]=n),n}dispose(){this.dispatchEvent({type:"dispose"})}transformUv(e){if(this.mapping!==Oo)return e;if(e.applyMatrix3(this.matrix),e.x<0||e.x>1)switch(this.wrapS){case Mr:e.x=e.x-Math.floor(e.x);break;case gn:e.x=e.x<0?0:1;break;case br:Math.abs(Math.floor(e.x)%2)===1?e.x=Math.ceil(e.x)-e.x:e.x=e.x-Math.floor(e.x);break}if(e.y<0||e.y>1)switch(this.wrapT){case Mr:e.y=e.y-Math.floor(e.y);break;case gn:e.y=e.y<0?0:1;break;case br:Math.abs(Math.floor(e.y)%2)===1?e.y=Math.ceil(e.y)-e.y:e.y=e.y-Math.floor(e.y);break}return this.flipY&&(e.y=1-e.y),e}set needsUpdate(e){e===!0&&(this.version++,this.source.needsUpdate=!0)}set needsPMREMUpdate(e){e===!0&&this.pmremVersion++}};zt.DEFAULT_IMAGE=null;zt.DEFAULT_MAPPING=Oo;zt.DEFAULT_ANISOTROPY=1;var ol=class ol{constructor(e=0,t=0,n=0,s=1){this.x=e,this.y=t,this.z=n,this.w=s}get width(){return this.z}set width(e){this.z=e}get height(){return this.w}set height(e){this.w=e}set(e,t,n,s){return this.x=e,this.y=t,this.z=n,this.w=s,this}setScalar(e){return this.x=e,this.y=e,this.z=e,this.w=e,this}setX(e){return this.x=e,this}setY(e){return this.y=e,this}setZ(e){return this.z=e,this}setW(e){return this.w=e,this}setComponent(e,t){switch(e){case 0:this.x=t;break;case 1:this.y=t;break;case 2:this.z=t;break;case 3:this.w=t;break;default:throw new Error("THREE.Vector4: index is out of range: "+e)}return this}getComponent(e){switch(e){case 0:return this.x;case 1:return this.y;case 2:return this.z;case 3:return this.w;default:throw new Error("THREE.Vector4: index is out of range: "+e)}}clone(){return new this.constructor(this.x,this.y,this.z,this.w)}copy(e){return this.x=e.x,this.y=e.y,this.z=e.z,this.w=e.w!==void 0?e.w:1,this}add(e){return this.x+=e.x,this.y+=e.y,this.z+=e.z,this.w+=e.w,this}addScalar(e){return this.x+=e,this.y+=e,this.z+=e,this.w+=e,this}addVectors(e,t){return this.x=e.x+t.x,this.y=e.y+t.y,this.z=e.z+t.z,this.w=e.w+t.w,this}addScaledVector(e,t){return this.x+=e.x*t,this.y+=e.y*t,this.z+=e.z*t,this.w+=e.w*t,this}sub(e){return this.x-=e.x,this.y-=e.y,this.z-=e.z,this.w-=e.w,this}subScalar(e){return this.x-=e,this.y-=e,this.z-=e,this.w-=e,this}subVectors(e,t){return this.x=e.x-t.x,this.y=e.y-t.y,this.z=e.z-t.z,this.w=e.w-t.w,this}multiply(e){return this.x*=e.x,this.y*=e.y,this.z*=e.z,this.w*=e.w,this}multiplyScalar(e){return this.x*=e,this.y*=e,this.z*=e,this.w*=e,this}applyMatrix4(e){let t=this.x,n=this.y,s=this.z,r=this.w,a=e.elements;return this.x=a[0]*t+a[4]*n+a[8]*s+a[12]*r,this.y=a[1]*t+a[5]*n+a[9]*s+a[13]*r,this.z=a[2]*t+a[6]*n+a[10]*s+a[14]*r,this.w=a[3]*t+a[7]*n+a[11]*s+a[15]*r,this}divide(e){return this.x/=e.x,this.y/=e.y,this.z/=e.z,this.w/=e.w,this}divideScalar(e){return this.multiplyScalar(1/e)}setAxisAngleFromQuaternion(e){this.w=2*Math.acos(e.w);let t=Math.sqrt(1-e.w*e.w);return t<1e-4?(this.x=1,this.y=0,this.z=0):(this.x=e.x/t,this.y=e.y/t,this.z=e.z/t),this}setAxisAngleFromRotationMatrix(e){let t,n,s,r,l=e.elements,c=l[0],h=l[4],g=l[8],d=l[1],m=l[5],_=l[9],S=l[2],p=l[6],u=l[10];if(Math.abs(h-d)<.01&&Math.abs(g-S)<.01&&Math.abs(_-p)<.01){if(Math.abs(h+d)<.1&&Math.abs(g+S)<.1&&Math.abs(_+p)<.1&&Math.abs(c+m+u-3)<.1)return this.set(1,0,0,0),this;t=Math.PI;let w=(c+1)/2,E=(m+1)/2,A=(u+1)/2,T=(h+d)/4,f=(g+S)/4,v=(_+p)/4;return w>E&&w>A?w<.01?(n=0,s=.707106781,r=.707106781):(n=Math.sqrt(w),s=T/n,r=f/n):E>A?E<.01?(n=.707106781,s=0,r=.707106781):(s=Math.sqrt(E),n=T/s,r=v/s):A<.01?(n=.707106781,s=.707106781,r=0):(r=Math.sqrt(A),n=f/r,s=v/r),this.set(n,s,r,t),this}let M=Math.sqrt((p-_)*(p-_)+(g-S)*(g-S)+(d-h)*(d-h));return Math.abs(M)<.001&&(M=1),this.x=(p-_)/M,this.y=(g-S)/M,this.z=(d-h)/M,this.w=Math.acos((c+m+u-1)/2),this}setFromMatrixPosition(e){let t=e.elements;return this.x=t[12],this.y=t[13],this.z=t[14],this.w=t[15],this}min(e){return this.x=Math.min(this.x,e.x),this.y=Math.min(this.y,e.y),this.z=Math.min(this.z,e.z),this.w=Math.min(this.w,e.w),this}max(e){return this.x=Math.max(this.x,e.x),this.y=Math.max(this.y,e.y),this.z=Math.max(this.z,e.z),this.w=Math.max(this.w,e.w),this}clamp(e,t){return this.x=ke(this.x,e.x,t.x),this.y=ke(this.y,e.y,t.y),this.z=ke(this.z,e.z,t.z),this.w=ke(this.w,e.w,t.w),this}clampScalar(e,t){return this.x=ke(this.x,e,t),this.y=ke(this.y,e,t),this.z=ke(this.z,e,t),this.w=ke(this.w,e,t),this}clampLength(e,t){let n=this.length();return this.divideScalar(n||1).multiplyScalar(ke(n,e,t))}floor(){return this.x=Math.floor(this.x),this.y=Math.floor(this.y),this.z=Math.floor(this.z),this.w=Math.floor(this.w),this}ceil(){return this.x=Math.ceil(this.x),this.y=Math.ceil(this.y),this.z=Math.ceil(this.z),this.w=Math.ceil(this.w),this}round(){return this.x=Math.round(this.x),this.y=Math.round(this.y),this.z=Math.round(this.z),this.w=Math.round(this.w),this}roundToZero(){return this.x=Math.trunc(this.x),this.y=Math.trunc(this.y),this.z=Math.trunc(this.z),this.w=Math.trunc(this.w),this}negate(){return this.x=-this.x,this.y=-this.y,this.z=-this.z,this.w=-this.w,this}dot(e){return this.x*e.x+this.y*e.y+this.z*e.z+this.w*e.w}lengthSq(){return this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w}length(){return Math.sqrt(this.x*this.x+this.y*this.y+this.z*this.z+this.w*this.w)}manhattanLength(){return Math.abs(this.x)+Math.abs(this.y)+Math.abs(this.z)+Math.abs(this.w)}normalize(){return this.divideScalar(this.length()||1)}setLength(e){return this.normalize().multiplyScalar(e)}lerp(e,t){return this.x+=(e.x-this.x)*t,this.y+=(e.y-this.y)*t,this.z+=(e.z-this.z)*t,this.w+=(e.w-this.w)*t,this}lerpVectors(e,t,n){return this.x=e.x+(t.x-e.x)*n,this.y=e.y+(t.y-e.y)*n,this.z=e.z+(t.z-e.z)*n,this.w=e.w+(t.w-e.w)*n,this}equals(e){return e.x===this.x&&e.y===this.y&&e.z===this.z&&e.w===this.w}fromArray(e,t=0){return this.x=e[t],this.y=e[t+1],this.z=e[t+2],this.w=e[t+3],this}toArray(e=[],t=0){return e[t]=this.x,e[t+1]=this.y,e[t+2]=this.z,e[t+3]=this.w,e}fromBufferAttribute(e,t){return this.x=e.getX(t),this.y=e.getY(t),this.z=e.getZ(t),this.w=e.getW(t),this}random(){return this.x=Math.random(),this.y=Math.random(),this.z=Math.random(),this.w=Math.random(),this}*[Symbol.iterator](){yield this.x,yield this.y,yield this.z,yield this.w}};ol.prototype.isVector4=!0;var at=ol,Ar=class extends ln{constructor(e=1,t=1,n={}){super(),n=Object.assign({generateMipmaps:!1,internalFormat:null,minFilter:Ft,depthBuffer:!0,stencilBuffer:!1,resolveColorBuffer:!0,resolveDepthBuffer:!0,resolveStencilBuffer:!0,storeMultisampledColorBuffer:!0,storeMultisampledDepthBuffer:!0,storeMultisampledStencilBuffer:!0,depthTexture:null,samples:0,count:1,depth:1,multiview:!1,useArrayDepthTexture:!1},n),this.isRenderTarget=!0,this.width=e,this.height=t,this.depth=n.depth,this.scissor=new at(0,0,e,t),this.scissorTest=!1,this.viewport=new at(0,0,e,t),this.textures=[];let s=n.count;for(let r=0;r<s;r++)this.textures[r]=new zt({width:e,height:t,depth:n.depth}),this.textures[r].isRenderTargetTexture=!0,this.textures[r].renderTarget=this;this._setTextureOptions(n),this.depthBuffer=n.depthBuffer,this.stencilBuffer=n.stencilBuffer,this.resolveColorBuffer=n.resolveColorBuffer,this.resolveDepthBuffer=n.resolveDepthBuffer,this.resolveStencilBuffer=n.resolveStencilBuffer,this.storeMultisampledColorBuffer=n.storeMultisampledColorBuffer,this.storeMultisampledDepthBuffer=n.storeMultisampledDepthBuffer,this.storeMultisampledStencilBuffer=n.storeMultisampledStencilBuffer,this._depthTexture=null,this.depthTexture=n.depthTexture,this.samples=n.samples,this.multiview=n.multiview,this.useArrayDepthTexture=n.useArrayDepthTexture}_setTextureOptions(e={}){let t={minFilter:Ft,generateMipmaps:!1,flipY:!1,internalFormat:null};e.mapping!==void 0&&(t.mapping=e.mapping),e.wrapS!==void 0&&(t.wrapS=e.wrapS),e.wrapT!==void 0&&(t.wrapT=e.wrapT),e.wrapR!==void 0&&(t.wrapR=e.wrapR),e.magFilter!==void 0&&(t.magFilter=e.magFilter),e.minFilter!==void 0&&(t.minFilter=e.minFilter),e.format!==void 0&&(t.format=e.format),e.type!==void 0&&(t.type=e.type),e.anisotropy!==void 0&&(t.anisotropy=e.anisotropy),e.colorSpace!==void 0&&(t.colorSpace=e.colorSpace),e.flipY!==void 0&&(t.flipY=e.flipY),e.generateMipmaps!==void 0&&(t.generateMipmaps=e.generateMipmaps),e.mipmapsAutoUpdate!==void 0&&(t.mipmapsAutoUpdate=e.mipmapsAutoUpdate),e.internalFormat!==void 0&&(t.internalFormat=e.internalFormat);for(let n=0;n<this.textures.length;n++)this.textures[n].setValues(t)}get texture(){return this.textures[0]}set texture(e){this.textures[0]=e}set depthTexture(e){this._depthTexture!==null&&this._depthTexture.renderTarget===this&&(this._depthTexture.renderTarget=null),e!==null&&e.renderTarget===null&&(e.renderTarget=this),this._depthTexture=e}get depthTexture(){return this._depthTexture}setSize(e,t,n=1){if(this.width!==e||this.height!==t||this.depth!==n){this.width=e,this.height=t,this.depth=n;for(let s=0,r=this.textures.length;s<r;s++)this.textures[s].image.width=e,this.textures[s].image.height=t,this.textures[s].image.depth=n,this.textures[s].isData3DTexture!==!0&&(this.textures[s].isArrayTexture=this.textures[s].image.depth>1);this.dispose()}this.viewport.set(0,0,e,t),this.scissor.set(0,0,e,t)}clone(){return new this.constructor().copy(this)}copy(e){this.width=e.width,this.height=e.height,this.depth=e.depth,this.scissor.copy(e.scissor),this.scissorTest=e.scissorTest,this.viewport.copy(e.viewport),this.textures.length=0;for(let t=0,n=e.textures.length;t<n;t++){this.textures[t]=e.textures[t].clone(),this.textures[t].isRenderTargetTexture=!0,this.textures[t].renderTarget=this;let s=Object.assign({},e.textures[t].image);this.textures[t].source=new Oi(s)}if(this.depthBuffer=e.depthBuffer,this.stencilBuffer=e.stencilBuffer,this.resolveColorBuffer=e.resolveColorBuffer,this.resolveDepthBuffer=e.resolveDepthBuffer,this.resolveStencilBuffer=e.resolveStencilBuffer,this.storeMultisampledColorBuffer=e.storeMultisampledColorBuffer,this.storeMultisampledDepthBuffer=e.storeMultisampledDepthBuffer,this.storeMultisampledStencilBuffer=e.storeMultisampledStencilBuffer,e.depthTexture!==null)if(e.depthTexture.renderTarget===e){let t=e.depthTexture.clone();t.renderTarget=null,this.depthTexture=t}else this.depthTexture=e.depthTexture;else this.depthTexture=null;return this.samples=e.samples,this.multiview=e.multiview,this.useArrayDepthTexture=e.useArrayDepthTexture,this}dispose(){this.dispatchEvent({type:"dispose"})}},Yt=class extends Ar{constructor(e=1,t=1,n={}){super(e,t,n),this.isWebGLRenderTarget=!0}},hs=class extends zt{constructor(e=null,t=1,n=1,s=1){super(null),this.isDataArrayTexture=!0,this.image={data:e,width:t,height:n,depth:s},this.magFilter=Mt,this.minFilter=Mt,this.wrapR=gn,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1,this.layerUpdates=new Set}copy(e){return super.copy(e),this.wrapR=e.wrapR,this}addLayerUpdate(e){this.layerUpdates.add(e)}clearLayerUpdates(){this.layerUpdates.clear()}};var wr=class extends zt{constructor(e=null,t=1,n=1,s=1){super(null),this.isData3DTexture=!0,this.image={data:e,width:t,height:n,depth:s},this.magFilter=Mt,this.minFilter=Mt,this.wrapR=gn,this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}copy(e){return super.copy(e),this.wrapR=e.wrapR,this}};var Yr=class Yr{constructor(e,t,n,s,r,a,o,l,c,h,g,d,m,_,S,p){this.elements=[1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1],e!==void 0&&this.set(e,t,n,s,r,a,o,l,c,h,g,d,m,_,S,p)}set(e,t,n,s,r,a,o,l,c,h,g,d,m,_,S,p){let u=this.elements;return u[0]=e,u[4]=t,u[8]=n,u[12]=s,u[1]=r,u[5]=a,u[9]=o,u[13]=l,u[2]=c,u[6]=h,u[10]=g,u[14]=d,u[3]=m,u[7]=_,u[11]=S,u[15]=p,this}identity(){return this.set(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1),this}clone(){return new Yr().fromArray(this.elements)}copy(e){let t=this.elements,n=e.elements;return t[0]=n[0],t[1]=n[1],t[2]=n[2],t[3]=n[3],t[4]=n[4],t[5]=n[5],t[6]=n[6],t[7]=n[7],t[8]=n[8],t[9]=n[9],t[10]=n[10],t[11]=n[11],t[12]=n[12],t[13]=n[13],t[14]=n[14],t[15]=n[15],this}copyPosition(e){let t=this.elements,n=e.elements;return t[12]=n[12],t[13]=n[13],t[14]=n[14],this}setFromMatrix3(e){let t=e.elements;return this.set(t[0],t[3],t[6],0,t[1],t[4],t[7],0,t[2],t[5],t[8],0,0,0,0,1),this}extractBasis(e,t,n){return this.determinantAffine()===0?(e.set(1,0,0),t.set(0,1,0),n.set(0,0,1),this):(e.setFromMatrixColumn(this,0),t.setFromMatrixColumn(this,1),n.setFromMatrixColumn(this,2),this)}makeBasis(e,t,n){return this.set(e.x,t.x,n.x,0,e.y,t.y,n.y,0,e.z,t.z,n.z,0,0,0,0,1),this}extractRotation(e){if(e.determinantAffine()===0)return this.identity();let t=this.elements,n=e.elements,s=1/vi.setFromMatrixColumn(e,0).length(),r=1/vi.setFromMatrixColumn(e,1).length(),a=1/vi.setFromMatrixColumn(e,2).length();return t[0]=n[0]*s,t[1]=n[1]*s,t[2]=n[2]*s,t[3]=0,t[4]=n[4]*r,t[5]=n[5]*r,t[6]=n[6]*r,t[7]=0,t[8]=n[8]*a,t[9]=n[9]*a,t[10]=n[10]*a,t[11]=0,t[12]=0,t[13]=0,t[14]=0,t[15]=1,this}makeRotationFromEuler(e){let t=this.elements,n=e.x,s=e.y,r=e.z,a=Math.cos(n),o=Math.sin(n),l=Math.cos(s),c=Math.sin(s),h=Math.cos(r),g=Math.sin(r);if(e.order==="XYZ"){let d=a*h,m=a*g,_=o*h,S=o*g;t[0]=l*h,t[4]=-l*g,t[8]=c,t[1]=m+_*c,t[5]=d-S*c,t[9]=-o*l,t[2]=S-d*c,t[6]=_+m*c,t[10]=a*l}else if(e.order==="YXZ"){let d=l*h,m=l*g,_=c*h,S=c*g;t[0]=d+S*o,t[4]=_*o-m,t[8]=a*c,t[1]=a*g,t[5]=a*h,t[9]=-o,t[2]=m*o-_,t[6]=S+d*o,t[10]=a*l}else if(e.order==="ZXY"){let d=l*h,m=l*g,_=c*h,S=c*g;t[0]=d-S*o,t[4]=-a*g,t[8]=_+m*o,t[1]=m+_*o,t[5]=a*h,t[9]=S-d*o,t[2]=-a*c,t[6]=o,t[10]=a*l}else if(e.order==="ZYX"){let d=a*h,m=a*g,_=o*h,S=o*g;t[0]=l*h,t[4]=_*c-m,t[8]=d*c+S,t[1]=l*g,t[5]=S*c+d,t[9]=m*c-_,t[2]=-c,t[6]=o*l,t[10]=a*l}else if(e.order==="YZX"){let d=a*l,m=a*c,_=o*l,S=o*c;t[0]=l*h,t[4]=S-d*g,t[8]=_*g+m,t[1]=g,t[5]=a*h,t[9]=-o*h,t[2]=-c*h,t[6]=m*g+_,t[10]=d-S*g}else if(e.order==="XZY"){let d=a*l,m=a*c,_=o*l,S=o*c;t[0]=l*h,t[4]=-g,t[8]=c*h,t[1]=d*g+S,t[5]=a*h,t[9]=m*g-_,t[2]=_*g-m,t[6]=o*h,t[10]=S*g+d}return t[3]=0,t[7]=0,t[11]=0,t[12]=0,t[13]=0,t[14]=0,t[15]=1,this}makeRotationFromQuaternion(e){return this.compose(d1,e,f1)}lookAt(e,t,n){let s=this.elements;return Ht.subVectors(e,t),Ht.lengthSq()===0&&(Ht.z=1),Ht.normalize(),Bn.crossVectors(n,Ht),Bn.lengthSq()===0&&(Math.abs(n.z)===1?Ht.x+=1e-4:Ht.z+=1e-4,Ht.normalize(),Bn.crossVectors(n,Ht)),Bn.normalize(),Xs.crossVectors(Ht,Bn),s[0]=Bn.x,s[4]=Xs.x,s[8]=Ht.x,s[1]=Bn.y,s[5]=Xs.y,s[9]=Ht.y,s[2]=Bn.z,s[6]=Xs.z,s[10]=Ht.z,this}multiply(e){return this.multiplyMatrices(this,e)}premultiply(e){return this.multiplyMatrices(e,this)}multiplyMatrices(e,t){let n=e.elements,s=t.elements,r=this.elements,a=n[0],o=n[4],l=n[8],c=n[12],h=n[1],g=n[5],d=n[9],m=n[13],_=n[2],S=n[6],p=n[10],u=n[14],M=n[3],w=n[7],E=n[11],A=n[15],T=s[0],f=s[4],v=s[8],N=s[12],I=s[1],D=s[5],z=s[9],q=s[13],P=s[2],W=s[6],$=s[10],G=s[14],te=s[3],H=s[7],j=s[11],Q=s[15];return r[0]=a*T+o*I+l*P+c*te,r[4]=a*f+o*D+l*W+c*H,r[8]=a*v+o*z+l*$+c*j,r[12]=a*N+o*q+l*G+c*Q,r[1]=h*T+g*I+d*P+m*te,r[5]=h*f+g*D+d*W+m*H,r[9]=h*v+g*z+d*$+m*j,r[13]=h*N+g*q+d*G+m*Q,r[2]=_*T+S*I+p*P+u*te,r[6]=_*f+S*D+p*W+u*H,r[10]=_*v+S*z+p*$+u*j,r[14]=_*N+S*q+p*G+u*Q,r[3]=M*T+w*I+E*P+A*te,r[7]=M*f+w*D+E*W+A*H,r[11]=M*v+w*z+E*$+A*j,r[15]=M*N+w*q+E*G+A*Q,this}multiplyScalar(e){let t=this.elements;return t[0]*=e,t[4]*=e,t[8]*=e,t[12]*=e,t[1]*=e,t[5]*=e,t[9]*=e,t[13]*=e,t[2]*=e,t[6]*=e,t[10]*=e,t[14]*=e,t[3]*=e,t[7]*=e,t[11]*=e,t[15]*=e,this}determinant(){let e=this.elements,t=e[0],n=e[4],s=e[8],r=e[12],a=e[1],o=e[5],l=e[9],c=e[13],h=e[2],g=e[6],d=e[10],m=e[14],_=e[3],S=e[7],p=e[11],u=e[15],M=l*m-c*d,w=o*m-c*g,E=o*d-l*g,A=a*m-c*h,T=a*d-l*h,f=a*g-o*h;return t*(S*M-p*w+u*E)-n*(_*M-p*A+u*T)+s*(_*w-S*A+u*f)-r*(_*E-S*T+p*f)}determinantAffine(){let e=this.elements,t=e[0],n=e[4],s=e[8],r=e[1],a=e[5],o=e[9],l=e[2],c=e[6],h=e[10];return t*(a*h-o*c)-n*(r*h-o*l)+s*(r*c-a*l)}transpose(){let e=this.elements,t;return t=e[1],e[1]=e[4],e[4]=t,t=e[2],e[2]=e[8],e[8]=t,t=e[6],e[6]=e[9],e[9]=t,t=e[3],e[3]=e[12],e[12]=t,t=e[7],e[7]=e[13],e[13]=t,t=e[11],e[11]=e[14],e[14]=t,this}setPosition(e,t,n){let s=this.elements;return e.isVector3?(s[12]=e.x,s[13]=e.y,s[14]=e.z):(s[12]=e,s[13]=t,s[14]=n),this}invert(){let e=this.elements,t=e[0],n=e[1],s=e[2],r=e[3],a=e[4],o=e[5],l=e[6],c=e[7],h=e[8],g=e[9],d=e[10],m=e[11],_=e[12],S=e[13],p=e[14],u=e[15],M=t*o-n*a,w=t*l-s*a,E=t*c-r*a,A=n*l-s*o,T=n*c-r*o,f=s*c-r*l,v=h*S-g*_,N=h*p-d*_,I=h*u-m*_,D=g*p-d*S,z=g*u-m*S,q=d*u-m*p,P=M*q-w*z+E*D+A*I-T*N+f*v;if(P===0)return this.set(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);let W=1/P;return e[0]=(o*q-l*z+c*D)*W,e[1]=(s*z-n*q-r*D)*W,e[2]=(S*f-p*T+u*A)*W,e[3]=(d*T-g*f-m*A)*W,e[4]=(l*I-a*q-c*N)*W,e[5]=(t*q-s*I+r*N)*W,e[6]=(p*E-_*f-u*w)*W,e[7]=(h*f-d*E+m*w)*W,e[8]=(a*z-o*I+c*v)*W,e[9]=(n*I-t*z-r*v)*W,e[10]=(_*T-S*E+u*M)*W,e[11]=(g*E-h*T-m*M)*W,e[12]=(o*N-a*D-l*v)*W,e[13]=(t*D-n*N+s*v)*W,e[14]=(S*w-_*A-p*M)*W,e[15]=(h*A-g*w+d*M)*W,this}scale(e){let t=this.elements,n=e.x,s=e.y,r=e.z;return t[0]*=n,t[4]*=s,t[8]*=r,t[1]*=n,t[5]*=s,t[9]*=r,t[2]*=n,t[6]*=s,t[10]*=r,t[3]*=n,t[7]*=s,t[11]*=r,this}getMaxScaleOnAxis(){let e=this.elements,t=e[0]*e[0]+e[1]*e[1]+e[2]*e[2],n=e[4]*e[4]+e[5]*e[5]+e[6]*e[6],s=e[8]*e[8]+e[9]*e[9]+e[10]*e[10];return Math.sqrt(Math.max(t,n,s))}makeTranslation(e,t,n){return e.isVector3?this.set(1,0,0,e.x,0,1,0,e.y,0,0,1,e.z,0,0,0,1):this.set(1,0,0,e,0,1,0,t,0,0,1,n,0,0,0,1),this}makeRotationX(e){let t=Math.cos(e),n=Math.sin(e);return this.set(1,0,0,0,0,t,-n,0,0,n,t,0,0,0,0,1),this}makeRotationY(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,0,n,0,0,1,0,0,-n,0,t,0,0,0,0,1),this}makeRotationZ(e){let t=Math.cos(e),n=Math.sin(e);return this.set(t,-n,0,0,n,t,0,0,0,0,1,0,0,0,0,1),this}makeRotationAxis(e,t){let n=Math.cos(t),s=Math.sin(t),r=1-n,a=e.x,o=e.y,l=e.z,c=r*a,h=r*o;return this.set(c*a+n,c*o-s*l,c*l+s*o,0,c*o+s*l,h*o+n,h*l-s*a,0,c*l-s*o,h*l+s*a,r*l*l+n,0,0,0,0,1),this}makeScale(e,t,n){return this.set(e,0,0,0,0,t,0,0,0,0,n,0,0,0,0,1),this}makeShear(e,t,n,s,r,a){return this.set(1,n,r,0,e,1,a,0,t,s,1,0,0,0,0,1),this}compose(e,t,n){let s=this.elements,r=t._x,a=t._y,o=t._z,l=t._w,c=r+r,h=a+a,g=o+o,d=r*c,m=r*h,_=r*g,S=a*h,p=a*g,u=o*g,M=l*c,w=l*h,E=l*g,A=n.x,T=n.y,f=n.z;return s[0]=(1-(S+u))*A,s[1]=(m+E)*A,s[2]=(_-w)*A,s[3]=0,s[4]=(m-E)*T,s[5]=(1-(d+u))*T,s[6]=(p+M)*T,s[7]=0,s[8]=(_+w)*f,s[9]=(p-M)*f,s[10]=(1-(d+S))*f,s[11]=0,s[12]=e.x,s[13]=e.y,s[14]=e.z,s[15]=1,this}decompose(e,t,n){let s=this.elements;e.x=s[12],e.y=s[13],e.z=s[14];let r=this.determinantAffine();if(r===0)return n.set(1,1,1),t.identity(),this;let a=vi.set(s[0],s[1],s[2]).length(),o=vi.set(s[4],s[5],s[6]).length(),l=vi.set(s[8],s[9],s[10]).length();r<0&&(a=-a),rn.copy(this);let c=1/a,h=1/o,g=1/l;return rn.elements[0]*=c,rn.elements[1]*=c,rn.elements[2]*=c,rn.elements[4]*=h,rn.elements[5]*=h,rn.elements[6]*=h,rn.elements[8]*=g,rn.elements[9]*=g,rn.elements[10]*=g,t.setFromRotationMatrix(rn),n.x=a,n.y=o,n.z=l,this}makePerspective(e,t,n,s,r,a,o=en,l=!1){let c=this.elements,h=2*r/(t-e),g=2*r/(n-s),d=(t+e)/(t-e),m=(n+s)/(n-s),_,S;if(l)_=r/(a-r),S=a*r/(a-r);else if(o===en)_=-(a+r)/(a-r),S=-2*a*r/(a-r);else if(o===Ni)_=-a/(a-r),S=-a*r/(a-r);else throw new Error("THREE.Matrix4.makePerspective(): Invalid coordinate system: "+o);return c[0]=h,c[4]=0,c[8]=d,c[12]=0,c[1]=0,c[5]=g,c[9]=m,c[13]=0,c[2]=0,c[6]=0,c[10]=_,c[14]=S,c[3]=0,c[7]=0,c[11]=-1,c[15]=0,this}makeOrthographic(e,t,n,s,r,a,o=en,l=!1){let c=this.elements,h=2/(t-e),g=2/(n-s),d=-(t+e)/(t-e),m=-(n+s)/(n-s),_,S;if(l)_=1/(a-r),S=a/(a-r);else if(o===en)_=-2/(a-r),S=-(a+r)/(a-r);else if(o===Ni)_=-1/(a-r),S=-r/(a-r);else throw new Error("THREE.Matrix4.makeOrthographic(): Invalid coordinate system: "+o);return c[0]=h,c[4]=0,c[8]=0,c[12]=d,c[1]=0,c[5]=g,c[9]=0,c[13]=m,c[2]=0,c[6]=0,c[10]=_,c[14]=S,c[3]=0,c[7]=0,c[11]=0,c[15]=1,this}equals(e){let t=this.elements,n=e.elements;for(let s=0;s<16;s++)if(t[s]!==n[s])return!1;return!0}fromArray(e,t=0){for(let n=0;n<16;n++)this.elements[n]=e[n+t];return this}toArray(e=[],t=0){let n=this.elements;return e[t]=n[0],e[t+1]=n[1],e[t+2]=n[2],e[t+3]=n[3],e[t+4]=n[4],e[t+5]=n[5],e[t+6]=n[6],e[t+7]=n[7],e[t+8]=n[8],e[t+9]=n[9],e[t+10]=n[10],e[t+11]=n[11],e[t+12]=n[12],e[t+13]=n[13],e[t+14]=n[14],e[t+15]=n[15],e}};Yr.prototype.isMatrix4=!0;var nt=Yr,vi=new U,rn=new nt,d1=new U(0,0,0),f1=new U(1,1,1),Bn=new U,Xs=new U,Ht=new U,Wl=new nt,Xl=new qt,Pn=class i{constructor(e=0,t=0,n=0,s=i.DEFAULT_ORDER){this.isEuler=!0,this._x=e,this._y=t,this._z=n,this._order=s}get x(){return this._x}set x(e){this._x=e,this._onChangeCallback()}get y(){return this._y}set y(e){this._y=e,this._onChangeCallback()}get z(){return this._z}set z(e){this._z=e,this._onChangeCallback()}get order(){return this._order}set order(e){this._order=e,this._onChangeCallback()}set(e,t,n,s=this._order){return this._x=e,this._y=t,this._z=n,this._order=s,this._onChangeCallback(),this}clone(){return new this.constructor(this._x,this._y,this._z,this._order)}copy(e){return this._x=e._x,this._y=e._y,this._z=e._z,this._order=e._order,this._onChangeCallback(),this}setFromRotationMatrix(e,t=this._order,n=!0){let s=e.elements,r=s[0],a=s[4],o=s[8],l=s[1],c=s[5],h=s[9],g=s[2],d=s[6],m=s[10];switch(t){case"XYZ":this._y=Math.asin(ke(o,-1,1)),Math.abs(o)<.9999999?(this._x=Math.atan2(-h,m),this._z=Math.atan2(-a,r)):(this._x=Math.atan2(d,c),this._z=0);break;case"YXZ":this._x=Math.asin(-ke(h,-1,1)),Math.abs(h)<.9999999?(this._y=Math.atan2(o,m),this._z=Math.atan2(l,c)):(this._y=Math.atan2(-g,r),this._z=0);break;case"ZXY":this._x=Math.asin(ke(d,-1,1)),Math.abs(d)<.9999999?(this._y=Math.atan2(-g,m),this._z=Math.atan2(-a,c)):(this._y=0,this._z=Math.atan2(l,r));break;case"ZYX":this._y=Math.asin(-ke(g,-1,1)),Math.abs(g)<.9999999?(this._x=Math.atan2(d,m),this._z=Math.atan2(l,r)):(this._x=0,this._z=Math.atan2(-a,c));break;case"YZX":this._z=Math.asin(ke(l,-1,1)),Math.abs(l)<.9999999?(this._x=Math.atan2(-h,c),this._y=Math.atan2(-g,r)):(this._x=0,this._y=Math.atan2(o,m));break;case"XZY":this._z=Math.asin(-ke(a,-1,1)),Math.abs(a)<.9999999?(this._x=Math.atan2(d,c),this._y=Math.atan2(o,r)):(this._x=Math.atan2(-h,m),this._y=0);break;default:Te("Euler: .setFromRotationMatrix() encountered an unknown order: "+t)}return this._order=t,n===!0&&this._onChangeCallback(),this}setFromQuaternion(e,t,n){return Wl.makeRotationFromQuaternion(e),this.setFromRotationMatrix(Wl,t,n)}setFromVector3(e,t=this._order){return this.set(e.x,e.y,e.z,t)}reorder(e){return Xl.setFromEuler(this),this.setFromQuaternion(Xl,e)}equals(e){return e._x===this._x&&e._y===this._y&&e._z===this._z&&e._order===this._order}fromArray(e){return this._x=e[0],this._y=e[1],this._z=e[2],e[3]!==void 0&&(this._order=e[3]),this._onChangeCallback(),this}toArray(e=[],t=0){return e[t]=this._x,e[t+1]=this._y,e[t+2]=this._z,e[t+3]=this._order,e}_onChange(e){return this._onChangeCallback=e,this}_onChangeCallback(){}*[Symbol.iterator](){yield this._x,yield this._y,yield this._z,yield this._order}};Pn.DEFAULT_ORDER="XYZ";var Bi=class{constructor(){this.mask=1}set(e){this.mask=(1<<e|0)>>>0}enable(e){this.mask|=1<<e|0}enableAll(){this.mask=-1}toggle(e){this.mask^=1<<e|0}disable(e){this.mask&=~(1<<e|0)}disableAll(){this.mask=0}test(e){return(this.mask&e.mask)!==0}isEnabled(e){return(this.mask&(1<<e|0))!==0}},p1=0,ql=new U,Si=new qt,Mn=new nt,qs=new U,ji=new U,m1=new U,g1=new qt,Yl=new U(1,0,0),Zl=new U(0,1,0),Jl=new U(0,0,1),$l={type:"added"},_1={type:"removed"},Mi={type:"childadded",child:null},ja={type:"childremoved",child:null},Pt=class i extends ln{constructor(){super(),this.isObject3D=!0,Object.defineProperty(this,"id",{value:p1++}),this.uuid=Zi(),this.name="",this.type="Object3D",this.parent=null,this.children=[],this.up=i.DEFAULT_UP.clone();let e=new U,t=new Pn,n=new qt,s=new U(1,1,1);function r(){n.setFromEuler(t,!1)}function a(){t.setFromQuaternion(n,void 0,!1)}t._onChange(r),n._onChange(a),Object.defineProperties(this,{position:{configurable:!0,enumerable:!0,value:e},rotation:{configurable:!0,enumerable:!0,value:t},quaternion:{configurable:!0,enumerable:!0,value:n},scale:{configurable:!0,enumerable:!0,value:s},modelViewMatrix:{value:new nt},normalMatrix:{value:new Ie}}),this.matrix=new nt,this.matrixWorld=new nt,this.matrixAutoUpdate=i.DEFAULT_MATRIX_AUTO_UPDATE,this.matrixWorldAutoUpdate=i.DEFAULT_MATRIX_WORLD_AUTO_UPDATE,this.matrixWorldNeedsUpdate=!1,this.layers=new Bi,this.visible=!0,this.castShadow=!1,this.receiveShadow=!1,this.frustumCulled=!0,this.renderOrder=0,this.animations=[],this.customDepthMaterial=void 0,this.customDistanceMaterial=void 0,this.static=!1,this.userData={},this.pivot=null}onBeforeShadow(){}onAfterShadow(){}onBeforeRender(){}onAfterRender(){}applyMatrix4(e){this.matrixAutoUpdate&&this.updateMatrix(),this.matrix.premultiply(e),this.matrix.decompose(this.position,this.quaternion,this.scale),this.pivot!==null&&this.position.copy(this.pivot).applyMatrix4(this.matrix).sub(this.pivot)}applyQuaternion(e){return this.quaternion.premultiply(e),this}setRotationFromAxisAngle(e,t){this.quaternion.setFromAxisAngle(e,t)}setRotationFromEuler(e){this.quaternion.setFromEuler(e,!0)}setRotationFromMatrix(e){this.quaternion.setFromRotationMatrix(e)}setRotationFromQuaternion(e){this.quaternion.copy(e)}rotateOnAxis(e,t){return Si.setFromAxisAngle(e,t),this.quaternion.multiply(Si),this}rotateOnWorldAxis(e,t){return Si.setFromAxisAngle(e,t),this.quaternion.premultiply(Si),this}rotateX(e){return this.rotateOnAxis(Yl,e)}rotateY(e){return this.rotateOnAxis(Zl,e)}rotateZ(e){return this.rotateOnAxis(Jl,e)}translateOnAxis(e,t){return ql.copy(e).applyQuaternion(this.quaternion),this.position.add(ql.multiplyScalar(t)),this}translateX(e){return this.translateOnAxis(Yl,e)}translateY(e){return this.translateOnAxis(Zl,e)}translateZ(e){return this.translateOnAxis(Jl,e)}localToWorld(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(this.matrixWorld)}worldToLocal(e){return this.updateWorldMatrix(!0,!1),e.applyMatrix4(Mn.copy(this.matrixWorld).invert())}lookAt(e,t,n){e.isVector3?qs.copy(e):qs.set(e,t,n);let s=this.parent;this.updateWorldMatrix(!0,!1),ji.setFromMatrixPosition(this.matrixWorld),this.isCamera||this.isLight?Mn.lookAt(ji,qs,this.up):Mn.lookAt(qs,ji,this.up),this.quaternion.setFromRotationMatrix(Mn),s&&(Mn.extractRotation(s.matrixWorld),Si.setFromRotationMatrix(Mn),this.quaternion.premultiply(Si.invert()))}add(e){if(arguments.length>1){for(let t=0;t<arguments.length;t++)this.add(arguments[t]);return this}return e===this?(Pe("Object3D.add: object can't be added as a child of itself.",e),this):(e&&e.isObject3D?(e.removeFromParent(),e.parent=this,this.children.push(e),e.dispatchEvent($l),Mi.child=e,this.dispatchEvent(Mi),Mi.child=null):Pe("Object3D.add: object not an instance of THREE.Object3D.",e),this)}remove(e){if(arguments.length>1){for(let n=0;n<arguments.length;n++)this.remove(arguments[n]);return this}let t=this.children.indexOf(e);return t!==-1&&(e.parent=null,this.children.splice(t,1),e.dispatchEvent(_1),ja.child=e,this.dispatchEvent(ja),ja.child=null),this}removeFromParent(){let e=this.parent;return e!==null&&e.remove(this),this}clear(){return this.remove(...this.children)}attach(e){return this.updateWorldMatrix(!0,!1),Mn.copy(this.matrixWorld).invert(),e.parent!==null&&(e.parent.updateWorldMatrix(!0,!1),Mn.multiply(e.parent.matrixWorld)),e.applyMatrix4(Mn),e.removeFromParent(),e.parent=this,this.children.push(e),e.updateWorldMatrix(!1,!0),e.dispatchEvent($l),Mi.child=e,this.dispatchEvent(Mi),Mi.child=null,this}getObjectById(e){return this.getObjectByProperty("id",e)}getObjectByName(e){return this.getObjectByProperty("name",e)}getObjectByProperty(e,t){if(this[e]===t)return this;for(let n=0,s=this.children.length;n<s;n++){let a=this.children[n].getObjectByProperty(e,t);if(a!==void 0)return a}}getObjectsByProperty(e,t,n=[]){this[e]===t&&n.push(this);let s=this.children;for(let r=0,a=s.length;r<a;r++)s[r].getObjectsByProperty(e,t,n);return n}getWorldPosition(e){return this.updateWorldMatrix(!0,!1),e.setFromMatrixPosition(this.matrixWorld)}getWorldQuaternion(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(ji,e,m1),e}getWorldScale(e){return this.updateWorldMatrix(!0,!1),this.matrixWorld.decompose(ji,g1,e),e}getWorldDirection(e){this.updateWorldMatrix(!0,!1);let t=this.matrixWorld.elements;return e.set(t[8],t[9],t[10]).normalize()}raycast(){}intersectsFrustum(){return!0}traverse(e){e(this);let t=this.children;for(let n=0,s=t.length;n<s;n++)t[n].traverse(e)}traverseVisible(e){if(this.visible===!1)return;e(this);let t=this.children;for(let n=0,s=t.length;n<s;n++)t[n].traverseVisible(e)}traverseAncestors(e){let t=this.parent;t!==null&&(e(t),t.traverseAncestors(e))}updateMatrix(){this.matrix.compose(this.position,this.quaternion,this.scale);let e=this.pivot;if(e!==null){let t=e.x,n=e.y,s=e.z,r=this.matrix.elements;r[12]+=t-r[0]*t-r[4]*n-r[8]*s,r[13]+=n-r[1]*t-r[5]*n-r[9]*s,r[14]+=s-r[2]*t-r[6]*n-r[10]*s}this.matrixWorldNeedsUpdate=!0}updateMatrixWorld(e){this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||e)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,e=!0);let t=this.children;for(let n=0,s=t.length;n<s;n++)t[n].updateMatrixWorld(e)}updateWorldMatrix(e,t,n=!1){let s=this.parent;if(e===!0&&s!==null&&s.updateWorldMatrix(!0,!1),this.matrixAutoUpdate&&this.updateMatrix(),(this.matrixWorldNeedsUpdate||n)&&(this.matrixWorldAutoUpdate===!0&&(this.parent===null?this.matrixWorld.copy(this.matrix):this.matrixWorld.multiplyMatrices(this.parent.matrixWorld,this.matrix)),this.matrixWorldNeedsUpdate=!1,n=!0),t===!0){let r=this.children;for(let a=0,o=r.length;a<o;a++)r[a].updateWorldMatrix(!1,!0,n)}}toJSON(e){let t=e===void 0||typeof e=="string",n={};t&&(e={geometries:{},materials:{},textures:{},images:{},shapes:{},skeletons:{},animations:{},nodes:{}},n.metadata={version:4.7,type:"Object",generator:"Object3D.toJSON"});let s={};s.uuid=this.uuid,s.type=this.type,s.name=this.name,s.castShadow=this.castShadow,s.receiveShadow=this.receiveShadow,s.visible=this.visible,s.frustumCulled=this.frustumCulled,s.renderOrder=this.renderOrder,s.static=this.static,s.matrixAutoUpdate=this.matrixAutoUpdate,Object.keys(this.userData).length>0&&(s.userData=this.userData),s.layers=this.layers.mask,s.matrix=this.matrix.toArray(),s.up=this.up.toArray(),this.pivot!==null&&(s.pivot=this.pivot.toArray()),this.morphTargetDictionary!==void 0&&(s.morphTargetDictionary=Object.assign({},this.morphTargetDictionary)),this.morphTargetInfluences!==void 0&&(s.morphTargetInfluences=this.morphTargetInfluences.slice()),this.isInstancedMesh&&(s.type="InstancedMesh",s.count=this.count,s.instanceMatrix=this.instanceMatrix.toJSON(),this.instanceColor!==null&&(s.instanceColor=this.instanceColor.toJSON())),this.isBatchedMesh&&(s.type="BatchedMesh",s.perObjectFrustumCulled=this.perObjectFrustumCulled,s.sortObjects=this.sortObjects,s.drawRanges=this._drawRanges,s.reservedRanges=this._reservedRanges,s.geometryInfo=this._geometryInfo.map(o=>({...o,boundingBox:o.boundingBox?o.boundingBox.toJSON():void 0,boundingSphere:o.boundingSphere?o.boundingSphere.toJSON():void 0})),s.instanceInfo=this._instanceInfo.map(o=>({...o})),s.availableInstanceIds=this._availableInstanceIds.slice(),s.availableGeometryIds=this._availableGeometryIds.slice(),s.nextIndexStart=this._nextIndexStart,s.nextVertexStart=this._nextVertexStart,s.geometryCount=this._geometryCount,s.maxInstanceCount=this._maxInstanceCount,s.maxVertexCount=this._maxVertexCount,s.maxIndexCount=this._maxIndexCount,s.geometryInitialized=this._geometryInitialized,s.matricesTexture=this._matricesTexture.toJSON(e),s.indirectTexture=this._indirectTexture.toJSON(e),this._colorsTexture!==null&&(s.colorsTexture=this._colorsTexture.toJSON(e)),this.boundingSphere!==null&&(s.boundingSphere=this.boundingSphere.toJSON()),this.boundingBox!==null&&(s.boundingBox=this.boundingBox.toJSON()));function r(o,l){return o[l.uuid]===void 0&&(o[l.uuid]=l.toJSON(e)),l.uuid}if(this.isScene)this.background&&(this.background.isColor?s.background=this.background.toJSON():this.background.isTexture&&(s.background=this.background.toJSON(e).uuid)),this.environment&&this.environment.isTexture&&this.environment.isRenderTargetTexture!==!0&&(s.environment=this.environment.toJSON(e).uuid);else if(this.isMesh||this.isLine||this.isPoints){s.geometry=r(e.geometries,this.geometry);let o=this.geometry.parameters;if(o!==void 0&&o.shapes!==void 0){let l=o.shapes;if(Array.isArray(l))for(let c=0,h=l.length;c<h;c++){let g=l[c];r(e.shapes,g)}else r(e.shapes,l)}}if(this.isSkinnedMesh&&(s.bindMode=this.bindMode,s.bindMatrix=this.bindMatrix.toArray(),this.skeleton!==void 0&&(r(e.skeletons,this.skeleton),s.skeleton=this.skeleton.uuid)),this.material!==void 0)if(Array.isArray(this.material)){let o=[];for(let l=0,c=this.material.length;l<c;l++)o.push(r(e.materials,this.material[l]));s.material=o}else s.material=r(e.materials,this.material);if(this.children.length>0){s.children=[];for(let o=0;o<this.children.length;o++)s.children.push(this.children[o].toJSON(e).object)}if(this.animations.length>0){s.animations=[];for(let o=0;o<this.animations.length;o++){let l=this.animations[o];s.animations.push(r(e.animations,l))}}if(t){let o=a(e.geometries),l=a(e.materials),c=a(e.textures),h=a(e.images),g=a(e.shapes),d=a(e.skeletons),m=a(e.animations),_=a(e.nodes);o.length>0&&(n.geometries=o),l.length>0&&(n.materials=l),c.length>0&&(n.textures=c),h.length>0&&(n.images=h),g.length>0&&(n.shapes=g),d.length>0&&(n.skeletons=d),m.length>0&&(n.animations=m),_.length>0&&(n.nodes=_)}return n.object=s,n;function a(o){let l=[];for(let c in o){let h=o[c];delete h.metadata,l.push(h)}return l}}clone(e){return new this.constructor().copy(this,e)}copy(e,t=!0){if(this.name=e.name,this.up.copy(e.up),this.position.copy(e.position),this.rotation.order=e.rotation.order,this.quaternion.copy(e.quaternion),this.scale.copy(e.scale),this.pivot=e.pivot!==null?e.pivot.clone():null,this.matrix.copy(e.matrix),this.matrixWorld.copy(e.matrixWorld),this.matrixAutoUpdate=e.matrixAutoUpdate,this.matrixWorldAutoUpdate=e.matrixWorldAutoUpdate,this.matrixWorldNeedsUpdate=e.matrixWorldNeedsUpdate,this.layers.mask=e.layers.mask,this.visible=e.visible,this.castShadow=e.castShadow,this.receiveShadow=e.receiveShadow,this.frustumCulled=e.frustumCulled,this.renderOrder=e.renderOrder,this.static=e.static,this.animations=e.animations.slice(),this.userData=JSON.parse(JSON.stringify(e.userData)),t===!0)for(let n=0;n<e.children.length;n++){let s=e.children[n];this.add(s.clone())}return this}dispose(){this.dispatchEvent({type:"dispose"})}};Pt.DEFAULT_UP=new U(0,1,0);Pt.DEFAULT_MATRIX_AUTO_UPDATE=!0;Pt.DEFAULT_MATRIX_WORLD_AUTO_UPDATE=!0;var wn=class extends Pt{constructor(){super(),this.isGroup=!0,this.type="Group"}},x1={type:"move"},zi=class{constructor(){this._targetRay=null,this._grip=null,this._hand=null}getHandSpace(){return this._hand===null&&(this._hand=new wn,this._hand.matrixAutoUpdate=!1,this._hand.visible=!1,this._hand.joints={},this._hand.inputState={pinching:!1}),this._hand}getTargetRaySpace(){return this._targetRay===null&&(this._targetRay=new wn,this._targetRay.matrixAutoUpdate=!1,this._targetRay.visible=!1,this._targetRay.hasLinearVelocity=!1,this._targetRay.linearVelocity=new U,this._targetRay.hasAngularVelocity=!1,this._targetRay.angularVelocity=new U),this._targetRay}getGripSpace(){return this._grip===null&&(this._grip=new wn,this._grip.matrixAutoUpdate=!1,this._grip.visible=!1,this._grip.hasLinearVelocity=!1,this._grip.linearVelocity=new U,this._grip.hasAngularVelocity=!1,this._grip.angularVelocity=new U,this._grip.eventsEnabled=!1),this._grip}dispatchEvent(e){return this._targetRay!==null&&this._targetRay.dispatchEvent(e),this._grip!==null&&this._grip.dispatchEvent(e),this._hand!==null&&this._hand.dispatchEvent(e),this}connect(e){if(e&&e.hand){let t=this._hand;if(t)for(let n of e.hand.values())this._getHandJoint(t,n)}return this.dispatchEvent({type:"connected",data:e}),this}disconnect(e){return this.dispatchEvent({type:"disconnected",data:e}),this._targetRay!==null&&(this._targetRay.visible=!1),this._grip!==null&&(this._grip.visible=!1),this._hand!==null&&(this._hand.visible=!1),this}update(e,t,n){let s=null,r=null,a=null,o=this._targetRay,l=this._grip,c=this._hand;if(e&&t.session.visibilityState!=="visible-blurred"){if(c&&e.hand){a=!0;for(let S of e.hand.values()){let p=t.getJointPose(S,n),u=this._getHandJoint(c,S);p!==null&&(u.matrix.fromArray(p.transform.matrix),u.matrix.decompose(u.position,u.quaternion,u.scale),u.matrixWorldNeedsUpdate=!0,u.jointRadius=p.radius),u.visible=p!==null}let h=c.joints["index-finger-tip"],g=c.joints["thumb-tip"],d=h.position.distanceTo(g.position),m=.02,_=.005;c.inputState.pinching&&d>m+_?(c.inputState.pinching=!1,this.dispatchEvent({type:"pinchend",handedness:e.handedness,target:this})):!c.inputState.pinching&&d<=m-_&&(c.inputState.pinching=!0,this.dispatchEvent({type:"pinchstart",handedness:e.handedness,target:this}))}else l!==null&&e.gripSpace&&(r=t.getPose(e.gripSpace,n),r!==null&&(l.matrix.fromArray(r.transform.matrix),l.matrix.decompose(l.position,l.quaternion,l.scale),l.matrixWorldNeedsUpdate=!0,r.linearVelocity?(l.hasLinearVelocity=!0,l.linearVelocity.copy(r.linearVelocity)):l.hasLinearVelocity=!1,r.angularVelocity?(l.hasAngularVelocity=!0,l.angularVelocity.copy(r.angularVelocity)):l.hasAngularVelocity=!1,l.eventsEnabled&&l.dispatchEvent({type:"gripUpdated",data:e,target:this})));o!==null&&(s=t.getPose(e.targetRaySpace,n),s===null&&r!==null&&(s=r),s!==null&&(o.matrix.fromArray(s.transform.matrix),o.matrix.decompose(o.position,o.quaternion,o.scale),o.matrixWorldNeedsUpdate=!0,s.linearVelocity?(o.hasLinearVelocity=!0,o.linearVelocity.copy(s.linearVelocity)):o.hasLinearVelocity=!1,s.angularVelocity?(o.hasAngularVelocity=!0,o.angularVelocity.copy(s.angularVelocity)):o.hasAngularVelocity=!1,this.dispatchEvent(x1)))}return o!==null&&(o.visible=s!==null),l!==null&&(l.visible=r!==null),c!==null&&(c.visible=a!==null),this}_getHandJoint(e,t){if(e.joints[t.jointName]===void 0){let n=new wn;n.matrixAutoUpdate=!1,n.visible=!1,e.joints[t.jointName]=n,e.add(n)}return e.joints[t.jointName]}},eh={aliceblue:15792383,antiquewhite:16444375,aqua:65535,aquamarine:8388564,azure:15794175,beige:16119260,bisque:16770244,black:0,blanchedalmond:16772045,blue:255,blueviolet:9055202,brown:10824234,burlywood:14596231,cadetblue:6266528,chartreuse:8388352,chocolate:13789470,coral:16744272,cornflowerblue:6591981,cornsilk:16775388,crimson:14423100,cyan:65535,darkblue:139,darkcyan:35723,darkgoldenrod:12092939,darkgray:11119017,darkgreen:25600,darkgrey:11119017,darkkhaki:12433259,darkmagenta:9109643,darkolivegreen:5597999,darkorange:16747520,darkorchid:10040012,darkred:9109504,darksalmon:15308410,darkseagreen:9419919,darkslateblue:4734347,darkslategray:3100495,darkslategrey:3100495,darkturquoise:52945,darkviolet:9699539,deeppink:16716947,deepskyblue:49151,dimgray:6908265,dimgrey:6908265,dodgerblue:2003199,firebrick:11674146,floralwhite:16775920,forestgreen:2263842,fuchsia:16711935,gainsboro:14474460,ghostwhite:16316671,gold:16766720,goldenrod:14329120,gray:8421504,green:32768,greenyellow:11403055,grey:8421504,honeydew:15794160,hotpink:16738740,indianred:13458524,indigo:4915330,ivory:16777200,khaki:15787660,lavender:15132410,lavenderblush:16773365,lawngreen:8190976,lemonchiffon:16775885,lightblue:11393254,lightcoral:15761536,lightcyan:14745599,lightgoldenrodyellow:16448210,lightgray:13882323,lightgreen:9498256,lightgrey:13882323,lightpink:16758465,lightsalmon:16752762,lightseagreen:2142890,lightskyblue:8900346,lightslategray:7833753,lightslategrey:7833753,lightsteelblue:11584734,lightyellow:16777184,lime:65280,limegreen:3329330,linen:16445670,magenta:16711935,maroon:8388608,mediumaquamarine:6737322,mediumblue:205,mediumorchid:12211667,mediumpurple:9662683,mediumseagreen:3978097,mediumslateblue:8087790,mediumspringgreen:64154,mediumturquoise:4772300,mediumvioletred:13047173,midnightblue:1644912,mintcream:16121850,mistyrose:16770273,moccasin:16770229,navajowhite:16768685,navy:128,oldlace:16643558,olive:8421376,olivedrab:7048739,orange:16753920,orangered:16729344,orchid:14315734,palegoldenrod:15657130,palegreen:10025880,paleturquoise:11529966,palevioletred:14381203,papayawhip:16773077,peachpuff:16767673,peru:13468991,pink:16761035,plum:14524637,powderblue:11591910,purple:8388736,rebeccapurple:6697881,red:16711680,rosybrown:12357519,royalblue:4286945,saddlebrown:9127187,salmon:16416882,sandybrown:16032864,seagreen:3050327,seashell:16774638,sienna:10506797,silver:12632256,skyblue:8900331,slateblue:6970061,slategray:7372944,slategrey:7372944,snow:16775930,springgreen:65407,steelblue:4620980,tan:13808780,teal:32896,thistle:14204888,tomato:16737095,turquoise:4251856,violet:15631086,wheat:16113331,white:16777215,whitesmoke:16119285,yellow:16776960,yellowgreen:10145074},zn={h:0,s:0,l:0},Ys={h:0,s:0,l:0};function Qa(i,e,t){return t<0&&(t+=1),t>1&&(t-=1),t<1/6?i+(e-i)*6*t:t<1/2?e:t<2/3?i+(e-i)*6*(2/3-t):i}var Be=class{constructor(e,t,n){return this.isColor=!0,this.r=1,this.g=1,this.b=1,this.set(e,t,n)}set(e,t,n){if(t===void 0&&n===void 0){let s=e;s&&s.isColor?this.copy(s):typeof s=="number"?this.setHex(s):typeof s=="string"&&this.setStyle(s)}else this.setRGB(e,t,n);return this}setScalar(e){return this.r=e,this.g=e,this.b=e,this}setHex(e,t=Nt){return e=Math.floor(e),this.r=(e>>16&255)/255,this.g=(e>>8&255)/255,this.b=(e&255)/255,We.colorSpaceToWorking(this,t),this}setRGB(e,t,n,s=We.workingColorSpace){return this.r=e,this.g=t,this.b=n,We.colorSpaceToWorking(this,s),this}setHSL(e,t,n,s=We.workingColorSpace){if(e=$o(e,1),t=ke(t,0,1),n=ke(n,0,1),t===0)this.r=this.g=this.b=n;else{let r=n<=.5?n*(1+t):n+t-n*t,a=2*n-r;this.r=Qa(a,r,e+1/3),this.g=Qa(a,r,e),this.b=Qa(a,r,e-1/3)}return We.colorSpaceToWorking(this,s),this}setStyle(e,t=Nt){function n(r){r!==void 0&&parseFloat(r)<1&&Te("Color: Alpha component of "+e+" will be ignored.")}let s;if(s=/^(\w+)\(([^\)]*)\)/.exec(e)){let r,a=s[1],o=s[2];switch(a){case"rgb":case"rgba":if(r=/^\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(255,parseInt(r[1],10))/255,Math.min(255,parseInt(r[2],10))/255,Math.min(255,parseInt(r[3],10))/255,t);if(r=/^\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setRGB(Math.min(100,parseFloat(r[1]))/100,Math.min(100,parseFloat(r[2]))/100,Math.min(100,parseFloat(r[3]))/100,t);break;case"hsl":case"hsla":if(r=/^\s*([+-]?(?:\d+(?:\.\d+)?|\.\d+))\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*,\s*(\d+(?:\.\d+)?|\.\d+)\%\s*(?:,\s*(\d+(?:\.\d+)?|\.\d+)\s*)?$/.exec(o))return n(r[4]),this.setHSL(parseFloat(r[1])/360,parseFloat(r[2])/100,parseFloat(r[3])/100,t);break;default:Te("Color: Unknown color model "+e)}}else if(s=/^\#([A-Fa-f\d]+)$/.exec(e)){let r=s[1],a=r.length;if(a===3)return this.setRGB(parseInt(r.charAt(0),16)/15,parseInt(r.charAt(1),16)/15,parseInt(r.charAt(2),16)/15,t);if(a===6)return this.setHex(parseInt(r,16),t);Te("Color: Invalid hex color "+e)}else if(e&&e.length>0)return this.setColorName(e,t);return this}setColorName(e,t=Nt){let n=eh[e.toLowerCase()];return n!==void 0?this.setHex(n,t):Te("Color: Unknown color "+e),this}clone(){return new this.constructor(this.r,this.g,this.b)}copy(e){return this.r=e.r,this.g=e.g,this.b=e.b,this}copySRGBToLinear(e){return this.r=Rn(e.r),this.g=Rn(e.g),this.b=Rn(e.b),this}copyLinearToSRGB(e){return this.r=Li(e.r),this.g=Li(e.g),this.b=Li(e.b),this}convertSRGBToLinear(){return this.copySRGBToLinear(this),this}convertLinearToSRGB(){return this.copyLinearToSRGB(this),this}getHex(e=Nt){return We.workingToColorSpace(Ct.copy(this),e),Math.round(ke(Ct.r*255,0,255))*65536+Math.round(ke(Ct.g*255,0,255))*256+Math.round(ke(Ct.b*255,0,255))}getHexString(e=Nt){return("000000"+this.getHex(e).toString(16)).slice(-6)}getHSL(e,t=We.workingColorSpace){We.workingToColorSpace(Ct.copy(this),t);let n=Ct.r,s=Ct.g,r=Ct.b,a=Math.max(n,s,r),o=Math.min(n,s,r),l,c,h=(o+a)/2;if(o===a)l=0,c=0;else{let g=a-o;switch(c=h<=.5?g/(a+o):g/(2-a-o),a){case n:l=(s-r)/g+(s<r?6:0);break;case s:l=(r-n)/g+2;break;case r:l=(n-s)/g+4;break}l/=6}return e.h=l,e.s=c,e.l=h,e}getRGB(e,t=We.workingColorSpace){return We.workingToColorSpace(Ct.copy(this),t),e.r=Ct.r,e.g=Ct.g,e.b=Ct.b,e}getStyle(e=Nt){We.workingToColorSpace(Ct.copy(this),e);let t=Ct.r,n=Ct.g,s=Ct.b;return e!==Nt?`color(${e} ${t.toFixed(3)} ${n.toFixed(3)} ${s.toFixed(3)})`:`rgb(${Math.round(t*255)},${Math.round(n*255)},${Math.round(s*255)})`}offsetHSL(e,t,n){return this.getHSL(zn),this.setHSL(zn.h+e,zn.s+t,zn.l+n)}add(e){return this.r+=e.r,this.g+=e.g,this.b+=e.b,this}addColors(e,t){return this.r=e.r+t.r,this.g=e.g+t.g,this.b=e.b+t.b,this}addScalar(e){return this.r+=e,this.g+=e,this.b+=e,this}sub(e){return this.r=Math.max(0,this.r-e.r),this.g=Math.max(0,this.g-e.g),this.b=Math.max(0,this.b-e.b),this}multiply(e){return this.r*=e.r,this.g*=e.g,this.b*=e.b,this}multiplyScalar(e){return this.r*=e,this.g*=e,this.b*=e,this}lerp(e,t){return this.r+=(e.r-this.r)*t,this.g+=(e.g-this.g)*t,this.b+=(e.b-this.b)*t,this}lerpColors(e,t,n){return this.r=e.r+(t.r-e.r)*n,this.g=e.g+(t.g-e.g)*n,this.b=e.b+(t.b-e.b)*n,this}lerpHSL(e,t){this.getHSL(zn),e.getHSL(Ys);let n=rs(zn.h,Ys.h,t),s=rs(zn.s,Ys.s,t),r=rs(zn.l,Ys.l,t);return this.setHSL(n,s,r),this}setFromVector3(e){return this.r=e.x,this.g=e.y,this.b=e.z,this}applyMatrix3(e){let t=this.r,n=this.g,s=this.b,r=e.elements;return this.r=r[0]*t+r[3]*n+r[6]*s,this.g=r[1]*t+r[4]*n+r[7]*s,this.b=r[2]*t+r[5]*n+r[8]*s,this}equals(e){return e.r===this.r&&e.g===this.g&&e.b===this.b}fromArray(e,t=0){return this.r=e[t],this.g=e[t+1],this.b=e[t+2],this}toArray(e=[],t=0){return e[t]=this.r,e[t+1]=this.g,e[t+2]=this.b,e}fromBufferAttribute(e,t){return this.r=e.getX(t),this.g=e.getY(t),this.b=e.getZ(t),this}toJSON(){return this.getHex()}*[Symbol.iterator](){yield this.r,yield this.g,yield this.b}},Ct=new Be;Be.NAMES=eh;var us=class extends Pt{constructor(){super(),this.isScene=!0,this.type="Scene",this.background=null,this.environment=null,this.fog=null,this.backgroundBlurriness=0,this.backgroundIntensity=1,this.backgroundRotation=new Pn,this.environmentIntensity=1,this.environmentRotation=new Pn,this.overrideMaterial=null,typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}copy(e,t){return super.copy(e,t),this.background=e.background!==null?e.background.clone():null,this.environment=e.environment!==null?e.environment.clone():null,this.fog=e.fog!==null?e.fog.clone():null,this.backgroundBlurriness=e.backgroundBlurriness,this.backgroundIntensity=e.backgroundIntensity,this.backgroundRotation.copy(e.backgroundRotation),this.environmentIntensity=e.environmentIntensity,this.environmentRotation.copy(e.environmentRotation),this.overrideMaterial=e.overrideMaterial!==null?e.overrideMaterial.clone():null,this.matrixAutoUpdate=e.matrixAutoUpdate,this}toJSON(e){let t=super.toJSON(e);return this.fog!==null&&(t.object.fog=this.fog.toJSON()),t.object.backgroundBlurriness=this.backgroundBlurriness,t.object.backgroundIntensity=this.backgroundIntensity,t.object.backgroundRotation=this.backgroundRotation.toArray(),t.object.environmentIntensity=this.environmentIntensity,t.object.environmentRotation=this.environmentRotation.toArray(),t}},an=new U,bn=new U,eo=new U,En=new U,bi=new U,Ei=new U,Kl=new U,to=new U,no=new U,io=new U,so=new at,ro=new at,ao=new at,Hn=class i{constructor(e=new U,t=new U,n=new U){this.a=e,this.b=t,this.c=n}static getNormal(e,t,n,s){s.subVectors(n,t),an.subVectors(e,t),s.cross(an);let r=s.lengthSq();return r>0?s.multiplyScalar(1/Math.sqrt(r)):s.set(0,0,0)}static getBarycoord(e,t,n,s,r){an.subVectors(s,t),bn.subVectors(n,t),eo.subVectors(e,t);let a=an.dot(an),o=an.dot(bn),l=an.dot(eo),c=bn.dot(bn),h=bn.dot(eo),g=a*c-o*o;if(g===0)return r.set(0,0,0),null;let d=1/g,m=(c*l-o*h)*d,_=(a*h-o*l)*d;return r.set(1-m-_,_,m)}static containsPoint(e,t,n,s){return this.getBarycoord(e,t,n,s,En)===null?!1:En.x>=0&&En.y>=0&&En.x+En.y<=1}static getInterpolation(e,t,n,s,r,a,o,l){return this.getBarycoord(e,t,n,s,En)===null?(l.x=0,l.y=0,"z"in l&&(l.z=0),"w"in l&&(l.w=0),null):(l.setScalar(0),l.addScaledVector(r,En.x),l.addScaledVector(a,En.y),l.addScaledVector(o,En.z),l)}static getInterpolatedAttribute(e,t,n,s,r,a){return so.setScalar(0),ro.setScalar(0),ao.setScalar(0),so.fromBufferAttribute(e,t),ro.fromBufferAttribute(e,n),ao.fromBufferAttribute(e,s),a.setScalar(0),a.addScaledVector(so,r.x),a.addScaledVector(ro,r.y),a.addScaledVector(ao,r.z),a}static isFrontFacing(e,t,n,s){return an.subVectors(n,t),bn.subVectors(e,t),an.cross(bn).dot(s)<0}set(e,t,n){return this.a.copy(e),this.b.copy(t),this.c.copy(n),this}setFromPointsAndIndices(e,t,n,s){return this.a.copy(e[t]),this.b.copy(e[n]),this.c.copy(e[s]),this}setFromAttributeAndIndices(e,t,n,s){return this.a.fromBufferAttribute(e,t),this.b.fromBufferAttribute(e,n),this.c.fromBufferAttribute(e,s),this}clone(){return new this.constructor().copy(this)}copy(e){return this.a.copy(e.a),this.b.copy(e.b),this.c.copy(e.c),this}getArea(){return an.subVectors(this.c,this.b),bn.subVectors(this.a,this.b),an.cross(bn).length()*.5}getMidpoint(e){return e.addVectors(this.a,this.b).add(this.c).multiplyScalar(1/3)}getNormal(e){return i.getNormal(this.a,this.b,this.c,e)}getPlane(e){return e.setFromCoplanarPoints(this.a,this.b,this.c)}getBarycoord(e,t){return i.getBarycoord(e,this.a,this.b,this.c,t)}getInterpolation(e,t,n,s,r){return i.getInterpolation(e,this.a,this.b,this.c,t,n,s,r)}containsPoint(e){return i.containsPoint(e,this.a,this.b,this.c)}isFrontFacing(e){return i.isFrontFacing(this.a,this.b,this.c,e)}intersectsBox(e){return e.intersectsTriangle(this)}closestPointToPoint(e,t){let n=this.a,s=this.b,r=this.c,a,o;bi.subVectors(s,n),Ei.subVectors(r,n),to.subVectors(e,n);let l=bi.dot(to),c=Ei.dot(to);if(l<=0&&c<=0)return t.copy(n);no.subVectors(e,s);let h=bi.dot(no),g=Ei.dot(no);if(h>=0&&g<=h)return t.copy(s);let d=l*g-h*c;if(d<=0&&l>=0&&h<=0&&l-h>0)return a=l/(l-h),t.copy(n).addScaledVector(bi,a);io.subVectors(e,r);let m=bi.dot(io),_=Ei.dot(io);if(_>=0&&m<=_)return t.copy(r);let S=m*c-l*_;if(S<=0&&c>=0&&_<=0)return o=c/(c-_),t.copy(n).addScaledVector(Ei,o);let p=h*_-m*g;if(p<=0&&g-h>=0&&m-_>=0)return Kl.subVectors(r,s),o=(g-h)/(g-h+(m-_)),t.copy(s).addScaledVector(Kl,o);let u=1/(p+S+d);return a=S*u,o=d*u,t.copy(n).addScaledVector(bi,a).addScaledVector(Ei,o)}equals(e){return e.a.equals(this.a)&&e.b.equals(this.b)&&e.c.equals(this.c)}},Wn=class{constructor(e=new U(1/0,1/0,1/0),t=new U(-1/0,-1/0,-1/0)){this.isBox3=!0,this.min=e,this.max=t}set(e,t){return this.min.copy(e),this.max.copy(t),this}setFromArray(e){this.makeEmpty();for(let t=0,n=e.length;t<n;t+=3)this.expandByPoint(on.fromArray(e,t));return this}setFromBufferAttribute(e){this.makeEmpty();for(let t=0,n=e.count;t<n;t++)this.expandByPoint(on.fromBufferAttribute(e,t));return this}setFromPoints(e){this.makeEmpty();for(let t=0,n=e.length;t<n;t++)this.expandByPoint(e[t]);return this}setFromCenterAndSize(e,t){let n=on.copy(t).multiplyScalar(.5);return this.min.copy(e).sub(n),this.max.copy(e).add(n),this}setFromObject(e,t=!1){return this.makeEmpty(),this.expandByObject(e,t)}clone(){return new this.constructor().copy(this)}copy(e){return this.min.copy(e.min),this.max.copy(e.max),this}makeEmpty(){return this.min.x=this.min.y=this.min.z=1/0,this.max.x=this.max.y=this.max.z=-1/0,this}isEmpty(){return this.max.x<this.min.x||this.max.y<this.min.y||this.max.z<this.min.z}getCenter(e){return this.isEmpty()?e.set(0,0,0):e.addVectors(this.min,this.max).multiplyScalar(.5)}getSize(e){return this.isEmpty()?e.set(0,0,0):e.subVectors(this.max,this.min)}expandByPoint(e){return this.min.min(e),this.max.max(e),this}expandByVector(e){return this.min.sub(e),this.max.add(e),this}expandByScalar(e){return this.min.addScalar(-e),this.max.addScalar(e),this}expandByObject(e,t=!1){e.updateWorldMatrix(!1,!1);let n=e.geometry;if(n!==void 0){let r=n.getAttribute("position");if(t===!0&&r!==void 0&&e.isInstancedMesh!==!0&&e.isBatchedMesh!==!0)for(let a=0,o=r.count;a<o;a++)e.isMesh===!0?e.getVertexPosition(a,on):on.fromBufferAttribute(r,a),on.applyMatrix4(e.matrixWorld),this.expandByPoint(on);else e.boundingBox!==void 0?(e.boundingBox===null&&e.computeBoundingBox(),Zs.copy(e.boundingBox)):(n.boundingBox===null&&n.computeBoundingBox(),Zs.copy(n.boundingBox)),Zs.applyMatrix4(e.matrixWorld),this.union(Zs)}let s=e.children;for(let r=0,a=s.length;r<a;r++)this.expandByObject(s[r],t);return this}containsPoint(e){return e.x>=this.min.x&&e.x<=this.max.x&&e.y>=this.min.y&&e.y<=this.max.y&&e.z>=this.min.z&&e.z<=this.max.z}containsBox(e){return this.min.x<=e.min.x&&e.max.x<=this.max.x&&this.min.y<=e.min.y&&e.max.y<=this.max.y&&this.min.z<=e.min.z&&e.max.z<=this.max.z}getParameter(e,t){return t.set((e.x-this.min.x)/(this.max.x-this.min.x),(e.y-this.min.y)/(this.max.y-this.min.y),(e.z-this.min.z)/(this.max.z-this.min.z))}intersectsBox(e){return e.max.x>=this.min.x&&e.min.x<=this.max.x&&e.max.y>=this.min.y&&e.min.y<=this.max.y&&e.max.z>=this.min.z&&e.min.z<=this.max.z}intersectsSphere(e){return this.clampPoint(e.center,on),on.distanceToSquared(e.center)<=e.radius*e.radius}intersectsPlane(e){let t,n;return e.normal.x>0?(t=e.normal.x*this.min.x,n=e.normal.x*this.max.x):(t=e.normal.x*this.max.x,n=e.normal.x*this.min.x),e.normal.y>0?(t+=e.normal.y*this.min.y,n+=e.normal.y*this.max.y):(t+=e.normal.y*this.max.y,n+=e.normal.y*this.min.y),e.normal.z>0?(t+=e.normal.z*this.min.z,n+=e.normal.z*this.max.z):(t+=e.normal.z*this.max.z,n+=e.normal.z*this.min.z),t<=-e.constant&&n>=-e.constant}intersectsTriangle(e){if(this.isEmpty())return!1;this.getCenter(Qi),Js.subVectors(this.max,Qi),Ti.subVectors(e.a,Qi),Ai.subVectors(e.b,Qi),wi.subVectors(e.c,Qi),kn.subVectors(Ai,Ti),Gn.subVectors(wi,Ai),ii.subVectors(Ti,wi);let t=[0,-kn.z,kn.y,0,-Gn.z,Gn.y,0,-ii.z,ii.y,kn.z,0,-kn.x,Gn.z,0,-Gn.x,ii.z,0,-ii.x,-kn.y,kn.x,0,-Gn.y,Gn.x,0,-ii.y,ii.x,0];return!oo(t,Ti,Ai,wi,Js)||(t=[1,0,0,0,1,0,0,0,1],!oo(t,Ti,Ai,wi,Js))?!1:($s.crossVectors(kn,Gn),t=[$s.x,$s.y,$s.z],oo(t,Ti,Ai,wi,Js))}clampPoint(e,t){return t.copy(e).clamp(this.min,this.max)}distanceToPoint(e){return this.clampPoint(e,on).distanceTo(e)}getBoundingSphere(e){return this.isEmpty()?e.makeEmpty():(this.getCenter(e.center),e.radius=this.getSize(on).length()*.5),e}intersect(e){return this.min.max(e.min),this.max.min(e.max),this.isEmpty()&&this.makeEmpty(),this}union(e){return this.min.min(e.min),this.max.max(e.max),this}applyMatrix4(e){return this.isEmpty()?this:(Tn[0].set(this.min.x,this.min.y,this.min.z).applyMatrix4(e),Tn[1].set(this.min.x,this.min.y,this.max.z).applyMatrix4(e),Tn[2].set(this.min.x,this.max.y,this.min.z).applyMatrix4(e),Tn[3].set(this.min.x,this.max.y,this.max.z).applyMatrix4(e),Tn[4].set(this.max.x,this.min.y,this.min.z).applyMatrix4(e),Tn[5].set(this.max.x,this.min.y,this.max.z).applyMatrix4(e),Tn[6].set(this.max.x,this.max.y,this.min.z).applyMatrix4(e),Tn[7].set(this.max.x,this.max.y,this.max.z).applyMatrix4(e),this.setFromPoints(Tn),this)}translate(e){return this.min.add(e),this.max.add(e),this}equals(e){return e.min.equals(this.min)&&e.max.equals(this.max)}toJSON(){return{min:this.min.toArray(),max:this.max.toArray()}}fromJSON(e){return this.min.fromArray(e.min),this.max.fromArray(e.max),this}},Tn=[new U,new U,new U,new U,new U,new U,new U,new U],on=new U,Zs=new Wn,Ti=new U,Ai=new U,wi=new U,kn=new U,Gn=new U,ii=new U,Qi=new U,Js=new U,$s=new U,si=new U;function oo(i,e,t,n,s){for(let r=0,a=i.length-3;r<=a;r+=3){si.fromArray(i,r);let o=s.x*Math.abs(si.x)+s.y*Math.abs(si.y)+s.z*Math.abs(si.z),l=e.dot(si),c=t.dot(si),h=n.dot(si);if(Math.max(-Math.max(l,c,h),Math.min(l,c,h))>o)return!1}return!0}var dt=new U,Ks=new Re,y1=0,_n=class extends ln{constructor(e,t,n=!1){if(super(),Array.isArray(e))throw new TypeError("THREE.BufferAttribute: array should be a Typed Array.");this.isBufferAttribute=!0,Object.defineProperty(this,"id",{value:y1++}),this.name="",this.array=e,this.itemSize=t,this.count=e!==void 0?e.length/t:0,this.normalized=n,this.usage=Yc,this.updateRanges=[],this.gpuType=hn,this.version=0,this._normalizationScale=e!==void 0?jo(e):void 0}onUploadCallback(){}set needsUpdate(e){e===!0&&this.version++}setUsage(e){return this.usage=e,this}addUpdateRange(e,t){this.updateRanges.push({start:e,count:t})}clearUpdateRanges(){this.updateRanges.length=0}copy(e){return this.name=e.name,this.array=new e.array.constructor(e.array),this.itemSize=e.itemSize,this.count=e.count,this.normalized=e.normalized,this.usage=e.usage,this.gpuType=e.gpuType,this._normalizationScale=e._normalizationScale,this}copyAt(e,t,n){e*=this.itemSize,n*=t.itemSize;for(let s=0,r=this.itemSize;s<r;s++)this.array[e+s]=t.array[n+s];return this}copyArray(e){return this.array.set(e),this}applyMatrix3(e){if(this.itemSize===2)for(let t=0,n=this.count;t<n;t++)Ks.fromBufferAttribute(this,t),Ks.applyMatrix3(e),this.setXY(t,Ks.x,Ks.y);else if(this.itemSize===3)for(let t=0,n=this.count;t<n;t++)dt.fromBufferAttribute(this,t),dt.applyMatrix3(e),this.setXYZ(t,dt.x,dt.y,dt.z);return this}applyMatrix4(e){for(let t=0,n=this.count;t<n;t++)dt.fromBufferAttribute(this,t),dt.applyMatrix4(e),this.setXYZ(t,dt.x,dt.y,dt.z);return this}applyNormalMatrix(e){for(let t=0,n=this.count;t<n;t++)dt.fromBufferAttribute(this,t),dt.applyNormalMatrix(e),this.setXYZ(t,dt.x,dt.y,dt.z);return this}transformDirection(e){for(let t=0,n=this.count;t<n;t++)dt.fromBufferAttribute(this,t),dt.transformDirection(e),this.setXYZ(t,dt.x,dt.y,dt.z);return this}set(e,t=0){return this.array.set(e,t),this}getComponent(e,t){let n=this.array[e*this.itemSize+t];return this.normalized&&(n=this._denormalize(n)),n}setComponent(e,t,n){return this.normalized&&(n=this._normalize(n)),this.array[e*this.itemSize+t]=n,this}getX(e){let t=this.array[e*this.itemSize];return this.normalized&&(t=this._denormalize(t)),t}setX(e,t){return this.normalized&&(t=this._normalize(t)),this.array[e*this.itemSize]=t,this}getY(e){let t=this.array[e*this.itemSize+1];return this.normalized&&(t=this._denormalize(t)),t}setY(e,t){return this.normalized&&(t=this._normalize(t)),this.array[e*this.itemSize+1]=t,this}getZ(e){let t=this.array[e*this.itemSize+2];return this.normalized&&(t=this._denormalize(t)),t}setZ(e,t){return this.normalized&&(t=this._normalize(t)),this.array[e*this.itemSize+2]=t,this}getW(e){let t=this.array[e*this.itemSize+3];return this.normalized&&(t=this._denormalize(t)),t}setW(e,t){return this.normalized&&(t=this._normalize(t)),this.array[e*this.itemSize+3]=t,this}setXY(e,t,n){return e*=this.itemSize,this.normalized&&(t=this._normalize(t),n=this._normalize(n)),this.array[e+0]=t,this.array[e+1]=n,this}setXYZ(e,t,n,s){return e*=this.itemSize,this.normalized&&(t=this._normalize(t),n=this._normalize(n),s=this._normalize(s)),this.array[e+0]=t,this.array[e+1]=n,this.array[e+2]=s,this}setXYZW(e,t,n,s,r){return e*=this.itemSize,this.normalized&&(t=this._normalize(t),n=this._normalize(n),s=this._normalize(s),r=this._normalize(r)),this.array[e+0]=t,this.array[e+1]=n,this.array[e+2]=s,this.array[e+3]=r,this}onUpload(e){return this.onUploadCallback=e,this}clone(){return new this.constructor(this.array,this.itemSize).copy(this)}toJSON(){let e={itemSize:this.itemSize,type:this.array.constructor.name,array:Array.from(this.array),normalized:this.normalized};return e.name=this.name,e.usage=this.usage,e.gpuType=this.gpuType,e}dispose(){this.dispatchEvent({type:"dispose"})}_denormalize(e){let t=this._normalizationScale;return t!==void 0?Math.max(e/t,-1):jc(e,this.array)}_normalize(e){let t=this._normalizationScale;return t!==void 0?Math.round(e*t):Qc(e,this.array)}};var ds=class extends _n{constructor(e,t,n){super(new Uint16Array(e),t,n)}};var fs=class extends _n{constructor(e,t,n){super(new Uint32Array(e),t,n)}};var ct=class extends _n{constructor(e,t,n){super(new Float32Array(e),t,n)}},v1=new Wn,es=new U,lo=new U,oi=class{constructor(e=new U,t=-1){this.isSphere=!0,this.center=e,this.radius=t}set(e,t){return this.center.copy(e),this.radius=t,this}setFromPoints(e,t){let n=this.center;t!==void 0?n.copy(t):v1.setFromPoints(e).getCenter(n);let s=0;for(let r=0,a=e.length;r<a;r++)s=Math.max(s,n.distanceToSquared(e[r]));return this.radius=Math.sqrt(s),this}copy(e){return this.center.copy(e.center),this.radius=e.radius,this}isEmpty(){return this.radius<0}makeEmpty(){return this.center.set(0,0,0),this.radius=-1,this}containsPoint(e){return e.distanceToSquared(this.center)<=this.radius*this.radius}distanceToPoint(e){return e.distanceTo(this.center)-this.radius}intersectsSphere(e){let t=this.radius+e.radius;return e.center.distanceToSquared(this.center)<=t*t}intersectsBox(e){return e.intersectsSphere(this)}intersectsPlane(e){return Math.abs(e.distanceToPoint(this.center))<=this.radius}clampPoint(e,t){let n=this.center.distanceToSquared(e);return t.copy(e),n>this.radius*this.radius&&(t.sub(this.center).normalize(),t.multiplyScalar(this.radius).add(this.center)),t}getBoundingBox(e){return this.isEmpty()?(e.makeEmpty(),e):(e.set(this.center,this.center),e.expandByScalar(this.radius),e)}applyMatrix4(e){return this.center.applyMatrix4(e),this.radius=this.radius*e.getMaxScaleOnAxis(),this}translate(e){return this.center.add(e),this}expandByPoint(e){if(this.isEmpty())return this.center.copy(e),this.radius=0,this;es.subVectors(e,this.center);let t=es.lengthSq();if(t>this.radius*this.radius){let n=Math.sqrt(t),s=(n-this.radius)*.5;this.center.addScaledVector(es,s/n),this.radius+=s}return this}union(e){return e.isEmpty()?this:this.isEmpty()?(this.copy(e),this):(this.center.equals(e.center)===!0?this.radius=Math.max(this.radius,e.radius):(lo.subVectors(e.center,this.center).setLength(e.radius),this.expandByPoint(es.copy(e.center).add(lo)),this.expandByPoint(es.copy(e.center).sub(lo))),this)}equals(e){return e.center.equals(this.center)&&e.radius===this.radius}clone(){return new this.constructor().copy(this)}toJSON(){return{radius:this.radius,center:this.center.toArray()}}fromJSON(e){return this.radius=e.radius,this.center.fromArray(e.center),this}},S1=0,Qt=new nt,co=new Pt,Ri=new U,Wt=new Wn,ts=new Wn,St=new U,kt=class i extends ln{constructor(){super(),this.isBufferGeometry=!0,Object.defineProperty(this,"id",{value:S1++}),this.uuid=Zi(),this.name="",this.type="BufferGeometry",this.index=null,this.indirect=null,this.indirectOffset=0,this.attributes={},this.morphAttributes={},this.morphTargetsRelative=!1,this.groups=[],this.boundingBox=null,this.boundingSphere=null,this.drawRange={start:0,count:1/0},this.userData={},this._transformed=!1}getIndex(){return this.index}setIndex(e){return Array.isArray(e)?this.index=new(qh(e)?fs:ds)(e,1):this.index=e,this}setIndirect(e,t=0){return this.indirect=e,this.indirectOffset=t,this}getIndirect(){return this.indirect}getAttribute(e){return this.attributes[e]}setAttribute(e,t){return this.attributes[e]=t,this}deleteAttribute(e){return delete this.attributes[e],this}hasAttribute(e){return this.attributes[e]!==void 0}addGroup(e,t,n=0){this.groups.push({start:e,count:t,materialIndex:n})}clearGroups(){this.groups=[]}setDrawRange(e,t){this.drawRange.start=e,this.drawRange.count=t}applyMatrix4(e){let t=this.attributes.position;t!==void 0&&(t.applyMatrix4(e),t.needsUpdate=!0);let n=this.attributes.normal;if(n!==void 0){let r=new Ie().getNormalMatrix(e);n.applyNormalMatrix(r),n.needsUpdate=!0}let s=this.attributes.tangent;return s!==void 0&&(s.transformDirection(e),s.needsUpdate=!0),this.boundingBox!==null&&this.computeBoundingBox(),this.boundingSphere!==null&&this.computeBoundingSphere(),this._transformed=!0,this}applyQuaternion(e){return Qt.makeRotationFromQuaternion(e),this.applyMatrix4(Qt),this}rotateX(e){return Qt.makeRotationX(e),this.applyMatrix4(Qt),this}rotateY(e){return Qt.makeRotationY(e),this.applyMatrix4(Qt),this}rotateZ(e){return Qt.makeRotationZ(e),this.applyMatrix4(Qt),this}translate(e,t,n){return Qt.makeTranslation(e,t,n),this.applyMatrix4(Qt),this}scale(e,t,n){return Qt.makeScale(e,t,n),this.applyMatrix4(Qt),this}lookAt(e){return co.lookAt(e),co.updateMatrix(),this.applyMatrix4(co.matrix),this}center(){return this.computeBoundingBox(),this.boundingBox.getCenter(Ri).negate(),this.translate(Ri.x,Ri.y,Ri.z),this}setFromPoints(e){let t=this.getAttribute("position");if(t===void 0){let n=[];for(let s=0,r=e.length;s<r;s++){let a=e[s];n.push(a.x,a.y,a.z||0)}this.setAttribute("position",new ct(n,3))}else{let n=Math.min(e.length,t.count);for(let s=0;s<n;s++){let r=e[s];t.setXYZ(s,r.x,r.y,r.z||0)}e.length>t.count&&Te("BufferGeometry: Buffer size too small for points data. Use .dispose() and create a new geometry."),t.needsUpdate=!0}return this}computeBoundingBox(){this.boundingBox===null&&(this.boundingBox=new Wn);let e=this.attributes.position,t=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){Pe("BufferGeometry.computeBoundingBox(): GLBufferAttribute requires a manual bounding box.",this),this.boundingBox.set(new U(-1/0,-1/0,-1/0),new U(1/0,1/0,1/0));return}if(e!==void 0){if(this.boundingBox.setFromBufferAttribute(e),t)for(let n=0,s=t.length;n<s;n++){let r=t[n];Wt.setFromBufferAttribute(r),this.morphTargetsRelative?(St.addVectors(this.boundingBox.min,Wt.min),this.boundingBox.expandByPoint(St),St.addVectors(this.boundingBox.max,Wt.max),this.boundingBox.expandByPoint(St)):(this.boundingBox.expandByPoint(Wt.min),this.boundingBox.expandByPoint(Wt.max))}}else this.boundingBox.makeEmpty();(isNaN(this.boundingBox.min.x)||isNaN(this.boundingBox.min.y)||isNaN(this.boundingBox.min.z))&&Pe('BufferGeometry.computeBoundingBox(): Computed min/max have NaN values. The "position" attribute is likely to have NaN values.',this)}computeBoundingSphere(){this.boundingSphere===null&&(this.boundingSphere=new oi);let e=this.attributes.position,t=this.morphAttributes.position;if(e&&e.isGLBufferAttribute){Pe("BufferGeometry.computeBoundingSphere(): GLBufferAttribute requires a manual bounding sphere.",this),this.boundingSphere.set(new U,1/0);return}if(e){let n=this.boundingSphere.center;if(Wt.setFromBufferAttribute(e),t)for(let r=0,a=t.length;r<a;r++){let o=t[r];ts.setFromBufferAttribute(o),this.morphTargetsRelative?(St.addVectors(Wt.min,ts.min),Wt.expandByPoint(St),St.addVectors(Wt.max,ts.max),Wt.expandByPoint(St)):(Wt.expandByPoint(ts.min),Wt.expandByPoint(ts.max))}Wt.getCenter(n);let s=0;for(let r=0,a=e.count;r<a;r++)St.fromBufferAttribute(e,r),s=Math.max(s,n.distanceToSquared(St));if(t)for(let r=0,a=t.length;r<a;r++){let o=t[r],l=this.morphTargetsRelative;for(let c=0,h=o.count;c<h;c++)St.fromBufferAttribute(o,c),l&&(Ri.fromBufferAttribute(e,c),St.add(Ri)),s=Math.max(s,n.distanceToSquared(St))}this.boundingSphere.radius=Math.sqrt(s),isNaN(this.boundingSphere.radius)&&Pe('BufferGeometry.computeBoundingSphere(): Computed radius is NaN. The "position" attribute is likely to have NaN values.',this)}}computeTangents(){let e=this.index,t=this.attributes;if(e===null||t.position===void 0||t.normal===void 0||t.uv===void 0){Pe("BufferGeometry: .computeTangents() failed. Missing required attributes (index, position, normal or uv)");return}let n=t.position,s=t.normal,r=t.uv,a=this.getAttribute("tangent");(a===void 0||a.count!==n.count)&&(a=new _n(new Float32Array(4*n.count),4),this.setAttribute("tangent",a));let o=[],l=[],c=new Uint8Array(n.count);for(let N=0;N<n.count;N++)o[N]=new U,l[N]=new U;let h=new U,g=new U,d=new U,m=new Re,_=new Re,S=new Re,p=new U,u=new U;function M(N,I,D){c[N]=c[I]=c[D]=1,h.fromBufferAttribute(n,N),g.fromBufferAttribute(n,I),d.fromBufferAttribute(n,D),m.fromBufferAttribute(r,N),_.fromBufferAttribute(r,I),S.fromBufferAttribute(r,D),g.sub(h),d.sub(h),_.sub(m),S.sub(m);let z=1/(_.x*S.y-S.x*_.y);isFinite(z)&&(p.copy(g).multiplyScalar(S.y).addScaledVector(d,-_.y).multiplyScalar(z),u.copy(d).multiplyScalar(_.x).addScaledVector(g,-S.x).multiplyScalar(z),o[N].add(p),o[I].add(p),o[D].add(p),l[N].add(u),l[I].add(u),l[D].add(u))}let w=this.groups;w.length===0&&(w=[{start:0,count:e.count}]);for(let N=0,I=w.length;N<I;++N){let D=w[N],z=D.start,q=D.count;for(let P=z,W=z+q;P<W;P+=3)M(e.getX(P+0),e.getX(P+1),e.getX(P+2))}let E=new U,A=new U,T=new U,f=new U;function v(N){T.fromBufferAttribute(s,N),f.copy(T);let I=o[N];E.copy(I),E.sub(T.multiplyScalar(T.dot(I))).normalize(),A.crossVectors(f,I);let z=A.dot(l[N])<0?-1:1;a.setXYZW(N,E.x,E.y,E.z,z)}for(let N=0,I=n.count;N<I;++N)c[N]&&v(N);this._transformed=!0}computeVertexNormals(){let e=this.index,t=this.getAttribute("position");if(t!==void 0){let n=this.getAttribute("normal");if(n===void 0||n.count!==t.count)n=new _n(new Float32Array(t.count*3),3),this.setAttribute("normal",n);else for(let d=0,m=n.count;d<m;d++)n.setXYZ(d,0,0,0);let s=new U,r=new U,a=new U,o=new U,l=new U,c=new U,h=new U,g=new U;if(e)for(let d=0,m=e.count;d<m;d+=3){let _=e.getX(d+0),S=e.getX(d+1),p=e.getX(d+2);s.fromBufferAttribute(t,_),r.fromBufferAttribute(t,S),a.fromBufferAttribute(t,p),h.subVectors(a,r),g.subVectors(s,r),h.cross(g),o.fromBufferAttribute(n,_),l.fromBufferAttribute(n,S),c.fromBufferAttribute(n,p),o.add(h),l.add(h),c.add(h),n.setXYZ(_,o.x,o.y,o.z),n.setXYZ(S,l.x,l.y,l.z),n.setXYZ(p,c.x,c.y,c.z)}else for(let d=0,m=t.count;d<m;d+=3)s.fromBufferAttribute(t,d+0),r.fromBufferAttribute(t,d+1),a.fromBufferAttribute(t,d+2),h.subVectors(a,r),g.subVectors(s,r),h.cross(g),n.setXYZ(d+0,h.x,h.y,h.z),n.setXYZ(d+1,h.x,h.y,h.z),n.setXYZ(d+2,h.x,h.y,h.z);this.normalizeNormals(),n.needsUpdate=!0}}normalizeNormals(){let e=this.attributes.normal;for(let t=0,n=e.count;t<n;t++)St.fromBufferAttribute(e,t),St.normalize(),e.setXYZ(t,St.x,St.y,St.z)}toNonIndexed(){function e(o,l){let c=o.array,h=o.itemSize,g=o.normalized,d=new c.constructor(l.length*h),m=0,_=0;for(let S=0,p=l.length;S<p;S++){o.isInterleavedBufferAttribute?m=l[S]*o.data.stride+o.offset:m=l[S]*h;for(let u=0;u<h;u++)d[_++]=c[m++]}return new _n(d,h,g)}if(this.index===null)return Te("BufferGeometry.toNonIndexed(): BufferGeometry is already non-indexed."),this;let t=new i,n=this.index.array,s=this.attributes;for(let o in s){let l=s[o],c=e(l,n);t.setAttribute(o,c)}let r=this.morphAttributes;for(let o in r){let l=[],c=r[o];for(let h=0,g=c.length;h<g;h++){let d=c[h],m=e(d,n);l.push(m)}t.morphAttributes[o]=l}t.morphTargetsRelative=this.morphTargetsRelative;let a=this.groups;for(let o=0,l=a.length;o<l;o++){let c=a[o];t.addGroup(c.start,c.count,c.materialIndex)}return t}toJSON(){let e={metadata:{version:4.7,type:"BufferGeometry",generator:"BufferGeometry.toJSON"}};if(e.uuid=this.uuid,e.type=this.parameters!==void 0&&this._transformed===!0?"BufferGeometry":this.type,e.name=this.name,Object.keys(this.userData).length>0&&(e.userData=this.userData),this.parameters!==void 0&&this._transformed!==!0){let l=this.parameters;for(let c in l)l[c]!==void 0&&(e[c]=l[c]);return e}e.data={attributes:{}};let t=this.index;t!==null&&(e.data.index={type:t.array.constructor.name,array:Array.prototype.slice.call(t.array)});let n=this.attributes;for(let l in n){let c=n[l];e.data.attributes[l]=c.toJSON(e.data)}let s={},r=!1;for(let l in this.morphAttributes){let c=this.morphAttributes[l],h=[];for(let g=0,d=c.length;g<d;g++){let m=c[g];h.push(m.toJSON(e.data))}h.length>0&&(s[l]=h,r=!0)}r&&(e.data.morphAttributes=s,e.data.morphTargetsRelative=this.morphTargetsRelative);let a=this.groups;a.length>0&&(e.data.groups=JSON.parse(JSON.stringify(a)));let o=this.boundingSphere;return o!==null&&(e.data.boundingSphere=o.toJSON()),e}clone(){return new this.constructor().copy(this)}copy(e){this.index=null,this.attributes={},this.morphAttributes={},this.groups=[],this.boundingBox=null,this.boundingSphere=null;let t={};this.name=e.name;let n=e.index;n!==null&&this.setIndex(n.clone());let s=e.attributes;for(let c in s){let h=s[c];this.setAttribute(c,h.clone(t))}let r=e.morphAttributes;for(let c in r){let h=[],g=r[c];for(let d=0,m=g.length;d<m;d++)h.push(g[d].clone(t));this.morphAttributes[c]=h}this.morphTargetsRelative=e.morphTargetsRelative;let a=e.groups;for(let c=0,h=a.length;c<h;c++){let g=a[c];this.addGroup(g.start,g.count,g.materialIndex)}let o=e.boundingBox;o!==null&&(this.boundingBox=o.clone());let l=e.boundingSphere;return l!==null&&(this.boundingSphere=l.clone()),this.drawRange.start=e.drawRange.start,this.drawRange.count=e.drawRange.count,this.userData=e.userData,this._transformed=e._transformed,this}dispose(){this.dispatchEvent({type:"dispose"})}};var ho=new U,M1=new U,b1=new Ie,Xt=class{constructor(e=new U(1,0,0),t=0){this.isPlane=!0,this.normal=e,this.constant=t}set(e,t){return this.normal.copy(e),this.constant=t,this}setComponents(e,t,n,s){return this.normal.set(e,t,n),this.constant=s,this}setFromNormalAndCoplanarPoint(e,t){return this.normal.copy(e),this.constant=-t.dot(this.normal),this}setFromCoplanarPoints(e,t,n){let s=ho.subVectors(n,t).cross(M1.subVectors(e,t)).normalize();return this.setFromNormalAndCoplanarPoint(s,e),this}copy(e){return this.normal.copy(e.normal),this.constant=e.constant,this}normalize(){let e=1/this.normal.length();return this.normal.multiplyScalar(e),this.constant*=e,this}negate(){return this.constant*=-1,this.normal.negate(),this}distanceToPoint(e){return this.normal.dot(e)+this.constant}distanceToSphere(e){return this.distanceToPoint(e.center)-e.radius}projectPoint(e,t){return t.copy(e).addScaledVector(this.normal,-this.distanceToPoint(e))}intersectLine(e,t,n=!0){let s=e.delta(ho),r=this.normal.dot(s);if(r===0)return this.distanceToPoint(e.start)===0?t.copy(e.start):null;let a=-(e.start.dot(this.normal)+this.constant)/r;return n===!0&&(a<0||a>1)?null:t.copy(e.start).addScaledVector(s,a)}intersectsLine(e){let t=this.distanceToPoint(e.start),n=this.distanceToPoint(e.end);return t<0&&n>0||n<0&&t>0}intersectsBox(e){return e.intersectsPlane(this)}intersectsSphere(e){return e.intersectsPlane(this)}coplanarPoint(e){return e.copy(this.normal).multiplyScalar(-this.constant)}applyMatrix4(e,t){let n=t||b1.getNormalMatrix(e),s=this.coplanarPoint(ho).applyMatrix4(e),r=this.normal.applyMatrix3(n).normalize();return this.constant=-s.dot(r),this}translate(e){return this.constant-=e.dot(this.normal),this}equals(e){return e.normal.equals(this.normal)&&e.constant===this.constant}clone(){return new this.constructor().copy(this)}toJSON(){return{normal:this.normal.toArray(),constant:this.constant}}fromJSON(e){return this.normal.fromArray(e.normal),this.constant=e.constant,this}},E1=0,In=class extends ln{constructor(){super(),this.isMaterial=!0,Object.defineProperty(this,"id",{value:E1++}),this.uuid=Zi(),this.name="",this.type="Material",this.blending=Xi,this.side=jn,this.vertexColors=!1,this.opacity=1,this.transparent=!1,this.alphaHash=!1,this.blendSrc=Ro,this.blendDst=Co,this.blendEquation=di,this.blendSrcAlpha=null,this.blendDstAlpha=null,this.blendEquationAlpha=null,this.blendColor=new Be(0,0,0),this.blendAlpha=0,this.depthFunc=Di,this.depthTest=!0,this.depthWrite=!0,this.stencilWriteMask=255,this.stencilFunc=Gc,this.stencilRef=0,this.stencilFuncMask=255,this.stencilFail=pr,this.stencilZFail=pr,this.stencilZPass=pr,this.stencilWrite=!1,this.clippingPlanes=null,this.clipIntersection=!1,this.clipShadows=!1,this.shadowSide=null,this.colorWrite=!0,this.precision=null,this.polygonOffset=!1,this.polygonOffsetFactor=0,this.polygonOffsetUnits=0,this.dithering=!1,this.alphaToCoverage=!1,this.premultipliedAlpha=!1,this.forceSinglePass=!1,this.allowOverride=!0,this.visible=!0,this.toneMapped=!0,this.userData={},this.version=0,this._alphaTest=0}get alphaTest(){return this._alphaTest}set alphaTest(e){this._alphaTest>0!=e>0&&this.version++,this._alphaTest=e}onBeforeRender(){}onBeforeCompile(){}customProgramCacheKey(){return this.onBeforeCompile.toString()}setValues(e){if(e!==void 0)for(let t in e){let n=e[t];if(n===void 0){Te(`Material: parameter '${t}' has value of undefined.`);continue}let s=this[t];if(s===void 0){Te(`Material: '${t}' is not a property of THREE.${this.type}.`);continue}s&&s.isColor?s.set(n):s&&s.isVector2&&n&&n.isVector2||s&&s.isEuler&&n&&n.isEuler||s&&s.isVector3&&n&&n.isVector3?s.copy(n):this[t]=n}}toJSON(e){let t=e===void 0||typeof e=="string";t&&(e={textures:{},images:{}});let n={metadata:{version:4.7,type:"Material",generator:"Material.toJSON"}};n.uuid=this.uuid,n.type=this.type,n.blending=this.blending,n.side=this.side,n.shadowSide=this.shadowSide,n.vertexColors=this.vertexColors,n.opacity=this.opacity,n.transparent=this.transparent,n.blendSrc=this.blendSrc,n.blendDst=this.blendDst,n.blendEquation=this.blendEquation,n.blendSrcAlpha=this.blendSrcAlpha,n.blendDstAlpha=this.blendDstAlpha,n.blendEquationAlpha=this.blendEquationAlpha,n.blendColor=this.blendColor.getHex(),n.blendAlpha=this.blendAlpha,n.depthFunc=this.depthFunc,n.depthTest=this.depthTest,n.depthWrite=this.depthWrite,n.colorWrite=this.colorWrite,n.clipIntersection=this.clipIntersection,n.clipShadows=this.clipShadows,n.stencilWriteMask=this.stencilWriteMask,n.stencilFunc=this.stencilFunc,n.stencilRef=this.stencilRef,n.stencilFuncMask=this.stencilFuncMask,n.stencilFail=this.stencilFail,n.stencilZFail=this.stencilZFail,n.stencilZPass=this.stencilZPass,n.stencilWrite=this.stencilWrite,n.polygonOffset=this.polygonOffset,n.polygonOffsetFactor=this.polygonOffsetFactor,n.polygonOffsetUnits=this.polygonOffsetUnits,n.dithering=this.dithering,n.alphaTest=this.alphaTest,n.alphaHash=this.alphaHash,n.alphaToCoverage=this.alphaToCoverage,n.premultipliedAlpha=this.premultipliedAlpha,n.forceSinglePass=this.forceSinglePass,n.allowOverride=this.allowOverride,n.visible=this.visible,n.toneMapped=this.toneMapped,n.name=this.name,this.color&&this.color.isColor&&(n.color=this.color.getHex()),this.roughness!==void 0&&(n.roughness=this.roughness),this.metalness!==void 0&&(n.metalness=this.metalness),this.sheen!==void 0&&(n.sheen=this.sheen),this.sheenColor&&this.sheenColor.isColor&&(n.sheenColor=this.sheenColor.getHex()),this.sheenRoughness!==void 0&&(n.sheenRoughness=this.sheenRoughness),this.emissive&&this.emissive.isColor&&(n.emissive=this.emissive.getHex()),this.emissiveIntensity!==void 0&&(n.emissiveIntensity=this.emissiveIntensity),this.specular&&this.specular.isColor&&(n.specular=this.specular.getHex()),this.specularIntensity!==void 0&&(n.specularIntensity=this.specularIntensity),this.specularColor&&this.specularColor.isColor&&(n.specularColor=this.specularColor.getHex()),this.shininess!==void 0&&(n.shininess=this.shininess),this.clearcoat!==void 0&&(n.clearcoat=this.clearcoat),this.clearcoatRoughness!==void 0&&(n.clearcoatRoughness=this.clearcoatRoughness),this.diffuseRoughness!==void 0&&(n.diffuseRoughness=this.diffuseRoughness),this.diffuseRoughnessMap&&this.diffuseRoughnessMap.isTexture&&(n.diffuseRoughnessMap=this.diffuseRoughnessMap.toJSON(e).uuid),this.clearcoatMap&&this.clearcoatMap.isTexture&&(n.clearcoatMap=this.clearcoatMap.toJSON(e).uuid),this.clearcoatRoughnessMap&&this.clearcoatRoughnessMap.isTexture&&(n.clearcoatRoughnessMap=this.clearcoatRoughnessMap.toJSON(e).uuid),this.clearcoatNormalMap&&this.clearcoatNormalMap.isTexture&&(n.clearcoatNormalMap=this.clearcoatNormalMap.toJSON(e).uuid,n.clearcoatNormalScale=this.clearcoatNormalScale.toArray()),this.sheenColorMap&&this.sheenColorMap.isTexture&&(n.sheenColorMap=this.sheenColorMap.toJSON(e).uuid),this.sheenRoughnessMap&&this.sheenRoughnessMap.isTexture&&(n.sheenRoughnessMap=this.sheenRoughnessMap.toJSON(e).uuid),this.dispersion!==void 0&&(n.dispersion=this.dispersion),this.retroreflectivity!==void 0&&(n.retroreflectivity=this.retroreflectivity),this.iridescence!==void 0&&(n.iridescence=this.iridescence),this.iridescenceIOR!==void 0&&(n.iridescenceIOR=this.iridescenceIOR),this.iridescenceThicknessMinimum!==void 0&&(n.iridescenceThicknessMinimum=this.iridescenceThicknessMinimum),this.iridescenceThicknessMaximum!==void 0&&(n.iridescenceThicknessMaximum=this.iridescenceThicknessMaximum),this.iridescenceMap&&this.iridescenceMap.isTexture&&(n.iridescenceMap=this.iridescenceMap.toJSON(e).uuid),this.iridescenceThicknessMap&&this.iridescenceThicknessMap.isTexture&&(n.iridescenceThicknessMap=this.iridescenceThicknessMap.toJSON(e).uuid),this.anisotropy!==void 0&&(n.anisotropy=this.anisotropy),this.anisotropyRotation!==void 0&&(n.anisotropyRotation=this.anisotropyRotation),this.anisotropyMap&&this.anisotropyMap.isTexture&&(n.anisotropyMap=this.anisotropyMap.toJSON(e).uuid),this.map&&this.map.isTexture&&(n.map=this.map.toJSON(e).uuid),this.matcap&&this.matcap.isTexture&&(n.matcap=this.matcap.toJSON(e).uuid),this.alphaMap&&this.alphaMap.isTexture&&(n.alphaMap=this.alphaMap.toJSON(e).uuid),this.lightMap&&this.lightMap.isTexture&&(n.lightMap=this.lightMap.toJSON(e).uuid,n.lightMapIntensity=this.lightMapIntensity),this.aoMap&&this.aoMap.isTexture&&(n.aoMap=this.aoMap.toJSON(e).uuid,n.aoMapIntensity=this.aoMapIntensity),this.bumpMap&&this.bumpMap.isTexture&&(n.bumpMap=this.bumpMap.toJSON(e).uuid,n.bumpScale=this.bumpScale),this.normalMap&&this.normalMap.isTexture&&(n.normalMap=this.normalMap.toJSON(e).uuid,n.normalMapType=this.normalMapType,n.normalScale=this.normalScale.toArray()),this.displacementMap&&this.displacementMap.isTexture&&(n.displacementMap=this.displacementMap.toJSON(e).uuid,n.displacementScale=this.displacementScale,n.displacementBias=this.displacementBias),this.roughnessMap&&this.roughnessMap.isTexture&&(n.roughnessMap=this.roughnessMap.toJSON(e).uuid),this.metalnessMap&&this.metalnessMap.isTexture&&(n.metalnessMap=this.metalnessMap.toJSON(e).uuid),this.emissiveMap&&this.emissiveMap.isTexture&&(n.emissiveMap=this.emissiveMap.toJSON(e).uuid),this.specularMap&&this.specularMap.isTexture&&(n.specularMap=this.specularMap.toJSON(e).uuid),this.specularIntensityMap&&this.specularIntensityMap.isTexture&&(n.specularIntensityMap=this.specularIntensityMap.toJSON(e).uuid),this.specularColorMap&&this.specularColorMap.isTexture&&(n.specularColorMap=this.specularColorMap.toJSON(e).uuid),this.envMap&&this.envMap.isTexture&&(n.envMap=this.envMap.toJSON(e).uuid,this.combine!==void 0&&(n.combine=this.combine)),this.envMapRotation!==void 0&&(n.envMapRotation=this.envMapRotation.toArray()),this.envMapIntensity!==void 0&&(n.envMapIntensity=this.envMapIntensity),this.reflectivity!==void 0&&(n.reflectivity=this.reflectivity),this.refractionRatio!==void 0&&(n.refractionRatio=this.refractionRatio),this.gradientMap&&this.gradientMap.isTexture&&(n.gradientMap=this.gradientMap.toJSON(e).uuid),this.transmission!==void 0&&(n.transmission=this.transmission),this.transmissionMap&&this.transmissionMap.isTexture&&(n.transmissionMap=this.transmissionMap.toJSON(e).uuid),this.thickness!==void 0&&(n.thickness=this.thickness),this.thicknessMap&&this.thicknessMap.isTexture&&(n.thicknessMap=this.thicknessMap.toJSON(e).uuid),this.attenuationDistance!==void 0&&(n.attenuationDistance=this.attenuationDistance),this.attenuationColor!==void 0&&(n.attenuationColor=this.attenuationColor.getHex()),this.size!==void 0&&(n.size=this.size),this.sizeAttenuation!==void 0&&(n.sizeAttenuation=this.sizeAttenuation),Array.isArray(this.clippingPlanes)&&this.clippingPlanes.length>0&&(n.clippingPlanes=this.clippingPlanes.map(r=>r.toJSON())),this.rotation!==void 0&&(n.rotation=this.rotation),this.depthPacking!==void 0&&(n.depthPacking=this.depthPacking),this.linewidth!==void 0&&(n.linewidth=this.linewidth),this.linecap!==void 0&&(n.linecap=this.linecap),this.linejoin!==void 0&&(n.linejoin=this.linejoin),this.dashSize!==void 0&&(n.dashSize=this.dashSize),this.gapSize!==void 0&&(n.gapSize=this.gapSize),this.scale!==void 0&&(n.scale=this.scale),this.wireframe!==void 0&&(n.wireframe=this.wireframe),this.wireframeLinewidth!==void 0&&(n.wireframeLinewidth=this.wireframeLinewidth),this.wireframeLinecap!==void 0&&(n.wireframeLinecap=this.wireframeLinecap),this.wireframeLinejoin!==void 0&&(n.wireframeLinejoin=this.wireframeLinejoin),this.flatShading!==void 0&&(n.flatShading=this.flatShading),this.fog!==void 0&&(n.fog=this.fog),Object.keys(this.userData).length>0&&(n.userData=this.userData);function s(r){let a=[];for(let o in r){let l=r[o];delete l.metadata,a.push(l)}return a}if(t){let r=s(e.textures),a=s(e.images);r.length>0&&(n.textures=r),a.length>0&&(n.images=a)}return n}fromJSON(e,t){if(e.uuid!==void 0&&(this.uuid=e.uuid),e.name!==void 0&&(this.name=e.name),e.color!==void 0&&this.color!==void 0&&this.color.setHex(e.color),e.roughness!==void 0&&(this.roughness=e.roughness),e.metalness!==void 0&&(this.metalness=e.metalness),e.sheen!==void 0&&(this.sheen=e.sheen),e.sheenColor!==void 0&&(this.sheenColor=new Be().setHex(e.sheenColor)),e.sheenRoughness!==void 0&&(this.sheenRoughness=e.sheenRoughness),e.emissive!==void 0&&this.emissive!==void 0&&this.emissive.setHex(e.emissive),e.specular!==void 0&&this.specular!==void 0&&this.specular.setHex(e.specular),e.specularIntensity!==void 0&&(this.specularIntensity=e.specularIntensity),e.specularColor!==void 0&&this.specularColor!==void 0&&this.specularColor.setHex(e.specularColor),e.shininess!==void 0&&(this.shininess=e.shininess),e.clearcoat!==void 0&&(this.clearcoat=e.clearcoat),e.clearcoatRoughness!==void 0&&(this.clearcoatRoughness=e.clearcoatRoughness),e.diffuseRoughness!==void 0&&(this.diffuseRoughness=e.diffuseRoughness),e.dispersion!==void 0&&(this.dispersion=e.dispersion),e.retroreflectivity!==void 0&&(this.retroreflectivity=e.retroreflectivity),e.iridescence!==void 0&&(this.iridescence=e.iridescence),e.iridescenceIOR!==void 0&&(this.iridescenceIOR=e.iridescenceIOR),e.iridescenceThicknessMinimum!==void 0&&(this.iridescenceThicknessMinimum=e.iridescenceThicknessMinimum),e.iridescenceThicknessMaximum!==void 0&&(this.iridescenceThicknessMaximum=e.iridescenceThicknessMaximum),e.iridescenceThicknessRange!==void 0&&(this.iridescenceThicknessMinimum=e.iridescenceThicknessRange[0],this.iridescenceThicknessMaximum=e.iridescenceThicknessRange[1]),e.transmission!==void 0&&(this.transmission=e.transmission),e.thickness!==void 0&&(this.thickness=e.thickness),e.attenuationDistance!==void 0&&(this.attenuationDistance=e.attenuationDistance),e.attenuationColor!==void 0&&this.attenuationColor!==void 0&&this.attenuationColor.setHex(e.attenuationColor),e.anisotropy!==void 0&&(this.anisotropy=e.anisotropy),e.anisotropyRotation!==void 0&&(this.anisotropyRotation=e.anisotropyRotation),e.fog!==void 0&&(this.fog=e.fog),e.flatShading!==void 0&&(this.flatShading=e.flatShading),e.blending!==void 0&&(this.blending=e.blending),e.combine!==void 0&&(this.combine=e.combine),e.side!==void 0&&(this.side=e.side),e.shadowSide!==void 0&&(this.shadowSide=e.shadowSide),e.opacity!==void 0&&(this.opacity=e.opacity),e.transparent!==void 0&&(this.transparent=e.transparent),e.alphaTest!==void 0&&(this.alphaTest=e.alphaTest),e.alphaHash!==void 0&&(this.alphaHash=e.alphaHash),e.depthFunc!==void 0&&(this.depthFunc=e.depthFunc),e.depthTest!==void 0&&(this.depthTest=e.depthTest),e.depthWrite!==void 0&&(this.depthWrite=e.depthWrite),e.colorWrite!==void 0&&(this.colorWrite=e.colorWrite),e.clippingPlanes!==void 0&&(this.clippingPlanes=e.clippingPlanes.map(n=>new Xt().fromJSON(n))),e.clipIntersection!==void 0&&(this.clipIntersection=e.clipIntersection),e.clipShadows!==void 0&&(this.clipShadows=e.clipShadows),e.depthPacking!==void 0&&(this.depthPacking=e.depthPacking),e.blendSrc!==void 0&&(this.blendSrc=e.blendSrc),e.blendDst!==void 0&&(this.blendDst=e.blendDst),e.blendEquation!==void 0&&(this.blendEquation=e.blendEquation),e.blendSrcAlpha!==void 0&&(this.blendSrcAlpha=e.blendSrcAlpha),e.blendDstAlpha!==void 0&&(this.blendDstAlpha=e.blendDstAlpha),e.blendEquationAlpha!==void 0&&(this.blendEquationAlpha=e.blendEquationAlpha),e.blendColor!==void 0&&this.blendColor!==void 0&&this.blendColor.setHex(e.blendColor),e.blendAlpha!==void 0&&(this.blendAlpha=e.blendAlpha),e.stencilWriteMask!==void 0&&(this.stencilWriteMask=e.stencilWriteMask),e.stencilFunc!==void 0&&(this.stencilFunc=e.stencilFunc),e.stencilRef!==void 0&&(this.stencilRef=e.stencilRef),e.stencilFuncMask!==void 0&&(this.stencilFuncMask=e.stencilFuncMask),e.stencilFail!==void 0&&(this.stencilFail=e.stencilFail),e.stencilZFail!==void 0&&(this.stencilZFail=e.stencilZFail),e.stencilZPass!==void 0&&(this.stencilZPass=e.stencilZPass),e.stencilWrite!==void 0&&(this.stencilWrite=e.stencilWrite),e.wireframe!==void 0&&(this.wireframe=e.wireframe),e.wireframeLinewidth!==void 0&&(this.wireframeLinewidth=e.wireframeLinewidth),e.wireframeLinecap!==void 0&&(this.wireframeLinecap=e.wireframeLinecap),e.wireframeLinejoin!==void 0&&(this.wireframeLinejoin=e.wireframeLinejoin),e.rotation!==void 0&&(this.rotation=e.rotation),e.linewidth!==void 0&&(this.linewidth=e.linewidth),e.linecap!==void 0&&(this.linecap=e.linecap),e.linejoin!==void 0&&(this.linejoin=e.linejoin),e.dashSize!==void 0&&(this.dashSize=e.dashSize),e.gapSize!==void 0&&(this.gapSize=e.gapSize),e.scale!==void 0&&(this.scale=e.scale),e.polygonOffset!==void 0&&(this.polygonOffset=e.polygonOffset),e.polygonOffsetFactor!==void 0&&(this.polygonOffsetFactor=e.polygonOffsetFactor),e.polygonOffsetUnits!==void 0&&(this.polygonOffsetUnits=e.polygonOffsetUnits),e.dithering!==void 0&&(this.dithering=e.dithering),e.alphaToCoverage!==void 0&&(this.alphaToCoverage=e.alphaToCoverage),e.premultipliedAlpha!==void 0&&(this.premultipliedAlpha=e.premultipliedAlpha),e.forceSinglePass!==void 0&&(this.forceSinglePass=e.forceSinglePass),e.allowOverride!==void 0&&(this.allowOverride=e.allowOverride),e.visible!==void 0&&(this.visible=e.visible),e.toneMapped!==void 0&&(this.toneMapped=e.toneMapped),e.userData!==void 0&&(this.userData=e.userData),e.vertexColors!==void 0&&(typeof e.vertexColors=="number"?this.vertexColors=e.vertexColors>0:this.vertexColors=e.vertexColors),e.size!==void 0&&(this.size=e.size),e.sizeAttenuation!==void 0&&(this.sizeAttenuation=e.sizeAttenuation),e.map!==void 0&&(this.map=t[e.map]||null),e.matcap!==void 0&&(this.matcap=t[e.matcap]||null),e.alphaMap!==void 0&&(this.alphaMap=t[e.alphaMap]||null),e.bumpMap!==void 0&&(this.bumpMap=t[e.bumpMap]||null),e.bumpScale!==void 0&&(this.bumpScale=e.bumpScale),e.normalMap!==void 0&&(this.normalMap=t[e.normalMap]||null),e.normalMapType!==void 0&&(this.normalMapType=e.normalMapType),e.normalScale!==void 0){let n=e.normalScale;Array.isArray(n)===!1&&(n=[n,n]),this.normalScale=new Re().fromArray(n)}return e.displacementMap!==void 0&&(this.displacementMap=t[e.displacementMap]||null),e.displacementScale!==void 0&&(this.displacementScale=e.displacementScale),e.displacementBias!==void 0&&(this.displacementBias=e.displacementBias),e.roughnessMap!==void 0&&(this.roughnessMap=t[e.roughnessMap]||null),e.metalnessMap!==void 0&&(this.metalnessMap=t[e.metalnessMap]||null),e.emissiveMap!==void 0&&(this.emissiveMap=t[e.emissiveMap]||null),e.emissiveIntensity!==void 0&&(this.emissiveIntensity=e.emissiveIntensity),e.specularMap!==void 0&&(this.specularMap=t[e.specularMap]||null),e.specularIntensityMap!==void 0&&(this.specularIntensityMap=t[e.specularIntensityMap]||null),e.specularColorMap!==void 0&&(this.specularColorMap=t[e.specularColorMap]||null),e.envMap!==void 0&&(this.envMap=t[e.envMap]||null),e.envMapRotation!==void 0&&this.envMapRotation.fromArray(e.envMapRotation),e.envMapIntensity!==void 0&&(this.envMapIntensity=e.envMapIntensity),e.reflectivity!==void 0&&(this.reflectivity=e.reflectivity),e.refractionRatio!==void 0&&(this.refractionRatio=e.refractionRatio),e.lightMap!==void 0&&(this.lightMap=t[e.lightMap]||null),e.lightMapIntensity!==void 0&&(this.lightMapIntensity=e.lightMapIntensity),e.aoMap!==void 0&&(this.aoMap=t[e.aoMap]||null),e.aoMapIntensity!==void 0&&(this.aoMapIntensity=e.aoMapIntensity),e.gradientMap!==void 0&&(this.gradientMap=t[e.gradientMap]||null),e.clearcoatMap!==void 0&&(this.clearcoatMap=t[e.clearcoatMap]||null),e.clearcoatRoughnessMap!==void 0&&(this.clearcoatRoughnessMap=t[e.clearcoatRoughnessMap]||null),e.clearcoatNormalMap!==void 0&&(this.clearcoatNormalMap=t[e.clearcoatNormalMap]||null),e.clearcoatNormalScale!==void 0&&(this.clearcoatNormalScale=new Re().fromArray(e.clearcoatNormalScale)),e.diffuseRoughnessMap!==void 0&&(this.diffuseRoughnessMap=t[e.diffuseRoughnessMap]||null),e.iridescenceMap!==void 0&&(this.iridescenceMap=t[e.iridescenceMap]||null),e.iridescenceThicknessMap!==void 0&&(this.iridescenceThicknessMap=t[e.iridescenceThicknessMap]||null),e.transmissionMap!==void 0&&(this.transmissionMap=t[e.transmissionMap]||null),e.thicknessMap!==void 0&&(this.thicknessMap=t[e.thicknessMap]||null),e.anisotropyMap!==void 0&&(this.anisotropyMap=t[e.anisotropyMap]||null),e.sheenColorMap!==void 0&&(this.sheenColorMap=t[e.sheenColorMap]||null),e.sheenRoughnessMap!==void 0&&(this.sheenRoughnessMap=t[e.sheenRoughnessMap]||null),this}clone(){return new this.constructor().copy(this)}copy(e){this.name=e.name,this.blending=e.blending,this.side=e.side,this.vertexColors=e.vertexColors,this.opacity=e.opacity,this.transparent=e.transparent,this.blendSrc=e.blendSrc,this.blendDst=e.blendDst,this.blendEquation=e.blendEquation,this.blendSrcAlpha=e.blendSrcAlpha,this.blendDstAlpha=e.blendDstAlpha,this.blendEquationAlpha=e.blendEquationAlpha,this.blendColor.copy(e.blendColor),this.blendAlpha=e.blendAlpha,this.depthFunc=e.depthFunc,this.depthTest=e.depthTest,this.depthWrite=e.depthWrite,this.stencilWriteMask=e.stencilWriteMask,this.stencilFunc=e.stencilFunc,this.stencilRef=e.stencilRef,this.stencilFuncMask=e.stencilFuncMask,this.stencilFail=e.stencilFail,this.stencilZFail=e.stencilZFail,this.stencilZPass=e.stencilZPass,this.stencilWrite=e.stencilWrite;let t=e.clippingPlanes,n=null;if(t!==null){let s=t.length;n=new Array(s);for(let r=0;r!==s;++r)n[r]=t[r].clone()}return this.clippingPlanes=n,this.clipIntersection=e.clipIntersection,this.clipShadows=e.clipShadows,this.shadowSide=e.shadowSide,this.colorWrite=e.colorWrite,this.precision=e.precision,this.polygonOffset=e.polygonOffset,this.polygonOffsetFactor=e.polygonOffsetFactor,this.polygonOffsetUnits=e.polygonOffsetUnits,this.dithering=e.dithering,this.alphaTest=e.alphaTest,this.alphaHash=e.alphaHash,this.alphaToCoverage=e.alphaToCoverage,this.premultipliedAlpha=e.premultipliedAlpha,this.forceSinglePass=e.forceSinglePass,this.allowOverride=e.allowOverride,this.visible=e.visible,this.toneMapped=e.toneMapped,this.userData=JSON.parse(JSON.stringify(e.userData)),this}dispose(){this.dispatchEvent({type:"dispose"})}set needsUpdate(e){e===!0&&this.version++}};var An=new U,uo=new U,js=new U,Qs=new U,Xn=class{constructor(e=new U,t=new U(0,0,-1)){this.origin=e,this.direction=t}set(e,t){return this.origin.copy(e),this.direction.copy(t),this}copy(e){return this.origin.copy(e.origin),this.direction.copy(e.direction),this}at(e,t){return t.copy(this.origin).addScaledVector(this.direction,e)}lookAt(e){return this.direction.copy(e).sub(this.origin).normalize(),this}recast(e){return this.origin.copy(this.at(e,An)),this}closestPointToPoint(e,t){t.subVectors(e,this.origin);let n=t.dot(this.direction);return n<0?t.copy(this.origin):t.copy(this.origin).addScaledVector(this.direction,n)}distanceToPoint(e){return Math.sqrt(this.distanceSqToPoint(e))}distanceSqToPoint(e){let t=An.subVectors(e,this.origin).dot(this.direction);return t<0?this.origin.distanceToSquared(e):(An.copy(this.origin).addScaledVector(this.direction,t),An.distanceToSquared(e))}distanceSqToSegment(e,t,n,s){uo.copy(e).add(t).multiplyScalar(.5),js.copy(t).sub(e).normalize(),Qs.copy(this.origin).sub(uo);let r=e.distanceTo(t)*.5,a=-this.direction.dot(js),o=Qs.dot(this.direction),l=-Qs.dot(js),c=Qs.lengthSq(),h=Math.abs(1-a*a),g,d,m,_;if(h>0)if(g=a*l-o,d=a*o-l,_=r*h,g>=0)if(d>=-_)if(d<=_){let S=1/h;g*=S,d*=S,m=g*(g+a*d+2*o)+d*(a*g+d+2*l)+c}else d=r,g=Math.max(0,-(a*d+o)),m=-g*g+d*(d+2*l)+c;else d=-r,g=Math.max(0,-(a*d+o)),m=-g*g+d*(d+2*l)+c;else d<=-_?(g=Math.max(0,-(-a*r+o)),d=g>0?-r:Math.min(Math.max(-r,-l),r),m=-g*g+d*(d+2*l)+c):d<=_?(g=0,d=Math.min(Math.max(-r,-l),r),m=d*(d+2*l)+c):(g=Math.max(0,-(a*r+o)),d=g>0?r:Math.min(Math.max(-r,-l),r),m=-g*g+d*(d+2*l)+c);else d=a>0?-r:r,g=Math.max(0,-(a*d+o)),m=-g*g+d*(d+2*l)+c;return n&&n.copy(this.origin).addScaledVector(this.direction,g),s&&s.copy(uo).addScaledVector(js,d),m}intersectSphere(e,t){if(e.radius<0)return null;An.subVectors(e.center,this.origin);let n=An.dot(this.direction),s=An.dot(An)-n*n,r=e.radius*e.radius;if(s>r)return null;let a=Math.sqrt(r-s),o=n-a,l=n+a;return l<0?null:o<0?this.at(l,t):this.at(o,t)}intersectsSphere(e){return e.radius<0?!1:this.distanceSqToPoint(e.center)<=e.radius*e.radius}distanceToPlane(e){let t=e.normal.dot(this.direction);if(t===0)return e.distanceToPoint(this.origin)===0?0:null;let n=-(this.origin.dot(e.normal)+e.constant)/t;return n>=0?n:null}intersectPlane(e,t){let n=this.distanceToPlane(e);return n===null?null:this.at(n,t)}intersectsPlane(e){let t=e.distanceToPoint(this.origin);return t===0||e.normal.dot(this.direction)*t<0}intersectBox(e,t){let n,s,r,a,o,l,c=1/this.direction.x,h=1/this.direction.y,g=1/this.direction.z,d=this.origin;return c>=0?(n=(e.min.x-d.x)*c,s=(e.max.x-d.x)*c):(n=(e.max.x-d.x)*c,s=(e.min.x-d.x)*c),h>=0?(r=(e.min.y-d.y)*h,a=(e.max.y-d.y)*h):(r=(e.max.y-d.y)*h,a=(e.min.y-d.y)*h),n>a||r>s||((r>n||isNaN(n))&&(n=r),(a<s||isNaN(s))&&(s=a),g>=0?(o=(e.min.z-d.z)*g,l=(e.max.z-d.z)*g):(o=(e.max.z-d.z)*g,l=(e.min.z-d.z)*g),n>l||o>s)||((o>n||n!==n)&&(n=o),(l<s||s!==s)&&(s=l),s<0)?null:this.at(n>=0?n:s,t)}intersectsBox(e){return this.intersectBox(e,An)!==null}intersectTriangle(e,t,n,s,r){let a=this.origin,o=this.direction,l=o.x,c=o.y,h=o.z,g=e.x-a.x,d=e.y-a.y,m=e.z-a.z,_=t.x-a.x,S=t.y-a.y,p=t.z-a.z,u=n.x-a.x,M=n.y-a.y,w=n.z-a.z,E=Math.abs(l),A=Math.abs(c),T=Math.abs(h),f,v,N,I,D,z,q,P,W,$,G,te;if(E>=A&&E>=T?(N=l,z=g,W=_,te=u,l>=0?(f=c,v=h,I=d,D=m,q=S,P=p,$=M,G=w):(f=h,v=c,I=m,D=d,q=p,P=S,$=w,G=M)):A>=T?(N=c,z=d,W=S,te=M,c>=0?(f=h,v=l,I=m,D=g,q=p,P=_,$=w,G=u):(f=l,v=h,I=g,D=m,q=_,P=p,$=u,G=w)):(N=h,z=m,W=p,te=w,h>=0?(f=l,v=c,I=g,D=d,q=_,P=S,$=u,G=M):(f=c,v=l,I=d,D=g,q=S,P=_,$=M,G=u)),N===0)return null;let H=f/N,j=v/N,Q=1/N,Se=I-H*z,De=D-j*z,Z=q-H*W,pe=P-j*W,xe=$-H*te,Ae=G-j*te,me=xe*pe-Ae*Z,Ue=Se*Ae-De*xe,ht=Z*De-pe*Se;if(s){if(me<0||Ue<0||ht<0)return null}else if((me<0||Ue<0||ht<0)&&(me>0||Ue>0||ht>0))return null;let Ce=me+Ue+ht;if(Ce===0)return null;let Ke=Q*(me*z+Ue*W+ht*te);return(Ce>0?Ke<0:Ke>0)?null:this.at(Ke/Ce,r)}applyMatrix4(e){return this.origin.applyMatrix4(e),this.direction.transformDirection(e),this}equals(e){return e.origin.equals(this.origin)&&e.direction.equals(this.direction)}clone(){return new this.constructor().copy(this)}},li=class extends In{constructor(e){super(),this.isMeshBasicMaterial=!0,this.type="MeshBasicMaterial",this.color=new Be(16777215),this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Pn,this.combine=Zr,this.reflectivity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.lightMap=e.lightMap,this.lightMapIntensity=e.lightMapIntensity,this.aoMap=e.aoMap,this.aoMapIntensity=e.aoMapIntensity,this.specularMap=e.specularMap,this.alphaMap=e.alphaMap,this.envMap=e.envMap,this.envMapRotation.copy(e.envMapRotation),this.combine=e.combine,this.reflectivity=e.reflectivity,this.refractionRatio=e.refractionRatio,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.wireframeLinecap=e.wireframeLinecap,this.wireframeLinejoin=e.wireframeLinejoin,this.fog=e.fog,this}},jl=new nt,ri=new Xn,er=new oi,Ql=new U,tr=new U,nr=new U,ir=new U,fo=new U,sr=new U,ec=new U,rr=new U,Ot=class extends Pt{constructor(e=new kt,t=new li){super(),this.isMesh=!0,this.type="Mesh",this.geometry=e,this.material=t,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.count=1,this.updateMorphTargets()}copy(e,t){return super.copy(e,t),e.morphTargetInfluences!==void 0?this.morphTargetInfluences=e.morphTargetInfluences.slice():this.morphTargetInfluences=void 0,e.morphTargetDictionary!==void 0?this.morphTargetDictionary=Object.assign({},e.morphTargetDictionary):this.morphTargetDictionary=void 0,this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}updateMorphTargets(){let t=this.geometry.morphAttributes,n=Object.keys(t);if(n.length>0){let s=t[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}getVertexPosition(e,t){let n=this.geometry,s=n.attributes.position,r=n.morphAttributes.position,a=n.morphTargetsRelative;t.fromBufferAttribute(s,e);let o=this.morphTargetInfluences;if(r&&o){sr.set(0,0,0);for(let l=0,c=r.length;l<c;l++){let h=o[l],g=r[l];h!==0&&(fo.fromBufferAttribute(g,e),a?sr.addScaledVector(fo,h):sr.addScaledVector(fo.sub(t),h))}t.add(sr)}return t}intersectsFrustum(e){return e.intersectsObject(this)}raycast(e,t){let n=this.geometry,s=this.material,r=this.matrixWorld;s!==void 0&&(n.boundingSphere===null&&n.computeBoundingSphere(),er.copy(n.boundingSphere),er.applyMatrix4(r),ri.copy(e.ray).recast(e.near),!(er.containsPoint(ri.origin)===!1&&(ri.intersectSphere(er,Ql)===null||ri.origin.distanceToSquared(Ql)>(e.far-e.near)**2))&&(jl.copy(r).invert(),ri.copy(e.ray).applyMatrix4(jl),!(n.boundingBox!==null&&ri.intersectsBox(n.boundingBox)===!1)&&this._computeIntersections(e,t,ri)))}_computeIntersections(e,t,n){let s,r=this.geometry,a=this.material,o=r.index,l=r.attributes.position,c=r.attributes.uv,h=r.attributes.uv1,g=r.attributes.normal,d=r.groups,m=r.drawRange;if(o!==null)if(Array.isArray(a))for(let _=0,S=d.length;_<S;_++){let p=d[_],u=a[p.materialIndex],M=Math.max(p.start,m.start),w=Math.min(o.count,Math.min(p.start+p.count,m.start+m.count));for(let E=M,A=w;E<A;E+=3){let T=o.getX(E),f=o.getX(E+1),v=o.getX(E+2);s=ar(this,u,e,n,c,h,g,T,f,v),s&&(s.faceIndex=Math.floor(E/3),s.face.materialIndex=p.materialIndex,t.push(s))}}else{let _=Math.max(0,m.start),S=Math.min(o.count,m.start+m.count);for(let p=_,u=S;p<u;p+=3){let M=o.getX(p),w=o.getX(p+1),E=o.getX(p+2);s=ar(this,a,e,n,c,h,g,M,w,E),s&&(s.faceIndex=Math.floor(p/3),t.push(s))}}else if(l!==void 0)if(Array.isArray(a))for(let _=0,S=d.length;_<S;_++){let p=d[_],u=a[p.materialIndex],M=Math.max(p.start,m.start),w=Math.min(l.count,Math.min(p.start+p.count,m.start+m.count));for(let E=M,A=w;E<A;E+=3){let T=E,f=E+1,v=E+2;s=ar(this,u,e,n,c,h,g,T,f,v),s&&(s.faceIndex=Math.floor(E/3),s.face.materialIndex=p.materialIndex,t.push(s))}}else{let _=Math.max(0,m.start),S=Math.min(l.count,m.start+m.count);for(let p=_,u=S;p<u;p+=3){let M=p,w=p+1,E=p+2;s=ar(this,a,e,n,c,h,g,M,w,E),s&&(s.faceIndex=Math.floor(p/3),t.push(s))}}}};function T1(i,e,t,n,s,r,a,o){let l;if(e.side===Tt?l=n.intersectTriangle(a,r,s,!0,o):l=n.intersectTriangle(s,r,a,e.side===jn,o),l===null)return null;rr.copy(o),rr.applyMatrix4(i.matrixWorld);let c=t.ray.origin.distanceTo(rr);return c<t.near||c>t.far?null:{distance:c,point:rr.clone(),object:i}}function ar(i,e,t,n,s,r,a,o,l,c){i.getVertexPosition(o,tr),i.getVertexPosition(l,nr),i.getVertexPosition(c,ir);let h=T1(i,e,t,n,tr,nr,ir,ec);if(h){let g=new U;Hn.getBarycoord(ec,tr,nr,ir,g),s&&(h.uv=Hn.getInterpolatedAttribute(s,o,l,c,g,new Re)),r&&(h.uv1=Hn.getInterpolatedAttribute(r,o,l,c,g,new Re)),a&&(h.normal=Hn.getInterpolatedAttribute(a,o,l,c,g,new U),h.normal.dot(n.direction)>0&&h.normal.multiplyScalar(-1));let d={a:o,b:l,c,normal:new U,materialIndex:0};Hn.getNormal(tr,nr,ir,d.normal),h.face=d,h.barycoord=g}return h}var Rr=class extends zt{constructor(e=null,t=1,n=1,s,r,a,o,l,c=Mt,h=Mt,g,d){super(null,a,o,l,c,h,s,r,g,d),this.isDataTexture=!0,this.image={data:e,width:t,height:n},this.generateMipmaps=!1,this.flipY=!1,this.unpackAlignment=1}};var ai=new oi,A1=new Re(.5,.5),or=new U,qn=class{constructor(e=new Xt,t=new Xt,n=new Xt,s=new Xt,r=new Xt,a=new Xt){this.planes=[e,t,n,s,r,a]}set(e,t,n,s,r,a){let o=this.planes;return o[0].copy(e),o[1].copy(t),o[2].copy(n),o[3].copy(s),o[4].copy(r),o[5].copy(a),this}copy(e){let t=this.planes;for(let n=0;n<6;n++)t[n].copy(e.planes[n]);return this}setFromProjectionMatrix(e,t=en,n=!1){let s=this.planes,r=e.elements,a=r[0],o=r[1],l=r[2],c=r[3],h=r[4],g=r[5],d=r[6],m=r[7],_=r[8],S=r[9],p=r[10],u=r[11],M=r[12],w=r[13],E=r[14],A=r[15];if(s[0].setComponents(c-a,m-h,u-_,A-M).normalize(),s[1].setComponents(c+a,m+h,u+_,A+M).normalize(),s[2].setComponents(c+o,m+g,u+S,A+w).normalize(),s[3].setComponents(c-o,m-g,u-S,A-w).normalize(),n)s[4].setComponents(l,d,p,E).normalize(),s[5].setComponents(c-l,m-d,u-p,A-E).normalize();else if(s[4].setComponents(c-l,m-d,u-p,A-E).normalize(),t===en)s[5].setComponents(c+l,m+d,u+p,A+E).normalize();else if(t===Ni)s[5].setComponents(l,d,p,E).normalize();else throw new Error("THREE.Frustum.setFromProjectionMatrix(): Invalid coordinate system: "+t);return this}intersectsObject(e){if(e.boundingSphere!==void 0)e.boundingSphere===null&&e.computeBoundingSphere(),ai.copy(e.boundingSphere).applyMatrix4(e.matrixWorld);else{let t=e.geometry;t.boundingSphere===null&&t.computeBoundingSphere(),ai.copy(t.boundingSphere).applyMatrix4(e.matrixWorld)}return this.intersectsSphere(ai)}intersectsSprite(e){ai.center.set(0,0,0);let t=A1.distanceTo(e.center);return ai.radius=.7071067811865476+t,ai.applyMatrix4(e.matrixWorld),this.intersectsSphere(ai)}intersectsSphere(e){let t=this.planes,n=e.center,s=-e.radius;for(let r=0;r<6;r++)if(t[r].distanceToPoint(n)<s)return!1;return!0}intersectsBox(e){let t=this.planes;for(let n=0;n<6;n++){let s=t[n];if(or.x=s.normal.x>0?e.max.x:e.min.x,or.y=s.normal.y>0?e.max.y:e.min.y,or.z=s.normal.z>0?e.max.z:e.min.z,s.distanceToPoint(or)<0)return!1}return!0}containsPoint(e){let t=this.planes;for(let n=0;n<6;n++)if(t[n].distanceToPoint(e)<0)return!1;return!0}clone(){return new this.constructor().copy(this)}},tc=new nt,Cr=class i{constructor(){this.coordinateSystem=en,this._frustums=[],this._count=0}setFromArrayCamera(e){let t=e.cameras,n=this._frustums;for(let s=0;s<t.length;s++){let r=t[s];tc.multiplyMatrices(r.projectionMatrix,r.matrixWorldInverse),n[s]===void 0&&(n[s]=new qn),n[s].setFromProjectionMatrix(tc,r.coordinateSystem,r.reversedDepth)}return this._count=t.length,this}getFrustum(e){return this._frustums[e]}intersectsObject(e){let t=this._frustums;for(let n=0;n<this._count;n++)if(t[n].intersectsObject(e))return!0;return!1}intersectsSprite(e){let t=this._frustums;for(let n=0;n<this._count;n++)if(t[n].intersectsSprite(e))return!0;return!1}intersectsSphere(e){let t=this._frustums;for(let n=0;n<this._count;n++)if(t[n].intersectsSphere(e))return!0;return!1}intersectsBox(e){let t=this._frustums;for(let n=0;n<this._count;n++)if(t[n].intersectsBox(e))return!0;return!1}containsPoint(e){let t=this._frustums;for(let n=0;n<this._count;n++)if(t[n].containsPoint(e))return!0;return!1}copy(e){this.coordinateSystem=e.coordinateSystem;let t=this._frustums,n=e._frustums;for(let s=0;s<e._count;s++)t[s]===void 0&&(t[s]=new qn),t[s].copy(n[s]);return this._count=e._count,this}clone(){return new i().copy(this)}};var ci=class extends In{constructor(e){super(),this.isLineBasicMaterial=!0,this.type="LineBasicMaterial",this.color=new Be(16777215),this.map=null,this.linewidth=1,this.linecap="round",this.linejoin="round",this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.map=e.map,this.linewidth=e.linewidth,this.linecap=e.linecap,this.linejoin=e.linejoin,this.fog=e.fog,this}},Pr=new U,Ir=new U,nc=new nt,ns=new Xn,lr=new oi,po=new U,ic=new U,ki=class extends Pt{constructor(e=new kt,t=new ci){super(),this.isLine=!0,this.type="Line",this.geometry=e,this.material=t,this.morphTargetDictionary=void 0,this.morphTargetInfluences=void 0,this.updateMorphTargets()}copy(e,t){return super.copy(e,t),e.morphTargetInfluences!==void 0?this.morphTargetInfluences=e.morphTargetInfluences.slice():this.morphTargetInfluences=void 0,e.morphTargetDictionary!==void 0?this.morphTargetDictionary=Object.assign({},e.morphTargetDictionary):this.morphTargetDictionary=void 0,this.material=Array.isArray(e.material)?e.material.slice():e.material,this.geometry=e.geometry,this}computeLineDistances(){let e=this.geometry;if(e.index===null){let t=e.attributes.position,n=[0];for(let s=1,r=t.count;s<r;s++)Pr.fromBufferAttribute(t,s-1),Ir.fromBufferAttribute(t,s),n[s]=n[s-1],n[s]+=Pr.distanceTo(Ir);e.setAttribute("lineDistance",new ct(n,1))}else Te("Line.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}intersectsFrustum(e){return e.intersectsObject(this)}raycast(e,t){let n=this.geometry,s=this.matrixWorld,r=e.params.Line.threshold,a=n.drawRange;if(n.boundingSphere===null&&n.computeBoundingSphere(),lr.copy(n.boundingSphere),lr.applyMatrix4(s),lr.radius+=r,e.ray.intersectsSphere(lr)===!1)return;nc.copy(s).invert(),ns.copy(e.ray).applyMatrix4(nc);let o=r/((this.scale.x+this.scale.y+this.scale.z)/3),l=o*o,c=this.isLineSegments?2:1,h=n.index,d=n.attributes.position;if(h!==null){let m=Math.max(0,a.start),_=Math.min(h.count,a.start+a.count);for(let S=m,p=_-1;S<p;S+=c){let u=h.getX(S),M=h.getX(S+1),w=cr(this,e,ns,l,u,M,S);w&&t.push(w)}if(this.isLineLoop){let S=h.getX(_-1),p=h.getX(m),u=cr(this,e,ns,l,S,p,_-1);u&&t.push(u)}}else{let m=Math.max(0,a.start),_=Math.min(d.count,a.start+a.count);for(let S=m,p=_-1;S<p;S+=c){let u=cr(this,e,ns,l,S,S+1,S);u&&t.push(u)}if(this.isLineLoop){let S=cr(this,e,ns,l,_-1,m,_-1);S&&t.push(S)}}}updateMorphTargets(){let t=this.geometry.morphAttributes,n=Object.keys(t);if(n.length>0){let s=t[n[0]];if(s!==void 0){this.morphTargetInfluences=[],this.morphTargetDictionary={};for(let r=0,a=s.length;r<a;r++){let o=s[r].name||String(r);this.morphTargetInfluences.push(0),this.morphTargetDictionary[o]=r}}}}};function cr(i,e,t,n,s,r,a){let o=i.geometry.attributes.position;if(Pr.fromBufferAttribute(o,s),Ir.fromBufferAttribute(o,r),t.distanceSqToSegment(Pr,Ir,po,ic)>n)return;po.applyMatrix4(i.matrixWorld);let c=e.ray.origin.distanceTo(po);if(!(c<e.near||c>e.far))return{distance:c,point:ic.clone().applyMatrix4(i.matrixWorld),index:a,face:null,faceIndex:null,barycoord:null,object:i}}var sc=new U,rc=new U,ps=class extends ki{constructor(e,t){super(e,t),this.isLineSegments=!0,this.type="LineSegments"}computeLineDistances(){let e=this.geometry;if(e.index===null){let t=e.attributes.position,n=[];for(let s=0,r=t.count;s<r;s+=2)sc.fromBufferAttribute(t,s),rc.fromBufferAttribute(t,s+1),n[s]=s===0?0:n[s-1],n[s+1]=n[s]+sc.distanceTo(rc);e.setAttribute("lineDistance",new ct(n,1))}else Te("LineSegments.computeLineDistances(): Computation only possible with non-indexed BufferGeometry.");return this}};var ms=class extends zt{constructor(e=[],t=fi,n,s,r,a,o,l,c,h){super(e,t,n,s,r,a,o,l,c,h),this.isCubeTexture=!0,this.flipY=!1}get images(){return this.image}set images(e){this.image=e}};var Ln=class extends zt{constructor(e,t,n=cn,s,r,a,o=Mt,l=Mt,c,h=Cn,g=1){if(h!==Cn&&h!==Nn)throw new Error("THREE.DepthTexture: format must be either THREE.DepthFormat or THREE.DepthStencilFormat");let d={width:e,height:t,depth:g};super(d,s,r,a,o,l,h,n,c),this.isDepthTexture=!0,this.flipY=!1,this.generateMipmaps=!1,this.compareFunction=null}copy(e){return super.copy(e),this.source=new Oi(Object.assign({},e.image)),this.compareFunction=e.compareFunction,this}toJSON(e){let t=super.toJSON(e);return t.compareFunction=this.compareFunction,t}},gs=class extends Ln{constructor(e,t=cn,n=fi,s,r,a=Mt,o=Mt,l,c=Cn){let h={width:e,height:e,depth:1},g=[h,h,h,h,h,h];super(e,e,t,n,s,r,a,o,l,c),this.image=g,this.isCubeDepthTexture=!0,this.isCubeTexture=!0}get images(){return this.image}set images(e){this.image=e}},_s=class extends zt{constructor(e=null){super(),this.sourceTexture=e,this.isExternalTexture=!0}copy(e){return super.copy(e),this.sourceTexture=e.sourceTexture,this}},Gi=class i extends kt{constructor(e=1,t=1,n=1,s=1,r=1,a=1){super(),this.type="BoxGeometry",this.parameters={width:e,height:t,depth:n,widthSegments:s,heightSegments:r,depthSegments:a};let o=this;s=Math.floor(s),r=Math.floor(r),a=Math.floor(a);let l=[],c=[],h=[],g=[],d=0,m=0;_("z","y","x",-1,-1,n,t,e,a,r,0),_("z","y","x",1,-1,n,t,-e,a,r,1),_("x","z","y",1,1,e,n,t,s,a,2),_("x","z","y",1,-1,e,n,-t,s,a,3),_("x","y","z",1,-1,e,t,n,s,r,4),_("x","y","z",-1,-1,e,t,-n,s,r,5),this.setIndex(l),this.setAttribute("position",new ct(c,3)),this.setAttribute("normal",new ct(h,3)),this.setAttribute("uv",new ct(g,2));function _(S,p,u,M,w,E,A,T,f,v,N){let I=E/f,D=A/v,z=E/2,q=A/2,P=T/2,W=f+1,$=v+1,G=0,te=0,H=new U;for(let j=0;j<$;j++){let Q=j*D-q;for(let Se=0;Se<W;Se++){let De=Se*I-z;H[S]=De*M,H[p]=Q*w,H[u]=P,c.push(H.x,H.y,H.z),H[S]=0,H[p]=0,H[u]=T>0?1:-1,h.push(H.x,H.y,H.z),g.push(Se/f),g.push(1-j/v),G+=1}}for(let j=0;j<v;j++)for(let Q=0;Q<f;Q++){let Se=d+Q+W*j,De=d+Q+W*(j+1),Z=d+(Q+1)+W*(j+1),pe=d+(Q+1)+W*j;l.push(Se,De,pe),l.push(De,Z,pe),te+=6}o.addGroup(m,te,N),m+=te,d+=G}}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new i(e.width,e.height,e.depth,e.widthSegments,e.heightSegments,e.depthSegments)}};var xs=class i extends kt{constructor(e=1,t=1,n=1,s=1){super(),this.type="PlaneGeometry",this.parameters={width:e,height:t,widthSegments:n,heightSegments:s};let r=e/2,a=t/2,o=Math.floor(n),l=Math.floor(s),c=o+1,h=l+1,g=e/o,d=t/l,m=[],_=[],S=[],p=[];for(let u=0;u<h;u++){let M=u*d-a;for(let w=0;w<c;w++){let E=w*g-r;_.push(E,-M,0),S.push(0,0,1),p.push(w/o),p.push(1-u/l)}}for(let u=0;u<l;u++)for(let M=0;M<o;M++){let w=M+c*u,E=M+c*(u+1),A=M+1+c*(u+1),T=M+1+c*u;m.push(w,E,T),m.push(E,A,T)}this.setIndex(m),this.setAttribute("position",new ct(_,3)),this.setAttribute("normal",new ct(S,3)),this.setAttribute("uv",new ct(p,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new i(e.width,e.height,e.widthSegments,e.heightSegments)}},ys=class i extends kt{constructor(e=.5,t=1,n=32,s=1,r=0,a=Math.PI*2){super(),this.type="RingGeometry",this.parameters={innerRadius:e,outerRadius:t,thetaSegments:n,phiSegments:s,thetaStart:r,thetaLength:a},n=Math.max(3,n),s=Math.max(1,s);let o=[],l=[],c=[],h=[],g=e,d=(t-e)/s,m=new U,_=new Re;for(let S=0;S<=s;S++){for(let p=0;p<=n;p++){let u=r+p/n*a;m.x=g*Math.cos(u),m.y=g*Math.sin(u),l.push(m.x,m.y,m.z),c.push(0,0,1),_.x=(m.x/t+1)/2,_.y=(m.y/t+1)/2,h.push(_.x,_.y)}g+=d}for(let S=0;S<s;S++){let p=S*(n+1);for(let u=0;u<n;u++){let M=u+p,w=M,E=M+n+1,A=M+n+2,T=M+1;o.push(w,E,T),o.push(E,A,T)}}this.setIndex(o),this.setAttribute("position",new ct(l,3)),this.setAttribute("normal",new ct(c,3)),this.setAttribute("uv",new ct(h,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new i(e.innerRadius,e.outerRadius,e.thetaSegments,e.phiSegments,e.thetaStart,e.thetaLength)}};var hi=class i extends kt{constructor(e=1,t=32,n=16,s=0,r=Math.PI*2,a=0,o=Math.PI){super(),this.type="SphereGeometry",this.parameters={radius:e,widthSegments:t,heightSegments:n,phiStart:s,phiLength:r,thetaStart:a,thetaLength:o},t=Math.max(3,Math.floor(t)),n=Math.max(2,Math.floor(n));let l=Math.min(a+o,Math.PI),c=0,h=[],g=new U,d=new U,m=[],_=[],S=[],p=[];for(let u=0;u<=n;u++){let M=[],w=u/n,E=a+w*o,A=e*Math.cos(E),T=Math.sqrt(e*e-A*A),f=0;u===0&&a===0?f=.5/t:u===n&&l===Math.PI&&(f=-.5/t);for(let v=0;v<=t;v++){let N=v/t,I=s+N*r;g.x=-T*Math.cos(I),g.y=A,g.z=T*Math.sin(I),_.push(g.x,g.y,g.z),d.copy(g).normalize(),S.push(d.x,d.y,d.z),p.push(N+f,1-w),M.push(c++)}h.push(M)}for(let u=0;u<n;u++)for(let M=0;M<t;M++){let w=h[u][M+1],E=h[u][M],A=h[u+1][M],T=h[u+1][M+1];(u!==0||a>0)&&m.push(w,E,T),(u!==n-1||l<Math.PI)&&m.push(E,A,T)}this.setIndex(m),this.setAttribute("position",new ct(_,3)),this.setAttribute("normal",new ct(S,3)),this.setAttribute("uv",new ct(p,2))}copy(e){return super.copy(e),this.parameters=Object.assign({},e.parameters),this}static fromJSON(e){return new i(e.radius,e.widthSegments,e.heightSegments,e.phiStart,e.phiLength,e.thetaStart,e.thetaLength)}};function mi(i){let e={};for(let t in i){e[t]={};for(let n in i[t]){let s=i[t][n];if(ac(s))s.isRenderTargetTexture?(Te("UniformsUtils: Textures of render targets cannot be cloned via cloneUniforms() or mergeUniforms()."),e[t][n]=null):e[t][n]=s.clone();else if(Array.isArray(s))if(ac(s[0])){let r=[];for(let a=0,o=s.length;a<o;a++)r[a]=s[a].clone();e[t][n]=r}else e[t][n]=s.slice();else e[t][n]=s}}return e}function It(i){let e={};for(let t=0;t<i.length;t++){let n=mi(i[t]);for(let s in n)e[s]=n[s]}return e}function ac(i){return i&&(i.isColor||i.isMatrix3||i.isMatrix4||i.isVector2||i.isVector3||i.isVector4||i.isTexture||i.isQuaternion)}function w1(i){let e=[];for(let t=0;t<i.length;t++)e.push(i[t].clone());return e}function el(i){let e=i.getRenderTarget();return e===null?i.outputColorSpace:e.isXRRenderTarget===!0?e.texture.colorSpace:We.workingColorSpace}var th={clone:mi,merge:It},R1=`void main() {
	gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
}`,C1=`void main() {
	gl_FragColor = vec4( 1.0, 0.0, 0.0, 1.0 );
}`,tn=class extends In{constructor(e){super(),this.isShaderMaterial=!0,this.type="ShaderMaterial",this.defines={},this.uniforms={},this.uniformsGroups=[],this.vertexShader=R1,this.fragmentShader=C1,this.linewidth=1,this.wireframe=!1,this.wireframeLinewidth=1,this.fog=!1,this.lights=!1,this.clipping=!1,this.forceSinglePass=!0,this.extensions={clipCullDistance:!1,multiDraw:!1},this.defaultAttributeValues={color:[1,1,1],uv:[0,0],uv1:[0,0]},this.index0AttributeName=void 0,this.uniformsNeedUpdate=!1,this.glslVersion=null,e!==void 0&&this.setValues(e)}copy(e){return super.copy(e),this.fragmentShader=e.fragmentShader,this.vertexShader=e.vertexShader,this.uniforms=mi(e.uniforms),this.uniformsGroups=w1(e.uniformsGroups),this.defines=Object.assign({},e.defines),this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.fog=e.fog,this.lights=e.lights,this.clipping=e.clipping,this.extensions=Object.assign({},e.extensions),this.glslVersion=e.glslVersion,this.defaultAttributeValues=Object.assign({},e.defaultAttributeValues),this.index0AttributeName=e.index0AttributeName,this.uniformsNeedUpdate=e.uniformsNeedUpdate,this}toJSON(e){let t=super.toJSON(e);t.glslVersion=this.glslVersion,t.uniforms={};for(let s in this.uniforms){let a=this.uniforms[s].value;a&&a.isTexture?t.uniforms[s]={type:"t",value:a.toJSON(e).uuid}:a&&a.isColor?t.uniforms[s]={type:"c",value:a.getHex()}:a&&a.isVector2?t.uniforms[s]={type:"v2",value:a.toArray()}:a&&a.isVector3?t.uniforms[s]={type:"v3",value:a.toArray()}:a&&a.isVector4?t.uniforms[s]={type:"v4",value:a.toArray()}:a&&a.isMatrix3?t.uniforms[s]={type:"m3",value:a.toArray()}:a&&a.isMatrix4?t.uniforms[s]={type:"m4",value:a.toArray()}:t.uniforms[s]={value:a}}Object.keys(this.defines).length>0&&(t.defines=this.defines),t.vertexShader=this.vertexShader,t.fragmentShader=this.fragmentShader,t.lights=this.lights,t.clipping=this.clipping;let n={};for(let s in this.extensions)this.extensions[s]===!0&&(n[s]=!0);return Object.keys(n).length>0&&(t.extensions=n),t}fromJSON(e,t){if(super.fromJSON(e,t),e.uniforms!==void 0)for(let n in e.uniforms){let s=e.uniforms[n];switch(this.uniforms[n]={},s.type){case"t":this.uniforms[n].value=t[s.value]||null;break;case"c":this.uniforms[n].value=new Be().setHex(s.value);break;case"v2":this.uniforms[n].value=new Re().fromArray(s.value);break;case"v3":this.uniforms[n].value=new U().fromArray(s.value);break;case"v4":this.uniforms[n].value=new at().fromArray(s.value);break;case"m3":this.uniforms[n].value=new Ie().fromArray(s.value);break;case"m4":this.uniforms[n].value=new nt().fromArray(s.value);break;default:this.uniforms[n].value=s.value}}if(e.defines!==void 0&&(this.defines=e.defines),e.vertexShader!==void 0&&(this.vertexShader=e.vertexShader),e.fragmentShader!==void 0&&(this.fragmentShader=e.fragmentShader),e.glslVersion!==void 0&&(this.glslVersion=e.glslVersion),e.extensions!==void 0)for(let n in e.extensions)this.extensions[n]=e.extensions[n];return e.lights!==void 0&&(this.lights=e.lights),e.clipping!==void 0&&(this.clipping=e.clipping),this}},Lr=class extends tn{constructor(e){super(e),this.isRawShaderMaterial=!0,this.type="RawShaderMaterial"}};var vs=class extends In{constructor(e){super(),this.isMeshPhongMaterial=!0,this.type="MeshPhongMaterial",this.color=new Be(16777215),this.specular=new Be(1118481),this.shininess=30,this.map=null,this.lightMap=null,this.lightMapIntensity=1,this.aoMap=null,this.aoMapIntensity=1,this.emissive=new Be(0),this.emissiveIntensity=1,this.emissiveMap=null,this.bumpMap=null,this.bumpScale=1,this.normalMap=null,this.normalMapType=Na,this.normalScale=new Re(1,1),this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.specularMap=null,this.alphaMap=null,this.envMap=null,this.envMapRotation=new Pn,this.combine=Zr,this.reflectivity=1,this.envMapIntensity=1,this.refractionRatio=.98,this.wireframe=!1,this.wireframeLinewidth=1,this.wireframeLinecap="round",this.wireframeLinejoin="round",this.flatShading=!1,this.fog=!0,this.setValues(e)}copy(e){return super.copy(e),this.color.copy(e.color),this.specular.copy(e.specular),this.shininess=e.shininess,this.map=e.map,this.lightMap=e.lightMap,this.lightMapIntensity=e.lightMapIntensity,this.aoMap=e.aoMap,this.aoMapIntensity=e.aoMapIntensity,this.emissive.copy(e.emissive),this.emissiveMap=e.emissiveMap,this.emissiveIntensity=e.emissiveIntensity,this.bumpMap=e.bumpMap,this.bumpScale=e.bumpScale,this.normalMap=e.normalMap,this.normalMapType=e.normalMapType,this.normalScale.copy(e.normalScale),this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this.specularMap=e.specularMap,this.alphaMap=e.alphaMap,this.envMap=e.envMap,this.envMapRotation.copy(e.envMapRotation),this.combine=e.combine,this.reflectivity=e.reflectivity,this.envMapIntensity=e.envMapIntensity,this.refractionRatio=e.refractionRatio,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this.wireframeLinecap=e.wireframeLinecap,this.wireframeLinejoin=e.wireframeLinejoin,this.flatShading=e.flatShading,this.fog=e.fog,this}};var Dr=class extends In{constructor(e){super(),this.isMeshDepthMaterial=!0,this.type="MeshDepthMaterial",this.depthPacking=zc,this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.wireframe=!1,this.wireframeLinewidth=1,this.setValues(e)}copy(e){return super.copy(e),this.depthPacking=e.depthPacking,this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this.wireframe=e.wireframe,this.wireframeLinewidth=e.wireframeLinewidth,this}},Nr=class extends In{constructor(e){super(),this.isMeshDistanceMaterial=!0,this.type="MeshDistanceMaterial",this.map=null,this.alphaMap=null,this.displacementMap=null,this.displacementScale=1,this.displacementBias=0,this.setValues(e)}copy(e){return super.copy(e),this.map=e.map,this.alphaMap=e.alphaMap,this.displacementMap=e.displacementMap,this.displacementScale=e.displacementScale,this.displacementBias=e.displacementBias,this}};function Ci(i,e){return!i||i.constructor===e?i:typeof e.BYTES_PER_ELEMENT=="number"?new e(i):Array.prototype.slice.call(i)}function hr(i){return i!==void 0&&i.inTangents!==void 0&&i.outTangents!==void 0}var Yn=class{constructor(e,t,n,s){this.parameterPositions=e,this._cachedIndex=0,this.resultBuffer=s!==void 0?s:new t.constructor(n),this.sampleValues=t,this.valueSize=n,this.settings=null,this.DefaultSettings_={}}evaluate(e){let t=this.parameterPositions,n=this._cachedIndex,s=t[n],r=t[n-1];n:{e:{let a;t:{i:if(!(e<s)){for(let o=n+2;;){if(s===void 0){if(e<r)break i;return n=t.length,this._cachedIndex=n,this.copySampleValue_(n-1)}if(n===o)break;if(r=s,s=t[++n],e<s)break e}a=t.length;break t}if(!(e>=r)){let o=t[1];e<o&&(n=2,r=o);for(let l=n-2;;){if(r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(n===l)break;if(s=r,r=t[--n-1],e>=r)break e}a=n,n=0;break t}break n}for(;n<a;){let o=n+a>>>1;e<t[o]?a=o:n=o+1}if(s=t[n],r=t[n-1],r===void 0)return this._cachedIndex=0,this.copySampleValue_(0);if(s===void 0)return n=t.length,this._cachedIndex=n,this.copySampleValue_(n-1)}this._cachedIndex=n,this.intervalChanged_(n,r,s)}return this.interpolate_(n,r,e,s)}getSettings_(){return this.settings||this.DefaultSettings_}copySampleValue_(e){let t=this.resultBuffer,n=this.sampleValues,s=this.valueSize,r=e*s;for(let a=0;a!==s;++a)t[a]=n[r+a];return t}interpolate_(){throw new Error("THREE.Interpolant: Call to abstract method.")}intervalChanged_(){}},Ur=class extends Yn{constructor(e,t,n,s){super(e,t,n,s),this._weightPrev=-0,this._offsetPrev=-0,this._weightNext=-0,this._offsetNext=-0,this.DefaultSettings_={endingStart:_o,endingEnd:_o}}intervalChanged_(e,t,n){let s=this.parameterPositions,r=e-2,a=e+1,o=s[r],l=s[a];if(o===void 0)switch(this.getSettings_().endingStart){case xo:r=e,o=2*t-n;break;case yo:r=s.length-2,o=t+s[r]-s[r+1];break;default:r=e,o=n}if(l===void 0)switch(this.getSettings_().endingEnd){case xo:a=e,l=2*n-t;break;case yo:a=1,l=n+s[1]-s[0];break;default:a=e-1,l=t}let c=(n-t)*.5,h=this.valueSize;this._weightPrev=c/(t-o),this._weightNext=c/(l-n),this._offsetPrev=r*h,this._offsetNext=a*h}interpolate_(e,t,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=e*o,c=l-o,h=this._offsetPrev,g=this._offsetNext,d=this._weightPrev,m=this._weightNext,_=(n-t)/(s-t),S=_*_,p=S*_,u=-d*p+2*d*S-d*_,M=(1+d)*p+(-1.5-2*d)*S+(-.5+d)*_+1,w=(-1-m)*p+(1.5+m)*S+.5*_,E=m*p-m*S;for(let A=0;A!==o;++A)r[A]=u*a[h+A]+M*a[c+A]+w*a[l+A]+E*a[g+A];return r}},Fr=class extends Yn{constructor(e,t,n,s){super(e,t,n,s)}interpolate_(e,t,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=e*o,c=l-o,h=(n-t)/(s-t),g=1-h;for(let d=0;d!==o;++d)r[d]=a[c+d]*g+a[l+d]*h;return r}},Or=class extends Yn{constructor(e,t,n,s){super(e,t,n,s)}interpolate_(e){return this.copySampleValue_(e-1)}},Br=class extends Yn{interpolate_(e,t,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=e*o,c=l-o,h=this.inTangents,g=this.outTangents;if(!h||!g){let _=(n-t)/(s-t),S=1-_;for(let p=0;p!==o;++p)r[p]=a[c+p]*S+a[l+p]*_;return r}let d=o*2,m=e-1;for(let _=0;_!==o;++_){let S=a[c+_],p=a[l+_],u=m*d+_*2,M=g[u],w=g[u+1],E=e*d+_*2,A=h[E],T=h[E+1],f=I1(n,t,M,A,s);r[_]=nh(f,S,w,T,p)}return r}};function nh(i,e,t,n,s){let r=1-i;return r*r*r*e+3*r*r*i*t+3*r*i*i*n+i*i*i*s}function P1(i,e,t,n,s){let r=1-i;return 3*r*r*(t-e)+6*r*i*(n-t)+3*i*i*(s-n)}function I1(i,e,t,n,s){let r=(i-e)/(s-e);for(let a=0;a<8;a++){let o=nh(r,e,t,n,s)-i;if(Math.abs(o)<1e-10)break;let l=P1(r,e,t,n,s);if(Math.abs(l)<1e-10)break;r=Math.max(0,Math.min(1,r-o/l))}return r}var Zt=class{constructor(e,t,n,s){if(e===void 0)throw new Error("THREE.KeyframeTrack: track name is undefined");if(t===void 0||t.length===0)throw new Error("THREE.KeyframeTrack: no keyframes in track named "+e);this.name=e,this.times=Ci(t,this.TimeBufferType),this.values=Ci(n,this.ValueBufferType),this.setInterpolation(s||this.DefaultInterpolation)}static toJSON(e){let t=e.constructor,n;if(t.toJSON!==this.toJSON)n=t.toJSON(e);else{n={name:e.name,times:Ci(e.times,Array),values:Ci(e.values,Array)};let s=e.getInterpolation();s!==e.DefaultInterpolation&&(n.interpolation=s),hr(e.settings)&&(n.settings={inTangents:Ci(e.settings.inTangents,Array),outTangents:Ci(e.settings.outTangents,Array)})}return n.type=e.ValueTypeName,n}InterpolantFactoryMethodDiscrete(e){return new Or(this.times,this.values,this.getValueSize(),e)}InterpolantFactoryMethodLinear(e){return new Fr(this.times,this.values,this.getValueSize(),e)}InterpolantFactoryMethodSmooth(e){return new Ur(this.times,this.values,this.getValueSize(),e)}InterpolantFactoryMethodBezier(e){let t=new Br(this.times,this.values,this.getValueSize(),e);return this.settings&&(t.inTangents=this.settings.inTangents,t.outTangents=this.settings.outTangents),t}setInterpolation(e){let t;switch(e){case as:t=this.InterpolantFactoryMethodDiscrete;break;case Er:t=this.InterpolantFactoryMethodLinear;break;case fr:t=this.InterpolantFactoryMethodSmooth;break;case go:t=this.InterpolantFactoryMethodBezier;break}if(t===void 0){let n="unsupported interpolation for "+this.ValueTypeName+" keyframe track named "+this.name;if(this.createInterpolant===void 0)if(e!==this.DefaultInterpolation)this.setInterpolation(this.DefaultInterpolation);else throw new Error(n);return Te("KeyframeTrack:",n),this}return this.createInterpolant=t,this}getInterpolation(){switch(this.createInterpolant){case this.InterpolantFactoryMethodDiscrete:return as;case this.InterpolantFactoryMethodLinear:return Er;case this.InterpolantFactoryMethodSmooth:return fr;case this.InterpolantFactoryMethodBezier:return go}}getValueSize(){return this.values.length/this.times.length}shift(e){if(e!==0){let t=this.times;for(let n=0,s=t.length;n!==s;++n)t[n]+=e;hr(this.settings)&&(oc(this.settings.inTangents,e),oc(this.settings.outTangents,e))}return this}scale(e){if(e!==1){let t=this.times;for(let n=0,s=t.length;n!==s;++n)t[n]*=e;hr(this.settings)&&(lc(this.settings.inTangents,e),lc(this.settings.outTangents,e))}return this}trim(e,t){let n=this.times,s=n.length,r=0,a=s-1;for(;r!==s&&n[r]<e;)++r;for(;a!==-1&&n[a]>t;)--a;if(++a,r!==0||a!==s){r>=a&&(a=Math.max(a,1),r=a-1);let o=this.getValueSize();this.times=n.slice(r,a),this.values=this.values.slice(r*o,a*o)}return this}validate(){let e=!0,t=this.getValueSize();t-Math.floor(t)!==0&&(Pe("KeyframeTrack: Invalid value size in track.",this),e=!1);let n=this.times,s=this.values,r=n.length;r===0&&(Pe("KeyframeTrack: Track is empty.",this),e=!1);let a=null;for(let o=0;o!==r;o++){let l=n[o];if(typeof l=="number"&&isNaN(l)){Pe("KeyframeTrack: Time is not a valid number.",this,o,l),e=!1;break}if(a!==null&&a>l){Pe("KeyframeTrack: Out of order keys.",this,o,l,a),e=!1;break}a=l}if(s!==void 0&&Yh(s))for(let o=0,l=s.length;o!==l;++o){let c=s[o];if(isNaN(c)){Pe("KeyframeTrack: Value is not a valid number.",this,o,c),e=!1;break}}return e}optimize(){let e=this.times.slice(),t=this.values.slice(),n=this.getValueSize(),s=this.getInterpolation()===fr,r=e.length-1,a=1;for(let o=1;o<r;++o){let l=!1,c=e[o],h=e[o+1];if(c!==h&&(o!==1||c!==e[0]))if(s)l=!0;else{let g=o*n,d=g-n,m=g+n;for(let _=0;_!==n;++_){let S=t[g+_];if(S!==t[d+_]||S!==t[m+_]){l=!0;break}}}if(l){if(o!==a){e[a]=e[o];let g=o*n,d=a*n;for(let m=0;m!==n;++m)t[d+m]=t[g+m]}++a}}if(r>0){e[a]=e[r];for(let o=r*n,l=a*n,c=0;c!==n;++c)t[l+c]=t[o+c];++a}return a!==e.length?(this.times=e.slice(0,a),this.values=t.slice(0,a*n)):(this.times=e,this.values=t),this}clone(){let e=this.times.slice(),t=this.values.slice(),n=this.constructor,s=new n(this.name,e,t);return s.createInterpolant=this.createInterpolant,hr(this.settings)&&(s.settings={inTangents:this.settings.inTangents.slice(),outTangents:this.settings.outTangents.slice()}),s}};function oc(i,e){for(let t=0,n=i.length;t!==n;t+=2)i[t]+=e}function lc(i,e){for(let t=0,n=i.length;t!==n;t+=2)i[t]*=e}Zt.prototype.ValueTypeName="";Zt.prototype.TimeBufferType=Float32Array;Zt.prototype.ValueBufferType=Float32Array;Zt.prototype.DefaultInterpolation=Er;var Zn=class extends Zt{constructor(e,t,n){super(e,t,n)}};Zn.prototype.ValueTypeName="bool";Zn.prototype.ValueBufferType=Array;Zn.prototype.DefaultInterpolation=as;Zn.prototype.InterpolantFactoryMethodLinear=void 0;Zn.prototype.InterpolantFactoryMethodSmooth=void 0;var zr=class extends Zt{constructor(e,t,n,s){super(e,t,n,s)}};zr.prototype.ValueTypeName="color";var kr=class extends Zt{constructor(e,t,n,s){super(e,t,n,s)}};kr.prototype.ValueTypeName="number";var Gr=class extends Yn{constructor(e,t,n,s){super(e,t,n,s)}interpolate_(e,t,n,s){let r=this.resultBuffer,a=this.sampleValues,o=this.valueSize,l=(n-t)/(s-t),c=e*o;for(let h=c+o;c!==h;c+=4)qt.slerpFlat(r,0,a,c-o,a,c,l);return r}},Ss=class extends Zt{constructor(e,t,n,s){super(e,t,n,s)}InterpolantFactoryMethodLinear(e){return new Gr(this.times,this.values,this.getValueSize(),e)}};Ss.prototype.ValueTypeName="quaternion";Ss.prototype.InterpolantFactoryMethodSmooth=void 0;var Jn=class extends Zt{constructor(e,t,n){super(e,t,n)}};Jn.prototype.ValueTypeName="string";Jn.prototype.ValueBufferType=Array;Jn.prototype.DefaultInterpolation=as;Jn.prototype.InterpolantFactoryMethodLinear=void 0;Jn.prototype.InterpolantFactoryMethodSmooth=void 0;var Vr=class extends Zt{constructor(e,t,n,s){super(e,t,n,s)}};Vr.prototype.ValueTypeName="vector";var Hr=class{constructor(e,t,n){let s=this,r=!1,a=0,o=0,l,c=[];this.onStart=void 0,this.onLoad=e,this.onProgress=t,this.onError=n,this._abortController=null,this.itemStart=function(h){o++,r===!1&&s.onStart!==void 0&&s.onStart(h,a,o),r=!0},this.itemEnd=function(h){a++,s.onProgress!==void 0&&s.onProgress(h,a,o),a===o&&(r=!1,s.onLoad!==void 0&&s.onLoad())},this.itemError=function(h){s.onError!==void 0&&s.onError(h)},this.resolveURL=function(h){return h=h.normalize("NFC"),l?l(h):h},this.setURLModifier=function(h){return l=h,this},this.addHandler=function(h,g){return c.push(h,g),this},this.removeHandler=function(h){let g=c.indexOf(h);return g!==-1&&c.splice(g,2),this},this.getHandler=function(h){for(let g=0,d=c.length;g<d;g+=2){let m=c[g],_=c[g+1];if(m.global&&(m.lastIndex=0),m.test(h))return _}return null},this.abort=function(){return this.abortController.abort(),this._abortController=null,this}}get abortController(){return this._abortController||(this._abortController=new AbortController),this._abortController}},ih=new Hr,Wr=class{constructor(e){this.manager=e!==void 0?e:ih,this.crossOrigin="anonymous",this.withCredentials=!1,this.path="",this.resourcePath="",this.requestHeader={},this.priority="auto",this.cache="default",typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}load(){}loadAsync(e,t){let n=this;return new Promise(function(s,r){n.load(e,s,t,r)})}parse(){}setCrossOrigin(e){return this.crossOrigin=e,this}setWithCredentials(e){return this.withCredentials=e,this}setPath(e){return this.path=e,this}setResourcePath(e){return this.resourcePath=e,this}setRequestHeader(e){return this.requestHeader=e,this}setPriority(e){return this.priority=e,this}setCache(e){return this.cache=e,this}abort(){return this}};Wr.DEFAULT_MATERIAL_NAME="__DEFAULT";var Ms=class extends Pt{static registerNode(e){this.prototype._lightNode=e}constructor(e,t=1){super(),this.isLight=!0,this.type="Light",this.color=new Be(e),this.intensity=t}copy(e,t){return super.copy(e,t),this.color.copy(e.color),this.intensity=e.intensity,this}toJSON(e){let t=super.toJSON(e);return t.object.color=this.color.getHex(),t.object.intensity=this.intensity,t}};var mo=new nt,cc=new U,hc=new U,Xr=class{constructor(e){this.camera=e,this.intensity=1,this.bias=0,this.biasNode=null,this.normalBias=0,this.radius=1,this.blurSamples=8,this.mapSize=new Re(512,512),this.mapType=Gt,this.map=null,this.mapPass=null,this.matrix=new nt,this.autoUpdate=!0,this.needsUpdate=!1,this._frustum=new qn,this._frameExtents=new Re(1,1),this._viewportCount=1,this._viewports=[new at(0,0,1,1)]}getViewportCount(){return this._viewportCount}getCamera(){return this.camera}getFrustum(){return this._frustum}updateMatrices(e){let t=this.camera;cc.setFromMatrixPosition(e.matrixWorld),t.position.copy(cc),hc.setFromMatrixPosition(e.target.matrixWorld),t.lookAt(hc),t.updateMatrixWorld(),this._updateMatrix(t,this.matrix,this._frustum)}_updateMatrix(e,t,n,s){mo.multiplyMatrices(e.projectionMatrix,e.matrixWorldInverse),n.setFromProjectionMatrix(mo,e.coordinateSystem,e.reversedDepth);let r=this._frameExtents,a=s?s.z/r.x:1,o=s?s.w/r.y:1,l=s?s.x/r.x:0,c=s?s.y/r.y:0;e.coordinateSystem===Ni||e.reversedDepth?t.set(.5*a,0,0,.5*a+l,0,.5*o,0,.5*o+c,0,0,1,0,0,0,0,1):t.set(.5*a,0,0,.5*a+l,0,.5*o,0,.5*o+c,0,0,.5,.5,0,0,0,1),t.multiply(mo)}getViewport(e){return this._viewports[e]}getFrameExtents(){return this._frameExtents}dispose(){this.map&&this.map.dispose(),this.mapPass&&this.mapPass.dispose()}copy(e){return this.camera=e.camera.clone(),this.intensity=e.intensity,this.bias=e.bias,this.radius=e.radius,this.autoUpdate=e.autoUpdate,this.needsUpdate=e.needsUpdate,this.normalBias=e.normalBias,this.blurSamples=e.blurSamples,this.mapSize.copy(e.mapSize),this.mapType=e.mapType,this.biasNode=e.biasNode,this}clone(){return new this.constructor().copy(this)}toJSON(){let e={};return e.intensity=this.intensity,e.bias=this.bias,e.normalBias=this.normalBias,e.radius=this.radius,e.blurSamples=this.blurSamples,e.mapSize=this.mapSize.toArray(),e.mapType=this.mapType,e.camera=this.camera.toJSON(!1).object,delete e.camera.matrix,e}},ur=new U,dr=new qt,mn=new U,bs=class extends Pt{constructor(){super(),this.isCamera=!0,this.type="Camera",this.matrixWorldInverse=new nt,this.projectionMatrix=new nt,this.projectionMatrixInverse=new nt,this.coordinateSystem=en,this._reversedDepth=!1}get reversedDepth(){return this._reversedDepth}copy(e,t){return super.copy(e,t),this.matrixWorldInverse.copy(e.matrixWorldInverse),this.projectionMatrix.copy(e.projectionMatrix),this.projectionMatrixInverse.copy(e.projectionMatrixInverse),this.coordinateSystem=e.coordinateSystem,this}getWorldDirection(e){return super.getWorldDirection(e).negate()}updateMatrixWorld(e){super.updateMatrixWorld(e),this.matrixWorld.decompose(ur,dr,mn),mn.x===1&&mn.y===1&&mn.z===1?this.matrixWorldInverse.copy(this.matrixWorld).invert():this.matrixWorldInverse.compose(ur,dr,mn.set(1,1,1)).invert()}updateWorldMatrix(e,t,n=!1){super.updateWorldMatrix(e,t,n),this.matrixWorld.decompose(ur,dr,mn),mn.x===1&&mn.y===1&&mn.z===1?this.matrixWorldInverse.copy(this.matrixWorld).invert():this.matrixWorldInverse.compose(ur,dr,mn.set(1,1,1)).invert()}clone(){return new this.constructor().copy(this)}},Vn=new U,uc=new Re,dc=new Re,Ut=class extends bs{constructor(e=50,t=1,n=.1,s=2e3){super(),this.isPerspectiveCamera=!0,this.type="PerspectiveCamera",this.fov=e,this.zoom=1,this.near=n,this.far=s,this.focus=10,this.aspect=t,this.view=null,this.filmGauge=35,this.filmOffset=0,this.updateProjectionMatrix()}copy(e,t){return super.copy(e,t),this.fov=e.fov,this.zoom=e.zoom,this.near=e.near,this.far=e.far,this.focus=e.focus,this.aspect=e.aspect,this.view=e.view===null?null:Object.assign({},e.view),this.filmGauge=e.filmGauge,this.filmOffset=e.filmOffset,this}setFocalLength(e){let t=.5*this.getFilmHeight()/e;this.fov=Fi*2*Math.atan(t),this.updateProjectionMatrix()}getFocalLength(){let e=Math.tan(ss*.5*this.fov);return .5*this.getFilmHeight()/e}getEffectiveFOV(){return Fi*2*Math.atan(Math.tan(ss*.5*this.fov)/this.zoom)}getFilmWidth(){return this.filmGauge*Math.min(this.aspect,1)}getFilmHeight(){return this.filmGauge/Math.max(this.aspect,1)}getViewBounds(e,t,n){Vn.set(-1,-1,.5).applyMatrix4(this.projectionMatrixInverse),t.set(Vn.x,Vn.y).multiplyScalar(-e/Vn.z),Vn.set(1,1,.5).applyMatrix4(this.projectionMatrixInverse),n.set(Vn.x,Vn.y).multiplyScalar(-e/Vn.z)}getViewSize(e,t){return this.getViewBounds(e,uc,dc),t.subVectors(dc,uc)}setViewOffset(e,t,n,s,r,a){this.aspect=e/t,this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=t,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let e=this.near,t=e*Math.tan(ss*.5*this.fov)/this.zoom,n=2*t,s=this.aspect*n,r=-.5*s,a=this.view;if(this.view!==null&&this.view.enabled){let l=a.fullWidth,c=a.fullHeight;r+=a.offsetX*s/l,t-=a.offsetY*n/c,s*=a.width/l,n*=a.height/c}let o=this.filmOffset;o!==0&&(r+=e*o/this.getFilmWidth()),this.projectionMatrix.makePerspective(r,r+s,t,t-n,e,this.far,this.coordinateSystem,this.reversedDepth),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){let t=super.toJSON(e);return t.object.fov=this.fov,t.object.zoom=this.zoom,t.object.near=this.near,t.object.far=this.far,t.object.focus=this.focus,t.object.aspect=this.aspect,this.view!==null&&(t.object.view=Object.assign({},this.view)),t.object.filmGauge=this.filmGauge,t.object.filmOffset=this.filmOffset,t}};var Es=class extends bs{constructor(e=-1,t=1,n=1,s=-1,r=.1,a=2e3){super(),this.isOrthographicCamera=!0,this.type="OrthographicCamera",this.zoom=1,this.view=null,this.left=e,this.right=t,this.top=n,this.bottom=s,this.near=r,this.far=a,this.updateProjectionMatrix()}copy(e,t){return super.copy(e,t),this.left=e.left,this.right=e.right,this.top=e.top,this.bottom=e.bottom,this.near=e.near,this.far=e.far,this.zoom=e.zoom,this.view=e.view===null?null:Object.assign({},e.view),this}setViewOffset(e,t,n,s,r,a){this.view===null&&(this.view={enabled:!0,fullWidth:1,fullHeight:1,offsetX:0,offsetY:0,width:1,height:1}),this.view.enabled=!0,this.view.fullWidth=e,this.view.fullHeight=t,this.view.offsetX=n,this.view.offsetY=s,this.view.width=r,this.view.height=a,this.updateProjectionMatrix()}clearViewOffset(){this.view!==null&&(this.view.enabled=!1),this.updateProjectionMatrix()}updateProjectionMatrix(){let e=(this.right-this.left)/(2*this.zoom),t=(this.top-this.bottom)/(2*this.zoom),n=(this.right+this.left)/2,s=(this.top+this.bottom)/2,r=n-e,a=n+e,o=s+t,l=s-t;if(this.view!==null&&this.view.enabled){let c=(this.right-this.left)/this.view.fullWidth/this.zoom,h=(this.top-this.bottom)/this.view.fullHeight/this.zoom;r+=c*this.view.offsetX,a=r+c*this.view.width,o-=h*this.view.offsetY,l=o-h*this.view.height}this.projectionMatrix.makeOrthographic(r,a,o,l,this.near,this.far,this.coordinateSystem,this.reversedDepth),this.projectionMatrixInverse.copy(this.projectionMatrix).invert()}toJSON(e){let t=super.toJSON(e);return t.object.zoom=this.zoom,t.object.left=this.left,t.object.right=this.right,t.object.top=this.top,t.object.bottom=this.bottom,t.object.near=this.near,t.object.far=this.far,this.view!==null&&(t.object.view=Object.assign({},this.view)),t}},vo=class extends Xr{constructor(){super(new Es(-5,5,5,-5,.5,500)),this.isDirectionalLightShadow=!0}},Ts=class extends Ms{constructor(e,t){super(e,t),this.isDirectionalLight=!0,this.type="DirectionalLight",this.position.copy(Pt.DEFAULT_UP),this.updateMatrix(),this.target=new Pt,this.shadow=new vo}dispose(){super.dispose(),this.shadow.dispose()}copy(e){return super.copy(e),this.target=e.target.clone(),this.shadow=e.shadow.clone(),this}toJSON(e){let t=super.toJSON(e);return t.object.shadow=this.shadow.toJSON(),t.object.target=this.target.uuid,t}},As=class extends Ms{constructor(e,t){super(e,t),this.isAmbientLight=!0,this.type="AmbientLight"}};var Pi=-90,Ii=1,Vi=class extends Pt{constructor(e,t,n){super(),this.type="CubeCamera",this.renderTarget=n,this.coordinateSystem=null,this.activeMipmapLevel=0;let s=new Ut(Pi,Ii,e,t);s.layers=this.layers,this.add(s);let r=new Ut(Pi,Ii,e,t);r.layers=this.layers,this.add(r);let a=new Ut(Pi,Ii,e,t);a.layers=this.layers,this.add(a);let o=new Ut(Pi,Ii,e,t);o.layers=this.layers,this.add(o);let l=new Ut(Pi,Ii,e,t);l.layers=this.layers,this.add(l);let c=new Ut(Pi,Ii,e,t);c.layers=this.layers,this.add(c)}updateCoordinateSystem(){let e=this.coordinateSystem,t=this.children.concat(),[n,s,r,a,o,l]=t;for(let c of t)this.remove(c);if(e===en)n.up.set(0,1,0),n.lookAt(1,0,0),s.up.set(0,1,0),s.lookAt(-1,0,0),r.up.set(0,0,-1),r.lookAt(0,1,0),a.up.set(0,0,1),a.lookAt(0,-1,0),o.up.set(0,1,0),o.lookAt(0,0,1),l.up.set(0,1,0),l.lookAt(0,0,-1);else if(e===Ni)n.up.set(0,-1,0),n.lookAt(-1,0,0),s.up.set(0,-1,0),s.lookAt(1,0,0),r.up.set(0,0,1),r.lookAt(0,1,0),a.up.set(0,0,-1),a.lookAt(0,-1,0),o.up.set(0,-1,0),o.lookAt(0,0,1),l.up.set(0,-1,0),l.lookAt(0,0,-1);else throw new Error("THREE.CubeCamera.updateCoordinateSystem(): Invalid coordinate system: "+e);for(let c of t)this.add(c),c.updateMatrixWorld()}update(e,t){this.parent===null&&this.updateMatrixWorld();let{renderTarget:n,activeMipmapLevel:s}=this;this.coordinateSystem!==e.coordinateSystem&&(this.coordinateSystem=e.coordinateSystem,this.updateCoordinateSystem());let[r,a,o,l,c,h]=this.children,g=e.getRenderTarget(),d=e.getActiveCubeFace(),m=e.getActiveMipmapLevel(),_=e.xr.enabled;e.xr.enabled=!1;let S=n.texture.mipmapsAutoUpdate;n.texture.mipmapsAutoUpdate=!1;let p=!1;e.isWebGLRenderer===!0?p=e.state.buffers.depth.getReversed():p=e.reversedDepthBuffer,e.setRenderTarget(n,0,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,r),e.setRenderTarget(n,1,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,a),e.setRenderTarget(n,2,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,o),e.setRenderTarget(n,3,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,l),e.setRenderTarget(n,4,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,c),n.texture.mipmapsAutoUpdate=S,e.setRenderTarget(n,5,s),p&&e.autoClear===!1&&e.clearDepth(),e.render(t,h),e.setRenderTarget(g,d,m),e.xr.enabled=_,n.texture.needsPMREMUpdate=!0}},qr=class extends Ut{constructor(e=[]){super(),this.isArrayCamera=!0,this.isMultiViewCamera=!1,this.cameras=e,this.perCameraFrustumCulled=!1}};var tl="\\[\\]\\.:\\/",L1=new RegExp("["+tl+"]","g"),nl="[^"+tl+"]",D1="[^"+tl.replace("\\.","")+"]",N1=/((?:WC+[\/:])*)/.source.replace("WC",nl),U1=/(WCOD+)?/.source.replace("WCOD",D1),F1=/(?:\.(WC+)(?:\[(.+)\])?)?/.source.replace("WC",nl),O1=/\.(WC+)(?:\[(.+)\])?/.source.replace("WC",nl),B1=new RegExp("^"+N1+U1+F1+O1+"$"),z1=["material","materials","bones","map"],So=class{constructor(e,t,n){let s=n||it.parseTrackName(t);this._targetGroup=e,this._bindings=e.subscribe_(t,s)}getValue(e,t){this.bind();let n=this._targetGroup.nCachedObjects_,s=this._bindings[n];s!==void 0&&s.getValue(e,t)}setValue(e,t){let n=this._bindings;for(let s=this._targetGroup.nCachedObjects_,r=n.length;s!==r;++s)n[s].setValue(e,t)}bind(){let e=this._bindings;for(let t=this._targetGroup.nCachedObjects_,n=e.length;t!==n;++t)e[t].bind()}unbind(){let e=this._bindings;for(let t=this._targetGroup.nCachedObjects_,n=e.length;t!==n;++t)e[t].unbind()}},it=class i{constructor(e,t,n){this.path=t,this.parsedPath=n||i.parseTrackName(t),this.node=i.findNode(e,this.parsedPath.nodeName),this.rootNode=e,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}static create(e,t,n){return e&&e.isAnimationObjectGroup?new i.Composite(e,t,n):new i(e,t,n)}static sanitizeNodeName(e){return e.replace(/\s/g,"_").replace(L1,"")}static parseTrackName(e){let t=B1.exec(e);if(t===null)throw new Error("THREE.PropertyBinding: Cannot parse trackName: "+e);let n={nodeName:t[2],objectName:t[3],objectIndex:t[4],propertyName:t[5],propertyIndex:t[6]},s=n.nodeName&&n.nodeName.lastIndexOf(".");if(s!==void 0&&s!==-1){let r=n.nodeName.substring(s+1);z1.indexOf(r)!==-1&&(n.nodeName=n.nodeName.substring(0,s),n.objectName=r)}if(n.propertyName===null||n.propertyName.length===0)throw new Error("THREE.PropertyBinding: can not parse propertyName from trackName: "+e);return n}static findNode(e,t){if(t===void 0||t===""||t==="."||t===-1||t===e.name||t===e.uuid)return e;if(e.skeleton){let n=e.skeleton.getBoneByName(t);if(n!==void 0)return n}if(e.children){let n=function(r){for(let a=0;a<r.length;a++){let o=r[a];if(o.name===t||o.uuid===t)return o;let l=n(o.children);if(l)return l}return null},s=n(e.children);if(s)return s}return null}_getValue_unavailable(){}_setValue_unavailable(){}_getValue_direct(e,t){e[t]=this.targetObject[this.propertyName]}_getValue_array(e,t){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)e[t++]=n[s]}_getValue_arrayElement(e,t){e[t]=this.resolvedProperty[this.propertyIndex]}_getValue_toArray(e,t){this.resolvedProperty.toArray(e,t)}_setValue_direct(e,t){this.targetObject[this.propertyName]=e[t]}_setValue_direct_setNeedsUpdate(e,t){this.targetObject[this.propertyName]=e[t],this.targetObject.needsUpdate=!0}_setValue_direct_setMatrixWorldNeedsUpdate(e,t){this.targetObject[this.propertyName]=e[t],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_array(e,t){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=e[t++]}_setValue_array_setNeedsUpdate(e,t){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=e[t++];this.targetObject.needsUpdate=!0}_setValue_array_setMatrixWorldNeedsUpdate(e,t){let n=this.resolvedProperty;for(let s=0,r=n.length;s!==r;++s)n[s]=e[t++];this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_arrayElement(e,t){this.resolvedProperty[this.propertyIndex]=e[t]}_setValue_arrayElement_setNeedsUpdate(e,t){this.resolvedProperty[this.propertyIndex]=e[t],this.targetObject.needsUpdate=!0}_setValue_arrayElement_setMatrixWorldNeedsUpdate(e,t){this.resolvedProperty[this.propertyIndex]=e[t],this.targetObject.matrixWorldNeedsUpdate=!0}_setValue_fromArray(e,t){this.resolvedProperty.fromArray(e,t)}_setValue_fromArray_setNeedsUpdate(e,t){this.resolvedProperty.fromArray(e,t),this.targetObject.needsUpdate=!0}_setValue_fromArray_setMatrixWorldNeedsUpdate(e,t){this.resolvedProperty.fromArray(e,t),this.targetObject.matrixWorldNeedsUpdate=!0}_getValue_unbound(e,t){this.bind(),this.getValue(e,t)}_setValue_unbound(e,t){this.bind(),this.setValue(e,t)}bind(){let e=this.node,t=this.parsedPath,n=t.objectName,s=t.propertyName,r=t.propertyIndex;if(e||(e=i.findNode(this.rootNode,t.nodeName),this.node=e),this.getValue=this._getValue_unavailable,this.setValue=this._setValue_unavailable,!e){Te("PropertyBinding: No target node found for track: "+this.path+".");return}if(n){let c=t.objectIndex;switch(n){case"materials":if(!e.material){Pe("PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!e.material.materials){Pe("PropertyBinding: Can not bind to material.materials as node.material does not have a materials array.",this);return}e=e.material.materials;break;case"bones":if(!e.skeleton){Pe("PropertyBinding: Can not bind to bones as node does not have a skeleton.",this);return}e=e.skeleton.bones;for(let h=0;h<e.length;h++)if(e[h].name===c){c=h;break}break;case"map":if("map"in e){e=e.map;break}if(!e.material){Pe("PropertyBinding: Can not bind to material as node does not have a material.",this);return}if(!e.material.map){Pe("PropertyBinding: Can not bind to material.map as node.material does not have a map.",this);return}e=e.material.map;break;default:if(e[n]===void 0){Pe("PropertyBinding: Can not bind to objectName of node undefined.",this);return}e=e[n]}if(c!==void 0){if(e[c]===void 0){Pe("PropertyBinding: Trying to bind to objectIndex of objectName, but is undefined.",this,e);return}e=e[c]}}let a=e[s];if(a===void 0){let c=t.nodeName;Pe("PropertyBinding: Trying to update property for track: "+c+"."+s+" but it wasn't found.",e);return}let o=this.Versioning.None;this.targetObject=e,e.isMaterial===!0?o=this.Versioning.NeedsUpdate:e.isObject3D===!0&&(o=this.Versioning.MatrixWorldNeedsUpdate);let l=this.BindingType.Direct;if(r!==void 0){if(s==="morphTargetInfluences"){if(!e.geometry){Pe("PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.",this);return}if(!e.geometry.morphAttributes){Pe("PropertyBinding: Can not bind to morphTargetInfluences because node does not have a geometry.morphAttributes.",this);return}e.morphTargetDictionary[r]!==void 0&&(r=e.morphTargetDictionary[r])}l=this.BindingType.ArrayElement,this.resolvedProperty=a,this.propertyIndex=r}else a.fromArray!==void 0&&a.toArray!==void 0?(l=this.BindingType.HasFromToArray,this.resolvedProperty=a):Array.isArray(a)?(l=this.BindingType.EntireArray,this.resolvedProperty=a):this.propertyName=s;this.getValue=this.GetterByBindingType[l],this.setValue=this.SetterByBindingTypeAndVersioning[l][o]}unbind(){this.node=null,this.getValue=this._getValue_unbound,this.setValue=this._setValue_unbound}};it.Composite=So;it.prototype.BindingType={Direct:0,EntireArray:1,ArrayElement:2,HasFromToArray:3};it.prototype.Versioning={None:0,NeedsUpdate:1,MatrixWorldNeedsUpdate:2};it.prototype.GetterByBindingType=[it.prototype._getValue_direct,it.prototype._getValue_array,it.prototype._getValue_arrayElement,it.prototype._getValue_toArray];it.prototype.SetterByBindingTypeAndVersioning=[[it.prototype._setValue_direct,it.prototype._setValue_direct_setNeedsUpdate,it.prototype._setValue_direct_setMatrixWorldNeedsUpdate],[it.prototype._setValue_array,it.prototype._setValue_array_setNeedsUpdate,it.prototype._setValue_array_setMatrixWorldNeedsUpdate],[it.prototype._setValue_arrayElement,it.prototype._setValue_arrayElement_setNeedsUpdate,it.prototype._setValue_arrayElement_setMatrixWorldNeedsUpdate],[it.prototype._setValue_fromArray,it.prototype._setValue_fromArray_setNeedsUpdate,it.prototype._setValue_fromArray_setMatrixWorldNeedsUpdate]];var X2=new Float32Array(1);var fc=new nt,ws=class{constructor(e,t,n=0,s=1/0){this.ray=new Xn(e,t),this.near=n,this.far=s,this.camera=null,this.layers=new Bi,this.params={Mesh:{},Line:{threshold:1},LOD:{},Points:{threshold:1},Sprite:{}}}set(e,t){this.ray.set(e,t)}setFromCamera(e,t){t.isPerspectiveCamera?(this.ray.origin.setFromMatrixPosition(t.matrixWorld),this.ray.direction.set(e.x,e.y,.5).unproject(t).sub(this.ray.origin).normalize(),this.camera=t):t.isOrthographicCamera?(this.ray.origin.set(e.x,e.y,t.projectionMatrix.elements[14]).unproject(t),this.ray.direction.set(0,0,-1).transformDirection(t.matrixWorld),this.camera=t):Pe("Raycaster: Unsupported camera type: "+t.type)}setFromXRController(e){return fc.identity().extractRotation(e.matrixWorld),this.ray.origin.setFromMatrixPosition(e.matrixWorld),this.ray.direction.set(0,0,-1).applyMatrix4(fc),this}intersectObject(e,t=!0,n=[]){return Mo(e,this,n,t),n.sort(pc),n}intersectObjects(e,t=!0,n=[]){for(let s=0,r=e.length;s<r;s++)Mo(e[s],this,n,t);return n.sort(pc),n}};function pc(i,e){return i.distance-e.distance}function Mo(i,e,t,n){let s=!0;if(i.layers.test(e.layers)&&i.raycast(e,t)===!1&&(s=!1),s===!0&&n===!0){let r=i.children;for(let a=0,o=r.length;a<o;a++)Mo(r[a],e,t,!0)}}var Rs=class{constructor(e=!0){this.autoStart=e,this.startTime=0,this.oldTime=0,this.elapsedTime=0,this.running=!1,Te("Clock: This module has been deprecated. Please use THREE.Timer instead.")}start(){this.startTime=performance.now(),this.oldTime=this.startTime,this.elapsedTime=0,this.running=!0}stop(){this.getElapsedTime(),this.running=!1,this.autoStart=!1}getElapsedTime(){return this.getDelta(),this.elapsedTime}getDelta(){let e=0;if(this.autoStart&&!this.running)return this.start(),0;if(this.running){let t=performance.now();e=(t-this.oldTime)/1e3,this.oldTime=t,this.elapsedTime+=e}return e}},Hi=class{constructor(e=1,t=0,n=0){this.radius=e,this.phi=t,this.theta=n}set(e,t,n){return this.radius=e,this.phi=t,this.theta=n,this}copy(e){return this.radius=e.radius,this.phi=e.phi,this.theta=e.theta,this}makeSafe(){return this.phi=ke(this.phi,1e-6,Math.PI-1e-6),this}setFromVector3(e){return this.setFromCartesianCoords(e.x,e.y,e.z)}setFromCartesianCoords(e,t,n){return this.radius=Math.sqrt(e*e+t*t+n*n),this.radius===0?(this.theta=0,this.phi=0):(this.theta=Math.atan2(e,n),this.phi=Math.acos(ke(t/this.radius,-1,1))),this}clone(){return new this.constructor().copy(this)}};var ll=class ll{constructor(e,t,n,s){this.elements=[1,0,0,1],e!==void 0&&this.set(e,t,n,s)}identity(){return this.set(1,0,0,1),this}fromArray(e,t=0){for(let n=0;n<4;n++)this.elements[n]=e[n+t];return this}set(e,t,n,s){let r=this.elements;return r[0]=e,r[2]=t,r[1]=n,r[3]=s,this}};ll.prototype.isMatrix2=!0;var bo=ll;var Cs=class extends ln{constructor(e,t=null){super(),this.object=e,this.domElement=t,this.enabled=!0,this.state=-1,this.keys={},this.mouseButtons={LEFT:null,MIDDLE:null,RIGHT:null},this.touches={ONE:null,TWO:null}}connect(e){this.domElement!==null&&this.disconnect(),this.domElement=e}disconnect(){}dispose(){}update(){}};function il(i,e,t,n){let s=k1(n);switch(t){case Vo:return i*e;case Wo:return i*e/s.components*s.byteLength;case ta:return i*e/s.components*s.byteLength;case Qn:return i*e*2/s.components*s.byteLength;case na:return i*e*2/s.components*s.byteLength;case Ho:return i*e*3/s.components*s.byteLength;case dn:return i*e*4/s.components*s.byteLength;case ia:return i*e*4/s.components*s.byteLength;case Ls:case Ds:return Math.floor((i+3)/4)*Math.floor((e+3)/4)*8;case Ns:case Us:return Math.floor((i+3)/4)*Math.floor((e+3)/4)*16;case ra:case oa:return Math.max(i,16)*Math.max(e,8)/4;case sa:case aa:return Math.max(i,8)*Math.max(e,8)/2;case la:case ca:case ua:case da:return Math.floor((i+3)/4)*Math.floor((e+3)/4)*8;case ha:case Fs:case fa:return Math.floor((i+3)/4)*Math.floor((e+3)/4)*16;case pa:return Math.floor((i+3)/4)*Math.floor((e+3)/4)*16;case ma:return Math.floor((i+4)/5)*Math.floor((e+3)/4)*16;case ga:return Math.floor((i+4)/5)*Math.floor((e+4)/5)*16;case _a:return Math.floor((i+5)/6)*Math.floor((e+4)/5)*16;case xa:return Math.floor((i+5)/6)*Math.floor((e+5)/6)*16;case ya:return Math.floor((i+7)/8)*Math.floor((e+4)/5)*16;case va:return Math.floor((i+7)/8)*Math.floor((e+5)/6)*16;case Sa:return Math.floor((i+7)/8)*Math.floor((e+7)/8)*16;case Ma:return Math.floor((i+9)/10)*Math.floor((e+4)/5)*16;case ba:return Math.floor((i+9)/10)*Math.floor((e+5)/6)*16;case Ea:return Math.floor((i+9)/10)*Math.floor((e+7)/8)*16;case Ta:return Math.floor((i+9)/10)*Math.floor((e+9)/10)*16;case Aa:return Math.floor((i+11)/12)*Math.floor((e+9)/10)*16;case wa:return Math.floor((i+11)/12)*Math.floor((e+11)/12)*16;case Ra:case Ca:case Pa:return Math.ceil(i/4)*Math.ceil(e/4)*16;case Ia:case La:return Math.ceil(i/4)*Math.ceil(e/4)*8;case Os:case Da:return Math.ceil(i/4)*Math.ceil(e/4)*16}throw new Error(`Unable to determine texture byte length for ${t} format.`)}function k1(i){switch(i){case Gt:case Bo:return{byteLength:1,components:1};case Yi:case zo:case un:return{byteLength:2,components:1};case Qr:case ea:return{byteLength:2,components:4};case cn:case jr:case hn:return{byteLength:4,components:1};case ko:case Go:return{byteLength:4,components:3}}throw new Error(`THREE.TextureUtils: Unknown texture type ${i}.`)}typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("register",{detail:{revision:"187"}}));typeof window<"u"&&(window.__THREE__?Te("WARNING: Multiple instances of Three.js being imported."):window.__THREE__="187");function Th(){let i=null,e=!1,t=null,n=null;function s(r,a){n=i.requestAnimationFrame(s),t(r,a)}return{start:function(){e!==!0&&t!==null&&i!==null&&(n=i.requestAnimationFrame(s),e=!0)},stop:function(){i!==null&&i.cancelAnimationFrame(n),e=!1},setAnimationLoop:function(r){t=r},setContext:function(r){i=r}}}function V1(i){let e=new WeakMap;function t(o,l){let c=o.array,h=o.usage,g=c.byteLength,d=i.createBuffer();i.bindBuffer(l,d),i.bufferData(l,c,h),o.onUploadCallback();let m;if(c instanceof Float32Array)m=i.FLOAT;else if(typeof Float16Array<"u"&&c instanceof Float16Array)m=i.HALF_FLOAT;else if(c instanceof Uint16Array)o.isFloat16BufferAttribute?m=i.HALF_FLOAT:m=i.UNSIGNED_SHORT;else if(c instanceof Int16Array)m=i.SHORT;else if(c instanceof Uint32Array)m=i.UNSIGNED_INT;else if(c instanceof Int32Array)m=i.INT;else if(c instanceof Int8Array)m=i.BYTE;else if(c instanceof Uint8Array)m=i.UNSIGNED_BYTE;else if(c instanceof Uint8ClampedArray)m=i.UNSIGNED_BYTE;else throw new Error("THREE.WebGLAttributes: Unsupported buffer data format: "+c);return{buffer:d,type:m,bytesPerElement:c.BYTES_PER_ELEMENT,version:o.version,size:g}}function n(o,l,c){let h=l.array,g=l.updateRanges;if(i.bindBuffer(c,o),g.length===0)i.bufferSubData(c,0,h);else{g.sort((m,_)=>m.start-_.start);let d=0;for(let m=1;m<g.length;m++){let _=g[d],S=g[m];S.start<=_.start+_.count+1?_.count=Math.max(_.count,S.start+S.count-_.start):(++d,g[d]=S)}g.length=d+1;for(let m=0,_=g.length;m<_;m++){let S=g[m];i.bufferSubData(c,S.start*h.BYTES_PER_ELEMENT,h,S.start,S.count)}l.clearUpdateRanges()}l.onUploadCallback()}function s(o){return o.isInterleavedBufferAttribute&&(o=o.data),e.get(o)}function r(o){o.isInterleavedBufferAttribute&&(o=o.data);let l=e.get(o);l&&(i.deleteBuffer(l.buffer),e.delete(o))}function a(o,l){if(o.isInterleavedBufferAttribute&&(o=o.data),o.isGLBufferAttribute){let h=e.get(o);(!h||h.version<o.version)&&e.set(o,{buffer:o.buffer,type:o.type,bytesPerElement:o.elementSize,version:o.version});return}let c=e.get(o);if(c===void 0)e.set(o,t(o,l));else if(c.version<o.version){if(c.size!==o.array.byteLength)throw new Error("THREE.WebGLAttributes: The size of the buffer attribute's array buffer does not match the original size. Resizing buffer attributes is not supported.");n(c.buffer,o,l),c.version=o.version}}return{get:s,remove:r,update:a}}var H1=`#ifdef USE_ALPHAHASH
	if ( diffuseColor.a < getAlphaHashThreshold( vPosition ) ) discard;
#endif`,W1=`#ifdef USE_ALPHAHASH
	const float ALPHA_HASH_SCALE = 0.05;
	float hash2D( vec2 value ) {
		return fract( 1.0e4 * sin( 17.0 * value.x + 0.1 * value.y ) * ( 0.1 + abs( sin( 13.0 * value.y + value.x ) ) ) );
	}
	float hash3D( vec3 value ) {
		return hash2D( vec2( hash2D( value.xy ), value.z ) );
	}
	float getAlphaHashThreshold( vec3 position ) {
		float maxDeriv = max(
			length( dFdx( position.xyz ) ),
			length( dFdy( position.xyz ) )
		);
		float pixScale = 1.0 / ( ALPHA_HASH_SCALE * maxDeriv );
		vec2 pixScales = vec2(
			exp2( floor( log2( pixScale ) ) ),
			exp2( ceil( log2( pixScale ) ) )
		);
		vec2 alpha = vec2(
			hash3D( floor( pixScales.x * position.xyz ) ),
			hash3D( floor( pixScales.y * position.xyz ) )
		);
		float lerpFactor = fract( log2( pixScale ) );
		float x = ( 1.0 - lerpFactor ) * alpha.x + lerpFactor * alpha.y;
		float a = min( lerpFactor, 1.0 - lerpFactor );
		vec3 cases = vec3(
			x * x / ( 2.0 * a * ( 1.0 - a ) ),
			( x - 0.5 * a ) / ( 1.0 - a ),
			1.0 - ( ( 1.0 - x ) * ( 1.0 - x ) / ( 2.0 * a * ( 1.0 - a ) ) )
		);
		float threshold = ( x < ( 1.0 - a ) )
			? ( ( x < a ) ? cases.x : cases.y )
			: cases.z;
		return clamp( threshold , 1.0e-6, 1.0 );
	}
#endif`,X1=`#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, vAlphaMapUv ).g;
#endif`,q1=`#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Y1=`#ifdef USE_ALPHATEST
	#ifdef ALPHA_TO_COVERAGE
	diffuseColor.a = smoothstep( alphaTest, alphaTest + fwidth( diffuseColor.a ), diffuseColor.a );
	if ( diffuseColor.a == 0.0 ) discard;
	#else
	if ( diffuseColor.a < alphaTest ) discard;
	#endif
#endif`,Z1=`#ifdef USE_ALPHATEST
	uniform float alphaTest;
#endif`,J1=`#ifdef USE_AOMAP
	float ambientOcclusion = ( texture2D( aoMap, vAoMapUv ).r - 1.0 ) * aoMapIntensity + 1.0;
	reflectedLight.indirectDiffuse *= ambientOcclusion;
	#if defined( USE_CLEARCOAT ) 
		clearcoatSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_SHEEN ) 
		sheenSpecularIndirect *= ambientOcclusion;
	#endif
	#if defined( USE_ENVMAP ) && defined( STANDARD )
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		reflectedLight.indirectSpecular *= computeSpecularOcclusion( dotNV, ambientOcclusion, material.roughness );
	#endif
#endif`,$1=`#ifdef USE_AOMAP
	uniform sampler2D aoMap;
	uniform float aoMapIntensity;
#endif`,K1=`#ifdef USE_BATCHING
	#if ! defined( GL_ANGLE_multi_draw )
	#define gl_DrawID _gl_DrawID
	uniform int _gl_DrawID;
	#endif
	uniform highp sampler2D batchingTexture;
	uniform highp usampler2D batchingIdTexture;
	mat4 getBatchingMatrix( const in float i ) {
		int size = textureSize( batchingTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( batchingTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( batchingTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( batchingTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( batchingTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
	float getIndirectIndex( const in int i ) {
		int size = textureSize( batchingIdTexture, 0 ).x;
		int x = i % size;
		int y = i / size;
		return float( texelFetch( batchingIdTexture, ivec2( x, y ), 0 ).r );
	}
#endif
#ifdef USE_BATCHING_COLOR
	uniform sampler2D batchingColorTexture;
	vec4 getBatchingColor( const in float i ) {
		int size = textureSize( batchingColorTexture, 0 ).x;
		int j = int( i );
		int x = j % size;
		int y = j / size;
		return texelFetch( batchingColorTexture, ivec2( x, y ), 0 );
	}
#endif`,j1=`#ifdef USE_BATCHING
	mat4 batchingMatrix = getBatchingMatrix( getIndirectIndex( gl_DrawID ) );
#endif`,Q1=`vec3 transformed = vec3( position );
#ifdef USE_ALPHAHASH
	vPosition = vec3( position );
#endif`,eu=`vec3 objectNormal = vec3( normal );
#ifdef USE_TANGENT
	vec3 objectTangent = vec3( tangent.xyz );
#endif`,tu=`float G_BlinnPhong_Implicit( ) {
	return 0.25;
}
float D_BlinnPhong( const in float shininess, const in float dotNH ) {
	return RECIPROCAL_PI * ( shininess * 0.5 + 1.0 ) * pow( dotNH, shininess );
}
vec3 BRDF_BlinnPhong( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 specularColor, const in float shininess ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( specularColor, 1.0, dotVH );
	float G = G_BlinnPhong_Implicit( );
	float D = D_BlinnPhong( shininess, dotNH );
	return F * ( G * D );
} // validated`,nu=`#ifdef USE_IRIDESCENCE
	const mat3 XYZ_TO_REC709 = mat3(
		 3.2404542, -0.9692660,  0.0556434,
		-1.5371385,  1.8760108, -0.2040259,
		-0.4985314,  0.0415560,  1.0572252
	);
	vec3 Fresnel0ToIor( vec3 fresnel0 ) {
		vec3 sqrtF0 = sqrt( fresnel0 );
		return ( vec3( 1.0 ) + sqrtF0 ) / ( vec3( 1.0 ) - sqrtF0 );
	}
	vec3 IorToFresnel0( vec3 transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - vec3( incidentIor ) ) / ( transmittedIor + vec3( incidentIor ) ) );
	}
	float IorToFresnel0( float transmittedIor, float incidentIor ) {
		return pow2( ( transmittedIor - incidentIor ) / ( transmittedIor + incidentIor ));
	}
	vec3 evalSensitivity( float OPD, vec3 shift ) {
		float phase = 2.0 * PI * OPD * 1.0e-9;
		vec3 val = vec3( 5.4856e-13, 4.4201e-13, 5.2481e-13 );
		vec3 pos = vec3( 1.6810e+06, 1.7953e+06, 2.2084e+06 );
		vec3 var = vec3( 4.3278e+09, 9.3046e+09, 6.6121e+09 );
		vec3 xyz = val * sqrt( 2.0 * PI * var ) * cos( pos * phase + shift ) * exp( - pow2( phase ) * var );
		xyz.x += 9.7470e-14 * sqrt( 2.0 * PI * 4.5282e+09 ) * cos( 2.2399e+06 * phase + shift[ 0 ] ) * exp( - 4.5282e+09 * pow2( phase ) );
		xyz /= 1.0685e-7;
		vec3 rgb = XYZ_TO_REC709 * xyz;
		return rgb;
	}
	vec3 evalIridescence( float outsideIOR, float eta2, float cosTheta1, float thinFilmThickness, vec3 baseF0 ) {
		vec3 I;
		float iridescenceIOR = mix( outsideIOR, eta2, smoothstep( 0.0, 0.03, thinFilmThickness ) );
		float sinTheta2Sq = pow2( outsideIOR / iridescenceIOR ) * ( 1.0 - pow2( cosTheta1 ) );
		float cosTheta2Sq = 1.0 - sinTheta2Sq;
		if ( cosTheta2Sq < 0.0 ) {
			return vec3( 1.0 );
		}
		float cosTheta2 = sqrt( cosTheta2Sq );
		float R0 = IorToFresnel0( iridescenceIOR, outsideIOR );
		float R12 = F_Schlick( R0, 1.0, cosTheta1 );
		float T121 = 1.0 - R12;
		float phi12 = 0.0;
		if ( iridescenceIOR < outsideIOR ) phi12 = PI;
		float phi21 = PI - phi12;
		vec3 baseIOR = Fresnel0ToIor( clamp( baseF0, 0.0, 0.9999 ) );		vec3 R1 = IorToFresnel0( baseIOR, iridescenceIOR );
		vec3 R23 = F_Schlick( R1, 1.0, cosTheta2 );
		vec3 phi23 = vec3( 0.0 );
		if ( baseIOR[ 0 ] < iridescenceIOR ) phi23[ 0 ] = PI;
		if ( baseIOR[ 1 ] < iridescenceIOR ) phi23[ 1 ] = PI;
		if ( baseIOR[ 2 ] < iridescenceIOR ) phi23[ 2 ] = PI;
		float OPD = 2.0 * iridescenceIOR * thinFilmThickness * cosTheta2;
		vec3 phi = vec3( phi21 ) + phi23;
		vec3 R123 = clamp( R12 * R23, 1e-5, 0.9999 );
		vec3 r123 = sqrt( R123 );
		vec3 Rs = pow2( T121 ) * R23 / ( vec3( 1.0 ) - R123 );
		vec3 C0 = R12 + Rs;
		I = C0;
		vec3 Cm = Rs - T121;
		for ( int m = 1; m <= 2; ++ m ) {
			Cm *= r123;
			vec3 Sm = 2.0 * evalSensitivity( float( m ) * OPD, float( m ) * phi );
			I += Cm * Sm;
		}
		return max( I, vec3( 0.0 ) );
	}
#endif`,iu=`#ifdef USE_BUMPMAP
	uniform sampler2D bumpMap;
	uniform float bumpScale;
	vec2 dHdxy_fwd() {
		vec2 dSTdx = dFdx( vBumpMapUv );
		vec2 dSTdy = dFdy( vBumpMapUv );
		float Hll = bumpScale * texture2D( bumpMap, vBumpMapUv ).x;
		float dBx = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdx ).x - Hll;
		float dBy = bumpScale * texture2D( bumpMap, vBumpMapUv + dSTdy ).x - Hll;
		return vec2( dBx, dBy );
	}
	vec3 perturbNormalArb( vec3 surf_pos, vec3 surf_norm, vec2 dHdxy, float faceDirection ) {
		vec3 vSigmaX = normalize( dFdx( surf_pos.xyz ) );
		vec3 vSigmaY = normalize( dFdy( surf_pos.xyz ) );
		vec3 vN = surf_norm;
		vec3 R1 = cross( vSigmaY, vN );
		vec3 R2 = cross( vN, vSigmaX );
		float fDet = dot( vSigmaX, R1 ) * faceDirection;
		vec3 vGrad = sign( fDet ) * ( dHdxy.x * R1 + dHdxy.y * R2 );
		return normalize( abs( fDet ) * surf_norm - vGrad );
	}
#endif`,su=`#if NUM_CLIPPING_PLANES > 0
	vec4 plane;
	#ifdef ALPHA_TO_COVERAGE
		float distanceToPlane, distanceGradient;
		float clipOpacity = 1.0;
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
			distanceGradient = fwidth( distanceToPlane ) / 2.0;
			clipOpacity *= smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			if ( clipOpacity == 0.0 ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			float unionClipOpacity = 1.0;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				distanceToPlane = - dot( vClipPosition, plane.xyz ) + plane.w;
				distanceGradient = fwidth( distanceToPlane ) / 2.0;
				unionClipOpacity *= 1.0 - smoothstep( - distanceGradient, distanceGradient, distanceToPlane );
			}
			#pragma unroll_loop_end
			clipOpacity *= 1.0 - unionClipOpacity;
		#endif
		diffuseColor.a *= clipOpacity;
		if ( diffuseColor.a == 0.0 ) discard;
	#else
		#pragma unroll_loop_start
		for ( int i = 0; i < UNION_CLIPPING_PLANES; i ++ ) {
			plane = clippingPlanes[ i ];
			if ( dot( vClipPosition, plane.xyz ) > plane.w ) discard;
		}
		#pragma unroll_loop_end
		#if UNION_CLIPPING_PLANES < NUM_CLIPPING_PLANES
			bool clipped = true;
			#pragma unroll_loop_start
			for ( int i = UNION_CLIPPING_PLANES; i < NUM_CLIPPING_PLANES; i ++ ) {
				plane = clippingPlanes[ i ];
				clipped = ( dot( vClipPosition, plane.xyz ) > plane.w ) && clipped;
			}
			#pragma unroll_loop_end
			if ( clipped ) discard;
		#endif
	#endif
#endif`,ru=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
	uniform vec4 clippingPlanes[ NUM_CLIPPING_PLANES ];
#endif`,au=`#if NUM_CLIPPING_PLANES > 0
	varying vec3 vClipPosition;
#endif`,ou=`#if NUM_CLIPPING_PLANES > 0
	vClipPosition = - mvPosition.xyz;
#endif`,lu=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA )
	diffuseColor *= vColor;
#endif`,cu=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA )
	varying vec4 vColor;
#endif`,hu=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	varying vec4 vColor;
#endif`,uu=`#if defined( USE_COLOR ) || defined( USE_COLOR_ALPHA ) || defined( USE_INSTANCING_COLOR ) || defined( USE_BATCHING_COLOR )
	vColor = vec4( 1.0 );
#endif
#ifdef USE_COLOR_ALPHA
	vColor *= color;
#elif defined( USE_COLOR )
	vColor.rgb *= color;
#endif
#ifdef USE_INSTANCING_COLOR
	vColor.rgb *= instanceColor.rgb;
#endif
#ifdef USE_BATCHING_COLOR
	vColor *= getBatchingColor( getIndirectIndex( gl_DrawID ) );
#endif`,du=`#define PI 3.141592653589793
#define PI2 6.283185307179586
#define PI_HALF 1.5707963267948966
#define RECIPROCAL_PI 0.3183098861837907
#define RECIPROCAL_PI2 0.15915494309189535
#define EPSILON 1e-6
#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
#define whiteComplement( a ) ( 1.0 - saturate( a ) )
float pow2( const in float x ) { return x*x; }
vec3 pow2( const in vec3 x ) { return x*x; }
float pow3( const in float x ) { return x*x*x; }
float pow4( const in float x ) { float x2 = x*x; return x2*x2; }
float max3( const in vec3 v ) { return max( max( v.x, v.y ), v.z ); }
float average( const in vec3 v ) { return dot( v, vec3( 0.3333333 ) ); }
highp float rand( const in vec2 uv ) {
	const highp float a = 12.9898, b = 78.233, c = 43758.5453;
	highp float dt = dot( uv.xy, vec2( a,b ) ), sn = mod( dt, PI );
	return fract( sin( sn ) * c );
}
#ifdef HIGH_PRECISION
	float precisionSafeLength( vec3 v ) { return length( v ); }
#else
	float precisionSafeLength( vec3 v ) {
		float maxComponent = max3( abs( v ) );
		return length( v / maxComponent ) * maxComponent;
	}
#endif
struct IncidentLight {
	vec3 color;
	vec3 direction;
	bool visible;
};
struct ReflectedLight {
	vec3 directDiffuse;
	vec3 directSpecular;
	vec3 indirectDiffuse;
	vec3 indirectSpecular;
};
#ifdef USE_ALPHAHASH
	varying vec3 vPosition;
#endif
vec3 transformDirection( in vec3 dir, in mat4 matrix ) {
	return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );
}
#define inverseTransformDirection transformDirectionByInverseViewMatrix
vec3 transformNormalByInverseViewMatrix( in vec3 normal, in mat4 viewMatrix ) {
	return normalize( ( vec4( normal, 0.0 ) * viewMatrix ).xyz );
}
vec3 transformDirectionByInverseViewMatrix( in vec3 dir, in mat4 viewMatrix ) {
	return normalize( ( vec4( dir, 0.0 ) * viewMatrix ).xyz );
}
bool isPerspectiveMatrix( mat4 m ) {
	return m[ 2 ][ 3 ] == - 1.0;
}
vec2 equirectUv( in vec3 dir ) {
	float u = atan( dir.z, dir.x ) * RECIPROCAL_PI2 + 0.5;
	float v = asin( clamp( dir.y, - 1.0, 1.0 ) ) * RECIPROCAL_PI + 0.5;
	return vec2( u, v );
}
vec3 BRDF_Lambert( const in vec3 diffuseColor ) {
	return RECIPROCAL_PI * diffuseColor;
}
vec3 F_Schlick( const in vec3 f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
}
float F_Schlick( const in float f0, const in float f90, const in float dotVH ) {
	float fresnel = exp2( ( - 5.55473 * dotVH - 6.98316 ) * dotVH );
	return f0 * ( 1.0 - fresnel ) + ( f90 * fresnel );
} // validated`,fu=`vec3 transformedNormal = objectNormal;
#ifdef USE_TANGENT
	vec3 transformedTangent = objectTangent;
#endif
#ifdef USE_BATCHING
	mat3 bm = mat3( batchingMatrix );
	transformedNormal /= vec3( dot( bm[ 0 ], bm[ 0 ] ), dot( bm[ 1 ], bm[ 1 ] ), dot( bm[ 2 ], bm[ 2 ] ) );
	transformedNormal = bm * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = bm * transformedTangent;
	#endif
#endif
#ifdef USE_INSTANCING
	mat3 im = mat3( instanceMatrix );
	transformedNormal /= vec3( dot( im[ 0 ], im[ 0 ] ), dot( im[ 1 ], im[ 1 ] ), dot( im[ 2 ], im[ 2 ] ) );
	transformedNormal = im * transformedNormal;
	#ifdef USE_TANGENT
		transformedTangent = im * transformedTangent;
	#endif
#endif
transformedNormal = normalMatrix * transformedNormal;
#ifdef FLIP_SIDED
	transformedNormal = - transformedNormal;
#endif
#ifdef USE_TANGENT
	transformedTangent = ( modelViewMatrix * vec4( transformedTangent, 0.0 ) ).xyz;
#endif`,pu=`#ifdef USE_DISPLACEMENTMAP
	uniform sampler2D displacementMap;
	uniform float displacementScale;
	uniform float displacementBias;
#endif`,mu=`#ifdef USE_DISPLACEMENTMAP
	transformed += normalize( objectNormal ) * ( texture2D( displacementMap, vDisplacementMapUv ).x * displacementScale + displacementBias );
#endif`,gu=`#ifdef USE_EMISSIVEMAP
	vec4 emissiveColor = texture2D( emissiveMap, vEmissiveMapUv );
	#ifdef DECODE_VIDEO_TEXTURE_EMISSIVE
		emissiveColor = sRGBTransferEOTF( emissiveColor );
	#endif
	totalEmissiveRadiance *= emissiveColor.rgb;
#endif`,_u=`#ifdef USE_EMISSIVEMAP
	uniform sampler2D emissiveMap;
#endif`,xu="gl_FragColor = linearToOutputTexel( gl_FragColor );",yu=`vec4 LinearTransferOETF( in vec4 value ) {
	return value;
}
vec4 sRGBTransferEOTF( in vec4 value ) {
	return vec4( mix( pow( value.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), value.rgb * 0.0773993808, vec3( lessThanEqual( value.rgb, vec3( 0.04045 ) ) ) ), value.a );
}
vec4 sRGBTransferOETF( in vec4 value ) {
	return vec4( mix( pow( value.rgb, vec3( 0.41666 ) ) * 1.055 - vec3( 0.055 ), value.rgb * 12.92, vec3( lessThanEqual( value.rgb, vec3( 0.0031308 ) ) ) ), value.a );
}`,vu=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vec3 cameraToFrag;
		if ( isOrthographic ) {
			cameraToFrag = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToFrag = normalize( vWorldPosition - cameraPosition );
		}
		vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vec3 reflectVec = reflect( cameraToFrag, worldNormal );
		#else
			vec3 reflectVec = refract( cameraToFrag, worldNormal, refractionRatio );
		#endif
	#else
		vec3 reflectVec = vReflect;
	#endif
	#ifdef ENVMAP_TYPE_CUBE
		vec4 envColor = textureCube( envMap, envMapRotation * reflectVec );
		#ifdef ENVMAP_BLENDING_MULTIPLY
			outgoingLight = mix( outgoingLight, outgoingLight * envColor.xyz, specularStrength * reflectivity );
		#elif defined( ENVMAP_BLENDING_MIX )
			outgoingLight = mix( outgoingLight, envColor.xyz, specularStrength * reflectivity );
		#elif defined( ENVMAP_BLENDING_ADD )
			outgoingLight += envColor.xyz * specularStrength * reflectivity;
		#endif
	#endif
#endif`,Su=`#ifdef USE_ENVMAP
	uniform float envMapIntensity;
	uniform mat3 envMapRotation;
	uniform samplerCube envMap;
	#ifdef ENVMAP_TYPE_PMREM
		float roughnessToMip( const in float roughness ) {
			float r = clamp( roughness, 0.0, 1.0 );
			return ENVMAP_MAX_LOD * r * ( 2.0 - r );
		}
	#endif
#endif`,Mu=`#ifdef USE_ENVMAP
	uniform float reflectivity;
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		varying vec3 vWorldPosition;
		uniform float refractionRatio;
	#else
		varying vec3 vReflect;
	#endif
#endif`,bu=`#ifdef USE_ENVMAP
	#if defined( USE_BUMPMAP ) || defined( USE_NORMALMAP ) || defined( PHONG ) || defined( LAMBERT )
		#define ENV_WORLDPOS
	#endif
	#ifdef ENV_WORLDPOS
		
		varying vec3 vWorldPosition;
	#else
		varying vec3 vReflect;
		uniform float refractionRatio;
	#endif
#endif`,Eu=`#ifdef USE_ENVMAP
	#ifdef ENV_WORLDPOS
		vWorldPosition = worldPosition.xyz;
	#else
		vec3 cameraToVertex;
		if ( isOrthographic ) {
			cameraToVertex = normalize( vec3( - viewMatrix[ 0 ][ 2 ], - viewMatrix[ 1 ][ 2 ], - viewMatrix[ 2 ][ 2 ] ) );
		} else {
			cameraToVertex = normalize( worldPosition.xyz - cameraPosition );
		}
		vec3 worldNormal = transformNormalByInverseViewMatrix( transformedNormal, viewMatrix );
		#ifdef ENVMAP_MODE_REFLECTION
			vReflect = reflect( cameraToVertex, worldNormal );
		#else
			vReflect = refract( cameraToVertex, worldNormal, refractionRatio );
		#endif
	#endif
#endif`,Tu=`#ifdef USE_FOG
	vFogDepth = - mvPosition.z;
#endif`,Au=`#ifdef USE_FOG
	varying float vFogDepth;
#endif`,wu=`#ifdef USE_FOG
	#ifdef FOG_EXP2
		float fogFactor = 1.0 - exp( - fogDensity * fogDensity * vFogDepth * vFogDepth );
	#else
		float fogFactor = smoothstep( fogNear, fogFar, vFogDepth );
	#endif
	gl_FragColor.rgb = mix( gl_FragColor.rgb, fogColor, fogFactor );
#endif`,Ru=`#ifdef USE_FOG
	uniform vec3 fogColor;
	varying float vFogDepth;
	#ifdef FOG_EXP2
		uniform float fogDensity;
	#else
		uniform float fogNear;
		uniform float fogFar;
	#endif
#endif`,Cu=`#ifdef USE_GRADIENTMAP
	uniform sampler2D gradientMap;
#endif
vec3 getGradientIrradiance( vec3 normal, vec3 lightDirection ) {
	float dotNL = dot( normal, lightDirection );
	vec2 coord = vec2( dotNL * 0.5 + 0.5, 0.0 );
	#ifdef USE_GRADIENTMAP
		return vec3( texture2D( gradientMap, coord ).r );
	#else
		vec2 fw = fwidth( coord ) * 0.5;
		return mix( vec3( 0.7 ), vec3( 1.0 ), smoothstep( 0.7 - fw.x, 0.7 + fw.x, coord.x ) );
	#endif
}`,Pu=`#ifdef USE_LIGHTMAP
	uniform sampler2D lightMap;
	uniform float lightMapIntensity;
#endif`,Iu=`LambertMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularStrength = specularStrength;`,Lu=`varying vec3 vViewPosition;
struct LambertMaterial {
	vec3 diffuseColor;
	float specularStrength;
};
void RE_Direct_Lambert( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Lambert( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in LambertMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Lambert
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Lambert`,Du=`uniform bool receiveShadow;
uniform vec3 ambientLightColor;
#if defined( USE_LIGHT_PROBES )
	uniform vec3 lightProbe[ 9 ];
#endif
vec3 shGetIrradianceAt( in vec3 normal, in vec3 shCoefficients[ 9 ] ) {
	float x = normal.x, y = normal.y, z = normal.z;
	vec3 result = shCoefficients[ 0 ] * 0.886227;
	result += shCoefficients[ 1 ] * 2.0 * 0.511664 * y;
	result += shCoefficients[ 2 ] * 2.0 * 0.511664 * z;
	result += shCoefficients[ 3 ] * 2.0 * 0.511664 * x;
	result += shCoefficients[ 4 ] * 2.0 * 0.429043 * x * y;
	result += shCoefficients[ 5 ] * 2.0 * 0.429043 * y * z;
	result += shCoefficients[ 6 ] * ( 0.743125 * z * z - 0.247708 );
	result += shCoefficients[ 7 ] * 2.0 * 0.429043 * x * z;
	result += shCoefficients[ 8 ] * 0.429043 * ( x * x - y * y );
	return result;
}
vec3 getLightProbeIrradiance( const in vec3 lightProbe[ 9 ], const in vec3 normal ) {
	vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
	vec3 irradiance = shGetIrradianceAt( worldNormal, lightProbe );
	return irradiance;
}
vec3 getAmbientLightIrradiance( const in vec3 ambientLightColor ) {
	vec3 irradiance = ambientLightColor;
	return irradiance;
}
float getDistanceAttenuation( const in float lightDistance, const in float cutoffDistance, const in float decayExponent ) {
	float distanceFalloff = 1.0 / max( pow( lightDistance, decayExponent ), 0.01 );
	if ( cutoffDistance > 0.0 ) {
		distanceFalloff *= pow2( saturate( 1.0 - pow4( lightDistance / cutoffDistance ) ) );
	}
	return distanceFalloff;
}
float getSpotAttenuation( const in float coneCosine, const in float penumbraCosine, const in float angleCosine ) {
	return smoothstep( coneCosine, penumbraCosine, angleCosine );
}
#if NUM_SUN_LIGHTS > 0
	struct SunLight {
		vec3 direction;
		vec3 color;
	};
	uniform SunLight sunLights[ NUM_SUN_LIGHTS ];
	void getSunLightInfo( const in SunLight sunLight, out IncidentLight light ) {
		light.color = sunLight.color;
		light.direction = sunLight.direction;
		light.visible = true;
	}
#endif
#if NUM_DIR_LIGHTS > 0
	struct DirectionalLight {
		vec3 direction;
		vec3 color;
	};
	uniform DirectionalLight directionalLights[ NUM_DIR_LIGHTS ];
	void getDirectionalLightInfo( const in DirectionalLight directionalLight, out IncidentLight light ) {
		light.color = directionalLight.color;
		light.direction = directionalLight.direction;
		light.visible = true;
	}
#endif
#if NUM_POINT_LIGHTS > 0
	struct PointLight {
		vec3 position;
		vec3 color;
		float distance;
		float decay;
	};
	uniform PointLight pointLights[ NUM_POINT_LIGHTS ];
	void getPointLightInfo( const in PointLight pointLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = pointLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float lightDistance = length( lVector );
		light.color = pointLight.color;
		light.color *= getDistanceAttenuation( lightDistance, pointLight.distance, pointLight.decay );
		light.visible = ( light.color != vec3( 0.0 ) );
	}
#endif
#if NUM_SPOT_LIGHTS > 0
	struct SpotLight {
		vec3 position;
		vec3 direction;
		vec3 color;
		float distance;
		float decay;
		float coneCos;
		float penumbraCos;
	};
	uniform SpotLight spotLights[ NUM_SPOT_LIGHTS ];
	void getSpotLightInfo( const in SpotLight spotLight, const in vec3 geometryPosition, out IncidentLight light ) {
		vec3 lVector = spotLight.position - geometryPosition;
		light.direction = normalize( lVector );
		float angleCos = dot( light.direction, spotLight.direction );
		float spotAttenuation = getSpotAttenuation( spotLight.coneCos, spotLight.penumbraCos, angleCos );
		if ( spotAttenuation > 0.0 ) {
			float lightDistance = length( lVector );
			light.color = spotLight.color * spotAttenuation;
			light.color *= getDistanceAttenuation( lightDistance, spotLight.distance, spotLight.decay );
			light.visible = ( light.color != vec3( 0.0 ) );
		} else {
			light.color = vec3( 0.0 );
			light.visible = false;
		}
	}
#endif
#if NUM_RECT_AREA_LIGHTS > 0
	struct RectAreaLight {
		vec3 color;
		vec3 position;
		vec3 halfWidth;
		vec3 halfHeight;
	};
	uniform sampler2D ltc_1;	uniform sampler2D ltc_2;
	uniform RectAreaLight rectAreaLights[ NUM_RECT_AREA_LIGHTS ];
#endif
#if NUM_HEMI_LIGHTS > 0
	struct HemisphereLight {
		vec3 direction;
		vec3 skyColor;
		vec3 groundColor;
	};
	uniform HemisphereLight hemisphereLights[ NUM_HEMI_LIGHTS ];
	vec3 getHemisphereLightIrradiance( const in HemisphereLight hemiLight, const in vec3 normal ) {
		float dotNL = dot( normal, hemiLight.direction );
		float hemiDiffuseWeight = 0.5 * dotNL + 0.5;
		vec3 irradiance = mix( hemiLight.groundColor, hemiLight.skyColor, hemiDiffuseWeight );
		return irradiance;
	}
#endif
#include <lightprobes_pars_fragment>`,Nu=`#ifdef USE_ENVMAP
	vec3 getIBLIrradiance( const in vec3 normal ) {
		#ifdef ENVMAP_TYPE_PMREM
			vec3 worldNormal = transformNormalByInverseViewMatrix( normal, viewMatrix );
			vec4 envMapColor = textureLod( envMap, envMapRotation * worldNormal, ENVMAP_MAX_LOD );
			return PI * envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	vec3 getIBLRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
		#ifdef ENVMAP_TYPE_PMREM
			vec3 reflectVec = reflect( - viewDir, normal );
			reflectVec = normalize( mix( reflectVec, normal, pow4( roughness ) ) );
			reflectVec = transformDirectionByInverseViewMatrix( reflectVec, viewMatrix );
			vec4 envMapColor = textureLod( envMap, envMapRotation * reflectVec, roughnessToMip( roughness ) );
			return envMapColor.rgb * envMapIntensity;
		#else
			return vec3( 0.0 );
		#endif
	}
	#ifdef USE_RETROREFLECTION
		vec3 getIBLRetroRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness ) {
			#ifdef ENVMAP_TYPE_PMREM
				vec3 retroVec = normalize( mix( viewDir, normal, pow4( roughness ) ) );
				retroVec = transformDirectionByInverseViewMatrix( retroVec, viewMatrix );
				vec4 envMapColor = textureLod( envMap, envMapRotation * retroVec, roughnessToMip( roughness ) );
				return envMapColor.rgb * envMapIntensity;
			#else
				return vec3( 0.0 );
			#endif
		}
	#endif
	#ifdef USE_ANISOTROPY
		vec3 getIBLAnisotropyRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
			#ifdef ENVMAP_TYPE_PMREM
				vec3 bentNormal = cross( bitangent, viewDir );
				bentNormal = normalize( cross( bentNormal, bitangent ) );
				bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
				return getIBLRadiance( viewDir, bentNormal, roughness );
			#else
				return vec3( 0.0 );
			#endif
		}
		#ifdef USE_RETROREFLECTION
			vec3 getIBLAnisotropyRetroRadiance( const in vec3 viewDir, const in vec3 normal, const in float roughness, const in vec3 bitangent, const in float anisotropy ) {
				#ifdef ENVMAP_TYPE_PMREM
					vec3 bentNormal = cross( bitangent, viewDir );
					bentNormal = normalize( cross( bentNormal, bitangent ) );
					bentNormal = normalize( mix( bentNormal, normal, pow2( pow2( 1.0 - anisotropy * ( 1.0 - roughness ) ) ) ) );
					return getIBLRetroRadiance( viewDir, bentNormal, roughness );
				#else
					return vec3( 0.0 );
				#endif
			}
		#endif
	#endif
#endif`,Uu=`ToonMaterial material;
material.diffuseColor = diffuseColor.rgb;`,Fu=`varying vec3 vViewPosition;
struct ToonMaterial {
	vec3 diffuseColor;
};
void RE_Direct_Toon( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 irradiance = getGradientIrradiance( geometryNormal, directLight.direction ) * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
void RE_IndirectDiffuse_Toon( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in ToonMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_Toon
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Toon`,Ou=`BlinnPhongMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.specularColor = specular;
material.specularShininess = shininess;
material.specularStrength = specularStrength;`,Bu=`varying vec3 vViewPosition;
struct BlinnPhongMaterial {
	vec3 diffuseColor;
	vec3 specularColor;
	float specularShininess;
	float specularStrength;
};
void RE_Direct_BlinnPhong( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	reflectedLight.directDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
	reflectedLight.directSpecular += irradiance * BRDF_BlinnPhong( directLight.direction, geometryViewDir, geometryNormal, material.specularColor, material.specularShininess ) * material.specularStrength;
}
void RE_IndirectDiffuse_BlinnPhong( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in BlinnPhongMaterial material, inout ReflectedLight reflectedLight ) {
	reflectedLight.indirectDiffuse += irradiance * BRDF_Lambert( material.diffuseColor );
}
#define RE_Direct				RE_Direct_BlinnPhong
#define RE_IndirectDiffuse		RE_IndirectDiffuse_BlinnPhong`,zu=`PhysicalMaterial material;
material.diffuseColor = diffuseColor.rgb;
material.diffuseContribution = diffuseColor.rgb * ( 1.0 - metalnessFactor );
material.metalness = metalnessFactor;
vec3 dxy = max( abs( dFdx( nonPerturbedNormal ) ), abs( dFdy( nonPerturbedNormal ) ) );
float geometryRoughness = max( max( dxy.x, dxy.y ), dxy.z );
material.roughness = max( roughnessFactor, 0.045 );
material.roughness += geometryRoughness;
material.roughness = min( material.roughness, 1.0 );
#ifdef USE_DIFFUSE_ROUGHNESS
	float diffuseRoughnessFactor = diffuseRoughness;
	#ifdef USE_DIFFUSE_ROUGHNESSMAP
		diffuseRoughnessFactor *= texture2D( diffuseRoughnessMap, vDiffuseRoughnessMapUv ).r;
	#endif
	material.diffuseRoughness = saturate( diffuseRoughnessFactor );
#endif
#ifdef IOR
	material.ior = ior;
	#ifdef USE_SPECULAR
		float specularIntensityFactor = specularIntensity;
		vec3 specularColorFactor = specularColor;
		#ifdef USE_SPECULAR_COLORMAP
			specularColorFactor *= texture2D( specularColorMap, vSpecularColorMapUv ).rgb;
		#endif
		#ifdef USE_SPECULAR_INTENSITYMAP
			specularIntensityFactor *= texture2D( specularIntensityMap, vSpecularIntensityMapUv ).a;
		#endif
		material.specularF90 = mix( specularIntensityFactor, 1.0, metalnessFactor );
	#else
		float specularIntensityFactor = 1.0;
		vec3 specularColorFactor = vec3( 1.0 );
		material.specularF90 = 1.0;
	#endif
	material.specularColor = min( pow2( ( material.ior - 1.0 ) / ( material.ior + 1.0 ) ) * specularColorFactor, vec3( 1.0 ) ) * specularIntensityFactor;
	material.specularColorBlended = mix( material.specularColor, diffuseColor.rgb, metalnessFactor );
#else
	material.specularColor = vec3( 0.04 );
	material.specularColorBlended = mix( material.specularColor, diffuseColor.rgb, metalnessFactor );
	material.specularF90 = 1.0;
#endif
#ifdef USE_CLEARCOAT
	material.clearcoat = clearcoat;
	material.clearcoatRoughness = clearcoatRoughness;
	material.clearcoatF0 = vec3( 0.04 );
	material.clearcoatF90 = 1.0;
	#ifdef USE_CLEARCOATMAP
		material.clearcoat *= texture2D( clearcoatMap, vClearcoatMapUv ).x;
	#endif
	#ifdef USE_CLEARCOAT_ROUGHNESSMAP
		material.clearcoatRoughness *= texture2D( clearcoatRoughnessMap, vClearcoatRoughnessMapUv ).y;
	#endif
	material.clearcoat = saturate( material.clearcoat );	material.clearcoatRoughness = max( material.clearcoatRoughness, 0.045 );
	material.clearcoatRoughness += geometryRoughness;
	material.clearcoatRoughness = min( material.clearcoatRoughness, 1.0 );
#endif
#ifdef USE_DISPERSION
	material.dispersion = dispersion;
#endif
#ifdef USE_RETROREFLECTION
	material.retroreflectivity = retroreflectivity;
#endif
#ifdef USE_IRIDESCENCE
	material.iridescence = iridescence;
	material.iridescenceIOR = iridescenceIOR;
	#ifdef USE_IRIDESCENCEMAP
		material.iridescence *= texture2D( iridescenceMap, vIridescenceMapUv ).r;
	#endif
	#ifdef USE_IRIDESCENCE_THICKNESSMAP
		material.iridescenceThickness = (iridescenceThicknessMaximum - iridescenceThicknessMinimum) * texture2D( iridescenceThicknessMap, vIridescenceThicknessMapUv ).g + iridescenceThicknessMinimum;
	#else
		material.iridescenceThickness = iridescenceThicknessMaximum;
	#endif
#endif
#ifdef USE_SHEEN
	material.sheenColor = sheenColor;
	#ifdef USE_SHEEN_COLORMAP
		material.sheenColor *= texture2D( sheenColorMap, vSheenColorMapUv ).rgb;
	#endif
	material.sheenRoughness = clamp( sheenRoughness, 0.0001, 1.0 );
	#ifdef USE_SHEEN_ROUGHNESSMAP
		material.sheenRoughness *= texture2D( sheenRoughnessMap, vSheenRoughnessMapUv ).a;
	#endif
#endif
#ifdef USE_ANISOTROPY
	#ifdef USE_ANISOTROPYMAP
		mat2 anisotropyMat = mat2( anisotropyVector.x, anisotropyVector.y, - anisotropyVector.y, anisotropyVector.x );
		vec3 anisotropyPolar = texture2D( anisotropyMap, vAnisotropyMapUv ).rgb;
		vec2 anisotropyV = anisotropyMat * normalize( 2.0 * anisotropyPolar.rg - vec2( 1.0 ) ) * anisotropyPolar.b;
	#else
		vec2 anisotropyV = anisotropyVector;
	#endif
	material.anisotropy = length( anisotropyV );
	if( material.anisotropy == 0.0 ) {
		anisotropyV = vec2( 1.0, 0.0 );
	} else {
		anisotropyV /= material.anisotropy;
		material.anisotropy = saturate( material.anisotropy );
	}
	material.alphaT = mix( pow2( material.roughness ), 1.0, pow2( material.anisotropy ) );
	material.anisotropyT = tbn[ 0 ] * anisotropyV.x + tbn[ 1 ] * anisotropyV.y;
	material.anisotropyB = tbn[ 1 ] * anisotropyV.x - tbn[ 0 ] * anisotropyV.y;
#endif`,ku=`uniform sampler2D dfgLUT;
struct PhysicalMaterial {
	vec3 diffuseColor;
	vec3 diffuseContribution;
	vec3 specularColor;
	vec3 specularColorBlended;
	float roughness;
	float metalness;
	float specularF90;
	float dispersion;
	vec2 dfg;
	vec3 multiScatteringCompensation;
	#ifdef USE_DIFFUSE_ROUGHNESS
		float diffuseRoughness;
	#endif
	#ifdef USE_RETROREFLECTION
		float retroreflectivity;
	#endif
	#ifdef USE_CLEARCOAT
		float clearcoat;
		float clearcoatRoughness;
		vec3 clearcoatF0;
		float clearcoatF90;
	#endif
	#ifdef USE_IRIDESCENCE
		float iridescence;
		float iridescenceIOR;
		float iridescenceThickness;
		vec3 iridescenceFresnel;
		vec3 iridescenceF0Dielectric;
		vec3 iridescenceF0Metallic;
	#endif
	#ifdef USE_SHEEN
		vec3 sheenColor;
		float sheenRoughness;
	#endif
	#ifdef IOR
		float ior;
	#endif
	#ifdef USE_TRANSMISSION
		float transmission;
		float transmissionAlpha;
		float thickness;
		float attenuationDistance;
		vec3 attenuationColor;
	#endif
	#ifdef USE_ANISOTROPY
		float anisotropy;
		float alphaT;
		vec3 anisotropyT;
		vec3 anisotropyB;
	#endif
};
vec3 clearcoatSpecularDirect = vec3( 0.0 );
vec3 clearcoatSpecularIndirect = vec3( 0.0 );
vec3 sheenSpecularDirect = vec3( 0.0 );
vec3 sheenSpecularIndirect = vec3(0.0 );
vec3 Schlick_to_F0( const in vec3 f, const in float f90, const in float dotVH ) {
    float x = clamp( 1.0 - dotVH, 0.0, 1.0 );
    float x2 = x * x;
    float x5 = clamp( x * x2 * x2, 0.0, 0.9999 );
    return ( f - vec3( f90 ) * x5 ) / ( 1.0 - x5 );
}
#ifdef USE_DIFFUSE_ROUGHNESS
	const float EON_EPSILON = 1e-7;
	float FON_DirectionalAlbedo( const in float mu, const in float roughness, const in float A ) {
		float muComp = 1.0 - mu;
		float gOverPi = muComp * ( 0.0571085289 + muComp * ( 0.491881867 + muComp * ( - 0.332181442 + muComp * 0.0714429953 ) ) );
		return A * ( 1.0 + roughness * gOverPi );
	}
	vec3 BRDF_EON( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in vec3 diffuseColor, const in float roughness ) {
		vec3 rho = saturate( diffuseColor );
		if ( roughness <= EON_EPSILON ) return BRDF_Lambert( rho );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float s = dot( lightDir, viewDir ) - dotNL * dotNV;
		float sOverT = ( s > 0.0 ) ? s / max( max( dotNL, dotNV ), EON_EPSILON ) : s;
		float A = 1.0 / ( 1.0 + ( 0.5 - 2.0 / ( 3.0 * PI ) ) * roughness );
		vec3 singleScatter = rho * RECIPROCAL_PI * A * ( 1.0 + roughness * sOverT );
		float averageAlbedo = A * ( 1.0 + ( 2.0 / 3.0 - 28.0 / ( 15.0 * PI ) ) * roughness );
		float albedoV = FON_DirectionalAlbedo( dotNV, roughness, A );
		float albedoL = FON_DirectionalAlbedo( dotNL, roughness, A );
		vec3 rhoMultiScatter = rho * rho * averageAlbedo / max( vec3( EON_EPSILON ), vec3( 1.0 ) - rho * ( 1.0 - averageAlbedo ) );
		vec3 multiScatter = rhoMultiScatter * RECIPROCAL_PI
			* max( EON_EPSILON, 1.0 - albedoV )
			* max( EON_EPSILON, 1.0 - albedoL )
			/ max( EON_EPSILON, 1.0 - averageAlbedo );
		return singleScatter + multiScatter;
	}
	vec3 EON_DirectionalAlbedo( const in vec3 diffuseColor, const in float roughness, const in float dotNV ) {
		vec3 rho = saturate( diffuseColor );
		if ( roughness <= EON_EPSILON ) return rho;
		float A = 1.0 / ( 1.0 + ( 0.5 - 2.0 / ( 3.0 * PI ) ) * roughness );
		float directionalAlbedo = FON_DirectionalAlbedo( dotNV, roughness, A );
		float averageAlbedo = A * ( 1.0 + ( 2.0 / 3.0 - 28.0 / ( 15.0 * PI ) ) * roughness );
		vec3 rhoMultiScatter = rho * rho * averageAlbedo / max( vec3( EON_EPSILON ), vec3( 1.0 ) - rho * ( 1.0 - averageAlbedo ) );
		return rho * directionalAlbedo + rhoMultiScatter * ( 1.0 - directionalAlbedo );
	}
#endif
float V_GGX_SmithCorrelated( const in float alpha, const in float dotNL, const in float dotNV ) {
	float a2 = pow2( alpha );
	float gv = dotNL * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNV ) );
	float gl = dotNV * sqrt( a2 + ( 1.0 - a2 ) * pow2( dotNL ) );
	return 0.5 / max( gv + gl, EPSILON );
}
float D_GGX( const in float alpha, const in float dotNH ) {
	float a2 = pow2( alpha );
	float denom = pow2( dotNH ) * ( a2 - 1.0 ) + 1.0;
	return RECIPROCAL_PI * a2 / pow2( denom );
}
#ifdef USE_ANISOTROPY
	float V_GGX_SmithCorrelated_Anisotropic( const in float alphaT, const in float alphaB, const in float dotTV, const in float dotBV, const in float dotTL, const in float dotBL, const in float dotNV, const in float dotNL ) {
		float gv = dotNL * length( vec3( alphaT * dotTV, alphaB * dotBV, dotNV ) );
		float gl = dotNV * length( vec3( alphaT * dotTL, alphaB * dotBL, dotNL ) );
		return 0.5 / max( gv + gl, EPSILON );
	}
	float D_GGX_Anisotropic( const in float alphaT, const in float alphaB, const in float dotNH, const in float dotTH, const in float dotBH ) {
		float a2 = alphaT * alphaB;
		highp vec3 v = vec3( alphaB * dotTH, alphaT * dotBH, a2 * dotNH );
		highp float v2 = dot( v, v );
		float w2 = a2 / v2;
		return RECIPROCAL_PI * a2 * pow2 ( w2 );
	}
#endif
#ifdef USE_CLEARCOAT
	vec3 BRDF_GGX_Clearcoat( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material) {
		vec3 f0 = material.clearcoatF0;
		float f90 = material.clearcoatF90;
		float roughness = max( material.clearcoatRoughness, 0.045 );
		float alpha = pow2( roughness );
		vec3 halfDir = normalize( lightDir + viewDir );
		float dotNL = saturate( dot( normal, lightDir ) );
		float dotNV = saturate( dot( normal, viewDir ) );
		float dotNH = saturate( dot( normal, halfDir ) );
		float dotVH = saturate( dot( viewDir, halfDir ) );
		vec3 F = F_Schlick( f0, f90, dotVH );
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
		return F * ( V * D );
	}
#endif
vec3 BRDF_GGX( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, const in PhysicalMaterial material ) {
	vec3 f0 = material.specularColorBlended;
	float f90 = material.specularF90;
	float roughness = max( material.roughness, 0.045 );
	float alpha = pow2( roughness );
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float dotVH = saturate( dot( viewDir, halfDir ) );
	vec3 F = F_Schlick( f0, f90, dotVH );
	#ifdef USE_IRIDESCENCE
		F = mix( F, material.iridescenceFresnel, material.iridescence );
	#endif
	#ifdef USE_ANISOTROPY
		float dotTL = dot( material.anisotropyT, lightDir );
		float dotTV = dot( material.anisotropyT, viewDir );
		float dotTH = dot( material.anisotropyT, halfDir );
		float dotBL = dot( material.anisotropyB, lightDir );
		float dotBV = dot( material.anisotropyB, viewDir );
		float dotBH = dot( material.anisotropyB, halfDir );
		float alphaT = max( material.alphaT, alpha );
		float V = V_GGX_SmithCorrelated_Anisotropic( alphaT, alpha, dotTV, dotBV, dotTL, dotBL, dotNV, dotNL );
		float D = D_GGX_Anisotropic( alphaT, alpha, dotNH, dotTH, dotBH );
	#else
		float V = V_GGX_SmithCorrelated( alpha, dotNL, dotNV );
		float D = D_GGX( alpha, dotNH );
	#endif
	return F * ( V * D );
}
vec2 LTC_Uv( const in vec3 N, const in vec3 V, const in float roughness ) {
	const float LUT_SIZE = 64.0;
	const float LUT_SCALE = ( LUT_SIZE - 1.0 ) / LUT_SIZE;
	const float LUT_BIAS = 0.5 / LUT_SIZE;
	float dotNV = saturate( dot( N, V ) );
	vec2 uv = vec2( roughness, sqrt( 1.0 - dotNV ) );
	uv = uv * LUT_SCALE + LUT_BIAS;
	return uv;
}
float LTC_ClippedSphereFormFactor( const in vec3 f ) {
	float l = length( f );
	return max( ( l * l + f.z ) / ( l + 1.0 ), 0.0 );
}
vec3 LTC_EdgeVectorFormFactor( const in vec3 v1, const in vec3 v2 ) {
	float x = dot( v1, v2 );
	float y = abs( x );
	float a = 0.8543985 + ( 0.4965155 + 0.0145206 * y ) * y;
	float b = 3.4175940 + ( 4.1616724 + y ) * y;
	float v = a / b;
	float theta_sintheta = ( x > 0.0 ) ? v : 0.5 * inversesqrt( max( 1.0 - x * x, 1e-7 ) ) - v;
	return cross( v1, v2 ) * theta_sintheta;
}
vec3 LTC_Evaluate( const in vec3 N, const in vec3 V, const in vec3 P, const in mat3 mInv, const in vec3 rectCoords[ 4 ] ) {
	vec3 v1 = rectCoords[ 1 ] - rectCoords[ 0 ];
	vec3 v2 = rectCoords[ 3 ] - rectCoords[ 0 ];
	vec3 lightNormal = cross( v1, v2 );
	if( dot( lightNormal, P - rectCoords[ 0 ] ) < 0.0 ) return vec3( 0.0 );
	vec3 T1, T2;
	T1 = normalize( V - N * dot( V, N ) );
	T2 = - cross( N, T1 );
	mat3 mat = mInv * transpose( mat3( T1, T2, N ) );
	vec3 coords[ 4 ];
	coords[ 0 ] = mat * ( rectCoords[ 0 ] - P );
	coords[ 1 ] = mat * ( rectCoords[ 1 ] - P );
	coords[ 2 ] = mat * ( rectCoords[ 2 ] - P );
	coords[ 3 ] = mat * ( rectCoords[ 3 ] - P );
	coords[ 0 ] = normalize( coords[ 0 ] );
	coords[ 1 ] = normalize( coords[ 1 ] );
	coords[ 2 ] = normalize( coords[ 2 ] );
	coords[ 3 ] = normalize( coords[ 3 ] );
	vec3 vectorFormFactor = vec3( 0.0 );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 0 ], coords[ 1 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 1 ], coords[ 2 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 2 ], coords[ 3 ] );
	vectorFormFactor += LTC_EdgeVectorFormFactor( coords[ 3 ], coords[ 0 ] );
	float result = LTC_ClippedSphereFormFactor( vectorFormFactor );
	return vec3( result );
}
#if defined( USE_SHEEN )
float D_Charlie( float roughness, float dotNH ) {
	float alpha = pow2( roughness );
	float invAlpha = 1.0 / alpha;
	float cos2h = dotNH * dotNH;
	float sin2h = max( 1.0 - cos2h, 0.0078125 );
	return ( 2.0 + invAlpha ) * pow( sin2h, invAlpha * 0.5 ) / ( 2.0 * PI );
}
float V_Neubelt( float dotNV, float dotNL ) {
	return saturate( 1.0 / ( 4.0 * ( dotNL + dotNV - dotNL * dotNV ) ) );
}
vec3 BRDF_Sheen( const in vec3 lightDir, const in vec3 viewDir, const in vec3 normal, vec3 sheenColor, const in float sheenRoughness ) {
	vec3 halfDir = normalize( lightDir + viewDir );
	float dotNL = saturate( dot( normal, lightDir ) );
	float dotNV = saturate( dot( normal, viewDir ) );
	float dotNH = saturate( dot( normal, halfDir ) );
	float D = D_Charlie( sheenRoughness, dotNH );
	float V = V_Neubelt( dotNV, dotNL );
	return sheenColor * ( D * V );
}
#endif
float IBLSheenBRDF( const in vec3 normal, const in vec3 viewDir, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	float r2 = roughness * roughness;
	float rInv = 1.0 / ( roughness + 0.1 );
	float a = -1.9362 + 1.0678 * roughness + 0.4573 * r2 - 0.8469 * rInv;
	float b = -0.6014 + 0.5538 * roughness - 0.4670 * r2 - 0.1255 * rInv;
	float DG = exp( a * dotNV + b );
	return saturate( DG );
}
vec3 EnvironmentBRDF( const in vec3 normal, const in vec3 viewDir, const in vec3 specularColor, const in float specularF90, const in float roughness ) {
	float dotNV = saturate( dot( normal, viewDir ) );
	vec2 fab = texture2D( dfgLUT, vec2( roughness, dotNV ) ).rg;
	return specularColor * fab.x + specularF90 * fab.y;
}
#ifdef USE_IRIDESCENCE
void computeMultiscatteringIridescence( const in vec2 fab, const in vec3 specularColor, const in float specularF90, const in float iridescence, const in vec3 iridescenceF0, inout vec3 singleScatter, inout vec3 multiScatter ) {
#else
void computeMultiscattering( const in vec2 fab, const in vec3 specularColor, const in float specularF90, inout vec3 singleScatter, inout vec3 multiScatter ) {
#endif
	#ifdef USE_IRIDESCENCE
		vec3 Fr = mix( specularColor, iridescenceF0, iridescence );
	#else
		vec3 Fr = specularColor;
	#endif
	vec3 FssEss = Fr * fab.x + specularF90 * fab.y;
	float Ess = fab.x + fab.y;
	float Ems = 1.0 - Ess;
	vec3 Favg = Fr + ( 1.0 - Fr ) * 0.047619;	vec3 Fms = FssEss * Favg / ( 1.0 - Ems * Favg );
	singleScatter += FssEss;
	multiScatter += Fms * Ems;
}
#if NUM_RECT_AREA_LIGHTS > 0
	void RE_Direct_RectArea_Physical( const in RectAreaLight rectAreaLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
		vec3 normal = geometryNormal;
		vec3 viewDir = geometryViewDir;
		vec3 position = geometryPosition;
		vec3 lightPos = rectAreaLight.position;
		vec3 halfWidth = rectAreaLight.halfWidth;
		vec3 halfHeight = rectAreaLight.halfHeight;
		vec3 lightColor = rectAreaLight.color;
		float roughness = material.roughness;
		vec3 rectCoords[ 4 ];
		rectCoords[ 0 ] = lightPos + halfWidth - halfHeight;		rectCoords[ 1 ] = lightPos - halfWidth - halfHeight;
		rectCoords[ 2 ] = lightPos - halfWidth + halfHeight;
		rectCoords[ 3 ] = lightPos + halfWidth + halfHeight;
		vec2 uv = LTC_Uv( normal, viewDir, roughness );
		vec4 t1 = texture2D( ltc_1, uv );
		vec4 t2 = texture2D( ltc_2, uv );
		mat3 mInv = mat3(
			vec3( t1.x, 0, t1.y ),
			vec3(    0, 1,    0 ),
			vec3( t1.z, 0, t1.w )
		);
		vec3 fresnel = ( material.specularColorBlended * t2.x + ( material.specularF90 - material.specularColorBlended ) * t2.y );
		reflectedLight.directSpecular += lightColor * fresnel * LTC_Evaluate( normal, viewDir, position, mInv, rectCoords );
		reflectedLight.directDiffuse += lightColor * material.diffuseContribution * LTC_Evaluate( normal, viewDir, position, mat3( 1.0 ), rectCoords );
		#ifdef USE_CLEARCOAT
			vec3 Ncc = geometryClearcoatNormal;
			vec2 uvClearcoat = LTC_Uv( Ncc, viewDir, material.clearcoatRoughness );
			vec4 t1Clearcoat = texture2D( ltc_1, uvClearcoat );
			vec4 t2Clearcoat = texture2D( ltc_2, uvClearcoat );
			mat3 mInvClearcoat = mat3(
				vec3( t1Clearcoat.x, 0, t1Clearcoat.y ),
				vec3(             0, 1,             0 ),
				vec3( t1Clearcoat.z, 0, t1Clearcoat.w )
			);
			vec3 fresnelClearcoat = material.clearcoatF0 * t2Clearcoat.x + ( material.clearcoatF90 - material.clearcoatF0 ) * t2Clearcoat.y;
			clearcoatSpecularDirect += lightColor * fresnelClearcoat * LTC_Evaluate( Ncc, viewDir, position, mInvClearcoat, rectCoords );
		#endif
	}
#endif
void RE_Direct_Physical( const in IncidentLight directLight, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	float dotNL = saturate( dot( geometryNormal, directLight.direction ) );
	vec3 irradiance = dotNL * directLight.color;
	#ifdef USE_CLEARCOAT
		float dotNLcc = saturate( dot( geometryClearcoatNormal, directLight.direction ) );
		vec3 ccIrradiance = dotNLcc * directLight.color;
		clearcoatSpecularDirect += ccIrradiance * BRDF_GGX_Clearcoat( directLight.direction, geometryViewDir, geometryClearcoatNormal, material );
	#endif
	#ifdef USE_SHEEN
 
 		sheenSpecularDirect += irradiance * BRDF_Sheen( directLight.direction, geometryViewDir, geometryNormal, material.sheenColor, material.sheenRoughness );
 
 		float sheenAlbedoV = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
 		float sheenAlbedoL = IBLSheenBRDF( geometryNormal, directLight.direction, material.sheenRoughness );
 
 		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * max( sheenAlbedoV, sheenAlbedoL );
 
 		irradiance *= sheenEnergyComp;
 
 	#endif
	vec3 specularBRDF = BRDF_GGX( directLight.direction, geometryViewDir, geometryNormal, material );
	#ifdef USE_RETROREFLECTION
		vec3 retroViewDir = reflect( - geometryViewDir, geometryNormal );
		vec3 retroSpecularBRDF = BRDF_GGX( directLight.direction, retroViewDir, geometryNormal, material );
		specularBRDF = mix( specularBRDF, retroSpecularBRDF, saturate( material.retroreflectivity ) );
	#endif
	reflectedLight.directSpecular += irradiance * specularBRDF * material.multiScatteringCompensation;
	vec3 halfDir = normalize( directLight.direction + geometryViewDir );
	float dotVH = saturate( dot( geometryViewDir, halfDir ) );
	vec3 F = F_Schlick( material.specularColor, material.specularF90, dotVH );
	#ifdef USE_RETROREFLECTION
		vec3 retroHalfDir = normalize( directLight.direction + retroViewDir );
		float dotRetroVH = saturate( dot( retroViewDir, retroHalfDir ) );
		vec3 retroF = F_Schlick( material.specularColor, material.specularF90, dotRetroVH );
		F = mix( F, retroF, saturate( material.retroreflectivity ) );
	#endif
	#ifdef USE_DIFFUSE_ROUGHNESS
		vec3 diffuseBRDF = BRDF_EON( directLight.direction, geometryViewDir, geometryNormal, material.diffuseColor, material.diffuseRoughness ) * ( 1.0 - material.metalness );
	#else
		vec3 diffuseBRDF = BRDF_Lambert( material.diffuseContribution );
	#endif
	reflectedLight.directDiffuse += irradiance * diffuseBRDF * ( 1.0 - F );
}
void RE_IndirectDiffuse_Physical( const in vec3 irradiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight ) {
	vec3 singleScattering = vec3( 0.0 );
	vec3 multiScattering = vec3( 0.0 );
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( material.dfg, material.specularColor, material.specularF90, material.iridescence, material.iridescenceF0Dielectric, singleScattering, multiScattering );
	#else
		computeMultiscattering( material.dfg, material.specularColor, material.specularF90, singleScattering, multiScattering );
	#endif
	#ifdef USE_DIFFUSE_ROUGHNESS
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		vec3 diffuseAlbedo = EON_DirectionalAlbedo( material.diffuseColor, material.diffuseRoughness, dotNV ) * ( 1.0 - material.metalness );
		vec3 diffuse = irradiance * RECIPROCAL_PI * diffuseAlbedo * ( 1.0 - singleScattering - multiScattering );
	#else
		vec3 diffuse = irradiance * BRDF_Lambert( material.diffuseContribution ) * ( 1.0 - singleScattering - multiScattering );
	#endif
	#ifdef USE_SHEEN
		float sheenAlbedo = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
		sheenSpecularIndirect += irradiance * material.sheenColor * sheenAlbedo * RECIPROCAL_PI;
		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * sheenAlbedo;
		diffuse *= sheenEnergyComp;
	#endif
	reflectedLight.indirectDiffuse += diffuse;
}
void RE_IndirectSpecular_Physical( const in vec3 radiance, const in vec3 irradiance, const in vec3 clearcoatRadiance, const in vec3 geometryPosition, const in vec3 geometryNormal, const in vec3 geometryViewDir, const in vec3 geometryClearcoatNormal, const in PhysicalMaterial material, inout ReflectedLight reflectedLight) {
	#ifdef USE_CLEARCOAT
		clearcoatSpecularIndirect += clearcoatRadiance * EnvironmentBRDF( geometryClearcoatNormal, geometryViewDir, material.clearcoatF0, material.clearcoatF90, material.clearcoatRoughness );
	#endif
	#ifdef USE_SHEEN
		sheenSpecularIndirect += irradiance * material.sheenColor * IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness ) * RECIPROCAL_PI;
 	#endif
	vec3 singleScatteringDielectric = vec3( 0.0 );
	vec3 multiScatteringDielectric = vec3( 0.0 );
	vec3 singleScatteringMetallic = vec3( 0.0 );
	vec3 multiScatteringMetallic = vec3( 0.0 );
	#ifdef USE_IRIDESCENCE
		computeMultiscatteringIridescence( material.dfg, material.specularColor, material.specularF90, material.iridescence, material.iridescenceF0Dielectric, singleScatteringDielectric, multiScatteringDielectric );
		computeMultiscatteringIridescence( material.dfg, material.diffuseColor, material.specularF90, material.iridescence, material.iridescenceF0Metallic, singleScatteringMetallic, multiScatteringMetallic );
	#else
		computeMultiscattering( material.dfg, material.specularColor, material.specularF90, singleScatteringDielectric, multiScatteringDielectric );
		computeMultiscattering( material.dfg, material.diffuseColor, material.specularF90, singleScatteringMetallic, multiScatteringMetallic );
	#endif
	vec3 singleScattering = mix( singleScatteringDielectric, singleScatteringMetallic, material.metalness );
	vec3 multiScattering = mix( multiScatteringDielectric, multiScatteringMetallic, material.metalness );
	vec3 totalScatteringDielectric = singleScatteringDielectric + multiScatteringDielectric;
	#ifdef USE_DIFFUSE_ROUGHNESS
		float dotNV = saturate( dot( geometryNormal, geometryViewDir ) );
		vec3 diffuse = EON_DirectionalAlbedo( material.diffuseColor, material.diffuseRoughness, dotNV ) * ( 1.0 - material.metalness ) * ( 1.0 - totalScatteringDielectric );
	#else
		vec3 diffuse = material.diffuseContribution * ( 1.0 - totalScatteringDielectric );
	#endif
	vec3 cosineWeightedIrradiance = irradiance * RECIPROCAL_PI;
	vec3 indirectSpecular = radiance * singleScattering;
	indirectSpecular += multiScattering * cosineWeightedIrradiance;
	vec3 indirectDiffuse = diffuse * cosineWeightedIrradiance;
	#ifdef USE_SHEEN
		float sheenAlbedo = IBLSheenBRDF( geometryNormal, geometryViewDir, material.sheenRoughness );
		float sheenEnergyComp = 1.0 - max3( material.sheenColor ) * sheenAlbedo;
		indirectSpecular *= sheenEnergyComp;
		indirectDiffuse *= sheenEnergyComp;
	#endif
	reflectedLight.indirectSpecular += indirectSpecular;
	reflectedLight.indirectDiffuse += indirectDiffuse;
}
#define RE_Direct				RE_Direct_Physical
#define RE_Direct_RectArea		RE_Direct_RectArea_Physical
#define RE_IndirectDiffuse		RE_IndirectDiffuse_Physical
#define RE_IndirectSpecular		RE_IndirectSpecular_Physical
float computeSpecularOcclusion( const in float dotNV, const in float ambientOcclusion, const in float roughness ) {
	return saturate( pow( dotNV + ambientOcclusion, exp2( - 16.0 * roughness - 1.0 ) ) - 1.0 + ambientOcclusion );
}`,Gu=`
vec3 geometryPosition = - vViewPosition;
vec3 geometryNormal = normal;
vec3 geometryViewDir = ( isOrthographic ) ? vec3( 0, 0, 1 ) : normalize( vViewPosition );
vec3 geometryClearcoatNormal = vec3( 0.0 );
#ifdef USE_CLEARCOAT
	geometryClearcoatNormal = clearcoatNormal;
#endif
#ifdef USE_IRIDESCENCE
	float dotNVi = saturate( dot( normal, geometryViewDir ) );
	if ( material.iridescenceThickness == 0.0 ) {
		material.iridescence = 0.0;
	} else {
		material.iridescence = saturate( material.iridescence );
	}
	if ( material.iridescence > 0.0 ) {
		vec3 iridescenceFresnelDielectric = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.specularColor );
		vec3 iridescenceFresnelMetallic = evalIridescence( 1.0, material.iridescenceIOR, dotNVi, material.iridescenceThickness, material.diffuseColor );
		material.iridescenceFresnel = mix( iridescenceFresnelDielectric, iridescenceFresnelMetallic, material.metalness );
		material.iridescenceF0Dielectric = Schlick_to_F0( iridescenceFresnelDielectric, 1.0, dotNVi );
		material.iridescenceF0Metallic = Schlick_to_F0( iridescenceFresnelMetallic, 1.0, dotNVi );
	}
#endif
#ifdef STANDARD
	float dotNVms = saturate( dot( geometryNormal, geometryViewDir ) );
	material.dfg = texture2D( dfgLUT, vec2( material.roughness, dotNVms ) ).rg;
	#if ( NUM_SUN_LIGHTS > 0 || NUM_DIR_LIGHTS > 0 || NUM_POINT_LIGHTS > 0 || NUM_SPOT_LIGHTS > 0 )
		float EssMs = material.dfg.x + material.dfg.y;
		material.multiScatteringCompensation = 1.0 + material.specularColorBlended * ( 1.0 / EssMs - 1.0 );
	#endif
#endif
IncidentLight directLight;
#if ( NUM_POINT_LIGHTS > 0 ) && defined( RE_Direct )
	PointLight pointLight;
	#if defined( USE_SHADOWMAP ) && NUM_POINT_LIGHT_SHADOWS > 0
	PointLightShadow pointLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHTS; i ++ ) {
		pointLight = pointLights[ i ];
		getPointLightInfo( pointLight, geometryPosition, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_POINT_LIGHT_SHADOWS ) && ( defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_BASIC ) )
		pointLightShadow = pointLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getPointShadow( pointShadowMap[ i ], pointLightShadow.shadowMapSize, pointLightShadow.shadowIntensity, pointLightShadow.shadowBias, pointLightShadow.shadowRadius, vPointShadowCoord[ i ], pointLightShadow.shadowCameraNear, pointLightShadow.shadowCameraFar ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SPOT_LIGHTS > 0 ) && defined( RE_Direct )
	SpotLight spotLight;
	vec4 spotColor;
	vec3 spotLightCoord;
	bool inSpotLightMap;
	#if defined( USE_SHADOWMAP ) && NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHTS; i ++ ) {
		spotLight = spotLights[ i ];
		getSpotLightInfo( spotLight, geometryPosition, directLight );
		#if ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#define SPOT_LIGHT_MAP_INDEX UNROLLED_LOOP_INDEX
		#elif ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		#define SPOT_LIGHT_MAP_INDEX NUM_SPOT_LIGHT_MAPS
		#else
		#define SPOT_LIGHT_MAP_INDEX ( UNROLLED_LOOP_INDEX - NUM_SPOT_LIGHT_SHADOWS + NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS )
		#endif
		#if ( SPOT_LIGHT_MAP_INDEX < NUM_SPOT_LIGHT_MAPS )
			spotLightCoord = vSpotLightCoord[ i ].xyz / vSpotLightCoord[ i ].w;
			inSpotLightMap = all( lessThan( abs( spotLightCoord * 2. - 1. ), vec3( 1.0 ) ) );
			spotColor = texture2D( spotLightMap[ SPOT_LIGHT_MAP_INDEX ], spotLightCoord.xy );
			directLight.color = inSpotLightMap ? directLight.color * spotColor.rgb : directLight.color;
		#endif
		#undef SPOT_LIGHT_MAP_INDEX
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
		spotLightShadow = spotLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( spotShadowMap[ i ], spotLightShadow.shadowMapSize, spotLightShadow.shadowIntensity, spotLightShadow.shadowBias, spotLightShadow.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_SUN_LIGHTS > 0 ) && defined( RE_Direct )
	SunLight sunLight;
	#if defined( USE_SHADOWMAP ) && NUM_SUN_LIGHT_SHADOWS > 0
	SunLightShadow sunLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SUN_LIGHTS; i ++ ) {
		sunLight = sunLights[ i ];
		getSunLightInfo( sunLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_SUN_LIGHT_SHADOWS )
		sunLightShadow = sunLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getSunShadow( sunShadowMap[ i ], sunLightShadow, UNROLLED_LOOP_INDEX ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_DIR_LIGHTS > 0 ) && defined( RE_Direct )
	DirectionalLight directionalLight;
	#if defined( USE_SHADOWMAP ) && NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLightShadow;
	#endif
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHTS; i ++ ) {
		directionalLight = directionalLights[ i ];
		getDirectionalLightInfo( directionalLight, directLight );
		#if defined( USE_SHADOWMAP ) && ( UNROLLED_LOOP_INDEX < NUM_DIR_LIGHT_SHADOWS )
		directionalLightShadow = directionalLightShadows[ i ];
		directLight.color *= ( directLight.visible && receiveShadow ) ? getShadow( directionalShadowMap[ i ], directionalLightShadow.shadowMapSize, directionalLightShadow.shadowIntensity, directionalLightShadow.shadowBias, directionalLightShadow.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
		#endif
		RE_Direct( directLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if ( NUM_RECT_AREA_LIGHTS > 0 ) && defined( RE_Direct_RectArea )
	RectAreaLight rectAreaLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_RECT_AREA_LIGHTS; i ++ ) {
		rectAreaLight = rectAreaLights[ i ];
		RE_Direct_RectArea( rectAreaLight, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
	}
	#pragma unroll_loop_end
#endif
#if defined( RE_IndirectDiffuse )
	vec3 iblIrradiance = vec3( 0.0 );
	vec3 irradiance = getAmbientLightIrradiance( ambientLightColor );
	#if defined( USE_LIGHT_PROBES )
		irradiance += getLightProbeIrradiance( lightProbe, geometryNormal );
	#endif
	#if ( NUM_HEMI_LIGHTS > 0 )
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_HEMI_LIGHTS; i ++ ) {
			irradiance += getHemisphereLightIrradiance( hemisphereLights[ i ], geometryNormal );
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_LIGHT_PROBE_GRIDS > 0
		vec3 probeWorldPos = ( ( vec4( geometryPosition, 1.0 ) - viewMatrix[ 3 ] ) * viewMatrix ).xyz;
		vec3 probeWorldNormal = transformNormalByInverseViewMatrix( geometryNormal, viewMatrix );
		int probeGrid = - 1;
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_LIGHT_PROBE_GRIDS; i ++ ) {
			if ( isInsideLightProbeGrid( probeWorldPos, probeWorldNormal, probesMin[ i ], probesMax[ i ], probesResolution[ i ] ) ) probeGrid = UNROLLED_LOOP_INDEX;
		}
		#pragma unroll_loop_end
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_LIGHT_PROBE_GRIDS; i ++ ) {
			if ( probeGrid == UNROLLED_LOOP_INDEX ) irradiance += getLightProbeGridIrradiance( probesSH[ i ], probesMin[ i ], probesMax[ i ], probesResolution[ i ], probeWorldPos, probeWorldNormal );
		}
		#pragma unroll_loop_end
	#endif
#endif
#if defined( RE_IndirectSpecular )
	vec3 radiance = vec3( 0.0 );
	vec3 clearcoatRadiance = vec3( 0.0 );
#endif`,Vu=`#if defined( RE_IndirectDiffuse )
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		vec3 lightMapIrradiance = lightMapTexel.rgb * lightMapIntensity;
		irradiance += lightMapIrradiance;
	#endif
	#if defined( USE_ENVMAP ) && defined( ENVMAP_TYPE_PMREM )
		#if defined( STANDARD ) || defined( LAMBERT ) || defined( PHONG )
			iblIrradiance += getIBLIrradiance( geometryNormal );
		#endif
	#endif
#endif
#if defined( USE_ENVMAP ) && defined( RE_IndirectSpecular )
	#ifdef USE_ANISOTROPY
		vec3 iblRadiance = getIBLAnisotropyRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
	#else
		vec3 iblRadiance = getIBLRadiance( geometryViewDir, geometryNormal, material.roughness );
	#endif
	#ifdef USE_RETROREFLECTION
		#ifdef USE_ANISOTROPY
			vec3 retroIBLRadiance = getIBLAnisotropyRetroRadiance( geometryViewDir, geometryNormal, material.roughness, material.anisotropyB, material.anisotropy );
		#else
			vec3 retroIBLRadiance = getIBLRetroRadiance( geometryViewDir, geometryNormal, material.roughness );
		#endif
		iblRadiance = mix( iblRadiance, retroIBLRadiance, saturate( material.retroreflectivity ) );
	#endif
	radiance += iblRadiance;
	#ifdef USE_CLEARCOAT
		clearcoatRadiance += getIBLRadiance( geometryViewDir, geometryClearcoatNormal, material.clearcoatRoughness );
	#endif
#endif`,Hu=`#if defined( RE_IndirectDiffuse )
	#if defined( LAMBERT ) || defined( PHONG )
		irradiance += iblIrradiance;
	#endif
	RE_IndirectDiffuse( irradiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif
#if defined( RE_IndirectSpecular )
	RE_IndirectSpecular( radiance, iblIrradiance, clearcoatRadiance, geometryPosition, geometryNormal, geometryViewDir, geometryClearcoatNormal, material, reflectedLight );
#endif`,Wu=`#if NUM_LIGHT_PROBE_GRIDS > 0
uniform highp sampler3D probesSH[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesMin[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesMax[ NUM_LIGHT_PROBE_GRIDS ];
uniform vec3 probesResolution[ NUM_LIGHT_PROBE_GRIDS ];
bool isInsideLightProbeGrid( vec3 worldPos, vec3 worldNormal, vec3 probesMin, vec3 probesMax, vec3 probesResolution ) {
	vec3 spacing = ( probesMax - probesMin ) / probesResolution;
	vec3 samplePos = worldPos + worldNormal * spacing * 0.5;
	vec3 margin = spacing * 0.01;
	return all( greaterThanEqual( samplePos, probesMin - margin ) ) && all( lessThanEqual( samplePos, probesMax + margin ) );
}
vec3 getLightProbeGridIrradiance( highp sampler3D probesSH, vec3 probesMin, vec3 probesMax, vec3 probesResolution, vec3 worldPos, vec3 worldNormal ) {
	vec3 res = probesResolution;
	vec3 gridRange = probesMax - probesMin;
	vec3 probeSpacing = gridRange / res;
	vec3 samplePos = worldPos + worldNormal * probeSpacing * 0.5;
	vec3 uvw = clamp( ( samplePos - probesMin ) / gridRange, 0.5 / res, 1.0 - 0.5 / res );
	float nz          = res.z;
	float paddedSlices = nz + 2.0;
	float atlasDepth  = 7.0 * paddedSlices;
	float uvZBase     = uvw.z * nz + 1.0;
	vec4 s0 = texture( probesSH, vec3( uvw.xy, ( uvZBase                       ) / atlasDepth ) );
	vec4 s1 = texture( probesSH, vec3( uvw.xy, ( uvZBase +       paddedSlices   ) / atlasDepth ) );
	vec4 s2 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 2.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s3 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 3.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s4 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 4.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s5 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 5.0 * paddedSlices   ) / atlasDepth ) );
	vec4 s6 = texture( probesSH, vec3( uvw.xy, ( uvZBase + 6.0 * paddedSlices   ) / atlasDepth ) );
	vec3 c0 = s0.xyz;
	vec3 c1 = vec3( s0.w, s1.xy );
	vec3 c2 = vec3( s1.zw, s2.x );
	vec3 c3 = s2.yzw;
	vec3 c4 = s3.xyz;
	vec3 c5 = vec3( s3.w, s4.xy );
	vec3 c6 = vec3( s4.zw, s5.x );
	vec3 c7 = s5.yzw;
	vec3 c8 = s6.xyz;
	float x = worldNormal.x, y = worldNormal.y, z = worldNormal.z;
	vec3 result = c0 * 0.886227;
	result += c1 * 2.0 * 0.511664 * y;
	result += c2 * 2.0 * 0.511664 * z;
	result += c3 * 2.0 * 0.511664 * x;
	result += c4 * 2.0 * 0.429043 * x * y;
	result += c5 * 2.0 * 0.429043 * y * z;
	result += c6 * ( 0.743125 * z * z - 0.247708 );
	result += c7 * 2.0 * 0.429043 * x * z;
	result += c8 * 0.429043 * ( x * x - y * y );
	return max( result, vec3( 0.0 ) );
}
#endif`,Xu=`#if defined( USE_LOGARITHMIC_DEPTH_BUFFER )
	gl_FragDepth = vIsPerspective == 0.0 ? gl_FragCoord.z : log2( vFragDepth ) * logDepthBufFC * 0.5;
#endif`,qu=`#if defined( USE_LOGARITHMIC_DEPTH_BUFFER )
	uniform float logDepthBufFC;
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Yu=`#ifdef USE_LOGARITHMIC_DEPTH_BUFFER
	varying float vFragDepth;
	varying float vIsPerspective;
#endif`,Zu=`#ifdef USE_LOGARITHMIC_DEPTH_BUFFER
	vFragDepth = 1.0 + gl_Position.w;
	vIsPerspective = float( isPerspectiveMatrix( projectionMatrix ) );
#endif`,Ju=`#ifdef USE_MAP
	vec4 sampledDiffuseColor = texture2D( map, vMapUv );
	#ifdef DECODE_VIDEO_TEXTURE
		sampledDiffuseColor = sRGBTransferEOTF( sampledDiffuseColor );
	#endif
	diffuseColor *= sampledDiffuseColor;
#endif`,$u=`#ifdef USE_MAP
	uniform sampler2D map;
#endif`,Ku=`#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
	#if defined( USE_POINTS_UV )
		vec2 uv = vUv;
	#else
		vec2 uv = ( uvTransform * vec3( gl_PointCoord.x, 1.0 - gl_PointCoord.y, 1 ) ).xy;
	#endif
#endif
#ifdef USE_MAP
	diffuseColor *= texture2D( map, uv );
#endif
#ifdef USE_ALPHAMAP
	diffuseColor.a *= texture2D( alphaMap, uv ).g;
#endif`,ju=`#if defined( USE_POINTS_UV )
	varying vec2 vUv;
#else
	#if defined( USE_MAP ) || defined( USE_ALPHAMAP )
		uniform mat3 uvTransform;
	#endif
#endif
#ifdef USE_MAP
	uniform sampler2D map;
#endif
#ifdef USE_ALPHAMAP
	uniform sampler2D alphaMap;
#endif`,Qu=`float metalnessFactor = metalness;
#ifdef USE_METALNESSMAP
	vec4 texelMetalness = texture2D( metalnessMap, vMetalnessMapUv );
	metalnessFactor *= texelMetalness.b;
#endif`,ed=`#ifdef USE_METALNESSMAP
	uniform sampler2D metalnessMap;
#endif`,td=`#ifdef USE_INSTANCING_MORPH
	float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	float morphTargetBaseInfluence = texelFetch( morphTexture, ivec2( 0, gl_InstanceID ), 0 ).r;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		morphTargetInfluences[i] =  texelFetch( morphTexture, ivec2( i + 1, gl_InstanceID ), 0 ).r;
	}
#endif`,nd=`#if defined( USE_MORPHCOLORS )
	#if defined( USE_COLOR_ALPHA )
		vColor *= morphTargetBaseInfluence;
	#elif defined( USE_COLOR )
		vColor.rgb *= morphTargetBaseInfluence;
	#endif
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		#if defined( USE_COLOR_ALPHA )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor += getMorph( gl_VertexID, i, 2 ) * morphTargetInfluences[ i ];
		#elif defined( USE_COLOR )
			if ( morphTargetInfluences[ i ] != 0.0 ) vColor.rgb += getMorph( gl_VertexID, i, 2 ).rgb * morphTargetInfluences[ i ];
		#endif
	}
#endif`,id=`#ifdef USE_MORPHNORMALS
	objectNormal *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) objectNormal += getMorph( gl_VertexID, i, 1 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,sd=`#ifdef USE_MORPHTARGETS
	#ifndef USE_INSTANCING_MORPH
		uniform float morphTargetBaseInfluence;
		uniform float morphTargetInfluences[ MORPHTARGETS_COUNT ];
	#endif
	uniform sampler2DArray morphTargetsTexture;
	uniform ivec2 morphTargetsTextureSize;
	vec4 getMorph( const in int vertexIndex, const in int morphTargetIndex, const in int offset ) {
		int texelIndex = vertexIndex * MORPHTARGETS_TEXTURE_STRIDE + offset;
		int y = texelIndex / morphTargetsTextureSize.x;
		int x = texelIndex - y * morphTargetsTextureSize.x;
		ivec3 morphUV = ivec3( x, y, morphTargetIndex );
		return texelFetch( morphTargetsTexture, morphUV, 0 );
	}
#endif`,rd=`#ifdef USE_MORPHTARGETS
	transformed *= morphTargetBaseInfluence;
	for ( int i = 0; i < MORPHTARGETS_COUNT; i ++ ) {
		if ( morphTargetInfluences[ i ] != 0.0 ) transformed += getMorph( gl_VertexID, i, 0 ).xyz * morphTargetInfluences[ i ];
	}
#endif`,ad=`float faceDirection = gl_FrontFacing ? 1.0 : - 1.0;
#ifdef FLAT_SHADED
	vec3 fdx = dFdx( vViewPosition );
	vec3 fdy = dFdy( vViewPosition );
	vec3 normal = normalize( cross( fdx, fdy ) );
#else
	vec3 normal = normalize( vNormal );
	#ifdef DOUBLE_SIDED
		normal *= faceDirection;
	#endif
#endif
#if defined( USE_NORMALMAP_TANGENTSPACE ) || defined( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY )
	#ifdef USE_TANGENT
		mat3 tbn = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn = getTangentFrame( - vViewPosition, normal,
		#if defined( USE_NORMALMAP )
			vNormalMapUv
		#elif defined( USE_CLEARCOAT_NORMALMAP )
			vClearcoatNormalMapUv
		#else
			vUv
		#endif
		);
	#endif
	#ifdef DOUBLE_SIDED
		tbn[0] *= faceDirection;
		tbn[1] *= faceDirection;
	#endif
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	#ifdef USE_TANGENT
		mat3 tbn2 = mat3( normalize( vTangent ), normalize( vBitangent ), normal );
	#else
		mat3 tbn2 = getTangentFrame( - vViewPosition, normal, vClearcoatNormalMapUv );
	#endif
	#ifdef DOUBLE_SIDED
		tbn2[0] *= faceDirection;
		tbn2[1] *= faceDirection;
	#endif
#endif
vec3 nonPerturbedNormal = normal;`,od=`#ifdef USE_NORMALMAP_OBJECTSPACE
	normal = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#ifdef FLIP_SIDED
		normal = - normal;
	#endif
	#ifdef DOUBLE_SIDED
		normal = normal * faceDirection;
	#endif
	normal = normalize( normalMatrix * normal );
#elif defined( USE_NORMALMAP_TANGENTSPACE )
	vec3 mapN = texture2D( normalMap, vNormalMapUv ).xyz * 2.0 - 1.0;
	#if defined( USE_PACKED_NORMALMAP )
		mapN = vec3( mapN.xy, sqrt( saturate( 1.0 - dot( mapN.xy, mapN.xy ) ) ) );
	#endif
	mapN.xy *= normalScale;
	normal = normalize( tbn * mapN );
#elif defined( USE_BUMPMAP )
	normal = perturbNormalArb( - vViewPosition, normal, dHdxy_fwd(), faceDirection );
#endif`,ld=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,cd=`#ifndef FLAT_SHADED
	varying vec3 vNormal;
	#ifdef USE_TANGENT
		varying vec3 vTangent;
		varying vec3 vBitangent;
	#endif
#endif`,hd=`#ifndef FLAT_SHADED
	vNormal = normalize( transformedNormal );
	#ifdef USE_TANGENT
		vTangent = normalize( transformedTangent );
		vBitangent = normalize( cross( vNormal, vTangent ) * tangent.w );
		#ifdef FLIP_SIDED
			vBitangent = - vBitangent;
		#endif
	#endif
#endif`,ud=`#ifdef USE_NORMALMAP
	uniform sampler2D normalMap;
	uniform vec2 normalScale;
#endif
#ifdef USE_NORMALMAP_OBJECTSPACE
	uniform mat3 normalMatrix;
#endif
#if ! defined ( USE_TANGENT ) && ( defined ( USE_NORMALMAP_TANGENTSPACE ) || defined ( USE_CLEARCOAT_NORMALMAP ) || defined( USE_ANISOTROPY ) )
	mat3 getTangentFrame( vec3 eye_pos, vec3 surf_norm, vec2 uv ) {
		vec3 q0 = dFdx( eye_pos.xyz );
		vec3 q1 = dFdy( eye_pos.xyz );
		vec2 st0 = dFdx( uv.st );
		vec2 st1 = dFdy( uv.st );
		vec3 N = surf_norm;
		vec3 q1perp = cross( q1, N );
		vec3 q0perp = cross( N, q0 );
		vec3 T = q1perp * st0.x + q0perp * st1.x;
		vec3 B = q1perp * st0.y + q0perp * st1.y;
		float det = max( dot( T, T ), dot( B, B ) );
		float scale = ( det == 0.0 ) ? 0.0 : inversesqrt( det );
		return mat3( T * scale, B * scale, N );
	}
#endif`,dd=`#ifdef USE_CLEARCOAT
	vec3 clearcoatNormal = nonPerturbedNormal;
#endif`,fd=`#ifdef USE_CLEARCOAT_NORMALMAP
	vec3 clearcoatMapN = texture2D( clearcoatNormalMap, vClearcoatNormalMapUv ).xyz * 2.0 - 1.0;
	clearcoatMapN.xy *= clearcoatNormalScale;
	clearcoatNormal = normalize( tbn2 * clearcoatMapN );
#endif`,pd=`#ifdef USE_CLEARCOATMAP
	uniform sampler2D clearcoatMap;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform sampler2D clearcoatNormalMap;
	uniform vec2 clearcoatNormalScale;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform sampler2D clearcoatRoughnessMap;
#endif`,md=`#ifdef USE_IRIDESCENCEMAP
	uniform sampler2D iridescenceMap;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform sampler2D iridescenceThicknessMap;
#endif`,gd=`#ifdef OPAQUE
diffuseColor.a = 1.0;
#endif
#ifdef USE_TRANSMISSION
diffuseColor.a *= material.transmissionAlpha;
#endif
gl_FragColor = vec4( outgoingLight, diffuseColor.a );`,_d=`vec3 packNormalToRGB( const in vec3 normal ) {
	return normalize( normal ) * 0.5 + 0.5;
}
vec3 unpackRGBToNormal( const in vec3 rgb ) {
	return 2.0 * rgb.xyz - 1.0;
}
const float PackUpscale = 256. / 255.;const float UnpackDownscale = 255. / 256.;const float ShiftRight8 = 1. / 256.;
const float Inv255 = 1. / 255.;
const vec4 PackFactors = vec4( 1.0, 256.0, 256.0 * 256.0, 256.0 * 256.0 * 256.0 );
const vec2 UnpackFactors2 = vec2( UnpackDownscale, 1.0 / PackFactors.g );
const vec3 UnpackFactors3 = vec3( UnpackDownscale / PackFactors.rg, 1.0 / PackFactors.b );
const vec4 UnpackFactors4 = vec4( UnpackDownscale / PackFactors.rgb, 1.0 / PackFactors.a );
vec4 packDepthToRGBA( const in float v ) {
	if( v <= 0.0 )
		return vec4( 0., 0., 0., 0. );
	if( v >= 1.0 )
		return vec4( 1., 1., 1., 1. );
	float vuf;
	float af = modf( v * PackFactors.a, vuf );
	float bf = modf( vuf * ShiftRight8, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec4( vuf * Inv255, gf * PackUpscale, bf * PackUpscale, af );
}
vec3 packDepthToRGB( const in float v ) {
	if( v <= 0.0 )
		return vec3( 0., 0., 0. );
	if( v >= 1.0 )
		return vec3( 1., 1., 1. );
	float vuf;
	float bf = modf( v * PackFactors.b, vuf );
	float gf = modf( vuf * ShiftRight8, vuf );
	return vec3( vuf * Inv255, gf * PackUpscale, bf );
}
vec2 packDepthToRG( const in float v ) {
	if( v <= 0.0 )
		return vec2( 0., 0. );
	if( v >= 1.0 )
		return vec2( 1., 1. );
	float vuf;
	float gf = modf( v * 256., vuf );
	return vec2( vuf * Inv255, gf );
}
float unpackRGBAToDepth( const in vec4 v ) {
	return dot( v, UnpackFactors4 );
}
float unpackRGBToDepth( const in vec3 v ) {
	return dot( v, UnpackFactors3 );
}
float unpackRGToDepth( const in vec2 v ) {
	return v.r * UnpackFactors2.r + v.g * UnpackFactors2.g;
}
vec4 pack2HalfToRGBA( const in vec2 v ) {
	vec4 r = vec4( v.x, fract( v.x * 255.0 ), v.y, fract( v.y * 255.0 ) );
	return vec4( r.x - r.y / 255.0, r.y, r.z - r.w / 255.0, r.w );
}
vec2 unpackRGBATo2Half( const in vec4 v ) {
	return vec2( v.x + ( v.y / 255.0 ), v.z + ( v.w / 255.0 ) );
}
float viewZToOrthographicDepth( const in float viewZ, const in float near, const in float far ) {
	return ( viewZ + near ) / ( near - far );
}
float orthographicDepthToViewZ( const in float depth, const in float near, const in float far ) {
	#ifdef USE_REVERSED_DEPTH_BUFFER
	
		return depth * ( far - near ) - far;
	#else
		return depth * ( near - far ) - near;
	#endif
}
float viewZToPerspectiveDepth( const in float viewZ, const in float near, const in float far ) {
	return ( ( near + viewZ ) * far ) / ( ( far - near ) * viewZ );
}
float perspectiveDepthToViewZ( const in float depth, const in float near, const in float far ) {
	
	#ifdef USE_REVERSED_DEPTH_BUFFER
		return ( near * far ) / ( ( near - far ) * depth - near );
	#else
		return ( near * far ) / ( ( far - near ) * depth - far );
	#endif
}`,xd=`#ifdef PREMULTIPLIED_ALPHA
	gl_FragColor.rgb *= gl_FragColor.a;
#endif`,yd=`vec4 mvPosition = vec4( transformed, 1.0 );
#ifdef USE_BATCHING
	mvPosition = batchingMatrix * mvPosition;
#endif
#ifdef USE_INSTANCING
	mvPosition = instanceMatrix * mvPosition;
#endif
mvPosition = modelViewMatrix * mvPosition;
gl_Position = projectionMatrix * mvPosition;`,vd=`#ifdef DITHERING
	gl_FragColor.rgb = dithering( gl_FragColor.rgb );
#endif`,Sd=`#ifdef DITHERING
	vec3 dithering( vec3 color ) {
		float grid_position = rand( gl_FragCoord.xy );
		vec3 dither_shift_RGB = vec3( 0.25 / 255.0, -0.25 / 255.0, 0.25 / 255.0 );
		dither_shift_RGB = mix( 2.0 * dither_shift_RGB, -2.0 * dither_shift_RGB, grid_position );
		return color + dither_shift_RGB;
	}
#endif`,Md=`float roughnessFactor = roughness;
#ifdef USE_ROUGHNESSMAP
	vec4 texelRoughness = texture2D( roughnessMap, vRoughnessMapUv );
	roughnessFactor *= texelRoughness.g;
#endif`,bd=`#ifdef USE_ROUGHNESSMAP
	uniform sampler2D roughnessMap;
#endif`,Ed=`#if NUM_SPOT_LIGHT_COORDS > 0
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#if NUM_SPOT_LIGHT_MAPS > 0
	uniform sampler2D spotLightMap[ NUM_SPOT_LIGHT_MAPS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
		#define SUN_LIGHT_CASCADES 2
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow sunShadowMap[ NUM_SUN_LIGHT_SHADOWS ];
		#else
			uniform sampler2D sunShadowMap[ NUM_SUN_LIGHT_SHADOWS ];
		#endif
		uniform mat4 sunShadowMatrix[ NUM_SUN_LIGHT_SHADOWS * SUN_LIGHT_CASCADES ];
		uniform vec4 sunShadowCascade[ NUM_SUN_LIGHT_SHADOWS * SUN_LIGHT_CASCADES ];
		varying vec4 vSunShadowWorldPosition;
		varying vec3 vSunShadowWorldNormal;
		struct SunLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SunLightShadow sunLightShadows[ NUM_SUN_LIGHT_SHADOWS ];
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		#else
			uniform sampler2D directionalShadowMap[ NUM_DIR_LIGHT_SHADOWS ];
		#endif
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform sampler2DShadow spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		#else
			uniform sampler2D spotShadowMap[ NUM_SPOT_LIGHT_SHADOWS ];
		#endif
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#if defined( SHADOWMAP_TYPE_PCF )
			uniform samplerCubeShadow pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		#elif defined( SHADOWMAP_TYPE_BASIC )
			uniform samplerCube pointShadowMap[ NUM_POINT_LIGHT_SHADOWS ];
		#endif
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
	#if defined( SHADOWMAP_TYPE_PCF )
		float interleavedGradientNoise( vec2 position ) {
			return fract( 52.9829189 * fract( dot( position, vec2( 0.06711056, 0.00583715 ) ) ) );
		}
		vec2 vogelDiskSample( int sampleIndex, int samplesCount, float phi ) {
			const float goldenAngle = 2.399963229728653;
			float r = sqrt( ( float( sampleIndex ) + 0.5 ) / float( samplesCount ) );
			float theta = float( sampleIndex ) * goldenAngle + phi;
			return vec2( cos( theta ), sin( theta ) ) * r;
		}
	#endif
	#if defined( SHADOWMAP_TYPE_PCF )
		float getShadow( sampler2DShadow shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				vec2 texelSize = vec2( 1.0 ) / shadowMapSize;
				vec2 radius = shadowRadius * texelSize;
				float phi = interleavedGradientNoise( gl_FragCoord.xy ) * PI2;
				shadow = (
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 0, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 1, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 2, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 3, 5, phi ) * radius, shadowCoord.z ) ) +
					texture( shadowMap, vec3( shadowCoord.xy + vogelDiskSample( 4, 5, phi ) * radius, shadowCoord.z ) )
				) * 0.2;
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#elif defined( SHADOWMAP_TYPE_VSM )
		float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				vec2 distribution = texture2D( shadowMap, shadowCoord.xy ).rg;
				float mean = distribution.x;
				float variance = distribution.y * distribution.y;
				#ifdef USE_REVERSED_DEPTH_BUFFER
					float hard_shadow = step( mean, shadowCoord.z );
				#else
					float hard_shadow = step( shadowCoord.z, mean );
				#endif
				
				if ( hard_shadow == 1.0 ) {
					shadow = 1.0;
				} else {
					variance = max( variance, 0.0000001 );
					float d = shadowCoord.z - mean;
					float p_max = variance / ( variance + d * d );
					p_max = clamp( ( p_max - 0.3 ) / 0.65, 0.0, 1.0 );
					shadow = max( hard_shadow, p_max );
				}
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#else
		float getShadow( sampler2D shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord ) {
			float shadow = 1.0;
			shadowCoord.xyz /= shadowCoord.w;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				shadowCoord.z -= shadowBias;
			#else
				shadowCoord.z += shadowBias;
			#endif
			bool inFrustum = shadowCoord.x >= 0.0 && shadowCoord.x <= 1.0 && shadowCoord.y >= 0.0 && shadowCoord.y <= 1.0;
			bool frustumTest = inFrustum && shadowCoord.z <= 1.0;
			if ( frustumTest ) {
				float depth = texture2D( shadowMap, shadowCoord.xy ).r;
				#ifdef USE_REVERSED_DEPTH_BUFFER
					shadow = step( depth, shadowCoord.z );
				#else
					shadow = step( shadowCoord.z, depth );
				#endif
			}
			return mix( 1.0, shadow, shadowIntensity );
		}
	#endif
	#if NUM_SUN_LIGHT_SHADOWS > 0
		float getSunShadow(
			#if defined( SHADOWMAP_TYPE_PCF )
				sampler2DShadow shadowMap,
			#else
				sampler2D shadowMap,
			#endif
			SunLightShadow sunLightShadow,
			int shadowIndex
		) {
			vec4 shadowWorldPosition = vec4( vSunShadowWorldPosition.xyz + vSunShadowWorldNormal * sunLightShadow.shadowNormalBias, 1.0 );
			float viewDepth = vSunShadowWorldPosition.w;
			int cascadeOffset = shadowIndex * SUN_LIGHT_CASCADES;
			float shadow = 1.0;
			for ( int i = SUN_LIGHT_CASCADES - 1; i >= 0; i -- ) {
				vec4 cascade = sunShadowCascade[ cascadeOffset + i ];
				if ( viewDepth >= cascade.x && viewDepth < cascade.y ) {
					float cascadeShadow = getShadow(
						shadowMap,
						sunLightShadow.shadowMapSize,
						sunLightShadow.shadowIntensity,
						sunLightShadow.shadowBias,
						sunLightShadow.shadowRadius,
						sunShadowMatrix[ cascadeOffset + i ] * shadowWorldPosition
					);
					shadow = mix( cascadeShadow, shadow, smoothstep( cascade.z, cascade.y, viewDepth ) );
				}
			}
			return shadow;
		}
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
	#if defined( SHADOWMAP_TYPE_PCF )
	float getPointShadow( samplerCubeShadow shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		vec3 bd3D = normalize( lightToPosition );
		vec3 absVec = abs( lightToPosition );
		float viewSpaceZ = max( max( absVec.x, absVec.y ), absVec.z );
		if ( viewSpaceZ - shadowCameraFar <= 0.0 && viewSpaceZ - shadowCameraNear >= 0.0 ) {
			float lightDistance = length( lightToPosition );
			float depthRange = shadowCameraFar - shadowCameraNear;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				float depthA = - shadowCameraNear / depthRange - shadowBias;
				float depthB = shadowCameraNear * shadowCameraFar / ( depthRange * lightDistance );
			#else
				float depthA = shadowCameraFar / depthRange + shadowBias;
				float depthB = - shadowCameraNear * shadowCameraFar / ( depthRange * lightDistance );
			#endif
			float texelSize = shadowRadius / shadowMapSize.x;
			vec3 absDir = abs( bd3D );
			vec3 tangent = absDir.x > absDir.z ? vec3( 0.0, 1.0, 0.0 ) : vec3( 1.0, 0.0, 0.0 );
			tangent = normalize( cross( bd3D, tangent ) );
			vec3 bitangent = cross( bd3D, tangent );
			float phi = interleavedGradientNoise( gl_FragCoord.xy ) * PI2;
			shadow = 0.0;
			for ( int i = 0; i < 5; i ++ ) {
				vec2 offset = vogelDiskSample( i, 5, phi );
				vec3 direction = bd3D + ( tangent * offset.x + bitangent * offset.y ) * texelSize;
				vec3 absDirection = abs( direction );
				float dp = depthA + depthB / max( max( absDirection.x, absDirection.y ), absDirection.z );
				shadow += texture( shadowMap, vec4( direction, dp ) );
			}
			shadow *= 0.2;
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	#elif defined( SHADOWMAP_TYPE_BASIC )
	float getPointShadow( samplerCube shadowMap, vec2 shadowMapSize, float shadowIntensity, float shadowBias, float shadowRadius, vec4 shadowCoord, float shadowCameraNear, float shadowCameraFar ) {
		float shadow = 1.0;
		vec3 lightToPosition = shadowCoord.xyz;
		vec3 absVec = abs( lightToPosition );
		float viewSpaceZ = max( max( absVec.x, absVec.y ), absVec.z );
		if ( viewSpaceZ - shadowCameraFar <= 0.0 && viewSpaceZ - shadowCameraNear >= 0.0 ) {
			float dp = ( shadowCameraFar * ( viewSpaceZ - shadowCameraNear ) ) / ( viewSpaceZ * ( shadowCameraFar - shadowCameraNear ) );
			dp += shadowBias;
			vec3 bd3D = normalize( lightToPosition );
			float depth = textureCube( shadowMap, bd3D ).r;
			#ifdef USE_REVERSED_DEPTH_BUFFER
				depth = 1.0 - depth;
			#endif
			shadow = step( dp, depth );
		}
		return mix( 1.0, shadow, shadowIntensity );
	}
	#endif
	#endif
#endif`,Td=`#if NUM_SPOT_LIGHT_COORDS > 0
	uniform mat4 spotLightMatrix[ NUM_SPOT_LIGHT_COORDS ];
	varying vec4 vSpotLightCoord[ NUM_SPOT_LIGHT_COORDS ];
#endif
#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
		varying vec4 vSunShadowWorldPosition;
		varying vec3 vSunShadowWorldNormal;
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		uniform mat4 directionalShadowMatrix[ NUM_DIR_LIGHT_SHADOWS ];
		varying vec4 vDirectionalShadowCoord[ NUM_DIR_LIGHT_SHADOWS ];
		struct DirectionalLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform DirectionalLightShadow directionalLightShadows[ NUM_DIR_LIGHT_SHADOWS ];
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
		struct SpotLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
		};
		uniform SpotLightShadow spotLightShadows[ NUM_SPOT_LIGHT_SHADOWS ];
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		uniform mat4 pointShadowMatrix[ NUM_POINT_LIGHT_SHADOWS ];
		varying vec4 vPointShadowCoord[ NUM_POINT_LIGHT_SHADOWS ];
		struct PointLightShadow {
			float shadowIntensity;
			float shadowBias;
			float shadowNormalBias;
			float shadowRadius;
			vec2 shadowMapSize;
			float shadowCameraNear;
			float shadowCameraFar;
		};
		uniform PointLightShadow pointLightShadows[ NUM_POINT_LIGHT_SHADOWS ];
	#endif
#endif`,Ad=`#if ( defined( USE_SHADOWMAP ) && ( NUM_DIR_LIGHT_SHADOWS > 0 || NUM_SUN_LIGHT_SHADOWS > 0 || NUM_POINT_LIGHT_SHADOWS > 0 ) ) || ( NUM_SPOT_LIGHT_COORDS > 0 )
	#ifdef HAS_NORMAL
		vec3 shadowWorldNormal = transformNormalByInverseViewMatrix( transformedNormal, viewMatrix );
	#else
		vec3 shadowWorldNormal = vec3( 0.0 );
	#endif
	vec4 shadowWorldPosition;
#endif
#if defined( USE_SHADOWMAP )
	#if NUM_SUN_LIGHT_SHADOWS > 0
		vSunShadowWorldPosition = vec4( worldPosition.xyz, - mvPosition.z );
		vSunShadowWorldNormal = shadowWorldNormal;
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * directionalLightShadows[ i ].shadowNormalBias, 0 );
			vDirectionalShadowCoord[ i ] = directionalShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0
		#pragma unroll_loop_start
		for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
			shadowWorldPosition = worldPosition + vec4( shadowWorldNormal * pointLightShadows[ i ].shadowNormalBias, 0 );
			vPointShadowCoord[ i ] = pointShadowMatrix[ i ] * shadowWorldPosition;
		}
		#pragma unroll_loop_end
	#endif
#endif
#if NUM_SPOT_LIGHT_COORDS > 0
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_COORDS; i ++ ) {
		shadowWorldPosition = worldPosition;
		#if ( defined( USE_SHADOWMAP ) && UNROLLED_LOOP_INDEX < NUM_SPOT_LIGHT_SHADOWS )
			shadowWorldPosition.xyz += shadowWorldNormal * spotLightShadows[ i ].shadowNormalBias;
		#endif
		vSpotLightCoord[ i ] = spotLightMatrix[ i ] * shadowWorldPosition;
	}
	#pragma unroll_loop_end
#endif`,wd=`float getShadowMask() {
	float shadow = 1.0;
	#ifdef USE_SHADOWMAP
	#if NUM_SUN_LIGHT_SHADOWS > 0
	SunLightShadow sunLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SUN_LIGHT_SHADOWS; i ++ ) {
		sunLight = sunLightShadows[ i ];
		shadow *= receiveShadow ? getSunShadow( sunShadowMap[ i ], sunLight, UNROLLED_LOOP_INDEX ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_DIR_LIGHT_SHADOWS > 0
	DirectionalLightShadow directionalLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_DIR_LIGHT_SHADOWS; i ++ ) {
		directionalLight = directionalLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( directionalShadowMap[ i ], directionalLight.shadowMapSize, directionalLight.shadowIntensity, directionalLight.shadowBias, directionalLight.shadowRadius, vDirectionalShadowCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_SPOT_LIGHT_SHADOWS > 0
	SpotLightShadow spotLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_SPOT_LIGHT_SHADOWS; i ++ ) {
		spotLight = spotLightShadows[ i ];
		shadow *= receiveShadow ? getShadow( spotShadowMap[ i ], spotLight.shadowMapSize, spotLight.shadowIntensity, spotLight.shadowBias, spotLight.shadowRadius, vSpotLightCoord[ i ] ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#if NUM_POINT_LIGHT_SHADOWS > 0 && ( defined( SHADOWMAP_TYPE_PCF ) || defined( SHADOWMAP_TYPE_BASIC ) )
	PointLightShadow pointLight;
	#pragma unroll_loop_start
	for ( int i = 0; i < NUM_POINT_LIGHT_SHADOWS; i ++ ) {
		pointLight = pointLightShadows[ i ];
		shadow *= receiveShadow ? getPointShadow( pointShadowMap[ i ], pointLight.shadowMapSize, pointLight.shadowIntensity, pointLight.shadowBias, pointLight.shadowRadius, vPointShadowCoord[ i ], pointLight.shadowCameraNear, pointLight.shadowCameraFar ) : 1.0;
	}
	#pragma unroll_loop_end
	#endif
	#endif
	return shadow;
}`,Rd=`#ifdef USE_SKINNING
	mat4 boneMatX = getBoneMatrix( skinIndex.x );
	mat4 boneMatY = getBoneMatrix( skinIndex.y );
	mat4 boneMatZ = getBoneMatrix( skinIndex.z );
	mat4 boneMatW = getBoneMatrix( skinIndex.w );
#endif`,Cd=`#ifdef USE_SKINNING
	uniform mat4 bindMatrix;
	uniform mat4 bindMatrixInverse;
	uniform highp sampler2D boneTexture;
	mat4 getBoneMatrix( const in float i ) {
		int size = textureSize( boneTexture, 0 ).x;
		int j = int( i ) * 4;
		int x = j % size;
		int y = j / size;
		vec4 v1 = texelFetch( boneTexture, ivec2( x, y ), 0 );
		vec4 v2 = texelFetch( boneTexture, ivec2( x + 1, y ), 0 );
		vec4 v3 = texelFetch( boneTexture, ivec2( x + 2, y ), 0 );
		vec4 v4 = texelFetch( boneTexture, ivec2( x + 3, y ), 0 );
		return mat4( v1, v2, v3, v4 );
	}
#endif`,Pd=`#ifdef USE_SKINNING
	vec4 skinVertex = bindMatrix * vec4( transformed, 1.0 );
	vec4 skinned = vec4( 0.0 );
	skinned += boneMatX * skinVertex * skinWeight.x;
	skinned += boneMatY * skinVertex * skinWeight.y;
	skinned += boneMatZ * skinVertex * skinWeight.z;
	skinned += boneMatW * skinVertex * skinWeight.w;
	transformed = ( bindMatrixInverse * skinned ).xyz;
#endif`,Id=`#ifdef USE_SKINNING
	mat4 skinMatrix = mat4( 0.0 );
	skinMatrix += skinWeight.x * boneMatX;
	skinMatrix += skinWeight.y * boneMatY;
	skinMatrix += skinWeight.z * boneMatZ;
	skinMatrix += skinWeight.w * boneMatW;
	skinMatrix = bindMatrixInverse * skinMatrix * bindMatrix;
	objectNormal = vec4( skinMatrix * vec4( objectNormal, 0.0 ) ).xyz;
	#ifdef USE_TANGENT
		objectTangent = vec4( skinMatrix * vec4( objectTangent, 0.0 ) ).xyz;
	#endif
#endif`,Ld=`float specularStrength;
#ifdef USE_SPECULARMAP
	vec4 texelSpecular = texture2D( specularMap, vSpecularMapUv );
	specularStrength = texelSpecular.r;
#else
	specularStrength = 1.0;
#endif`,Dd=`#ifdef USE_SPECULARMAP
	uniform sampler2D specularMap;
#endif`,Nd=`#if defined( TONE_MAPPING )
	gl_FragColor.rgb = toneMapping( gl_FragColor.rgb );
#endif`,Ud=`#ifndef saturate
#define saturate( a ) clamp( a, 0.0, 1.0 )
#endif
uniform float toneMappingExposure;
vec3 LinearToneMapping( vec3 color ) {
	return saturate( toneMappingExposure * color );
}
vec3 ReinhardToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	return saturate( color / ( vec3( 1.0 ) + color ) );
}
vec3 CineonToneMapping( vec3 color ) {
	color *= toneMappingExposure;
	color = max( vec3( 0.0 ), color - 0.004 );
	return pow( ( color * ( 6.2 * color + 0.5 ) ) / ( color * ( 6.2 * color + 1.7 ) + 0.06 ), vec3( 2.2 ) );
}
vec3 RRTAndODTFit( vec3 v ) {
	vec3 a = v * ( v + 0.0245786 ) - 0.000090537;
	vec3 b = v * ( 0.983729 * v + 0.4329510 ) + 0.238081;
	return a / b;
}
vec3 ACESFilmicToneMapping( vec3 color ) {
	const mat3 ACESInputMat = mat3(
		vec3( 0.59719, 0.07600, 0.02840 ),		vec3( 0.35458, 0.90834, 0.13383 ),
		vec3( 0.04823, 0.01566, 0.83777 )
	);
	const mat3 ACESOutputMat = mat3(
		vec3(  1.60475, -0.10208, -0.00327 ),		vec3( -0.53108,  1.10813, -0.07276 ),
		vec3( -0.07367, -0.00605,  1.07602 )
	);
	color *= toneMappingExposure / 0.6;
	color = ACESInputMat * color;
	color = RRTAndODTFit( color );
	color = ACESOutputMat * color;
	return saturate( color );
}
const mat3 LINEAR_REC2020_TO_LINEAR_SRGB = mat3(
	vec3( 1.6605, - 0.1246, - 0.0182 ),
	vec3( - 0.5876, 1.1329, - 0.1006 ),
	vec3( - 0.0728, - 0.0083, 1.1187 )
);
const mat3 LINEAR_SRGB_TO_LINEAR_REC2020 = mat3(
	vec3( 0.6274, 0.0691, 0.0164 ),
	vec3( 0.3293, 0.9195, 0.0880 ),
	vec3( 0.0433, 0.0113, 0.8956 )
);
vec3 agxDefaultContrastApprox( vec3 x ) {
	vec3 x2 = x * x;
	vec3 x4 = x2 * x2;
	return + 15.5 * x4 * x2
		- 40.14 * x4 * x
		+ 31.96 * x4
		- 6.868 * x2 * x
		+ 0.4298 * x2
		+ 0.1191 * x
		- 0.00232;
}
vec3 AgXToneMapping( vec3 color ) {
	const mat3 AgXInsetMatrix = mat3(
		vec3( 0.856627153315983, 0.137318972929847, 0.11189821299995 ),
		vec3( 0.0951212405381588, 0.761241990602591, 0.0767994186031903 ),
		vec3( 0.0482516061458583, 0.101439036467562, 0.811302368396859 )
	);
	const mat3 AgXOutsetMatrix = mat3(
		vec3( 1.1271005818144368, - 0.1413297634984383, - 0.14132976349843826 ),
		vec3( - 0.11060664309660323, 1.157823702216272, - 0.11060664309660294 ),
		vec3( - 0.016493938717834573, - 0.016493938717834257, 1.2519364065950405 )
	);
	const float AgxMinEv = - 12.47393;	const float AgxMaxEv = 4.026069;
	color *= toneMappingExposure;
	color = LINEAR_SRGB_TO_LINEAR_REC2020 * color;
	color = AgXInsetMatrix * color;
	color = max( color, 1e-10 );	color = log2( color );
	color = ( color - AgxMinEv ) / ( AgxMaxEv - AgxMinEv );
	color = clamp( color, 0.0, 1.0 );
	color = agxDefaultContrastApprox( color );
	color = AgXOutsetMatrix * color;
	color = pow( max( vec3( 0.0 ), color ), vec3( 2.2 ) );
	color = LINEAR_REC2020_TO_LINEAR_SRGB * color;
	color = clamp( color, 0.0, 1.0 );
	return color;
}
vec3 NeutralToneMapping( vec3 color ) {
	const float StartCompression = 0.8 - 0.04;
	const float Desaturation = 0.15;
	color *= toneMappingExposure;
	float x = min( color.r, min( color.g, color.b ) );
	float offset = x < 0.08 ? x - 6.25 * x * x : 0.04;
	color -= offset;
	float peak = max( color.r, max( color.g, color.b ) );
	if ( peak < StartCompression ) return color;
	float d = 1. - StartCompression;
	float newPeak = 1. - d * d / ( peak + d - StartCompression );
	color *= newPeak / peak;
	float g = 1. - 1. / ( Desaturation * ( peak - newPeak ) + 1. );
	return mix( color, vec3( newPeak ), g );
}
vec3 CustomToneMapping( vec3 color ) { return color; }`,Fd=`#ifdef USE_TRANSMISSION
	material.transmission = transmission;
	material.transmissionAlpha = 1.0;
	material.thickness = thickness;
	material.attenuationDistance = attenuationDistance;
	material.attenuationColor = attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		material.transmission *= texture2D( transmissionMap, vTransmissionMapUv ).r;
	#endif
	#ifdef USE_THICKNESSMAP
		material.thickness *= texture2D( thicknessMap, vThicknessMapUv ).g;
	#endif
	vec3 pos = vWorldPosition;
	vec3 v = normalize( cameraPosition - pos );
	vec3 n = transformNormalByInverseViewMatrix( normal, viewMatrix );
	vec4 transmitted = getIBLVolumeRefraction(
		n, v, material.roughness, material.diffuseContribution, material.specularColorBlended, material.specularF90,
		pos, modelMatrix, viewMatrix, projectionMatrix, material.dispersion, material.ior, material.thickness,
		material.attenuationColor, material.attenuationDistance );
	material.transmissionAlpha = mix( material.transmissionAlpha, transmitted.a, material.transmission );
	totalDiffuse = mix( totalDiffuse, transmitted.rgb, material.transmission );
#endif`,Od=`#ifdef USE_TRANSMISSION
	uniform float transmission;
	uniform float thickness;
	uniform float attenuationDistance;
	uniform vec3 attenuationColor;
	#ifdef USE_TRANSMISSIONMAP
		uniform sampler2D transmissionMap;
	#endif
	#ifdef USE_THICKNESSMAP
		uniform sampler2D thicknessMap;
	#endif
	uniform vec2 transmissionSamplerSize;
	uniform sampler2D transmissionSamplerMap;
	uniform mat4 modelMatrix;
	uniform mat4 projectionMatrix;
	varying vec3 vWorldPosition;
	float w0( float a ) {
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - a + 3.0 ) - 3.0 ) + 1.0 );
	}
	float w1( float a ) {
		return ( 1.0 / 6.0 ) * ( a *  a * ( 3.0 * a - 6.0 ) + 4.0 );
	}
	float w2( float a ){
		return ( 1.0 / 6.0 ) * ( a * ( a * ( - 3.0 * a + 3.0 ) + 3.0 ) + 1.0 );
	}
	float w3( float a ) {
		return ( 1.0 / 6.0 ) * ( a * a * a );
	}
	float g0( float a ) {
		return w0( a ) + w1( a );
	}
	float g1( float a ) {
		return w2( a ) + w3( a );
	}
	float h0( float a ) {
		return - 1.0 + w1( a ) / ( w0( a ) + w1( a ) );
	}
	float h1( float a ) {
		return 1.0 + w3( a ) / ( w2( a ) + w3( a ) );
	}
	vec4 bicubic( sampler2D tex, vec2 uv, vec4 texelSize, float lod ) {
		uv = uv * texelSize.zw + 0.5;
		vec2 iuv = floor( uv );
		vec2 fuv = fract( uv );
		float g0x = g0( fuv.x );
		float g1x = g1( fuv.x );
		float h0x = h0( fuv.x );
		float h1x = h1( fuv.x );
		float h0y = h0( fuv.y );
		float h1y = h1( fuv.y );
		vec2 p0 = ( vec2( iuv.x + h0x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p1 = ( vec2( iuv.x + h1x, iuv.y + h0y ) - 0.5 ) * texelSize.xy;
		vec2 p2 = ( vec2( iuv.x + h0x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		vec2 p3 = ( vec2( iuv.x + h1x, iuv.y + h1y ) - 0.5 ) * texelSize.xy;
		return g0( fuv.y ) * ( g0x * textureLod( tex, p0, lod ) + g1x * textureLod( tex, p1, lod ) ) +
			g1( fuv.y ) * ( g0x * textureLod( tex, p2, lod ) + g1x * textureLod( tex, p3, lod ) );
	}
	vec4 textureBicubic( sampler2D sampler, vec2 uv, float lod ) {
		vec2 fLodSize = vec2( textureSize( sampler, int( lod ) ) );
		vec2 cLodSize = vec2( textureSize( sampler, int( lod + 1.0 ) ) );
		vec2 fLodSizeInv = 1.0 / fLodSize;
		vec2 cLodSizeInv = 1.0 / cLodSize;
		vec4 fSample = bicubic( sampler, uv, vec4( fLodSizeInv, fLodSize ), floor( lod ) );
		vec4 cSample = bicubic( sampler, uv, vec4( cLodSizeInv, cLodSize ), ceil( lod ) );
		return mix( fSample, cSample, fract( lod ) );
	}
	vec3 getVolumeTransmissionRay( const in vec3 n, const in vec3 v, const in float thickness, const in float ior, const in mat4 modelMatrix ) {
		vec3 refractionVector = refract( - v, normalize( n ), 1.0 / ior );
		vec3 modelScale;
		modelScale.x = length( vec3( modelMatrix[ 0 ].xyz ) );
		modelScale.y = length( vec3( modelMatrix[ 1 ].xyz ) );
		modelScale.z = length( vec3( modelMatrix[ 2 ].xyz ) );
		return normalize( refractionVector ) * thickness * modelScale;
	}
	float applyIorToRoughness( const in float roughness, const in float ior ) {
		return roughness * clamp( ior * 2.0 - 2.0, 0.0, 1.0 );
	}
	vec4 getTransmissionSample( const in vec2 fragCoord, const in float roughness, const in float ior ) {
		float lod = log2( transmissionSamplerSize.x ) * applyIorToRoughness( roughness, ior );
		return textureBicubic( transmissionSamplerMap, fragCoord.xy, lod );
	}
	vec3 volumeAttenuation( const in float transmissionDistance, const in vec3 attenuationColor, const in float attenuationDistance ) {
		if ( isinf( attenuationDistance ) ) {
			return vec3( 1.0 );
		} else {
			vec3 attenuationCoefficient = -log( attenuationColor ) / attenuationDistance;
			vec3 transmittance = exp( - attenuationCoefficient * transmissionDistance );			return transmittance;
		}
	}
	vec4 getIBLVolumeRefraction( const in vec3 n, const in vec3 v, const in float roughness, const in vec3 diffuseColor,
		const in vec3 specularColor, const in float specularF90, const in vec3 position, const in mat4 modelMatrix,
		const in mat4 viewMatrix, const in mat4 projMatrix, const in float dispersion, const in float ior, const in float thickness,
		const in vec3 attenuationColor, const in float attenuationDistance ) {
		vec4 transmittedLight;
		vec3 transmittance;
		#ifdef USE_DISPERSION
			float halfSpread = ( ior - 1.0 ) * 0.025 * dispersion;
			vec3 iors = vec3( ior - halfSpread, ior, ior + halfSpread );
			for ( int i = 0; i < 3; i ++ ) {
				vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, iors[ i ], modelMatrix );
				vec3 refractedRayExit = position + transmissionRay;
				vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
				vec2 refractionCoords = ndcPos.xy / ndcPos.w;
				refractionCoords += 1.0;
				refractionCoords /= 2.0;
				vec4 transmissionSample = getTransmissionSample( refractionCoords, roughness, iors[ i ] );
				transmittedLight[ i ] = transmissionSample[ i ];
				transmittedLight.a += transmissionSample.a;
				transmittance[ i ] = diffuseColor[ i ] * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance )[ i ];
			}
			transmittedLight.a /= 3.0;
		#else
			vec3 transmissionRay = getVolumeTransmissionRay( n, v, thickness, ior, modelMatrix );
			vec3 refractedRayExit = position + transmissionRay;
			vec4 ndcPos = projMatrix * viewMatrix * vec4( refractedRayExit, 1.0 );
			vec2 refractionCoords = ndcPos.xy / ndcPos.w;
			refractionCoords += 1.0;
			refractionCoords /= 2.0;
			transmittedLight = getTransmissionSample( refractionCoords, roughness, ior );
			transmittance = diffuseColor * volumeAttenuation( length( transmissionRay ), attenuationColor, attenuationDistance );
		#endif
		vec3 attenuatedColor = transmittance * transmittedLight.rgb;
		vec3 F = EnvironmentBRDF( n, v, specularColor, specularF90, roughness );
		float transmittanceFactor = ( transmittance.r + transmittance.g + transmittance.b ) / 3.0;
		return vec4( ( 1.0 - F ) * attenuatedColor, 1.0 - ( 1.0 - transmittedLight.a ) * transmittanceFactor );
	}
#endif`,Bd=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	varying vec2 vDiffuseRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_SPECULARMAP
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,zd=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	varying vec2 vUv;
#endif
#ifdef USE_MAP
	uniform mat3 mapTransform;
	varying vec2 vMapUv;
#endif
#ifdef USE_ALPHAMAP
	uniform mat3 alphaMapTransform;
	varying vec2 vAlphaMapUv;
#endif
#ifdef USE_LIGHTMAP
	uniform mat3 lightMapTransform;
	varying vec2 vLightMapUv;
#endif
#ifdef USE_AOMAP
	uniform mat3 aoMapTransform;
	varying vec2 vAoMapUv;
#endif
#ifdef USE_BUMPMAP
	uniform mat3 bumpMapTransform;
	varying vec2 vBumpMapUv;
#endif
#ifdef USE_NORMALMAP
	uniform mat3 normalMapTransform;
	varying vec2 vNormalMapUv;
#endif
#ifdef USE_DISPLACEMENTMAP
	uniform mat3 displacementMapTransform;
	varying vec2 vDisplacementMapUv;
#endif
#ifdef USE_EMISSIVEMAP
	uniform mat3 emissiveMapTransform;
	varying vec2 vEmissiveMapUv;
#endif
#ifdef USE_METALNESSMAP
	uniform mat3 metalnessMapTransform;
	varying vec2 vMetalnessMapUv;
#endif
#ifdef USE_ROUGHNESSMAP
	uniform mat3 roughnessMapTransform;
	varying vec2 vRoughnessMapUv;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	uniform mat3 diffuseRoughnessMapTransform;
	varying vec2 vDiffuseRoughnessMapUv;
#endif
#ifdef USE_ANISOTROPYMAP
	uniform mat3 anisotropyMapTransform;
	varying vec2 vAnisotropyMapUv;
#endif
#ifdef USE_CLEARCOATMAP
	uniform mat3 clearcoatMapTransform;
	varying vec2 vClearcoatMapUv;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	uniform mat3 clearcoatNormalMapTransform;
	varying vec2 vClearcoatNormalMapUv;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	uniform mat3 clearcoatRoughnessMapTransform;
	varying vec2 vClearcoatRoughnessMapUv;
#endif
#ifdef USE_SHEEN_COLORMAP
	uniform mat3 sheenColorMapTransform;
	varying vec2 vSheenColorMapUv;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	uniform mat3 sheenRoughnessMapTransform;
	varying vec2 vSheenRoughnessMapUv;
#endif
#ifdef USE_IRIDESCENCEMAP
	uniform mat3 iridescenceMapTransform;
	varying vec2 vIridescenceMapUv;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	uniform mat3 iridescenceThicknessMapTransform;
	varying vec2 vIridescenceThicknessMapUv;
#endif
#ifdef USE_SPECULARMAP
	uniform mat3 specularMapTransform;
	varying vec2 vSpecularMapUv;
#endif
#ifdef USE_SPECULAR_COLORMAP
	uniform mat3 specularColorMapTransform;
	varying vec2 vSpecularColorMapUv;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	uniform mat3 specularIntensityMapTransform;
	varying vec2 vSpecularIntensityMapUv;
#endif
#ifdef USE_TRANSMISSIONMAP
	uniform mat3 transmissionMapTransform;
	varying vec2 vTransmissionMapUv;
#endif
#ifdef USE_THICKNESSMAP
	uniform mat3 thicknessMapTransform;
	varying vec2 vThicknessMapUv;
#endif`,kd=`#if defined( USE_UV ) || defined( USE_ANISOTROPY )
	vUv = vec3( uv, 1 ).xy;
#endif
#ifdef USE_MAP
	vMapUv = ( mapTransform * vec3( MAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ALPHAMAP
	vAlphaMapUv = ( alphaMapTransform * vec3( ALPHAMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_LIGHTMAP
	vLightMapUv = ( lightMapTransform * vec3( LIGHTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_AOMAP
	vAoMapUv = ( aoMapTransform * vec3( AOMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_BUMPMAP
	vBumpMapUv = ( bumpMapTransform * vec3( BUMPMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_NORMALMAP
	vNormalMapUv = ( normalMapTransform * vec3( NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DISPLACEMENTMAP
	vDisplacementMapUv = ( displacementMapTransform * vec3( DISPLACEMENTMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_EMISSIVEMAP
	vEmissiveMapUv = ( emissiveMapTransform * vec3( EMISSIVEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_METALNESSMAP
	vMetalnessMapUv = ( metalnessMapTransform * vec3( METALNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ROUGHNESSMAP
	vRoughnessMapUv = ( roughnessMapTransform * vec3( ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_DIFFUSE_ROUGHNESSMAP
	vDiffuseRoughnessMapUv = ( diffuseRoughnessMapTransform * vec3( DIFFUSE_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_ANISOTROPYMAP
	vAnisotropyMapUv = ( anisotropyMapTransform * vec3( ANISOTROPYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOATMAP
	vClearcoatMapUv = ( clearcoatMapTransform * vec3( CLEARCOATMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_NORMALMAP
	vClearcoatNormalMapUv = ( clearcoatNormalMapTransform * vec3( CLEARCOAT_NORMALMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_CLEARCOAT_ROUGHNESSMAP
	vClearcoatRoughnessMapUv = ( clearcoatRoughnessMapTransform * vec3( CLEARCOAT_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCEMAP
	vIridescenceMapUv = ( iridescenceMapTransform * vec3( IRIDESCENCEMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_IRIDESCENCE_THICKNESSMAP
	vIridescenceThicknessMapUv = ( iridescenceThicknessMapTransform * vec3( IRIDESCENCE_THICKNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_COLORMAP
	vSheenColorMapUv = ( sheenColorMapTransform * vec3( SHEEN_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SHEEN_ROUGHNESSMAP
	vSheenRoughnessMapUv = ( sheenRoughnessMapTransform * vec3( SHEEN_ROUGHNESSMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULARMAP
	vSpecularMapUv = ( specularMapTransform * vec3( SPECULARMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_COLORMAP
	vSpecularColorMapUv = ( specularColorMapTransform * vec3( SPECULAR_COLORMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_SPECULAR_INTENSITYMAP
	vSpecularIntensityMapUv = ( specularIntensityMapTransform * vec3( SPECULAR_INTENSITYMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_TRANSMISSIONMAP
	vTransmissionMapUv = ( transmissionMapTransform * vec3( TRANSMISSIONMAP_UV, 1 ) ).xy;
#endif
#ifdef USE_THICKNESSMAP
	vThicknessMapUv = ( thicknessMapTransform * vec3( THICKNESSMAP_UV, 1 ) ).xy;
#endif`,Gd=`#if defined( USE_ENVMAP ) || defined( DISTANCE ) || defined ( USE_SHADOWMAP ) || defined ( USE_TRANSMISSION ) || NUM_SPOT_LIGHT_COORDS > 0
	vec4 worldPosition = vec4( transformed, 1.0 );
	#ifdef USE_BATCHING
		worldPosition = batchingMatrix * worldPosition;
	#endif
	#ifdef USE_INSTANCING
		worldPosition = instanceMatrix * worldPosition;
	#endif
	worldPosition = modelMatrix * worldPosition;
#endif`,Vd=`varying vec2 vUv;
uniform mat3 uvTransform;
void main() {
	vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	gl_Position = vec4( position.xy, 1.0, 1.0 );
}`,Hd=`uniform sampler2D t2D;
uniform float backgroundIntensity;
varying vec2 vUv;
void main() {
	vec4 texColor = texture2D( t2D, vUv );
	#ifdef DECODE_VIDEO_TEXTURE
		texColor = vec4( mix( pow( texColor.rgb * 0.9478672986 + vec3( 0.0521327014 ), vec3( 2.4 ) ), texColor.rgb * 0.0773993808, vec3( lessThanEqual( texColor.rgb, vec3( 0.04045 ) ) ) ), texColor.w );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Wd=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Xd=`uniform float backgroundBlurriness;
uniform float backgroundIntensity;
uniform mat3 backgroundRotation;
varying vec3 vWorldDirection;
#include <envmap_common_pars_fragment>
void main() {
	#ifdef ENVMAP_TYPE_PMREM
		vec4 texColor = textureLod( envMap, backgroundRotation * vWorldDirection, roughnessToMip( backgroundBlurriness ) );
	#else
		vec4 texColor = textureCube( envMap, backgroundRotation * vWorldDirection );
	#endif
	texColor.rgb *= backgroundIntensity;
	gl_FragColor = texColor;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,qd=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
	gl_Position.z = gl_Position.w;
}`,Yd=`uniform samplerCube tCube;
uniform float tFlip;
uniform float opacity;
varying vec3 vWorldDirection;
void main() {
	vec4 texColor = textureCube( tCube, vec3( tFlip * vWorldDirection.x, vWorldDirection.yz ) );
	gl_FragColor = texColor;
	gl_FragColor.a *= opacity;
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,Zd=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
varying vec2 vHighPrecisionZW;
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vHighPrecisionZW = gl_Position.zw;
}`,Jd=`#if DEPTH_PACKING == 3200
	uniform float opacity;
#endif
#include <common>
#include <packing>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
varying vec2 vHighPrecisionZW;
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#if DEPTH_PACKING == 3200
		diffuseColor.a = opacity;
	#endif
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <logdepthbuf_fragment>
	#ifdef USE_REVERSED_DEPTH_BUFFER
		float fragCoordZ = vHighPrecisionZW[ 0 ] / vHighPrecisionZW[ 1 ];
	#else
		float fragCoordZ = 0.5 * vHighPrecisionZW[ 0 ] / vHighPrecisionZW[ 1 ] + 0.5;
	#endif
	#if DEPTH_PACKING == 3200
		gl_FragColor = vec4( vec3( 1.0 - fragCoordZ ), opacity );
	#elif DEPTH_PACKING == 3201
		gl_FragColor = packDepthToRGBA( fragCoordZ );
	#elif DEPTH_PACKING == 3202
		gl_FragColor = vec4( packDepthToRGB( fragCoordZ ), 1.0 );
	#elif DEPTH_PACKING == 3203
		gl_FragColor = vec4( packDepthToRG( fragCoordZ ), 0.0, 1.0 );
	#endif
}`,$d=`#define DISTANCE
varying vec3 vWorldPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <skinbase_vertex>
	#include <morphinstance_vertex>
	#ifdef USE_DISPLACEMENTMAP
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <worldpos_vertex>
	#include <clipping_planes_vertex>
	vWorldPosition = worldPosition.xyz;
}`,Kd=`#define DISTANCE
uniform vec3 referencePosition;
uniform float nearDistance;
uniform float farDistance;
varying vec3 vWorldPosition;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 1.0 );
	#include <clipping_planes_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	float dist = length( vWorldPosition - referencePosition );
	dist = ( dist - nearDistance ) / ( farDistance - nearDistance );
	dist = saturate( dist );
	gl_FragColor = vec4( dist, 0.0, 0.0, 1.0 );
}`,jd=`varying vec3 vWorldDirection;
#include <common>
void main() {
	vWorldDirection = transformDirection( position, modelMatrix );
	#include <begin_vertex>
	#include <project_vertex>
}`,Qd=`uniform sampler2D tEquirect;
varying vec3 vWorldDirection;
#include <common>
void main() {
	vec3 direction = normalize( vWorldDirection );
	vec2 sampleUV = equirectUv( direction );
	gl_FragColor = texture2D( tEquirect, sampleUV );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
}`,ef=`uniform float scale;
attribute float lineDistance;
varying float vLineDistance;
#include <common>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	vLineDistance = scale * lineDistance;
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,tf=`uniform vec3 diffuse;
uniform float opacity;
uniform float dashSize;
uniform float totalSize;
varying float vLineDistance;
#include <common>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	if ( mod( vLineDistance, totalSize ) > dashSize ) {
		discard;
	}
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,nf=`#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#if defined ( USE_ENVMAP ) || defined ( USE_SKINNING )
		#include <beginnormal_vertex>
		#include <morphnormal_vertex>
		#include <skinbase_vertex>
		#include <skinnormal_vertex>
		#include <defaultnormal_vertex>
	#endif
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <fog_vertex>
}`,sf=`uniform vec3 diffuse;
uniform float opacity;
#ifndef FLAT_SHADED
	varying vec3 vNormal;
#endif
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <fog_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	#ifdef USE_LIGHTMAP
		vec4 lightMapTexel = texture2D( lightMap, vLightMapUv );
		reflectedLight.indirectDiffuse += lightMapTexel.rgb * lightMapIntensity * RECIPROCAL_PI;
	#else
		reflectedLight.indirectDiffuse += vec3( 1.0 );
	#endif
	#include <aomap_fragment>
	reflectedLight.indirectDiffuse *= diffuseColor.rgb;
	vec3 outgoingLight = reflectedLight.indirectDiffuse;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,rf=`#define LAMBERT
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,af=`#define LAMBERT
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_lambert_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_lambert_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,of=`#define MATCAP
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <color_pars_vertex>
#include <displacementmap_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
	vViewPosition = - mvPosition.xyz;
}`,lf=`#define MATCAP
uniform vec3 diffuse;
uniform float opacity;
uniform sampler2D matcap;
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	vec3 viewDir = normalize( vViewPosition );
	vec3 x = normalize( vec3( viewDir.z, 0.0, - viewDir.x ) );
	vec3 y = cross( viewDir, x );
	vec2 uv = vec2( dot( x, normal ), dot( y, normal ) ) * 0.495 + 0.5;
	#ifdef USE_MATCAP
		vec4 matcapColor = texture2D( matcap, uv );
	#else
		vec4 matcapColor = vec4( vec3( mix( 0.2, 0.8, uv.y ) ), 1.0 );
	#endif
	vec3 outgoingLight = diffuseColor.rgb * matcapColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,cf=`#define NORMAL
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	vViewPosition = - mvPosition.xyz;
#endif
}`,hf=`#define NORMAL
uniform float opacity;
#if defined( FLAT_SHADED ) || defined( USE_BUMPMAP ) || defined( USE_NORMALMAP_TANGENTSPACE )
	varying vec3 vViewPosition;
#endif
#include <uv_pars_fragment>
#include <normal_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( 0.0, 0.0, 0.0, opacity );
	#include <clipping_planes_fragment>
	#include <logdepthbuf_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	gl_FragColor = vec4( normalize( normal ) * 0.5 + 0.5, diffuseColor.a );
	#ifdef OPAQUE
		gl_FragColor.a = 1.0;
	#endif
}`,uf=`#define PHONG
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <envmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <envmap_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,df=`#define PHONG
uniform vec3 diffuse;
uniform vec3 emissive;
uniform vec3 specular;
uniform float shininess;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_phong_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <specularmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <specularmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_phong_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + reflectedLight.directSpecular + reflectedLight.indirectSpecular + totalEmissiveRadiance;
	#include <envmap_fragment>
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,ff=`#define STANDARD
varying vec3 vViewPosition;
#ifdef USE_TRANSMISSION
	varying vec3 vWorldPosition;
#endif
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
#ifdef USE_TRANSMISSION
	vWorldPosition = worldPosition.xyz;
#endif
}`,pf=`#define STANDARD
#ifdef PHYSICAL
	#define IOR
	#define USE_SPECULAR
#endif
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float roughness;
uniform float metalness;
uniform float opacity;
#ifdef IOR
	uniform float ior;
#endif
#ifdef USE_SPECULAR
	uniform float specularIntensity;
	uniform vec3 specularColor;
	#ifdef USE_SPECULAR_COLORMAP
		uniform sampler2D specularColorMap;
	#endif
	#ifdef USE_SPECULAR_INTENSITYMAP
		uniform sampler2D specularIntensityMap;
	#endif
#endif
#ifdef USE_CLEARCOAT
	uniform float clearcoat;
	uniform float clearcoatRoughness;
#endif
#ifdef USE_DIFFUSE_ROUGHNESS
	uniform float diffuseRoughness;
	#ifdef USE_DIFFUSE_ROUGHNESSMAP
		uniform sampler2D diffuseRoughnessMap;
	#endif
#endif
#ifdef USE_DISPERSION
	uniform float dispersion;
#endif
#ifdef USE_RETROREFLECTION
	uniform float retroreflectivity;
#endif
#ifdef USE_IRIDESCENCE
	uniform float iridescence;
	uniform float iridescenceIOR;
	uniform float iridescenceThicknessMinimum;
	uniform float iridescenceThicknessMaximum;
#endif
#ifdef USE_SHEEN
	uniform vec3 sheenColor;
	uniform float sheenRoughness;
	#ifdef USE_SHEEN_COLORMAP
		uniform sampler2D sheenColorMap;
	#endif
	#ifdef USE_SHEEN_ROUGHNESSMAP
		uniform sampler2D sheenRoughnessMap;
	#endif
#endif
#ifdef USE_ANISOTROPY
	uniform vec2 anisotropyVector;
	#ifdef USE_ANISOTROPYMAP
		uniform sampler2D anisotropyMap;
	#endif
#endif
varying vec3 vViewPosition;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <iridescence_fragment>
#include <envmap_common_pars_fragment>
#include <envmap_physical_pars_fragment>
#include <fog_pars_fragment>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_physical_pars_fragment>
#include <transmission_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <clearcoat_pars_fragment>
#include <iridescence_pars_fragment>
#include <roughnessmap_pars_fragment>
#include <metalnessmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <roughnessmap_fragment>
	#include <metalnessmap_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <clearcoat_normal_fragment_begin>
	#include <clearcoat_normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_physical_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 totalDiffuse = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse;
	vec3 totalSpecular = reflectedLight.directSpecular + reflectedLight.indirectSpecular;
	#include <transmission_fragment>
	vec3 outgoingLight = totalDiffuse + totalSpecular + totalEmissiveRadiance;
	#ifdef USE_SHEEN
 
		outgoingLight = outgoingLight + sheenSpecularDirect + sheenSpecularIndirect;
 
 	#endif
	#ifdef USE_CLEARCOAT
		float dotNVcc = saturate( dot( geometryClearcoatNormal, geometryViewDir ) );
		vec3 Fcc = F_Schlick( material.clearcoatF0, material.clearcoatF90, dotNVcc );
		outgoingLight = outgoingLight * ( 1.0 - material.clearcoat * Fcc ) + ( clearcoatSpecularDirect + clearcoatSpecularIndirect ) * material.clearcoat;
	#endif
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,mf=`#define TOON
varying vec3 vViewPosition;
#include <common>
#include <batching_pars_vertex>
#include <uv_pars_vertex>
#include <displacementmap_pars_vertex>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <normal_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <shadowmap_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <normal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <displacementmap_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	vViewPosition = - mvPosition.xyz;
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,gf=`#define TOON
uniform vec3 diffuse;
uniform vec3 emissive;
uniform float opacity;
#include <common>
#include <dithering_pars_fragment>
#include <color_pars_fragment>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <aomap_pars_fragment>
#include <lightmap_pars_fragment>
#include <emissivemap_pars_fragment>
#include <gradientmap_pars_fragment>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <normal_pars_fragment>
#include <lights_toon_pars_fragment>
#include <shadowmap_pars_fragment>
#include <bumpmap_pars_fragment>
#include <normalmap_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	ReflectedLight reflectedLight = ReflectedLight( vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ), vec3( 0.0 ) );
	vec3 totalEmissiveRadiance = emissive;
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <color_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	#include <normal_fragment_begin>
	#include <normal_fragment_maps>
	#include <emissivemap_fragment>
	#include <lights_toon_fragment>
	#include <lights_fragment_begin>
	#include <lights_fragment_maps>
	#include <lights_fragment_end>
	#include <aomap_fragment>
	vec3 outgoingLight = reflectedLight.directDiffuse + reflectedLight.indirectDiffuse + totalEmissiveRadiance;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
	#include <dithering_fragment>
}`,_f=`uniform float size;
uniform float scale;
#include <common>
#include <color_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
#ifdef USE_POINTS_UV
	varying vec2 vUv;
	uniform mat3 uvTransform;
#endif
void main() {
	#ifdef USE_POINTS_UV
		vUv = ( uvTransform * vec3( uv, 1 ) ).xy;
	#endif
	#include <color_vertex>
	#include <morphinstance_vertex>
	#include <morphcolor_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <project_vertex>
	gl_PointSize = size;
	#ifdef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) gl_PointSize *= ( scale / - mvPosition.z );
	#endif
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <worldpos_vertex>
	#include <fog_vertex>
}`,xf=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <color_pars_fragment>
#include <map_particle_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_particle_fragment>
	#include <color_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,yf=`#include <common>
#include <batching_pars_vertex>
#include <fog_pars_vertex>
#include <morphtarget_pars_vertex>
#include <skinning_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <shadowmap_pars_vertex>
void main() {
	#include <batching_vertex>
	#include <beginnormal_vertex>
	#include <morphinstance_vertex>
	#include <morphnormal_vertex>
	#include <skinbase_vertex>
	#include <skinnormal_vertex>
	#include <defaultnormal_vertex>
	#include <begin_vertex>
	#include <morphtarget_vertex>
	#include <skinning_vertex>
	#include <project_vertex>
	#include <logdepthbuf_vertex>
	#include <worldpos_vertex>
	#include <shadowmap_vertex>
	#include <fog_vertex>
}`,vf=`uniform vec3 color;
uniform float opacity;
#include <common>
#include <fog_pars_fragment>
#include <bsdfs>
#include <lights_pars_begin>
#include <logdepthbuf_pars_fragment>
#include <shadowmap_pars_fragment>
#include <shadowmask_pars_fragment>
void main() {
	#include <logdepthbuf_fragment>
	gl_FragColor = vec4( color, opacity * ( 1.0 - getShadowMask() ) );
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
	#include <premultiplied_alpha_fragment>
}`,Sf=`uniform float rotation;
uniform vec2 center;
#include <common>
#include <uv_pars_vertex>
#include <fog_pars_vertex>
#include <logdepthbuf_pars_vertex>
#include <clipping_planes_pars_vertex>
void main() {
	#include <uv_vertex>
	vec4 mvPosition = modelViewMatrix[ 3 ];
	vec2 scale = vec2( length( modelMatrix[ 0 ].xyz ), length( modelMatrix[ 1 ].xyz ) );
	#ifndef USE_SIZEATTENUATION
		bool isPerspective = isPerspectiveMatrix( projectionMatrix );
		if ( isPerspective ) scale *= - mvPosition.z;
	#endif
	vec2 alignedPosition = ( position.xy - ( center - vec2( 0.5 ) ) ) * scale;
	vec2 rotatedPosition;
	rotatedPosition.x = cos( rotation ) * alignedPosition.x - sin( rotation ) * alignedPosition.y;
	rotatedPosition.y = sin( rotation ) * alignedPosition.x + cos( rotation ) * alignedPosition.y;
	mvPosition.xy += rotatedPosition;
	gl_Position = projectionMatrix * mvPosition;
	#include <logdepthbuf_vertex>
	#include <clipping_planes_vertex>
	#include <fog_vertex>
}`,Mf=`uniform vec3 diffuse;
uniform float opacity;
#include <common>
#include <uv_pars_fragment>
#include <map_pars_fragment>
#include <alphamap_pars_fragment>
#include <alphatest_pars_fragment>
#include <alphahash_pars_fragment>
#include <fog_pars_fragment>
#include <logdepthbuf_pars_fragment>
#include <clipping_planes_pars_fragment>
void main() {
	vec4 diffuseColor = vec4( diffuse, opacity );
	#include <clipping_planes_fragment>
	vec3 outgoingLight = vec3( 0.0 );
	#include <logdepthbuf_fragment>
	#include <map_fragment>
	#include <alphamap_fragment>
	#include <alphatest_fragment>
	#include <alphahash_fragment>
	outgoingLight = diffuseColor.rgb;
	#include <opaque_fragment>
	#include <tonemapping_fragment>
	#include <colorspace_fragment>
	#include <fog_fragment>
}`,ze={alphahash_fragment:H1,alphahash_pars_fragment:W1,alphamap_fragment:X1,alphamap_pars_fragment:q1,alphatest_fragment:Y1,alphatest_pars_fragment:Z1,aomap_fragment:J1,aomap_pars_fragment:$1,batching_pars_vertex:K1,batching_vertex:j1,begin_vertex:Q1,beginnormal_vertex:eu,bsdfs:tu,iridescence_fragment:nu,bumpmap_pars_fragment:iu,clipping_planes_fragment:su,clipping_planes_pars_fragment:ru,clipping_planes_pars_vertex:au,clipping_planes_vertex:ou,color_fragment:lu,color_pars_fragment:cu,color_pars_vertex:hu,color_vertex:uu,common:du,defaultnormal_vertex:fu,displacementmap_pars_vertex:pu,displacementmap_vertex:mu,emissivemap_fragment:gu,emissivemap_pars_fragment:_u,colorspace_fragment:xu,colorspace_pars_fragment:yu,envmap_fragment:vu,envmap_common_pars_fragment:Su,envmap_pars_fragment:Mu,envmap_pars_vertex:bu,envmap_physical_pars_fragment:Nu,envmap_vertex:Eu,fog_vertex:Tu,fog_pars_vertex:Au,fog_fragment:wu,fog_pars_fragment:Ru,gradientmap_pars_fragment:Cu,lightmap_pars_fragment:Pu,lights_lambert_fragment:Iu,lights_lambert_pars_fragment:Lu,lights_pars_begin:Du,lights_toon_fragment:Uu,lights_toon_pars_fragment:Fu,lights_phong_fragment:Ou,lights_phong_pars_fragment:Bu,lights_physical_fragment:zu,lights_physical_pars_fragment:ku,lights_fragment_begin:Gu,lights_fragment_maps:Vu,lights_fragment_end:Hu,lightprobes_pars_fragment:Wu,logdepthbuf_fragment:Xu,logdepthbuf_pars_fragment:qu,logdepthbuf_pars_vertex:Yu,logdepthbuf_vertex:Zu,map_fragment:Ju,map_pars_fragment:$u,map_particle_fragment:Ku,map_particle_pars_fragment:ju,metalnessmap_fragment:Qu,metalnessmap_pars_fragment:ed,morphinstance_vertex:td,morphcolor_vertex:nd,morphnormal_vertex:id,morphtarget_pars_vertex:sd,morphtarget_vertex:rd,normal_fragment_begin:ad,normal_fragment_maps:od,normal_pars_fragment:ld,normal_pars_vertex:cd,normal_vertex:hd,normalmap_pars_fragment:ud,clearcoat_normal_fragment_begin:dd,clearcoat_normal_fragment_maps:fd,clearcoat_pars_fragment:pd,iridescence_pars_fragment:md,opaque_fragment:gd,packing:_d,premultiplied_alpha_fragment:xd,project_vertex:yd,dithering_fragment:vd,dithering_pars_fragment:Sd,roughnessmap_fragment:Md,roughnessmap_pars_fragment:bd,shadowmap_pars_fragment:Ed,shadowmap_pars_vertex:Td,shadowmap_vertex:Ad,shadowmask_pars_fragment:wd,skinbase_vertex:Rd,skinning_pars_vertex:Cd,skinning_vertex:Pd,skinnormal_vertex:Id,specularmap_fragment:Ld,specularmap_pars_fragment:Dd,tonemapping_fragment:Nd,tonemapping_pars_fragment:Ud,transmission_fragment:Fd,transmission_pars_fragment:Od,uv_pars_fragment:Bd,uv_pars_vertex:zd,uv_vertex:kd,worldpos_vertex:Gd,background_vert:Vd,background_frag:Hd,backgroundCube_vert:Wd,backgroundCube_frag:Xd,cube_vert:qd,cube_frag:Yd,depth_vert:Zd,depth_frag:Jd,distance_vert:$d,distance_frag:Kd,equirect_vert:jd,equirect_frag:Qd,linedashed_vert:ef,linedashed_frag:tf,meshbasic_vert:nf,meshbasic_frag:sf,meshlambert_vert:rf,meshlambert_frag:af,meshmatcap_vert:of,meshmatcap_frag:lf,meshnormal_vert:cf,meshnormal_frag:hf,meshphong_vert:uf,meshphong_frag:df,meshphysical_vert:ff,meshphysical_frag:pf,meshtoon_vert:mf,meshtoon_frag:gf,points_vert:_f,points_frag:xf,shadow_vert:yf,shadow_frag:vf,sprite_vert:Sf,sprite_frag:Mf},fe={common:{diffuse:{value:new Be(16777215)},opacity:{value:1},map:{value:null},mapTransform:{value:new Ie},alphaMap:{value:null},alphaMapTransform:{value:new Ie},alphaTest:{value:0}},specularmap:{specularMap:{value:null},specularMapTransform:{value:new Ie}},envmap:{envMap:{value:null},envMapRotation:{value:new Ie},reflectivity:{value:1},ior:{value:1.5},refractionRatio:{value:.98},dfgLUT:{value:null}},aomap:{aoMap:{value:null},aoMapIntensity:{value:1},aoMapTransform:{value:new Ie}},lightmap:{lightMap:{value:null},lightMapIntensity:{value:1},lightMapTransform:{value:new Ie}},bumpmap:{bumpMap:{value:null},bumpMapTransform:{value:new Ie},bumpScale:{value:1}},normalmap:{normalMap:{value:null},normalMapTransform:{value:new Ie},normalScale:{value:new Re(1,1)}},displacementmap:{displacementMap:{value:null},displacementMapTransform:{value:new Ie},displacementScale:{value:1},displacementBias:{value:0}},emissivemap:{emissiveMap:{value:null},emissiveMapTransform:{value:new Ie}},metalnessmap:{metalnessMap:{value:null},metalnessMapTransform:{value:new Ie}},roughnessmap:{roughnessMap:{value:null},roughnessMapTransform:{value:new Ie}},gradientmap:{gradientMap:{value:null}},fog:{fogDensity:{value:25e-5},fogNear:{value:1},fogFar:{value:2e3},fogColor:{value:new Be(16777215)}},lights:{ambientLightColor:{value:[]},lightProbe:{value:[]},sunLights:{value:[],properties:{direction:{},color:{}}},sunLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},sunShadowMatrix:{value:[]},sunShadowCascade:{value:[]},directionalLights:{value:[],properties:{direction:{},color:{}}},directionalLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},directionalShadowMatrix:{value:[]},spotLights:{value:[],properties:{color:{},position:{},direction:{},distance:{},coneCos:{},penumbraCos:{},decay:{}}},spotLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{}}},spotLightMap:{value:[]},spotLightMatrix:{value:[]},pointLights:{value:[],properties:{color:{},position:{},decay:{},distance:{}}},pointLightShadows:{value:[],properties:{shadowIntensity:1,shadowBias:{},shadowNormalBias:{},shadowRadius:{},shadowMapSize:{},shadowCameraNear:{},shadowCameraFar:{}}},pointShadowMatrix:{value:[]},hemisphereLights:{value:[],properties:{direction:{},skyColor:{},groundColor:{}}},rectAreaLights:{value:[],properties:{color:{},position:{},width:{},height:{}}},ltc_1:{value:null},ltc_2:{value:null},probesSH:{value:[]},probesMin:{value:[]},probesMax:{value:[]},probesResolution:{value:[]}},points:{diffuse:{value:new Be(16777215)},opacity:{value:1},size:{value:1},scale:{value:1},map:{value:null},alphaMap:{value:null},alphaMapTransform:{value:new Ie},alphaTest:{value:0},uvTransform:{value:new Ie}},sprite:{diffuse:{value:new Be(16777215)},opacity:{value:1},center:{value:new Re(.5,.5)},rotation:{value:0},map:{value:null},mapTransform:{value:new Ie},alphaMap:{value:null},alphaMapTransform:{value:new Ie},alphaTest:{value:0}}},vn={basic:{uniforms:It([fe.common,fe.specularmap,fe.envmap,fe.aomap,fe.lightmap,fe.fog]),vertexShader:ze.meshbasic_vert,fragmentShader:ze.meshbasic_frag},lambert:{uniforms:It([fe.common,fe.specularmap,fe.envmap,fe.aomap,fe.lightmap,fe.emissivemap,fe.bumpmap,fe.normalmap,fe.displacementmap,fe.fog,fe.lights,{emissive:{value:new Be(0)},envMapIntensity:{value:1}}]),vertexShader:ze.meshlambert_vert,fragmentShader:ze.meshlambert_frag},phong:{uniforms:It([fe.common,fe.specularmap,fe.envmap,fe.aomap,fe.lightmap,fe.emissivemap,fe.bumpmap,fe.normalmap,fe.displacementmap,fe.fog,fe.lights,{emissive:{value:new Be(0)},specular:{value:new Be(1118481)},shininess:{value:30},envMapIntensity:{value:1}}]),vertexShader:ze.meshphong_vert,fragmentShader:ze.meshphong_frag},standard:{uniforms:It([fe.common,fe.envmap,fe.aomap,fe.lightmap,fe.emissivemap,fe.bumpmap,fe.normalmap,fe.displacementmap,fe.roughnessmap,fe.metalnessmap,fe.fog,fe.lights,{emissive:{value:new Be(0)},roughness:{value:1},metalness:{value:0},envMapIntensity:{value:1}}]),vertexShader:ze.meshphysical_vert,fragmentShader:ze.meshphysical_frag},toon:{uniforms:It([fe.common,fe.aomap,fe.lightmap,fe.emissivemap,fe.bumpmap,fe.normalmap,fe.displacementmap,fe.gradientmap,fe.fog,fe.lights,{emissive:{value:new Be(0)}}]),vertexShader:ze.meshtoon_vert,fragmentShader:ze.meshtoon_frag},matcap:{uniforms:It([fe.common,fe.bumpmap,fe.normalmap,fe.displacementmap,fe.fog,{matcap:{value:null}}]),vertexShader:ze.meshmatcap_vert,fragmentShader:ze.meshmatcap_frag},points:{uniforms:It([fe.points,fe.fog]),vertexShader:ze.points_vert,fragmentShader:ze.points_frag},dashed:{uniforms:It([fe.common,fe.fog,{scale:{value:1},dashSize:{value:1},totalSize:{value:2}}]),vertexShader:ze.linedashed_vert,fragmentShader:ze.linedashed_frag},depth:{uniforms:It([fe.common,fe.displacementmap]),vertexShader:ze.depth_vert,fragmentShader:ze.depth_frag},normal:{uniforms:It([fe.common,fe.bumpmap,fe.normalmap,fe.displacementmap,{opacity:{value:1}}]),vertexShader:ze.meshnormal_vert,fragmentShader:ze.meshnormal_frag},sprite:{uniforms:It([fe.sprite,fe.fog]),vertexShader:ze.sprite_vert,fragmentShader:ze.sprite_frag},background:{uniforms:{uvTransform:{value:new Ie},t2D:{value:null},backgroundIntensity:{value:1}},vertexShader:ze.background_vert,fragmentShader:ze.background_frag},backgroundCube:{uniforms:{envMap:{value:null},backgroundBlurriness:{value:0},backgroundIntensity:{value:1},backgroundRotation:{value:new Ie}},vertexShader:ze.backgroundCube_vert,fragmentShader:ze.backgroundCube_frag},cube:{uniforms:{tCube:{value:null},tFlip:{value:-1},opacity:{value:1}},vertexShader:ze.cube_vert,fragmentShader:ze.cube_frag},equirect:{uniforms:{tEquirect:{value:null}},vertexShader:ze.equirect_vert,fragmentShader:ze.equirect_frag},distance:{uniforms:It([fe.common,fe.displacementmap,{referencePosition:{value:new U},nearDistance:{value:1},farDistance:{value:1e3}}]),vertexShader:ze.distance_vert,fragmentShader:ze.distance_frag},shadow:{uniforms:It([fe.lights,fe.fog,{color:{value:new Be(0)},opacity:{value:1}}]),vertexShader:ze.shadow_vert,fragmentShader:ze.shadow_frag}};vn.physical={uniforms:It([vn.standard.uniforms,{clearcoat:{value:0},clearcoatMap:{value:null},clearcoatMapTransform:{value:new Ie},clearcoatNormalMap:{value:null},clearcoatNormalMapTransform:{value:new Ie},clearcoatNormalScale:{value:new Re(1,1)},clearcoatRoughness:{value:0},clearcoatRoughnessMap:{value:null},clearcoatRoughnessMapTransform:{value:new Ie},diffuseRoughness:{value:0},diffuseRoughnessMap:{value:null},diffuseRoughnessMapTransform:{value:new Ie},dispersion:{value:0},retroreflectivity:{value:0},iridescence:{value:0},iridescenceMap:{value:null},iridescenceMapTransform:{value:new Ie},iridescenceIOR:{value:1.3},iridescenceThicknessMinimum:{value:100},iridescenceThicknessMaximum:{value:400},iridescenceThicknessMap:{value:null},iridescenceThicknessMapTransform:{value:new Ie},sheen:{value:0},sheenColor:{value:new Be(0)},sheenColorMap:{value:null},sheenColorMapTransform:{value:new Ie},sheenRoughness:{value:1},sheenRoughnessMap:{value:null},sheenRoughnessMapTransform:{value:new Ie},transmission:{value:0},transmissionMap:{value:null},transmissionMapTransform:{value:new Ie},transmissionSamplerSize:{value:new Re},transmissionSamplerMap:{value:null},thickness:{value:0},thicknessMap:{value:null},thicknessMapTransform:{value:new Ie},attenuationDistance:{value:0},attenuationColor:{value:new Be(0)},specularColor:{value:new Be(1,1,1)},specularColorMap:{value:null},specularColorMapTransform:{value:new Ie},specularIntensity:{value:1},specularIntensityMap:{value:null},specularIntensityMapTransform:{value:new Ie},anisotropyVector:{value:new Re},anisotropyMap:{value:null},anisotropyMapTransform:{value:new Ie}}]),vertexShader:ze.meshphysical_vert,fragmentShader:ze.meshphysical_frag};var Ua={r:0,b:0,g:0},bf=new nt,Ah=new Ie;Ah.set(-1,0,0,0,1,0,0,0,1);function Ef(i,e,t,n,s,r){let a=new Be(0),o=s===!0?0:1,l,c,h=null,g=0,d=null;function m(M){let w=M.isScene===!0?M.background:null;if(w&&w.isTexture){let E=M.backgroundBlurriness>0;w=e.get(w,E)}return w}function _(M){let w=!1,E=m(M);E===null?p(a,o):E&&E.isColor&&(p(E,1),w=!0);let A=i.xr.getEnvironmentBlendMode();A==="additive"?t.buffers.color.setClear(0,0,0,1,r):A==="alpha-blend"&&t.buffers.color.setClear(0,0,0,0,r),(i.autoClear||w)&&(t.buffers.depth.setTest(!0),t.buffers.depth.setMask(!0),t.buffers.color.setMask(!0),i.clear(i.autoClearColor,i.autoClearDepth,i.autoClearStencil))}function S(M,w){let E=m(w);E&&E.isCubeTexture?(c===void 0&&(c=new Ot(new Gi(1,1,1),new tn({name:"BackgroundCubeMaterial",uniforms:mi(vn.backgroundCube.uniforms),vertexShader:vn.backgroundCube.vertexShader,fragmentShader:vn.backgroundCube.fragmentShader,side:Tt,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),c.geometry.deleteAttribute("normal"),c.geometry.deleteAttribute("uv"),c.onBeforeRender=function(A,T,f){this.matrixWorld.copyPosition(f.matrixWorld)},Object.defineProperty(c.material,"envMap",{get:function(){return this.uniforms.envMap.value}}),n.update(c)),c.material.uniforms.envMap.value=E,c.material.uniforms.backgroundBlurriness.value=w.backgroundBlurriness,c.material.uniforms.backgroundIntensity.value=w.backgroundIntensity,c.material.uniforms.backgroundRotation.value.setFromMatrix4(bf.makeRotationFromEuler(w.backgroundRotation)).transpose(),E.isRenderTargetTexture===!1&&c.material.uniforms.backgroundRotation.value.premultiply(Ah),c.material.toneMapped=We.getTransfer(E.colorSpace)!==$e,(h!==E||g!==E.version||d!==i.toneMapping)&&(c.material.needsUpdate=!0,h=E,g=E.version,d=i.toneMapping),c.layers.enableAll(),M.unshift(c,c.geometry,c.material,0,0,null)):E&&E.isTexture&&(l===void 0&&(l=new Ot(new xs(2,2),new tn({name:"BackgroundMaterial",uniforms:mi(vn.background.uniforms),vertexShader:vn.background.vertexShader,fragmentShader:vn.background.fragmentShader,side:jn,depthTest:!1,depthWrite:!1,fog:!1,allowOverride:!1})),l.geometry.deleteAttribute("normal"),Object.defineProperty(l.material,"map",{get:function(){return this.uniforms.t2D.value}}),n.update(l)),l.material.uniforms.t2D.value=E,l.material.uniforms.backgroundIntensity.value=w.backgroundIntensity,l.material.toneMapped=We.getTransfer(E.colorSpace)!==$e,E.matrixAutoUpdate===!0&&E.updateMatrix(),l.material.uniforms.uvTransform.value.copy(E.matrix),(h!==E||g!==E.version||d!==i.toneMapping)&&(l.material.needsUpdate=!0,h=E,g=E.version,d=i.toneMapping),l.layers.enableAll(),M.unshift(l,l.geometry,l.material,0,0,null))}function p(M,w){M.getRGB(Ua,el(i)),t.buffers.color.setClear(Ua.r,Ua.g,Ua.b,w,r)}function u(){c!==void 0&&(c.geometry.dispose(),c.material.dispose(),c=void 0),l!==void 0&&(l.geometry.dispose(),l.material.dispose(),l=void 0)}return{getClearColor:function(){return a},setClearColor:function(M,w=1){a.set(M),o=w,p(a,o)},getClearAlpha:function(){return o},setClearAlpha:function(M){o=M,p(a,o)},render:_,addToRenderList:S,dispose:u}}function Tf(i,e){let t=i.getParameter(i.MAX_VERTEX_ATTRIBS),n={},s=d(null),r=s,a=!1;function o(D,z,q,P,W){let $=!1,G=g(D,P,q,z);r!==G&&(r=G,c(r.object)),$=m(D,P,q,W),$&&_(D,P,q,W),W!==null&&e.update(W,i.ELEMENT_ARRAY_BUFFER),($||a)&&(a=!1,E(D,z,q,P),W!==null&&i.bindBuffer(i.ELEMENT_ARRAY_BUFFER,e.get(W).buffer))}function l(){return i.createVertexArray()}function c(D){return i.bindVertexArray(D)}function h(D){return i.deleteVertexArray(D)}function g(D,z,q,P){let W=P.wireframe===!0,$=n[z.id];$===void 0&&($={},n[z.id]=$);let G=D.isInstancedMesh===!0?D.id:0,te=$[G];te===void 0&&(te={},$[G]=te);let H=te[q.id];H===void 0&&(H={},te[q.id]=H);let j=H[W];return j===void 0&&(j=d(l()),H[W]=j),j}function d(D){let z=[],q=[],P=[];for(let W=0;W<t;W++)z[W]=0,q[W]=0,P[W]=0;return{geometry:null,program:null,wireframe:!1,newAttributes:z,enabledAttributes:q,attributeDivisors:P,object:D,attributes:{},index:null}}function m(D,z,q,P){let W=r.attributes,$=z.attributes,G=0,te=q.getAttributes();for(let H in te)if(te[H].location>=0){let Q=W[H],Se=$[H];if(Se===void 0&&(H==="instanceMatrix"&&D.instanceMatrix&&(Se=D.instanceMatrix),H==="instanceColor"&&D.instanceColor&&(Se=D.instanceColor)),Q===void 0||Q.attribute!==Se||Se&&Q.data!==Se.data)return!0;G++}return r.attributesNum!==G||r.index!==P}function _(D,z,q,P){let W={},$=z.attributes,G=0,te=q.getAttributes();for(let H in te)if(te[H].location>=0){let Q=$[H];Q===void 0&&(H==="instanceMatrix"&&D.instanceMatrix&&(Q=D.instanceMatrix),H==="instanceColor"&&D.instanceColor&&(Q=D.instanceColor));let Se={};Se.attribute=Q,Q&&Q.data&&(Se.data=Q.data),W[H]=Se,G++}r.attributes=W,r.attributesNum=G,r.index=P}function S(){let D=r.newAttributes;for(let z=0,q=D.length;z<q;z++)D[z]=0}function p(D){u(D,0)}function u(D,z){let q=r.newAttributes,P=r.enabledAttributes,W=r.attributeDivisors;q[D]=1,P[D]===0&&(i.enableVertexAttribArray(D),P[D]=1),W[D]!==z&&(i.vertexAttribDivisor(D,z),W[D]=z)}function M(){let D=r.newAttributes,z=r.enabledAttributes;for(let q=0,P=z.length;q<P;q++)z[q]!==D[q]&&(i.disableVertexAttribArray(q),z[q]=0)}function w(D,z,q,P,W,$,G){G===!0?i.vertexAttribIPointer(D,z,q,W,$):i.vertexAttribPointer(D,z,q,P,W,$)}function E(D,z,q,P){S();let W=P.attributes,$=q.getAttributes(),G=z.defaultAttributeValues;for(let te in $){let H=$[te];if(H.location>=0){let j=W[te];if(j===void 0&&(te==="instanceMatrix"&&D.instanceMatrix&&(j=D.instanceMatrix),te==="instanceColor"&&D.instanceColor&&(j=D.instanceColor)),j!==void 0){let Q=j.normalized,Se=j.itemSize,De=e.get(j);if(De===void 0)continue;let Z=De.buffer,pe=De.type,xe=De.bytesPerElement,Ae=pe===i.INT||pe===i.UNSIGNED_INT||j.gpuType===jr;if(j.isInterleavedBufferAttribute){let me=j.data,Ue=me.isInterleavedBuffer===!0?me.stride:me.itemSize,ht=j.offset;if(me.isInstancedInterleavedBuffer||me.isInstancedBufferAttribute){for(let Ce=0;Ce<H.locationSize;Ce++)u(H.location+Ce,me.meshPerAttribute);D.isInstancedMesh!==!0&&P._maxInstanceCount===void 0&&(P._maxInstanceCount=me.meshPerAttribute*me.count)}else for(let Ce=0;Ce<H.locationSize;Ce++)p(H.location+Ce);i.bindBuffer(i.ARRAY_BUFFER,Z);for(let Ce=0;Ce<H.locationSize;Ce++)w(H.location+Ce,Se/H.locationSize,pe,Q,Ue*xe,(ht+Se/H.locationSize*Ce)*xe,Ae)}else{if(j.isInstancedBufferAttribute){for(let me=0;me<H.locationSize;me++)u(H.location+me,j.meshPerAttribute);D.isInstancedMesh!==!0&&P._maxInstanceCount===void 0&&(P._maxInstanceCount=j.meshPerAttribute*j.count)}else for(let me=0;me<H.locationSize;me++)p(H.location+me);i.bindBuffer(i.ARRAY_BUFFER,Z);for(let me=0;me<H.locationSize;me++)w(H.location+me,Se/H.locationSize,pe,Q,Se*xe,Se/H.locationSize*me*xe,Ae)}}else if(G!==void 0){let Q=G[te];if(Q!==void 0)switch(Q.length){case 2:i.vertexAttrib2fv(H.location,Q);break;case 3:i.vertexAttrib3fv(H.location,Q);break;case 4:i.vertexAttrib4fv(H.location,Q);break;default:i.vertexAttrib1fv(H.location,Q)}}}}M()}function A(){N();for(let D in n){let z=n[D];for(let q in z){let P=z[q];for(let W in P){let $=P[W];for(let G in $)h($[G].object),delete $[G];delete P[W]}}delete n[D]}}function T(D){if(n[D.id]===void 0)return;let z=n[D.id];for(let q in z){let P=z[q];for(let W in P){let $=P[W];for(let G in $)h($[G].object),delete $[G];delete P[W]}}delete n[D.id]}function f(D){for(let z in n){let q=n[z];for(let P in q){let W=q[P];if(W[D.id]===void 0)continue;let $=W[D.id];for(let G in $)h($[G].object),delete $[G];delete W[D.id]}}}function v(D){for(let z in n){let q=n[z],P=D.isInstancedMesh===!0?D.id:0,W=q[P];if(W!==void 0){for(let $ in W){let G=W[$];for(let te in G)h(G[te].object),delete G[te];delete W[$]}delete q[P],Object.keys(q).length===0&&delete n[z]}}}function N(){I(),a=!0,r!==s&&(r=s,c(r.object))}function I(){s.geometry=null,s.program=null,s.wireframe=!1}return{setup:o,reset:N,resetDefaultState:I,dispose:A,releaseStatesOfGeometry:T,releaseStatesOfObject:v,releaseStatesOfProgram:f,initAttributes:S,enableAttribute:p,disableUnusedAttributes:M}}function Af(i,e,t){let n;function s(l){n=l}function r(l,c){i.drawArrays(n,l,c),t.update(c,n,1)}function a(l,c,h){h!==0&&(i.drawArraysInstanced(n,l,c,h),t.update(c,n,h))}function o(l,c,h){if(h===0)return;e.get("WEBGL_multi_draw").multiDrawArraysWEBGL(n,l,0,c,0,h);let d=0;for(let m=0;m<h;m++)d+=c[m];t.update(d,n,1)}this.setMode=s,this.render=r,this.renderInstances=a,this.renderMultiDraw=o}function wf(i,e,t,n){let s;function r(){if(s!==void 0)return s;if(e.has("EXT_texture_filter_anisotropic")===!0){let f=e.get("EXT_texture_filter_anisotropic");s=i.getParameter(f.MAX_TEXTURE_MAX_ANISOTROPY_EXT)}else s=0;return s}function a(f){return!(f!==dn&&n.convert(f)!==i.getParameter(i.IMPLEMENTATION_COLOR_READ_FORMAT))}function o(f){let v=f===un&&(e.has("EXT_color_buffer_half_float")||e.has("EXT_color_buffer_float"));return!(f!==Gt&&f!==hn&&!v&&n.convert(f)!==i.getParameter(i.IMPLEMENTATION_COLOR_READ_TYPE))}function l(f){if(f==="highp"){if(i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.HIGH_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.HIGH_FLOAT).precision>0)return"highp";f="mediump"}return f==="mediump"&&i.getShaderPrecisionFormat(i.VERTEX_SHADER,i.MEDIUM_FLOAT).precision>0&&i.getShaderPrecisionFormat(i.FRAGMENT_SHADER,i.MEDIUM_FLOAT).precision>0?"mediump":"lowp"}let c=t.precision!==void 0?t.precision:"highp",h=l(c);h!==c&&(Te("WebGLRenderer:",c,"not supported, using",h,"instead."),c=h);let g=t.reversedDepthBuffer===!0&&e.has("EXT_clip_control"),d=t.logarithmicDepthBuffer===!0&&g===!1;t.reversedDepthBuffer===!0&&g===!1&&Te("WebGLRenderer: Unable to use reversed depth buffer due to missing EXT_clip_control extension. Fallback to default depth buffer."),t.logarithmicDepthBuffer===!0&&g===!0&&Te("WebGLRenderer: Logarithmic depth buffer is ignored when reversed depth buffer is enabled.");let m=i.getParameter(i.MAX_TEXTURE_IMAGE_UNITS),_=i.getParameter(i.MAX_VERTEX_TEXTURE_IMAGE_UNITS),S=i.getParameter(i.MAX_TEXTURE_SIZE),p=i.getParameter(i.MAX_CUBE_MAP_TEXTURE_SIZE),u=i.getParameter(i.MAX_VERTEX_ATTRIBS),M=i.getParameter(i.MAX_VERTEX_UNIFORM_VECTORS),w=i.getParameter(i.MAX_VARYING_VECTORS),E=i.getParameter(i.MAX_FRAGMENT_UNIFORM_VECTORS),A=i.getParameter(i.MAX_SAMPLES),T=i.getParameter(i.SAMPLES);return{isWebGL2:!0,getMaxAnisotropy:r,getMaxPrecision:l,textureFormatReadable:a,textureTypeReadable:o,precision:c,logarithmicDepthBuffer:d,reversedDepthBuffer:g,maxTextures:m,maxVertexTextures:_,maxTextureSize:S,maxCubemapSize:p,maxAttributes:u,maxVertexUniforms:M,maxVaryings:w,maxFragmentUniforms:E,maxSamples:A,samples:T}}function Rf(i){let e=this,t=null,n=0,s=!1,r=!1,a=new Xt,o=new Ie,l={value:null,needsUpdate:!1};this.uniform=l,this.numPlanes=0,this.numIntersection=0,this.init=function(g,d){let m=g.length!==0||d||n!==0||s;return s=d,n=g.length,m},this.beginShadows=function(){r=!0,h(null)},this.endShadows=function(){r=!1},this.setGlobalState=function(g,d){t=h(g,d,0)},this.setState=function(g,d,m){let _=g.clippingPlanes,S=g.clipIntersection,p=g.clipShadows,u=i.get(g);if(!s||_===null||_.length===0||r&&!p)r?h(null):c();else{let M=r?0:n,w=M*4,E=u.clippingState||null;l.value=E,E=h(_,d,w,m);for(let A=0;A!==w;++A)E[A]=t[A];u.clippingState=E,this.numIntersection=S?this.numPlanes:0,this.numPlanes+=M}};function c(){l.value!==t&&(l.value=t,l.needsUpdate=n>0),e.numPlanes=n,e.numIntersection=0}function h(g,d,m,_){let S=g!==null?g.length:0,p=null;if(S!==0){if(p=l.value,_!==!0||p===null){let u=m+S*4,M=d.matrixWorldInverse;o.getNormalMatrix(M),(p===null||p.length<u)&&(p=new Float32Array(u));for(let w=0,E=m;w!==S;++w,E+=4)a.copy(g[w]).applyMatrix4(M,o),a.normal.toArray(p,E),p[E+3]=a.constant}l.value=p,l.needsUpdate=!0}return e.numPlanes=S,e.numIntersection=0,p}}var ks=class extends Yt{constructor(e=1,t={}){super(e,e,t),this.isWebGLCubeRenderTarget=!0;let n={width:e,height:e,depth:1},s=[n,n,n,n,n,n];this.texture=new ms(s),this._setTextureOptions(t),this.texture.isRenderTargetTexture=!0}fromEquirectangularTexture(e,t){this.texture.type=t.type,this.texture.colorSpace=t.colorSpace,this.texture.generateMipmaps=t.generateMipmaps,this.texture.minFilter=t.minFilter,this.texture.magFilter=t.magFilter;let n={uniforms:{tEquirect:{value:null}},vertexShader:`

				varying vec3 vWorldDirection;

				vec3 transformDirection( in vec3 dir, in mat4 matrix ) {

					return normalize( ( matrix * vec4( dir, 0.0 ) ).xyz );

				}

				void main() {

					vWorldDirection = transformDirection( position, modelMatrix );

					#include <begin_vertex>
					#include <project_vertex>

				}
			`,fragmentShader:`

				uniform sampler2D tEquirect;

				varying vec3 vWorldDirection;

				#include <common>

				void main() {

					vec3 direction = normalize( vWorldDirection );

					vec2 sampleUV = equirectUv( direction );

					gl_FragColor = texture2D( tEquirect, sampleUV );

				}
			`},s=new Gi(5,5,5),r=new tn({name:"CubemapFromEquirect",uniforms:mi(n.uniforms),vertexShader:n.vertexShader,fragmentShader:n.fragmentShader,side:Tt,blending:ui});r.uniforms.tEquirect.value=t;let a=new Ot(s,r),o=t.minFilter;return t.minFilter===Dn&&(t.minFilter=Ft),new Vi(1,10,this).update(e,a),t.minFilter=o,a.geometry.dispose(),a.material.dispose(),this}clear(e,t=!0,n=!0,s=!0){let r=e.getRenderTarget();for(let a=0;a<6;a++)e.setRenderTarget(this,a),e.clear(t,n,s);e.setRenderTarget(r)}},sh=256,Cf=3,Pf=20,wh=256,Rh=16,If=3,Lf=new U,Df=new Be,Oa=class i{constructor(e){this._renderer=e,this._cubeSize=0,this._sourceTarget=null,this._cubeCamera=new Vi(1,10,null),this._boxMesh=new Ot(new Gi(5,5,5),null),this._cubemapMaterial=null,this._equirectMaterial=null,this._blurMaterial=null,this._ggxMaterial=null,this._integrationMaterial=null}fromScene(e,t=0,n=.1,s=100,r={}){let{size:a=256,position:o=Lf}=r,l=this._renderer;this._setSize(a);let c=this._allocateTarget(),h=this._getSourceTarget(!0);t>0&&(h.texture.mipmapsAutoUpdate=!1);let g=l.autoClear,d=l.autoClearColor,m=l.autoClearDepth,_=l.autoClearStencil,S=e.background;l.autoClear=!0,l.autoClearColor=!0,l.autoClearDepth=!0,l.autoClearStencil=!0,S===null&&(e.background=l.getClearColor(Df));let p=new Vi(n,s,h);return p.position.copy(o),p.update(l,e),l.autoClear=g,l.autoClearColor=d,l.autoClearDepth=m,l.autoClearStencil=_,e.background=S,t>0&&(h.texture.mipmapsAutoUpdate=!0,this._blur(c,t)),this._applyPMREM(c),c}fromEquirectangular(e,t=null){return this._fromTexture(e,t)}fromCubemap(e,t=null){return this._fromTexture(e,t)}compileCubemapShader(){this._cubemapMaterial===null&&(this._cubemapMaterial=oh(),this._compileMaterial(this._cubemapMaterial))}compileEquirectangularShader(){this._equirectMaterial===null&&(this._equirectMaterial=ah(),this._compileMaterial(this._equirectMaterial))}dispose(){this._sourceTarget!==null&&this._sourceTarget.dispose(),this._cubemapMaterial!==null&&this._cubemapMaterial.dispose(),this._equirectMaterial!==null&&this._equirectMaterial.dispose(),this._blurMaterial!==null&&this._blurMaterial.dispose(),this._ggxMaterial!==null&&this._ggxMaterial.dispose(),this._integrationMaterial!==null&&this._integrationMaterial.dispose(),this._boxMesh.geometry.dispose()}static lodToRoughness(e,t){return t>0?1-Math.sqrt(1-e/t):0}_setSize(e){this._cubeSize=Math.max(sh,Ko(e))}_fromTexture(e,t){e.mapping===fi||e.mapping===qi?this._setSize(e.image.length===0?sh:e.image[0].width||e.image[0].image.width):this._setSize(e.image.width/4);let n=t||this._allocateTarget();return this._textureToCubemap(e),this._applyPMREM(n),n}_allocateTarget(){let e=this._cubeSize,t=rh(e,!1,!1),n=Math.log2(e)-Cf;for(let s=0;s<=n;s++)t.texture.mipmaps.push({width:e>>s,height:e>>s});return t.texture.name="PMREM",t.texture.isPMREMTexture=!0,t}_getSourceTarget(e=!1){let t=this._cubeSize,n=this._sourceTarget;return(n===null||n.width!==t||e&&n.depthBuffer===!1)&&(n!==null&&n.dispose(),this._sourceTarget=rh(t,!0,e)),this._sourceTarget}_compileMaterial(e){this._boxMesh.material=e,this._renderer.compile(this._boxMesh,this._cubeCamera.children[0])}_renderCube(e,t,n){let s=this._boxMesh,r=this._cubeCamera;s.material=n,r.renderTarget=e,r.activeMipmapLevel=t;let a=e.width>>t;e.viewport.set(0,0,a,a),r.update(this._renderer,s),e.viewport.set(0,0,e.width,e.height)}_textureToCubemap(e){let t;e.mapping===fi||e.mapping===qi?(this._cubemapMaterial===null&&(this._cubemapMaterial=oh()),t=this._cubemapMaterial,t.uniforms.flipEnvMap.value=e.isRenderTargetTexture===!1?-1:1):(this._equirectMaterial===null&&(this._equirectMaterial=ah()),t=this._equirectMaterial),t.uniforms.envMap.value=e,this._renderCube(this._getSourceTarget(),0,t)}_applyPMREM(e){this._ggxMaterial===null&&(this._ggxMaterial=Nf(),this._integrationMaterial=Uf());let t=this._cubeSize,n=e.texture.mipmaps.length-1,s=this._ggxMaterial.uniforms;s.envMap.value=this._sourceTarget.texture;let r=this._integrationMaterial.uniforms;r.envMap.value=this._sourceTarget.texture,r.sourceLod.value=Math.log2(t/Rh);for(let a=0;a<=n;a++){let o=i.lodToRoughness(a,n);if(a>n-If)r.roughness.value=o,this._renderCube(e,a,this._integrationMaterial);else{let l=o>0?Math.log2(t)+.5*Math.log2(6/(wh*Math.pow(o,4)))+.5:0;s.roughness.value=o,s.lodBias.value=l,this._renderCube(e,a,this._ggxMaterial)}}}_blur(e,t){this._blurMaterial===null&&(this._blurMaterial=Ff());let n=this._blurMaterial,s=n.uniforms,r=this._sourceTarget;s.sigma.value=Math.min(t,Math.PI)/Math.SQRT2,s.envMap.value=r.texture,this._renderCube(e,0,n),s.envMap.value=e.texture,this._renderCube(r,0,n)}};function rh(i,e,t){return new ks(i,{minFilter:Dn,generateMipmaps:e,type:un,colorSpace:os,depthBuffer:t})}function Gs(i,e,t){return new tn({name:i,uniforms:e,vertexShader:ze.cube_vert,fragmentShader:t,side:Tt,blending:ui,depthTest:!1,depthWrite:!1})}function Nf(){return Gs("PMREMGGXConvolution",{envMap:{value:null},roughness:{value:0},lodBias:{value:0}},`

		#define GGX_SAMPLES ${wh}u

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float roughness;
		uniform float lodBias;

		#include <common>

		// Van der Corput radical inverse
		float radicalInverse_VdC( uint bits ) {

			bits = ( bits << 16u ) | ( bits >> 16u );
			bits = ( ( bits & 0x55555555u ) << 1u ) | ( ( bits & 0xAAAAAAAAu ) >> 1u );
			bits = ( ( bits & 0x33333333u ) << 2u ) | ( ( bits & 0xCCCCCCCCu ) >> 2u );
			bits = ( ( bits & 0x0F0F0F0Fu ) << 4u ) | ( ( bits & 0xF0F0F0F0u ) >> 4u );
			bits = ( ( bits & 0x00FF00FFu ) << 8u ) | ( ( bits & 0xFF00FF00u ) >> 8u );
			return float( bits ) * 2.3283064365386963e-10; // / 0x100000000

		}

		// Hammersley sequence
		vec2 hammersley( uint i, uint N ) {

			return vec2( float( i ) / float( N ), radicalInverse_VdC( i ) );

		}

		void main() {

			vec3 N = normalize( vWorldDirection );

			// For very low roughness, just sample the environment directly
			if ( roughness < 0.001 ) {

				gl_FragColor = vec4( textureLod( envMap, N, 0.0 ).rgb, 1.0 );
				return;

			}

			float alpha = roughness * roughness;
			float alpha2 = alpha * alpha;

			// Tangent space basis for VNDF sampling
			vec3 up = abs( N.z ) < 0.999 ? vec3( 0.0, 0.0, 1.0 ) : vec3( 1.0, 0.0, 0.0 );
			vec3 tangent = normalize( cross( up, N ) );
			vec3 bitangent = cross( N, tangent );

			vec3 prefilteredColor = vec3( 0.0 );
			float totalWeight = 0.0;

			for ( uint i = 0u; i < GGX_SAMPLES; i ++ ) {

				vec2 Xi = hammersley( i, GGX_SAMPLES );

				// With V = N, sample the reflected direction directly.
				float invQ = 1.0 / ( 1.0 - Xi.x + alpha2 * Xi.x );
				float NdotL = ( 1.0 - Xi.x - alpha2 * Xi.x ) * invQ;

				if ( NdotL > 0.0 ) {

					float phi = 2.0 * PI * Xi.y;
					float sinTheta = 2.0 * alpha * sqrt( Xi.x * ( 1.0 - Xi.x ) ) * invQ;
					vec3 L = N * NdotL + ( tangent * cos( phi ) + bitangent * sin( phi ) ) * sinTheta;

					// Match the source mip to the sample's solid angle. The terms
					// independent of the sample are precomputed in lodBias.
					float d = alpha2 * invQ;
					float lod = max( log2( d ) + lodBias, 0.0 );

					// Weight by NdotL for the split-sum approximation
					prefilteredColor += textureLod( envMap, L, lod ).rgb * NdotL;
					totalWeight += NdotL;

				}

			}

			gl_FragColor = vec4( prefilteredColor / totalWeight, 1.0 );

		}
	`)}function Uf(){return Gs("PMREMGGXIntegration",{envMap:{value:null},roughness:{value:0},sourceLod:{value:0},sourceSize:{value:Rh}},`

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float roughness;
		uniform float sourceLod;
		uniform int sourceSize;

		void main() {

			vec3 N = normalize( vWorldDirection );

			float alpha = roughness * roughness;
			float alpha2 = alpha * alpha;

			float texelSize = 2.0 / float( sourceSize );

			vec3 prefilteredColor = vec3( 0.0 );
			float totalWeight = 0.0;

			// Pair opposite texels: only the one in N's hemisphere contributes.
			for ( int face = 0; face < 3; face ++ ) {

				for ( int y = 0; y < sourceSize; y ++ ) {

					for ( int x = 0; x < sourceSize; x ++ ) {

						vec2 uv = ( vec2( x, y ) + 0.5 ) * texelSize - 1.0;
						vec3 texelDirection = face == 0 ? vec3( 1.0, uv ) : ( face == 1 ? vec3( uv.x, 1.0, uv.y ) : vec3( uv, 1.0 ) );

						float invDistance = inversesqrt( 1.0 + dot( uv, uv ) );
						float NdotL = dot( N, texelDirection );
						texelDirection *= NdotL < 0.0 ? - 1.0 : 1.0;
						NdotL = abs( NdotL ) * invDistance;

						// With V = N, NdotH squared is ( 1 + NdotL ) / 2. Common factors
						// in the GGX distribution and texel solid angle cancel when normalized.
						float d = 1.0 + alpha2 + ( alpha2 - 1.0 ) * NdotL;
						float weight = NdotL * invDistance * invDistance * invDistance / ( d * d );

						prefilteredColor += textureLod( envMap, texelDirection, sourceLod ).rgb * weight;
						totalWeight += weight;

					}

				}

			}

			gl_FragColor = vec4( prefilteredColor / totalWeight, 1.0 );

		}
	`)}function Ff(){return Gs("PMREMSphericalGaussianBlur",{envMap:{value:null},sigma:{value:0}},`

		#define SAMPLES ${Pf}
		#define GOLDEN_ANGLE 2.39996322973

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float sigma;

		#include <common>

		void main() {

			vec3 outputDirection = normalize( vWorldDirection );

			vec3 up = abs( outputDirection.z ) < 0.999 ? vec3( 0.0, 0.0, 1.0 ) : vec3( 1.0, 0.0, 0.0 );
			vec3 tangent = normalize( cross( up, outputDirection ) );
			vec3 bitangent = cross( outputDirection, tangent );

			// Truncate the kernel at three standard deviations or at the antipode.
			float thetaMax = min( 3.0 * sigma, PI );
			float truncation = 1.0 - exp( - 0.5 * thetaMax * thetaMax / ( sigma * sigma ) );

			vec3 accumColor = vec3( 0.0 );
			float accumWeight = 0.0;

			for ( int i = 0; i < SAMPLES; i ++ ) {

				// Stratified inverse-CDF sampling of the Gaussian, placed on a golden-angle spiral.
				float stratum = ( float( i ) + 0.5 ) / float( SAMPLES );
				float theta = sigma * sqrt( - 2.0 * log( 1.0 - stratum * truncation ) );
				float phi = float( i ) * GOLDEN_ANGLE;

				vec3 offset = cos( phi ) * tangent + sin( phi ) * bitangent;
				vec3 sampleDirection = cos( theta ) * outputDirection + sin( theta ) * offset;

				// Correct the planar sample density to solid angle.
				float weight = sin( theta ) / theta;

				accumColor += weight * textureLod( envMap, sampleDirection, 0.0 ).rgb;
				accumWeight += weight;

			}

			gl_FragColor = vec4( accumColor / accumWeight, 1.0 );

		}
	`)}function ah(){return Gs("PMREMEquirectangularToCubemap",{envMap:{value:null}},`

		varying vec3 vWorldDirection;

		uniform sampler2D envMap;

		#include <common>

		void main() {

			// Average four subpixel samples to preserve small, bright features.
			vec3 direction = normalize( vWorldDirection );
			vec3 dx = dFdx( direction ) * 0.25;
			vec3 dy = dFdy( direction ) * 0.25;

			vec3 color = textureLod( envMap, equirectUv( normalize( direction - dx - dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction + dx - dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction - dx + dy ) ), 0.0 ).rgb;
			color += textureLod( envMap, equirectUv( normalize( direction + dx + dy ) ), 0.0 ).rgb;
			gl_FragColor = vec4( color * 0.25, 1.0 );

		}
	`)}function oh(){return Gs("PMREMCubemapToCubemap",{envMap:{value:null},flipEnvMap:{value:-1}},`

		varying vec3 vWorldDirection;

		uniform samplerCube envMap;
		uniform float flipEnvMap;

		void main() {

			gl_FragColor = vec4( textureCube( envMap, vec3( flipEnvMap * vWorldDirection.x, vWorldDirection.yz ) ).rgb, 1.0 );

		}
	`)}function Of(i){let e=new WeakMap,t=new WeakMap,n=null;function s(d,m=!1){return d==null?null:m?a(d):r(d)}function r(d){if(d&&d.isTexture){let m=d.mapping;if(m===Jr||m===$r)if(e.has(d)){let _=e.get(d).texture;return o(_,d.mapping)}else{let _=d.image;if(_&&_.height>0){let S=new ks(_.height);return S.fromEquirectangularTexture(i,d),e.set(d,S),d.addEventListener("dispose",c),o(S.texture,d.mapping)}else return null}}return d}function a(d){if(d&&d.isTexture&&d.isPMREMTexture!==!0){let m=d.mapping,_=m===Jr||m===$r,S=m===fi||m===qi;if(_||S){let p=t.get(d),u=p!==void 0?p.texture.pmremVersion:0;if(d.isRenderTargetTexture&&d.pmremVersion!==u)return n===null&&(n=new Oa(i)),p=_?n.fromEquirectangular(d,p):n.fromCubemap(d,p),p.texture.pmremVersion=d.pmremVersion,t.set(d,p),p.texture;if(p!==void 0)return p.texture;{let M=d.image;return _&&M&&M.height>0||S&&M&&l(M)?(n===null&&(n=new Oa(i)),p=_?n.fromEquirectangular(d):n.fromCubemap(d),p.texture.pmremVersion=d.pmremVersion,t.set(d,p),d.addEventListener("dispose",h),p.texture):null}}}return d}function o(d,m){return m===Jr?d.mapping=fi:m===$r&&(d.mapping=qi),d}function l(d){let m=0,_=6;for(let S=0;S<_;S++)d[S]!==void 0&&m++;return m===_}function c(d){let m=d.target;m.removeEventListener("dispose",c);let _=e.get(m);_!==void 0&&(e.delete(m),_.dispose())}function h(d){let m=d.target;m.removeEventListener("dispose",h);let _=t.get(m);_!==void 0&&(t.delete(m),_.dispose())}function g(){e=new WeakMap,t=new WeakMap,n!==null&&(n.dispose(),n=null)}return{get:s,dispose:g}}function Bf(i){let e={};function t(n){if(e[n]!==void 0)return e[n];let s=i.getExtension(n);return e[n]=s,s}return{has:function(n){return t(n)!==null},init:function(){t("EXT_color_buffer_float"),t("WEBGL_clip_cull_distance"),t("OES_texture_float_linear"),t("EXT_color_buffer_half_float"),t("WEBGL_multisampled_render_to_texture"),t("WEBGL_render_shared_exponent")},get:function(n){let s=t(n);return s===null&&is("WebGLRenderer: "+n+" extension not supported."),s}}}function zf(i,e,t,n){let s={},r=new WeakMap,a=new FinalizationRegistry(_=>delete s[_]);function o(_){l(_.target)}function l(_){_.index!==null&&e.remove(_.index);for(let p in _.attributes)e.remove(_.attributes[p]);_.removeEventListener("dispose",o),delete s[_.id],a.unregister(_);let S=r.get(_);S&&(e.remove(S),r.delete(_)),n.releaseStatesOfGeometry(_),_.isInstancedBufferGeometry===!0&&delete _._maxInstanceCount,t.memory.geometries--}function c(_,S){return s[S.id]!==void 0||(S.addEventListener("dispose",o),s[S.id]=new WeakRef(S),a.register(S,S.id,S),t.memory.geometries++),S}function h(_){let S=_.attributes;for(let p in S)e.update(S[p],i.ARRAY_BUFFER)}function g(_){let S=_.index,p=_.attributes.position,u=0;if(p===void 0)return;let M=S!==null?S.array.length:p.array.length/3-1,w=p.count>=65535?fs:ds,E=new w(Math.ceil(M/3)*6,1),A=E.array;if(S!==null){let f=S.array;u=S.version;for(let v=0,N=0;v<M;v+=3){let I=f[v+0],D=f[v+1],z=f[v+2];A[N++]=I,A[N++]=D,A[N++]=D,A[N++]=z,A[N++]=z,A[N++]=I}}else{u=p.version;for(let f=0,v=0;f<M;f+=3){let N=f+0,I=f+1,D=f+2;A[v++]=N,A[v++]=I,A[v++]=I,A[v++]=D,A[v++]=D,A[v++]=N}}E.version=u;let T=r.get(_);T&&e.remove(T),r.set(_,E)}function d(_){let S=r.get(_);if(S){let p=_.index;p!==null&&S.version<p.version&&g(_)}else g(_);return r.get(_)}function m(){for(let _ in s){let S=s[_].deref();S!==void 0&&l(S)}}return{get:c,update:h,getWireframeAttribute:d,dispose:m}}function kf(i,e,t){let n;function s(g){n=g}let r,a;function o(g){r=g.type,a=g.bytesPerElement}function l(g,d){i.drawElements(n,d,r,g*a),t.update(d,n,1)}function c(g,d,m){m!==0&&(i.drawElementsInstanced(n,d,r,g*a,m),t.update(d,n,m))}function h(g,d,m){if(m===0)return;e.get("WEBGL_multi_draw").multiDrawElementsWEBGL(n,d,0,r,g,0,m);let S=0;for(let p=0;p<m;p++)S+=d[p];t.update(S,n,1)}this.setMode=s,this.setIndex=o,this.render=l,this.renderInstances=c,this.renderMultiDraw=h}function Gf(i){let e={geometries:0,textures:0},t={frame:0,calls:0,triangles:0,points:0,lines:0};function n(r,a,o){switch(t.calls++,a){case i.TRIANGLES:t.triangles+=o*(r/3);break;case i.LINES:t.lines+=o*(r/2);break;case i.LINE_STRIP:t.lines+=o*(r-1);break;case i.LINE_LOOP:t.lines+=o*r;break;case i.POINTS:t.points+=o*r;break;default:Pe("WebGLInfo: Unknown draw mode:",a);break}}function s(){t.calls=0,t.triangles=0,t.points=0,t.lines=0}return{memory:e,render:t,programs:null,autoReset:!0,reset:s,update:n}}function Vf(i,e,t){let n=new WeakMap,s=new at;function r(a,o,l){let c=a.morphTargetInfluences,h=o.morphAttributes.position||o.morphAttributes.normal||o.morphAttributes.color,g=h!==void 0?h.length:0,d=n.get(o);if(d===void 0||d.count!==g){let N=function(){f.dispose(),n.delete(o),o.removeEventListener("dispose",N)};d!==void 0&&d.texture.dispose();let m=o.morphAttributes.position!==void 0,_=o.morphAttributes.normal!==void 0,S=o.morphAttributes.color!==void 0,p=o.morphAttributes.position||[],u=o.morphAttributes.normal||[],M=o.morphAttributes.color||[],w=0;m===!0&&(w=1),_===!0&&(w=2),S===!0&&(w=3);let E=o.attributes.position.count*w,A=1;E>e.maxTextureSize&&(A=Math.ceil(E/e.maxTextureSize),E=e.maxTextureSize);let T=new Float32Array(E*A*4*g),f=new hs(T,E,A,g);f.type=hn,f.needsUpdate=!0;let v=w*4;for(let I=0;I<g;I++){let D=p[I],z=u[I],q=M[I],P=E*A*4*I;for(let W=0;W<D.count;W++){let $=W*v;m===!0&&(s.fromBufferAttribute(D,W),T[P+$+0]=s.x,T[P+$+1]=s.y,T[P+$+2]=s.z,T[P+$+3]=0),_===!0&&(s.fromBufferAttribute(z,W),T[P+$+4]=s.x,T[P+$+5]=s.y,T[P+$+6]=s.z,T[P+$+7]=0),S===!0&&(s.fromBufferAttribute(q,W),T[P+$+8]=s.x,T[P+$+9]=s.y,T[P+$+10]=s.z,T[P+$+11]=q.itemSize===4?s.w:1)}}d={count:g,texture:f,size:new Re(E,A)},n.set(o,d),o.addEventListener("dispose",N)}if(a.isInstancedMesh===!0&&a.morphTexture!==null)l.getUniforms().setValue(i,"morphTexture",a.morphTexture,t);else{let m=0;for(let S=0;S<c.length;S++)m+=c[S];let _=o.morphTargetsRelative?1:1-m;l.getUniforms().setValue(i,"morphTargetBaseInfluence",_),l.getUniforms().setValue(i,"morphTargetInfluences",c)}l.getUniforms().setValue(i,"morphTargetsTexture",d.texture,t),l.getUniforms().setValue(i,"morphTargetsTextureSize",d.size)}return{update:r}}function Hf(i,e,t,n,s){let r=new WeakMap;function a(c){let h=s.render.frame,g=c.geometry,d=e.get(c,g);if(r.get(d)!==h&&(e.update(d),r.set(d,h)),c.isInstancedMesh&&(c.hasEventListener("dispose",l)===!1&&c.addEventListener("dispose",l),r.get(c)!==h&&(t.update(c.instanceMatrix,i.ARRAY_BUFFER),c.instanceColor!==null&&t.update(c.instanceColor,i.ARRAY_BUFFER),r.set(c,h))),c.isSkinnedMesh){let m=c.skeleton;r.get(m)!==h&&(m.update(),r.set(m,h))}return d}function o(){r=new WeakMap}function l(c){let h=c.target;h.removeEventListener("dispose",l),n.releaseStatesOfObject(h),t.remove(h.instanceMatrix),h.instanceColor!==null&&t.remove(h.instanceColor)}return{update:a,dispose:o}}var Wf={[Po]:"LINEAR_TONE_MAPPING",[Io]:"REINHARD_TONE_MAPPING",[Lo]:"CINEON_TONE_MAPPING",[Do]:"ACES_FILMIC_TONE_MAPPING",[Uo]:"AGX_TONE_MAPPING",[Fo]:"NEUTRAL_TONE_MAPPING",[No]:"CUSTOM_TONE_MAPPING"};function Xf(i,e,t,n,s,r){let a=new Yt(e,t,{type:i,depthBuffer:s,stencilBuffer:r,samples:n?4:0,storeMultisampledDepthBuffer:!1,storeMultisampledStencilBuffer:!1,resolveDepthBuffer:!1,resolveStencilBuffer:!1}),o=null,l=null,c=null,h=new kt;h.setAttribute("position",new ct([-1,3,0,-1,-1,0,3,-1,0],3)),h.setAttribute("uv",new ct([0,2,0,0,2,0],2));let g=new Lr({uniforms:{tDiffuse:{value:null}},vertexShader:`
			precision highp float;

			uniform mat4 modelViewMatrix;
			uniform mat4 projectionMatrix;

			attribute vec3 position;
			attribute vec2 uv;

			varying vec2 vUv;

			void main() {
				vUv = uv;
				gl_Position = projectionMatrix * modelViewMatrix * vec4( position, 1.0 );
			}`,fragmentShader:`
			precision highp float;

			uniform sampler2D tDiffuse;

			varying vec2 vUv;

			#include <tonemapping_pars_fragment>
			#include <colorspace_pars_fragment>

			void main() {
				gl_FragColor = texture2D( tDiffuse, vUv );

				#ifdef LINEAR_TONE_MAPPING
					gl_FragColor.rgb = LinearToneMapping( gl_FragColor.rgb );
				#elif defined( REINHARD_TONE_MAPPING )
					gl_FragColor.rgb = ReinhardToneMapping( gl_FragColor.rgb );
				#elif defined( CINEON_TONE_MAPPING )
					gl_FragColor.rgb = CineonToneMapping( gl_FragColor.rgb );
				#elif defined( ACES_FILMIC_TONE_MAPPING )
					gl_FragColor.rgb = ACESFilmicToneMapping( gl_FragColor.rgb );
				#elif defined( AGX_TONE_MAPPING )
					gl_FragColor.rgb = AgXToneMapping( gl_FragColor.rgb );
				#elif defined( NEUTRAL_TONE_MAPPING )
					gl_FragColor.rgb = NeutralToneMapping( gl_FragColor.rgb );
				#elif defined( CUSTOM_TONE_MAPPING )
					gl_FragColor.rgb = CustomToneMapping( gl_FragColor.rgb );
				#endif

				#ifdef SRGB_TRANSFER
					gl_FragColor = sRGBTransferOETF( gl_FragColor );
				#endif
			}`,depthTest:!1,depthWrite:!1}),d=new Ot(h,g),m=new Es(-1,1,1,-1,0,1),_=null,S=null,p=!1,u,M=null,w=[],E=!1;this.setSize=function(A,T){a.setSize(A,T),o!==null&&o.setSize(A,T),l!==null&&l.setSize(A,T);for(let f=0;f<w.length;f++){let v=w[f];v.setSize&&v.setSize(A,T)}},this.setEffects=function(A){w=A,E=w.length>0&&w[0].isRenderPass===!0;let T=a.width,f=a.height;w.length>0&&o===null&&(o=new Yt(T,f,{type:un,depthBuffer:!1,stencilBuffer:!1}),l=new Yt(T,f,{type:un,depthBuffer:!1,stencilBuffer:!1}));let v=s===!0&&w.some(N=>N.needsDepthTexture===!0);v!==(a.depthTexture!==null)&&(v===!0&&c===null&&(c=new Ln(T,f),r===!0&&(c.format=Nn,c.type=pi)),a.dispose(),a.depthTexture=v?c:null,a.resolveDepthBuffer=v,a.storeMultisampledDepthBuffer=v);for(let N=0;N<w.length;N++){let I=w[N];I.setSize&&I.setSize(T,f),v&&I.needsDepthTexture===!0&&I.setDepthTexture&&I.setDepthTexture(c)}},this.begin=function(A,T){if(p||A.toneMapping===xn&&w.length===0)return!1;if(M=T,T!==null){let f=T.width,v=T.height;(a.width!==f||a.height!==v)&&this.setSize(f,v)}return E===!1&&A.setRenderTarget(a),u=A.toneMapping,A.toneMapping=xn,!0},this.hasRenderPass=function(){return E},this.end=function(A,T){A.toneMapping=u,p=!0;let f=a,v=o;for(let N=0;N<w.length;N++){let I=w[N];I.enabled!==!1&&(I.render(A,v,f,T),I.needsSwap!==!1&&(f=v,v=v===o?l:o))}if(_!==A.outputColorSpace||S!==A.toneMapping){_=A.outputColorSpace,S=A.toneMapping,g.defines={},We.getTransfer(_)===$e&&(g.defines.SRGB_TRANSFER="");let N=Wf[S];N&&(g.defines[N]=""),g.needsUpdate=!0}g.uniforms.tDiffuse.value=f.texture,A.setRenderTarget(M),A.render(d,m),M=null,p=!1},this.isCompositing=function(){return p},this.dispose=function(){a.dispose(),o!==null&&o.dispose(),l!==null&&l.dispose(),h.dispose(),g.dispose()}}var Ch=new zt,Ph=new Ln(1,1),Ih=new gs(1),Lh=new hs,Dh=new wr,Nh=new ms,lh=[],ch=[],hh=new Float32Array(16),uh=new Float32Array(9),dh=new Float32Array(4);function $i(i,e,t){let n=i[0];if(n<=0||n>0)return i;let s=e*t,r=lh[s];if(r===void 0&&(r=new Float32Array(s),lh[s]=r),e!==0){n.toArray(r,0);for(let a=1,o=0;a!==e;++a)o+=t,i[a].toArray(r,o)}return r}function mt(i,e){if(i.length!==e.length)return!1;for(let t=0,n=i.length;t<n;t++)if(i[t]!==e[t])return!1;return!0}function gt(i,e){for(let t=0,n=e.length;t<n;t++)i[t]=e[t]}function za(i,e){let t=ch[e];t===void 0&&(t=new Int32Array(e),ch[e]=t);for(let n=0;n!==e;++n)t[n]=i.allocateTextureUnit();return t}function qf(i,e){let t=this.cache;t[0]!==e&&(i.uniform1f(this.addr,e),t[0]=e)}function Yf(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(i.uniform2f(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(mt(t,e))return;i.uniform2fv(this.addr,e),gt(t,e)}}function Zf(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(i.uniform3f(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else if(e.r!==void 0)(t[0]!==e.r||t[1]!==e.g||t[2]!==e.b)&&(i.uniform3f(this.addr,e.r,e.g,e.b),t[0]=e.r,t[1]=e.g,t[2]=e.b);else{if(mt(t,e))return;i.uniform3fv(this.addr,e),gt(t,e)}}function Jf(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(i.uniform4f(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(mt(t,e))return;i.uniform4fv(this.addr,e),gt(t,e)}}function $f(i,e){let t=this.cache,n=e.elements;if(n===void 0){if(mt(t,e))return;i.uniformMatrix2fv(this.addr,!1,e),gt(t,e)}else{if(mt(t,n))return;dh.set(n),i.uniformMatrix2fv(this.addr,!1,dh),gt(t,n)}}function Kf(i,e){let t=this.cache,n=e.elements;if(n===void 0){if(mt(t,e))return;i.uniformMatrix3fv(this.addr,!1,e),gt(t,e)}else{if(mt(t,n))return;uh.set(n),i.uniformMatrix3fv(this.addr,!1,uh),gt(t,n)}}function jf(i,e){let t=this.cache,n=e.elements;if(n===void 0){if(mt(t,e))return;i.uniformMatrix4fv(this.addr,!1,e),gt(t,e)}else{if(mt(t,n))return;hh.set(n),i.uniformMatrix4fv(this.addr,!1,hh),gt(t,n)}}function Qf(i,e){let t=this.cache;t[0]!==e&&(i.uniform1i(this.addr,e),t[0]=e)}function ep(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(i.uniform2i(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(mt(t,e))return;i.uniform2iv(this.addr,e),gt(t,e)}}function tp(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(i.uniform3i(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else{if(mt(t,e))return;i.uniform3iv(this.addr,e),gt(t,e)}}function np(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(i.uniform4i(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(mt(t,e))return;i.uniform4iv(this.addr,e),gt(t,e)}}function ip(i,e){let t=this.cache;t[0]!==e&&(i.uniform1ui(this.addr,e),t[0]=e)}function sp(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y)&&(i.uniform2ui(this.addr,e.x,e.y),t[0]=e.x,t[1]=e.y);else{if(mt(t,e))return;i.uniform2uiv(this.addr,e),gt(t,e)}}function rp(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z)&&(i.uniform3ui(this.addr,e.x,e.y,e.z),t[0]=e.x,t[1]=e.y,t[2]=e.z);else{if(mt(t,e))return;i.uniform3uiv(this.addr,e),gt(t,e)}}function ap(i,e){let t=this.cache;if(e.x!==void 0)(t[0]!==e.x||t[1]!==e.y||t[2]!==e.z||t[3]!==e.w)&&(i.uniform4ui(this.addr,e.x,e.y,e.z,e.w),t[0]=e.x,t[1]=e.y,t[2]=e.z,t[3]=e.w);else{if(mt(t,e))return;i.uniform4uiv(this.addr,e),gt(t,e)}}function ka(i){return i.version===0&&(i.compareFunction=Yo,i.needsUpdate=!0),i}function op(i,e,t){let n=this.cache,s=t.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r;this.type===i.SAMPLER_2D_SHADOW?r=ka(Ph):r=Ch,t.setTexture2D(e||r,s)}function lp(i,e,t){let n=this.cache,s=t.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),t.setTexture3D(e||Dh,s)}function cp(i,e,t){let n=this.cache,s=t.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s);let r;this.type===i.SAMPLER_CUBE_SHADOW?r=ka(Ih):r=Nh,t.setTextureCube(e||r,s)}function hp(i,e,t){let n=this.cache,s=t.allocateTextureUnit();n[0]!==s&&(i.uniform1i(this.addr,s),n[0]=s),t.setTexture2DArray(e||Lh,s)}function up(i){switch(i){case 5126:return qf;case 35664:return Yf;case 35665:return Zf;case 35666:return Jf;case 35674:return $f;case 35675:return Kf;case 35676:return jf;case 5124:case 35670:return Qf;case 35667:case 35671:return ep;case 35668:case 35672:return tp;case 35669:case 35673:return np;case 5125:return ip;case 36294:return sp;case 36295:return rp;case 36296:return ap;case 35678:case 36198:case 36298:case 36306:case 35682:return op;case 35679:case 36299:case 36307:return lp;case 35680:case 36300:case 36308:case 36293:return cp;case 36289:case 36303:case 36311:case 36292:return hp}}function dp(i,e){i.uniform1fv(this.addr,e)}function fp(i,e){let t=$i(e,this.size,2);i.uniform2fv(this.addr,t)}function pp(i,e){let t=$i(e,this.size,3);i.uniform3fv(this.addr,t)}function mp(i,e){let t=$i(e,this.size,4);i.uniform4fv(this.addr,t)}function gp(i,e){let t=$i(e,this.size,4);i.uniformMatrix2fv(this.addr,!1,t)}function _p(i,e){let t=$i(e,this.size,9);i.uniformMatrix3fv(this.addr,!1,t)}function xp(i,e){let t=$i(e,this.size,16);i.uniformMatrix4fv(this.addr,!1,t)}function yp(i,e){i.uniform1iv(this.addr,e)}function vp(i,e){i.uniform2iv(this.addr,e)}function Sp(i,e){i.uniform3iv(this.addr,e)}function Mp(i,e){i.uniform4iv(this.addr,e)}function bp(i,e){i.uniform1uiv(this.addr,e)}function Ep(i,e){i.uniform2uiv(this.addr,e)}function Tp(i,e){i.uniform3uiv(this.addr,e)}function Ap(i,e){i.uniform4uiv(this.addr,e)}function wp(i,e,t){let n=this.cache,s=e.length,r=za(t,s);mt(n,r)||(i.uniform1iv(this.addr,r),gt(n,r));let a;this.type===i.SAMPLER_2D_SHADOW?a=ka(Ph):a=Ch;for(let o=0;o!==s;++o)t.setTexture2D(e[o]||a,r[o])}function Rp(i,e,t){let n=this.cache,s=e.length,r=za(t,s);mt(n,r)||(i.uniform1iv(this.addr,r),gt(n,r));for(let a=0;a!==s;++a)t.setTexture3D(e[a]||Dh,r[a])}function Cp(i,e,t){let n=this.cache,s=e.length,r=za(t,s);mt(n,r)||(i.uniform1iv(this.addr,r),gt(n,r));let a;this.type===i.SAMPLER_CUBE_SHADOW?a=ka(Ih):a=Nh;for(let o=0;o!==s;++o)t.setTextureCube(e[o]||a,r[o])}function Pp(i,e,t){let n=this.cache,s=e.length,r=za(t,s);mt(n,r)||(i.uniform1iv(this.addr,r),gt(n,r));for(let a=0;a!==s;++a)t.setTexture2DArray(e[a]||Lh,r[a])}function Ip(i){switch(i){case 5126:return dp;case 35664:return fp;case 35665:return pp;case 35666:return mp;case 35674:return gp;case 35675:return _p;case 35676:return xp;case 5124:case 35670:return yp;case 35667:case 35671:return vp;case 35668:case 35672:return Sp;case 35669:case 35673:return Mp;case 5125:return bp;case 36294:return Ep;case 36295:return Tp;case 36296:return Ap;case 35678:case 36198:case 36298:case 36306:case 35682:return wp;case 35679:case 36299:case 36307:return Rp;case 35680:case 36300:case 36308:case 36293:return Cp;case 36289:case 36303:case 36311:case 36292:return Pp}}var ul=class{constructor(e,t,n){this.id=e,this.addr=n,this.cache=[],this.type=t.type,this.setValue=up(t.type)}},dl=class{constructor(e,t,n){this.id=e,this.addr=n,this.cache=[],this.type=t.type,this.size=t.size,this.setValue=Ip(t.type)}},fl=class{constructor(e){this.id=e,this.seq=[],this.map={}}setValue(e,t,n){let s=this.seq;for(let r=0,a=s.length;r!==a;++r){let o=s[r];o.setValue(e,t[o.id],n)}}},cl=/(\w+)(\])?(\[|\.)?/g;function fh(i,e){i.seq.push(e),i.map[e.id]=e}function Lp(i,e,t){let n=i.name,s=n.length;for(cl.lastIndex=0;;){let r=cl.exec(n),a=cl.lastIndex,o=r[1],l=r[2]==="]",c=r[3];if(l&&(o=o|0),c===void 0||c==="["&&a+2===s){fh(t,c===void 0?new ul(o,i,e):new dl(o,i,e));break}else{let g=t.map[o];g===void 0&&(g=new fl(o),fh(t,g)),t=g}}}var Ji=class{constructor(e,t){this.seq=[],this.map={};let n=e.getProgramParameter(t,e.ACTIVE_UNIFORMS);for(let a=0;a<n;++a){let o=e.getActiveUniform(t,a),l=e.getUniformLocation(t,o.name);Lp(o,l,this)}let s=[],r=[];for(let a of this.seq)a.type===e.SAMPLER_2D_SHADOW||a.type===e.SAMPLER_CUBE_SHADOW||a.type===e.SAMPLER_2D_ARRAY_SHADOW?s.push(a):r.push(a);s.length>0&&(this.seq=s.concat(r))}setValue(e,t,n,s){let r=this.map[t];r!==void 0&&r.setValue(e,n,s)}setOptional(e,t,n){let s=t[n];s!==void 0&&this.setValue(e,n,s)}static upload(e,t,n,s){for(let r=0,a=t.length;r!==a;++r){let o=t[r],l=n[o.id];l.needsUpdate!==!1&&o.setValue(e,l.value,s)}}static seqWithValue(e,t){let n=[];for(let s=0,r=e.length;s!==r;++s){let a=e[s];a.id in t&&n.push(a)}return n}};function ph(i,e,t){let n=i.createShader(e);return i.shaderSource(n,t),i.compileShader(n),n}var Dp=37297,Np=0;function Up(i,e){let t=i.split(`
`),n=[],s=Math.max(e-6,0),r=Math.min(e+6,t.length);for(let a=s;a<r;a++){let o=a+1;n.push(`${o===e?">":" "} ${o}: ${t[a]}`)}return n.join(`
`)}var mh=new Ie;function Fp(i){We._getMatrix(mh,We.workingColorSpace,i);let e=`mat3( ${mh.elements.map(t=>t.toFixed(4))} )`;switch(We.getTransfer(i)){case ls:return[e,"LinearTransferOETF"];case $e:return[e,"sRGBTransferOETF"];default:return Te("WebGLProgram: Unsupported color space: ",i),[e,"LinearTransferOETF"]}}function gh(i,e,t){let n=i.getShaderParameter(e,i.COMPILE_STATUS),r=(i.getShaderInfoLog(e)||"").trim();if(n&&r==="")return"";let a=/ERROR: 0:(\d+)/.exec(r);if(a){let o=parseInt(a[1]);return t.toUpperCase()+`

`+r+`

`+Up(i.getShaderSource(e),o)}else return r}function Op(i,e){let t=Fp(e);return[`vec4 ${i}( vec4 value ) {`,`	return ${t[1]}( vec4( ${t[0]} * value.rgb, value.a ) );`,"}"].join(`
`)}var Bp={[Po]:"Linear",[Io]:"Reinhard",[Lo]:"Cineon",[Do]:"ACESFilmic",[Uo]:"AgX",[Fo]:"Neutral",[No]:"Custom"};function zp(i,e){let t=Bp[e];return t===void 0?(Te("WebGLProgram: Unsupported toneMapping:",e),"vec3 "+i+"( vec3 color ) { return LinearToneMapping( color ); }"):"vec3 "+i+"( vec3 color ) { return "+t+"ToneMapping( color ); }"}var Fa=new U;function kp(){We.getLuminanceCoefficients(Fa);let i=Fa.x.toFixed(4),e=Fa.y.toFixed(4),t=Fa.z.toFixed(4);return["float luminance( const in vec3 rgb ) {",`	const vec3 weights = vec3( ${i}, ${e}, ${t} );`,"	return dot( weights, rgb );","}"].join(`
`)}function Gp(i){return[i.extensionClipCullDistance?"#extension GL_ANGLE_clip_cull_distance : require":"",i.extensionMultiDraw?"#extension GL_ANGLE_multi_draw : require":""].filter(zs).join(`
`)}function Vp(i){let e=[];for(let t in i){let n=i[t];n!==!1&&e.push("#define "+t+" "+n)}return e.join(`
`)}function Hp(i,e){let t={},n=i.getProgramParameter(e,i.ACTIVE_ATTRIBUTES);for(let s=0;s<n;s++){let r=i.getActiveAttrib(e,s),a=r.name,o=1;r.type===i.FLOAT_MAT2&&(o=2),r.type===i.FLOAT_MAT3&&(o=3),r.type===i.FLOAT_MAT4&&(o=4),t[a]={type:r.type,location:i.getAttribLocation(e,a),locationSize:o}}return t}function zs(i){return i!==""}function _h(i,e){let t=e.numSpotLightShadows+e.numSpotLightMaps-e.numSpotLightShadowsWithMaps;return i.replace(/NUM_SUN_LIGHTS/g,e.numSunLights).replace(/NUM_DIR_LIGHTS/g,e.numDirLights).replace(/NUM_SPOT_LIGHTS/g,e.numSpotLights).replace(/NUM_SPOT_LIGHT_MAPS/g,e.numSpotLightMaps).replace(/NUM_SPOT_LIGHT_COORDS/g,t).replace(/NUM_RECT_AREA_LIGHTS/g,e.numRectAreaLights).replace(/NUM_POINT_LIGHTS/g,e.numPointLights).replace(/NUM_HEMI_LIGHTS/g,e.numHemiLights).replace(/NUM_SUN_LIGHT_SHADOWS/g,e.numSunLightShadows).replace(/NUM_DIR_LIGHT_SHADOWS/g,e.numDirLightShadows).replace(/NUM_SPOT_LIGHT_SHADOWS_WITH_MAPS/g,e.numSpotLightShadowsWithMaps).replace(/NUM_SPOT_LIGHT_SHADOWS/g,e.numSpotLightShadows).replace(/NUM_POINT_LIGHT_SHADOWS/g,e.numPointLightShadows).replace(/NUM_LIGHT_PROBE_GRIDS/g,e.numLightProbeGrids)}function xh(i,e){return i.replace(/NUM_CLIPPING_PLANES/g,e.numClippingPlanes).replace(/UNION_CLIPPING_PLANES/g,e.numClippingPlanes-e.numClipIntersection)}var Wp=/^[ \t]*#include +<([\w\d./]+)>/gm;function pl(i){return i.replace(Wp,Xp)}function Xp(i,e){let t=ze[e];if(t===void 0)throw new Error("THREE.WebGLProgram: Can not resolve #include <"+e+">");return pl(t)}var qp=/#pragma unroll_loop_start\s+for\s*\(\s*int\s+i\s*=\s*(\d+)\s*;\s*i\s*<\s*(\d+)\s*;\s*i\s*\+\+\s*\)\s*{([\s\S]+?)}\s+#pragma unroll_loop_end/g;function yh(i){return i.replace(qp,Yp)}function Yp(i,e,t,n){let s="";for(let r=parseInt(e);r<parseInt(t);r++)s+=n.replace(/\[\s*i\s*\]/g,"[ "+r+" ]").replace(/UNROLLED_LOOP_INDEX/g,r);return s}function vh(i){let e=`precision ${i.precision} float;
	precision ${i.precision} int;
	precision ${i.precision} sampler2D;
	precision ${i.precision} samplerCube;
	precision ${i.precision} sampler3D;
	precision ${i.precision} sampler2DArray;
	precision ${i.precision} sampler2DShadow;
	precision ${i.precision} samplerCubeShadow;
	precision ${i.precision} sampler2DArrayShadow;
	precision ${i.precision} isampler2D;
	precision ${i.precision} isampler3D;
	precision ${i.precision} isamplerCube;
	precision ${i.precision} isampler2DArray;
	precision ${i.precision} usampler2D;
	precision ${i.precision} usampler3D;
	precision ${i.precision} usamplerCube;
	precision ${i.precision} usampler2DArray;
	`;return i.precision==="highp"?e+=`
#define HIGH_PRECISION`:i.precision==="mediump"?e+=`
#define MEDIUM_PRECISION`:i.precision==="lowp"&&(e+=`
#define LOW_PRECISION`),e}var Zp={[Ps]:"SHADOWMAP_TYPE_PCF",[Wi]:"SHADOWMAP_TYPE_VSM"};function Jp(i){return Zp[i.shadowMapType]||"SHADOWMAP_TYPE_BASIC"}var $p={[qi]:"ENVMAP_MODE_REFRACTION"};function Kp(i){return i.envMap===!1?"ENVMAP_MODE_REFLECTION":$p[i.envMapMode]||"ENVMAP_MODE_REFLECTION"}var jp={[Zr]:"ENVMAP_BLENDING_MULTIPLY",[Fc]:"ENVMAP_BLENDING_MIX",[Oc]:"ENVMAP_BLENDING_ADD"};function Qp(i){return i.envMap===!1?"ENVMAP_BLENDING_NONE":jp[i.combine]||"ENVMAP_BLENDING_NONE"}function e2(i,e,t,n){let s=i.getContext(),r=t.defines,a=t.vertexShader,o=t.fragmentShader,l=Jp(t),c=t.envMapPMREM===!0?"ENVMAP_TYPE_PMREM":"ENVMAP_TYPE_CUBE",h=Kp(t),g=Qp(t),d=Gp(t),m=Vp(r),_=s.createProgram(),S,p,u=t.glslVersion?"#version "+t.glslVersion+`
`:"";t.isRawShaderMaterial?(S=["#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,m].filter(zs).join(`
`),S.length>0&&(S+=`
`),p=["#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,m].filter(zs).join(`
`),p.length>0&&(p+=`
`)):(S=[vh(t),"#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,m,t.extensionClipCullDistance?"#define USE_CLIP_DISTANCE":"",t.batching?"#define USE_BATCHING":"",t.batchingColor?"#define USE_BATCHING_COLOR":"",t.instancing?"#define USE_INSTANCING":"",t.instancingColor?"#define USE_INSTANCING_COLOR":"",t.instancingMorph?"#define USE_INSTANCING_MORPH":"",t.useFog&&t.fog?"#define USE_FOG":"",t.useFog&&t.fogExp2?"#define FOG_EXP2":"",t.map?"#define USE_MAP":"",t.envMap?"#define USE_ENVMAP":"",t.envMap?"#define "+h:"",t.lightMap?"#define USE_LIGHTMAP":"",t.aoMap?"#define USE_AOMAP":"",t.bumpMap?"#define USE_BUMPMAP":"",t.normalMap?"#define USE_NORMALMAP":"",t.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",t.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",t.displacementMap?"#define USE_DISPLACEMENTMAP":"",t.emissiveMap?"#define USE_EMISSIVEMAP":"",t.anisotropy?"#define USE_ANISOTROPY":"",t.anisotropyMap?"#define USE_ANISOTROPYMAP":"",t.clearcoatMap?"#define USE_CLEARCOATMAP":"",t.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",t.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",t.diffuseRoughnessMap?"#define USE_DIFFUSE_ROUGHNESSMAP":"",t.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",t.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",t.specularMap?"#define USE_SPECULARMAP":"",t.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",t.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",t.roughnessMap?"#define USE_ROUGHNESSMAP":"",t.metalnessMap?"#define USE_METALNESSMAP":"",t.alphaMap?"#define USE_ALPHAMAP":"",t.alphaHash?"#define USE_ALPHAHASH":"",t.transmission?"#define USE_TRANSMISSION":"",t.transmissionMap?"#define USE_TRANSMISSIONMAP":"",t.thicknessMap?"#define USE_THICKNESSMAP":"",t.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",t.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",t.mapUv?"#define MAP_UV "+t.mapUv:"",t.alphaMapUv?"#define ALPHAMAP_UV "+t.alphaMapUv:"",t.lightMapUv?"#define LIGHTMAP_UV "+t.lightMapUv:"",t.aoMapUv?"#define AOMAP_UV "+t.aoMapUv:"",t.emissiveMapUv?"#define EMISSIVEMAP_UV "+t.emissiveMapUv:"",t.bumpMapUv?"#define BUMPMAP_UV "+t.bumpMapUv:"",t.normalMapUv?"#define NORMALMAP_UV "+t.normalMapUv:"",t.displacementMapUv?"#define DISPLACEMENTMAP_UV "+t.displacementMapUv:"",t.metalnessMapUv?"#define METALNESSMAP_UV "+t.metalnessMapUv:"",t.roughnessMapUv?"#define ROUGHNESSMAP_UV "+t.roughnessMapUv:"",t.anisotropyMapUv?"#define ANISOTROPYMAP_UV "+t.anisotropyMapUv:"",t.clearcoatMapUv?"#define CLEARCOATMAP_UV "+t.clearcoatMapUv:"",t.clearcoatNormalMapUv?"#define CLEARCOAT_NORMALMAP_UV "+t.clearcoatNormalMapUv:"",t.clearcoatRoughnessMapUv?"#define CLEARCOAT_ROUGHNESSMAP_UV "+t.clearcoatRoughnessMapUv:"",t.diffuseRoughnessMapUv?"#define DIFFUSE_ROUGHNESSMAP_UV "+t.diffuseRoughnessMapUv:"",t.iridescenceMapUv?"#define IRIDESCENCEMAP_UV "+t.iridescenceMapUv:"",t.iridescenceThicknessMapUv?"#define IRIDESCENCE_THICKNESSMAP_UV "+t.iridescenceThicknessMapUv:"",t.sheenColorMapUv?"#define SHEEN_COLORMAP_UV "+t.sheenColorMapUv:"",t.sheenRoughnessMapUv?"#define SHEEN_ROUGHNESSMAP_UV "+t.sheenRoughnessMapUv:"",t.specularMapUv?"#define SPECULARMAP_UV "+t.specularMapUv:"",t.specularColorMapUv?"#define SPECULAR_COLORMAP_UV "+t.specularColorMapUv:"",t.specularIntensityMapUv?"#define SPECULAR_INTENSITYMAP_UV "+t.specularIntensityMapUv:"",t.transmissionMapUv?"#define TRANSMISSIONMAP_UV "+t.transmissionMapUv:"",t.thicknessMapUv?"#define THICKNESSMAP_UV "+t.thicknessMapUv:"",t.vertexTangents&&t.flatShading===!1?"#define USE_TANGENT":"",t.vertexNormals?"#define HAS_NORMAL":"",t.vertexColors?"#define USE_COLOR":"",t.vertexAlphas?"#define USE_COLOR_ALPHA":"",t.vertexUv1s?"#define USE_UV1":"",t.vertexUv2s?"#define USE_UV2":"",t.vertexUv3s?"#define USE_UV3":"",t.pointsUvs?"#define USE_POINTS_UV":"",t.flatShading?"#define FLAT_SHADED":"",t.skinning?"#define USE_SKINNING":"",t.morphTargets?"#define USE_MORPHTARGETS":"",t.morphNormals&&t.flatShading===!1?"#define USE_MORPHNORMALS":"",t.morphColors?"#define USE_MORPHCOLORS":"",t.morphTargetsCount>0?"#define MORPHTARGETS_TEXTURE_STRIDE "+t.morphTextureStride:"",t.morphTargetsCount>0?"#define MORPHTARGETS_COUNT "+t.morphTargetsCount:"",t.doubleSided?"#define DOUBLE_SIDED":"",t.flipSided?"#define FLIP_SIDED":"",t.shadowMapEnabled?"#define USE_SHADOWMAP":"",t.shadowMapEnabled?"#define "+l:"",t.sizeAttenuation?"#define USE_SIZEATTENUATION":"",t.numLightProbes>0?"#define USE_LIGHT_PROBES":"",t.logarithmicDepthBuffer?"#define USE_LOGARITHMIC_DEPTH_BUFFER":"",t.reversedDepthBuffer?"#define USE_REVERSED_DEPTH_BUFFER":"","uniform mat4 modelMatrix;","uniform mat4 modelViewMatrix;","uniform mat4 projectionMatrix;","uniform mat4 viewMatrix;","uniform mat3 normalMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;","#ifdef USE_INSTANCING","	attribute mat4 instanceMatrix;","#endif","#ifdef USE_INSTANCING_COLOR","	attribute vec3 instanceColor;","#endif","#ifdef USE_INSTANCING_MORPH","	uniform sampler2D morphTexture;","#endif","attribute vec3 position;","attribute vec3 normal;","attribute vec2 uv;","#ifdef USE_UV1","	attribute vec2 uv1;","#endif","#ifdef USE_UV2","	attribute vec2 uv2;","#endif","#ifdef USE_UV3","	attribute vec2 uv3;","#endif","#ifdef USE_TANGENT","	attribute vec4 tangent;","#endif","#if defined( USE_COLOR_ALPHA )","	attribute vec4 color;","#elif defined( USE_COLOR )","	attribute vec3 color;","#endif","#ifdef USE_SKINNING","	attribute vec4 skinIndex;","	attribute vec4 skinWeight;","#endif",`
`].filter(zs).join(`
`),p=[vh(t),"#define SHADER_TYPE "+t.shaderType,"#define SHADER_NAME "+t.shaderName,m,t.useFog&&t.fog?"#define USE_FOG":"",t.useFog&&t.fogExp2?"#define FOG_EXP2":"",t.alphaToCoverage?"#define ALPHA_TO_COVERAGE":"",t.map?"#define USE_MAP":"",t.matcap?"#define USE_MATCAP":"",t.envMap?"#define USE_ENVMAP":"",t.envMap?"#define "+c:"",t.envMap?"#define "+h:"",t.envMap?"#define "+g:"",t.envMapPMREM?"#define ENVMAP_MAX_LOD "+t.envMapMaxLod+".0":"",t.envMapPMREM?"#define ENVMAP_SIZE "+t.envMapSize+".0":"",t.lightMap?"#define USE_LIGHTMAP":"",t.aoMap?"#define USE_AOMAP":"",t.bumpMap?"#define USE_BUMPMAP":"",t.normalMap?"#define USE_NORMALMAP":"",t.normalMapObjectSpace?"#define USE_NORMALMAP_OBJECTSPACE":"",t.normalMapTangentSpace?"#define USE_NORMALMAP_TANGENTSPACE":"",t.packedNormalMap?"#define USE_PACKED_NORMALMAP":"",t.emissiveMap?"#define USE_EMISSIVEMAP":"",t.anisotropy?"#define USE_ANISOTROPY":"",t.anisotropyMap?"#define USE_ANISOTROPYMAP":"",t.clearcoat?"#define USE_CLEARCOAT":"",t.clearcoatMap?"#define USE_CLEARCOATMAP":"",t.clearcoatRoughnessMap?"#define USE_CLEARCOAT_ROUGHNESSMAP":"",t.clearcoatNormalMap?"#define USE_CLEARCOAT_NORMALMAP":"",t.diffuseRoughness?"#define USE_DIFFUSE_ROUGHNESS":"",t.diffuseRoughnessMap?"#define USE_DIFFUSE_ROUGHNESSMAP":"",t.dispersion?"#define USE_DISPERSION":"",t.retroreflection?"#define USE_RETROREFLECTION":"",t.iridescence?"#define USE_IRIDESCENCE":"",t.iridescenceMap?"#define USE_IRIDESCENCEMAP":"",t.iridescenceThicknessMap?"#define USE_IRIDESCENCE_THICKNESSMAP":"",t.specularMap?"#define USE_SPECULARMAP":"",t.specularColorMap?"#define USE_SPECULAR_COLORMAP":"",t.specularIntensityMap?"#define USE_SPECULAR_INTENSITYMAP":"",t.roughnessMap?"#define USE_ROUGHNESSMAP":"",t.metalnessMap?"#define USE_METALNESSMAP":"",t.alphaMap?"#define USE_ALPHAMAP":"",t.alphaTest?"#define USE_ALPHATEST":"",t.alphaHash?"#define USE_ALPHAHASH":"",t.sheen?"#define USE_SHEEN":"",t.sheenColorMap?"#define USE_SHEEN_COLORMAP":"",t.sheenRoughnessMap?"#define USE_SHEEN_ROUGHNESSMAP":"",t.transmission?"#define USE_TRANSMISSION":"",t.transmissionMap?"#define USE_TRANSMISSIONMAP":"",t.thicknessMap?"#define USE_THICKNESSMAP":"",t.vertexTangents&&t.flatShading===!1?"#define USE_TANGENT":"",t.vertexColors||t.instancingColor?"#define USE_COLOR":"",t.vertexAlphas||t.batchingColor?"#define USE_COLOR_ALPHA":"",t.vertexUv1s?"#define USE_UV1":"",t.vertexUv2s?"#define USE_UV2":"",t.vertexUv3s?"#define USE_UV3":"",t.pointsUvs?"#define USE_POINTS_UV":"",t.gradientMap?"#define USE_GRADIENTMAP":"",t.flatShading?"#define FLAT_SHADED":"",t.doubleSided?"#define DOUBLE_SIDED":"",t.flipSided?"#define FLIP_SIDED":"",t.shadowMapEnabled?"#define USE_SHADOWMAP":"",t.shadowMapEnabled?"#define "+l:"",t.premultipliedAlpha?"#define PREMULTIPLIED_ALPHA":"",t.numLightProbes>0?"#define USE_LIGHT_PROBES":"",t.decodeVideoTexture?"#define DECODE_VIDEO_TEXTURE":"",t.decodeVideoTextureEmissive?"#define DECODE_VIDEO_TEXTURE_EMISSIVE":"",t.logarithmicDepthBuffer?"#define USE_LOGARITHMIC_DEPTH_BUFFER":"",t.reversedDepthBuffer?"#define USE_REVERSED_DEPTH_BUFFER":"","uniform mat4 viewMatrix;","uniform vec3 cameraPosition;","uniform bool isOrthographic;",t.toneMapping!==xn?"#define TONE_MAPPING":"",t.toneMapping!==xn?ze.tonemapping_pars_fragment:"",t.toneMapping!==xn?zp("toneMapping",t.toneMapping):"",t.dithering?"#define DITHERING":"",t.opaque?"#define OPAQUE":"",ze.colorspace_pars_fragment,Op("linearToOutputTexel",t.outputColorSpace),kp(),t.useDepthPacking?"#define DEPTH_PACKING "+t.depthPacking:"",`
`].filter(zs).join(`
`)),a=pl(a),a=_h(a,t),a=xh(a,t),o=pl(o),o=_h(o,t),o=xh(o,t),a=yh(a),o=yh(o),t.isRawShaderMaterial!==!0&&(u=`#version 300 es
`,S=[d,"#define attribute in","#define varying out","#define texture2D texture"].join(`
`)+`
`+S,p=["#define varying in",t.glslVersion===Zo?"":"layout(location = 0) out highp vec4 pc_fragColor;",t.glslVersion===Zo?"":"#define gl_FragColor pc_fragColor","#define gl_FragDepthEXT gl_FragDepth","#define texture2D texture","#define textureCube texture","#define texture2DProj textureProj","#define texture2DLodEXT textureLod","#define texture2DProjLodEXT textureProjLod","#define textureCubeLodEXT textureLod","#define texture2DGradEXT textureGrad","#define texture2DProjGradEXT textureProjGrad","#define textureCubeGradEXT textureGrad"].join(`
`)+`
`+p);let M=u+S+a,w=u+p+o,E=ph(s,s.VERTEX_SHADER,M),A=ph(s,s.FRAGMENT_SHADER,w);s.attachShader(_,E),s.attachShader(_,A),t.index0AttributeName!==void 0?s.bindAttribLocation(_,0,t.index0AttributeName):t.hasPositionAttribute===!0&&s.bindAttribLocation(_,0,"position"),s.linkProgram(_);function T(I){if(i.debug.checkShaderErrors){let D=s.getProgramInfoLog(_)||"",z=s.getShaderInfoLog(E)||"",q=s.getShaderInfoLog(A)||"",P=D.trim(),W=z.trim(),$=q.trim(),G=!0,te=!0;if(s.getProgramParameter(_,s.LINK_STATUS)===!1)if(G=!1,typeof i.debug.onShaderError=="function")i.debug.onShaderError(s,_,E,A);else{let H=gh(s,E,"vertex"),j=gh(s,A,"fragment");Pe("WebGLProgram: Shader Error "+s.getError()+" - VALIDATE_STATUS "+s.getProgramParameter(_,s.VALIDATE_STATUS)+`

Material Name: `+I.name+`
Material Type: `+I.type+`

Program Info Log: `+P+`
`+H+`
`+j)}else P!==""?Te("WebGLProgram: Program Info Log:",P):(W===""||$==="")&&(te=!1);te&&(I.diagnostics={runnable:G,programLog:P,vertexShader:{log:W,prefix:S},fragmentShader:{log:$,prefix:p}})}s.deleteShader(E),s.deleteShader(A),f=new Ji(s,_),v=Hp(s,_)}let f;this.getUniforms=function(){return f===void 0&&T(this),f};let v;this.getAttributes=function(){return v===void 0&&T(this),v};let N=t.rendererExtensionParallelShaderCompile===!1;return this.isReady=function(){return N===!1&&(N=s.getProgramParameter(_,Dp)),N},this.destroy=function(){n.releaseStatesOfProgram(this),s.deleteProgram(_),this.program=void 0},this.type=t.shaderType,this.name=t.shaderName,this.id=Np++,this.cacheKey=e,this.usedTimes=1,this.program=_,this.vertexShader=E,this.fragmentShader=A,this}var t2=0,ml=class{constructor(){this.shaderCache=new Map,this.materialCache=new Map}update(e,t,n){let s=this._getShaderCacheForMaterial(e);return s.has(t)===!1&&(s.add(t),t.usedTimes++),s.has(n)===!1&&(s.add(n),n.usedTimes++),this}remove(e){let t=this.materialCache.get(e);for(let n of t)n.usedTimes--,n.usedTimes===0&&this.shaderCache.delete(n.code);return this.materialCache.delete(e),this}getVertexShaderStage(e){return this._getShaderStage(e.vertexShader)}getFragmentShaderStage(e){return this._getShaderStage(e.fragmentShader)}dispose(){this.shaderCache.clear(),this.materialCache.clear()}_getShaderCacheForMaterial(e){let t=this.materialCache,n=t.get(e);return n===void 0&&(n=new Set,t.set(e,n)),n}_getShaderStage(e){let t=this.shaderCache,n=t.get(e);return n===void 0&&(n=new gl(e),t.set(e,n)),n}},gl=class{constructor(e){this.id=t2++,this.code=e,this.usedTimes=0}};function n2(i){return i===Qn||i===Fs||i===Os}function i2(i,e,t,n,s,r){let a=new Bi,o=new ml,l=new Set,c=[],h=new Map,g=n.logarithmicDepthBuffer,d={MeshDepthMaterial:"depth",MeshDistanceMaterial:"distance",MeshNormalMaterial:"normal",MeshBasicMaterial:"basic",MeshLambertMaterial:"lambert",MeshPhongMaterial:"phong",MeshToonMaterial:"toon",MeshStandardMaterial:"physical",MeshPhysicalMaterial:"physical",MeshMatcapMaterial:"matcap",LineBasicMaterial:"basic",LineDashedMaterial:"dashed",PointsMaterial:"points",ShadowMaterial:"shadow",SpriteMaterial:"sprite"};function m(f){return l.add(f),f===0?"uv":`uv${f}`}function _(f,v,N,I,D,z){let q=I.fog,P=D.geometry,W=f.isMeshStandardMaterial||f.isMeshLambertMaterial||f.isMeshPhongMaterial?I.environment:null,$=f.isMeshStandardMaterial||f.isMeshLambertMaterial&&!f.envMap||f.isMeshPhongMaterial&&!f.envMap,G=e.get(f.envMap||W,$),te=d[f.type],H=n.precision;f.precision!==null&&(H=n.getMaxPrecision(f.precision),H!==f.precision&&Te("WebGLProgram.getParameters:",f.precision,"not supported, using",H,"instead."));let j=P.morphAttributes.position||P.morphAttributes.normal||P.morphAttributes.color,Q=j!==void 0?j.length:0,Se=0;P.morphAttributes.position!==void 0&&(Se=1),P.morphAttributes.normal!==void 0&&(Se=2),P.morphAttributes.color!==void 0&&(Se=3);let De,Z,pe,xe;if(te){let de=vn[te];De=de.vertexShader,Z=de.fragmentShader}else{De=f.vertexShader,Z=f.fragmentShader;let de=o.getVertexShaderStage(f),je=o.getFragmentShaderStage(f);o.update(f,de,je),pe=de.id,xe=je.id}let Ae=i.getRenderTarget(),me=i.state.buffers.depth.getReversed(),Ue=D.isInstancedMesh===!0,ht=D.isBatchedMesh===!0,Ce=!!f.map,Ke=!!f.matcap,Qe=!!G,Ge=Qe&&G.isPMREMTexture===!0,bt=!!f.aoMap,ft=!!f.lightMap,Bt=!!f.bumpMap&&f.wireframe===!1,ot=!!f.normalMap,pn=!!f.displacementMap,xt=!!f.emissiveMap,Jt=!!f.metalnessMap,$t=!!f.roughnessMap,Kt=f.anisotropy>0,L=f.clearcoat>0,jt=f.diffuseRoughness>0,st=f.dispersion>0,rt=f.retroreflectivity>0,ue=f.iridescence>0,pt=f.sheen>0,we=f.transmission>0,Le=Kt&&!!f.anisotropyMap,b=L&&!!f.clearcoatMap,x=L&&!!f.clearcoatNormalMap,O=L&&!!f.clearcoatRoughnessMap,ee=jt&&!!f.diffuseRoughnessMap,K=ue&&!!f.iridescenceMap,se=ue&&!!f.iridescenceThicknessMap,ce=pt&&!!f.sheenColorMap,X=pt&&!!f.sheenRoughnessMap,Y=!!f.specularMap,ae=!!f.specularColorMap,R=!!f.specularIntensityMap,J=we&&!!f.transmissionMap,V=we&&!!f.thicknessMap,oe=!!f.gradientMap,ie=!!f.alphaMap,re=f.alphaTest>0,be=!!f.alphaHash,Oe=!!f.extensions,ne=xn;f.toneMapped&&(Ae===null||Ae.isXRRenderTarget===!0)&&(ne=i.toneMapping);let Ee=Ge?G.isCompressedCubeTexture?G.image[0].mipmaps:G.mipmaps:null,Fe={shaderID:te,shaderType:f.type,shaderName:f.name,vertexShader:De,fragmentShader:Z,defines:f.defines,customVertexShaderID:pe,customFragmentShaderID:xe,isRawShaderMaterial:f.isRawShaderMaterial===!0,glslVersion:f.glslVersion,precision:H,batching:ht,batchingColor:ht&&D._colorsTexture!==null,instancing:Ue,instancingColor:Ue&&D.instanceColor!==null,instancingMorph:Ue&&D.morphTexture!==null,outputColorSpace:Ae===null?i.outputColorSpace:Ae.isXRRenderTarget===!0?Ae.texture.colorSpace:We.workingColorSpace,alphaToCoverage:!!f.alphaToCoverage,map:Ce,matcap:Ke,envMap:Qe,envMapMode:Qe&&G.mapping,envMapPMREM:Ge,envMapMaxLod:Ge?Ee.length-1:null,envMapSize:Ge?Ee[0].width:null,aoMap:bt,lightMap:ft,bumpMap:Bt,normalMap:ot,displacementMap:pn,emissiveMap:xt,normalMapObjectSpace:ot&&f.normalMapType===kc,normalMapTangentSpace:ot&&f.normalMapType===Na,packedNormalMap:ot&&f.normalMapType===Na&&n2(f.normalMap.format),metalnessMap:Jt,roughnessMap:$t,anisotropy:Kt,anisotropyMap:Le,clearcoat:L,clearcoatMap:b,clearcoatNormalMap:x,clearcoatRoughnessMap:O,diffuseRoughness:jt,diffuseRoughnessMap:ee,dispersion:st,retroreflection:rt,iridescence:ue,iridescenceMap:K,iridescenceThicknessMap:se,sheen:pt,sheenColorMap:ce,sheenRoughnessMap:X,specularMap:Y,specularColorMap:ae,specularIntensityMap:R,transmission:we,transmissionMap:J,thicknessMap:V,gradientMap:oe,opaque:f.transparent===!1&&f.blending===Xi&&f.alphaToCoverage===!1,alphaMap:ie,alphaTest:re,alphaHash:be,combine:f.combine,mapUv:Ce&&m(f.map.channel),aoMapUv:bt&&m(f.aoMap.channel),lightMapUv:ft&&m(f.lightMap.channel),bumpMapUv:Bt&&m(f.bumpMap.channel),normalMapUv:ot&&m(f.normalMap.channel),displacementMapUv:pn&&m(f.displacementMap.channel),emissiveMapUv:xt&&m(f.emissiveMap.channel),metalnessMapUv:Jt&&m(f.metalnessMap.channel),roughnessMapUv:$t&&m(f.roughnessMap.channel),anisotropyMapUv:Le&&m(f.anisotropyMap.channel),clearcoatMapUv:b&&m(f.clearcoatMap.channel),clearcoatNormalMapUv:x&&m(f.clearcoatNormalMap.channel),clearcoatRoughnessMapUv:O&&m(f.clearcoatRoughnessMap.channel),diffuseRoughnessMapUv:ee&&m(f.diffuseRoughnessMap.channel),iridescenceMapUv:K&&m(f.iridescenceMap.channel),iridescenceThicknessMapUv:se&&m(f.iridescenceThicknessMap.channel),sheenColorMapUv:ce&&m(f.sheenColorMap.channel),sheenRoughnessMapUv:X&&m(f.sheenRoughnessMap.channel),specularMapUv:Y&&m(f.specularMap.channel),specularColorMapUv:ae&&m(f.specularColorMap.channel),specularIntensityMapUv:R&&m(f.specularIntensityMap.channel),transmissionMapUv:J&&m(f.transmissionMap.channel),thicknessMapUv:V&&m(f.thicknessMap.channel),alphaMapUv:ie&&m(f.alphaMap.channel),vertexTangents:!!P.attributes.tangent&&(ot||Kt),vertexNormals:!!P.attributes.normal,vertexColors:f.vertexColors,vertexAlphas:f.vertexColors===!0&&!!P.attributes.color&&P.attributes.color.itemSize===4,pointsUvs:D.isPoints===!0&&!!P.attributes.uv&&(Ce||ie),fog:!!q,useFog:f.fog===!0,fogExp2:!!q&&q.isFogExp2,flatShading:f.wireframe===!1&&(f.flatShading===!0||P.attributes.normal===void 0&&ot===!1&&(f.isMeshLambertMaterial||f.isMeshPhongMaterial||f.isMeshStandardMaterial||f.isMeshPhysicalMaterial)),sizeAttenuation:f.sizeAttenuation===!0,logarithmicDepthBuffer:g,reversedDepthBuffer:me,skinning:D.isSkinnedMesh===!0,hasPositionAttribute:P.attributes.position!==void 0,morphTargets:P.morphAttributes.position!==void 0,morphNormals:P.morphAttributes.normal!==void 0,morphColors:P.morphAttributes.color!==void 0,morphTargetsCount:Q,morphTextureStride:Se,numSunLights:v.sun.length,numDirLights:v.directional.length,numPointLights:v.point.length,numSpotLights:v.spot.length,numSpotLightMaps:v.spotLightMap.length,numRectAreaLights:v.rectArea.length,numHemiLights:v.hemi.length,numSunLightShadows:v.sunShadowMap.length,numDirLightShadows:v.directionalShadowMap.length,numPointLightShadows:v.pointShadowMap.length,numSpotLightShadows:v.spotShadowMap.length,numSpotLightShadowsWithMaps:v.numSpotLightShadowsWithMaps,numLightProbes:v.numLightProbes,numLightProbeGrids:z.filter(de=>de.texture!==null).length,numClippingPlanes:r.numPlanes,numClipIntersection:r.numIntersection,dithering:f.dithering,shadowMapEnabled:i.shadowMap.enabled&&N.length>0,shadowMapType:i.shadowMap.type,toneMapping:ne,decodeVideoTexture:Ce&&f.map.isVideoTexture===!0&&We.getTransfer(f.map.colorSpace)===$e,decodeVideoTextureEmissive:xt&&f.emissiveMap.isVideoTexture===!0&&We.getTransfer(f.emissiveMap.colorSpace)===$e,premultipliedAlpha:f.premultipliedAlpha,doubleSided:f.side===nn,flipSided:f.side===Tt,useDepthPacking:f.depthPacking>=0,depthPacking:f.depthPacking||0,index0AttributeName:f.index0AttributeName,extensionClipCullDistance:Oe&&f.extensions.clipCullDistance===!0&&t.has("WEBGL_clip_cull_distance"),extensionMultiDraw:(Oe&&f.extensions.multiDraw===!0||ht)&&t.has("WEBGL_multi_draw"),rendererExtensionParallelShaderCompile:t.has("KHR_parallel_shader_compile"),customProgramCacheKey:f.customProgramCacheKey()};return Fe.vertexUv1s=l.has(1),Fe.vertexUv2s=l.has(2),Fe.vertexUv3s=l.has(3),l.clear(),Fe}function S(f){let v=[];if(f.shaderID?v.push(f.shaderID):(v.push(f.customVertexShaderID),v.push(f.customFragmentShaderID)),f.defines!==void 0)for(let N in f.defines)v.push(N),v.push(f.defines[N]);return f.isRawShaderMaterial===!1&&(p(v,f),u(v,f),v.push(i.outputColorSpace)),v.push(f.customProgramCacheKey),v.join()}function p(f,v){f.push(v.precision),f.push(v.outputColorSpace),f.push(v.envMapMode),f.push(v.envMapPMREM),f.push(v.envMapMaxLod),f.push(v.envMapSize),f.push(v.mapUv),f.push(v.alphaMapUv),f.push(v.lightMapUv),f.push(v.aoMapUv),f.push(v.bumpMapUv),f.push(v.normalMapUv),f.push(v.displacementMapUv),f.push(v.emissiveMapUv),f.push(v.metalnessMapUv),f.push(v.roughnessMapUv),f.push(v.anisotropyMapUv),f.push(v.clearcoatMapUv),f.push(v.clearcoatNormalMapUv),f.push(v.clearcoatRoughnessMapUv),f.push(v.diffuseRoughnessMapUv),f.push(v.iridescenceMapUv),f.push(v.iridescenceThicknessMapUv),f.push(v.sheenColorMapUv),f.push(v.sheenRoughnessMapUv),f.push(v.specularMapUv),f.push(v.specularColorMapUv),f.push(v.specularIntensityMapUv),f.push(v.transmissionMapUv),f.push(v.thicknessMapUv),f.push(v.combine),f.push(v.fogExp2),f.push(v.sizeAttenuation),f.push(v.morphTargetsCount),f.push(v.numSunLights),f.push(v.numDirLights),f.push(v.numPointLights),f.push(v.numSpotLights),f.push(v.numSpotLightMaps),f.push(v.numHemiLights),f.push(v.numRectAreaLights),f.push(v.numSunLightShadows),f.push(v.numDirLightShadows),f.push(v.numPointLightShadows),f.push(v.numSpotLightShadows),f.push(v.numSpotLightShadowsWithMaps),f.push(v.numLightProbes),f.push(v.numLightProbeGrids),f.push(v.shadowMapType),f.push(v.toneMapping),f.push(v.numClippingPlanes),f.push(v.numClipIntersection),f.push(v.depthPacking)}function u(f,v){a.disableAll(),v.instancing&&a.enable(0),v.instancingColor&&a.enable(1),v.instancingMorph&&a.enable(2),v.matcap&&a.enable(3),v.envMap&&a.enable(4),v.normalMapObjectSpace&&a.enable(5),v.normalMapTangentSpace&&a.enable(6),v.clearcoat&&a.enable(7),v.iridescence&&a.enable(8),v.alphaTest&&a.enable(9),v.vertexColors&&a.enable(10),v.vertexAlphas&&a.enable(11),v.vertexUv1s&&a.enable(12),v.vertexUv2s&&a.enable(13),v.vertexUv3s&&a.enable(14),v.vertexTangents&&a.enable(15),v.anisotropy&&a.enable(16),v.alphaHash&&a.enable(17),v.batching&&a.enable(18),v.dispersion&&a.enable(19),v.retroreflection&&a.enable(24),v.diffuseRoughness&&a.enable(25),v.batchingColor&&a.enable(20),v.gradientMap&&a.enable(21),v.packedNormalMap&&a.enable(22),v.vertexNormals&&a.enable(23),f.push(a.mask),a.disableAll(),v.fog&&a.enable(0),v.useFog&&a.enable(1),v.flatShading&&a.enable(2),v.logarithmicDepthBuffer&&a.enable(3),v.reversedDepthBuffer&&a.enable(4),v.skinning&&a.enable(5),v.morphTargets&&a.enable(6),v.morphNormals&&a.enable(7),v.morphColors&&a.enable(8),v.premultipliedAlpha&&a.enable(9),v.shadowMapEnabled&&a.enable(10),v.doubleSided&&a.enable(11),v.flipSided&&a.enable(12),v.useDepthPacking&&a.enable(13),v.dithering&&a.enable(14),v.transmission&&a.enable(15),v.sheen&&a.enable(16),v.opaque&&a.enable(17),v.pointsUvs&&a.enable(18),v.decodeVideoTexture&&a.enable(19),v.decodeVideoTextureEmissive&&a.enable(20),v.alphaToCoverage&&a.enable(21),v.numLightProbeGrids>0&&a.enable(22),v.hasPositionAttribute&&a.enable(23),f.push(a.mask)}function M(f){let v=d[f.type],N;if(v){let I=vn[v];N=th.clone(I.uniforms)}else N=f.uniforms;return N}function w(f,v){let N=h.get(v);return N!==void 0?++N.usedTimes:(N=new e2(i,v,f,s),c.push(N),h.set(v,N)),N}function E(f){if(--f.usedTimes===0){let v=c.indexOf(f);c[v]=c[c.length-1],c.pop(),h.delete(f.cacheKey),f.destroy()}}function A(f){o.remove(f)}function T(){o.dispose()}return{getParameters:_,getProgramCacheKey:S,getUniforms:M,acquireProgram:w,releaseProgram:E,releaseShaderCache:A,programs:c,dispose:T}}function s2(){let i=new WeakMap;function e(a){return i.has(a)}function t(a){let o=i.get(a);return o===void 0&&(o={},i.set(a,o)),o}function n(a){i.delete(a)}function s(a,o,l){i.get(a)[o]=l}function r(){i=new WeakMap}return{has:e,get:t,remove:n,update:s,dispose:r}}function r2(i,e){return i.groupOrder!==e.groupOrder?i.groupOrder-e.groupOrder:i.renderOrder!==e.renderOrder?i.renderOrder-e.renderOrder:i.material.id!==e.material.id?i.material.id-e.material.id:i.materialVariant!==e.materialVariant?i.materialVariant-e.materialVariant:i.z!==e.z?i.z-e.z:i.id-e.id}function Sh(i,e){return i.groupOrder!==e.groupOrder?i.groupOrder-e.groupOrder:i.renderOrder!==e.renderOrder?i.renderOrder-e.renderOrder:i.z!==e.z?e.z-i.z:i.id-e.id}function Mh(){let i=[],e=0,t=[],n=[],s=[];function r(){e=0,t.length=0,n.length=0,s.length=0}function a(d){let m=0;return d.isInstancedMesh&&(m+=2),d.isSkinnedMesh&&(m+=1),m}function o(d,m,_,S,p,u){let M=i[e];return M===void 0?(M={id:d.id,object:d,geometry:m,material:_,materialVariant:a(d),groupOrder:S,renderOrder:d.renderOrder,z:p,group:u},i[e]=M):(M.id=d.id,M.object=d,M.geometry=m,M.material=_,M.materialVariant=a(d),M.groupOrder=S,M.renderOrder=d.renderOrder,M.z=p,M.group=u),e++,M}function l(d,m,_,S,p,u,M){M.reversedDepth===!0&&(p=-p);let w=o(d,m,_,S,p,u);_.transmission>0?n.push(w):_.transparent===!0?s.push(w):t.push(w)}function c(d,m,_,S,p,u){let M=o(d,m,_,S,p,u);_.transmission>0?n.unshift(M):_.transparent===!0?s.unshift(M):t.unshift(M)}function h(d,m){t.length>1&&t.sort(d||r2),n.length>1&&n.sort(m||Sh),s.length>1&&s.sort(m||Sh)}function g(){for(let d=e,m=i.length;d<m;d++){let _=i[d];if(_.id===null)break;_.id=null,_.object=null,_.geometry=null,_.material=null,_.group=null}}return{opaque:t,transmissive:n,transparent:s,init:r,push:l,unshift:c,finish:g,sort:h}}function a2(){let i=new WeakMap;function e(n,s){let r=i.get(n),a;return r===void 0?(a=new Mh,i.set(n,[a])):s>=r.length?(a=new Mh,r.push(a)):a=r[s],a}function t(){i=new WeakMap}return{get:e,dispose:t}}function o2(){let i={};return{get:function(e){if(i[e.id]!==void 0)return i[e.id];let t;switch(e.type){case"SunLight":case"DirectionalLight":t={direction:new U,color:new Be};break;case"SpotLight":t={position:new U,direction:new U,color:new Be,distance:0,coneCos:0,penumbraCos:0,decay:0};break;case"PointLight":t={position:new U,color:new Be,distance:0,decay:0};break;case"HemisphereLight":t={direction:new U,skyColor:new Be,groundColor:new Be};break;case"RectAreaLight":t={color:new Be,position:new U,halfWidth:new U,halfHeight:new U};break}return i[e.id]=t,t}}}function l2(){let i={};return{get:function(e){if(i[e.id]!==void 0)return i[e.id];let t;switch(e.type){case"SunLight":case"DirectionalLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Re};break;case"SpotLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Re};break;case"PointLight":t={shadowIntensity:1,shadowBias:0,shadowNormalBias:0,shadowRadius:1,shadowMapSize:new Re,shadowCameraNear:1,shadowCameraFar:1e3};break}return i[e.id]=t,t}}}var c2=0;function h2(i,e){return(e.castShadow?2:0)-(i.castShadow?2:0)+(e.map?1:0)-(i.map?1:0)}function u2(i){let e=new o2,t=l2(),n={version:0,hash:{sunLength:-1,directionalLength:-1,pointLength:-1,spotLength:-1,rectAreaLength:-1,hemiLength:-1,numSunShadows:-1,numDirectionalShadows:-1,numPointShadows:-1,numSpotShadows:-1,numSpotMaps:-1,numLightProbes:-1},ambient:[0,0,0],probe:[],sun:[],sunShadow:[],sunShadowMap:[],sunShadowMatrix:[],sunShadowCascade:[],directional:[],directionalShadow:[],directionalShadowMap:[],directionalShadowMatrix:[],spot:[],spotLightMap:[],spotShadow:[],spotShadowMap:[],spotLightMatrix:[],rectArea:[],rectAreaLTC1:null,rectAreaLTC2:null,point:[],pointShadow:[],pointShadowMap:[],pointShadowMatrix:[],hemi:[],numSpotLightShadowsWithMaps:0,numLightProbes:0};for(let c=0;c<9;c++)n.probe.push(new U);let s=new U,r=new nt,a=new nt;function o(c){let h=0,g=0,d=0;for(let z=0;z<9;z++)n.probe[z].set(0,0,0);let m=0,_=0,S=0,p=0,u=0,M=0,w=0,E=0,A=0,T=0,f=0,v=0,N=0,I=0;c.sort(h2);for(let z=0,q=c.length;z<q;z++){let P=c[z],W=P.color,$=P.intensity,G=P.distance,te=null;if(P.shadow&&P.shadow.map&&(P.shadow.map.texture.format===Qn?te=P.shadow.map.texture:te=P.shadow.map.depthTexture||P.shadow.map.texture),P.isAmbientLight)h+=W.r*$,g+=W.g*$,d+=W.b*$;else if(P.isLightProbe){for(let H=0;H<9;H++)n.probe[H].addScaledVector(P.sh.coefficients[H],$);I++}else if(P.isSunLight){let H=e.get(P);if(H.color.copy(P.color).multiplyScalar(P.intensity),P.castShadow){let j=P.shadow,Q=t.get(P);Q.shadowIntensity=j.intensity,Q.shadowBias=j.bias,Q.shadowNormalBias=j.normalBias,Q.shadowRadius=j.radius,Q.shadowMapSize.copy(j.mapSize).multiply(j.getFrameExtents()),n.sunShadow[_]=Q,n.sunShadowMap[_]=te;let Se=j.getViewportCount();for(let De=0;De<Se;De++)n.sunShadowMatrix[S+De]=j.getMatrix(De),n.sunShadowCascade[S+De]=j._cascadeData[De];S+=Se,_++}n.sun[m]=H,m++}else if(P.isDirectionalLight){let H=e.get(P);if(H.color.copy(P.color).multiplyScalar(P.intensity),P.castShadow){let j=P.shadow,Q=t.get(P);Q.shadowIntensity=j.intensity,Q.shadowBias=j.bias,Q.shadowNormalBias=j.normalBias,Q.shadowRadius=j.radius,Q.shadowMapSize=j.mapSize,n.directionalShadow[p]=Q,n.directionalShadowMap[p]=te,n.directionalShadowMatrix[p]=P.shadow.matrix,A++}n.directional[p]=H,p++}else if(P.isSpotLight){let H=e.get(P);H.position.setFromMatrixPosition(P.matrixWorld),H.color.copy(W).multiplyScalar($),H.distance=G,H.coneCos=Math.cos(P.angle),H.penumbraCos=Math.cos(P.angle*(1-P.penumbra)),H.decay=P.decay,n.spot[M]=H;let j=P.shadow;if(P.map&&(n.spotLightMap[v]=P.map,v++,j.updateMatrices(P),P.castShadow&&N++),n.spotLightMatrix[M]=j.matrix,P.castShadow){let Q=t.get(P);Q.shadowIntensity=j.intensity,Q.shadowBias=j.bias,Q.shadowNormalBias=j.normalBias,Q.shadowRadius=j.radius,Q.shadowMapSize=j.mapSize,n.spotShadow[M]=Q,n.spotShadowMap[M]=te,f++}M++}else if(P.isRectAreaLight){let H=e.get(P);H.color.copy(W).multiplyScalar($),H.halfWidth.set(P.width*.5,0,0),H.halfHeight.set(0,P.height*.5,0),n.rectArea[w]=H,w++}else if(P.isPointLight){let H=e.get(P);if(H.color.copy(P.color).multiplyScalar(P.intensity),H.distance=P.distance,H.decay=P.decay,P.castShadow){let j=P.shadow,Q=t.get(P);Q.shadowIntensity=j.intensity,Q.shadowBias=j.bias,Q.shadowNormalBias=j.normalBias,Q.shadowRadius=j.radius,Q.shadowMapSize=j.mapSize,Q.shadowCameraNear=j.camera.near,Q.shadowCameraFar=j.camera.far,n.pointShadow[u]=Q,n.pointShadowMap[u]=te,n.pointShadowMatrix[u]=P.shadow.matrix,T++}n.point[u]=H,u++}else if(P.isHemisphereLight){let H=e.get(P);H.skyColor.copy(P.color).multiplyScalar($),H.groundColor.copy(P.groundColor).multiplyScalar($),n.hemi[E]=H,E++}}w>0&&(i.has("OES_texture_float_linear")===!0?(n.rectAreaLTC1=fe.LTC_FLOAT_1,n.rectAreaLTC2=fe.LTC_FLOAT_2):(n.rectAreaLTC1=fe.LTC_HALF_1,n.rectAreaLTC2=fe.LTC_HALF_2)),n.ambient[0]=h,n.ambient[1]=g,n.ambient[2]=d;let D=n.hash;(D.sunLength!==m||D.directionalLength!==p||D.pointLength!==u||D.spotLength!==M||D.rectAreaLength!==w||D.hemiLength!==E||D.numSunShadows!==_||D.numDirectionalShadows!==A||D.numPointShadows!==T||D.numSpotShadows!==f||D.numSpotMaps!==v||D.numLightProbes!==I)&&(n.sun.length=m,n.directional.length=p,n.spot.length=M,n.rectArea.length=w,n.point.length=u,n.hemi.length=E,n.sunShadow.length=_,n.sunShadowMap.length=_,n.sunShadowMatrix.length=S,n.sunShadowCascade.length=S,n.directionalShadow.length=A,n.directionalShadowMap.length=A,n.directionalShadowMatrix.length=A,n.pointShadow.length=T,n.pointShadowMap.length=T,n.pointShadowMatrix.length=T,n.spotShadow.length=f,n.spotShadowMap.length=f,n.spotLightMatrix.length=f+v-N,n.spotLightMap.length=v,n.numSpotLightShadowsWithMaps=N,n.numLightProbes=I,D.sunLength=m,D.directionalLength=p,D.pointLength=u,D.spotLength=M,D.rectAreaLength=w,D.hemiLength=E,D.numSunShadows=_,D.numDirectionalShadows=A,D.numPointShadows=T,D.numSpotShadows=f,D.numSpotMaps=v,D.numLightProbes=I,n.version=c2++)}function l(c,h){let g=0,d=0,m=0,_=0,S=0,p=0,u=h.matrixWorldInverse;for(let M=0,w=c.length;M<w;M++){let E=c[M];if(E.isSunLight){let A=n.sun[g];A.direction.setFromMatrixPosition(E.matrixWorld),A.direction.transformDirection(u),g++}else if(E.isDirectionalLight){let A=n.directional[d];A.direction.setFromMatrixPosition(E.matrixWorld),s.setFromMatrixPosition(E.target.matrixWorld),A.direction.sub(s),A.direction.transformDirection(u),d++}else if(E.isSpotLight){let A=n.spot[_];A.position.setFromMatrixPosition(E.matrixWorld),A.position.applyMatrix4(u),A.direction.setFromMatrixPosition(E.matrixWorld),s.setFromMatrixPosition(E.target.matrixWorld),A.direction.sub(s),A.direction.transformDirection(u),_++}else if(E.isRectAreaLight){let A=n.rectArea[S];A.position.setFromMatrixPosition(E.matrixWorld),A.position.applyMatrix4(u),a.identity(),r.copy(E.matrixWorld),r.premultiply(u),a.extractRotation(r),A.halfWidth.set(E.width*.5,0,0),A.halfHeight.set(0,E.height*.5,0),A.halfWidth.applyMatrix4(a),A.halfHeight.applyMatrix4(a),S++}else if(E.isPointLight){let A=n.point[m];A.position.setFromMatrixPosition(E.matrixWorld),A.position.applyMatrix4(u),m++}else if(E.isHemisphereLight){let A=n.hemi[p];A.direction.setFromMatrixPosition(E.matrixWorld),A.direction.transformDirection(u),p++}}}return{setup:o,setupView:l,state:n}}function bh(i){let e=new u2(i),t=[],n=[],s=[];function r(g){h.camera=g,t.length=0,n.length=0,s.length=0}function a(g){g.isLightProbeGrid?s.push(g):t.push(g)}function o(g){n.push(g)}function l(){e.setup(t),s.sort((g,d)=>g.priority-d.priority||g.id-d.id)}function c(g){e.setupView(t,g)}let h={lightsArray:t,shadowsArray:n,lightProbeGridArray:s,camera:null,lights:e,transmissionRenderTarget:{},textureUnits:0};return{init:r,state:h,setupLights:l,setupLightsView:c,pushLight:a,pushShadow:o}}function d2(i){let e=new WeakMap;function t(s,r=0){let a=e.get(s),o;return a===void 0?(o=new bh(i),e.set(s,[o])):r>=a.length?(o=new bh(i),a.push(o)):o=a[r],o}function n(){e=new WeakMap}return{get:t,dispose:n}}var f2=`void main() {
	gl_Position = vec4( position, 1.0 );
}`,p2=`uniform sampler2D shadow_pass;
uniform vec2 resolution;
uniform float radius;
void main() {
	const float samples = float( VSM_SAMPLES );
	float mean = 0.0;
	float squared_mean = 0.0;
	float uvStride = samples <= 1.0 ? 0.0 : 2.0 / ( samples - 1.0 );
	float uvStart = samples <= 1.0 ? 0.0 : - 1.0;
	for ( float i = 0.0; i < samples; i ++ ) {
		float uvOffset = uvStart + i * uvStride;
		#ifdef HORIZONTAL_PASS
			vec2 distribution = texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( uvOffset, 0.0 ) * radius ) / resolution ).rg;
			mean += distribution.x;
			squared_mean += distribution.y * distribution.y + distribution.x * distribution.x;
		#else
			float depth = texture2D( shadow_pass, ( gl_FragCoord.xy + vec2( 0.0, uvOffset ) * radius ) / resolution ).r;
			mean += depth;
			squared_mean += depth * depth;
		#endif
	}
	mean = mean / samples;
	squared_mean = squared_mean / samples;
	float std_dev = sqrt( max( 0.0, squared_mean - mean * mean ) );
	gl_FragColor = vec4( mean, std_dev, 0.0, 1.0 );
}`,m2=[new U(1,0,0),new U(-1,0,0),new U(0,1,0),new U(0,-1,0),new U(0,0,1),new U(0,0,-1)],g2=[new U(0,-1,0),new U(0,-1,0),new U(0,0,1),new U(0,0,-1),new U(0,-1,0),new U(0,-1,0)],Eh=new nt,Bs=new U,hl=new U;function _2(i,e,t){let n=new qn,s=new Re,r=new Re,a=new at,o=new Dr,l=new Nr,c={},h=t.maxTextureSize,g={[jn]:Tt,[Tt]:jn,[nn]:nn},d=new tn({defines:{VSM_SAMPLES:8},uniforms:{shadow_pass:{value:null},resolution:{value:new Re},radius:{value:4}},vertexShader:f2,fragmentShader:p2}),m=d.clone();m.defines.HORIZONTAL_PASS=1;let _=new kt;_.setAttribute("position",new _n(new Float32Array([-1,-1,.5,3,-1,.5,-1,3,.5]),3));let S=new Ot(_,d),p=this;this.enabled=!1,this.autoUpdate=!0,this.needsUpdate=!1,this.type=Ps;let u=this.type;this.render=function(T,f,v){if(p.enabled===!1||p.autoUpdate===!1&&p.needsUpdate===!1||T.length===0)return;this.type===_c&&(Te("WebGLShadowMap: PCFSoftShadowMap has been removed. Using PCFShadowMap instead."),this.type=Ps);let N=i.getRenderTarget(),I=i.getActiveCubeFace(),D=i.getActiveMipmapLevel(),z=i.state;z.setBlending(ui),z.buffers.depth.getReversed()===!0?z.buffers.color.setClear(0,0,0,0):z.buffers.color.setClear(1,1,1,1),z.buffers.depth.setTest(!0),z.setScissorTest(!1);let q=u!==this.type;q&&f.traverse(function(P){P.material&&(Array.isArray(P.material)?P.material.forEach(W=>W.needsUpdate=!0):P.material.needsUpdate=!0)});for(let P=0,W=T.length;P<W;P++){let $=T[P],G=$.shadow;if(G===void 0){Te("WebGLShadowMap:",$,"has no shadow.");continue}if(G.autoUpdate===!1&&G.needsUpdate===!1)continue;s.copy(G.mapSize);let te=G.getFrameExtents();s.multiply(te),r.copy(G.mapSize),(s.x>h||s.y>h)&&(s.x>h&&(r.x=Math.floor(h/te.x),s.x=r.x*te.x,G.mapSize.x=r.x),s.y>h&&(r.y=Math.floor(h/te.y),s.y=r.y*te.y,G.mapSize.y=r.y));let H=i.state.buffers.depth.getReversed();if(G.camera._reversedDepth=H,G.map===null||q===!0){if(G.map!==null&&(G.map.depthTexture!==null&&(G.map.depthTexture.dispose(),G.map.depthTexture=null),G.map.dispose()),this.type===Wi){if($.isPointLight){Te("WebGLShadowMap: VSM shadow maps are not supported for PointLights. Use PCF or BasicShadowMap instead.");continue}G.map=new Yt(s.x,s.y,{format:Qn,type:un,minFilter:Ft,magFilter:Ft,generateMipmaps:!1}),G.map.texture.name=$.name+".shadowMap",G.map.depthTexture=new Ln(s.x,s.y,hn),G.map.depthTexture.name=$.name+".shadowMapDepth",G.map.depthTexture.format=Cn,G.map.depthTexture.compareFunction=null,G.map.depthTexture.minFilter=Mt,G.map.depthTexture.magFilter=Mt}else $.isPointLight?(G.map=new ks(s.x),G.map.depthTexture=new gs(s.x,cn)):(G.map=new Yt(s.x,s.y),G.map.depthTexture=new Ln(s.x,s.y,cn)),G.map.depthTexture.name=$.name+".shadowMap",G.map.depthTexture.format=Cn,this.type===Ps?(G.map.depthTexture.compareFunction=H?qo:Xo,G.map.depthTexture.minFilter=Ft,G.map.depthTexture.magFilter=Ft):(G.map.depthTexture.compareFunction=null,G.map.depthTexture.minFilter=Mt,G.map.depthTexture.magFilter=Mt);G.camera.updateProjectionMatrix()}G.map.isWebGLCubeRenderTarget!==!0&&(G.map.width!==s.x||G.map.height!==s.y)&&G.map.setSize(s.x,s.y);let j=G.map.isWebGLCubeRenderTarget?6:G.getViewportCount();$.isPointLight!==!0&&G.updateMatrices($,v);let Q=(G.camera.layers.mask&4294967294)!==0?G.camera.layers:v.layers;for(let Se=0;Se<j;Se++){let De=G.getCamera(Se);if($.isPointLight){let Z=G.camera,pe=G.matrix,xe=$.distance||Z.far;xe!==Z.far&&(Z.far=xe,Z.updateProjectionMatrix()),Bs.setFromMatrixPosition($.matrixWorld),Z.position.copy(Bs),hl.copy(Z.position),hl.add(m2[Se]),Z.up.copy(g2[Se]),Z.lookAt(hl),Z.updateMatrixWorld(),pe.makeTranslation(-Bs.x,-Bs.y,-Bs.z),Eh.multiplyMatrices(Z.projectionMatrix,Z.matrixWorldInverse),G._frustum.setFromProjectionMatrix(Eh,Z.coordinateSystem,Z.reversedDepth)}if(G.map.isWebGLCubeRenderTarget)i.setRenderTarget(G.map,Se),i.clear();else{Se===0&&(i.setRenderTarget(G.map),i.clear());let Z=G.getViewport(Se);a.set(r.x*Z.x,r.y*Z.y,r.x*Z.z,r.y*Z.w),z.viewport(a)}n=G.getFrustum(Se),E(f,v,De,$,Q,this.type)}G.isPointLightShadow!==!0&&this.type===Wi&&M(G,v),G.needsUpdate=!1}u=this.type,p.needsUpdate=!1,i.setRenderTarget(N,I,D)};function M(T,f){let v=e.update(S);d.defines.VSM_SAMPLES!==T.blurSamples&&(d.defines.VSM_SAMPLES=T.blurSamples,m.defines.VSM_SAMPLES=T.blurSamples,d.needsUpdate=!0,m.needsUpdate=!0),T.mapPass===null?T.mapPass=new Yt(s.x,s.y,{format:Qn,type:un}):(T.mapPass.width!==T.map.width||T.mapPass.height!==T.map.height)&&T.mapPass.setSize(T.map.width,T.map.height),d.uniforms.shadow_pass.value=T.map.depthTexture,d.uniforms.resolution.value.set(T.map.width,T.map.height),d.uniforms.radius.value=T.radius,i.setRenderTarget(T.mapPass),i.clear(),i.renderBufferDirect(f,null,v,d,S,null),m.uniforms.shadow_pass.value=T.mapPass.texture,m.uniforms.resolution.value.set(T.map.width,T.map.height),m.uniforms.radius.value=T.radius,i.setRenderTarget(T.map),i.clear(),i.renderBufferDirect(f,null,v,m,S,null)}function w(T,f,v,N){let I=null,D=v.isPointLight===!0?T.customDistanceMaterial:T.customDepthMaterial;if(D!==void 0)I=D;else if(I=v.isPointLight===!0?l:o,i.localClippingEnabled&&f.clipShadows===!0&&Array.isArray(f.clippingPlanes)&&f.clippingPlanes.length!==0||f.displacementMap&&f.displacementScale!==0||f.alphaMap&&f.alphaTest>0||f.map&&f.alphaTest>0||f.alphaToCoverage===!0){let z=I.uuid,q=f.uuid,P=c[z];P===void 0&&(P={},c[z]=P);let W=P[q];W===void 0&&(W=I.clone(),P[q]=W,f.addEventListener("dispose",A)),I=W}if(I.visible=f.visible,I.wireframe=f.wireframe,N===Wi?I.side=f.shadowSide!==null?f.shadowSide:f.side:I.side=f.shadowSide!==null?f.shadowSide:g[f.side],I.alphaMap=f.alphaMap,I.alphaTest=f.alphaToCoverage===!0?.5:f.alphaTest,I.map=f.map,I.clipShadows=f.clipShadows,I.clippingPlanes=f.clippingPlanes,I.clipIntersection=f.clipIntersection,I.displacementMap=f.displacementMap,I.displacementScale=f.displacementScale,I.displacementBias=f.displacementBias,I.wireframeLinewidth=f.wireframeLinewidth,I.linewidth=f.linewidth,v.isPointLight===!0&&I.isMeshDistanceMaterial===!0){let z=i.properties.get(I);z.light=v}return I}function E(T,f,v,N,I,D){if(T.visible===!1)return;if(T.layers.test(I)&&(T.isMesh||T.isLine||T.isPoints)&&(T.castShadow||T.receiveShadow&&D===Wi)&&(!T.frustumCulled||T.intersectsFrustum(n))){T.modelViewMatrix.multiplyMatrices(v.matrixWorldInverse,T.matrixWorld);let P=e.update(T),W=T.material;if(Array.isArray(W)){let $=P.groups;for(let G=0,te=$.length;G<te;G++){let H=$[G],j=W[H.materialIndex];if(j&&j.visible){let Q=w(T,j,N,D);T.onBeforeShadow(i,T,f,v,P,Q,H),i.renderBufferDirect(v,null,P,Q,T,H),T.onAfterShadow(i,T,f,v,P,Q,H)}}}else if(W.visible){let $=w(T,W,N,D);T.onBeforeShadow(i,T,f,v,P,$,null),i.renderBufferDirect(v,null,P,$,T,null),T.onAfterShadow(i,T,f,v,P,$,null)}}let q=T.children;for(let P=0,W=q.length;P<W;P++)E(q[P],f,v,N,I,D)}function A(T){T.target.removeEventListener("dispose",A);for(let v in c){let N=c[v],I=T.target.uuid;I in N&&(N[I].dispose(),delete N[I])}}}function x2(i,e){function t(){let R=!1,J=new at,V=null,oe=new at(0,0,0,0);return{setMask:function(ie){V!==ie&&!R&&(i.colorMask(ie,ie,ie,ie),V=ie)},setLocked:function(ie){R=ie},setClear:function(ie,re,be,Oe,ne){ne===!0&&(ie*=Oe,re*=Oe,be*=Oe),J.set(ie,re,be,Oe),oe.equals(J)===!1&&(i.clearColor(ie,re,be,Oe),oe.copy(J))},reset:function(){R=!1,V=null,oe.set(-1,0,0,0)}}}function n(){let R=!1,J=!1,V=null,oe=null,ie=null;return{setReversed:function(re){if(J!==re){let be=e.get("EXT_clip_control");re?be.clipControlEXT(be.LOWER_LEFT_EXT,be.ZERO_TO_ONE_EXT):be.clipControlEXT(be.LOWER_LEFT_EXT,be.NEGATIVE_ONE_TO_ONE_EXT),J=re;let Oe=ie;ie=null,this.setClear(Oe)}},getReversed:function(){return J},setTest:function(re){re?me(i.DEPTH_TEST):Ue(i.DEPTH_TEST)},setMask:function(re){V!==re&&!R&&(i.depthMask(re),V=re)},setFunc:function(re){if(J&&(re=Kc[re]),oe!==re){switch(re){case mr:i.depthFunc(i.NEVER);break;case gr:i.depthFunc(i.ALWAYS);break;case _r:i.depthFunc(i.LESS);break;case Di:i.depthFunc(i.LEQUAL);break;case xr:i.depthFunc(i.EQUAL);break;case yr:i.depthFunc(i.GEQUAL);break;case vr:i.depthFunc(i.GREATER);break;case Sr:i.depthFunc(i.NOTEQUAL);break;default:i.depthFunc(i.LEQUAL)}oe=re}},setLocked:function(re){R=re},setClear:function(re){ie!==re&&(ie=re,J&&(re=1-re),i.clearDepth(re))},reset:function(){R=!1,V=null,oe=null,ie=null,J=!1}}}function s(){let R=!1,J=null,V=null,oe=null,ie=null,re=null,be=null,Oe=null,ne=null;return{setTest:function(Ee){R||(Ee?me(i.STENCIL_TEST):Ue(i.STENCIL_TEST))},setMask:function(Ee){J!==Ee&&!R&&(i.stencilMask(Ee),J=Ee)},setFunc:function(Ee,Fe,de){(V!==Ee||oe!==Fe||ie!==de)&&(i.stencilFunc(Ee,Fe,de),V=Ee,oe=Fe,ie=de)},setOp:function(Ee,Fe,de){(re!==Ee||be!==Fe||Oe!==de)&&(i.stencilOp(Ee,Fe,de),re=Ee,be=Fe,Oe=de)},setLocked:function(Ee){R=Ee},setClear:function(Ee){ne!==Ee&&(i.clearStencil(Ee),ne=Ee)},reset:function(){R=!1,J=null,V=null,oe=null,ie=null,re=null,be=null,Oe=null,ne=null}}}let r=new t,a=new n,o=new s,l={},c=new WeakMap,h={},g={},d={},m=new WeakMap,_=[],S=null,p=!1,u=null,M=null,w=null,E=null,A=null,T=null,f=null,v=new Be(0,0,0),N=0,I=!1,D=null,z=null,q=null,P=null,W=null,$=i.getParameter(i.MAX_COMBINED_TEXTURE_IMAGE_UNITS),G=!1,te=0,H=i.getParameter(i.VERSION);H.indexOf("WebGL")!==-1?(te=parseFloat(/^WebGL (\d)/.exec(H)[1]),G=te>=1):H.indexOf("OpenGL ES")!==-1&&(te=parseFloat(/^OpenGL ES (\d)/.exec(H)[1]),G=te>=2);let j=null,Q={},Se=i.getParameter(i.SCISSOR_BOX),De=i.getParameter(i.VIEWPORT),Z=new at().fromArray(Se),pe=new at().fromArray(De);function xe(R,J,V,oe){let ie=new Uint8Array(4),re=i.createTexture();i.bindTexture(R,re),i.texParameteri(R,i.TEXTURE_MIN_FILTER,i.NEAREST),i.texParameteri(R,i.TEXTURE_MAG_FILTER,i.NEAREST);for(let be=0;be<V;be++)R===i.TEXTURE_3D||R===i.TEXTURE_2D_ARRAY?i.texImage3D(J,0,i.RGBA,1,1,oe,0,i.RGBA,i.UNSIGNED_BYTE,ie):i.texImage2D(J+be,0,i.RGBA,1,1,0,i.RGBA,i.UNSIGNED_BYTE,ie);return re}let Ae={};Ae[i.TEXTURE_2D]=xe(i.TEXTURE_2D,i.TEXTURE_2D,1),Ae[i.TEXTURE_CUBE_MAP]=xe(i.TEXTURE_CUBE_MAP,i.TEXTURE_CUBE_MAP_POSITIVE_X,6),Ae[i.TEXTURE_2D_ARRAY]=xe(i.TEXTURE_2D_ARRAY,i.TEXTURE_2D_ARRAY,1,1),Ae[i.TEXTURE_3D]=xe(i.TEXTURE_3D,i.TEXTURE_3D,1,1),r.setClear(0,0,0,1),a.setClear(1),o.setClear(0),me(i.DEPTH_TEST),a.setFunc(Di),Bt(!1),ot(Eo),me(i.CULL_FACE),bt(ui);function me(R){h[R]!==!0&&(i.enable(R),h[R]=!0)}function Ue(R){h[R]!==!1&&(i.disable(R),h[R]=!1)}function ht(R,J){return d[R]!==J?(i.bindFramebuffer(R,J),d[R]=J,R===i.DRAW_FRAMEBUFFER&&(d[i.FRAMEBUFFER]=J),R===i.FRAMEBUFFER&&(d[i.DRAW_FRAMEBUFFER]=J),!0):!1}function Ce(R,J){let V=_,oe=!1;if(R){V=m.get(J),V===void 0&&(V=[],m.set(J,V));let ie=R.textures;if(V.length!==ie.length||V[0]!==i.COLOR_ATTACHMENT0){for(let re=0,be=ie.length;re<be;re++)V[re]=i.COLOR_ATTACHMENT0+re;V.length=ie.length,oe=!0}}else V[0]!==i.BACK&&(V[0]=i.BACK,oe=!0);oe&&i.drawBuffers(V)}function Ke(R){return S!==R?(i.useProgram(R),S=R,!0):!1}let Qe={[di]:i.FUNC_ADD,[yc]:i.FUNC_SUBTRACT,[vc]:i.FUNC_REVERSE_SUBTRACT};Qe[Sc]=i.MIN,Qe[Mc]=i.MAX;let Ge={[bc]:i.ZERO,[Ec]:i.ONE,[Tc]:i.SRC_COLOR,[Ro]:i.SRC_ALPHA,[Ic]:i.SRC_ALPHA_SATURATE,[Cc]:i.DST_COLOR,[wc]:i.DST_ALPHA,[Ac]:i.ONE_MINUS_SRC_COLOR,[Co]:i.ONE_MINUS_SRC_ALPHA,[Pc]:i.ONE_MINUS_DST_COLOR,[Rc]:i.ONE_MINUS_DST_ALPHA,[Lc]:i.CONSTANT_COLOR,[Dc]:i.ONE_MINUS_CONSTANT_COLOR,[Nc]:i.CONSTANT_ALPHA,[Uc]:i.ONE_MINUS_CONSTANT_ALPHA};function bt(R,J,V,oe,ie,re,be,Oe,ne,Ee){if(R===ui){p===!0&&(Ue(i.BLEND),p=!1);return}if(p===!1&&(me(i.BLEND),p=!0),R!==xc){if(R!==u||Ee!==I){if((M!==di||A!==di)&&(i.blendEquation(i.FUNC_ADD),M=di,A=di),Ee)switch(R){case Xi:i.blendFuncSeparate(i.ONE,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case To:i.blendFunc(i.ONE,i.ONE);break;case Ao:i.blendFuncSeparate(i.ZERO,i.ONE_MINUS_SRC_COLOR,i.ZERO,i.ONE);break;case wo:i.blendFuncSeparate(i.DST_COLOR,i.ONE_MINUS_SRC_ALPHA,i.ZERO,i.ONE);break;default:Pe("WebGLState: Invalid blending: ",R);break}else switch(R){case Xi:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE_MINUS_SRC_ALPHA,i.ONE,i.ONE_MINUS_SRC_ALPHA);break;case To:i.blendFuncSeparate(i.SRC_ALPHA,i.ONE,i.ONE,i.ONE);break;case Ao:Pe("WebGLState: SubtractiveBlending requires material.premultipliedAlpha = true");break;case wo:Pe("WebGLState: MultiplyBlending requires material.premultipliedAlpha = true");break;default:Pe("WebGLState: Invalid blending: ",R);break}w=null,E=null,T=null,f=null,v.set(0,0,0),N=0,u=R,I=Ee}return}ie=ie||J,re=re||V,be=be||oe,(J!==M||ie!==A)&&(i.blendEquationSeparate(Qe[J],Qe[ie]),M=J,A=ie),(V!==w||oe!==E||re!==T||be!==f)&&(i.blendFuncSeparate(Ge[V],Ge[oe],Ge[re],Ge[be]),w=V,E=oe,T=re,f=be),(Oe.equals(v)===!1||ne!==N)&&(i.blendColor(Oe.r,Oe.g,Oe.b,ne),v.copy(Oe),N=ne),u=R,I=!1}function ft(R,J){R.side===nn?Ue(i.CULL_FACE):me(i.CULL_FACE);let V=R.side===Tt;J&&(V=!V),Bt(V),R.blending===Xi&&R.transparent===!1?bt(ui):bt(R.blending,R.blendEquation,R.blendSrc,R.blendDst,R.blendEquationAlpha,R.blendSrcAlpha,R.blendDstAlpha,R.blendColor,R.blendAlpha,R.premultipliedAlpha),a.setFunc(R.depthFunc),a.setTest(R.depthTest),a.setMask(R.depthWrite),r.setMask(R.colorWrite);let oe=R.stencilWrite;o.setTest(oe),oe&&(o.setMask(R.stencilWriteMask),o.setFunc(R.stencilFunc,R.stencilRef,R.stencilFuncMask),o.setOp(R.stencilFail,R.stencilZFail,R.stencilZPass)),xt(R.polygonOffset,R.polygonOffsetFactor,R.polygonOffsetUnits),R.alphaToCoverage===!0?me(i.SAMPLE_ALPHA_TO_COVERAGE):Ue(i.SAMPLE_ALPHA_TO_COVERAGE)}function Bt(R){D!==R&&(R?i.frontFace(i.CW):i.frontFace(i.CCW),D=R)}function ot(R){R!==mc?(me(i.CULL_FACE),R!==z&&(R===Eo?i.cullFace(i.BACK):R===gc?i.cullFace(i.FRONT):i.cullFace(i.FRONT_AND_BACK))):Ue(i.CULL_FACE),z=R}function pn(R){R!==q&&(G&&i.lineWidth(R),q=R)}function xt(R,J,V){R?(me(i.POLYGON_OFFSET_FILL),(P!==J||W!==V)&&(P=J,W=V,a.getReversed()&&(J=-J,V=-V),i.polygonOffset(J,V))):Ue(i.POLYGON_OFFSET_FILL)}function Jt(R){R?me(i.SCISSOR_TEST):Ue(i.SCISSOR_TEST)}function $t(R){R===void 0&&(R=i.TEXTURE0+$-1),j!==R&&(i.activeTexture(R),j=R)}function Kt(R,J,V){V===void 0&&(j===null?V=i.TEXTURE0+$-1:V=j);let oe=Q[V];oe===void 0&&(oe={type:void 0,texture:void 0},Q[V]=oe),(oe.type!==R||oe.texture!==J)&&(j!==V&&(i.activeTexture(V),j=V),i.bindTexture(R,J||Ae[R]),oe.type=R,oe.texture=J)}function L(){let R=Q[j];R!==void 0&&R.type!==void 0&&(i.bindTexture(R.type,null),R.type=void 0,R.texture=void 0)}function jt(){try{i.compressedTexImage2D(...arguments)}catch(R){Pe("WebGLState:",R)}}function st(){try{i.compressedTexImage3D(...arguments)}catch(R){Pe("WebGLState:",R)}}function rt(){try{i.texSubImage2D(...arguments)}catch(R){Pe("WebGLState:",R)}}function ue(){try{i.texSubImage3D(...arguments)}catch(R){Pe("WebGLState:",R)}}function pt(){try{i.compressedTexSubImage2D(...arguments)}catch(R){Pe("WebGLState:",R)}}function we(){try{i.compressedTexSubImage3D(...arguments)}catch(R){Pe("WebGLState:",R)}}function Le(){try{i.texStorage2D(...arguments)}catch(R){Pe("WebGLState:",R)}}function b(){try{i.texStorage3D(...arguments)}catch(R){Pe("WebGLState:",R)}}function x(){try{i.texImage2D(...arguments)}catch(R){Pe("WebGLState:",R)}}function O(){try{i.texImage3D(...arguments)}catch(R){Pe("WebGLState:",R)}}function ee(R){return g[R]!==void 0?g[R]:i.getParameter(R)}function K(R,J){g[R]!==J&&(i.pixelStorei(R,J),g[R]=J)}function se(R){Z.equals(R)===!1&&(i.scissor(R.x,R.y,R.z,R.w),Z.copy(R))}function ce(R){pe.equals(R)===!1&&(i.viewport(R.x,R.y,R.z,R.w),pe.copy(R))}function X(R,J){let V=c.get(J);V===void 0&&(V=new WeakMap,c.set(J,V));let oe=V.get(R);oe===void 0&&(oe=i.getUniformBlockIndex(J,R.name),i.uniformBlockBinding(J,oe,oe),V.set(R,oe))}function Y(R,J,V){let ie=c.get(J).get(R);l[ie]!==V&&(i.bindBufferBase(i.UNIFORM_BUFFER,ie,V),l[ie]=V)}function ae(){i.disable(i.BLEND),i.disable(i.CULL_FACE),i.disable(i.DEPTH_TEST),i.disable(i.POLYGON_OFFSET_FILL),i.disable(i.SCISSOR_TEST),i.disable(i.STENCIL_TEST),i.disable(i.SAMPLE_ALPHA_TO_COVERAGE),i.blendEquation(i.FUNC_ADD),i.blendFunc(i.ONE,i.ZERO),i.blendFuncSeparate(i.ONE,i.ZERO,i.ONE,i.ZERO),i.blendColor(0,0,0,0),i.colorMask(!0,!0,!0,!0),i.clearColor(0,0,0,0),i.depthMask(!0),i.depthFunc(i.LESS),a.setReversed(!1),i.clearDepth(1),i.stencilMask(4294967295),i.stencilFunc(i.ALWAYS,0,4294967295),i.stencilOp(i.KEEP,i.KEEP,i.KEEP),i.clearStencil(0),i.cullFace(i.BACK),i.frontFace(i.CCW),i.polygonOffset(0,0),i.activeTexture(i.TEXTURE0),i.bindFramebuffer(i.FRAMEBUFFER,null),i.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),i.bindFramebuffer(i.READ_FRAMEBUFFER,null),i.useProgram(null),i.lineWidth(1),i.scissor(0,0,i.canvas.width,i.canvas.height),i.viewport(0,0,i.canvas.width,i.canvas.height),i.pixelStorei(i.PACK_ALIGNMENT,4),i.pixelStorei(i.UNPACK_ALIGNMENT,4),i.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,!1),i.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,!1),i.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,i.BROWSER_DEFAULT_WEBGL),i.pixelStorei(i.PACK_ROW_LENGTH,0),i.pixelStorei(i.PACK_SKIP_PIXELS,0),i.pixelStorei(i.PACK_SKIP_ROWS,0),i.pixelStorei(i.UNPACK_ROW_LENGTH,0),i.pixelStorei(i.UNPACK_IMAGE_HEIGHT,0),i.pixelStorei(i.UNPACK_SKIP_PIXELS,0),i.pixelStorei(i.UNPACK_SKIP_ROWS,0),i.pixelStorei(i.UNPACK_SKIP_IMAGES,0),h={},g={},j=null,Q={},d={},l={},m=new WeakMap,_=[],S=null,p=!1,u=null,M=null,w=null,E=null,A=null,T=null,f=null,v=new Be(0,0,0),N=0,I=!1,D=null,z=null,q=null,P=null,W=null,Z.set(0,0,i.canvas.width,i.canvas.height),pe.set(0,0,i.canvas.width,i.canvas.height),r.reset(),a.reset(),o.reset()}return{buffers:{color:r,depth:a,stencil:o},enable:me,disable:Ue,bindFramebuffer:ht,drawBuffers:Ce,useProgram:Ke,setBlending:bt,setMaterial:ft,setFlipSided:Bt,setCullFace:ot,setLineWidth:pn,setPolygonOffset:xt,setScissorTest:Jt,activeTexture:$t,bindTexture:Kt,unbindTexture:L,compressedTexImage2D:jt,compressedTexImage3D:st,texImage2D:x,texImage3D:O,pixelStorei:K,getParameter:ee,updateUBOMapping:X,uniformBlockBinding:Y,texStorage2D:Le,texStorage3D:b,texSubImage2D:rt,texSubImage3D:ue,compressedTexSubImage2D:pt,compressedTexSubImage3D:we,scissor:se,viewport:ce,reset:ae}}function y2(i,e,t,n,s,r,a){let o=e.has("WEBGL_multisampled_render_to_texture")?e.get("WEBGL_multisampled_render_to_texture"):null,l=typeof navigator>"u"?!1:/OculusBrowser/g.test(navigator.userAgent),c=new Re,h=new WeakMap,g=new Set,d,m=new WeakMap,_=new Set,S=new FinalizationRegistry(b=>_.delete(b)),p=!1;try{p=typeof OffscreenCanvas<"u"&&new OffscreenCanvas(1,1).getContext("2d")!==null}catch{}function u(b,x){return p?new OffscreenCanvas(b,x):cs("canvas")}function M(b,x,O){let ee=1,K=Le(b);if((K.width>O||K.height>O)&&(ee=O/Math.max(K.width,K.height)),ee<1)if(typeof HTMLImageElement<"u"&&b instanceof HTMLImageElement||typeof HTMLCanvasElement<"u"&&b instanceof HTMLCanvasElement||typeof ImageBitmap<"u"&&b instanceof ImageBitmap||typeof VideoFrame<"u"&&b instanceof VideoFrame){let se=Math.floor(ee*K.width),ce=Math.floor(ee*K.height);d===void 0&&(d=u(se,ce));let X=x?u(se,ce):d;return X.width=se,X.height=ce,X.getContext("2d").drawImage(b,0,0,se,ce),Te("WebGLRenderer: Texture has been resized from ("+K.width+"x"+K.height+") to ("+se+"x"+ce+")."),X}else return"data"in b&&Te("WebGLRenderer: Image in DataTexture is too big ("+K.width+"x"+K.height+")."),b;return b}function w(b){return b.generateMipmaps}function E(b){i.generateMipmap(b)}function A(b){return b.isWebGLCubeRenderTarget?i.TEXTURE_CUBE_MAP:b.isWebGL3DRenderTarget?i.TEXTURE_3D:b.isWebGLArrayRenderTarget||b.isCompressedArrayTexture?i.TEXTURE_2D_ARRAY:i.TEXTURE_2D}function T(b,x,O,ee,K,se=!1){if(b!==null){if(i[b]!==void 0)return i[b];Te("WebGLRenderer: Attempt to use non-existing WebGL internal format '"+b+"'")}let ce;ee&&(ce=e.get("EXT_texture_norm16"),ce||Te("WebGLRenderer: Unable to use normalized textures without EXT_texture_norm16 extension"));let X=x;if(x===i.RED&&(O===i.FLOAT&&(X=i.R32F),O===i.HALF_FLOAT&&(X=i.R16F),O===i.UNSIGNED_BYTE&&(X=i.R8),O===i.UNSIGNED_SHORT&&ce&&(X=ce.R16_EXT),O===i.SHORT&&ce&&(X=ce.R16_SNORM_EXT)),x===i.RED_INTEGER&&(O===i.UNSIGNED_BYTE&&(X=i.R8UI),O===i.UNSIGNED_SHORT&&(X=i.R16UI),O===i.UNSIGNED_INT&&(X=i.R32UI),O===i.BYTE&&(X=i.R8I),O===i.SHORT&&(X=i.R16I),O===i.INT&&(X=i.R32I)),x===i.RG&&(O===i.FLOAT&&(X=i.RG32F),O===i.HALF_FLOAT&&(X=i.RG16F),O===i.UNSIGNED_BYTE&&(X=i.RG8),O===i.UNSIGNED_SHORT&&ce&&(X=ce.RG16_EXT),O===i.SHORT&&ce&&(X=ce.RG16_SNORM_EXT)),x===i.RG_INTEGER&&(O===i.UNSIGNED_BYTE&&(X=i.RG8UI),O===i.UNSIGNED_SHORT&&(X=i.RG16UI),O===i.UNSIGNED_INT&&(X=i.RG32UI),O===i.BYTE&&(X=i.RG8I),O===i.SHORT&&(X=i.RG16I),O===i.INT&&(X=i.RG32I)),x===i.RGB_INTEGER&&(O===i.UNSIGNED_BYTE&&(X=i.RGB8UI),O===i.UNSIGNED_SHORT&&(X=i.RGB16UI),O===i.UNSIGNED_INT&&(X=i.RGB32UI),O===i.BYTE&&(X=i.RGB8I),O===i.SHORT&&(X=i.RGB16I),O===i.INT&&(X=i.RGB32I)),x===i.RGBA_INTEGER&&(O===i.UNSIGNED_BYTE&&(X=i.RGBA8UI),O===i.UNSIGNED_SHORT&&(X=i.RGBA16UI),O===i.UNSIGNED_INT&&(X=i.RGBA32UI),O===i.BYTE&&(X=i.RGBA8I),O===i.SHORT&&(X=i.RGBA16I),O===i.INT&&(X=i.RGBA32I)),x===i.RGB&&(O===i.UNSIGNED_SHORT&&ce&&(X=ce.RGB16_EXT),O===i.SHORT&&ce&&(X=ce.RGB16_SNORM_EXT),O===i.UNSIGNED_INT_5_9_9_9_REV&&(X=i.RGB9_E5),O===i.UNSIGNED_INT_10F_11F_11F_REV&&(X=i.R11F_G11F_B10F)),x===i.RGBA){let Y=se?ls:We.getTransfer(K);O===i.FLOAT&&(X=i.RGBA32F),O===i.HALF_FLOAT&&(X=i.RGBA16F),O===i.UNSIGNED_BYTE&&(X=Y===$e?i.SRGB8_ALPHA8:i.RGBA8),O===i.UNSIGNED_SHORT&&ce&&(X=ce.RGBA16_EXT),O===i.SHORT&&ce&&(X=ce.RGBA16_SNORM_EXT),O===i.UNSIGNED_SHORT_4_4_4_4&&(X=i.RGBA4),O===i.UNSIGNED_SHORT_5_5_5_1&&(X=i.RGB5_A1)}return(X===i.R16F||X===i.R32F||X===i.RG16F||X===i.RG32F||X===i.RGBA16F||X===i.RGBA32F)&&e.get("EXT_color_buffer_float"),X}function f(b,x){let O;return b?x===null||x===cn||x===pi?O=i.DEPTH24_STENCIL8:x===hn?O=i.DEPTH32F_STENCIL8:x===Yi&&(O=i.DEPTH24_STENCIL8,Te("DepthTexture: 16 bit depth attachment is not supported with stencil. Using 24-bit attachment.")):x===null||x===cn||x===pi?O=i.DEPTH_COMPONENT24:x===hn?O=i.DEPTH_COMPONENT32F:x===Yi&&(O=i.DEPTH_COMPONENT16),O}function v(b,x){return w(b)===!0||b.isFramebufferTexture&&b.minFilter!==Mt&&b.minFilter!==Ft?Math.log2(Math.max(x.width,x.height))+1:b.mipmaps.length>0?b.mipmaps.length:b.isCompressedTexture&&Array.isArray(b.image)?x.mipmaps.length:1}function N(b){let x=new WeakRef(b);n.get(b).__ref=x,_.add(x),S.register(b,x,x)}function I(b){let x=n.get(b).__ref;x!==void 0&&(_.delete(x),S.unregister(x))}function D(b){q(b.target)}function z(b){P(b.target)}function q(b){b.removeEventListener("dispose",D),I(b),$(b),b.isVideoTexture&&h.delete(b),b.isHTMLTexture&&g.delete(b)}function P(b){b.removeEventListener("dispose",z),I(b),te(b)}function W(){for(let b of _){let x=b.deref();x!==void 0&&(x.isRenderTarget===!0?P(x):q(x))}_.clear(),g.clear()}function $(b){let x=n.get(b);if(x.__webglInit===void 0)return;let O=b.source,ee=m.get(O);if(ee){let K=ee[x.__cacheKey];K.usedTimes--,K.usedTimes===0&&G(b),Object.keys(ee).length===0&&m.delete(O)}n.remove(b)}function G(b){let x=n.get(b);i.deleteTexture(x.__webglTexture);let O=b.source,ee=m.get(O);delete ee[x.__cacheKey],a.memory.textures--}function te(b){let x=n.get(b);x.__depthDisposeCallback&&x.__depthDisposeCallback();let O=b.depthTexture;if(O&&O.renderTarget===b&&q(O),b.isWebGLCubeRenderTarget)for(let K=0;K<6;K++){if(Array.isArray(x.__webglFramebuffer[K]))for(let se=0;se<x.__webglFramebuffer[K].length;se++)i.deleteFramebuffer(x.__webglFramebuffer[K][se]);else i.deleteFramebuffer(x.__webglFramebuffer[K]);x.__webglDepthbuffer&&i.deleteRenderbuffer(x.__webglDepthbuffer[K])}else{if(Array.isArray(x.__webglFramebuffer))for(let K=0;K<x.__webglFramebuffer.length;K++)i.deleteFramebuffer(x.__webglFramebuffer[K]);else i.deleteFramebuffer(x.__webglFramebuffer);if(x.__webglDepthbuffer&&i.deleteRenderbuffer(x.__webglDepthbuffer),x.__webglMultisampledFramebuffer&&i.deleteFramebuffer(x.__webglMultisampledFramebuffer),x.__webglColorRenderbuffer)for(let K=0;K<x.__webglColorRenderbuffer.length;K++)x.__webglColorRenderbuffer[K]&&i.deleteRenderbuffer(x.__webglColorRenderbuffer[K]);x.__webglDepthRenderbuffer&&i.deleteRenderbuffer(x.__webglDepthRenderbuffer)}let ee=b.textures;for(let K=0,se=ee.length;K<se;K++){let ce=n.get(ee[K]);ce.__webglTexture&&(i.deleteTexture(ce.__webglTexture),a.memory.textures--),n.remove(ee[K])}n.remove(b)}let H=0;function j(){H=0}function Q(){return H}function Se(b){H=b}function De(){let b=H;return b>=s.maxTextures&&Te("WebGLTextures: Trying to use "+(b+1)+" texture units while this GPU supports only "+s.maxTextures),H+=1,b}function Z(b){let x=[];return x.push(b.wrapS),x.push(b.wrapT),x.push(b.wrapR||0),x.push(b.magFilter),x.push(b.minFilter),x.push(b.anisotropy),x.push(b.internalFormat),x.push(b.format),x.push(b.type),x.push(b.generateMipmaps),x.push(b.mipmapsAutoUpdate),x.push(b.premultiplyAlpha),x.push(b.flipY),x.push(b.unpackAlignment),x.push(b.colorSpace),x.join()}function pe(b,x){let O=n.get(b);if(b.isVideoTexture&&pt(b),b.isRenderTargetTexture===!1&&b.isExternalTexture!==!0&&b.version>0&&O.__version!==b.version){let ee=b.image;if(ee===null)Te("WebGLRenderer: Texture marked for update but no image data found.");else if(ee.complete===!1)Te("WebGLRenderer: Texture marked for update but image is incomplete");else{ft(O,b,x);return}}else b.isExternalTexture&&(O.__webglTexture=b.sourceTexture?b.sourceTexture:null);t.bindTexture(i.TEXTURE_2D,O.__webglTexture,i.TEXTURE0+x)}function xe(b,x){let O=n.get(b);if(b.isRenderTargetTexture===!1&&b.version>0&&O.__version!==b.version){ft(O,b,x);return}else b.isExternalTexture&&(O.__webglTexture=b.sourceTexture?b.sourceTexture:null);t.bindTexture(i.TEXTURE_2D_ARRAY,O.__webglTexture,i.TEXTURE0+x)}function Ae(b,x){let O=n.get(b);if(b.isRenderTargetTexture===!1&&b.version>0&&O.__version!==b.version){ft(O,b,x);return}t.bindTexture(i.TEXTURE_3D,O.__webglTexture,i.TEXTURE0+x)}function me(b,x){let O=n.get(b);if(b.version>0&&O.__version!==b.version){Bt(O,b,x);return}t.bindTexture(i.TEXTURE_CUBE_MAP,O.__webglTexture,i.TEXTURE0+x)}let Ue={[Mr]:i.REPEAT,[gn]:i.CLAMP_TO_EDGE,[br]:i.MIRRORED_REPEAT},ht={[Mt]:i.NEAREST,[Bc]:i.NEAREST_MIPMAP_NEAREST,[Is]:i.NEAREST_MIPMAP_LINEAR,[Ft]:i.LINEAR,[Kr]:i.LINEAR_MIPMAP_NEAREST,[Dn]:i.LINEAR_MIPMAP_LINEAR},Ce={[Vc]:i.NEVER,[Yo]:i.ALWAYS,[Hc]:i.LESS,[Xo]:i.LEQUAL,[Wc]:i.EQUAL,[qo]:i.GEQUAL,[Xc]:i.GREATER,[qc]:i.NOTEQUAL};function Ke(b,x){if(x.type===hn&&e.has("OES_texture_float_linear")===!1&&(x.magFilter===Ft||x.magFilter===Kr||x.magFilter===Is||x.magFilter===Dn||x.minFilter===Ft||x.minFilter===Kr||x.minFilter===Is||x.minFilter===Dn)&&Te("WebGLRenderer: Unable to use linear filtering with floating point textures. OES_texture_float_linear not supported on this device."),i.texParameteri(b,i.TEXTURE_WRAP_S,Ue[x.wrapS]),i.texParameteri(b,i.TEXTURE_WRAP_T,Ue[x.wrapT]),(b===i.TEXTURE_3D||b===i.TEXTURE_2D_ARRAY)&&i.texParameteri(b,i.TEXTURE_WRAP_R,Ue[x.wrapR]),i.texParameteri(b,i.TEXTURE_MAG_FILTER,ht[x.magFilter]),i.texParameteri(b,i.TEXTURE_MIN_FILTER,ht[x.minFilter]),x.compareFunction&&(i.texParameteri(b,i.TEXTURE_COMPARE_MODE,i.COMPARE_REF_TO_TEXTURE),i.texParameteri(b,i.TEXTURE_COMPARE_FUNC,Ce[x.compareFunction])),e.has("EXT_texture_filter_anisotropic")===!0){if(x.magFilter===Mt||x.minFilter!==Is&&x.minFilter!==Dn||x.type===hn&&e.has("OES_texture_float_linear")===!1)return;if(x.anisotropy>1||n.get(x).__currentAnisotropy){let O=e.get("EXT_texture_filter_anisotropic");i.texParameterf(b,O.TEXTURE_MAX_ANISOTROPY_EXT,Math.min(x.anisotropy,s.getMaxAnisotropy())),n.get(x).__currentAnisotropy=x.anisotropy}}}function Qe(b,x){let O=!1;b.__webglInit===void 0&&(b.__webglInit=!0,x.addEventListener("dispose",D),N(x));let ee=x.source,K=m.get(ee);K===void 0&&(K={},m.set(ee,K));let se=Z(x);if(se!==b.__cacheKey){K[se]===void 0&&(K[se]={texture:i.createTexture(),usedTimes:0},a.memory.textures++,O=!0),K[se].usedTimes++;let ce=K[b.__cacheKey];ce!==void 0&&(K[b.__cacheKey].usedTimes--,ce.usedTimes===0&&G(x)),b.__cacheKey=se,b.__webglTexture=K[se].texture}return O}function Ge(b,x,O){return Math.floor(Math.floor(b/O)/x)}function bt(b,x,O,ee){let se=b.updateRanges;if(se.length===0)t.texSubImage2D(i.TEXTURE_2D,0,0,0,x.width,x.height,O,ee,x.data);else{se.sort((R,J)=>R.start-J.start);let ce=0;for(let R=1;R<se.length;R++){let J=se[ce],V=se[R],oe=J.start+J.count,ie=Ge(V.start,x.width,4),re=Ge(J.start,x.width,4);V.start<=oe+1&&ie===re&&Ge(V.start+V.count-1,x.width,4)===ie?J.count=Math.max(J.count,V.start+V.count-J.start):(++ce,se[ce]=V)}se.length=ce+1;let X=t.getParameter(i.UNPACK_ROW_LENGTH),Y=t.getParameter(i.UNPACK_SKIP_PIXELS),ae=t.getParameter(i.UNPACK_SKIP_ROWS);t.pixelStorei(i.UNPACK_ROW_LENGTH,x.width);for(let R=0,J=se.length;R<J;R++){let V=se[R],oe=Math.floor(V.start/4),ie=Math.ceil(V.count/4),re=oe%x.width,be=Math.floor(oe/x.width),Oe=ie,ne=1;t.pixelStorei(i.UNPACK_SKIP_PIXELS,re),t.pixelStorei(i.UNPACK_SKIP_ROWS,be),t.texSubImage2D(i.TEXTURE_2D,0,re,be,Oe,ne,O,ee,x.data)}b.clearUpdateRanges(),t.pixelStorei(i.UNPACK_ROW_LENGTH,X),t.pixelStorei(i.UNPACK_SKIP_PIXELS,Y),t.pixelStorei(i.UNPACK_SKIP_ROWS,ae)}}function ft(b,x,O){let ee=i.TEXTURE_2D;(x.isDataArrayTexture||x.isCompressedArrayTexture)&&(ee=i.TEXTURE_2D_ARRAY),x.isData3DTexture&&(ee=i.TEXTURE_3D);let K=Qe(b,x),se=x.source;t.bindTexture(ee,b.__webglTexture,i.TEXTURE0+O);let ce=n.get(se);if(se.version!==ce.__version||K===!0){if(t.activeTexture(i.TEXTURE0+O),(typeof ImageBitmap<"u"&&x.image instanceof ImageBitmap)===!1){let ne=We.getPrimaries(We.workingColorSpace),Ee=x.colorSpace===Un?null:We.getPrimaries(x.colorSpace),Fe=x.colorSpace===Un||ne===Ee?i.NONE:i.BROWSER_DEFAULT_WEBGL;t.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,x.flipY),t.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,x.premultiplyAlpha),t.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,Fe)}t.pixelStorei(i.UNPACK_ALIGNMENT,x.unpackAlignment);let Y=M(x.image,!1,s.maxTextureSize);Y=we(x,Y);let ae=r.convert(x.format,x.colorSpace),R=r.convert(x.type),J=T(x.internalFormat,ae,R,x.normalized,x.colorSpace,x.isVideoTexture);Ke(ee,x);let V,oe=x.mipmaps,ie=x.isVideoTexture!==!0,re=ce.__version===void 0||K===!0,be=se.dataReady,Oe=v(x,Y);if(x.isDepthTexture)J=f(x.format===Nn,x.type),re&&(ie?t.texStorage2D(i.TEXTURE_2D,1,J,Y.width,Y.height):t.texImage2D(i.TEXTURE_2D,0,J,Y.width,Y.height,0,ae,R,null));else if(x.isDataTexture)if(oe.length>0){ie&&re&&t.texStorage2D(i.TEXTURE_2D,Oe,J,oe[0].width,oe[0].height);for(let ne=0,Ee=oe.length;ne<Ee;ne++)V=oe[ne],ie?be&&t.texSubImage2D(i.TEXTURE_2D,ne,0,0,V.width,V.height,ae,R,V.data):t.texImage2D(i.TEXTURE_2D,ne,J,V.width,V.height,0,ae,R,V.data);x.generateMipmaps=!1}else ie?(re&&t.texStorage2D(i.TEXTURE_2D,Oe,J,Y.width,Y.height),be&&bt(x,Y,ae,R)):t.texImage2D(i.TEXTURE_2D,0,J,Y.width,Y.height,0,ae,R,Y.data);else if(x.isCompressedTexture)if(x.isCompressedArrayTexture){ie&&re&&t.texStorage3D(i.TEXTURE_2D_ARRAY,Oe,J,oe[0].width,oe[0].height,Y.depth);for(let ne=0,Ee=oe.length;ne<Ee;ne++)if(V=oe[ne],x.format!==dn)if(ae!==null)if(ie){if(be)if(x.layerUpdates.size>0){let Fe=il(V.width,V.height,x.format,x.type);for(let de of x.layerUpdates){let je=V.data.subarray(de*Fe/V.data.BYTES_PER_ELEMENT,(de+1)*Fe/V.data.BYTES_PER_ELEMENT);t.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,ne,0,0,de,V.width,V.height,1,ae,je)}}else t.compressedTexSubImage3D(i.TEXTURE_2D_ARRAY,ne,0,0,0,V.width,V.height,Y.depth,ae,V.data)}else t.compressedTexImage3D(i.TEXTURE_2D_ARRAY,ne,J,V.width,V.height,Y.depth,0,V.data,0,0);else Te("WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()");else ie?be&&t.texSubImage3D(i.TEXTURE_2D_ARRAY,ne,0,0,0,V.width,V.height,Y.depth,ae,R,V.data):t.texImage3D(i.TEXTURE_2D_ARRAY,ne,J,V.width,V.height,Y.depth,0,ae,R,V.data);x.layerUpdates.size>0&&x.clearLayerUpdates()}else{ie&&re&&t.texStorage2D(i.TEXTURE_2D,Oe,J,oe[0].width,oe[0].height);for(let ne=0,Ee=oe.length;ne<Ee;ne++)V=oe[ne],x.format!==dn?ae!==null?ie?be&&t.compressedTexSubImage2D(i.TEXTURE_2D,ne,0,0,V.width,V.height,ae,V.data):t.compressedTexImage2D(i.TEXTURE_2D,ne,J,V.width,V.height,0,V.data):Te("WebGLRenderer: Attempt to load unsupported compressed texture format in .uploadTexture()"):ie?be&&t.texSubImage2D(i.TEXTURE_2D,ne,0,0,V.width,V.height,ae,R,V.data):t.texImage2D(i.TEXTURE_2D,ne,J,V.width,V.height,0,ae,R,V.data)}else if(x.isDataArrayTexture)if(ie){if(re&&t.texStorage3D(i.TEXTURE_2D_ARRAY,Oe,J,Y.width,Y.height,Y.depth),be)if(x.layerUpdates.size>0){let ne=il(Y.width,Y.height,x.format,x.type);for(let Ee of x.layerUpdates){let Fe=Y.data.subarray(Ee*ne/Y.data.BYTES_PER_ELEMENT,(Ee+1)*ne/Y.data.BYTES_PER_ELEMENT);t.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,Ee,Y.width,Y.height,1,ae,R,Fe)}x.clearLayerUpdates()}else t.texSubImage3D(i.TEXTURE_2D_ARRAY,0,0,0,0,Y.width,Y.height,Y.depth,ae,R,Y.data)}else t.texImage3D(i.TEXTURE_2D_ARRAY,0,J,Y.width,Y.height,Y.depth,0,ae,R,Y.data);else if(x.isData3DTexture)ie?(re&&t.texStorage3D(i.TEXTURE_3D,Oe,J,Y.width,Y.height,Y.depth),be&&t.texSubImage3D(i.TEXTURE_3D,0,0,0,0,Y.width,Y.height,Y.depth,ae,R,Y.data)):t.texImage3D(i.TEXTURE_3D,0,J,Y.width,Y.height,Y.depth,0,ae,R,Y.data);else if(x.isFramebufferTexture){if(re)if(ie)t.texStorage2D(i.TEXTURE_2D,Oe,J,Y.width,Y.height);else{let ne=Y.width,Ee=Y.height;for(let Fe=0;Fe<Oe;Fe++)t.texImage2D(i.TEXTURE_2D,Fe,J,ne,Ee,0,ae,R,null),ne>>=1,Ee>>=1}}else if(x.isHTMLTexture){if("texElementImage2D"in i){let ne=i.canvas;if(ne.hasAttribute("layoutsubtree")||ne.setAttribute("layoutsubtree","true"),Y.parentNode!==ne){ne.appendChild(Y),g.add(x),ne.onpaint=Ee=>{let Fe=Ee.changedElements;for(let de of g)Fe.includes(de.image)&&(de.needsUpdate=!0)},ne.requestPaint();return}if(i.texElementImage2D.length===3)i.texElementImage2D(i.TEXTURE_2D,i.RGBA8,Y);else{let Fe=i.RGBA,de=i.RGBA,je=i.UNSIGNED_BYTE;i.texElementImage2D(i.TEXTURE_2D,0,Fe,de,je,Y)}i.texParameteri(i.TEXTURE_2D,i.TEXTURE_MIN_FILTER,i.LINEAR),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_S,i.CLAMP_TO_EDGE),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_T,i.CLAMP_TO_EDGE)}}else if(oe.length>0){if(ie&&re){let ne=Le(oe[0]);t.texStorage2D(i.TEXTURE_2D,Oe,J,ne.width,ne.height)}for(let ne=0,Ee=oe.length;ne<Ee;ne++)V=oe[ne],ie?be&&t.texSubImage2D(i.TEXTURE_2D,ne,0,0,ae,R,V):t.texImage2D(i.TEXTURE_2D,ne,J,ae,R,V);x.generateMipmaps=!1}else if(ie){if(re){let ne=Le(Y);t.texStorage2D(i.TEXTURE_2D,Oe,J,ne.width,ne.height)}be&&t.texSubImage2D(i.TEXTURE_2D,0,0,0,ae,R,Y)}else t.texImage2D(i.TEXTURE_2D,0,J,ae,R,Y);w(x)&&x.mipmapsAutoUpdate===!0&&E(ee),ce.__version=se.version,x.onUpdate&&x.onUpdate(x)}b.__version=x.version}function Bt(b,x,O){if(x.image.length!==6)return;let ee=Qe(b,x),K=x.source;t.bindTexture(i.TEXTURE_CUBE_MAP,b.__webglTexture,i.TEXTURE0+O);let se=n.get(K);if(K.version!==se.__version||ee===!0){t.activeTexture(i.TEXTURE0+O);let ce=We.getPrimaries(We.workingColorSpace),X=x.colorSpace===Un?null:We.getPrimaries(x.colorSpace),Y=x.colorSpace===Un||ce===X?i.NONE:i.BROWSER_DEFAULT_WEBGL;t.pixelStorei(i.UNPACK_FLIP_Y_WEBGL,x.flipY),t.pixelStorei(i.UNPACK_PREMULTIPLY_ALPHA_WEBGL,x.premultiplyAlpha),t.pixelStorei(i.UNPACK_ALIGNMENT,x.unpackAlignment),t.pixelStorei(i.UNPACK_COLORSPACE_CONVERSION_WEBGL,Y);let ae=x.isCompressedTexture||x.image[0].isCompressedTexture,R=x.image[0]&&x.image[0].isDataTexture,J=[];for(let de=0;de<6;de++)!ae&&!R?J[de]=M(x.image[de],!0,s.maxCubemapSize):J[de]=R?x.image[de].image:x.image[de],J[de]=we(x,J[de]);let V=J[0],oe=r.convert(x.format,x.colorSpace),ie=r.convert(x.type),re=T(x.internalFormat,oe,ie,x.normalized,x.colorSpace),be=x.isVideoTexture!==!0,Oe=se.__version===void 0||ee===!0,ne=K.dataReady,Ee=v(x,V);Ke(i.TEXTURE_CUBE_MAP,x);let Fe;if(x.isDepthTexture){if(re=f(x.format===Nn,x.type),Oe)if(be)t.texStorage2D(i.TEXTURE_CUBE_MAP,1,re,V.width,V.height);else for(let de=0;de<6;de++)t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,0,re,V.width,V.height,0,oe,ie,null)}else if(ae){be&&Oe&&t.texStorage2D(i.TEXTURE_CUBE_MAP,Ee,re,V.width,V.height);for(let de=0;de<6;de++){Fe=J[de].mipmaps;for(let je=0;je<Fe.length;je++){let yt=Fe[je];x.format!==dn?oe!==null?be?ne&&t.compressedTexSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je,0,0,yt.width,yt.height,oe,yt.data):t.compressedTexImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je,re,yt.width,yt.height,0,yt.data):Te("WebGLRenderer: Attempt to load unsupported compressed texture format in .setTextureCube()"):be?ne&&t.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je,0,0,yt.width,yt.height,oe,ie,yt.data):t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je,re,yt.width,yt.height,0,oe,ie,yt.data)}}}else{if(Fe=x.mipmaps,be&&Oe){Fe.length>0&&Ee++;let de=Le(J[0]);t.texStorage2D(i.TEXTURE_CUBE_MAP,Ee,re,de.width,de.height)}for(let de=0;de<6;de++)if(R){be?ne&&t.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,0,0,0,J[de].width,J[de].height,oe,ie,J[de].data):t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,0,re,J[de].width,J[de].height,0,oe,ie,J[de].data);for(let je=0;je<Fe.length;je++){let Fn=Fe[je].image[de].image;be?ne&&t.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je+1,0,0,Fn.width,Fn.height,oe,ie,Fn.data):t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je+1,re,Fn.width,Fn.height,0,oe,ie,Fn.data)}}else{be?ne&&t.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,0,0,0,oe,ie,J[de]):t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,0,re,oe,ie,J[de]);for(let je=0;je<Fe.length;je++){let yt=Fe[je];be?ne&&t.texSubImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je+1,0,0,oe,ie,yt.image[de]):t.texImage2D(i.TEXTURE_CUBE_MAP_POSITIVE_X+de,je+1,re,oe,ie,yt.image[de])}}}w(x)&&x.mipmapsAutoUpdate===!0&&E(i.TEXTURE_CUBE_MAP),se.__version=K.version,x.onUpdate&&x.onUpdate(x)}b.__version=x.version}function ot(b,x,O,ee,K,se){let ce=r.convert(O.format,O.colorSpace),X=r.convert(O.type),Y=T(O.internalFormat,ce,X,O.normalized,O.colorSpace),ae=n.get(x),R=n.get(O);if(R.__renderTarget=x,!ae.__hasExternalTextures){let J=Math.max(1,x.width>>se),V=Math.max(1,x.height>>se);K===i.TEXTURE_3D||K===i.TEXTURE_2D_ARRAY?t.texImage3D(K,se,Y,J,V,x.depth,0,ce,X,null):t.texImage2D(K,se,Y,J,V,0,ce,X,null)}t.bindFramebuffer(i.FRAMEBUFFER,b),ue(x)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,ee,K,R.__webglTexture,0,rt(x)):(K===i.TEXTURE_2D||K>=i.TEXTURE_CUBE_MAP_POSITIVE_X&&K<=i.TEXTURE_CUBE_MAP_NEGATIVE_Z)&&i.framebufferTexture2D(i.FRAMEBUFFER,ee,K,R.__webglTexture,se),t.bindFramebuffer(i.FRAMEBUFFER,null)}function pn(b,x,O){if(i.bindRenderbuffer(i.RENDERBUFFER,b),x.depthBuffer){let ee=x.depthTexture,K=ee&&ee.isDepthTexture?ee.type:null,se=f(x.stencilBuffer,K),ce=x.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;ue(x)?o.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,rt(x),se,x.width,x.height):O?i.renderbufferStorageMultisample(i.RENDERBUFFER,rt(x),se,x.width,x.height):i.renderbufferStorage(i.RENDERBUFFER,se,x.width,x.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,ce,i.RENDERBUFFER,b)}else{let ee=x.textures;for(let K=0;K<ee.length;K++){let se=ee[K],ce=r.convert(se.format,se.colorSpace),X=r.convert(se.type),Y=T(se.internalFormat,ce,X,se.normalized,se.colorSpace);ue(x)?o.renderbufferStorageMultisampleEXT(i.RENDERBUFFER,rt(x),Y,x.width,x.height):O?i.renderbufferStorageMultisample(i.RENDERBUFFER,rt(x),Y,x.width,x.height):i.renderbufferStorage(i.RENDERBUFFER,Y,x.width,x.height)}}i.bindRenderbuffer(i.RENDERBUFFER,null)}function xt(b,x,O){let ee=x.isWebGLCubeRenderTarget===!0;if(t.bindFramebuffer(i.FRAMEBUFFER,b),!(x.depthTexture&&x.depthTexture.isDepthTexture))throw new Error("THREE.WebGLTextures: renderTarget.depthTexture must be an instance of THREE.DepthTexture.");let K=n.get(x.depthTexture);K.__renderTarget=x;let se=ee?x.depthTexture.image[0]:x.depthTexture.image;(!K.__webglTexture||se.width!==x.width||se.height!==x.height)&&(se.width=x.width,se.height=x.height,x.depthTexture.needsUpdate=!0),ee?me(x.depthTexture,0):pe(x.depthTexture,0);let ce=K.__webglTexture,X=rt(x),Y=ee?i.TEXTURE_CUBE_MAP_POSITIVE_X+O:i.TEXTURE_2D,ae=x.depthTexture.format===Nn?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;if(x.depthTexture.format===Cn)ue(x)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,ae,Y,ce,0,X):i.framebufferTexture2D(i.FRAMEBUFFER,ae,Y,ce,0);else if(x.depthTexture.format===Nn)ue(x)?o.framebufferTexture2DMultisampleEXT(i.FRAMEBUFFER,ae,Y,ce,0,X):i.framebufferTexture2D(i.FRAMEBUFFER,ae,Y,ce,0);else throw new Error("THREE.WebGLTextures: Unknown depthTexture format.")}function Jt(b){let x=n.get(b),O=b.isWebGLCubeRenderTarget===!0;if(x.__boundDepthTexture!==b.depthTexture){let ee=b.depthTexture;if(x.__depthDisposeCallback&&x.__depthDisposeCallback(),ee){let K=()=>{delete x.__boundDepthTexture,delete x.__depthDisposeCallback,ee.removeEventListener("dispose",K)};ee.addEventListener("dispose",K),x.__depthDisposeCallback=K}x.__boundDepthTexture=ee}if(b.depthTexture&&!x.__autoAllocateDepthBuffer)if(O)for(let ee=0;ee<6;ee++)xt(x.__webglFramebuffer[ee],b,ee);else b.texture.mipmaps.length>0?xt(x.__webglFramebuffer[0],b,0):xt(x.__webglFramebuffer,b,0);else if(O){x.__webglDepthbuffer=[];for(let ee=0;ee<6;ee++)if(t.bindFramebuffer(i.FRAMEBUFFER,x.__webglFramebuffer[ee]),x.__webglDepthbuffer[ee]===void 0)x.__webglDepthbuffer[ee]=i.createRenderbuffer(),pn(x.__webglDepthbuffer[ee],b,!1);else{let K=b.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,se=x.__webglDepthbuffer[ee];i.bindRenderbuffer(i.RENDERBUFFER,se),i.framebufferRenderbuffer(i.FRAMEBUFFER,K,i.RENDERBUFFER,se)}}else if(b.texture.mipmaps.length>0?t.bindFramebuffer(i.FRAMEBUFFER,x.__webglFramebuffer[0]):t.bindFramebuffer(i.FRAMEBUFFER,x.__webglFramebuffer),x.__webglDepthbuffer===void 0)x.__webglDepthbuffer=i.createRenderbuffer(),pn(x.__webglDepthbuffer,b,!1);else{let K=b.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,se=x.__webglDepthbuffer;i.bindRenderbuffer(i.RENDERBUFFER,se),i.framebufferRenderbuffer(i.FRAMEBUFFER,K,i.RENDERBUFFER,se)}t.bindFramebuffer(i.FRAMEBUFFER,null)}function $t(b,x,O){let ee=n.get(b);x!==void 0&&ot(ee.__webglFramebuffer,b,b.texture,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,0),O!==void 0&&Jt(b)}function Kt(b){let x=b.texture,O=n.get(b),ee=n.get(x);b.addEventListener("dispose",z),N(b);let K=b.textures,se=b.isWebGLCubeRenderTarget===!0,ce=K.length>1;if(ce||(ee.__webglTexture===void 0&&(ee.__webglTexture=i.createTexture()),ee.__version=x.version,a.memory.textures++),se){O.__webglFramebuffer=[];for(let X=0;X<6;X++)if(x.mipmaps.length>0){O.__webglFramebuffer[X]=[];for(let Y=0;Y<x.mipmaps.length;Y++)O.__webglFramebuffer[X][Y]=i.createFramebuffer()}else O.__webglFramebuffer[X]=i.createFramebuffer()}else{if(x.mipmaps.length>0){O.__webglFramebuffer=[];for(let X=0;X<x.mipmaps.length;X++)O.__webglFramebuffer[X]=i.createFramebuffer()}else O.__webglFramebuffer=i.createFramebuffer();if(ce)for(let X=0,Y=K.length;X<Y;X++){let ae=n.get(K[X]);ae.__webglTexture===void 0&&(ae.__webglTexture=i.createTexture(),a.memory.textures++)}if(b.samples>0&&ue(b)===!1){O.__webglMultisampledFramebuffer=i.createFramebuffer(),O.__webglColorRenderbuffer=[],t.bindFramebuffer(i.FRAMEBUFFER,O.__webglMultisampledFramebuffer);for(let X=0;X<K.length;X++){let Y=K[X];O.__webglColorRenderbuffer[X]=i.createRenderbuffer(),i.bindRenderbuffer(i.RENDERBUFFER,O.__webglColorRenderbuffer[X]);let ae=r.convert(Y.format,Y.colorSpace),R=r.convert(Y.type),J=T(Y.internalFormat,ae,R,Y.normalized,Y.colorSpace,b.isXRRenderTarget===!0),V=rt(b);i.renderbufferStorageMultisample(i.RENDERBUFFER,V,J,b.width,b.height),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+X,i.RENDERBUFFER,O.__webglColorRenderbuffer[X])}i.bindRenderbuffer(i.RENDERBUFFER,null),b.depthBuffer&&(O.__webglDepthRenderbuffer=i.createRenderbuffer(),pn(O.__webglDepthRenderbuffer,b,!0)),t.bindFramebuffer(i.FRAMEBUFFER,null)}}if(se){t.bindTexture(i.TEXTURE_CUBE_MAP,ee.__webglTexture),Ke(i.TEXTURE_CUBE_MAP,x);for(let X=0;X<6;X++)if(x.mipmaps.length>0)for(let Y=0;Y<x.mipmaps.length;Y++)ot(O.__webglFramebuffer[X][Y],b,x,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+X,Y);else ot(O.__webglFramebuffer[X],b,x,i.COLOR_ATTACHMENT0,i.TEXTURE_CUBE_MAP_POSITIVE_X+X,0);w(x)?E(i.TEXTURE_CUBE_MAP):x.mipmaps.length>0&&i.texParameteri(i.TEXTURE_CUBE_MAP,i.TEXTURE_MAX_LEVEL,x.mipmaps.length-1),t.unbindTexture()}else if(ce){for(let X=0,Y=K.length;X<Y;X++){let ae=K[X],R=n.get(ae),J=i.TEXTURE_2D;(b.isWebGL3DRenderTarget||b.isWebGLArrayRenderTarget)&&(J=b.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY),t.bindTexture(J,R.__webglTexture),Ke(J,ae),ot(O.__webglFramebuffer,b,ae,i.COLOR_ATTACHMENT0+X,J,0),w(ae)&&E(J)}t.unbindTexture()}else{let X=i.TEXTURE_2D;if((b.isWebGL3DRenderTarget||b.isWebGLArrayRenderTarget)&&(X=b.isWebGL3DRenderTarget?i.TEXTURE_3D:i.TEXTURE_2D_ARRAY),t.bindTexture(X,ee.__webglTexture),Ke(X,x),x.mipmaps.length>0)for(let Y=0;Y<x.mipmaps.length;Y++)ot(O.__webglFramebuffer[Y],b,x,i.COLOR_ATTACHMENT0,X,Y);else ot(O.__webglFramebuffer,b,x,i.COLOR_ATTACHMENT0,X,0);w(x)?E(X):x.mipmaps.length>0&&i.texParameteri(X,i.TEXTURE_MAX_LEVEL,x.mipmaps.length-1),t.unbindTexture()}b.depthBuffer&&Jt(b)}function L(b){let x=b.textures;for(let O=0,ee=x.length;O<ee;O++){let K=x[O];if(w(K)&&K.mipmapsAutoUpdate===!0){let se=A(b),ce=n.get(K).__webglTexture;t.bindTexture(se,ce),E(se),t.unbindTexture()}}}let jt=[];function st(b){if(b.samples>0){if(ue(b)===!1){let x=b.textures,O=b.width,ee=b.height,K=i.COLOR_BUFFER_BIT,se=b.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT,ce=n.get(b),X=x.length>1;if(X)for(let ae=0;ae<x.length;ae++)t.bindFramebuffer(i.FRAMEBUFFER,ce.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+ae,i.RENDERBUFFER,null),t.bindFramebuffer(i.FRAMEBUFFER,ce.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+ae,i.TEXTURE_2D,null,0);t.bindFramebuffer(i.READ_FRAMEBUFFER,ce.__webglMultisampledFramebuffer),b.texture.mipmaps.length>0?t.bindFramebuffer(i.DRAW_FRAMEBUFFER,ce.__webglFramebuffer[0]):t.bindFramebuffer(i.DRAW_FRAMEBUFFER,ce.__webglFramebuffer);for(let ae=0;ae<x.length;ae++){if(b.resolveDepthBuffer&&(b.depthBuffer&&(K|=i.DEPTH_BUFFER_BIT),b.stencilBuffer&&b.resolveStencilBuffer&&(K|=i.STENCIL_BUFFER_BIT)),X){i.framebufferRenderbuffer(i.READ_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.RENDERBUFFER,ce.__webglColorRenderbuffer[ae]);let R=n.get(x[ae]).__webglTexture;i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0,i.TEXTURE_2D,R,0)}i.blitFramebuffer(0,0,O,ee,0,0,O,ee,K,i.NEAREST),l===!0&&(jt.length=0,jt.push(i.COLOR_ATTACHMENT0+ae),b.depthBuffer&&b.storeMultisampledDepthBuffer===!1&&jt.push(se),i.invalidateFramebuffer(i.READ_FRAMEBUFFER,jt))}if(t.bindFramebuffer(i.READ_FRAMEBUFFER,null),t.bindFramebuffer(i.DRAW_FRAMEBUFFER,null),X)for(let ae=0;ae<x.length;ae++){t.bindFramebuffer(i.FRAMEBUFFER,ce.__webglMultisampledFramebuffer),i.framebufferRenderbuffer(i.FRAMEBUFFER,i.COLOR_ATTACHMENT0+ae,i.RENDERBUFFER,ce.__webglColorRenderbuffer[ae]);let R=n.get(x[ae]).__webglTexture;t.bindFramebuffer(i.FRAMEBUFFER,ce.__webglFramebuffer),i.framebufferTexture2D(i.DRAW_FRAMEBUFFER,i.COLOR_ATTACHMENT0+ae,i.TEXTURE_2D,R,0)}t.bindFramebuffer(i.DRAW_FRAMEBUFFER,ce.__webglMultisampledFramebuffer)}else if(b.depthBuffer&&b.storeMultisampledDepthBuffer===!1&&l){let x=b.stencilBuffer?i.DEPTH_STENCIL_ATTACHMENT:i.DEPTH_ATTACHMENT;i.invalidateFramebuffer(i.DRAW_FRAMEBUFFER,[x])}}}function rt(b){return Math.min(s.maxSamples,b.samples)}function ue(b){let x=n.get(b);return b.samples>0&&e.has("WEBGL_multisampled_render_to_texture")===!0&&x.__useRenderToTexture!==!1}function pt(b){let x=a.render.frame;h.get(b)!==x&&(h.set(b,x),b.update())}function we(b,x){let O=b.colorSpace,ee=b.format,K=b.type;return b.isCompressedTexture===!0||b.isVideoTexture===!0||O!==os&&O!==Un&&(We.getTransfer(O)===$e?(ee!==dn||K!==Gt)&&Te("WebGLTextures: sRGB encoded textures have to use RGBAFormat and UnsignedByteType."):Pe("WebGLTextures: Unsupported texture color space:",O)),x}function Le(b){return typeof HTMLImageElement<"u"&&b instanceof HTMLImageElement?(c.width=b.naturalWidth||b.width,c.height=b.naturalHeight||b.height):typeof VideoFrame<"u"&&b instanceof VideoFrame?(c.width=b.displayWidth,c.height=b.displayHeight):(c.width=b.width,c.height=b.height),c}this.allocateTextureUnit=De,this.resetTextureUnits=j,this.getTextureUnits=Q,this.setTextureUnits=Se,this.setTexture2D=pe,this.setTexture2DArray=xe,this.setTexture3D=Ae,this.setTextureCube=me,this.rebindTextures=$t,this.setupRenderTarget=Kt,this.updateRenderTargetMipmap=L,this.updateMultisampleRenderTarget=st,this.setupDepthRenderbuffer=Jt,this.setupFrameBufferTexture=ot,this.useMultisampledRTT=ue,this.dispose=W}function v2(i,e){function t(n,s=Un){let r,a=We.getTransfer(s);if(n===Gt)return i.UNSIGNED_BYTE;if(n===Qr)return i.UNSIGNED_SHORT_4_4_4_4;if(n===ea)return i.UNSIGNED_SHORT_5_5_5_1;if(n===ko)return i.UNSIGNED_INT_5_9_9_9_REV;if(n===Go)return i.UNSIGNED_INT_10F_11F_11F_REV;if(n===Bo)return i.BYTE;if(n===zo)return i.SHORT;if(n===Yi)return i.UNSIGNED_SHORT;if(n===jr)return i.INT;if(n===cn)return i.UNSIGNED_INT;if(n===hn)return i.FLOAT;if(n===un)return i.HALF_FLOAT;if(n===Vo)return i.ALPHA;if(n===Ho)return i.RGB;if(n===dn)return i.RGBA;if(n===Cn)return i.DEPTH_COMPONENT;if(n===Nn)return i.DEPTH_STENCIL;if(n===Wo)return i.RED;if(n===ta)return i.RED_INTEGER;if(n===Qn)return i.RG;if(n===na)return i.RG_INTEGER;if(n===ia)return i.RGBA_INTEGER;if(n===Ls||n===Ds||n===Ns||n===Us)if(a===$e)if(r=e.get("WEBGL_compressed_texture_s3tc_srgb"),r!==null){if(n===Ls)return r.COMPRESSED_SRGB_S3TC_DXT1_EXT;if(n===Ds)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT;if(n===Ns)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT;if(n===Us)return r.COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT}else return null;else if(r=e.get("WEBGL_compressed_texture_s3tc"),r!==null){if(n===Ls)return r.COMPRESSED_RGB_S3TC_DXT1_EXT;if(n===Ds)return r.COMPRESSED_RGBA_S3TC_DXT1_EXT;if(n===Ns)return r.COMPRESSED_RGBA_S3TC_DXT3_EXT;if(n===Us)return r.COMPRESSED_RGBA_S3TC_DXT5_EXT}else return null;if(n===sa||n===ra||n===aa||n===oa)if(r=e.get("WEBGL_compressed_texture_pvrtc"),r!==null){if(n===sa)return r.COMPRESSED_RGB_PVRTC_4BPPV1_IMG;if(n===ra)return r.COMPRESSED_RGB_PVRTC_2BPPV1_IMG;if(n===aa)return r.COMPRESSED_RGBA_PVRTC_4BPPV1_IMG;if(n===oa)return r.COMPRESSED_RGBA_PVRTC_2BPPV1_IMG}else return null;if(n===la||n===ca||n===ha||n===ua||n===da||n===Fs||n===fa)if(r=e.get("WEBGL_compressed_texture_etc"),r!==null){if(n===la||n===ca)return a===$e?r.COMPRESSED_SRGB8_ETC2:r.COMPRESSED_RGB8_ETC2;if(n===ha)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ETC2_EAC:r.COMPRESSED_RGBA8_ETC2_EAC;if(n===ua)return r.COMPRESSED_R11_EAC;if(n===da)return r.COMPRESSED_SIGNED_R11_EAC;if(n===Fs)return r.COMPRESSED_RG11_EAC;if(n===fa)return r.COMPRESSED_SIGNED_RG11_EAC}else return null;if(n===pa||n===ma||n===ga||n===_a||n===xa||n===ya||n===va||n===Sa||n===Ma||n===ba||n===Ea||n===Ta||n===Aa||n===wa)if(r=e.get("WEBGL_compressed_texture_astc"),r!==null){if(n===pa)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR:r.COMPRESSED_RGBA_ASTC_4x4_KHR;if(n===ma)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR:r.COMPRESSED_RGBA_ASTC_5x4_KHR;if(n===ga)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR:r.COMPRESSED_RGBA_ASTC_5x5_KHR;if(n===_a)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR:r.COMPRESSED_RGBA_ASTC_6x5_KHR;if(n===xa)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR:r.COMPRESSED_RGBA_ASTC_6x6_KHR;if(n===ya)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR:r.COMPRESSED_RGBA_ASTC_8x5_KHR;if(n===va)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR:r.COMPRESSED_RGBA_ASTC_8x6_KHR;if(n===Sa)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR:r.COMPRESSED_RGBA_ASTC_8x8_KHR;if(n===Ma)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR:r.COMPRESSED_RGBA_ASTC_10x5_KHR;if(n===ba)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR:r.COMPRESSED_RGBA_ASTC_10x6_KHR;if(n===Ea)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR:r.COMPRESSED_RGBA_ASTC_10x8_KHR;if(n===Ta)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR:r.COMPRESSED_RGBA_ASTC_10x10_KHR;if(n===Aa)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR:r.COMPRESSED_RGBA_ASTC_12x10_KHR;if(n===wa)return a===$e?r.COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR:r.COMPRESSED_RGBA_ASTC_12x12_KHR}else return null;if(n===Ra||n===Ca||n===Pa)if(r=e.get("EXT_texture_compression_bptc"),r!==null){if(n===Ra)return a===$e?r.COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT:r.COMPRESSED_RGBA_BPTC_UNORM_EXT;if(n===Ca)return r.COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT;if(n===Pa)return r.COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT}else return null;if(n===Ia||n===La||n===Os||n===Da)if(r=e.get("EXT_texture_compression_rgtc"),r!==null){if(n===Ia)return r.COMPRESSED_RED_RGTC1_EXT;if(n===La)return r.COMPRESSED_SIGNED_RED_RGTC1_EXT;if(n===Os)return r.COMPRESSED_RED_GREEN_RGTC2_EXT;if(n===Da)return r.COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT}else return null;return n===pi?i.UNSIGNED_INT_24_8:i[n]!==void 0?i[n]:null}return{convert:t}}var S2=`
void main() {

	gl_Position = vec4( position, 1.0 );

}`,M2=`
uniform sampler2DArray depthColor;
uniform float depthWidth;
uniform float depthHeight;

void main() {

	vec2 coord = vec2( gl_FragCoord.x / depthWidth, gl_FragCoord.y / depthHeight );

	if ( coord.x >= 1.0 ) {

		gl_FragDepth = texture( depthColor, vec3( coord.x - 1.0, coord.y, 1 ) ).r;

	} else {

		gl_FragDepth = texture( depthColor, vec3( coord.x, coord.y, 0 ) ).r;

	}

}`,_l=class{constructor(){this.texture=null,this.mesh=null,this.depthNear=0,this.depthFar=0}init(e,t){if(this.texture===null){let n=new _s(e.texture);(e.depthNear!==t.depthNear||e.depthFar!==t.depthFar)&&(this.depthNear=e.depthNear,this.depthFar=e.depthFar),this.texture=n}}getMesh(e){if(this.texture!==null&&this.mesh===null){let t=e.cameras[0].viewport,n=new tn({vertexShader:S2,fragmentShader:M2,uniforms:{depthColor:{value:this.texture},depthWidth:{value:t.z},depthHeight:{value:t.w}}});this.mesh=new Ot(new xs(20,20),n)}return this.mesh}reset(){this.texture=null,this.mesh=null}getDepthTexture(){return this.texture}},xl=class extends ln{constructor(e,t){super();let n=this,s=null,r=1,a=null,o="local-floor",l=1,c=null,h=null,g=null,d=null,m=null,_=null,S=typeof XRWebGLBinding<"u",p=new _l,u={},M=t.getContextAttributes(),w=null,E=null,A=[],T=[],f=new Re,v=null,N=null,I=new Ut;I.viewport=new at;let D=new Ut;D.viewport=new at;let z=[I,D],q=new qr,P=null,W=null;this.cameraAutoUpdate=!0,this.enabled=!1,this.isPresenting=!1,this.getController=function(Z){let pe=A[Z];return pe===void 0&&(pe=new zi,A[Z]=pe),pe.getTargetRaySpace()},this.getControllerGrip=function(Z){let pe=A[Z];return pe===void 0&&(pe=new zi,A[Z]=pe),pe.getGripSpace()},this.getHand=function(Z){let pe=A[Z];return pe===void 0&&(pe=new zi,A[Z]=pe),pe.getHandSpace()};function $(Z){let pe=T.indexOf(Z.inputSource);if(pe===-1)return;let xe=A[pe];xe!==void 0&&(xe.update(Z.inputSource,Z.frame,c||a),xe.dispatchEvent({type:Z.type,data:Z.inputSource}))}function G(){s.removeEventListener("select",$),s.removeEventListener("selectstart",$),s.removeEventListener("selectend",$),s.removeEventListener("squeeze",$),s.removeEventListener("squeezestart",$),s.removeEventListener("squeezeend",$),s.removeEventListener("end",G),s.removeEventListener("inputsourceschange",te);for(let Z=0;Z<A.length;Z++){let pe=T[Z];pe!==null&&(T[Z]=null,A[Z].disconnect(pe))}P=null,W=null,p.reset();for(let Z in u)delete u[Z];if(e.setRenderTarget(w),m=null,d=null,g=null,s=null,E=null,De.stop(),n.isPresenting=!1,e.setPixelRatio(v),e.setSize(f.width,f.height,!1),N!==null){let Z=N.camera;Z.fov=N.fov,Z.zoom=N.zoom,Z.updateProjectionMatrix(),N=null}n.dispatchEvent({type:"sessionend"})}this.setFramebufferScaleFactor=function(Z){r=Z,n.isPresenting===!0&&Te("WebXRManager: Cannot change framebuffer scale while presenting.")},this.setReferenceSpaceType=function(Z){o=Z,n.isPresenting===!0&&Te("WebXRManager: Cannot change reference space type while presenting.")},this.getReferenceSpace=function(){return c||a},this.setReferenceSpace=function(Z){c=Z},this.getBaseLayer=function(){return d!==null?d:m},this.getBinding=function(){return g===null&&S&&(g=new XRWebGLBinding(s,t)),g},this.getFrame=function(){return _},this.getSession=function(){return s},this.setSession=async function(Z){if(s=Z,s!==null){if(w=e.getRenderTarget(),s.addEventListener("select",$),s.addEventListener("selectstart",$),s.addEventListener("selectend",$),s.addEventListener("squeeze",$),s.addEventListener("squeezestart",$),s.addEventListener("squeezeend",$),s.addEventListener("end",G),s.addEventListener("inputsourceschange",te),M.xrCompatible!==!0&&await t.makeXRCompatible(),v=e.getPixelRatio(),e.getSize(f),S&&"createProjectionLayer"in XRWebGLBinding.prototype){let xe=null,Ae=null,me=null;M.depth&&(me=M.stencil?t.DEPTH24_STENCIL8:t.DEPTH_COMPONENT24,xe=M.stencil?Nn:Cn,Ae=M.stencil?pi:cn);let Ue={colorFormat:t.RGBA8,depthFormat:me,scaleFactor:r};g=this.getBinding(),d=g.createProjectionLayer(Ue),s.updateRenderState({layers:[d]}),e.setPixelRatio(1),e.setSize(d.textureWidth,d.textureHeight,!1),E=new Yt(d.textureWidth,d.textureHeight,{format:dn,type:Gt,depthTexture:new Ln(d.textureWidth,d.textureHeight,Ae,void 0,void 0,void 0,void 0,void 0,void 0,xe),stencilBuffer:M.stencil,colorSpace:e.outputColorSpace,samples:M.antialias?4:0,resolveDepthBuffer:d.ignoreDepthValues===!1,resolveStencilBuffer:d.ignoreDepthValues===!1,storeMultisampledDepthBuffer:d.ignoreDepthValues===!1,storeMultisampledStencilBuffer:d.ignoreDepthValues===!1})}else{let xe={antialias:M.antialias,alpha:!0,depth:M.depth,stencil:M.stencil,framebufferScaleFactor:r};m=new XRWebGLLayer(s,t,xe),s.updateRenderState({baseLayer:m}),e.setPixelRatio(1),e.setSize(m.framebufferWidth,m.framebufferHeight,!1),E=new Yt(m.framebufferWidth,m.framebufferHeight,{format:dn,type:Gt,colorSpace:e.outputColorSpace,stencilBuffer:M.stencil,resolveDepthBuffer:m.ignoreDepthValues===!1,resolveStencilBuffer:m.ignoreDepthValues===!1,storeMultisampledDepthBuffer:m.ignoreDepthValues===!1,storeMultisampledStencilBuffer:m.ignoreDepthValues===!1})}E.isXRRenderTarget=!0,this.setFoveation(l),c=null,a=await s.requestReferenceSpace(o),De.setContext(s),De.start(),n.isPresenting=!0,n.dispatchEvent({type:"sessionstart"})}},this.getEnvironmentBlendMode=function(){if(s!==null)return s.environmentBlendMode},this.getDepthTexture=function(){return p.getDepthTexture()};function te(Z){for(let pe=0;pe<Z.removed.length;pe++){let xe=Z.removed[pe],Ae=T.indexOf(xe);Ae>=0&&(T[Ae]=null,A[Ae].disconnect(xe))}for(let pe=0;pe<Z.added.length;pe++){let xe=Z.added[pe],Ae=T.indexOf(xe);if(Ae===-1){for(let Ue=0;Ue<A.length;Ue++)if(Ue>=T.length){T.push(xe),Ae=Ue;break}else if(T[Ue]===null){T[Ue]=xe,Ae=Ue;break}if(Ae===-1)break}let me=A[Ae];me&&me.connect(xe)}}function H(Z,pe){pe===null?Z.matrixWorld.copy(Z.matrix):Z.matrixWorld.multiplyMatrices(pe.matrixWorld,Z.matrix),Z.matrixWorldInverse.copy(Z.matrixWorld).invert()}this.updateCamera=function(Z){if(s===null)return;let pe=Z.near,xe=Z.far;p.texture!==null&&(p.depthNear>0&&(pe=p.depthNear),p.depthFar>0&&(xe=p.depthFar)),q.near=D.near=I.near=pe,q.far=D.far=I.far=xe,(P!==q.near||W!==q.far)&&(s.updateRenderState({depthNear:q.near,depthFar:q.far}),P=q.near,W=q.far),q.layers.mask=Z.layers.mask|6,I.layers.mask=q.layers.mask&-5,D.layers.mask=q.layers.mask&-3;let Ae=Z.parent,me=q.cameras;H(q,Ae);for(let Ue=0;Ue<me.length;Ue++)H(me[Ue],Ae);q.projectionMatrix.copy(I.projectionMatrix),q.projectionMatrixInverse.copy(I.projectionMatrixInverse),N===null&&Z.isPerspectiveCamera&&(N={camera:Z,fov:Z.fov,zoom:Z.zoom}),j(Z,q,Ae)};function j(Z,pe,xe){xe===null?Z.matrix.copy(pe.matrixWorld):(Z.matrix.copy(xe.matrixWorld),Z.matrix.invert(),Z.matrix.multiply(pe.matrixWorld)),Z.matrix.decompose(Z.position,Z.quaternion,Z.scale),Z.updateMatrixWorld(!0),Z.projectionMatrix.copy(pe.projectionMatrix),Z.projectionMatrixInverse.copy(pe.projectionMatrixInverse),Z.isPerspectiveCamera&&(Z.fov=Fi*2*Math.atan(1/Z.projectionMatrix.elements[5]),Z.zoom=1)}this.getCamera=function(){return q},this.getFoveation=function(){if(!(d===null&&m===null))return l},this.setFoveation=function(Z){l=Z,d!==null&&(d.fixedFoveation=Z),m!==null&&m.fixedFoveation!==void 0&&(m.fixedFoveation=Z)},this.hasDepthSensing=function(){return p.texture!==null},this.getDepthSensingMesh=function(){return p.getMesh(q)},this.getCameraTexture=function(Z){return u[Z]};let Q=null;function Se(Z,pe){if(h=pe.getViewerPose(c||a),_=pe,h!==null){let xe=h.views;m!==null&&(e.setRenderTargetFramebuffer(E,m.framebuffer),e.setRenderTarget(E));let Ae=!1;xe.length!==q.cameras.length&&(q.cameras.length=0,Ae=!0);for(let Ce=0;Ce<xe.length;Ce++){let Ke=xe[Ce],Qe=null;if(m!==null)Qe=m.getViewport(Ke);else{let bt=g.getViewSubImage(d,Ke);Qe=bt.viewport,Ce===0&&(e.setRenderTargetTextures(E,bt.colorTexture,bt.depthStencilTexture),e.setRenderTarget(E))}let Ge=z[Ce];Ge===void 0&&(Ge=new Ut,Ge.layers.enable(Ce),Ge.viewport=new at,z[Ce]=Ge),Ge.matrix.fromArray(Ke.transform.matrix),Ge.matrix.decompose(Ge.position,Ge.quaternion,Ge.scale),Ge.projectionMatrix.fromArray(Ke.projectionMatrix),Ge.projectionMatrixInverse.copy(Ge.projectionMatrix).invert(),Ge.viewport.set(Qe.x,Qe.y,Qe.width,Qe.height),Ce===0&&(q.matrix.copy(Ge.matrix),q.matrix.decompose(q.position,q.quaternion,q.scale)),Ae===!0&&q.cameras.push(Ge)}let me=s.enabledFeatures;if(me&&me.includes("depth-sensing")&&s.depthUsage=="gpu-optimized"&&S){g=n.getBinding();let Ce=g.getDepthInformation(xe[0]);Ce&&Ce.isValid&&Ce.texture&&p.init(Ce,s.renderState)}if(me&&me.includes("camera-access")&&S){e.state.unbindTexture(),g=n.getBinding();for(let Ce=0;Ce<xe.length;Ce++){let Ke=xe[Ce].camera;if(Ke){let Qe=u[Ke];Qe||(Qe=new _s,u[Ke]=Qe);let Ge=g.getCameraImage(Ke);Qe.sourceTexture=Ge}}}}for(let xe=0;xe<A.length;xe++){let Ae=T[xe],me=A[xe];Ae!==null&&me!==void 0&&me.update(Ae,pe,c||a)}Q&&Q(Z,pe),pe.detectedPlanes&&n.dispatchEvent({type:"planesdetected",data:pe}),_=null}let De=new Th;De.setAnimationLoop(Se),this.setAnimationLoop=function(Z){Q=Z},this.dispose=function(){}}},b2=new nt,Uh=new Ie;Uh.set(-1,0,0,0,1,0,0,0,1);function E2(i,e){function t(p,u){p.matrixAutoUpdate===!0&&p.updateMatrix(),u.value.copy(p.matrix)}function n(p,u){u.color.getRGB(p.fogColor.value,el(i)),u.isFog?(p.fogNear.value=u.near,p.fogFar.value=u.far):u.isFogExp2&&(p.fogDensity.value=u.density)}function s(p,u,M,w,E){u.isNodeMaterial?u.uniformsNeedUpdate=!1:u.isMeshBasicMaterial?r(p,u):u.isMeshLambertMaterial?(r(p,u),u.envMap&&(p.envMapIntensity.value=u.envMapIntensity)):u.isMeshToonMaterial?(r(p,u),g(p,u)):u.isMeshPhongMaterial?(r(p,u),h(p,u),u.envMap&&(p.envMapIntensity.value=u.envMapIntensity)):u.isMeshStandardMaterial?(r(p,u),d(p,u),u.isMeshPhysicalMaterial&&m(p,u,E)):u.isMeshMatcapMaterial?(r(p,u),_(p,u)):u.isMeshDepthMaterial?r(p,u):u.isMeshDistanceMaterial?(r(p,u),S(p,u)):u.isMeshNormalMaterial?r(p,u):u.isLineBasicMaterial?(a(p,u),u.isLineDashedMaterial&&o(p,u)):u.isPointsMaterial?l(p,u,M,w):u.isSpriteMaterial?c(p,u):u.isShadowMaterial?(p.color.value.copy(u.color),p.opacity.value=u.opacity):u.isShaderMaterial&&(u.uniformsNeedUpdate=!1)}function r(p,u){p.opacity.value=u.opacity,u.color&&p.diffuse.value.copy(u.color),u.emissive&&p.emissive.value.copy(u.emissive).multiplyScalar(u.emissiveIntensity),u.map&&(p.map.value=u.map,t(u.map,p.mapTransform)),u.alphaMap&&(p.alphaMap.value=u.alphaMap,t(u.alphaMap,p.alphaMapTransform)),u.bumpMap&&(p.bumpMap.value=u.bumpMap,t(u.bumpMap,p.bumpMapTransform),p.bumpScale.value=u.bumpScale,u.side===Tt&&(p.bumpScale.value*=-1)),u.normalMap&&(p.normalMap.value=u.normalMap,t(u.normalMap,p.normalMapTransform),p.normalScale.value.copy(u.normalScale),u.side===Tt&&p.normalScale.value.negate()),u.displacementMap&&(p.displacementMap.value=u.displacementMap,t(u.displacementMap,p.displacementMapTransform),p.displacementScale.value=u.displacementScale,p.displacementBias.value=u.displacementBias),u.emissiveMap&&(p.emissiveMap.value=u.emissiveMap,t(u.emissiveMap,p.emissiveMapTransform)),u.specularMap&&(p.specularMap.value=u.specularMap,t(u.specularMap,p.specularMapTransform)),u.alphaTest>0&&(p.alphaTest.value=u.alphaTest);let M=e.get(u),w=M.envMap,E=M.envMapRotation;w&&(p.envMap.value=w,p.envMapRotation.value.setFromMatrix4(b2.makeRotationFromEuler(E)).transpose(),w.isCubeTexture&&w.isRenderTargetTexture===!1&&p.envMapRotation.value.premultiply(Uh),p.reflectivity.value=u.reflectivity,p.ior.value=u.ior,p.refractionRatio.value=u.refractionRatio),u.lightMap&&(p.lightMap.value=u.lightMap,p.lightMapIntensity.value=u.lightMapIntensity,t(u.lightMap,p.lightMapTransform)),u.aoMap&&(p.aoMap.value=u.aoMap,p.aoMapIntensity.value=u.aoMapIntensity,t(u.aoMap,p.aoMapTransform))}function a(p,u){p.diffuse.value.copy(u.color),p.opacity.value=u.opacity,u.map&&(p.map.value=u.map,t(u.map,p.mapTransform))}function o(p,u){p.dashSize.value=u.dashSize,p.totalSize.value=u.dashSize+u.gapSize,p.scale.value=u.scale}function l(p,u,M,w){p.diffuse.value.copy(u.color),p.opacity.value=u.opacity,p.size.value=u.size*M,p.scale.value=w*.5,u.map&&(p.map.value=u.map,t(u.map,p.uvTransform)),u.alphaMap&&(p.alphaMap.value=u.alphaMap,t(u.alphaMap,p.alphaMapTransform)),u.alphaTest>0&&(p.alphaTest.value=u.alphaTest)}function c(p,u){p.diffuse.value.copy(u.color),p.opacity.value=u.opacity,p.rotation.value=u.rotation,u.map&&(p.map.value=u.map,t(u.map,p.mapTransform)),u.alphaMap&&(p.alphaMap.value=u.alphaMap,t(u.alphaMap,p.alphaMapTransform)),u.alphaTest>0&&(p.alphaTest.value=u.alphaTest)}function h(p,u){p.specular.value.copy(u.specular),p.shininess.value=Math.max(u.shininess,1e-4)}function g(p,u){u.gradientMap&&(p.gradientMap.value=u.gradientMap)}function d(p,u){p.metalness.value=u.metalness,u.metalnessMap&&(p.metalnessMap.value=u.metalnessMap,t(u.metalnessMap,p.metalnessMapTransform)),p.roughness.value=u.roughness,u.roughnessMap&&(p.roughnessMap.value=u.roughnessMap,t(u.roughnessMap,p.roughnessMapTransform)),u.envMap&&(p.envMapIntensity.value=u.envMapIntensity)}function m(p,u,M){p.ior.value=u.ior,u.diffuseRoughness>0&&(p.diffuseRoughness.value=u.diffuseRoughness,u.diffuseRoughnessMap&&(p.diffuseRoughnessMap.value=u.diffuseRoughnessMap,t(u.diffuseRoughnessMap,p.diffuseRoughnessMapTransform))),u.sheen>0&&(p.sheenColor.value.copy(u.sheenColor).multiplyScalar(u.sheen),p.sheenRoughness.value=u.sheenRoughness,u.sheenColorMap&&(p.sheenColorMap.value=u.sheenColorMap,t(u.sheenColorMap,p.sheenColorMapTransform)),u.sheenRoughnessMap&&(p.sheenRoughnessMap.value=u.sheenRoughnessMap,t(u.sheenRoughnessMap,p.sheenRoughnessMapTransform))),u.clearcoat>0&&(p.clearcoat.value=u.clearcoat,p.clearcoatRoughness.value=u.clearcoatRoughness,u.clearcoatMap&&(p.clearcoatMap.value=u.clearcoatMap,t(u.clearcoatMap,p.clearcoatMapTransform)),u.clearcoatRoughnessMap&&(p.clearcoatRoughnessMap.value=u.clearcoatRoughnessMap,t(u.clearcoatRoughnessMap,p.clearcoatRoughnessMapTransform)),u.clearcoatNormalMap&&(p.clearcoatNormalMap.value=u.clearcoatNormalMap,t(u.clearcoatNormalMap,p.clearcoatNormalMapTransform),p.clearcoatNormalScale.value.copy(u.clearcoatNormalScale),u.side===Tt&&p.clearcoatNormalScale.value.negate())),u.dispersion>0&&(p.dispersion.value=u.dispersion),u.retroreflectivity>0&&(p.retroreflectivity.value=u.retroreflectivity),u.iridescence>0&&(p.iridescence.value=u.iridescence,p.iridescenceIOR.value=u.iridescenceIOR,p.iridescenceThicknessMinimum.value=u.iridescenceThicknessMinimum,p.iridescenceThicknessMaximum.value=u.iridescenceThicknessMaximum,u.iridescenceMap&&(p.iridescenceMap.value=u.iridescenceMap,t(u.iridescenceMap,p.iridescenceMapTransform)),u.iridescenceThicknessMap&&(p.iridescenceThicknessMap.value=u.iridescenceThicknessMap,t(u.iridescenceThicknessMap,p.iridescenceThicknessMapTransform))),u.transmission>0&&(p.transmission.value=u.transmission,p.transmissionSamplerMap.value=M.texture,p.transmissionSamplerSize.value.set(M.width,M.height),u.transmissionMap&&(p.transmissionMap.value=u.transmissionMap,t(u.transmissionMap,p.transmissionMapTransform)),p.thickness.value=u.thickness,u.thicknessMap&&(p.thicknessMap.value=u.thicknessMap,t(u.thicknessMap,p.thicknessMapTransform)),p.attenuationDistance.value=u.attenuationDistance,p.attenuationColor.value.copy(u.attenuationColor)),u.anisotropy>0&&(p.anisotropyVector.value.set(u.anisotropy*Math.cos(u.anisotropyRotation),u.anisotropy*Math.sin(u.anisotropyRotation)),u.anisotropyMap&&(p.anisotropyMap.value=u.anisotropyMap,t(u.anisotropyMap,p.anisotropyMapTransform))),p.specularIntensity.value=u.specularIntensity,p.specularColor.value.copy(u.specularColor),u.specularColorMap&&(p.specularColorMap.value=u.specularColorMap,t(u.specularColorMap,p.specularColorMapTransform)),u.specularIntensityMap&&(p.specularIntensityMap.value=u.specularIntensityMap,t(u.specularIntensityMap,p.specularIntensityMapTransform))}function _(p,u){u.matcap&&(p.matcap.value=u.matcap)}function S(p,u){let M=e.get(u).light;p.referencePosition.value.setFromMatrixPosition(M.matrixWorld),p.nearDistance.value=M.shadow.camera.near,p.farDistance.value=M.shadow.camera.far}return{refreshFogUniforms:n,refreshMaterialUniforms:s}}function T2(i,e,t,n){let s={},r={};function a(M,w){let E=w.program;n.uniformBlockBinding(M,E,s[M.id])}function o(M,w){let E=s[M.id];E===void 0&&(_(M),E=l(M),s[M.id]=E,M.addEventListener("dispose",p));let A=w.program;n.updateUBOMapping(M,A);let T=e.render.frame;r[M.id]!==T&&(c(M),r[M.id]=T)}function l(M){let w=i.createBuffer(),E=M.__size,A=M.usage;return i.bindBuffer(i.UNIFORM_BUFFER,w),i.bufferData(i.UNIFORM_BUFFER,E,A),i.bindBuffer(i.UNIFORM_BUFFER,null),w}function c(M){let w=s[M.id],E=M.uniforms,A=M.__cache;i.bindBuffer(i.UNIFORM_BUFFER,w);for(let T=0,f=E.length;T<f;T++){let v=E[T];if(Array.isArray(v))for(let N=0,I=v.length;N<I;N++)h(v[N],T,N,A);else h(v,T,0,A)}i.bindBuffer(i.UNIFORM_BUFFER,null)}function h(M,w,E,A){if(d(M,w,E,A)===!0){let T=M.__offset,f=M.value;if(Array.isArray(f)){let v=0;for(let N=0;N<f.length;N++){let I=f[N],D=S(I,!0);g(I,M.__data,v),v+=D.storage/Float32Array.BYTES_PER_ELEMENT}}else g(f,M.__data,0);i.bufferSubData(i.UNIFORM_BUFFER,T,M.__data)}}function g(M,w,E){typeof M=="number"||typeof M=="boolean"?w[E]=M:M.isMatrix3?(w[E]=M.elements[0],w[E+1]=M.elements[1],w[E+2]=M.elements[2],w[E+3]=0,w[E+4]=M.elements[3],w[E+5]=M.elements[4],w[E+6]=M.elements[5],w[E+7]=0,w[E+8]=M.elements[6],w[E+9]=M.elements[7],w[E+10]=M.elements[8],w[E+11]=0):ArrayBuffer.isView(M)?w.set(M.subarray(0,w.length-E),E):M.toArray(w,E)}function d(M,w,E,A){let T=M.value,f=w+"_"+E;if(Array.isArray(T)){A[f]===void 0&&(A[f]=[]);let v=A[f],N=!1;for(let I=0;I<T.length;I++)m(T[I],v,I)===!0&&(N=!0);return N}return m(T,A,f)}function m(M,w,E){if(w[E]===void 0)return typeof M=="number"||typeof M=="boolean"?w[E]=M:ArrayBuffer.isView(M)?w[E]=M.slice():w[E]=M.clone(),!0;{let A=w[E];if(typeof M=="number"||typeof M=="boolean"){if(A!==M)return w[E]=M,!0}else{if(ArrayBuffer.isView(M))return!0;if(A.equals(M)===!1)return A.copy(M),!0}}return!1}function _(M){let w=M.uniforms,E=0,A=16;for(let f=0,v=w.length;f<v;f++){let N=Array.isArray(w[f])?w[f]:[w[f]];for(let I=0,D=N.length;I<D;I++){let z=N[I],q=Array.isArray(z.value)?z.value:[z.value],P=Array.isArray(w[f])||Array.isArray(z.value),W=E;for(let G=0,te=q.length;G<te;G++){let H=q[G],j=S(H,P),Q=E%A,Se=Q%j.boundary,De=Q+Se;E+=Se,De!==0&&A-De<j.storage&&(E+=A-De),G===0&&(W=E),E+=j.storage}let $=z.type==="int"?Int32Array:z.type==="uint"?Uint32Array:Float32Array;z.__data=new $((E-W)/Float32Array.BYTES_PER_ELEMENT),z.__offset=W}}let T=E%A;return T>0&&(E+=A-T),M.__size=E,M.__cache={},this}function S(M,w){let E={boundary:0,storage:0};return typeof M=="number"||typeof M=="boolean"?(E.boundary=4,E.storage=4):M.isVector2?(E.boundary=8,E.storage=8):M.isVector3||M.isColor?(E.boundary=16,E.storage=12):M.isVector4?(E.boundary=16,E.storage=16):M.isMatrix3?(E.boundary=16,E.storage=48):M.isMatrix4?(E.boundary=16,E.storage=64):M.isTexture?Te("WebGLRenderer: Texture samplers can not be part of an uniforms group."):ArrayBuffer.isView(M)?(E.boundary=16,E.storage=M.byteLength):Te("WebGLRenderer: Unsupported uniform value type.",M),w===!0&&(E.boundary=16,E.storage=Math.ceil(E.storage/16)*16),E}function p(M){let w=M.target;w.removeEventListener("dispose",p),i.deleteBuffer(s[w.id]),delete s[w.id],delete r[w.id]}function u(){for(let M in s)i.deleteBuffer(s[M]);s={},r={}}return{bind:a,update:o,dispose:u}}var A2=new Uint16Array([12469,15057,12620,14925,13266,14620,13807,14376,14323,13990,14545,13625,14713,13328,14840,12882,14931,12528,14996,12233,15039,11829,15066,11525,15080,11295,15085,10976,15082,10705,15073,10495,13880,14564,13898,14542,13977,14430,14158,14124,14393,13732,14556,13410,14702,12996,14814,12596,14891,12291,14937,11834,14957,11489,14958,11194,14943,10803,14921,10506,14893,10278,14858,9960,14484,14039,14487,14025,14499,13941,14524,13740,14574,13468,14654,13106,14743,12678,14818,12344,14867,11893,14889,11509,14893,11180,14881,10751,14852,10428,14812,10128,14765,9754,14712,9466,14764,13480,14764,13475,14766,13440,14766,13347,14769,13070,14786,12713,14816,12387,14844,11957,14860,11549,14868,11215,14855,10751,14825,10403,14782,10044,14729,9651,14666,9352,14599,9029,14967,12835,14966,12831,14963,12804,14954,12723,14936,12564,14917,12347,14900,11958,14886,11569,14878,11247,14859,10765,14828,10401,14784,10011,14727,9600,14660,9289,14586,8893,14508,8533,15111,12234,15110,12234,15104,12216,15092,12156,15067,12010,15028,11776,14981,11500,14942,11205,14902,10752,14861,10393,14812,9991,14752,9570,14682,9252,14603,8808,14519,8445,14431,8145,15209,11449,15208,11451,15202,11451,15190,11438,15163,11384,15117,11274,15055,10979,14994,10648,14932,10343,14871,9936,14803,9532,14729,9218,14645,8742,14556,8381,14461,8020,14365,7603,15273,10603,15272,10607,15267,10619,15256,10631,15231,10614,15182,10535,15118,10389,15042,10167,14963,9787,14883,9447,14800,9115,14710,8665,14615,8318,14514,7911,14411,7507,14279,7198,15314,9675,15313,9683,15309,9712,15298,9759,15277,9797,15229,9773,15166,9668,15084,9487,14995,9274,14898,8910,14800,8539,14697,8234,14590,7790,14479,7409,14367,7067,14178,6621,15337,8619,15337,8631,15333,8677,15325,8769,15305,8871,15264,8940,15202,8909,15119,8775,15022,8565,14916,8328,14804,8009,14688,7614,14569,7287,14448,6888,14321,6483,14088,6171,15350,7402,15350,7419,15347,7480,15340,7613,15322,7804,15287,7973,15229,8057,15148,8012,15046,7846,14933,7611,14810,7357,14682,7069,14552,6656,14421,6316,14251,5948,14007,5528,15356,5942,15356,5977,15353,6119,15348,6294,15332,6551,15302,6824,15249,7044,15171,7122,15070,7050,14949,6861,14818,6611,14679,6349,14538,6067,14398,5651,14189,5311,13935,4958,15359,4123,15359,4153,15356,4296,15353,4646,15338,5160,15311,5508,15263,5829,15188,6042,15088,6094,14966,6001,14826,5796,14678,5543,14527,5287,14377,4985,14133,4586,13869,4257,15360,1563,15360,1642,15358,2076,15354,2636,15341,3350,15317,4019,15273,4429,15203,4732,15105,4911,14981,4932,14836,4818,14679,4621,14517,4386,14359,4156,14083,3795,13808,3437,15360,122,15360,137,15358,285,15355,636,15344,1274,15322,2177,15281,2765,15215,3223,15120,3451,14995,3569,14846,3567,14681,3466,14511,3305,14344,3121,14037,2800,13753,2467,15360,0,15360,1,15359,21,15355,89,15346,253,15325,479,15287,796,15225,1148,15133,1492,15008,1749,14856,1882,14685,1886,14506,1783,14324,1608,13996,1398,13702,1183]),yn=null;function w2(){return yn===null&&(yn=new Rr(A2,16,16,Qn,un),yn.name="DFG_LUT",yn.minFilter=Ft,yn.magFilter=Ft,yn.wrapS=gn,yn.wrapT=gn,yn.generateMipmaps=!1,yn.needsUpdate=!0),yn}var Ba=class{constructor(e={}){let{canvas:t=Zc(),context:n=null,depth:s=!0,stencil:r=!1,alpha:a=!1,antialias:o=!1,premultipliedAlpha:l=!0,preserveDrawingBuffer:c=!1,powerPreference:h="default",failIfMajorPerformanceCaveat:g=!1,reversedDepthBuffer:d=!1,outputBufferType:m=Gt}=e;this.isWebGLRenderer=!0;let _;if(n!==null){if(typeof WebGLRenderingContext<"u"&&n instanceof WebGLRenderingContext)throw new Error("THREE.WebGLRenderer: WebGL 1 is not supported since r163.");_=n.getContextAttributes().alpha}else _=a;let S=m,p=new Set([ia,na,ta]),u=new Set([Gt,cn,Yi,pi,Qr,ea]),M=new Uint32Array(4),w=new Int32Array(4),E={textures:[],min:[],max:[],resolution:[]},A=null,T=null,f=[],v=[],N=null;this.domElement=t,this.debug={checkShaderErrors:!0,diagnostics:{keywords:!1},onShaderError:null},this.autoClear=!0,this.autoClearColor=!0,this.autoClearDepth=!0,this.autoClearStencil=!0,this.sortObjects=!0,this.clippingPlanes=[],this.localClippingEnabled=!1,this.toneMapping=xn,this.toneMappingExposure=1,this.transmissionResolutionScale=1;let I=this,D=!1,z=null,q=null,P=null,W=null;this._outputColorSpace=Nt;let $=0,G=0,te=null,H=-1,j=null,Q=new at,Se=new at,De=null,Z=new Be(0),pe=0,xe=t.width,Ae=t.height,me=1,Ue=null,ht=null,Ce=new at(0,0,xe,Ae),Ke=new at(0,0,xe,Ae),Qe=!1,Ge=new qn,bt=new Cr,ft=!1,Bt=!1,ot=new nt,pn=new U,xt=new at,Jt={background:null,fog:null,environment:null,overrideMaterial:null,isScene:!0},$t=!1;function Kt(){return te===null?me:1}let L=n;function jt(y,C){return t.getContext(y,C)}let st,rt,ue,pt,we,Le,b,x,O,ee,K,se,ce,X,Y,ae,R,J,V,oe,ie,re,be;try{let y={alpha:!0,depth:s,stencil:r,antialias:o,premultipliedAlpha:l,preserveDrawingBuffer:c,powerPreference:h,failIfMajorPerformanceCaveat:g};if("setAttribute"in t&&t.setAttribute("data-engine",`three.js r${"187"}`),t.addEventListener("webglcontextlost",Ee,!1),t.addEventListener("webglcontextrestored",Fe,!1),t.addEventListener("webglcontextcreationerror",de,!1),L===null){let C="webgl2";if(L=jt(C,y),L===null)throw jt(C)?new Error("THREE.WebGLRenderer: Error creating WebGL context with your selected attributes."):new Error("THREE.WebGLRenderer: Error creating WebGL context.")}Oe()}catch(y){throw t.removeEventListener("webglcontextlost",Ee,!1),t.removeEventListener("webglcontextrestored",Fe,!1),t.removeEventListener("webglcontextcreationerror",de,!1),Pe("WebGLRenderer: "+y.message),y}function Oe(){st=new Bf(L),st.init(),ie=new v2(L,st),rt=new wf(L,st,e,ie),ue=new x2(L,st),rt.reversedDepthBuffer&&d&&ue.buffers.depth.setReversed(!0),q=L.createFramebuffer(),P=L.createFramebuffer(),W=L.createFramebuffer(),pt=new Gf(L),we=new s2,Le=new y2(L,st,ue,we,rt,ie,pt),b=new Of(I),x=new V1(L),re=new Tf(L,x),O=new zf(L,x,pt,re),ee=new Hf(L,O,x,re,pt),J=new Vf(L,rt,Le),Y=new Rf(we),K=new i2(I,b,st,rt,re,Y),se=new E2(I,we),ce=new a2,X=new d2(st),R=new Ef(I,b,ue,ee,_,l),ae=new _2(I,ee,rt),be=new T2(L,pt,rt,ue),V=new Af(L,st,pt),oe=new kf(L,st,pt),pt.programs=K.programs,I.capabilities=rt,I.extensions=st,I.properties=we,I.renderLists=ce,I.shadowMap=ae,I.state=ue,I.info=pt}S!==Gt&&(N=new Xf(S,t.width,t.height,o,s,r));let ne=new xl(I,L);this.xr=ne,this.getContext=function(){return L},this.getContextAttributes=function(){return L.getContextAttributes()},this.forceContextLoss=function(){let y=st.get("WEBGL_lose_context");y&&y.loseContext()},this.forceContextRestore=function(){let y=st.get("WEBGL_lose_context");y&&y.restoreContext()},this.getPixelRatio=function(){return me},this.setPixelRatio=function(y){y!==void 0&&(me=y,this.setSize(xe,Ae,!1))},this.getSize=function(y){return y.set(xe,Ae)},this.setSize=function(y,C,k=!0){if(ne.isPresenting){Te("WebGLRenderer: Can't change size while VR device is presenting.");return}xe=y,Ae=C,t.width=Math.floor(y*me),t.height=Math.floor(C*me),k===!0&&(t.style.width=y+"px",t.style.height=C+"px"),N!==null&&N.setSize(t.width,t.height),this.setViewport(0,0,y,C)},this.getDrawingBufferSize=function(y){return y.set(xe*me,Ae*me).floor()},this.setDrawingBufferSize=function(y,C,k){xe=y,Ae=C,me=k,t.width=Math.floor(y*k),t.height=Math.floor(C*k),this.setViewport(0,0,y,C)},this.setEffects=function(y){if(S===Gt){Pe("WebGLRenderer: setEffects() requires outputBufferType set to HalfFloatType or FloatType.");return}if(y){for(let C=0;C<y.length;C++)if(y[C].isOutputPass===!0){Te("WebGLRenderer: OutputPass is not needed in setEffects(). Tone mapping and color space conversion are applied automatically.");break}}N.setEffects(y||[])},this.getCurrentViewport=function(y){return y.copy(Q)},this.getViewport=function(y){return y.copy(Ce)},this.setViewport=function(y,C,k,F){y.isVector4?Ce.set(y.x,y.y,y.z,y.w):Ce.set(y,C,k,F),ue.viewport(Q.copy(Ce).multiplyScalar(Kt()).round())},this.getScissor=function(y){return y.copy(Ke)},this.setScissor=function(y,C,k,F){y.isVector4?Ke.set(y.x,y.y,y.z,y.w):Ke.set(y,C,k,F),ue.scissor(Se.copy(Ke).multiplyScalar(Kt()).round())},this.getScissorTest=function(){return Qe},this.setScissorTest=function(y){ue.setScissorTest(Qe=y)},this.setOpaqueSort=function(y){Ue=y},this.setTransparentSort=function(y){ht=y},this.getClearColor=function(y){return y.copy(R.getClearColor())},this.setClearColor=function(){R.setClearColor(...arguments)},this.getClearAlpha=function(){return R.getClearAlpha()},this.setClearAlpha=function(){R.setClearAlpha(...arguments)},this.clear=function(y=!0,C=!0,k=!0){let F=0;if(y){let B=!1;if(te!==null){let he=te.texture.format;B=p.has(he)}if(B){let he=te.texture.type,_e=u.has(he),le=R.getClearColor(),ge=R.getClearAlpha(),Me=le.r,Ne=le.g,Ve=le.b;_e?(M[0]=Me,M[1]=Ne,M[2]=Ve,M[3]=ge,L.clearBufferuiv(L.COLOR,0,M)):(w[0]=Me,w[1]=Ne,w[2]=Ve,w[3]=ge,L.clearBufferiv(L.COLOR,0,w))}else F|=L.COLOR_BUFFER_BIT}C&&(F|=L.DEPTH_BUFFER_BIT,this.state.buffers.depth.setMask(!0)),k&&(F|=L.STENCIL_BUFFER_BIT,this.state.buffers.stencil.setMask(4294967295)),F!==0&&L.clear(F)},this.clearColor=function(){this.clear(!0,!1,!1)},this.clearDepth=function(){this.clear(!1,!0,!1)},this.clearStencil=function(){this.clear(!1,!1,!0)},this.setNodesHandler=function(y){y.setRenderer(this),z=y},this.dispose=function(){t.removeEventListener("webglcontextlost",Ee,!1),t.removeEventListener("webglcontextrestored",Fe,!1),t.removeEventListener("webglcontextcreationerror",de,!1),R.dispose(),ce.dispose(),X.dispose(),Le.dispose(),we.dispose(),b.dispose(),ee.dispose(),O.dispose(),re.dispose(),be.dispose(),K.dispose(),ne.dispose(),ne.removeEventListener("sessionstart",Cl),ne.removeEventListener("sessionend",Pl),ei.stop()};function Ee(y){y.preventDefault(),Jo("WebGLRenderer: Context Lost."),D=!0}function Fe(){Jo("WebGLRenderer: Context Restored."),D=!1;let y=pt.autoReset,C=ae.enabled,k=ae.autoUpdate,F=ae.needsUpdate,B=ae.type;Oe(),pt.autoReset=y,ae.enabled=C,ae.autoUpdate=k,ae.needsUpdate=F,ae.type=B}function de(y){Pe("WebGLRenderer: A WebGL context could not be created. Reason: ",y.statusMessage)}function je(y){let C=y.target;C.removeEventListener("dispose",je),yt(C)}function yt(y){Fn(y),we.remove(y)}function Fn(y){let C=we.get(y).programs;C!==void 0&&(C.forEach(function(k){K.releaseProgram(k)}),y.isShaderMaterial&&K.releaseShaderCache(y))}this.renderBufferDirect=function(y,C,k,F,B,he){C===null&&(C=Jt);let _e=B.isMesh&&B.matrixWorld.determinantAffine()<0,le=Hh(y,C,k,F,B);ue.setMaterial(F,_e);let ge=k.index,Me=1;if(F.wireframe===!0){if(ge=O.getWireframeAttribute(k),ge===void 0)return;Me=2}let Ne=k.drawRange,Ve=k.attributes.position,ye=Ne.start*Me,He=(Ne.start+Ne.count)*Me;he!==null&&(ye=Math.max(ye,he.start*Me),He=Math.min(He,(he.start+he.count)*Me)),ge!==null?(ye=Math.max(ye,0),He=Math.min(He,ge.count)):Ve!=null&&(ye=Math.max(ye,0),He=Math.min(He,Ve.count));let ut=He-ye;if(ut<0||ut===1/0)return;re.setup(B,F,le,k,ge);let tt,et=V;if(ge!==null&&(tt=x.get(ge),et=oe,et.setIndex(tt)),B.isMesh)F.wireframe===!0?(ue.setLineWidth(F.wireframeLinewidth*Kt()),et.setMode(L.LINES)):et.setMode(L.TRIANGLES);else if(B.isLine){let At=F.linewidth;At===void 0&&(At=1),ue.setLineWidth(At*Kt()),B.isLineSegments?et.setMode(L.LINES):B.isLineLoop?et.setMode(L.LINE_LOOP):et.setMode(L.LINE_STRIP)}else B.isPoints?et.setMode(L.POINTS):B.isSprite&&et.setMode(L.TRIANGLES);if(B.isBatchedMesh)if(st.get("WEBGL_multi_draw"))et.renderMultiDraw(B._multiDrawStarts,B._multiDrawCounts,B._multiDrawCount);else{let At=B._multiDrawStarts,ve=B._multiDrawCounts,Dt=B._multiDrawCount,Ye=ge?x.get(ge).bytesPerElement:1,ti=we.get(F).currentProgram.getUniforms();for(let wt=0;wt<Dt;wt++)ti.setValue(L,"_gl_DrawID",wt),et.render(At[wt]/Ye,ve[wt])}else if(B.isInstancedMesh)et.renderInstances(ye,ut,B.count);else if(k.isInstancedBufferGeometry){let At=k._maxInstanceCount!==void 0?k._maxInstanceCount:1/0,ve=Math.min(k.instanceCount,At);et.renderInstances(ye,ut,ve)}else et.render(ye,ut)};function Rl(y,C,k,F){z!==null&&y.isNodeMaterial&&z.setObject(F,y),ft===!0&&Y.setState(y,k,!1),y.transparent===!0&&y.side===nn&&y.forceSinglePass===!1?(y.side=Tt,y.needsUpdate=!0,Ki(y,C,F),y.side=jn,y.needsUpdate=!0,Ki(y,C,F),y.side=nn):Ki(y,C,F)}this.compile=function(y,C,k=null){k===null&&(k=y),z!==null&&z.renderStart(y,C,k),T=X.get(k),T.init(C),v.push(T),k.traverseVisible(function(B){B.isLight&&B.layers.test(C.layers)&&(T.pushLight(B),B.castShadow&&T.pushShadow(B))}),y!==k&&y.traverseVisible(function(B){B.isLight&&B.layers.test(C.layers)&&(T.pushLight(B),B.castShadow&&T.pushShadow(B))}),T.setupLights(),z!==null&&z.updateLights(T.state.lightsArray),Bt=this.localClippingEnabled,ft=Y.init(this.clippingPlanes,Bt),ft===!0&&Y.setGlobalState(this.clippingPlanes,C),z!==null&&ae.render(T.state.shadowsArray,k,C);let F=new Set;return y.traverse(function(B){if(!(B.isMesh||B.isPoints||B.isLine||B.isSprite))return;let he=B.material;if(he)if(Array.isArray(he))for(let _e=0;_e<he.length;_e++){let le=he[_e];Rl(le,k,C,B),F.add(le)}else Rl(he,k,C,B),F.add(he)}),T=v.pop(),z!==null&&z.renderEnd(),F},this.compileAsync=function(y,C,k=null){let F=this.compile(y,C,k);return new Promise(B=>{function he(){if(F.forEach(function(_e){let ge=we.get(_e).currentProgram;(ge===void 0||ge.isReady())&&F.delete(_e)}),F.size===0){B(y);return}setTimeout(he,10)}st.get("KHR_parallel_shader_compile")!==null?he():setTimeout(he,10)})};let qa=null;function Gh(y){qa&&qa(y)}function Cl(){ei.stop()}function Pl(){ei.start()}let ei=new Th;ei.setAnimationLoop(Gh),typeof self<"u"&&ei.setContext(self),this.setAnimationLoop=function(y){qa=y,ne.setAnimationLoop(y),y===null?ei.stop():ei.start()},ne.addEventListener("sessionstart",Cl),ne.addEventListener("sessionend",Pl),this.render=function(y,C){if(C!==void 0&&C.isCamera!==!0){Pe("WebGLRenderer.render: camera is not an instance of THREE.Camera.");return}if(D===!0)return;z!==null&&z.renderStart(y,C);let k=ne.enabled===!0&&ne.isPresenting===!0,F=N!==null&&(te===null||k)&&N.begin(I,te);if(y.matrixWorldAutoUpdate===!0&&y.updateMatrixWorld(),C.parent===null&&C.matrixWorldAutoUpdate===!0&&C.updateMatrixWorld(),ne.enabled===!0&&ne.isPresenting===!0&&(N===null||N.isCompositing()===!1)&&(ne.cameraAutoUpdate===!0&&ne.updateCamera(C),C=ne.getCamera()),y.isScene===!0&&y.onBeforeRender(I,y,C,te),T=X.get(y,v.length),T.init(C),T.state.textureUnits=Le.getTextureUnits(),v.push(T),ot.multiplyMatrices(C.projectionMatrix,C.matrixWorldInverse),C.isArrayCamera?bt.setFromArrayCamera(C):Ge.setFromProjectionMatrix(ot,en,C.reversedDepth),Bt=this.localClippingEnabled,ft=Y.init(this.clippingPlanes,Bt),A=ce.get(y,f.length),A.init(),f.push(A),this.info.render.frame++,ne.enabled===!0&&ne.isPresenting===!0){let _e=I.xr.getDepthSensingMesh();_e!==null&&Ya(_e,C,-1/0,I.sortObjects)}Ya(y,C,0,I.sortObjects),A.finish(),z!==null&&z.updateLights(T.state.lightsArray),I.sortObjects===!0&&A.sort(Ue,ht),$t=ne.enabled===!1||ne.isPresenting===!1||ne.hasDepthSensing()===!1,$t&&R.addToRenderList(A,y),this.info.autoReset===!0&&this.info.reset(),ft===!0&&Y.beginShadows();let B=T.state.shadowsArray;if(ae.render(B,y,C),ft===!0&&Y.endShadows(),(F&&N.hasRenderPass())===!1){let _e=A.opaque,le=A.transmissive;if(T.setupLights(),C.isArrayCamera){let ge=C.cameras;if(le.length>0)for(let Me=0,Ne=ge.length;Me<Ne;Me++){let Ve=ge[Me];Ll(_e,le,y,Ve)}$t&&R.render(y);for(let Me=0,Ne=ge.length;Me<Ne;Me++){let Ve=ge[Me];Il(A,y,Ve,Ve.viewport)}}else le.length>0&&Ll(_e,le,y,C),$t&&R.render(y),Il(A,y,C)}te!==null&&G===0&&(Le.updateMultisampleRenderTarget(te),Le.updateRenderTargetMipmap(te)),F&&N.end(I),y.isScene===!0&&y.onAfterRender(I,y,C),re.resetDefaultState(),H=-1,j=null,v.pop(),v.length>0?(T=v[v.length-1],Le.setTextureUnits(T.state.textureUnits),ft===!0&&Y.setGlobalState(I.clippingPlanes,T.state.camera)):T=null,f.pop(),f.length>0?A=f[f.length-1]:A=null,z!==null&&z.renderEnd()};function Ya(y,C,k,F){if(y.visible===!1)return;if(y.layers.test(C.layers)){if(y.isGroup)k=y.renderOrder;else if(y.isLOD)y.autoUpdate===!0&&y.update(C);else if(y.isLight)T.pushLight(y),y.castShadow&&T.pushShadow(y);else if(y.isSprite){let _e=C.isArrayCamera?bt:Ge;if(!y.frustumCulled||y.intersectsFrustum(_e)){F&&xt.setFromMatrixPosition(y.matrixWorld).applyMatrix4(ot);let le=ee.update(y),ge=y.material;ge.visible&&A.push(y,le,ge,k,xt.z,null,C)}}else if(y.isMesh||y.isLine||y.isPoints){let _e=C.isArrayCamera?bt:Ge;if(!y.frustumCulled||y.intersectsFrustum(_e)){let le=ee.update(y),ge=y.material;if(F&&(y.boundingSphere!==void 0?(y.boundingSphere===null&&y.computeBoundingSphere(),xt.copy(y.boundingSphere.center)):(le.boundingSphere===null&&le.computeBoundingSphere(),xt.copy(le.boundingSphere.center)),xt.applyMatrix4(y.matrixWorld).applyMatrix4(ot)),Array.isArray(ge)){let Me=le.groups;for(let Ne=0,Ve=Me.length;Ne<Ve;Ne++){let ye=Me[Ne],He=ge[ye.materialIndex];He&&He.visible&&A.push(y,le,He,k,xt.z,ye,C)}}else ge.visible&&A.push(y,le,ge,k,xt.z,null,C)}}}let he=y.children;for(let _e=0,le=he.length;_e<le;_e++)Ya(he[_e],C,k,F)}function Il(y,C,k,F){let{opaque:B,transmissive:he,transparent:_e}=y;T.setupLightsView(k),ft===!0&&Y.setGlobalState(I.clippingPlanes,k),F&&ue.viewport(Q.copy(F)),B.length>0&&Hs(B,C,k),he.length>0&&Hs(he,C,k),_e.length>0&&Hs(_e,C,k),ue.buffers.depth.setTest(!0),ue.buffers.depth.setMask(!0),ue.buffers.color.setMask(!0),ue.setPolygonOffset(!1)}function Ll(y,C,k,F){if((k.isScene===!0?k.overrideMaterial:null)!==null)return;if(T.state.transmissionRenderTarget[F.id]===void 0){let ye=st.has("EXT_color_buffer_half_float")||st.has("EXT_color_buffer_float");T.state.transmissionRenderTarget[F.id]=new Yt(1,1,{generateMipmaps:!0,type:ye?un:Gt,minFilter:Dn,samples:Math.max(4,rt.samples),stencilBuffer:r,resolveDepthBuffer:!1,resolveStencilBuffer:!1,storeMultisampledDepthBuffer:!1,storeMultisampledStencilBuffer:!1,colorSpace:We.workingColorSpace})}let he=T.state.transmissionRenderTarget[F.id],_e=F.viewport||Q;he.setSize(_e.z*I.transmissionResolutionScale,_e.w*I.transmissionResolutionScale);let le=I.getRenderTarget(),ge=I.getActiveCubeFace(),Me=I.getActiveMipmapLevel();I.setRenderTarget(he),I.getClearColor(Z),pe=I.getClearAlpha(),pe<1&&I.setClearColor(16777215,.5),I.clear(),$t&&R.render(k);let Ne=I.toneMapping;I.toneMapping=xn;let Ve=F.viewport;if(F.viewport!==void 0&&(F.viewport=void 0),T.setupLightsView(F),ft===!0&&Y.setGlobalState(I.clippingPlanes,F),Hs(y,k,F),Le.updateMultisampleRenderTarget(he),Le.updateRenderTargetMipmap(he),st.has("WEBGL_multisampled_render_to_texture")===!1){let ye=!1;for(let He=0,ut=C.length;He<ut;He++){let tt=C[He],{object:et,geometry:At,material:ve,group:Dt}=tt;if(ve.side===nn&&et.layers.test(F.layers)){let Ye=ve.side;ve.side=Tt,ve.needsUpdate=!0,Dl(et,k,F,At,ve,Dt),ve.side=Ye,ve.needsUpdate=!0,ye=!0}}ye===!0&&(Le.updateMultisampleRenderTarget(he),Le.updateRenderTargetMipmap(he))}I.setRenderTarget(le,ge,Me),I.setClearColor(Z,pe),Ve!==void 0&&(F.viewport=Ve),I.toneMapping=Ne}function Hs(y,C,k){let F=C.isScene===!0?C.overrideMaterial:null;for(let B=0,he=y.length;B<he;B++){let _e=y[B],{object:le,geometry:ge,group:Me}=_e,Ne=_e.material;Ne.allowOverride===!0&&F!==null&&(Ne=F),le.layers.test(k.layers)&&Dl(le,C,k,ge,Ne,Me)}}function Dl(y,C,k,F,B,he){z!==null&&B.isNodeMaterial&&z.setObject(y,B),y.onBeforeRender(I,C,k,F,B,he),y.modelViewMatrix.multiplyMatrices(k.matrixWorldInverse,y.matrixWorld),y.normalMatrix.getNormalMatrix(y.modelViewMatrix),B.onBeforeRender(I,C,k,F,y,he),B.transparent===!0&&B.side===nn&&B.forceSinglePass===!1?(B.side=Tt,B.needsUpdate=!0,I.renderBufferDirect(k,C,F,B,y,he),B.side=jn,B.needsUpdate=!0,I.renderBufferDirect(k,C,F,B,y,he),B.side=nn):I.renderBufferDirect(k,C,F,B,y,he),y.onAfterRender(I,C,k,F,B,he)}function Nl(y){let C=0;for(let k of y)k.texture!==null&&C++;return C}function Ki(y,C,k){C.isScene!==!0&&(C=Jt);let F=we.get(y),B=T.state.lights,he=T.state.shadowsArray,_e=B.state.version,le=K.getParameters(y,B.state,he,C,k,T.state.lightProbeGridArray),ge=K.getProgramCacheKey(le),Me=F.programs;F.environment=y.isMeshStandardMaterial||y.isMeshLambertMaterial||y.isMeshPhongMaterial?C.environment:null,F.fog=C.fog;let Ne=y.isMeshStandardMaterial||y.isMeshLambertMaterial&&!y.envMap||y.isMeshPhongMaterial&&!y.envMap;F.envMap=b.get(y.envMap||F.environment,Ne),F.envMapRotation=F.environment!==null&&y.envMap===null?C.environmentRotation:y.envMapRotation,Me===void 0&&(y.addEventListener("dispose",je),Me=new Map,F.programs=Me,F.programVariants=new Map);let Ve=Me.get(ge);if(Ve!==void 0){if(F.currentProgram===Ve&&F.lightsStateVersion===_e)return Fl(y,le),Ve}else le.uniforms=K.getUniforms(y),z!==null&&y.isNodeMaterial&&z.build(y,k,le),y.onBeforeCompile(le,I),Ve=K.acquireProgram(le,ge),Me.set(ge,Ve),F.uniforms=le.uniforms;let ye=F.uniforms;return(!y.isShaderMaterial&&!y.isRawShaderMaterial||y.clipping===!0)&&(ye.clippingPlanes=Y.uniform),Fl(y,le),F.needsLights=Xh(y),F.lightsStateVersion=_e,F.needsLights&&(ye.ambientLightColor.value=B.state.ambient,ye.lightProbe.value=B.state.probe,ye.sunLights.value=B.state.sun,ye.sunLightShadows.value=B.state.sunShadow,ye.directionalLights.value=B.state.directional,ye.directionalLightShadows.value=B.state.directionalShadow,ye.spotLights.value=B.state.spot,ye.spotLightShadows.value=B.state.spotShadow,ye.rectAreaLights.value=B.state.rectArea,ye.ltc_1.value=B.state.rectAreaLTC1,ye.ltc_2.value=B.state.rectAreaLTC2,ye.pointLights.value=B.state.point,ye.pointLightShadows.value=B.state.pointShadow,ye.hemisphereLights.value=B.state.hemi,ye.sunShadowMatrix.value=B.state.sunShadowMatrix,ye.sunShadowCascade.value=B.state.sunShadowCascade,ye.directionalShadowMatrix.value=B.state.directionalShadowMatrix,ye.spotLightMatrix.value=B.state.spotLightMatrix,ye.spotLightMap.value=B.state.spotLightMap,ye.pointShadowMatrix.value=B.state.pointShadowMatrix),F.numLightProbeGrids=Nl(T.state.lightProbeGridArray),F.currentProgram=Ve,F.uniformsList=null,Ve}function Vh(y,C,k,F,B){let he=we.get(y),_e=he.currentProgram.id+","+F+","+B,le=he.programVariants.get(_e);return le===void 0?(le=Ki(y,C,k),he.programVariants.set(_e,le)):(he.currentProgram=le,he.uniformsList=null,he.outputColorSpace=F,he.toneMapping=B),le}function Ul(y){if(y.uniformsList===null){let C=y.currentProgram.getUniforms();y.uniformsList=Ji.seqWithValue(C.seq,y.uniforms)}return y.uniformsList}function Fl(y,C){let k=we.get(y);k.outputColorSpace=C.outputColorSpace,k.batching=C.batching,k.batchingColor=C.batchingColor,k.instancing=C.instancing,k.instancingColor=C.instancingColor,k.instancingMorph=C.instancingMorph,k.skinning=C.skinning,k.morphTargets=C.morphTargets,k.morphNormals=C.morphNormals,k.morphColors=C.morphColors,k.morphTargetsCount=C.morphTargetsCount,k.numClippingPlanes=C.numClippingPlanes,k.numIntersection=C.numClipIntersection,k.vertexAlphas=C.vertexAlphas,k.vertexTangents=C.vertexTangents,k.toneMapping=C.toneMapping}function Hh(y,C,k,F,B){C.isScene!==!0&&(C=Jt),Le.resetTextureUnits();let he=C.fog,_e=F.isMeshStandardMaterial||F.isMeshLambertMaterial||F.isMeshPhongMaterial?C.environment:null,le=te===null?I.outputColorSpace:te.isXRRenderTarget===!0?te.texture.colorSpace:We.workingColorSpace,ge=F.isMeshStandardMaterial||F.isMeshLambertMaterial&&!F.envMap||F.isMeshPhongMaterial&&!F.envMap,Me=b.get(F.envMap||_e,ge),Ne=F.vertexColors===!0&&!!k.attributes.color&&k.attributes.color.itemSize===4,Ve=!!k.attributes.tangent&&(!!F.normalMap||F.anisotropy>0),ye=!!k.morphAttributes.position,He=!!k.morphAttributes.normal,ut=!!k.morphAttributes.color,tt=xn;F.toneMapped&&(te===null||te.isXRRenderTarget===!0)&&(tt=I.toneMapping);let et=k.morphAttributes.position||k.morphAttributes.normal||k.morphAttributes.color,At=et!==void 0?et.length:0,ve=we.get(F),Dt=T.state.lights;if(ft===!0&&(Bt===!0||y!==j)){let lt=y===j&&F.id===H;Y.setState(F,y,lt)}let Ye=!1,ti=!1;F.version===ve.__version?ve.needsLights&&ve.lightsStateVersion!==Dt.state.version||B.isBatchedMesh&&ve.batching===!1||!B.isBatchedMesh&&ve.batching===!0||B.isBatchedMesh&&ve.batchingColor===!0&&B._colorsTexture===null||B.isBatchedMesh&&ve.batchingColor===!1&&B._colorsTexture!==null||B.isInstancedMesh&&ve.instancing===!1||!B.isInstancedMesh&&ve.instancing===!0||B.isSkinnedMesh&&ve.skinning===!1||!B.isSkinnedMesh&&ve.skinning===!0||B.isInstancedMesh&&ve.instancingColor===!0&&B.instanceColor===null||B.isInstancedMesh&&ve.instancingColor===!1&&B.instanceColor!==null||B.isInstancedMesh&&ve.instancingMorph===!0&&B.morphTexture===null||B.isInstancedMesh&&ve.instancingMorph===!1&&B.morphTexture!==null||ve.envMap!==Me||F.fog===!0&&ve.fog!==he||ve.numClippingPlanes!==void 0&&(ve.numClippingPlanes!==Y.numPlanes||ve.numIntersection!==Y.numIntersection)||ve.vertexAlphas!==Ne||ve.vertexTangents!==Ve||ve.morphTargets!==ye||ve.morphNormals!==He||ve.morphColors!==ut||ve.morphTargetsCount!==At||ve.numLightProbeGrids!==Nl(T.state.lightProbeGridArray)?Ye=!0:(ve.outputColorSpace!==le||ve.toneMapping!==tt)&&(ti=!0):(Ye=!0,ve.__version=F.version);let wt=ve.currentProgram;(Ye===!0||ti===!0)&&(wt=ti===!0?Vh(F,C,B,le,tt):Ki(F,C,B),z&&F.isNodeMaterial&&z.onUpdateProgram(F,wt,ve));let Ws=!1,On=!1,ni=!1,qe=wt.getUniforms(),Et=ve.uniforms;if(ue.useProgram(wt.program)&&(Ws=!0,On=!0,ni=!0),F.id!==H&&(H=F.id,On=!0),Ws||j!==y){ue.buffers.depth.getReversed()&&y.reversedDepth!==!0&&(y._reversedDepth=!0,y.updateProjectionMatrix()),qe.setValue(L,"projectionMatrix",y.projectionMatrix),qe.setValue(L,"viewMatrix",y.matrixWorldInverse);let vt=qe.map.cameraPosition;vt!==void 0&&vt.setValue(L,pn.setFromMatrixPosition(y.matrixWorld)),rt.logarithmicDepthBuffer&&qe.setValue(L,"logDepthBufFC",2/(Math.log(y.far+1)/Math.LN2)),(F.isMeshPhongMaterial||F.isMeshToonMaterial||F.isMeshLambertMaterial||F.isMeshBasicMaterial||F.isMeshStandardMaterial||F.isShaderMaterial)&&qe.setValue(L,"isOrthographic",y.isOrthographicCamera===!0),j!==y&&(j=y,On=!0,ni=!0)}if(ve.needsLights&&(Dt.state.sunShadowMap.length>0&&qe.setValue(L,"sunShadowMap",Dt.state.sunShadowMap,Le),Dt.state.directionalShadowMap.length>0&&qe.setValue(L,"directionalShadowMap",Dt.state.directionalShadowMap,Le),Dt.state.spotShadowMap.length>0&&qe.setValue(L,"spotShadowMap",Dt.state.spotShadowMap,Le),Dt.state.pointShadowMap.length>0&&qe.setValue(L,"pointShadowMap",Dt.state.pointShadowMap,Le)),B.isSkinnedMesh){qe.setOptional(L,B,"bindMatrix"),qe.setOptional(L,B,"bindMatrixInverse");let lt=B.skeleton;lt&&(lt.boneTexture===null&&lt.computeBoneTexture(),qe.setValue(L,"boneTexture",lt.boneTexture,Le))}B.isBatchedMesh&&(qe.setOptional(L,B,"batchingTexture"),qe.setValue(L,"batchingTexture",B._matricesTexture,Le),qe.setOptional(L,B,"batchingIdTexture"),qe.setValue(L,"batchingIdTexture",B._indirectTexture,Le),qe.setOptional(L,B,"batchingColorTexture"),B._colorsTexture!==null&&qe.setValue(L,"batchingColorTexture",B._colorsTexture,Le));let sn=k.morphAttributes;if((sn.position!==void 0||sn.normal!==void 0||sn.color!==void 0)&&J.update(B,k,wt),(On||ve.receiveShadow!==B.receiveShadow)&&(ve.receiveShadow=B.receiveShadow,qe.setValue(L,"receiveShadow",B.receiveShadow)),(F.isMeshStandardMaterial||F.isMeshLambertMaterial||F.isMeshPhongMaterial)&&F.envMap===null&&C.environment!==null&&(Et.envMapIntensity.value=C.environmentIntensity),Et.dfgLUT!==void 0&&(Et.dfgLUT.value=w2()),On){if(qe.setValue(L,"toneMappingExposure",I.toneMappingExposure),ve.needsLights&&Wh(Et,ni),he&&F.fog===!0&&se.refreshFogUniforms(Et,he),se.refreshMaterialUniforms(Et,F,me,Ae,T.state.transmissionRenderTarget[y.id]),ve.needsLights&&ve.numLightProbeGrids>0){let lt=E,vt=0;for(let Sn of T.state.lightProbeGridArray)Sn.texture!==null&&(lt.textures[vt]=Sn.texture,lt.min[vt]=Sn.boundingBox.min,lt.max[vt]=Sn.boundingBox.max,lt.resolution[vt]=Sn.resolution,vt++);for(let Sn in lt)lt[Sn].length=vt;Et.probesSH.value=lt.textures,Et.probesMin.value=lt.min,Et.probesMax.value=lt.max,Et.probesResolution.value=lt.resolution}Ji.upload(L,Ul(ve),Et,Le)}if(F.isShaderMaterial&&F.uniformsNeedUpdate===!0&&(Ji.upload(L,Ul(ve),Et,Le),F.uniformsNeedUpdate=!1),F.isSpriteMaterial&&qe.setValue(L,"center",B.center),qe.setValue(L,"modelViewMatrix",B.modelViewMatrix),qe.setValue(L,"normalMatrix",B.normalMatrix),qe.setValue(L,"modelMatrix",B.matrixWorld),F.uniformsGroups!==void 0){let lt=F.uniformsGroups;for(let vt=0,Sn=lt.length;vt<Sn;vt++){let Bl=lt[vt];be.update(Bl,wt),be.bind(Bl,wt)}}return wt}function Wh(y,C){y.ambientLightColor.needsUpdate=C,y.lightProbe.needsUpdate=C,y.sunLights.needsUpdate=C,y.sunLightShadows.needsUpdate=C,y.directionalLights.needsUpdate=C,y.directionalLightShadows.needsUpdate=C,y.pointLights.needsUpdate=C,y.pointLightShadows.needsUpdate=C,y.spotLights.needsUpdate=C,y.spotLightShadows.needsUpdate=C,y.rectAreaLights.needsUpdate=C,y.hemisphereLights.needsUpdate=C}function Xh(y){return y.isMeshLambertMaterial||y.isMeshToonMaterial||y.isMeshPhongMaterial||y.isMeshStandardMaterial||y.isShadowMaterial||y.isShaderMaterial&&y.lights===!0}this.getActiveCubeFace=function(){return $},this.getActiveMipmapLevel=function(){return G},this.getRenderTarget=function(){return te},this.setRenderTargetTextures=function(y,C,k){let F=we.get(y);F.__autoAllocateDepthBuffer=y.resolveDepthBuffer===!1,F.__autoAllocateDepthBuffer===!1&&(F.__useRenderToTexture=!1),we.get(y.texture).__webglTexture=C,we.get(y.depthTexture).__webglTexture=F.__autoAllocateDepthBuffer?void 0:k,F.__hasExternalTextures=!0},this.setRenderTargetFramebuffer=function(y,C){let k=we.get(y);k.__webglFramebuffer=C,k.__useDefaultFramebuffer=C===void 0},this.setRenderTarget=function(y,C=0,k=0){te=y,$=C,G=k;let F=null,B=!1,he=!1;if(y){let le=we.get(y);if(le.__useDefaultFramebuffer!==void 0){ue.bindFramebuffer(L.FRAMEBUFFER,le.__webglFramebuffer),Q.copy(y.viewport),Se.copy(y.scissor),De=y.scissorTest,ue.viewport(Q),ue.scissor(Se),ue.setScissorTest(De),H=-1;return}else if(le.__webglFramebuffer===void 0)Le.setupRenderTarget(y);else if(le.__hasExternalTextures)Le.rebindTextures(y,we.get(y.texture).__webglTexture,we.get(y.depthTexture).__webglTexture);else if(y.depthBuffer){let Ne=y.depthTexture;if(le.__boundDepthTexture!==Ne){if(Ne!==null&&we.has(Ne)&&(y.width!==Ne.image.width||y.height!==Ne.image.height))throw new Error("THREE.WebGLRenderer: Attached DepthTexture is initialized to the incorrect size.");Le.setupDepthRenderbuffer(y)}}let ge=y.texture;(ge.isData3DTexture||ge.isDataArrayTexture||ge.isCompressedArrayTexture)&&(he=!0);let Me=we.get(y).__webglFramebuffer;y.isWebGLCubeRenderTarget?(Array.isArray(Me[C])?F=Me[C][k]:F=Me[C],B=!0):y.samples>0&&Le.useMultisampledRTT(y)===!1?F=we.get(y).__webglMultisampledFramebuffer:Array.isArray(Me)?F=Me[k]:F=Me,Q.copy(y.viewport),Se.copy(y.scissor),De=y.scissorTest}else Q.copy(Ce).multiplyScalar(me).floor(),Se.copy(Ke).multiplyScalar(me).floor(),De=Qe;if(k!==0&&(F=q),ue.bindFramebuffer(L.FRAMEBUFFER,F)&&ue.drawBuffers(y,F),ue.viewport(Q),ue.scissor(Se),ue.setScissorTest(De),B){let le=we.get(y.texture);L.framebufferTexture2D(L.FRAMEBUFFER,L.COLOR_ATTACHMENT0,L.TEXTURE_CUBE_MAP_POSITIVE_X+C,le.__webglTexture,k)}else if(he){let le=C;for(let ge=0;ge<y.textures.length;ge++){let Me=we.get(y.textures[ge]);L.framebufferTextureLayer(L.FRAMEBUFFER,L.COLOR_ATTACHMENT0+ge,Me.__webglTexture,k,le)}}else if(y!==null&&k!==0){let le=we.get(y.texture);L.framebufferTexture2D(L.FRAMEBUFFER,L.COLOR_ATTACHMENT0,L.TEXTURE_2D,le.__webglTexture,k)}H=-1};function Ol(y){let C=we.get(y);return(C.__readFormat!==y.format||C.__readType!==y.type)&&(C.__readFormat=y.format,C.__readType=y.type,C.__formatReadable=rt.textureFormatReadable(y.format),C.__typeReadable=rt.textureTypeReadable(y.type)),C}this.readRenderTargetPixels=function(y,C,k,F,B,he,_e,le=0){if(!(y&&y.isWebGLRenderTarget)){Pe("WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");return}let ge=we.get(y).__webglFramebuffer;if(y.isWebGLCubeRenderTarget&&_e!==void 0&&(ge=ge[_e],Array.isArray(ge)&&(ge=ge[0])),ge){ue.bindFramebuffer(L.FRAMEBUFFER,ge);try{let Me=y.textures[le],Ne=Me.format,Ve=Me.type;y.textures.length>1&&L.readBuffer(L.COLOR_ATTACHMENT0+le);let ye=Ol(Me);if(ye.__formatReadable===!1){Pe("WebGLRenderer.readRenderTargetPixels: renderTarget is not in RGBA or implementation defined format.");return}if(ye.__typeReadable===!1){Pe("WebGLRenderer.readRenderTargetPixels: renderTarget is not in UnsignedByteType or implementation defined type.");return}C>=0&&C<=y.width-F&&k>=0&&k<=y.height-B&&L.readPixels(C,k,F,B,ie.convert(Ne),ie.convert(Ve),he)}finally{let Me=te!==null?we.get(te).__webglFramebuffer:null;ue.bindFramebuffer(L.FRAMEBUFFER,Me)}}},this.readRenderTargetPixelsAsync=async function(y,C,k,F,B,he,_e,le=0){if(!(y&&y.isWebGLRenderTarget))throw new Error("THREE.WebGLRenderer.readRenderTargetPixels: renderTarget is not THREE.WebGLRenderTarget.");let ge=we.get(y).__webglFramebuffer;if(y.isWebGLCubeRenderTarget&&_e!==void 0&&(ge=ge[_e],Array.isArray(ge)&&(ge=ge[0])),ge)if(C>=0&&C<=y.width-F&&k>=0&&k<=y.height-B){ue.bindFramebuffer(L.FRAMEBUFFER,ge);let Me=y.textures[le],Ne=Me.format,Ve=Me.type;y.textures.length>1&&L.readBuffer(L.COLOR_ATTACHMENT0+le);let ye=Ol(Me);if(ye.__formatReadable===!1)throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in RGBA or implementation defined format.");if(ye.__typeReadable===!1)throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: renderTarget is not in UnsignedByteType or implementation defined type.");let He=L.createBuffer();L.bindBuffer(L.PIXEL_PACK_BUFFER,He),L.bufferData(L.PIXEL_PACK_BUFFER,he.byteLength,L.STREAM_READ),L.readPixels(C,k,F,B,ie.convert(Ne),ie.convert(Ve),0),L.bindBuffer(L.PIXEL_PACK_BUFFER,null);let ut=te!==null?we.get(te).__webglFramebuffer:null;ue.bindFramebuffer(L.FRAMEBUFFER,ut);let tt=L.fenceSync(L.SYNC_GPU_COMMANDS_COMPLETE,0);return L.flush(),await $c(L,tt,4),L.bindBuffer(L.PIXEL_PACK_BUFFER,He),L.getBufferSubData(L.PIXEL_PACK_BUFFER,0,he),L.bindBuffer(L.PIXEL_PACK_BUFFER,null),L.deleteBuffer(He),L.deleteSync(tt),he}else throw new Error("THREE.WebGLRenderer.readRenderTargetPixelsAsync: requested read bounds are out of range.")},this.copyFramebufferToTexture=function(y,C=null,k=0){let F=Math.pow(2,-k),B=Math.floor(y.image.width*F),he=Math.floor(y.image.height*F),_e=C!==null?C.x:0,le=C!==null?C.y:0;Le.setTexture2D(y,0),L.copyTexSubImage2D(L.TEXTURE_2D,k,0,0,_e,le,B,he),ue.unbindTexture()},this.copyTextureToTexture=function(y,C,k=null,F=null,B=0,he=0){let _e,le,ge,Me,Ne,Ve,ye,He,ut,tt=y.isCompressedTexture?y.mipmaps[he]:y.image;if(k!==null)_e=k.max.x-k.min.x,le=k.max.y-k.min.y,ge=k.isBox3?k.max.z-k.min.z:1,Me=k.min.x,Ne=k.min.y,Ve=k.isBox3?k.min.z:0;else{let qe=Math.pow(2,-B);_e=Math.floor(tt.width*qe),le=Math.floor(tt.height*qe),y.isDataArrayTexture?ge=tt.depth:y.isData3DTexture?ge=Math.floor(tt.depth*qe):ge=1,Me=0,Ne=0,Ve=0}F!==null?(ye=F.x,He=F.y,ut=F.z):(ye=0,He=0,ut=0);let et=ie.convert(C.format),At=ie.convert(C.type),ve;C.isData3DTexture?(Le.setTexture3D(C,0),ve=L.TEXTURE_3D):C.isDataArrayTexture||C.isCompressedArrayTexture?(Le.setTexture2DArray(C,0),ve=L.TEXTURE_2D_ARRAY):(Le.setTexture2D(C,0),ve=L.TEXTURE_2D),ue.activeTexture(L.TEXTURE0),ue.pixelStorei(L.UNPACK_FLIP_Y_WEBGL,C.flipY),ue.pixelStorei(L.UNPACK_PREMULTIPLY_ALPHA_WEBGL,C.premultiplyAlpha),ue.pixelStorei(L.UNPACK_ALIGNMENT,C.unpackAlignment);let Dt=ue.getParameter(L.UNPACK_ROW_LENGTH),Ye=ue.getParameter(L.UNPACK_IMAGE_HEIGHT),ti=ue.getParameter(L.UNPACK_SKIP_PIXELS),wt=ue.getParameter(L.UNPACK_SKIP_ROWS),Ws=ue.getParameter(L.UNPACK_SKIP_IMAGES);ue.pixelStorei(L.UNPACK_ROW_LENGTH,tt.width),ue.pixelStorei(L.UNPACK_IMAGE_HEIGHT,tt.height),ue.pixelStorei(L.UNPACK_SKIP_PIXELS,Me),ue.pixelStorei(L.UNPACK_SKIP_ROWS,Ne),ue.pixelStorei(L.UNPACK_SKIP_IMAGES,Ve);let On=y.isDataArrayTexture||y.isData3DTexture,ni=C.isDataArrayTexture||C.isData3DTexture;if(y.isDepthTexture){let qe=we.get(y),Et=we.get(C),sn=we.get(qe.__renderTarget),lt=we.get(Et.__renderTarget);ue.bindFramebuffer(L.READ_FRAMEBUFFER,sn.__webglFramebuffer),ue.bindFramebuffer(L.DRAW_FRAMEBUFFER,lt.__webglFramebuffer);for(let vt=0;vt<ge;vt++)On&&(L.framebufferTextureLayer(L.READ_FRAMEBUFFER,L.COLOR_ATTACHMENT0,we.get(y).__webglTexture,B,Ve+vt),L.framebufferTextureLayer(L.DRAW_FRAMEBUFFER,L.COLOR_ATTACHMENT0,we.get(C).__webglTexture,he,ut+vt)),L.blitFramebuffer(Me,Ne,Me+_e,Ne+le,ye,He,ye+_e,He+le,L.DEPTH_BUFFER_BIT,L.NEAREST);ue.bindFramebuffer(L.READ_FRAMEBUFFER,null),ue.bindFramebuffer(L.DRAW_FRAMEBUFFER,null)}else if(B!==0||y.isRenderTargetTexture||we.has(y)){let qe=we.get(y),Et=we.get(C);ue.bindFramebuffer(L.READ_FRAMEBUFFER,P),ue.bindFramebuffer(L.DRAW_FRAMEBUFFER,W);for(let sn=0;sn<ge;sn++)On?L.framebufferTextureLayer(L.READ_FRAMEBUFFER,L.COLOR_ATTACHMENT0,qe.__webglTexture,B,Ve+sn):L.framebufferTexture2D(L.READ_FRAMEBUFFER,L.COLOR_ATTACHMENT0,L.TEXTURE_2D,qe.__webglTexture,B),ni?L.framebufferTextureLayer(L.DRAW_FRAMEBUFFER,L.COLOR_ATTACHMENT0,Et.__webglTexture,he,ut+sn):L.framebufferTexture2D(L.DRAW_FRAMEBUFFER,L.COLOR_ATTACHMENT0,L.TEXTURE_2D,Et.__webglTexture,he),B!==0?L.blitFramebuffer(Me,Ne,Me+_e,Ne+le,ye,He,ye+_e,He+le,L.COLOR_BUFFER_BIT,L.NEAREST):ni?L.copyTexSubImage3D(ve,he,ye,He,ut+sn,Me,Ne,_e,le):L.copyTexSubImage2D(ve,he,ye,He,Me,Ne,_e,le);ue.bindFramebuffer(L.READ_FRAMEBUFFER,null),ue.bindFramebuffer(L.DRAW_FRAMEBUFFER,null)}else ni?y.isDataTexture||y.isData3DTexture?L.texSubImage3D(ve,he,ye,He,ut,_e,le,ge,et,At,tt.data):C.isCompressedArrayTexture?L.compressedTexSubImage3D(ve,he,ye,He,ut,_e,le,ge,et,tt.data):L.texSubImage3D(ve,he,ye,He,ut,_e,le,ge,et,At,tt):y.isDataTexture?L.texSubImage2D(L.TEXTURE_2D,he,ye,He,_e,le,et,At,tt.data):y.isCompressedTexture?L.compressedTexSubImage2D(L.TEXTURE_2D,he,ye,He,tt.width,tt.height,et,tt.data):L.texSubImage2D(L.TEXTURE_2D,he,ye,He,_e,le,et,At,tt);ue.pixelStorei(L.UNPACK_ROW_LENGTH,Dt),ue.pixelStorei(L.UNPACK_IMAGE_HEIGHT,Ye),ue.pixelStorei(L.UNPACK_SKIP_PIXELS,ti),ue.pixelStorei(L.UNPACK_SKIP_ROWS,wt),ue.pixelStorei(L.UNPACK_SKIP_IMAGES,Ws),he===0&&C.generateMipmaps===!0&&C.mipmapsAutoUpdate===!0&&L.generateMipmap(ve),ue.unbindTexture()},this.initRenderTarget=function(y){we.get(y).__webglFramebuffer===void 0&&Le.setupRenderTarget(y)},this.initTexture=function(y){y.isCubeTexture?Le.setTextureCube(y,0):y.isData3DTexture?Le.setTexture3D(y,0):y.isDataArrayTexture||y.isCompressedArrayTexture?Le.setTexture2DArray(y,0):Le.setTexture2D(y,0),ue.unbindTexture()},this.resetState=function(){$=0,G=0,te=null,ue.reset(),re.reset()},typeof __THREE_DEVTOOLS__<"u"&&__THREE_DEVTOOLS__.dispatchEvent(new CustomEvent("observe",{detail:this}))}get coordinateSystem(){return en}get outputColorSpace(){return this._outputColorSpace}set outputColorSpace(e){this._outputColorSpace=e;let t=this.getContext();t.drawingBufferColorSpace=We._getDrawingBufferColorSpace(e),t.unpackColorSpace=We._getUnpackColorSpace()}};var Fh={type:"change"},vl={type:"start"},Bh={type:"end"},Ga=new Xn,Oh=new Xt,C2=Math.cos(70*Qo.DEG2RAD),_t=new U,Vt=2*Math.PI,Ze={NONE:-1,ROTATE:0,DOLLY:1,PAN:2,TOUCH_ROTATE:3,TOUCH_PAN:4,TOUCH_DOLLY_PAN:5,TOUCH_DOLLY_ROTATE:6},yl=1e-6,Va=class extends Cs{constructor(e,t=null){super(e,t),this.state=Ze.NONE,this.target=new U,this.cursor=new U,this.minDistance=0,this.maxDistance=1/0,this.minZoom=0,this.maxZoom=1/0,this.minTargetRadius=0,this.maxTargetRadius=1/0,this.minPolarAngle=0,this.maxPolarAngle=Math.PI,this.minAzimuthAngle=-1/0,this.maxAzimuthAngle=1/0,this.enableDamping=!1,this.dampingFactor=.05,this.enableZoom=!0,this.zoomSpeed=1,this.enableRotate=!0,this.rotateSpeed=1,this.keyRotateSpeed=1,this.enablePan=!0,this.panSpeed=1,this.screenSpacePanning=!0,this.keyPanSpeed=7,this.zoomToCursor=!1,this.autoRotate=!1,this.autoRotateSpeed=2,this.keys={LEFT:"ArrowLeft",UP:"ArrowUp",RIGHT:"ArrowRight",BOTTOM:"ArrowDown"},this.mouseButtons={LEFT:$n.ROTATE,MIDDLE:$n.DOLLY,RIGHT:$n.PAN},this.touches={ONE:Kn.ROTATE,TWO:Kn.DOLLY_PAN},this.target0=this.target.clone(),this.position0=this.object.position.clone(),this.zoom0=this.object.zoom,this._cursorStyle="auto",this._domElementKeyEvents=null,this._lastPosition=new U,this._lastQuaternion=new qt,this._lastTargetPosition=new U,this._quat=new qt().setFromUnitVectors(e.up,new U(0,1,0)),this._quatInverse=this._quat.clone().invert(),this._spherical=new Hi,this._sphericalDelta=new Hi,this._scale=1,this._panOffset=new U,this._rotateStart=new Re,this._rotateEnd=new Re,this._rotateDelta=new Re,this._panStart=new Re,this._panEnd=new Re,this._panDelta=new Re,this._dollyStart=new Re,this._dollyEnd=new Re,this._dollyDelta=new Re,this._dollyDirection=new U,this._mouse=new Re,this._performCursorZoom=!1,this._pointers=[],this._pointerPositions={},this._controlActive=!1,this._onPointerMove=I2.bind(this),this._onPointerDown=P2.bind(this),this._onPointerUp=L2.bind(this),this._onContextMenu=z2.bind(this),this._onMouseWheel=U2.bind(this),this._onKeyDown=F2.bind(this),this._onTouchStart=O2.bind(this),this._onTouchMove=B2.bind(this),this._onMouseDown=D2.bind(this),this._onMouseMove=N2.bind(this),this._interceptControlDown=k2.bind(this),this._interceptControlUp=G2.bind(this),this.domElement!==null&&this.connect(this.domElement),this.update()}set cursorStyle(e){this._cursorStyle=e,e==="grab"?this.domElement.style.cursor="grab":this.domElement.style.cursor="auto"}get cursorStyle(){return this._cursorStyle}connect(e){super.connect(e),this.domElement.addEventListener("pointerdown",this._onPointerDown),this.domElement.addEventListener("pointercancel",this._onPointerUp),this.domElement.addEventListener("contextmenu",this._onContextMenu),this.domElement.addEventListener("wheel",this._onMouseWheel,{passive:!1}),this.domElement.ownerDocument.addEventListener("keydown",this._interceptControlDown,{passive:!0,capture:!0}),this.domElement.style.touchAction="none"}disconnect(){this.state=Ze.NONE,this.domElement.removeEventListener("pointerdown",this._onPointerDown),this.domElement.ownerDocument.removeEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.removeEventListener("pointerup",this._onPointerUp),this.domElement.removeEventListener("pointercancel",this._onPointerUp),this.domElement.removeEventListener("wheel",this._onMouseWheel),this.domElement.removeEventListener("contextmenu",this._onContextMenu),this.stopListenToKeyEvents(),this.domElement.ownerDocument.removeEventListener("keydown",this._interceptControlDown,{capture:!0}),this.domElement.ownerDocument.removeEventListener("keyup",this._interceptControlUp,{capture:!0}),this._controlActive=!1,this._pointers.length=0,this._pointerPositions={},this.domElement.style.touchAction="",this.domElement.style.cursor="auto"}dispose(){this.disconnect()}getPolarAngle(){return this._spherical.phi}getAzimuthalAngle(){return this._spherical.theta}getDistance(){return this.object.position.distanceTo(this.target)}listenToKeyEvents(e){e.addEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=e}stopListenToKeyEvents(){this._domElementKeyEvents!==null&&(this._domElementKeyEvents.removeEventListener("keydown",this._onKeyDown),this._domElementKeyEvents=null)}saveState(){this.target0.copy(this.target),this.position0.copy(this.object.position),this.zoom0=this.object.zoom}reset(){this.target.copy(this.target0),this.object.position.copy(this.position0),this.object.zoom=this.zoom0,this.object.updateProjectionMatrix(),this.dispatchEvent(Fh),this.update(),this.state=Ze.NONE}pan(e,t){this._pan(e,t),this.update()}dollyIn(e){this._dollyIn(e),this.update()}dollyOut(e){this._dollyOut(e),this.update()}rotateLeft(e){this._rotateLeft(e),this.update()}rotateUp(e){this._rotateUp(e),this.update()}update(e=null){let t=this.object.position;_t.copy(t).sub(this.target),_t.applyQuaternion(this._quat),this._spherical.setFromVector3(_t),this.autoRotate&&this.state===Ze.NONE&&this._rotateLeft(this._getAutoRotationAngle(e)),this.enableDamping?(this._spherical.theta+=this._sphericalDelta.theta*this.dampingFactor,this._spherical.phi+=this._sphericalDelta.phi*this.dampingFactor):(this._spherical.theta+=this._sphericalDelta.theta,this._spherical.phi+=this._sphericalDelta.phi);let n=this.minAzimuthAngle,s=this.maxAzimuthAngle;isFinite(n)&&isFinite(s)&&(n<-Math.PI?n+=Vt:n>Math.PI&&(n-=Vt),s<-Math.PI?s+=Vt:s>Math.PI&&(s-=Vt),n<=s?this._spherical.theta=Math.max(n,Math.min(s,this._spherical.theta)):this._spherical.theta=this._spherical.theta>(n+s)/2?Math.max(n,this._spherical.theta):Math.min(s,this._spherical.theta)),this._spherical.phi=Math.max(this.minPolarAngle,Math.min(this.maxPolarAngle,this._spherical.phi)),this._spherical.makeSafe(),this.enableDamping===!0?this.target.addScaledVector(this._panOffset,this.dampingFactor):this.target.add(this._panOffset),this.target.sub(this.cursor),this.target.clampLength(this.minTargetRadius,this.maxTargetRadius),this.target.add(this.cursor);let r=!1;if(this.zoomToCursor&&this._performCursorZoom||this.object.isOrthographicCamera)this._spherical.radius=this._clampDistance(this._spherical.radius);else{let a=this._spherical.radius;this._spherical.radius=this._clampDistance(this._spherical.radius*this._scale),r=a!=this._spherical.radius}if(_t.setFromSpherical(this._spherical),_t.applyQuaternion(this._quatInverse),t.copy(this.target).add(_t),this.object.lookAt(this.target),this.enableDamping===!0?(this._sphericalDelta.theta*=1-this.dampingFactor,this._sphericalDelta.phi*=1-this.dampingFactor,this._panOffset.multiplyScalar(1-this.dampingFactor)):(this._sphericalDelta.set(0,0,0),this._panOffset.set(0,0,0)),this.zoomToCursor&&this._performCursorZoom){let a=null;if(this.object.isPerspectiveCamera){let o=_t.length();a=this._clampDistance(o*this._scale);let l=o-a;this.object.position.addScaledVector(this._dollyDirection,l),this.object.updateMatrixWorld(),r=!!l}else if(this.object.isOrthographicCamera){let o=new U(this._mouse.x,this._mouse.y,0);o.unproject(this.object);let l=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),this.object.updateProjectionMatrix(),r=l!==this.object.zoom;let c=new U(this._mouse.x,this._mouse.y,0);c.unproject(this.object),this.object.position.sub(c).add(o),this.object.updateMatrixWorld(),a=_t.length()}else console.warn("WARNING: OrbitControls.js encountered an unknown camera type - zoom to cursor disabled."),this.zoomToCursor=!1;a!==null&&(this.screenSpacePanning?this.target.set(0,0,-1).transformDirection(this.object.matrix).multiplyScalar(a).add(this.object.position):(Ga.origin.copy(this.object.position),Ga.direction.set(0,0,-1).transformDirection(this.object.matrix),Math.abs(this.object.up.dot(Ga.direction))<C2?this.object.lookAt(this.target):(Oh.setFromNormalAndCoplanarPoint(this.object.up,this.target),Ga.intersectPlane(Oh,this.target))))}else if(this.object.isOrthographicCamera){let a=this.object.zoom;this.object.zoom=Math.max(this.minZoom,Math.min(this.maxZoom,this.object.zoom/this._scale)),a!==this.object.zoom&&(this.object.updateProjectionMatrix(),r=!0)}return this._scale=1,this._performCursorZoom=!1,r||this._lastPosition.distanceToSquared(this.object.position)>yl||8*(1-this._lastQuaternion.dot(this.object.quaternion))>yl||this._lastTargetPosition.distanceToSquared(this.target)>yl?(this.dispatchEvent(Fh),this._lastPosition.copy(this.object.position),this._lastQuaternion.copy(this.object.quaternion),this._lastTargetPosition.copy(this.target),!0):!1}_getAutoRotationAngle(e){return e!==null?Vt/60*this.autoRotateSpeed*e:Vt/60/60*this.autoRotateSpeed}_getZoomScale(e){let t=Math.abs(e*.01);return Math.pow(.95,this.zoomSpeed*t)}_rotateLeft(e){this._sphericalDelta.theta-=e}_rotateUp(e){this._sphericalDelta.phi-=e}_panLeft(e,t){_t.setFromMatrixColumn(t,0),_t.multiplyScalar(-e),this._panOffset.add(_t)}_panUp(e,t){this.screenSpacePanning===!0?_t.setFromMatrixColumn(t,1):(_t.setFromMatrixColumn(t,0),_t.crossVectors(this.object.up,_t)),_t.multiplyScalar(e),this._panOffset.add(_t)}_pan(e,t){let n=this.domElement;if(this.object.isPerspectiveCamera){let s=this.object.position;_t.copy(s).sub(this.target);let r=_t.length();r*=Math.tan(this.object.fov/2*Math.PI/180),this._panLeft(2*e*r/n.clientHeight,this.object.matrix),this._panUp(2*t*r/n.clientHeight,this.object.matrix)}else this.object.isOrthographicCamera?(this._panLeft(e*(this.object.right-this.object.left)/this.object.zoom/n.clientWidth,this.object.matrix),this._panUp(t*(this.object.top-this.object.bottom)/this.object.zoom/n.clientHeight,this.object.matrix)):(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - pan disabled."),this.enablePan=!1)}_dollyOut(e){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale/=e:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_dollyIn(e){this.object.isPerspectiveCamera||this.object.isOrthographicCamera?this._scale*=e:(console.warn("WARNING: OrbitControls.js encountered an unknown camera type - dolly/zoom disabled."),this.enableZoom=!1)}_updateZoomParameters(e,t){if(!this.zoomToCursor)return;this._performCursorZoom=!0;let n=this.domElement.getBoundingClientRect(),s=e-n.left,r=t-n.top,a=n.width,o=n.height;this._mouse.x=s/a*2-1,this._mouse.y=-(r/o)*2+1,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()}_clampDistance(e){return Math.max(this.minDistance,Math.min(this.maxDistance,e))}_handleMouseDownRotate(e){this._rotateStart.set(e.clientX,e.clientY)}_handleMouseDownDolly(e){this._updateZoomParameters(e.clientX,e.clientY),this._dollyStart.set(e.clientX,e.clientY)}_handleMouseDownPan(e){this._panStart.set(e.clientX,e.clientY)}_handleMouseMoveRotate(e){this._rotateEnd.set(e.clientX,e.clientY),this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);let t=this.domElement;this._rotateLeft(Vt*this._rotateDelta.x/t.clientHeight),this._rotateUp(Vt*this._rotateDelta.y/t.clientHeight),this._rotateStart.copy(this._rotateEnd),this.update()}_handleMouseMoveDolly(e){this._dollyEnd.set(e.clientX,e.clientY),this._dollyDelta.subVectors(this._dollyEnd,this._dollyStart),this._dollyDelta.y>0?this._dollyOut(this._getZoomScale(this._dollyDelta.y)):this._dollyDelta.y<0&&this._dollyIn(this._getZoomScale(this._dollyDelta.y)),this._dollyStart.copy(this._dollyEnd),this.zoomToCursor&&(this._performCursorZoom=!0,this._dollyDirection.set(this._mouse.x,this._mouse.y,1).unproject(this.object).sub(this.object.position).normalize()),this.update()}_handleMouseMovePan(e){this._panEnd.set(e.clientX,e.clientY),this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd),this.update()}_handleMouseWheel(e){this._updateZoomParameters(e.clientX,e.clientY),e.deltaY<0?this._dollyIn(this._getZoomScale(e.deltaY)):e.deltaY>0&&this._dollyOut(this._getZoomScale(e.deltaY)),this.update()}_handleKeyDown(e){let t=!1;switch(e.code){case this.keys.UP:e.ctrlKey||e.metaKey||e.shiftKey?this.enableRotate&&this._rotateUp(Vt*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,this.keyPanSpeed),t=!0;break;case this.keys.BOTTOM:e.ctrlKey||e.metaKey||e.shiftKey?this.enableRotate&&this._rotateUp(-Vt*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(0,-this.keyPanSpeed),t=!0;break;case this.keys.LEFT:e.ctrlKey||e.metaKey||e.shiftKey?this.enableRotate&&this._rotateLeft(Vt*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(this.keyPanSpeed,0),t=!0;break;case this.keys.RIGHT:e.ctrlKey||e.metaKey||e.shiftKey?this.enableRotate&&this._rotateLeft(-Vt*this.keyRotateSpeed/this.domElement.clientHeight):this.enablePan&&this._pan(-this.keyPanSpeed,0),t=!0;break}t&&(e.preventDefault(),this.update())}_handleTouchStartRotate(e){if(this._pointers.length===1)this._rotateStart.set(e.pageX,e.pageY);else{let t=this._getSecondPointerPosition(e),n=.5*(e.pageX+t.x),s=.5*(e.pageY+t.y);this._rotateStart.set(n,s)}}_handleTouchStartPan(e){if(this._pointers.length===1)this._panStart.set(e.pageX,e.pageY);else{let t=this._getSecondPointerPosition(e),n=.5*(e.pageX+t.x),s=.5*(e.pageY+t.y);this._panStart.set(n,s)}}_handleTouchStartDolly(e){let t=this._getSecondPointerPosition(e),n=e.pageX-t.x,s=e.pageY-t.y,r=Math.sqrt(n*n+s*s);this._dollyStart.set(0,r)}_handleTouchStartDollyPan(e){this.enableZoom&&this._handleTouchStartDolly(e),this.enablePan&&this._handleTouchStartPan(e)}_handleTouchStartDollyRotate(e){this.enableZoom&&this._handleTouchStartDolly(e),this.enableRotate&&this._handleTouchStartRotate(e)}_handleTouchMoveRotate(e){if(this._pointers.length==1)this._rotateEnd.set(e.pageX,e.pageY);else{let n=this._getSecondPointerPosition(e),s=.5*(e.pageX+n.x),r=.5*(e.pageY+n.y);this._rotateEnd.set(s,r)}this._rotateDelta.subVectors(this._rotateEnd,this._rotateStart).multiplyScalar(this.rotateSpeed);let t=this.domElement;this._rotateLeft(Vt*this._rotateDelta.x/t.clientHeight),this._rotateUp(Vt*this._rotateDelta.y/t.clientHeight),this._rotateStart.copy(this._rotateEnd)}_handleTouchMovePan(e){if(this._pointers.length===1)this._panEnd.set(e.pageX,e.pageY);else{let t=this._getSecondPointerPosition(e),n=.5*(e.pageX+t.x),s=.5*(e.pageY+t.y);this._panEnd.set(n,s)}this._panDelta.subVectors(this._panEnd,this._panStart).multiplyScalar(this.panSpeed),this._pan(this._panDelta.x,this._panDelta.y),this._panStart.copy(this._panEnd)}_handleTouchMoveDolly(e){let t=this._getSecondPointerPosition(e),n=e.pageX-t.x,s=e.pageY-t.y,r=Math.sqrt(n*n+s*s);this._dollyEnd.set(0,r),this._dollyDelta.set(0,Math.pow(this._dollyEnd.y/this._dollyStart.y,this.zoomSpeed)),this._dollyOut(this._dollyDelta.y),this._dollyStart.copy(this._dollyEnd);let a=(e.pageX+t.x)*.5,o=(e.pageY+t.y)*.5;this._updateZoomParameters(a,o)}_handleTouchMoveDollyPan(e){this.enableZoom&&this._handleTouchMoveDolly(e),this.enablePan&&this._handleTouchMovePan(e)}_handleTouchMoveDollyRotate(e){this.enableZoom&&this._handleTouchMoveDolly(e),this.enableRotate&&this._handleTouchMoveRotate(e)}_addPointer(e){this._pointers.push(e.pointerId)}_removePointer(e){delete this._pointerPositions[e.pointerId];for(let t=0;t<this._pointers.length;t++)if(this._pointers[t]==e.pointerId){this._pointers.splice(t,1);return}}_isTrackingPointer(e){for(let t=0;t<this._pointers.length;t++)if(this._pointers[t]==e.pointerId)return!0;return!1}_trackPointer(e){let t=this._pointerPositions[e.pointerId];t===void 0&&(t=new Re,this._pointerPositions[e.pointerId]=t),t.set(e.pageX,e.pageY)}_getSecondPointerPosition(e){let t=e.pointerId===this._pointers[0]?this._pointers[1]:this._pointers[0];return this._pointerPositions[t]}_customWheelEvent(e){let t=e.deltaMode,n={clientX:e.clientX,clientY:e.clientY,deltaY:e.deltaY};switch(t){case 1:n.deltaY*=16;break;case 2:n.deltaY*=100;break}return e.ctrlKey&&!this._controlActive&&(n.deltaY*=10),n}};function P2(i){this.enabled!==!1&&(this._pointers.length===0&&(this.domElement.setPointerCapture(i.pointerId),this.domElement.ownerDocument.addEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.addEventListener("pointerup",this._onPointerUp)),!this._isTrackingPointer(i)&&(this._addPointer(i),i.pointerType==="touch"?this._onTouchStart(i):this._onMouseDown(i),this._cursorStyle==="grab"&&(this.domElement.style.cursor="grabbing")))}function I2(i){this.enabled!==!1&&(i.pointerType==="touch"?this._onTouchMove(i):this._onMouseMove(i))}function L2(i){switch(this._removePointer(i),this._pointers.length){case 0:this.domElement.releasePointerCapture(i.pointerId),this.domElement.ownerDocument.removeEventListener("pointermove",this._onPointerMove),this.domElement.ownerDocument.removeEventListener("pointerup",this._onPointerUp),this.dispatchEvent(Bh),this.state=Ze.NONE,this._cursorStyle==="grab"&&(this.domElement.style.cursor="grab");break;case 1:let e=this._pointers[0],t=this._pointerPositions[e];this._onTouchStart({pointerId:e,pageX:t.x,pageY:t.y});break}}function D2(i){let e;switch(i.button){case 0:e=this.mouseButtons.LEFT;break;case 1:e=this.mouseButtons.MIDDLE;break;case 2:e=this.mouseButtons.RIGHT;break;default:e=-1}switch(e){case $n.DOLLY:if(this.enableZoom===!1)return;this._handleMouseDownDolly(i),this.state=Ze.DOLLY;break;case $n.ROTATE:if(i.ctrlKey||i.metaKey||i.shiftKey){if(this.enablePan===!1)return;this._handleMouseDownPan(i),this.state=Ze.PAN}else{if(this.enableRotate===!1)return;this._handleMouseDownRotate(i),this.state=Ze.ROTATE}break;case $n.PAN:if(i.ctrlKey||i.metaKey||i.shiftKey){if(this.enableRotate===!1)return;this._handleMouseDownRotate(i),this.state=Ze.ROTATE}else{if(this.enablePan===!1)return;this._handleMouseDownPan(i),this.state=Ze.PAN}break;default:this.state=Ze.NONE}this.state!==Ze.NONE&&this.dispatchEvent(vl)}function N2(i){switch(this.state){case Ze.ROTATE:if(this.enableRotate===!1)return;this._handleMouseMoveRotate(i);break;case Ze.DOLLY:if(this.enableZoom===!1)return;this._handleMouseMoveDolly(i);break;case Ze.PAN:if(this.enablePan===!1)return;this._handleMouseMovePan(i);break}}function U2(i){this.enabled===!1||this.enableZoom===!1||this.state!==Ze.NONE||(i.preventDefault(),this.dispatchEvent(vl),this._handleMouseWheel(this._customWheelEvent(i)),this.dispatchEvent(Bh))}function F2(i){this.enabled!==!1&&this._handleKeyDown(i)}function O2(i){switch(this._trackPointer(i),this._pointers.length){case 1:switch(this.touches.ONE){case Kn.ROTATE:if(this.enableRotate===!1){this.state=Ze.NONE;break}this._handleTouchStartRotate(i),this.state=Ze.TOUCH_ROTATE;break;case Kn.PAN:if(this.enablePan===!1){this.state=Ze.NONE;break}this._handleTouchStartPan(i),this.state=Ze.TOUCH_PAN;break;default:this.state=Ze.NONE}break;case 2:switch(this.touches.TWO){case Kn.DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchStartDollyPan(i),this.state=Ze.TOUCH_DOLLY_PAN;break;case Kn.DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchStartDollyRotate(i),this.state=Ze.TOUCH_DOLLY_ROTATE;break;default:this.state=Ze.NONE}break;default:this.state=Ze.NONE}this.state!==Ze.NONE&&this.dispatchEvent(vl)}function B2(i){switch(this._trackPointer(i),this.state){case Ze.TOUCH_ROTATE:if(this.enableRotate===!1)return;this._handleTouchMoveRotate(i),this.update();break;case Ze.TOUCH_PAN:if(this.enablePan===!1)return;this._handleTouchMovePan(i),this.update();break;case Ze.TOUCH_DOLLY_PAN:if(this.enableZoom===!1&&this.enablePan===!1)return;this._handleTouchMoveDollyPan(i),this.update();break;case Ze.TOUCH_DOLLY_ROTATE:if(this.enableZoom===!1&&this.enableRotate===!1)return;this._handleTouchMoveDollyRotate(i),this.update();break;default:this.state=Ze.NONE}}function z2(i){this.enabled!==!1&&i.preventDefault()}function k2(i){i.key==="Control"&&(this._controlActive=!0,this.domElement.ownerDocument.addEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}function G2(i){i.key==="Control"&&(this._controlActive=!1,this.domElement.ownerDocument.removeEventListener("keyup",this._interceptControlUp,{passive:!0,capture:!0}))}var Lt={editions:[{year:1896,city:"\u96C5\u5178",lat:37.98,lon:23.73,records:380,delegations:12,female:0,medalRecords:143},{year:1900,city:"\u5DF4\u9ECE",lat:48.86,lon:2.35,records:1936,delegations:31,female:1.7,medalRecords:604},{year:1904,city:"\u5723\u8DEF\u6613\u65AF",lat:38.63,lon:-90.2,records:1301,delegations:15,female:1.2,medalRecords:486},{year:1908,city:"\u4F26\u6566",lat:51.51,lon:-.13,records:3101,delegations:22,female:1.5,medalRecords:831},{year:1912,city:"\u65AF\u5FB7\u54E5\u5C14\u6469",lat:59.33,lon:18.07,records:4040,delegations:29,female:2.2,medalRecords:941},{year:1920,city:"\u5B89\u7279\u536B\u666E",lat:51.22,lon:4.4,records:4292,delegations:29,female:3.1,medalRecords:1308},{year:1924,city:"\u5DF4\u9ECE",lat:48.86,lon:2.35,records:5233,delegations:45,female:4.7,medalRecords:832},{year:1928,city:"\u963F\u59C6\u65AF\u7279\u4E39",lat:52.37,lon:4.9,records:4992,delegations:46,female:8.1,medalRecords:734},{year:1932,city:"\u6D1B\u6749\u77F6",lat:34.05,lon:-118.24,records:2969,delegations:47,female:11.7,medalRecords:647},{year:1936,city:"\u67CF\u6797",lat:52.52,lon:13.4,records:6506,delegations:49,female:7.2,medalRecords:917},{year:1948,city:"\u4F26\u6566",lat:51.51,lon:-.13,records:6405,delegations:59,female:9.8,medalRecords:852},{year:1952,city:"\u8D6B\u5C14\u8F9B\u57FA",lat:60.17,lon:24.94,records:8270,delegations:69,female:18.1,medalRecords:897},{year:1956,city:"\u58A8\u5C14\u672C",lat:-37.81,lon:144.96,records:5127,delegations:72,female:17.4,medalRecords:893},{year:1960,city:"\u7F57\u9A6C",lat:41.9,lon:12.5,records:8119,delegations:84,female:17.7,medalRecords:911},{year:1964,city:"\u4E1C\u4EAC",lat:35.68,lon:139.69,records:7702,delegations:93,female:17.5,medalRecords:1029},{year:1968,city:"\u58A8\u897F\u54E5\u57CE",lat:19.43,lon:-99.13,records:8588,delegations:112,female:20.7,medalRecords:1057},{year:1972,city:"\u6155\u5C3C\u9ED1",lat:48.14,lon:11.58,records:10304,delegations:121,female:21.3,medalRecords:1215},{year:1976,city:"\u8499\u7279\u5229\u5C14",lat:45.5,lon:-73.57,records:8641,delegations:92,female:25.1,medalRecords:1320},{year:1980,city:"\u83AB\u65AF\u79D1",lat:55.75,lon:37.62,records:7191,delegations:80,female:24.4,medalRecords:1384},{year:1984,city:"\u6D1B\u6749\u77F6",lat:34.05,lon:-118.24,records:9454,delegations:140,female:25.9,medalRecords:1476},{year:1988,city:"\u9996\u5C14",lat:37.56,lon:126.98,records:12037,delegations:159,female:29.4,medalRecords:1582},{year:1992,city:"\u5DF4\u585E\u7F57\u90A3",lat:41.38,lon:2.17,records:12977,delegations:169,female:31.8,medalRecords:1712},{year:1996,city:"\u4E9A\u7279\u5170\u5927",lat:33.75,lon:-84.39,records:13780,delegations:197,female:36.3,medalRecords:1842},{year:2e3,city:"\u6089\u5C3C",lat:-33.87,lon:151.21,records:13821,delegations:200,female:39.3,medalRecords:2004},{year:2004,city:"\u96C5\u5178",lat:37.98,lon:23.73,records:13443,delegations:201,female:41.3,medalRecords:2001},{year:2008,city:"\u5317\u4EAC",lat:39.9,lon:116.4,records:13602,delegations:204,female:42.8,medalRecords:2048},{year:2012,city:"\u4F26\u6566",lat:51.51,lon:-.13,records:12920,delegations:205,female:45,medalRecords:1941},{year:2016,city:"\u91CC\u7EA6\u70ED\u5185\u5362",lat:-22.91,lon:-43.2,records:13688,delegations:207,female:45.5,medalRecords:2023},{year:2020,city:"\u4E1C\u4EAC",lat:35.68,lon:139.69,records:15121,delegations:206,female:48.1,medalRecords:2449},{year:2024,city:"\u5DF4\u9ECE",lat:48.86,lon:2.35,records:14892,delegations:206,female:49.1,medalRecords:2281}],delegationSeries:{USA:[{year:1896,present:!0,medalShare:13.99},{year:1900,present:!0,medalShare:10.43},{year:1904,present:!0,medalShare:81.07},{year:1908,present:!0,medalShare:7.82},{year:1912,present:!0,medalShare:11.37},{year:1920,present:!0,medalShare:14.83},{year:1924,present:!0,medalShare:21.88},{year:1928,present:!0,medalShare:11.99},{year:1932,present:!0,medalShare:29.21},{year:1936,present:!0,medalShare:10.47},{year:1948,present:!0,medalShare:17.84},{year:1952,present:!0,medalShare:14.94},{year:1956,present:!0,medalShare:13.77},{year:1960,present:!0,medalShare:13.72},{year:1964,present:!0,medalShare:16.42},{year:1968,present:!0,medalShare:15.7},{year:1972,present:!0,medalShare:14.07},{year:1976,present:!0,medalShare:12.42},{year:1980,present:!1,medalShare:null},{year:1984,present:!0,medalShare:23.85},{year:1988,present:!0,medalShare:13.08},{year:1992,present:!0,medalShare:13.08},{year:1996,present:!0,medalShare:14.06},{year:2e3,present:!0,medalShare:12.08},{year:2004,present:!0,medalShare:13.14},{year:2008,present:!0,medalShare:15.48},{year:2012,present:!0,medalShare:12.78},{year:2016,present:!0,medalShare:13.05},{year:2020,present:!0,medalShare:12.17},{year:2024,present:!0,medalShare:14.07}],GBR:[{year:1896,present:!0,medalShare:6.29},{year:1900,present:!0,medalShare:17.88},{year:1904,present:!0,medalShare:.41},{year:1908,present:!0,medalShare:44.28},{year:1912,present:!0,medalShare:18.07},{year:1920,present:!0,medalShare:8.49},{year:1924,present:!0,medalShare:7.69},{year:1928,present:!0,medalShare:7.9},{year:1932,present:!0,medalShare:5.41},{year:1936,present:!0,medalShare:3.93},{year:1948,present:!0,medalShare:7.16},{year:1952,present:!0,medalShare:3.46},{year:1956,present:!0,medalShare:5.15},{year:1960,present:!0,medalShare:3.07},{year:1964,present:!0,medalShare:2.72},{year:1968,present:!0,medalShare:1.8},{year:1972,present:!0,medalShare:2.39},{year:1976,present:!0,medalShare:2.42},{year:1980,present:!0,medalShare:3.4},{year:1984,present:!0,medalShare:4.81},{year:1988,present:!0,medalShare:3.41},{year:1992,present:!0,medalShare:2.92},{year:1996,present:!0,medalShare:1.41},{year:2e3,present:!0,medalShare:2.69},{year:2004,present:!0,medalShare:2.85},{year:2008,present:!0,medalShare:3.96},{year:2012,present:!0,medalShare:6.49},{year:2016,present:!0,medalShare:7.17},{year:2020,present:!0,medalShare:5.76},{year:2024,present:!0,medalShare:6.84}],URS:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!1,medalShare:null},{year:1932,present:!1,medalShare:null},{year:1936,present:!1,medalShare:null},{year:1948,present:!1,medalShare:null},{year:1952,present:!0,medalShare:13.04},{year:1956,present:!0,medalShare:18.92},{year:1960,present:!0,medalShare:18.55},{year:1964,present:!0,medalShare:16.91},{year:1968,present:!0,medalShare:18.16},{year:1972,present:!0,medalShare:17.61},{year:1976,present:!0,medalShare:21.67},{year:1980,present:!0,medalShare:31.94},{year:1984,present:!1,medalShare:null},{year:1988,present:!0,medalShare:18.96},{year:1992,present:!1,medalShare:null},{year:1996,present:!1,medalShare:null},{year:2e3,present:!1,medalShare:null},{year:2004,present:!1,medalShare:null},{year:2008,present:!1,medalShare:null},{year:2012,present:!1,medalShare:null},{year:2016,present:!1,medalShare:null},{year:2020,present:!1,medalShare:null},{year:2024,present:!1,medalShare:null}],GDR:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!1,medalShare:null},{year:1932,present:!1,medalShare:null},{year:1936,present:!1,medalShare:null},{year:1948,present:!1,medalShare:null},{year:1952,present:!1,medalShare:null},{year:1956,present:!1,medalShare:null},{year:1960,present:!1,medalShare:null},{year:1964,present:!1,medalShare:null},{year:1968,present:!0,medalShare:4.92},{year:1972,present:!0,medalShare:12.43},{year:1976,present:!0,medalShare:14.77},{year:1980,present:!0,medalShare:19.08},{year:1984,present:!1,medalShare:null},{year:1988,present:!0,medalShare:11.44},{year:1992,present:!1,medalShare:null},{year:1996,present:!1,medalShare:null},{year:2e3,present:!1,medalShare:null},{year:2004,present:!1,medalShare:null},{year:2008,present:!1,medalShare:null},{year:2012,present:!1,medalShare:null},{year:2016,present:!1,medalShare:null},{year:2020,present:!1,medalShare:null},{year:2024,present:!1,medalShare:null}],FRG:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!1,medalShare:null},{year:1932,present:!1,medalShare:null},{year:1936,present:!1,medalShare:null},{year:1948,present:!1,medalShare:null},{year:1952,present:!1,medalShare:null},{year:1956,present:!1,medalShare:null},{year:1960,present:!1,medalShare:null},{year:1964,present:!1,medalShare:null},{year:1968,present:!0,medalShare:4.82},{year:1972,present:!0,medalShare:8.4},{year:1976,present:!0,medalShare:5.91},{year:1980,present:!1,medalShare:null},{year:1984,present:!0,medalShare:10.7},{year:1988,present:!0,medalShare:7.27},{year:1992,present:!1,medalShare:null},{year:1996,present:!1,medalShare:null},{year:2e3,present:!1,medalShare:null},{year:2004,present:!1,medalShare:null},{year:2008,present:!1,medalShare:null},{year:2012,present:!1,medalShare:null},{year:2016,present:!1,medalShare:null},{year:2020,present:!1,medalShare:null},{year:2024,present:!1,medalShare:null}],GER:[{year:1896,present:!0,medalShare:22.38},{year:1900,present:!0,medalShare:7.45},{year:1904,present:!0,medalShare:3.29},{year:1908,present:!0,medalShare:2.53},{year:1912,present:!0,medalShare:5.63},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!0,medalShare:10.49},{year:1932,present:!0,medalShare:6.65},{year:1936,present:!0,medalShare:24.43},{year:1948,present:!1,medalShare:null},{year:1952,present:!0,medalShare:4.46},{year:1956,present:!0,medalShare:5.82},{year:1960,present:!0,medalShare:9.77},{year:1964,present:!0,medalShare:11.27},{year:1968,present:!1,medalShare:null},{year:1972,present:!1,medalShare:null},{year:1976,present:!1,medalShare:null},{year:1980,present:!1,medalShare:null},{year:1984,present:!1,medalShare:null},{year:1988,present:!1,medalShare:null},{year:1992,present:!0,medalShare:11.57},{year:1996,present:!0,medalShare:6.73},{year:2e3,present:!0,medalShare:5.89},{year:2004,present:!0,medalShare:7.45},{year:2008,present:!0,medalShare:4.83},{year:2012,present:!0,medalShare:4.84},{year:2016,present:!0,medalShare:7.86},{year:2020,present:!0,medalShare:3.31},{year:2024,present:!0,medalShare:4.73}],CHN:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!1,medalShare:null},{year:1932,present:!0,medalShare:0},{year:1936,present:!0,medalShare:0},{year:1948,present:!0,medalShare:0},{year:1952,present:!0,medalShare:0},{year:1956,present:!1,medalShare:null},{year:1960,present:!1,medalShare:null},{year:1964,present:!1,medalShare:null},{year:1968,present:!1,medalShare:null},{year:1972,present:!1,medalShare:null},{year:1976,present:!1,medalShare:null},{year:1980,present:!1,medalShare:null},{year:1984,present:!0,medalShare:5.01},{year:1988,present:!0,medalShare:3.29},{year:1992,present:!0,medalShare:4.79},{year:1996,present:!0,medalShare:5.75},{year:2e3,present:!0,medalShare:3.94},{year:2004,present:!0,medalShare:4.7},{year:2008,present:!0,medalShare:8.98},{year:2012,present:!0,medalShare:6.44},{year:2016,present:!0,medalShare:5.59},{year:2020,present:!0,medalShare:5.76},{year:2024,present:!0,medalShare:7.37}],JPN:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!0,medalShare:0},{year:1920,present:!0,medalShare:.23},{year:1924,present:!0,medalShare:.12},{year:1928,present:!0,medalShare:1.23},{year:1932,present:!0,medalShare:4.79},{year:1936,present:!0,medalShare:2.51},{year:1948,present:!1,medalShare:null},{year:1952,present:!0,medalShare:1.34},{year:1956,present:!0,medalShare:2.69},{year:1960,present:!0,medalShare:3.4},{year:1964,present:!0,medalShare:6.03},{year:1968,present:!0,medalShare:5.96},{year:1972,present:!0,medalShare:4.61},{year:1976,present:!0,medalShare:3.11},{year:1980,present:!1,medalShare:null},{year:1984,present:!0,medalShare:3.32},{year:1988,present:!0,medalShare:1.26},{year:1992,present:!0,medalShare:2.75},{year:1996,present:!0,medalShare:2.28},{year:2e3,present:!0,medalShare:2.2},{year:2004,present:!0,medalShare:4.65},{year:2008,present:!0,medalShare:2.49},{year:2012,present:!0,medalShare:4.33},{year:2016,present:!0,medalShare:3.16},{year:2020,present:!0,medalShare:5.35},{year:2024,present:!0,medalShare:3.59}],KOR:[{year:1896,present:!1,medalShare:null},{year:1900,present:!1,medalShare:null},{year:1904,present:!1,medalShare:null},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!1,medalShare:null},{year:1924,present:!1,medalShare:null},{year:1928,present:!1,medalShare:null},{year:1932,present:!1,medalShare:null},{year:1936,present:!1,medalShare:null},{year:1948,present:!0,medalShare:.23},{year:1952,present:!0,medalShare:.22},{year:1956,present:!0,medalShare:.22},{year:1960,present:!0,medalShare:0},{year:1964,present:!0,medalShare:.29},{year:1968,present:!0,medalShare:.19},{year:1972,present:!0,medalShare:.08},{year:1976,present:!0,medalShare:1.29},{year:1980,present:!1,medalShare:null},{year:1984,present:!0,medalShare:2.78},{year:1988,present:!0,medalShare:4.87},{year:1992,present:!0,medalShare:2.86},{year:1996,present:!0,medalShare:3.58},{year:2e3,present:!0,medalShare:3.64},{year:2004,present:!0,medalShare:2.6},{year:2008,present:!0,medalShare:3.81},{year:2012,present:!0,medalShare:3.14},{year:2016,present:!0,medalShare:1.29},{year:2020,present:!0,medalShare:1.55},{year:2024,present:!0,medalShare:2.54}],AUS:[{year:1896,present:!0,medalShare:2.1},{year:1900,present:!0,medalShare:.99},{year:1904,present:!0,medalShare:.82},{year:1908,present:!1,medalShare:null},{year:1912,present:!1,medalShare:null},{year:1920,present:!0,medalShare:.54},{year:1924,present:!0,medalShare:1.2},{year:1928,present:!0,medalShare:.54},{year:1932,present:!0,medalShare:.77},{year:1936,present:!0,medalShare:.11},{year:1948,present:!0,medalShare:1.88},{year:1952,present:!0,medalShare:2.23},{year:1956,present:!0,medalShare:7.5},{year:1960,present:!0,medalShare:5.05},{year:1964,present:!0,medalShare:4.28},{year:1968,present:!0,medalShare:4.82},{year:1972,present:!0,medalShare:1.65},{year:1976,present:!0,medalShare:1.74},{year:1980,present:!0,medalShare:.94},{year:1984,present:!0,medalShare:3.52},{year:1988,present:!0,medalShare:2.21},{year:1992,present:!0,medalShare:3.33},{year:1996,present:!0,medalShare:7.17},{year:2e3,present:!0,medalShare:9.13},{year:2004,present:!0,medalShare:7.85},{year:2008,present:!0,medalShare:7.28},{year:2012,present:!0,medalShare:5.87},{year:2016,present:!0,medalShare:4.05},{year:2020,present:!0,medalShare:5.35},{year:2024,present:!0,medalShare:5.3}],FRA:[{year:1896,present:!0,medalShare:7.69},{year:1900,present:!0,medalShare:38.91},{year:1904,present:!0,medalShare:.41},{year:1908,present:!0,medalShare:4.81},{year:1912,present:!0,medalShare:2.76},{year:1920,present:!0,medalShare:10.78},{year:1924,present:!0,medalShare:13.22},{year:1928,present:!0,medalShare:6.81},{year:1932,present:!0,medalShare:6.18},{year:1936,present:!0,medalShare:4.8},{year:1948,present:!0,medalShare:8.45},{year:1952,present:!0,medalShare:4.46},{year:1956,present:!0,medalShare:3.7},{year:1960,present:!0,medalShare:1.32},{year:1964,present:!0,medalShare:3.01},{year:1968,present:!0,medalShare:2.55},{year:1972,present:!0,medalShare:1.81},{year:1976,present:!0,medalShare:1.52},{year:1980,present:!0,medalShare:2.1},{year:1984,present:!0,medalShare:4.54},{year:1988,present:!0,medalShare:1.83},{year:1992,present:!0,medalShare:3.33},{year:1996,present:!0,medalShare:2.77},{year:2e3,present:!0,medalShare:3.29},{year:2004,present:!0,medalShare:2.65},{year:2008,present:!0,medalShare:3.76},{year:2012,present:!0,medalShare:4.22},{year:2016,present:!0,medalShare:4.75},{year:2020,present:!0,medalShare:5.76},{year:2024,present:!0,medalShare:8.2}],NED:[{year:1896,present:!1,medalShare:null},{year:1900,present:!0,medalShare:4.47},{year:1904,present:!1,medalShare:null},{year:1908,present:!0,medalShare:1.93},{year:1912,present:!0,medalShare:2.76},{year:1920,present:!0,medalShare:3.82},{year:1924,present:!0,medalShare:3.25},{year:1928,present:!0,medalShare:7.77},{year:1932,present:!0,medalShare:2.01},{year:1936,present:!0,medalShare:4.03},{year:1948,present:!0,medalShare:4.93},{year:1952,present:!0,medalShare:2.01},{year:1956,present:!0,medalShare:0},{year:1960,present:!0,medalShare:.33},{year:1964,present:!0,medalShare:3.01},{year:1968,present:!0,medalShare:1.32},{year:1972,present:!0,medalShare:.49},{year:1976,present:!0,medalShare:1.06},{year:1980,present:!0,medalShare:.43},{year:1984,present:!0,medalShare:2.78},{year:1988,present:!0,medalShare:2.84},{year:1992,present:!0,medalShare:1.93},{year:1996,present:!0,medalShare:3.96},{year:2e3,present:!0,medalShare:3.94},{year:2004,present:!0,medalShare:3.85},{year:2008,present:!0,medalShare:2.98},{year:2012,present:!0,medalShare:3.55},{year:2016,present:!0,medalShare:2.32},{year:2020,present:!0,medalShare:2.94},{year:2024,present:!0,medalShare:5.17}]},nocNames:{USA:"\u7F8E\u56FD",CHN:"\u4E2D\u56FD",GBR:"\u82F1\u56FD",JPN:"\u65E5\u672C",AUS:"\u6FB3\u5927\u5229\u4E9A",FRA:"\u6CD5\u56FD",GER:"\u5FB7\u56FD",FRG:"\u897F\u5FB7",GDR:"\u4E1C\u5FB7",URS:"\u82CF\u8054",KOR:"\u97E9\u56FD",NED:"\u8377\u5170"},sportSeries:[{key:"Tug-Of-War",name:"\u62D4\u6CB3",present:[0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Croquet",name:"\u69CC\u7403",present:[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Art Competitions",name:"\u827A\u672F\u7ADE\u8D5B",present:[0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Polo",name:"\u9A6C\u7403",present:[0,1,0,1,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Figure Skating",name:"\u82B1\u6837\u6ED1\u51B0",present:[0,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Ice Hockey",name:"\u51B0\u7403",present:[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]},{key:"Taekwondo",name:"\u8DC6\u62F3\u9053",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]},{key:"Triathlon",name:"\u94C1\u4EBA\u4E09\u9879",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]},{key:"Rugby",name:"\u6A44\u6984\u7403",present:[0,1,0,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]},{key:"Skateboarding",name:"\u6ED1\u677F",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]},{key:"Surfing",name:"\u51B2\u6D6A",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]},{key:"Sport Climbing",name:"\u8FD0\u52A8\u6500\u5CA9",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]},{key:"Breaking",name:"\u9739\u96F3\u821E",present:[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]}],geography:[[[178.12,-17.51],[178.37,-17.34],[178.72,-17.63],[178.55,-18.15],[177.93,-18.29],[177.38,-18.16],[177.29,-17.72],[177.67,-17.38],[178.12,-17.51]],[[-180,-16.07],[-179.79,-16.02],[-179.92,-16.5],[-180,-16.56],[179.36,-16.8],[178.73,-17.01],[178.6,-16.64],[179.1,-16.43],[179.41,-16.38],[180,-16.07],[-180,-16.07]],[[33.9,-.95],[34.07,-1.06],[37.7,-3.1],[37.77,-3.68],[39.2,-4.68],[38.74,-5.91],[38.8,-6.48],[39.44,-6.84],[39.47,-7.1],[39.2,-7.7],[39.25,-8.01],[39.19,-8.49],[39.54,-9.11],[39.95,-10.1],[40.32,-10.32],[39.52,-10.9],[38.43,-11.29],[37.83,-11.27],[37.47,-11.57],[36.78,-11.6],[36.51,-11.72],[35.31,-11.44],[34.56,-11.52],[34.28,-10.16],[33.94,-9.69],[33.74,-9.42],[32.76,-9.23],[32.19,-8.93],[31.56,-8.76],[31.16,-8.59],[30.74,-8.34],[30.2,-7.08],[29.62,-6.52],[29.42,-5.94],[29.52,-5.42],[29.34,-4.5],[29.75,-4.45],[30.12,-4.09],[30.5,-3.57],[30.75,-3.36],[30.74,-3.03],[30.53,-2.81],[30.47,-2.41],[30.76,-2.29],[30.81,-1.7],[30.42,-1.14],[30.77,-1.01],[31.87,-1.03],[33.9,-.95]],[[-8.67,27.66],[-8.66,27.59],[-8.69,27.4],[-8.69,25.88],[-11.97,25.93],[-11.94,23.37],[-12.88,23.29],[-13.12,22.77],[-12.93,21.33],[-16.85,21.33],[-17.06,21],[-17.02,21.42],[-17,21.42],[-14.75,21.5],[-14.63,21.86],[-14.22,22.31],[-13.89,23.69],[-12.5,24.77],[-12.03,26.03],[-11.72,26.1],[-11.39,26.88],[-10.55,26.99],[-10.19,26.86],[-9.74,26.86],[-9.41,27.09],[-8.79,27.12],[-8.82,27.66],[-8.67,27.66]],[[-122.84,49],[-122.98,49],[-124.91,49.99],[-125.63,50.42],[-127.44,50.83],[-127.99,51.72],[-127.85,52.33],[-129.13,52.76],[-129.3,53.56],[-130.51,54.29],[-130.54,54.8],[-129.98,55.28],[-130.01,55.92],[-131.71,56.55],[-132.73,57.69],[-133.35,58.41],[-134.27,58.86],[-134.95,59.27],[-135.47,59.79],[-136.48,59.46],[-137.45,58.91],[-138.34,59.56],[-139.04,60],[-140.01,60.28],[-141,60.31],[-140.99,66],[-140.99,69.71],[-139.12,69.47],[-137.54,68.99],[-136.5,68.9],[-135.63,69.32],[-134.42,69.63],[-132.93,69.51],[-131.43,69.94],[-129.79,70.19],[-129.11,69.78],[-128.36,70.01],[-128.14,70.48],[-127.45,70.38],[-125.75,69.48],[-124.43,70.16],[-124.29,69.4],[-123.06,69.56],[-122.68,69.86],[-121.47,69.8],[-119.94,69.38],[-117.6,69.01],[-116.23,68.84],[-115.25,68.91],[-113.9,68.4],[-115.3,67.9],[-113.5,67.69],[-110.8,67.81],[-109.95,67.98],[-108.88,67.38],[-107.79,67.89],[-108.81,68.31],[-108.17,68.65],[-106.95,68.7],[-106.15,68.8],[-105.34,68.56],[-104.34,68.02],[-103.22,68.1],[-101.45,67.65],[-99.9,67.81],[-98.44,67.78],[-98.56,68.4],[-97.67,68.58],[-96.12,68.24],[-96.13,67.29],[-95.49,68.09],[-94.69,68.06],[-94.23,69.07],[-95.31,69.68],[-96.47,70.09],[-96.39,71.19],[-95.21,71.92],[-93.89,71.76],[-92.88,71.32],[-91.52,70.19],[-92.41,69.7],[-90.55,69.5],[-90.55,68.47],[-89.21,69.26],[-88.02,68.62],[-88.32,67.87],[-87.35,67.2],[-86.31,67.92],[-85.58,68.78],[-85.52,69.88],[-84.1,69.81],[-82.62,69.66],[-81.28,69.16],[-81.22,68.67],[-81.96,68.13],[-81.26,67.6],[-81.39,67.11],[-83.35,66.41],[-84.74,66.26],[-85.77,66.56],[-86.07,66.06],[-87.03,65.21],[-87.32,64.77],[-88.48,64.1],[-89.91,64.03],[-90.7,63.61],[-90.77,62.96],[-91.93,62.84],[-93.16,62.02],[-94.24,60.9],[-94.63,60.11],[-94.69,58.95],[-93.21,58.78],[-92.76,57.85],[-92.3,57.09],[-90.9,57.29],[-89.04,56.85],[-88.04,56.47],[-87.32,56],[-86.07,55.72],[-85.01,55.3],[-83.36,55.25],[-82.27,55.15],[-82.44,54.28],[-82.13,53.28],[-81.4,52.16],[-79.91,51.21],[-79.14,51.53],[-78.6,52.56],[-79.12,54.14],[-79.83,54.67],[-78.23,55.14],[-77.1,55.84],[-76.54,56.53],[-76.62,57.2],[-77.3,58.05],[-78.52,58.81],[-77.34,59.85],[-77.77,60.76],[-78.11,62.32],[-77.41,62.55],[-75.7,62.28],[-74.67,62.18],[-73.84,62.44],[-72.91,62.11],[-71.68,61.53],[-71.37,61.14],[-69.59,61.06],[-69.62,60.22],[-69.29,58.96],[-68.37,58.8],[-67.65,58.21],[-66.2,58.77],[-65.25,59.87],[-64.58,60.34],[-63.81,59.44],[-62.5,58.17],[-61.4,56.97],[-61.8,56.34],[-60.47,55.78],[-59.57,55.2],[-57.98,54.95],[-57.33,54.63],[-56.94,53.78],[-56.16,53.65],[-55.76,53.27],[-55.68,52.15],[-56.41,51.77],[-57.13,51.42],[-58.78,51.07],[-60.03,50.24],[-61.72,50.08],[-63.86,50.29],[-65.36,50.3],[-66.4,50.23],[-67.24,49.51],[-68.51,49.07],[-69.95,47.74],[-71.11,46.82],[-70.26,46.99],[-68.65,48.3],[-66.55,49.13],[-65.06,49.23],[-64.17,48.74],[-65.12,48.07],[-64.8,46.99],[-64.47,46.24],[-63.17,45.74],[-61.52,45.88],[-60.52,47.01],[-60.45,46.28],[-59.8,45.92],[-61.04,45.26],[-63.25,44.67],[-64.25,44.27],[-65.36,43.55],[-66.12,43.62],[-66.16,44.47],[-64.42,45.29],[-66.03,45.26],[-67.14,45.14],[-67.79,45.7],[-67.79,47.07],[-68.23,47.35],[-68.91,47.19],[-69.24,47.45],[-70,46.69],[-70.3,45.91],[-70.66,45.46],[-71.08,45.31],[-71.4,45.25],[-71.51,45.01],[-73.35,45.01],[-74.87,45],[-75.32,44.82],[-76.38,44.1],[-76.5,44.02],[-76.82,43.63],[-77.74,43.63],[-78.72,43.62],[-79.17,43.47],[-79.01,43.27],[-78.92,42.96],[-78.94,42.86],[-80.25,42.37],[-81.28,42.21],[-82.44,41.67],[-82.69,41.67],[-83.03,41.83],[-83.14,41.98],[-83.12,42.08],[-82.9,42.43],[-82.43,42.98],[-82.14,43.57],[-82.34,44.44],[-82.55,45.35],[-83.59,45.82],[-83.47,45.99],[-83.62,46.12],[-83.89,46.12],[-84.09,46.28],[-84.14,46.51],[-84.34,46.41],[-84.61,46.44],[-84.55,46.54],[-84.78,46.64],[-84.88,46.9],[-85.65,47.22],[-86.46,47.55],[-87.44,47.94],[-88.38,48.3],[-89.27,48.02],[-89.6,48.01],[-90.83,48.27],[-91.64,48.14],[-92.61,48.45],[-93.63,48.61],[-94.33,48.67],[-94.64,48.84],[-94.82,49.39],[-95.15,49.38],[-95.16,49],[-97.23,49],[-100.65,49],[-104.05,49],[-107.05,49],[-110.05,49],[-113,49],[-116.05,49],[-117.03,49],[-120,49],[-122.84,49]],[[-83.99,62.45],[-83.25,62.91],[-81.88,62.9],[-81.9,62.71],[-83.07,62.16],[-83.77,62.18],[-83.99,62.45]],[[-79.77,72.8],[-80.88,73.33],[-80.83,73.69],[-80.35,73.76],[-78.06,73.65],[-76.34,73.1],[-76.25,72.83],[-77.32,72.86],[-78.39,72.88],[-79.49,72.74],[-79.77,72.8]],[[-80.32,62.09],[-79.93,62.38],[-79.52,62.36],[-79.27,62.16],[-79.66,61.63],[-80.1,61.72],[-80.36,62.02],[-80.32,62.09]],[[-93.61,74.98],[-94.16,74.59],[-95.61,74.67],[-96.82,74.93],[-96.29,75.38],[-94.85,75.65],[-93.98,75.3],[-93.61,74.98]],[[-93.84,77.52],[-94.29,77.49],[-96.17,77.56],[-96.44,77.83],[-94.42,77.82],[-93.72,77.63],[-93.84,77.52]],[[-96.75,78.77],[-95.56,78.42],[-95.83,78.06],[-97.31,77.85],[-98.12,78.08],[-98.55,78.46],[-98.63,78.87],[-97.34,78.83],[-96.75,78.77]],[[-88.15,74.39],[-89.77,74.52],[-92.42,74.84],[-92.77,75.39],[-92.89,75.88],[-93.89,76.32],[-95.96,76.44],[-97.12,76.75],[-96.75,77.16],[-94.68,77.1],[-93.57,76.78],[-91.6,76.78],[-90.74,76.45],[-90.97,76.07],[-89.82,75.85],[-89.19,75.61],[-87.84,75.57],[-86.38,75.48],[-84.79,75.7],[-82.75,75.78],[-81.13,75.71],[-80.06,75.34],[-79.83,74.92],[-80.46,74.66],[-81.95,74.44],[-83.23,74.56],[-86.1,74.41],[-88.15,74.39]],[[-111.26,78.15],[-109.85,78],[-110.19,77.7],[-112.05,77.41],[-113.53,77.73],[-112.73,78.05],[-111.26,78.15]],[[-110.96,78.8],[-109.66,78.6],[-110.88,78.41],[-112.54,78.41],[-112.52,78.55],[-111.5,78.85],[-110.96,78.8]],[[-55.6,51.32],[-56.13,50.69],[-56.8,49.81],[-56.14,50.15],[-55.47,49.94],[-55.82,49.59],[-54.93,49.31],[-54.47,49.56],[-53.48,49.25],[-53.79,48.52],[-53.09,48.69],[-52.96,48.16],[-52.65,47.54],[-53.07,46.66],[-53.52,46.62],[-54.18,46.81],[-53.96,47.63],[-54.24,47.75],[-55.4,46.88],[-56,46.92],[-55.29,47.39],[-56.25,47.63],[-57.33,47.57],[-59.27,47.6],[-59.42,47.9],[-58.8,48.25],[-59.23,48.52],[-58.39,49.13],[-57.36,50.72],[-56.74,51.29],[-55.87,51.63],[-55.41,51.59],[-55.6,51.32]],[[-83.88,65.11],[-82.79,64.77],[-81.64,64.45],[-81.55,63.98],[-80.82,64.06],[-80.1,63.73],[-80.99,63.41],[-82.55,63.65],[-83.11,64.1],[-84.1,63.57],[-85.52,63.05],[-85.87,63.64],[-87.22,63.54],[-86.35,64.04],[-86.23,64.82],[-85.88,65.74],[-85.16,65.66],[-84.98,65.22],[-84.46,65.37],[-83.88,65.11]],[[-78.77,72.35],[-77.82,72.75],[-75.61,72.24],[-74.23,71.77],[-74.1,71.33],[-72.24,71.56],[-71.2,70.92],[-68.79,70.52],[-67.92,70.12],[-66.97,69.19],[-68.81,68.72],[-66.45,68.07],[-64.86,67.85],[-63.42,66.93],[-61.85,66.86],[-62.16,66.16],[-63.92,65],[-65.15,65.43],[-66.72,66.39],[-68.01,66.26],[-68.14,65.69],[-67.09,65.11],[-65.73,64.65],[-65.32,64.38],[-64.67,63.39],[-65.01,62.67],[-66.27,62.95],[-68.78,63.75],[-67.37,62.88],[-66.33,62.28],[-66.17,61.93],[-68.88,62.33],[-71.02,62.91],[-72.24,63.4],[-71.89,63.68],[-73.38,64.19],[-74.84,64.68],[-74.82,64.39],[-77.71,64.23],[-78.55,64.57],[-77.9,65.31],[-76.02,65.33],[-73.96,65.46],[-74.29,65.81],[-73.95,66.31],[-72.65,67.28],[-72.93,67.73],[-73.31,68.07],[-74.84,68.55],[-76.87,68.89],[-76.23,69.15],[-77.29,69.77],[-78.17,69.83],[-78.96,70.17],[-79.49,69.87],[-81.31,69.74],[-84.94,69.97],[-87.06,70.26],[-88.68,70.41],[-89.51,70.76],[-88.47,71.22],[-89.89,71.22],[-90.2,72.24],[-89.44,73.13],[-88.41,73.54],[-85.83,73.8],[-86.56,73.16],[-85.77,72.53],[-84.85,73.34],[-82.32,73.75],[-80.6,72.72],[-80.75,72.06],[-78.77,72.35]],[[-94.5,74.13],[-92.42,74.1],[-90.51,73.86],[-92,72.97],[-93.2,72.77],[-94.27,72.02],[-95.41,72.06],[-96.03,72.94],[-96.02,73.44],[-95.5,73.86],[-94.5,74.13]],[[-122.86,76.12],[-121.16,76.86],[-119.11,77.51],[-117.57,77.5],[-116.2,77.65],[-116.34,76.88],[-117.11,76.53],[-118.04,76.48],[-119.9,76.05],[-121.5,75.9],[-122.86,76.12]],[[-132.71,54.04],[-131.75,54.12],[-132.05,52.98],[-131.18,52.18],[-131.58,52.18],[-132.18,52.64],[-132.55,53.1],[-133.06,53.41],[-133.24,53.85],[-133.18,54.17],[-132.71,54.04]],[[-105.49,79.3],[-103.53,79.16],[-100.82,78.8],[-100.06,78.33],[-99.67,77.91],[-101.3,78.02],[-102.95,78.34],[-105.18,78.38],[-104.21,78.68],[-105.42,78.92],[-105.49,79.3]],[[-123.51,48.51],[-124.01,48.37],[-125.65,48.83],[-125.96,49.18],[-126.85,49.53],[-127.03,49.81],[-128.06,50],[-128.44,50.54],[-128.36,50.77],[-127.31,50.55],[-126.69,50.4],[-125.75,50.29],[-125.42,49.95],[-124.92,49.48],[-123.92,49.06],[-123.51,48.51]],[[-121.54,74.45],[-120.11,74.24],[-117.56,74.19],[-116.59,73.9],[-115.51,73.47],[-116.77,73.22],[-119.22,72.52],[-120.46,71.82],[-120.46,71.38],[-123.09,70.9],[-123.62,71.34],[-125.93,71.87],[-125.5,72.29],[-124.81,73.02],[-123.94,73.68],[-124.92,74.29],[-121.54,74.45]],[[-107.82,75.85],[-106.93,76.01],[-105.88,75.97],[-105.71,75.48],[-106.31,75],[-109.7,74.85],[-112.22,74.42],[-113.74,74.39],[-113.87,74.72],[-111.79,75.16],[-116.31,75.04],[-117.71,75.22],[-116.35,76.2],[-115.4,76.48],[-112.59,76.14],[-110.81,75.55],[-109.07,75.47],[-110.5,76.43],[-109.58,76.79],[-108.55,76.68],[-108.21,76.2],[-107.82,75.85]],[[-106.52,73.08],[-105.4,72.67],[-104.77,71.7],[-104.46,70.99],[-102.79,70.5],[-100.98,70.03],[-101.09,69.59],[-102.73,69.5],[-102.09,69.12],[-102.43,68.75],[-104.24,68.91],[-105.96,69.18],[-107.12,69.12],[-109,68.78],[-111.53,68.63],[-113.31,68.54],[-113.86,69.01],[-115.22,69.28],[-116.11,69.17],[-117.34,69.96],[-116.68,70.07],[-115.13,70.24],[-113.72,70.19],[-112.42,70.37],[-114.35,70.6],[-116.49,70.52],[-117.91,70.54],[-118.43,70.91],[-116.11,71.31],[-117.65,71.29],[-119.4,71.56],[-118.56,72.31],[-117.87,72.71],[-115.19,73.31],[-114.17,73.12],[-114.67,72.65],[-112.44,72.95],[-111.05,72.45],[-109.92,72.96],[-109.01,72.63],[-108.19,71.65],[-107.69,72.06],[-108.4,73.09],[-107.52,73.24],[-106.52,73.08]],[[-100.44,72.71],[-101.54,73.36],[-100.36,73.84],[-99.16,73.63],[-97.38,73.76],[-97.12,73.47],[-98.05,72.99],[-96.54,72.56],[-96.72,71.66],[-98.36,71.27],[-99.32,71.36],[-100.01,71.74],[-102.5,72.51],[-102.48,72.83],[-100.44,72.71]],[[-106.6,73.6],[-105.26,73.64],[-104.5,73.42],[-105.38,72.76],[-106.94,73.46],[-106.6,73.6]],[[-98.5,76.72],[-97.74,76.26],[-97.7,75.74],[-98.16,75],[-99.81,74.9],[-100.88,75.06],[-100.86,75.64],[-102.5,75.56],[-102.57,76.34],[-101.49,76.31],[-99.98,76.65],[-98.58,76.59],[-98.5,76.72]],[[-96.01,80.6],[-95.32,80.91],[-94.3,80.98],[-94.74,81.21],[-92.41,81.26],[-91.13,80.72],[-89.45,80.51],[-87.81,80.32],[-87.02,79.66],[-85.82,79.34],[-87.19,79.04],[-89.03,78.29],[-90.81,78.22],[-92.88,78.34],[-93.95,78.75],[-93.94,79.11],[-93.15,79.38],[-94.97,79.37],[-96.08,79.7],[-96.71,80.16],[-96.01,80.6]],[[-91.59,81.9],[-90.1,82.08],[-88.93,82.12],[-86.97,82.28],[-85.5,82.65],[-84.26,82.6],[-83.18,82.32],[-82.42,82.86],[-81.1,83.02],[-79.31,83.13],[-76.25,83.17],[-75.72,83.06],[-72.83,83.23],[-70.67,83.17],[-68.5,83.11],[-65.83,83.03],[-63.68,82.9],[-61.85,82.63],[-61.89,82.36],[-64.33,81.93],[-66.75,81.73],[-67.66,81.5],[-65.48,81.51],[-67.84,80.9],[-69.47,80.62],[-71.18,79.8],[-73.24,79.63],[-73.88,79.43],[-76.91,79.32],[-75.53,79.2],[-76.22,79.02],[-75.39,78.53],[-76.34,78.18],[-77.89,77.9],[-78.36,77.51],[-79.76,77.21],[-79.62,76.98],[-77.91,77.02],[-77.89,76.78],[-80.56,76.18],[-83.17,76.45],[-86.11,76.3],[-87.6,76.42],[-89.49,76.47],[-89.62,76.95],[-87.77,77.18],[-88.26,77.9],[-87.65,77.97],[-84.98,77.54],[-86.34,78.18],[-87.96,78.37],[-87.15,78.76],[-85.38,79],[-85.1,79.35],[-86.51,79.74],[-86.93,80.25],[-84.2,80.21],[-83.41,80.1],[-81.85,80.46],[-84.1,80.58],[-87.6,80.52],[-89.37,80.86],[-90.2,81.26],[-91.37,81.55],[-91.59,81.9]],[[-75.22,67.44],[-75.87,67.15],[-76.99,67.1],[-77.24,67.59],[-76.81,68.15],[-75.89,68.29],[-75.11,68.01],[-75.1,67.58],[-75.22,67.44]],[[-96.26,69.49],[-95.65,69.11],[-96.27,68.76],[-97.62,69.06],[-98.43,68.95],[-99.8,69.4],[-98.92,69.71],[-98.22,70.14],[-97.16,69.86],[-96.56,69.68],[-96.26,69.49]],[[-64.52,49.87],[-64.17,49.96],[-62.86,49.71],[-61.84,49.29],[-61.81,49.11],[-62.29,49.09],[-63.59,49.4],[-64.52,49.87]],[[-64.01,47.04],[-63.66,46.55],[-62.94,46.42],[-62.01,46.44],[-62.51,46.03],[-62.87,45.97],[-64.14,46.39],[-64.39,46.73],[-64.01,47.04]],[[-122.84,49],[-120,49],[-117.03,49],[-116.05,49],[-113,49],[-110.05,49],[-107.05,49],[-104.05,49],[-100.65,49],[-97.23,49],[-95.16,49],[-95.15,49.38],[-94.82,49.39],[-94.64,48.84],[-94.33,48.67],[-93.63,48.61],[-92.61,48.45],[-91.64,48.14],[-90.83,48.27],[-89.6,48.01],[-89.27,48.02],[-88.38,48.3],[-87.44,47.94],[-86.46,47.55],[-85.65,47.22],[-84.88,46.9],[-84.78,46.64],[-84.55,46.54],[-84.61,46.44],[-84.34,46.41],[-84.14,46.51],[-84.09,46.28],[-83.89,46.12],[-83.62,46.12],[-83.47,45.99],[-83.59,45.82],[-82.55,45.35],[-82.34,44.44],[-82.14,43.57],[-82.43,42.98],[-82.9,42.43],[-83.12,42.08],[-83.14,41.98],[-83.03,41.83],[-82.69,41.67],[-82.44,41.67],[-81.28,42.21],[-80.25,42.37],[-78.94,42.86],[-78.92,42.96],[-79.01,43.27],[-79.17,43.47],[-78.72,43.62],[-77.74,43.63],[-76.82,43.63],[-76.5,44.02],[-76.38,44.1],[-75.32,44.82],[-74.87,45],[-73.35,45.01],[-71.51,45.01],[-71.4,45.25],[-71.08,45.31],[-70.66,45.46],[-70.3,45.91],[-70,46.69],[-69.24,47.45],[-68.91,47.19],[-68.23,47.35],[-67.79,47.07],[-67.79,45.7],[-67.14,45.14],[-66.97,44.81],[-68.03,44.33],[-69.06,43.98],[-70.12,43.68],[-70.65,43.09],[-70.81,42.86],[-70.83,42.33],[-70.49,41.81],[-70.08,41.78],[-70.18,42.15],[-69.89,41.92],[-69.96,41.64],[-70.64,41.48],[-71.12,41.49],[-71.86,41.32],[-72.29,41.27],[-72.88,41.22],[-73.71,40.93],[-72.24,41.12],[-71.94,40.93],[-73.35,40.63],[-73.98,40.63],[-73.95,40.75],[-74.26,40.47],[-73.96,40.43],[-74.18,39.71],[-74.91,38.94],[-74.98,39.2],[-75.2,39.25],[-75.53,39.5],[-75.32,38.96],[-75.07,38.78],[-75.06,38.4],[-75.38,38.02],[-75.94,37.22],[-76.03,37.26],[-75.72,37.94],[-76.23,38.32],[-76.35,39.15],[-76.54,38.72],[-76.33,38.08],[-76.99,38.24],[-76.3,37.92],[-76.26,36.97],[-75.97,36.9],[-75.87,36.55],[-75.73,35.55],[-76.36,34.81],[-77.4,34.51],[-78.05,33.93],[-78.55,33.86],[-79.06,33.49],[-79.2,33.16],[-80.3,32.51],[-80.87,32.03],[-81.34,31.44],[-81.49,30.73],[-81.31,30.04],[-80.98,29.18],[-80.53,28.47],[-80.53,28.04],[-80.06,26.88],[-80.09,26.21],[-80.13,25.82],[-80.38,25.21],[-80.68,25.08],[-81.17,25.2],[-81.33,25.64],[-81.71,25.87],[-82.24,26.73],[-82.71,27.49],[-82.86,27.89],[-82.65,28.55],[-82.93,29.1],[-83.71,29.94],[-84.1,30.09],[-85.11,29.64],[-85.29,29.69],[-85.77,30.15],[-86.4,30.4],[-87.53,30.27],[-88.42,30.39],[-89.18,30.32],[-89.59,30.16],[-89.41,29.89],[-89.43,29.49],[-89.22,29.29],[-89.41,29.16],[-89.78,29.31],[-90.15,29.12],[-90.88,29.15],[-91.63,29.68],[-92.5,29.55],[-93.22,29.78],[-93.85,29.71],[-94.69,29.48],[-95.6,28.74],[-96.59,28.31],[-97.14,27.83],[-97.37,27.38],[-97.38,26.69],[-97.33,26.21],[-97.14,25.87],[-97.53,25.84],[-98.24,26.06],[-99.02,26.37],[-99.3,26.84],[-99.52,27.54],[-100.11,28.11],[-100.46,28.7],[-100.96,29.38],[-101.66,29.78],[-102.48,29.76],[-103.11,28.97],[-103.94,29.27],[-104.46,29.57],[-104.71,30.12],[-105.04,30.64],[-105.63,31.08],[-106.14,31.4],[-106.51,31.75],[-108.24,31.75],[-108.24,31.34],[-109.04,31.34],[-111.02,31.33],[-113.31,32.04],[-114.81,32.52],[-114.72,32.72],[-115.99,32.61],[-117.13,32.53],[-117.29,33.05],[-117.94,33.62],[-118.41,33.74],[-118.52,34.03],[-119.08,34.08],[-119.44,34.35],[-120.37,34.45],[-120.62,34.61],[-120.74,35.16],[-121.72,36.16],[-122.55,37.55],[-122.51,37.78],[-122.95,38.11],[-123.73,38.95],[-123.86,39.77],[-124.4,40.31],[-124.18,41.14],[-124.21,42],[-124.53,42.77],[-124.14,43.71],[-124.02,44.62],[-123.9,45.52],[-124.08,46.86],[-124.4,47.72],[-124.69,48.18],[-124.57,48.38],[-123.12,48.04],[-122.59,47.1],[-122.34,47.36],[-122.5,48.18],[-122.84,49]],[[-155.4,20.08],[-155.22,19.99],[-155.06,19.86],[-154.81,19.51],[-154.83,19.45],[-155.22,19.24],[-155.54,19.08],[-155.69,18.92],[-155.94,19.06],[-155.91,19.34],[-156.07,19.7],[-156.02,19.81],[-155.85,19.98],[-155.92,20.17],[-155.86,20.27],[-155.79,20.25],[-155.4,20.08]],[[-155.99,20.76],[-156.08,20.64],[-156.42,20.57],[-156.59,20.78],[-156.7,20.86],[-156.71,20.93],[-156.61,21.01],[-156.26,20.92],[-155.99,20.76]],[[-156.76,21.18],[-156.79,21.07],[-157.33,21.1],[-157.25,21.22],[-156.76,21.18]],[[-158.03,21.72],[-157.94,21.65],[-157.65,21.32],[-157.71,21.26],[-157.78,21.28],[-158.13,21.31],[-158.25,21.54],[-158.29,21.58],[-158.03,21.72]],[[-159.36,22.22],[-159.35,21.98],[-159.47,21.88],[-159.8,22.06],[-159.75,22.14],[-159.59,22.24],[-159.36,22.22]],[[-166.47,60.38],[-165.68,60.29],[-165.58,59.91],[-166.19,59.75],[-166.85,59.94],[-167.45,60.21],[-166.47,60.38]],[[-153.23,57.97],[-152.56,57.9],[-152.14,57.59],[-153.01,57.12],[-154,56.74],[-154.52,56.99],[-154.67,57.46],[-153.76,57.82],[-153.23,57.97]],[[-140.99,69.71],[-140.99,66],[-141,60.31],[-140.01,60.28],[-139.04,60],[-138.34,59.56],[-137.45,58.91],[-136.48,59.46],[-135.47,59.79],[-134.95,59.27],[-134.27,58.86],[-133.35,58.41],[-132.73,57.69],[-131.71,56.55],[-130.01,55.92],[-129.98,55.28],[-130.54,54.8],[-131.09,55.18],[-131.97,55.5],[-132.25,56.37],[-133.54,57.18],[-134.08,58.12],[-135.04,58.19],[-136.63,58.21],[-137.8,58.5],[-139.87,59.54],[-140.82,59.73],[-142.57,60.08],[-143.96,60],[-145.93,60.46],[-147.11,60.89],[-148.23,60.67],[-148.02,59.98],[-148.57,59.91],[-149.73,59.71],[-150.61,59.37],[-151.72,59.16],[-151.86,59.74],[-151.41,60.73],[-150.35,61.03],[-150.62,61.28],[-151.89,60.73],[-152.58,60.06],[-154.02,59.35],[-153.29,58.86],[-154.23,58.15],[-155.31,57.73],[-156.31,57.42],[-156.56,56.98],[-158.12,56.46],[-158.43,55.99],[-159.6,55.57],[-160.29,55.64],[-161.22,55.36],[-162.24,55.02],[-163.07,54.69],[-164.79,54.4],[-164.94,54.57],[-163.85,55.04],[-162.87,55.35],[-161.81,55.9],[-160.56,56.01],[-160.07,56.42],[-158.68,57.02],[-158.46,57.22],[-157.72,57.57],[-157.55,58.33],[-157.04,58.92],[-158.19,58.62],[-158.52,58.79],[-159.06,58.42],[-159.71,58.93],[-159.98,58.57],[-160.35,59.07],[-161.36,58.67],[-161.97,58.67],[-162.05,59.27],[-161.87,59.63],[-162.52,59.99],[-163.82,59.8],[-164.66,60.27],[-165.35,60.51],[-165.35,61.07],[-166.12,61.5],[-165.73,62.08],[-164.92,62.63],[-164.56,63.15],[-163.75,63.22],[-163.07,63.06],[-162.26,63.54],[-161.54,63.46],[-160.77,63.77],[-160.96,64.22],[-161.52,64.4],[-160.78,64.79],[-161.39,64.78],[-162.45,64.56],[-162.76,64.34],[-163.55,64.56],[-164.96,64.45],[-166.42,64.69],[-166.85,65.09],[-168.11,65.67],[-166.71,66.09],[-164.47,66.58],[-163.65,66.58],[-163.79,66.08],[-161.68,66.12],[-162.49,66.73],[-163.72,67.12],[-164.43,67.62],[-165.39,68.04],[-166.76,68.36],[-166.2,68.88],[-164.43,68.91],[-163.17,69.37],[-162.93,69.86],[-161.91,70.33],[-160.93,70.45],[-159.04,70.89],[-158.12,70.82],[-156.58,71.36],[-155.07,71.15],[-154.34,70.7],[-153.9,70.89],[-152.21,70.83],[-152.27,70.6],[-150.74,70.43],[-149.72,70.53],[-147.61,70.21],[-145.69,70.12],[-144.92,69.99],[-143.59,70.15],[-142.07,69.85],[-140.99,69.71]],[[-171.73,63.78],[-171.12,63.59],[-170.49,63.69],[-169.68,63.43],[-168.69,63.3],[-168.77,63.19],[-169.53,62.98],[-170.29,63.19],[-170.67,63.38],[-171.55,63.32],[-171.79,63.41],[-171.73,63.78]],[[87.36,49.22],[86.6,48.55],[85.77,48.46],[85.72,47.45],[85.16,47],[83.18,47.33],[82.46,45.54],[81.95,45.32],[79.97,44.92],[80.87,43.18],[80.18,42.92],[80.26,42.35],[79.65,42.5],[79.14,42.86],[77.66,42.96],[76,42.99],[75.64,42.88],[74.21,43.3],[73.64,43.09],[73.49,42.5],[71.84,42.85],[71.19,42.7],[70.96,42.27],[70.39,42.08],[69.07,41.38],[68.63,40.67],[68.26,40.66],[67.98,41.14],[66.71,41.17],[66.51,41.99],[66.02,41.99],[66.1,43],[64.9,43.73],[63.19,43.65],[62.01,43.5],[61.06,44.41],[60.24,44.78],[58.69,45.5],[58.5,45.59],[55.93,45],[55.97,41.31],[55.46,41.26],[54.75,42.04],[54.08,42.32],[52.94,42.12],[52.5,41.78],[52.45,42.03],[52.69,42.44],[52.5,42.79],[51.34,43.13],[50.89,44.03],[50.34,44.28],[50.31,44.61],[51.28,44.51],[51.32,45.25],[52.17,45.41],[53.04,45.26],[53.22,46.23],[53.04,46.85],[52.04,46.8],[51.19,47.05],[50.04,46.61],[49.1,46.4],[48.59,46.56],[48.7,47.08],[48.06,47.74],[47.31,47.72],[46.47,48.39],[47.04,49.15],[46.75,49.36],[47.55,50.45],[48.58,49.88],[48.7,50.6],[50.77,51.69],[52.33,51.72],[54.53,51.03],[55.72,50.62],[56.78,51.04],[58.36,51.06],[59.64,50.55],[59.93,50.84],[61.34,50.8],[61.59,51.27],[59.97,51.96],[60.93,52.45],[60.74,52.72],[61.7,52.98],[60.98,53.66],[61.44,54.01],[65.18,54.35],[65.67,54.6],[68.17,54.97],[69.07,55.38],[70.86,55.17],[71.18,54.13],[72.23,54.38],[73.51,54.04],[73.42,53.49],[74.39,53.55],[76.89,54.49],[76.52,54.18],[77.8,53.4],[80.03,50.87],[80.57,51.39],[81.95,50.81],[83.38,51.07],[83.94,50.89],[84.42,50.31],[85.11,50.12],[85.54,49.69],[86.83,49.83],[87.36,49.22]],[[55.97,41.31],[55.93,45],[58.5,45.59],[58.69,45.5],[60.24,44.78],[61.06,44.41],[62.01,43.5],[63.19,43.65],[64.9,43.73],[66.1,43],[66.02,41.99],[66.51,41.99],[66.71,41.17],[67.98,41.14],[68.26,40.66],[68.63,40.67],[69.07,41.38],[70.39,42.08],[70.96,42.27],[71.26,42.17],[70.42,41.52],[71.16,41.14],[71.87,41.39],[73.05,40.87],[71.78,40.15],[71.01,40.24],[70.6,40.22],[70.46,40.5],[70.67,40.96],[69.33,40.73],[69.01,40.09],[68.54,39.53],[67.7,39.58],[67.44,39.14],[68.18,38.9],[68.39,38.16],[67.83,37.15],[67.07,37.36],[66.52,37.36],[66.54,37.97],[65.22,38.4],[64.17,38.89],[63.52,39.36],[62.38,40.05],[61.88,41.08],[61.55,41.27],[60.46,41.22],[60.08,41.43],[59.97,42.22],[58.63,42.75],[57.79,42.17],[56.93,41.83],[57.09,41.32],[55.97,41.31]],[[141,-2.6],[142.74,-3.29],[144.58,-3.86],[145.27,-4.37],[145.83,-4.88],[145.98,-5.47],[147.65,-6.08],[147.89,-6.61],[146.97,-6.72],[147.19,-7.39],[148.09,-8.04],[148.73,-9.11],[149.31,-9.07],[149.27,-9.51],[150.04,-9.68],[149.74,-9.87],[150.8,-10.29],[150.69,-10.58],[150.03,-10.65],[149.78,-10.39],[148.92,-10.28],[147.91,-10.13],[147.14,-9.49],[146.57,-8.94],[146.05,-8.07],[144.74,-7.63],[143.9,-7.92],[143.29,-8.25],[143.41,-8.98],[142.63,-9.33],[142.07,-9.16],[141.03,-9.12],[141.02,-5.86],[141,-2.6]],[[152.64,-3.66],[153.02,-3.98],[153.14,-4.5],[152.83,-4.77],[152.64,-4.18],[152.41,-3.79],[151.95,-3.46],[151.38,-3.04],[150.66,-2.74],[150.94,-2.5],[151.48,-2.78],[151.82,-3],[152.24,-3.24],[152.64,-3.66]],[[151.3,-5.84],[150.75,-6.08],[150.24,-6.32],[149.71,-6.32],[148.89,-6.03],[148.32,-5.75],[148.4,-5.44],[149.3,-5.58],[149.85,-5.51],[150,-5.03],[150.14,-5],[150.24,-5.53],[150.81,-5.46],[151.09,-5.11],[151.65,-4.76],[151.54,-4.17],[152.14,-4.15],[152.34,-4.31],[152.32,-4.87],[151.98,-5.48],[151.46,-5.56],[151.3,-5.84]],[[154.76,-5.34],[155.06,-5.57],[155.55,-6.2],[156.02,-6.54],[155.88,-6.82],[155.6,-6.92],[155.17,-6.54],[154.73,-5.9],[154.52,-5.14],[154.65,-5.04],[154.76,-5.34]],[[141,-2.6],[141.02,-5.86],[141.03,-9.12],[140.14,-8.3],[139.13,-8.1],[138.88,-8.38],[137.61,-8.41],[138.04,-7.6],[138.67,-7.32],[138.41,-6.23],[137.93,-5.39],[135.99,-4.55],[135.17,-4.46],[133.66,-3.54],[133.37,-4.02],[132.98,-4.11],[132.76,-3.75],[132.75,-3.31],[131.99,-2.82],[133.07,-2.46],[133.78,-2.48],[133.7,-2.21],[132.23,-2.21],[131.84,-1.62],[130.94,-1.43],[130.52,-.94],[131.87,-.7],[132.38,-.37],[133.98,-.78],[134.14,-1.15],[134.42,-2.77],[135.46,-3.37],[136.29,-2.31],[137.44,-1.7],[138.33,-1.7],[139.19,-2.05],[139.93,-2.41],[141,-2.6]],[[124.97,-8.89],[125.07,-9.09],[125.09,-9.39],[124.44,-10.14],[123.58,-10.36],[123.46,-10.24],[123.55,-9.9],[123.98,-9.29],[124.97,-8.89]],[[134.21,-6.89],[134.11,-6.14],[134.29,-5.78],[134.5,-5.44],[134.73,-5.74],[134.73,-6.21],[134.21,-6.89]],[[117.88,4.14],[117.31,3.24],[118.05,2.29],[117.87,1.83],[119,.9],[117.81,.78],[117.48,.1],[117.52,-.8],[116.56,-1.49],[116.53,-2.48],[116.15,-4.01],[116,-3.66],[114.86,-4.11],[114.47,-3.5],[113.76,-3.44],[113.26,-3.12],[112.07,-3.48],[111.7,-3],[111.05,-3.05],[110.22,-2.93],[110.07,-1.59],[109.57,-1.31],[109.09,-.46],[108.95,.42],[109.07,1.34],[109.66,2.01],[109.83,1.34],[110.52,.77],[111.16,.98],[111.8,.9],[112.38,1.41],[112.86,1.5],[113.81,1.22],[114.62,1.43],[115.13,2.82],[115.52,3.17],[115.87,4.31],[117.01,4.31],[117.88,4.14]],[[129.37,-2.8],[130.47,-3.09],[130.83,-3.86],[129.99,-3.45],[129.16,-3.36],[128.59,-3.43],[127.9,-3.39],[128.13,-2.84],[129.37,-2.8]],[[126.87,-3.79],[126.18,-3.61],[125.99,-3.18],[127,-3.13],[127.25,-3.46],[126.87,-3.79]],[[127.93,2.17],[128,1.63],[128.6,1.54],[128.69,1.13],[128.63,.26],[128.12,.36],[127.97,-.25],[128.38,-.78],[128.1,-.9],[127.7,-.27],[127.4,1.01],[127.6,1.81],[127.93,2.17]],[[122.93,.88],[124.08,.92],[125.07,1.64],[125.24,1.42],[124.44,.43],[123.68,.24],[122.72,.43],[121.06,.38],[120.18,.24],[120.04,-.52],[120.93,-1.41],[121.47,-.96],[123.34,-.62],[123.26,-1.08],[122.82,-.93],[122.39,-1.52],[121.51,-1.91],[122.45,-3.19],[122.27,-3.53],[123.17,-4.68],[123.16,-5.34],[122.63,-5.63],[122.24,-5.28],[122.72,-4.46],[121.74,-4.85],[121.49,-4.57],[121.62,-4.19],[120.9,-3.6],[120.97,-2.63],[120.3,-2.93],[120.39,-4.1],[120.43,-5.53],[119.8,-5.67],[119.37,-5.38],[119.65,-4.46],[119.5,-3.49],[119.08,-3.49],[118.77,-2.8],[119.18,-2.15],[119.32,-1.35],[119.83,.15],[120.03,.57],[120.89,1.31],[121.67,1.01],[122.93,.88]],[[120.29,-10.26],[118.97,-9.56],[119.9,-9.36],[120.43,-9.67],[120.78,-9.97],[120.71,-10.24],[120.29,-10.26]],[[121.34,-8.54],[122.01,-8.46],[122.9,-8.09],[122.76,-8.65],[121.25,-8.93],[119.92,-8.81],[119.92,-8.45],[120.71,-8.24],[121.34,-8.54]],[[118.26,-8.36],[118.88,-8.28],[119.13,-8.71],[117.97,-8.91],[117.28,-9.04],[116.74,-9.03],[117.08,-8.46],[117.63,-8.45],[117.9,-8.09],[118.26,-8.36]],[[108.49,-6.42],[108.62,-6.78],[110.54,-6.88],[110.76,-6.46],[112.61,-6.95],[112.98,-7.59],[114.48,-7.78],[115.71,-8.37],[114.57,-8.75],[113.46,-8.35],[112.56,-8.38],[111.52,-8.3],[110.59,-8.12],[109.43,-7.74],[108.69,-7.64],[108.28,-7.77],[106.45,-7.36],[106.28,-6.93],[105.36,-6.85],[106.05,-5.9],[107.26,-5.96],[108.07,-6.35],[108.49,-6.42]],[[104.37,-1.08],[104.54,-1.78],[104.89,-2.34],[105.62,-2.43],[106.11,-3.06],[105.86,-4.31],[105.82,-5.85],[104.71,-5.87],[103.87,-5.04],[102.58,-4.22],[102.16,-3.61],[101.4,-2.8],[100.9,-2.05],[100.14,-.65],[99.26,.18],[98.97,1.04],[98.6,1.82],[97.7,2.45],[97.18,3.31],[96.43,3.87],[95.38,4.97],[95.29,5.48],[95.94,5.44],[97.48,5.25],[98.37,4.27],[99.14,3.59],[99.69,3.17],[100.64,2.1],[101.66,2.08],[102.5,1.4],[103.08,.56],[103.84,.1],[103.44,-.71],[104.01,-1.06],[104.37,-1.08]],[[-68.63,-52.64],[-68.25,-53.1],[-67.75,-53.85],[-66.45,-54.45],[-65.05,-54.7],[-65.5,-55.2],[-66.45,-55.25],[-66.96,-54.9],[-67.56,-54.87],[-68.63,-54.87],[-68.63,-52.64]],[[-57.62,-30.22],[-57.88,-31.02],[-58.14,-32.04],[-58.13,-33.04],[-58.35,-33.26],[-58.43,-33.91],[-58.5,-34.43],[-57.22,-35.29],[-57.36,-35.98],[-56.74,-36.41],[-56.79,-36.9],[-57.75,-38.18],[-59.23,-38.72],[-61.24,-38.93],[-62.34,-38.83],[-62.12,-39.42],[-62.33,-40.17],[-62.15,-40.68],[-62.75,-41.03],[-63.77,-41.17],[-64.73,-40.8],[-65.12,-41.06],[-64.98,-42.06],[-64.3,-42.36],[-63.75,-42.04],[-63.46,-42.56],[-64.38,-42.87],[-65.18,-43.49],[-65.33,-44.5],[-65.57,-45.04],[-66.51,-45.04],[-67.29,-45.55],[-67.58,-46.3],[-66.6,-47.03],[-65.64,-47.24],[-65.99,-48.13],[-67.17,-48.7],[-67.82,-49.87],[-68.73,-50.27],[-69.14,-50.73],[-68.82,-51.77],[-68.15,-52.35],[-68.57,-52.3],[-69.5,-52.14],[-71.92,-52.01],[-72.33,-51.43],[-72.31,-50.68],[-72.97,-50.74],[-73.33,-50.38],[-73.41,-49.32],[-72.65,-48.88],[-72.33,-48.24],[-72.45,-47.74],[-71.92,-46.88],[-71.55,-45.56],[-71.66,-44.97],[-71.22,-44.78],[-71.33,-44.41],[-71.79,-44.21],[-71.46,-43.79],[-71.92,-43.41],[-72.15,-42.25],[-71.75,-42.05],[-71.92,-40.83],[-71.68,-39.81],[-71.41,-38.92],[-70.81,-38.55],[-71.12,-37.58],[-71.12,-36.66],[-70.36,-36.01],[-70.39,-35.17],[-69.82,-34.19],[-69.81,-33.27],[-70.07,-33.09],[-70.53,-31.36],[-69.92,-30.34],[-70.02,-29.37],[-69.66,-28.46],[-69,-27.52],[-68.29,-26.9],[-68.59,-26.51],[-68.38,-26.18],[-68.42,-24.52],[-67.33,-24.03],[-66.98,-22.99],[-67.11,-22.74],[-66.27,-21.83],[-64.96,-22.08],[-64.38,-22.8],[-63.99,-21.99],[-62.85,-22.03],[-62.69,-22.25],[-60.85,-23.88],[-60.03,-24.03],[-58.81,-24.77],[-57.78,-25.16],[-57.63,-25.6],[-58.62,-27.12],[-57.61,-27.4],[-56.49,-27.55],[-55.69,-27.39],[-54.79,-26.62],[-54.63,-25.74],[-54.13,-25.55],[-53.63,-26.12],[-53.65,-26.92],[-54.49,-27.47],[-55.16,-27.88],[-56.29,-28.85],[-57.62,-30.22]],[[-68.63,-52.64],[-68.63,-54.87],[-67.56,-54.87],[-66.96,-54.9],[-67.29,-55.3],[-68.15,-55.61],[-68.64,-55.58],[-69.23,-55.5],[-69.96,-55.2],[-71.01,-55.05],[-72.27,-54.49],[-73.28,-53.96],[-74.66,-52.84],[-73.84,-53.05],[-72.43,-53.72],[-71.11,-54.07],[-70.59,-53.62],[-70.27,-52.93],[-69.35,-52.52],[-68.63,-52.64]],[[-69.59,-17.58],[-69.1,-18.26],[-68.97,-18.98],[-68.44,-19.4],[-68.76,-20.37],[-68.22,-21.49],[-67.83,-22.87],[-67.11,-22.74],[-66.98,-22.99],[-67.33,-24.03],[-68.42,-24.52],[-68.38,-26.18],[-68.59,-26.51],[-68.29,-26.9],[-69,-27.52],[-69.66,-28.46],[-70.02,-29.37],[-69.92,-30.34],[-70.53,-31.36],[-70.07,-33.09],[-69.81,-33.27],[-69.82,-34.19],[-70.39,-35.17],[-70.36,-36.01],[-71.12,-36.66],[-71.12,-37.58],[-70.81,-38.55],[-71.41,-38.92],[-71.68,-39.81],[-71.92,-40.83],[-71.75,-42.05],[-72.15,-42.25],[-71.92,-43.41],[-71.46,-43.79],[-71.79,-44.21],[-71.33,-44.41],[-71.22,-44.78],[-71.66,-44.97],[-71.55,-45.56],[-71.92,-46.88],[-72.45,-47.74],[-72.33,-48.24],[-72.65,-48.88],[-73.41,-49.32],[-73.33,-50.38],[-72.97,-50.74],[-72.31,-50.68],[-72.33,-51.43],[-71.92,-52.01],[-69.5,-52.14],[-68.57,-52.3],[-69.46,-52.29],[-69.94,-52.54],[-70.84,-52.9],[-71.01,-53.83],[-71.43,-53.86],[-72.56,-53.53],[-73.7,-52.83],[-74.95,-52.26],[-75.26,-51.63],[-74.98,-51.04],[-75.48,-50.38],[-75.61,-48.67],[-75.18,-47.71],[-74.13,-46.94],[-75.65,-46.65],[-74.69,-45.76],[-74.35,-44.1],[-73.24,-44.45],[-72.72,-42.38],[-73.39,-42.12],[-73.7,-43.37],[-74.33,-43.23],[-74.02,-41.8],[-73.68,-39.94],[-73.22,-39.26],[-73.51,-38.28],[-73.59,-37.16],[-73.17,-37.12],[-72.55,-35.51],[-71.86,-33.91],[-71.44,-32.42],[-71.67,-30.92],[-71.37,-30.1],[-71.49,-28.86],[-70.9,-27.64],[-70.72,-25.71],[-70.4,-23.63],[-70.09,-21.39],[-70.16,-19.76],[-70.37,-18.35],[-69.86,-18.09],[-69.59,-17.58]],[[29.34,-4.5],[29.52,-5.42],[29.42,-5.94],[29.62,-6.52],[30.2,-7.08],[30.74,-8.34],[30.35,-8.24],[29,-8.41],[28.73,-8.53],[28.45,-9.16],[28.67,-9.61],[28.5,-10.79],[28.37,-11.79],[28.64,-11.97],[29.34,-12.36],[29.62,-12.18],[29.7,-13.26],[28.94,-13.25],[28.52,-12.7],[28.15,-12.27],[27.39,-12.13],[27.16,-11.61],[26.55,-11.93],[25.75,-11.78],[25.42,-11.33],[24.78,-11.24],[24.31,-11.26],[24.26,-10.95],[23.91,-10.93],[23.46,-10.87],[22.84,-11.02],[22.4,-10.99],[22.16,-11.08],[22.21,-9.89],[21.88,-9.52],[21.8,-8.91],[21.95,-8.31],[21.75,-7.92],[21.73,-7.29],[20.51,-7.3],[20.6,-6.94],[20.09,-6.94],[20.04,-7.12],[19.42,-7.16],[19.17,-7.74],[19.02,-7.99],[18.46,-7.85],[18.14,-7.99],[17.47,-8.07],[17.09,-7.54],[16.86,-7.22],[16.57,-6.62],[16.33,-5.88],[13.38,-5.86],[13.02,-5.98],[12.74,-5.97],[12.32,-6.1],[12.18,-5.79],[12.44,-5.68],[12.47,-5.25],[12.63,-4.99],[12.99,-4.78],[13.26,-4.88],[13.6,-4.5],[14.15,-4.51],[14.21,-4.79],[14.58,-4.97],[15.17,-4.34],[15.75,-3.86],[16.01,-3.54],[15.97,-2.71],[16.41,-1.74],[16.86,-1.23],[17.52,-.74],[17.64,-.42],[17.66,-.06],[17.83,.29],[17.78,.86],[17.9,1.74],[18.1,2.37],[18.39,2.9],[18.45,3.5],[18.54,4.2],[18.93,4.71],[19.47,5.03],[20.29,4.69],[20.93,4.32],[21.66,4.22],[22.4,4.03],[22.7,4.63],[22.84,4.71],[23.3,4.61],[24.41,5.11],[24.81,4.9],[25.13,4.93],[25.28,5.17],[25.65,5.26],[26.4,5.15],[27.05,5.13],[27.37,5.23],[27.98,4.41],[28.43,4.29],[28.7,4.46],[29.16,4.39],[29.72,4.6],[29.95,4.17],[30.83,3.51],[30.77,2.34],[31.17,2.2],[30.85,1.85],[30.47,1.58],[30.09,1.06],[29.87,.6],[29.82,-.21],[29.59,-.59],[29.58,-1.34],[29.29,-1.62],[29.26,-2.21],[29.12,-2.29],[29.03,-2.84],[29.28,-3.29],[29.34,-4.5]],[[41.59,-1.68],[40.99,-.86],[40.98,2.78],[41.86,3.92],[42.13,4.23],[42.77,4.25],[43.66,4.96],[44.96,5],[47.79,8],[48.49,8.84],[48.94,9.45],[48.94,9.97],[48.94,10.98],[48.94,11.39],[48.95,11.41],[49.27,11.43],[49.73,11.58],[50.26,11.68],[50.73,12.02],[51.11,12.02],[51.13,11.75],[51.04,11.17],[51.05,10.64],[50.83,10.28],[50.55,9.2],[50.07,8.08],[49.45,6.8],[48.6,5.34],[47.74,4.22],[46.56,2.86],[45.56,2.05],[44.07,1.05],[43.14,.29],[42.04,-.92],[41.81,-1.45],[41.59,-1.68]],[[39.2,-4.68],[37.77,-3.68],[37.7,-3.1],[34.07,-1.06],[33.9,-.95],[33.89,.11],[34.18,.52],[34.67,1.18],[35.04,1.91],[34.59,3.05],[34.48,3.55],[34,4.25],[34.62,4.85],[35.3,5.51],[35.82,5.34],[35.82,4.78],[36.16,4.45],[36.86,4.45],[38.12,3.6],[38.44,3.59],[38.67,3.62],[38.89,3.5],[39.56,3.42],[39.85,3.84],[40.77,4.26],[41.17,3.92],[41.86,3.92],[40.98,2.78],[40.99,-.86],[41.59,-1.68],[40.88,-2.08],[40.64,-2.5],[40.26,-2.57],[40.12,-3.28],[39.8,-3.68],[39.61,-4.35],[39.2,-4.68]],[[24.57,8.23],[23.81,8.67],[23.46,8.95],[23.39,9.27],[23.56,9.68],[23.55,10.09],[22.98,10.71],[22.87,11.14],[22.88,11.38],[22.51,11.68],[22.5,12.26],[22.29,12.65],[21.94,12.59],[22.04,12.96],[22.3,13.37],[22.18,13.79],[22.51,14.09],[22.3,14.33],[22.57,14.94],[23.02,15.68],[23.89,15.61],[23.84,19.58],[23.85,20],[25,20],[25,22],[29.02,22],[32.9,22],[36.87,22],[37.19,21.02],[36.97,20.84],[37.11,19.81],[37.48,18.61],[37.86,18.37],[38.41,18],[37.9,17.43],[37.17,17.26],[36.85,16.96],[36.75,16.29],[36.32,14.82],[36.43,14.42],[36.27,13.56],[35.87,12.58],[35.26,12.08],[34.83,11.32],[34.73,10.91],[34.26,10.63],[33.96,9.58],[33.98,8.69],[33.96,9.46],[33.82,9.48],[33.84,9.98],[33.72,10.33],[33.21,10.72],[33.09,11.44],[33.21,12.18],[32.74,12.25],[32.68,12.02],[32.07,11.97],[32.32,11.68],[32.4,11.08],[31.85,10.53],[31.35,9.81],[30.84,9.71],[30,10.29],[29.62,10.08],[29.51,9.79],[29,9.6],[28.97,9.4],[27.97,9.4],[27.83,9.6],[27.11,9.64],[26.75,9.47],[26.48,9.55],[25.96,10.14],[25.79,10.41],[25.07,10.27],[24.8,9.81],[24.54,8.92],[24.19,8.73],[23.89,8.62],[24.57,8.23]],[[23.84,19.58],[23.89,15.61],[23.02,15.68],[22.57,14.94],[22.3,14.33],[22.51,14.09],[22.18,13.79],[22.3,13.37],[22.04,12.96],[21.94,12.59],[22.29,12.65],[22.5,12.26],[22.51,11.68],[22.88,11.38],[22.87,11.14],[22.23,10.97],[21.72,10.57],[21,9.48],[20.06,9.01],[19.09,9.07],[18.81,8.98],[18.91,8.63],[18.39,8.28],[17.97,7.89],[16.71,7.51],[16.46,7.74],[16.29,7.75],[16.1,7.5],[15.28,7.42],[15.44,7.69],[15.12,8.38],[14.98,8.8],[14.55,8.97],[13.96,9.55],[14.17,10.02],[14.63,9.92],[14.91,9.99],[15.47,9.98],[14.92,10.89],[14.96,11.56],[14.9,12.22],[14.5,12.86],[14.6,13.33],[13.96,13.35],[13.96,14],[13.54,14.37],[13.97,15.68],[15.25,16.63],[15.3,17.93],[15.69,19.96],[15.9,20.39],[15.49,20.73],[15.47,21.05],[15.1,21.31],[14.85,22.86],[15.86,23.41],[19.85,21.49],[23.84,19.58]],[[-71.71,19.71],[-71.62,19.17],[-71.7,18.78],[-71.94,18.62],[-71.69,18.32],[-71.71,18.04],[-72.37,18.21],[-72.84,18.14],[-73.45,18.22],[-73.92,18.03],[-74.46,18.34],[-74.37,18.66],[-73.45,18.53],[-72.69,18.45],[-72.33,18.67],[-72.79,19.1],[-72.78,19.48],[-73.41,19.64],[-73.19,19.92],[-72.58,19.87],[-71.71,19.71]],[[-71.71,18.04],[-71.69,18.32],[-71.94,18.62],[-71.7,18.78],[-71.62,19.17],[-71.71,19.71],[-71.59,19.88],[-70.81,19.88],[-70.21,19.62],[-69.95,19.65],[-69.77,19.29],[-69.22,19.31],[-69.26,19.01],[-68.81,18.98],[-68.32,18.61],[-68.69,18.21],[-69.17,18.42],[-69.62,18.38],[-69.95,18.43],[-70.13,18.25],[-70.52,18.18],[-70.67,18.43],[-71,18.28],[-71.4,17.6],[-71.66,17.76],[-71.71,18.04]],[[93.78,81.03],[95.94,81.25],[97.88,80.75],[100.19,79.78],[99.94,78.88],[97.76,78.76],[94.97,79.04],[93.31,79.43],[92.54,80.14],[91.18,80.34],[93.78,81.03]],[[102.84,79.28],[105.37,78.71],[105.08,78.31],[99.44,77.92],[101.26,79.23],[102.09,79.35],[102.84,79.28]],[[138.83,76.14],[141.47,76.09],[145.09,75.56],[144.3,74.82],[140.62,74.85],[138.96,74.61],[136.98,75.26],[137.51,75.95],[138.83,76.14]],[[148.22,75.35],[150.73,75.08],[149.58,74.69],[147.98,74.78],[146.12,75.17],[146.36,75.5],[148.22,75.35]],[[139.86,73.37],[140.81,73.77],[142.06,73.86],[143.48,73.47],[143.6,73.21],[142.09,73.21],[140.04,73.32],[139.86,73.37]],[[44.85,80.59],[46.8,80.77],[48.32,80.78],[48.52,80.51],[49.1,80.75],[50.04,80.92],[51.52,80.7],[51.14,80.55],[49.79,80.42],[48.89,80.34],[48.75,80.18],[47.59,80.01],[46.5,80.25],[47.07,80.56],[44.85,80.59]],[[22.73,54.33],[20.89,54.31],[19.66,54.43],[19.89,54.87],[21.27,55.19],[22.31,55.02],[22.76,54.86],[22.65,54.58],[22.73,54.33]],[[53.51,73.75],[55.9,74.63],[55.63,75.08],[57.87,75.61],[61.17,76.25],[64.5,76.44],[66.21,76.81],[68.16,76.94],[68.85,76.54],[68.18,76.23],[64.64,75.74],[61.58,75.26],[58.48,74.31],[56.99,73.33],[55.42,72.37],[55.62,71.54],[57.53,70.72],[56.94,70.63],[53.68,70.76],[53.41,71.21],[51.6,71.47],[51.46,72.02],[52.48,72.23],[52.44,72.78],[54.43,73.63],[53.51,73.75]],[[142.92,53.7],[143.26,52.74],[143.24,51.76],[143.65,50.75],[144.65,48.98],[143.18,49.31],[142.56,47.86],[143.54,46.84],[143.51,46.14],[142.75,46.74],[142.09,45.97],[141.91,46.81],[142.02,47.78],[141.9,48.86],[142.13,49.61],[142.18,50.95],[141.59,51.94],[141.68,53.3],[142.61,53.76],[142.21,54.23],[142.65,54.37],[142.92,53.7]],[[130.78,42.22],[130.64,42.4],[130.63,42.9],[131.14,42.93],[131.29,44.11],[131.03,44.97],[131.88,45.32],[133.1,45.14],[133.77,46.12],[134.11,47.21],[134.5,47.58],[135.02,48.48],[133.37,48.18],[132.51,47.79],[130.99,47.79],[130.58,48.73],[129.4,49.44],[127.66,49.76],[127.29,50.74],[126.94,51.35],[126.56,51.78],[125.95,52.79],[125.07,53.16],[123.57,53.46],[122.24,53.43],[121,53.25],[120.18,52.75],[120.73,52.52],[120.74,51.96],[120.18,51.64],[119.28,50.58],[119.29,50.14],[117.88,49.51],[116.68,49.89],[115.49,49.81],[114.96,50.14],[114.36,50.25],[112.9,49.54],[111.58,49.38],[110.66,49.13],[109.4,49.29],[108.47,49.28],[107.87,49.79],[106.89,50.27],[105.89,50.41],[104.62,50.27],[103.68,50.09],[102.26,50.51],[102.07,51.26],[100.89,51.52],[99.98,51.63],[98.86,52.05],[97.83,51.01],[98.23,50.42],[97.26,49.73],[95.81,49.98],[94.82,50.01],[94.15,50.48],[93.11,50.49],[92.23,50.8],[90.71,50.33],[88.8,49.47],[87.75,49.3],[87.36,49.22],[86.83,49.83],[85.54,49.69],[85.11,50.12],[84.42,50.31],[83.94,50.89],[83.38,51.07],[81.95,50.81],[80.57,51.39],[80.03,50.87],[77.8,53.4],[76.52,54.18],[76.89,54.49],[74.39,53.55],[73.42,53.49],[73.51,54.04],[72.23,54.38],[71.18,54.13],[70.86,55.17],[69.07,55.38],[68.17,54.97],[65.67,54.6],[65.18,54.35],[61.44,54.01],[60.98,53.66],[61.7,52.98],[60.74,52.72],[60.93,52.45],[59.97,51.96],[61.59,51.27],[61.34,50.8],[59.93,50.84],[59.64,50.55],[58.36,51.06],[56.78,51.04],[55.72,50.62],[54.53,51.03],[52.33,51.72],[50.77,51.69],[48.7,50.6],[48.58,49.88],[47.55,50.45],[46.75,49.36],[47.04,49.15],[46.47,48.39],[47.31,47.72],[48.06,47.74],[48.7,47.08],[48.59,46.56],[49.1,46.4],[48.65,45.81],[47.68,45.64],[46.68,44.61],[47.59,43.66],[47.49,42.99],[48.58,41.81],[47.99,41.41],[47.81,41.15],[47.37,41.22],[46.69,41.83],[46.41,41.86],[45.78,42.09],[45.47,42.5],[44.54,42.71],[43.93,42.55],[43.76,42.74],[42.4,43.22],[40.92,43.38],[40.08,43.55],[39.95,43.44],[38.68,44.28],[37.54,44.66],[36.68,45.24],[37.4,45.41],[38.23,46.24],[37.67,46.64],[39.15,47.05],[39.12,47.26],[38.22,47.1],[38.26,47.55],[38.77,47.83],[39.74,47.9],[39.9,48.23],[39.67,48.78],[40.08,49.31],[40.07,49.6],[38.59,49.93],[38.01,49.92],[37.39,50.38],[36.62,50.23],[35.36,50.58],[35.38,50.77],[35.02,51.21],[34.22,51.26],[34.14,51.57],[34.39,51.77],[33.75,52.33],[32.72,52.24],[32.41,52.29],[32.16,52.06],[31.79,52.1],[31.54,52.74],[31.3,53.07],[31.5,53.17],[32.3,53.13],[32.69,53.35],[32.41,53.62],[31.73,53.79],[31.79,53.97],[31.38,54.16],[30.76,54.81],[30.97,55.08],[30.88,55.55],[29.9,55.79],[29.37,55.67],[29.23,55.92],[28.18,56.17],[27.86,56.76],[27.77,57.24],[27.29,57.47],[27.72,57.79],[27.42,58.72],[28.13,59.3],[27.98,59.48],[29.12,60.03],[28.07,60.5],[30.21,61.78],[31.14,62.36],[31.52,62.87],[30.04,63.55],[30.44,64.2],[29.54,64.95],[30.22,65.81],[29.05,66.94],[29.98,67.7],[28.45,68.36],[28.59,69.07],[29.4,69.16],[31.1,69.56],[32.13,69.91],[33.77,69.3],[36.51,69.06],[40.29,67.93],[41.06,67.46],[41.13,66.79],[40.02,66.27],[38.38,66],[33.92,66.76],[33.18,66.63],[34.81,65.9],[34.88,65.44],[34.94,64.41],[36.23,64.11],[37.01,63.85],[37.14,64.33],[36.54,64.76],[37.18,65.14],[39.59,64.52],[40.43,64.76],[39.76,65.5],[42.09,66.48],[43.02,66.42],[43.95,66.07],[44.53,66.76],[43.7,67.35],[44.19,67.95],[43.45,68.57],[46.25,68.25],[46.82,67.69],[45.56,67.57],[45.56,67.01],[46.35,66.67],[47.89,66.88],[48.14,67.52],[50.23,68],[53.72,68.86],[54.47,68.81],[53.49,68.2],[54.73,68.1],[55.44,68.44],[57.32,68.47],[58.8,68.88],[59.94,68.28],[61.08,68.94],[60.03,69.52],[60.55,69.85],[63.5,69.55],[64.89,69.23],[68.51,68.09],[69.18,68.62],[68.16,69.14],[68.14,69.36],[66.93,69.45],[67.26,69.93],[66.72,70.71],[66.7,71.03],[68.54,71.93],[69.2,72.84],[69.94,73.04],[72.59,72.78],[72.79,72.22],[71.85,71.41],[72.47,71.09],[72.79,70.39],[72.56,69.02],[73.67,68.41],[73.24,67.74],[71.28,66.32],[72.42,66.17],[72.82,66.53],[73.92,66.79],[74.19,67.28],[75.05,67.76],[74.47,68.33],[74.94,68.99],[73.84,69.07],[73.6,69.63],[74.4,70.63],[73.1,71.45],[74.89,72.12],[74.66,72.83],[75.16,72.86],[75.68,72.3],[75.29,71.34],[76.36,71.15],[75.9,71.87],[77.58,72.27],[79.65,72.32],[81.5,71.75],[80.61,72.58],[80.51,73.65],[82.25,73.85],[84.66,73.81],[86.82,73.94],[86.01,74.46],[87.17,75.12],[88.31,75.14],[90.26,75.64],[92.9,75.77],[93.24,76.05],[95.86,76.14],[96.68,75.92],[98.92,76.45],[100.76,76.43],[101.04,76.86],[101.99,77.29],[104.35,77.7],[106.07,77.37],[104.71,77.13],[106.97,76.97],[107.24,76.48],[108.15,76.72],[111.08,76.71],[113.33,76.22],[114.13,75.85],[113.89,75.33],[112.78,75.03],[110.15,74.48],[109.4,74.18],[110.64,74.04],[112.12,73.79],[113.02,73.98],[113.53,73.34],[113.97,73.59],[115.57,73.75],[118.78,73.59],[119.02,73.12],[123.2,72.97],[123.26,73.74],[125.38,73.56],[126.98,73.57],[128.59,73.04],[129.05,72.4],[128.46,71.98],[129.71,71.19],[131.29,70.79],[132.25,71.84],[133.86,71.39],[135.56,71.66],[137.5,71.35],[138.23,71.63],[139.87,71.49],[139.15,72.42],[140.47,72.85],[149.5,72.2],[150.35,71.61],[152.97,70.84],[157.01,71.03],[159,70.87],[159.83,70.45],[159.71,69.72],[160.94,69.44],[162.28,69.64],[164.05,69.67],[165.94,69.47],[167.84,69.58],[169.58,68.69],[170.82,69.01],[170.01,69.65],[170.45,70.1],[173.64,69.82],[175.72,69.88],[178.6,69.4],[-180,68.96],[-177.55,68.2],[-174.93,67.21],[-175.01,66.58],[-174.34,66.34],[-174.57,67.06],[-171.86,66.91],[-169.9,65.98],[-170.89,65.54],[-172.53,65.44],[-172.56,64.46],[-172.95,64.25],[-173.89,64.28],[-174.65,64.63],[-175.98,64.92],[-176.21,65.36],[-177.22,65.52],[-178.36,65.39],[-178.9,65.74],[-178.69,66.11],[-179.88,65.87],[-179.43,65.4],[-180,64.98],[179.99,64.97],[178.71,64.53],[177.41,64.61],[178.31,64.08],[178.91,63.25],[179.37,62.98],[179.49,62.57],[179.23,62.3],[177.36,62.52],[174.57,61.77],[173.68,61.65],[172.15,60.95],[170.7,60.34],[170.33,59.88],[168.9,60.57],[166.29,59.79],[165.84,60.16],[164.88,59.73],[163.54,59.87],[163.22,59.21],[162.02,58.24],[162.05,57.84],[163.19,57.62],[163.06,56.16],[162.13,56.12],[161.7,55.29],[162.12,54.85],[160.37,54.34],[160.02,53.2],[158.53,52.96],[158.23,51.94],[156.79,51.01],[156.42,51.7],[155.99,53.16],[155.43,55.38],[155.92,56.77],[156.76,57.36],[156.81,57.83],[158.36,58.06],[160.15,59.31],[161.87,60.34],[163.67,61.14],[164.47,62.55],[163.26,62.47],[162.66,61.64],[160.12,60.54],[159.3,61.77],[156.72,61.43],[154.22,59.76],[155.04,59.15],[152.81,58.88],[151.26,58.78],[151.34,59.5],[149.78,59.66],[148.55,59.16],[145.49,59.34],[142.2,59.04],[138.96,57.09],[135.13,54.73],[136.7,54.6],[137.19,53.98],[138.16,53.75],[138.8,54.25],[139.9,54.19],[141.35,53.09],[141.38,52.24],[140.6,51.24],[140.51,50.05],[140.06,48.45],[138.56,47],[138.22,46.31],[136.86,45.14],[135.51,43.99],[134.87,43.4],[133.54,42.81],[132.91,42.8],[132.28,43.28],[130.94,42.55],[130.78,42.22]],[[-180,71.52],[-179.87,71.56],[-179.02,71.56],[-177.58,71.27],[-177.66,71.13],[-178.69,70.89],[-180,70.83],[178.9,70.78],[178.73,71.1],[-180,71.52]],[[33.44,45.97],[33.7,46.22],[34.41,46],[34.73,45.97],[34.86,45.77],[35.01,45.74],[35.02,45.65],[35.51,45.41],[36.53,45.47],[36.33,45.11],[35.24,44.94],[33.88,44.36],[33.33,44.57],[33.55,45.03],[32.45,45.33],[32.63,45.52],[33.59,45.85],[33.44,45.97]],[[-78.98,26.79],[-78.51,26.87],[-77.85,26.84],[-77.82,26.58],[-78.91,26.42],[-78.98,26.79]],[[-77.79,27.04],[-77,26.59],[-77.17,25.88],[-77.36,26.01],[-77.34,26.53],[-77.79,26.93],[-77.79,27.04]],[[-78.19,25.21],[-77.89,25.17],[-77.54,24.34],[-77.54,23.76],[-77.78,23.71],[-78.03,24.29],[-78.41,24.57],[-78.19,25.21]],[[-61.2,-51.85],[-60,-51.25],[-59.15,-51.5],[-58.55,-51.1],[-57.75,-51.55],[-58.05,-51.9],[-59.4,-52.2],[-59.85,-51.85],[-60.7,-52.3],[-61.2,-51.85]],[[15.14,79.67],[15.52,80.02],[16.99,80.05],[18.25,79.7],[21.54,78.96],[19.03,78.56],[18.47,77.83],[17.6,77.64],[17.12,76.81],[15.91,76.77],[13.76,77.38],[14.67,77.74],[13.17,78.02],[11.22,78.87],[10.45,79.65],[13.17,80.01],[13.72,79.66],[15.14,79.67]],[[31.1,69.56],[29.4,69.16],[28.59,69.07],[29.01,69.77],[27.73,70.16],[26.18,69.83],[25.69,69.09],[24.73,68.65],[23.66,68.89],[22.36,68.84],[21.25,69.37],[20.64,69.11],[20.03,69.07],[19.88,68.41],[17.99,68.57],[17.73,68.01],[16.77,68.01],[16.11,67.3],[15.11,66.19],[13.56,64.79],[13.92,64.44],[13.57,64.05],[12.58,64.07],[11.93,63.13],[11.99,61.8],[12.63,61.29],[12.3,60.12],[11.47,59.43],[11.03,58.86],[10.36,59.47],[8.38,58.31],[7.05,58.08],[5.66,58.59],[5.31,59.66],[4.99,61.97],[5.91,62.62],[8.55,63.45],[10.53,64.49],[12.36,65.88],[14.76,67.81],[16.44,68.56],[19.18,69.82],[21.38,70.26],[23.02,70.2],[24.55,71.03],[26.37,70.99],[28.16,71.19],[31.29,70.45],[30,70.19],[31.1,69.56]],[[27.41,80.06],[25.93,79.52],[23.02,79.4],[20.08,79.57],[19.9,79.84],[18.46,79.86],[17.37,80.32],[20.46,80.6],[21.91,80.36],[22.92,80.66],[25.45,80.41],[27.41,80.06]],[[24.72,77.85],[22.49,77.45],[20.73,77.68],[21.41,77.93],[20.81,78.25],[22.88,78.46],[23.28,78.08],[24.72,77.85]],[[-46.76,82.63],[-43.41,83.23],[-39.9,83.18],[-38.62,83.55],[-35.09,83.65],[-27.1,83.52],[-20.85,82.73],[-22.69,82.34],[-26.52,82.3],[-31.9,82.2],[-31.4,82.02],[-27.86,82.13],[-24.85,81.79],[-22.9,82.09],[-22.07,81.73],[-23.17,81.15],[-20.62,81.52],[-15.77,81.91],[-12.77,81.72],[-12.21,81.29],[-16.28,80.58],[-16.85,80.35],[-20.05,80.18],[-17.73,80.13],[-18.9,79.4],[-19.7,78.75],[-19.67,77.64],[-18.47,76.98],[-20.04,76.94],[-21.68,76.63],[-19.83,76.1],[-19.6,75.25],[-20.67,75.16],[-19.37,74.3],[-21.59,74.22],[-20.44,73.82],[-20.76,73.46],[-22.17,73.31],[-23.57,73.31],[-22.31,72.63],[-22.3,72.18],[-24.28,72.6],[-24.79,72.33],[-23.44,72.08],[-22.13,71.47],[-21.75,70.66],[-23.54,70.47],[-24.31,70.86],[-25.54,71.43],[-25.2,70.75],[-26.36,70.23],[-23.73,70.18],[-22.35,70.13],[-25.03,69.26],[-27.75,68.47],[-30.67,68.12],[-31.78,68.12],[-32.81,67.74],[-34.2,66.68],[-36.35,65.98],[-37.04,65.94],[-38.37,65.69],[-39.81,65.46],[-40.67,64.84],[-40.68,64.14],[-41.19,63.48],[-42.82,62.68],[-42.42,61.9],[-42.87,61.07],[-43.38,60.1],[-44.79,60.04],[-46.26,60.85],[-48.26,60.86],[-49.23,61.41],[-49.9,62.38],[-51.63,63.63],[-52.14,64.28],[-52.28,65.18],[-53.66,66.1],[-53.3,66.84],[-53.97,67.19],[-52.98,68.36],[-51.48,68.73],[-51.08,69.15],[-50.87,69.93],[-52.02,69.57],[-52.56,69.43],[-53.46,69.28],[-54.68,69.61],[-54.75,70.29],[-54.36,70.82],[-53.43,70.84],[-51.39,70.57],[-53.11,71.2],[-54.01,71.55],[-55,71.41],[-55.83,71.66],[-54.72,72.59],[-55.33,72.96],[-56.12,73.65],[-57.33,74.71],[-58.6,75.1],[-58.59,75.52],[-61.27,76.1],[-63.39,76.18],[-66.07,76.14],[-68.5,76.06],[-69.67,76.38],[-71.4,77.01],[-68.78,77.32],[-66.76,77.38],[-71.04,77.64],[-73.3,78.04],[-73.16,78.43],[-69.37,78.91],[-65.71,79.4],[-65.32,79.76],[-68.02,80.12],[-67.15,80.52],[-63.69,81.21],[-62.24,81.32],[-62.65,81.77],[-60.28,82.03],[-57.21,82.19],[-54.14,82.2],[-53.04,81.89],[-50.39,82.44],[-48,82.06],[-46.6,81.99],[-44.52,81.66],[-46.9,82.2],[-46.76,82.63]],[[68.94,-48.62],[69.58,-48.94],[70.53,-49.07],[70.56,-49.25],[70.28,-49.71],[68.74,-49.77],[68.72,-49.24],[68.87,-48.83],[68.94,-48.62]],[[124.97,-8.89],[125.09,-8.66],[125.95,-8.43],[126.64,-8.4],[126.96,-8.27],[127.34,-8.4],[126.97,-8.67],[125.93,-9.11],[125.09,-9.39],[125.07,-9.09],[124.97,-8.89]],[[16.35,-28.58],[16.82,-28.08],[17.22,-28.36],[17.39,-28.78],[17.84,-28.86],[18.47,-29.05],[19,-28.97],[19.9,-28.46],[19.9,-24.77],[20.17,-24.92],[20.76,-25.87],[20.67,-26.48],[20.89,-26.83],[21.61,-26.73],[22.11,-26.28],[22.58,-25.98],[22.83,-25.5],[23.31,-25.27],[23.73,-25.39],[24.21,-25.67],[25.03,-25.72],[25.67,-25.49],[25.77,-25.17],[25.94,-24.7],[26.49,-24.62],[26.79,-24.24],[27.12,-23.58],[28.02,-22.83],[29.43,-22.09],[29.84,-22.1],[30.32,-22.27],[30.66,-22.15],[31.19,-22.25],[31.67,-23.66],[31.93,-24.37],[31.75,-25.48],[31.84,-25.84],[31.33,-25.66],[31.04,-25.73],[30.95,-26.02],[30.68,-26.4],[30.68,-26.74],[31.28,-27.29],[31.87,-27.18],[32.07,-26.73],[32.83,-26.74],[32.58,-27.47],[32.46,-28.3],[32.2,-28.75],[31.52,-29.26],[31.33,-29.4],[30.9,-29.91],[30.62,-30.42],[30.05,-31.14],[28.92,-32.17],[28.22,-32.77],[27.46,-33.23],[26.42,-33.62],[25.91,-33.67],[25.78,-33.95],[25.17,-33.8],[24.68,-33.99],[23.59,-33.79],[22.99,-33.92],[22.57,-33.86],[21.54,-34.26],[20.69,-34.42],[20.07,-34.8],[19.61,-34.82],[19.19,-34.46],[18.86,-34.44],[18.42,-34],[18.38,-34.14],[18.24,-33.87],[18.25,-33.28],[17.93,-32.61],[18.25,-32.43],[18.22,-31.66],[17.57,-30.73],[17.07,-29.88],[17.06,-29.88],[16.35,-28.58]],[[28.98,-28.96],[29.32,-29.26],[29.02,-29.74],[28.85,-30.07],[28.29,-30.23],[28.11,-30.55],[27.75,-30.64],[27,-29.88],[27.53,-29.24],[28.07,-28.85],[28.54,-28.65],[28.98,-28.96]],[[-117.13,32.53],[-115.99,32.61],[-114.72,32.72],[-114.81,32.52],[-113.31,32.04],[-111.02,31.33],[-109.04,31.34],[-108.24,31.34],[-108.24,31.75],[-106.51,31.75],[-106.14,31.4],[-105.63,31.08],[-105.04,30.64],[-104.71,30.12],[-104.46,29.57],[-103.94,29.27],[-103.11,28.97],[-102.48,29.76],[-101.66,29.78],[-100.96,29.38],[-100.46,28.7],[-100.11,28.11],[-99.52,27.54],[-99.3,26.84],[-99.02,26.37],[-98.24,26.06],[-97.53,25.84],[-97.14,25.87],[-97.53,24.99],[-97.7,24.27],[-97.78,22.93],[-97.87,22.44],[-97.7,21.9],[-97.39,21.41],[-97.19,20.64],[-96.53,19.89],[-96.29,19.32],[-95.9,18.83],[-94.84,18.56],[-94.43,18.14],[-93.55,18.42],[-92.79,18.53],[-92.04,18.71],[-91.41,18.88],[-90.77,19.28],[-90.53,19.87],[-90.45,20.71],[-90.28,21],[-89.6,21.26],[-88.54,21.49],[-87.66,21.46],[-87.05,21.54],[-86.81,21.33],[-86.85,20.85],[-87.38,20.26],[-87.62,19.65],[-87.44,19.47],[-87.59,19.04],[-87.84,18.26],[-88.09,18.52],[-88.3,18.5],[-88.49,18.49],[-88.85,17.88],[-89.03,18],[-89.15,17.96],[-89.14,17.81],[-90.07,17.82],[-91,17.82],[-91,17.25],[-91.45,17.25],[-91.08,16.92],[-90.71,16.69],[-90.6,16.47],[-90.44,16.41],[-90.46,16.07],[-91.75,16.07],[-92.23,15.25],[-92.09,15.06],[-92.2,14.83],[-92.23,14.54],[-93.36,15.62],[-93.88,15.94],[-94.69,16.2],[-95.25,16.13],[-96.05,15.75],[-96.56,15.65],[-97.26,15.92],[-98.01,16.11],[-98.95,16.57],[-99.7,16.71],[-100.83,17.17],[-101.67,17.65],[-101.92,17.92],[-102.48,17.98],[-103.5,18.29],[-103.92,18.75],[-104.99,19.32],[-105.49,19.95],[-105.73,20.43],[-105.4,20.53],[-105.5,20.82],[-105.27,21.08],[-105.27,21.42],[-105.6,21.87],[-105.69,22.27],[-106.03,22.77],[-106.91,23.77],[-107.92,24.55],[-108.4,25.17],[-109.26,25.58],[-109.44,25.83],[-109.29,26.44],[-109.8,26.68],[-110.39,27.16],[-110.64,27.86],[-111.18,27.94],[-111.76,28.47],[-112.23,28.96],[-112.27,29.27],[-112.81,30.02],[-113.17,30.79],[-113.15,31.17],[-113.87,31.57],[-114.21,31.52],[-114.78,31.8],[-114.94,31.39],[-114.77,30.91],[-114.67,30.16],[-114.33,29.75],[-113.59,29.06],[-113.42,28.83],[-113.27,28.76],[-113.14,28.41],[-112.96,28.43],[-112.76,27.78],[-112.46,27.53],[-112.24,27.17],[-111.62,26.66],[-111.29,25.73],[-110.99,25.29],[-110.71,24.83],[-110.66,24.3],[-110.17,24.27],[-109.77,23.81],[-109.41,23.36],[-109.43,23.19],[-109.85,22.82],[-110.03,22.82],[-110.3,23.43],[-110.95,24],[-111.67,24.49],[-112.18,24.74],[-112.15,25.47],[-112.3,26.01],[-112.78,26.32],[-113.46,26.77],[-113.6,26.64],[-113.85,26.9],[-114.46,27.14],[-115.06,27.72],[-114.98,27.8],[-114.57,27.74],[-114.2,28.12],[-114.16,28.57],[-114.93,29.28],[-115.52,29.56],[-115.89,30.18],[-116.26,30.84],[-116.72,31.64],[-117.13,32.53]],[[-57.62,-30.22],[-56.98,-30.11],[-55.97,-30.88],[-55.6,-30.85],[-54.57,-31.49],[-53.79,-32.05],[-53.21,-32.73],[-53.65,-33.2],[-53.37,-33.77],[-53.81,-34.4],[-54.93,-34.95],[-55.67,-34.75],[-56.22,-34.86],[-57.14,-34.43],[-57.82,-34.46],[-58.43,-33.91],[-58.35,-33.26],[-58.13,-33.04],[-58.14,-32.04],[-57.88,-31.02],[-57.62,-30.22]],[[-53.37,-33.77],[-53.65,-33.2],[-53.21,-32.73],[-53.79,-32.05],[-54.57,-31.49],[-55.6,-30.85],[-55.97,-30.88],[-56.98,-30.11],[-57.62,-30.22],[-56.29,-28.85],[-55.16,-27.88],[-54.49,-27.47],[-53.65,-26.92],[-53.63,-26.12],[-54.13,-25.55],[-54.63,-25.74],[-54.43,-25.16],[-54.29,-24.57],[-54.29,-24.02],[-54.65,-23.84],[-55.03,-24],[-55.4,-23.96],[-55.52,-23.57],[-55.61,-22.66],[-55.8,-22.36],[-56.47,-22.09],[-56.88,-22.28],[-57.94,-22.09],[-57.87,-20.73],[-58.17,-20.18],[-57.85,-19.97],[-57.95,-19.4],[-57.67,-18.96],[-57.5,-18.17],[-57.74,-17.55],[-58.28,-17.27],[-58.39,-16.88],[-58.24,-16.3],[-60.16,-16.26],[-60.54,-15.09],[-60.25,-15.08],[-60.26,-14.65],[-60.46,-14.35],[-60.5,-13.78],[-61.08,-13.48],[-61.71,-13.49],[-62.13,-13.2],[-62.8,-13],[-63.2,-12.63],[-64.32,-12.46],[-65.4,-11.57],[-65.32,-10.9],[-65.44,-10.51],[-65.34,-9.76],[-66.65,-9.93],[-67.17,-10.31],[-68.05,-10.71],[-68.27,-11.01],[-68.79,-11.04],[-69.53,-10.95],[-70.09,-11.12],[-70.55,-11.01],[-70.48,-9.49],[-71.3,-10.08],[-72.19,-10.05],[-72.56,-9.52],[-73.23,-9.46],[-73.01,-9.03],[-73.57,-8.42],[-73.99,-7.52],[-73.72,-7.34],[-73.72,-6.92],[-73.12,-6.63],[-73.22,-6.09],[-72.96,-5.74],[-72.89,-5.28],[-71.75,-4.59],[-70.93,-4.4],[-70.8,-4.25],[-69.89,-4.3],[-69.44,-1.56],[-69.42,-1.12],[-69.58,-.55],[-70.02,-.19],[-70.02,.54],[-69.45,.71],[-69.25,.6],[-69.22,.99],[-69.8,1.09],[-69.82,1.72],[-67.87,1.69],[-67.54,2.04],[-67.26,1.72],[-67.06,1.13],[-66.88,1.25],[-66.33,.72],[-65.55,.79],[-65.35,1.1],[-64.61,1.33],[-64.2,1.49],[-64.08,1.92],[-63.37,2.2],[-63.42,2.41],[-64.27,2.5],[-64.41,3.13],[-64.37,3.8],[-64.82,4.06],[-64.63,4.15],[-63.89,4.02],[-63.09,3.77],[-62.8,4.01],[-62.08,4.16],[-60.97,4.54],[-60.6,4.92],[-60.73,5.2],[-60.21,5.24],[-59.98,5.01],[-60.11,4.58],[-59.77,4.42],[-59.54,3.96],[-59.82,3.61],[-59.97,2.76],[-59.72,2.25],[-59.65,1.79],[-59.03,1.32],[-58.54,1.27],[-58.43,1.46],[-58.11,1.51],[-57.66,1.68],[-57.34,1.95],[-56.78,1.86],[-56.54,1.9],[-56,1.82],[-55.91,2.02],[-56.07,2.22],[-55.97,2.51],[-55.57,2.42],[-55.1,2.52],[-54.52,2.31],[-54.09,2.11],[-53.78,2.38],[-53.56,2.33],[-53.42,2.05],[-52.94,2.12],[-52.56,2.5],[-52.25,3.24],[-51.66,4.16],[-51.32,4.2],[-51.07,3.65],[-50.51,1.9],[-49.97,1.74],[-49.95,1.05],[-50.7,.22],[-50.39,-.08],[-48.62,-.23],[-48.58,-1.24],[-47.82,-.58],[-46.57,-.94],[-44.91,-1.55],[-44.42,-2.14],[-44.58,-2.69],[-43.42,-2.38],[-41.47,-2.91],[-39.98,-2.87],[-38.5,-3.7],[-37.22,-4.82],[-36.45,-5.11],[-35.6,-5.15],[-35.24,-5.46],[-34.9,-6.74],[-34.73,-7.34],[-35.13,-9],[-35.64,-9.65],[-37.05,-11.04],[-37.68,-12.17],[-38.42,-13.04],[-38.67,-13.06],[-38.95,-13.79],[-38.88,-15.67],[-39.16,-17.21],[-39.27,-17.87],[-39.58,-18.26],[-39.76,-19.6],[-40.78,-20.9],[-40.95,-21.94],[-41.76,-22.37],[-41.99,-22.97],[-43.08,-22.97],[-44.65,-23.35],[-45.35,-23.8],[-46.47,-24.09],[-47.65,-24.89],[-48.49,-25.88],[-48.64,-26.62],[-48.48,-27.18],[-48.66,-28.19],[-48.89,-28.67],[-49.59,-29.22],[-50.7,-30.99],[-51.58,-31.78],[-52.26,-32.25],[-52.71,-33.2],[-53.37,-33.77]],[[-69.53,-10.95],[-68.79,-11.04],[-68.27,-11.01],[-68.05,-10.71],[-67.17,-10.31],[-66.65,-9.93],[-65.34,-9.76],[-65.44,-10.51],[-65.32,-10.9],[-65.4,-11.57],[-64.32,-12.46],[-63.2,-12.63],[-62.8,-13],[-62.13,-13.2],[-61.71,-13.49],[-61.08,-13.48],[-60.5,-13.78],[-60.46,-14.35],[-60.26,-14.65],[-60.25,-15.08],[-60.54,-15.09],[-60.16,-16.26],[-58.24,-16.3],[-58.39,-16.88],[-58.28,-17.27],[-57.74,-17.55],[-57.5,-18.17],[-57.67,-18.96],[-57.95,-19.4],[-57.85,-19.97],[-58.17,-20.18],[-58.18,-19.87],[-59.11,-19.36],[-60.04,-19.34],[-61.79,-19.63],[-62.26,-20.51],[-62.29,-21.05],[-62.69,-22.25],[-62.85,-22.03],[-63.99,-21.99],[-64.38,-22.8],[-64.96,-22.08],[-66.27,-21.83],[-67.11,-22.74],[-67.83,-22.87],[-68.22,-21.49],[-68.76,-20.37],[-68.44,-19.4],[-68.97,-18.98],[-69.1,-18.26],[-69.59,-17.58],[-68.96,-16.5],[-69.39,-15.66],[-69.16,-15.32],[-69.34,-14.95],[-68.95,-14.45],[-68.93,-13.6],[-68.88,-12.9],[-68.67,-12.56],[-69.53,-10.95]],[[-69.89,-4.3],[-70.8,-4.25],[-70.93,-4.4],[-71.75,-4.59],[-72.89,-5.28],[-72.96,-5.74],[-73.22,-6.09],[-73.12,-6.63],[-73.72,-6.92],[-73.72,-7.34],[-73.99,-7.52],[-73.57,-8.42],[-73.01,-9.03],[-73.23,-9.46],[-72.56,-9.52],[-72.19,-10.05],[-71.3,-10.08],[-70.48,-9.49],[-70.55,-11.01],[-70.09,-11.12],[-69.53,-10.95],[-68.67,-12.56],[-68.88,-12.9],[-68.93,-13.6],[-68.95,-14.45],[-69.34,-14.95],[-69.16,-15.32],[-69.39,-15.66],[-68.96,-16.5],[-69.59,-17.58],[-69.86,-18.09],[-70.37,-18.35],[-71.38,-17.77],[-71.46,-17.36],[-73.45,-16.36],[-75.24,-15.27],[-76.01,-14.65],[-76.42,-13.82],[-76.26,-13.53],[-77.11,-12.22],[-78.09,-10.38],[-79.04,-8.39],[-79.45,-7.93],[-79.76,-7.19],[-80.54,-6.54],[-81.25,-6.14],[-80.93,-5.69],[-81.41,-4.74],[-81.1,-4.04],[-80.3,-3.4],[-80.19,-3.82],[-80.47,-4.06],[-80.44,-4.43],[-80.03,-4.35],[-79.62,-4.45],[-79.21,-4.96],[-78.64,-4.55],[-78.45,-3.87],[-77.84,-3],[-76.64,-2.61],[-75.54,-1.56],[-75.24,-.91],[-75.37,-.15],[-75.11,-.06],[-74.44,-.53],[-74.12,-1],[-73.66,-1.26],[-73.07,-2.31],[-72.33,-2.44],[-71.78,-2.17],[-71.41,-2.34],[-70.81,-2.26],[-70.05,-2.72],[-70.69,-3.74],[-70.39,-3.77],[-69.89,-4.3]],[[-66.88,1.25],[-67.06,1.13],[-67.26,1.72],[-67.54,2.04],[-67.87,1.69],[-69.82,1.72],[-69.8,1.09],[-69.22,.99],[-69.25,.6],[-69.45,.71],[-70.02,.54],[-70.02,-.19],[-69.58,-.55],[-69.42,-1.12],[-69.44,-1.56],[-69.89,-4.3],[-70.39,-3.77],[-70.69,-3.74],[-70.05,-2.72],[-70.81,-2.26],[-71.41,-2.34],[-71.78,-2.17],[-72.33,-2.44],[-73.07,-2.31],[-73.66,-1.26],[-74.12,-1],[-74.44,-.53],[-75.11,-.06],[-75.37,-.15],[-75.8,.09],[-76.29,.42],[-76.58,.26],[-77.42,.39],[-77.67,.83],[-77.86,.81],[-78.86,1.38],[-78.99,1.69],[-78.62,1.77],[-78.66,2.27],[-78.43,2.63],[-77.93,2.7],[-77.51,3.32],[-77.13,3.85],[-77.5,4.09],[-77.31,4.67],[-77.53,5.58],[-77.32,5.84],[-77.48,6.69],[-77.88,7.22],[-77.75,7.71],[-77.43,7.64],[-77.24,7.94],[-77.47,8.52],[-77.35,8.67],[-76.84,8.64],[-76.08,9.34],[-75.67,9.44],[-75.66,9.77],[-75.48,10.62],[-74.91,11.08],[-74.28,11.1],[-74.2,11.31],[-73.41,11.23],[-72.63,11.73],[-72.24,11.96],[-71.75,12.44],[-71.4,12.38],[-71.14,12.11],[-71.33,11.78],[-71.97,11.61],[-72.23,11.11],[-72.61,10.82],[-72.91,10.45],[-73.03,9.74],[-73.31,9.15],[-72.79,9.08],[-72.66,8.63],[-72.44,8.41],[-72.36,8],[-72.48,7.63],[-72.45,7.42],[-72.2,7.34],[-71.96,6.99],[-70.67,7.09],[-70.09,6.96],[-69.39,6.1],[-68.99,6.21],[-68.27,6.15],[-67.7,6.27],[-67.34,6.1],[-67.52,5.56],[-67.74,5.22],[-67.82,4.5],[-67.62,3.84],[-67.34,3.54],[-67.3,3.32],[-67.81,2.82],[-67.45,2.6],[-67.18,2.25],[-66.88,1.25]],[[-77.35,8.67],[-77.47,8.52],[-77.24,7.94],[-77.43,7.64],[-77.75,7.71],[-77.88,7.22],[-78.22,7.51],[-78.43,8.05],[-78.18,8.32],[-78.44,8.39],[-78.62,8.72],[-79.12,9],[-79.56,8.93],[-79.76,8.59],[-80.16,8.33],[-80.38,8.3],[-80.48,8.09],[-80.01,7.55],[-80.28,7.42],[-80.42,7.27],[-80.89,7.22],[-81.06,7.82],[-81.19,7.65],[-81.52,7.71],[-81.72,8.11],[-82.13,8.18],[-82.39,8.29],[-82.82,8.29],[-82.85,8.07],[-82.96,8.22],[-82.91,8.42],[-82.83,8.63],[-82.87,8.81],[-82.72,8.93],[-82.93,9.07],[-82.93,9.48],[-82.55,9.57],[-82.19,9.21],[-82.21,8.99],[-81.81,8.95],[-81.72,9.03],[-81.44,8.79],[-80.95,8.86],[-80.52,9.11],[-79.92,9.31],[-79.57,9.61],[-79.02,9.55],[-79.06,9.46],[-78.5,9.42],[-78.05,9.25],[-77.73,8.95],[-77.35,8.67]],[[-82.55,9.57],[-82.93,9.48],[-82.93,9.07],[-82.72,8.93],[-82.87,8.81],[-82.83,8.63],[-82.91,8.42],[-82.96,8.22],[-83.51,8.45],[-83.71,8.66],[-83.59,8.83],[-83.63,9.05],[-83.91,9.29],[-84.3,9.49],[-84.65,9.62],[-84.71,9.91],[-84.98,10.09],[-84.91,9.8],[-85.11,9.56],[-85.34,9.83],[-85.66,9.93],[-85.8,10.14],[-85.79,10.44],[-85.66,10.76],[-85.94,10.9],[-85.71,11.09],[-85.56,11.22],[-84.9,10.95],[-84.67,11.08],[-84.35,11],[-84.19,10.79],[-83.89,10.73],[-83.66,10.94],[-83.4,10.4],[-83.02,9.99],[-82.55,9.57]],[[-83.66,10.94],[-83.89,10.73],[-84.19,10.79],[-84.35,11],[-84.67,11.08],[-84.9,10.95],[-85.56,11.22],[-85.71,11.09],[-86.06,11.4],[-86.53,11.81],[-86.74,12.14],[-87.17,12.46],[-87.67,12.91],[-87.56,13.06],[-87.39,12.91],[-87.32,12.98],[-87.01,13.03],[-86.88,13.26],[-86.73,13.26],[-86.76,13.75],[-86.52,13.78],[-86.31,13.77],[-86.1,14.04],[-85.8,13.84],[-85.7,13.96],[-85.51,14.08],[-85.16,14.36],[-85.15,14.56],[-85.05,14.55],[-84.92,14.79],[-84.82,14.82],[-84.65,14.67],[-84.45,14.62],[-84.23,14.75],[-83.98,14.75],[-83.63,14.88],[-83.49,15.02],[-83.15,15],[-83.23,14.9],[-83.29,14.68],[-83.18,14.31],[-83.41,13.97],[-83.52,13.57],[-83.55,13.13],[-83.5,12.87],[-83.47,12.42],[-83.63,12.32],[-83.72,11.89],[-83.65,11.63],[-83.85,11.37],[-83.81,11.1],[-83.66,10.94]],[[-83.15,15],[-83.49,15.02],[-83.63,14.88],[-83.98,14.75],[-84.23,14.75],[-84.45,14.62],[-84.65,14.67],[-84.82,14.82],[-84.92,14.79],[-85.05,14.55],[-85.15,14.56],[-85.16,14.36],[-85.51,14.08],[-85.7,13.96],[-85.8,13.84],[-86.1,14.04],[-86.31,13.77],[-86.52,13.78],[-86.76,13.75],[-86.73,13.26],[-86.88,13.26],[-87.01,13.03],[-87.32,12.98],[-87.49,13.3],[-87.79,13.38],[-87.72,13.78],[-87.86,13.89],[-88.07,13.96],[-88.51,13.85],[-88.54,13.98],[-88.84,14.14],[-89.06,14.34],[-89.35,14.42],[-89.15,14.68],[-89.23,14.87],[-89.15,15.07],[-88.68,15.35],[-88.22,15.73],[-88.12,15.69],[-87.9,15.86],[-87.62,15.88],[-87.52,15.8],[-87.37,15.85],[-86.9,15.76],[-86.44,15.78],[-86.12,15.89],[-86,16.01],[-85.68,15.95],[-85.45,15.89],[-85.18,15.91],[-84.98,16],[-84.53,15.86],[-84.37,15.83],[-84.06,15.65],[-83.77,15.42],[-83.41,15.27],[-83.15,15]],[[-89.35,14.42],[-89.06,14.34],[-88.84,14.14],[-88.54,13.98],[-88.51,13.85],[-88.07,13.96],[-87.86,13.89],[-87.72,13.78],[-87.79,13.38],[-87.9,13.15],[-88.48,13.16],[-88.84,13.26],[-89.26,13.46],[-89.81,13.52],[-90.1,13.74],[-90.06,13.88],[-89.72,14.13],[-89.53,14.25],[-89.59,14.36],[-89.35,14.42]],[[-92.23,14.54],[-92.2,14.83],[-92.09,15.06],[-92.23,15.25],[-91.75,16.07],[-90.46,16.07],[-90.44,16.41],[-90.6,16.47],[-90.71,16.69],[-91.08,16.92],[-91.45,17.25],[-91,17.25],[-91,17.82],[-90.07,17.82],[-89.14,17.81],[-89.15,17.02],[-89.23,15.89],[-88.93,15.89],[-88.61,15.71],[-88.52,15.85],[-88.22,15.73],[-88.68,15.35],[-89.15,15.07],[-89.23,14.87],[-89.15,14.68],[-89.35,14.42],[-89.59,14.36],[-89.53,14.25],[-89.72,14.13],[-90.06,13.88],[-90.1,13.74],[-90.61,13.91],[-91.23,13.93],[-91.69,14.13],[-92.23,14.54]],[[-89.14,17.81],[-89.15,17.96],[-89.03,18],[-88.85,17.88],[-88.49,18.49],[-88.3,18.5],[-88.3,18.35],[-88.11,18.35],[-88.12,18.08],[-88.29,17.64],[-88.2,17.49],[-88.3,17.13],[-88.24,17.04],[-88.35,16.53],[-88.55,16.27],[-88.73,16.23],[-88.93,15.89],[-89.23,15.89],[-89.15,17.02],[-89.14,17.81]],[[-60.73,5.2],[-60.6,4.92],[-60.97,4.54],[-62.08,4.16],[-62.8,4.01],[-63.09,3.77],[-63.89,4.02],[-64.63,4.15],[-64.82,4.06],[-64.37,3.8],[-64.41,3.13],[-64.27,2.5],[-63.42,2.41],[-63.37,2.2],[-64.08,1.92],[-64.2,1.49],[-64.61,1.33],[-65.35,1.1],[-65.55,.79],[-66.33,.72],[-66.88,1.25],[-67.18,2.25],[-67.45,2.6],[-67.81,2.82],[-67.3,3.32],[-67.34,3.54],[-67.62,3.84],[-67.82,4.5],[-67.74,5.22],[-67.52,5.56],[-67.34,6.1],[-67.7,6.27],[-68.27,6.15],[-68.99,6.21],[-69.39,6.1],[-70.09,6.96],[-70.67,7.09],[-71.96,6.99],[-72.2,7.34],[-72.45,7.42],[-72.48,7.63],[-72.36,8],[-72.44,8.41],[-72.66,8.63],[-72.79,9.08],[-73.31,9.15],[-73.03,9.74],[-72.91,10.45],[-72.61,10.82],[-72.23,11.11],[-71.97,11.61],[-71.33,11.78],[-71.36,11.54],[-71.95,11.42],[-71.62,10.97],[-71.63,10.45],[-72.07,9.86],[-71.7,9.07],[-71.26,9.14],[-71.04,9.86],[-71.35,10.21],[-71.4,10.97],[-70.16,11.38],[-70.29,11.85],[-69.94,12.16],[-69.58,11.46],[-68.88,11.44],[-68.23,10.89],[-68.19,10.56],[-67.3,10.55],[-66.23,10.65],[-65.66,10.2],[-64.89,10.08],[-64.33,10.39],[-64.32,10.64],[-63.08,10.7],[-61.88,10.72],[-62.73,10.42],[-62.39,9.95],[-61.59,9.87],[-60.83,9.38],[-60.67,8.58],[-60.15,8.6],[-59.76,8.37],[-60.55,7.78],[-60.64,7.42],[-60.3,7.04],[-60.54,6.86],[-61.16,6.7],[-61.14,6.23],[-61.41,5.96],[-60.73,5.2]],[[-56.54,1.9],[-56.78,1.86],[-57.34,1.95],[-57.66,1.68],[-58.11,1.51],[-58.43,1.46],[-58.54,1.27],[-59.03,1.32],[-59.65,1.79],[-59.72,2.25],[-59.97,2.76],[-59.82,3.61],[-59.54,3.96],[-59.77,4.42],[-60.11,4.58],[-59.98,5.01],[-60.21,5.24],[-60.73,5.2],[-61.41,5.96],[-61.14,6.23],[-61.16,6.7],[-60.54,6.86],[-60.3,7.04],[-60.64,7.42],[-60.55,7.78],[-59.76,8.37],[-59.1,8],[-58.48,7.35],[-58.46,6.83],[-58.08,6.81],[-57.54,6.32],[-57.15,5.97],[-57.31,5.07],[-57.92,4.81],[-57.86,4.58],[-58.05,4.06],[-57.6,3.33],[-57.28,3.33],[-57.15,2.77],[-56.54,1.9]],[[-54.52,2.31],[-55.1,2.52],[-55.57,2.42],[-55.97,2.51],[-56.07,2.22],[-55.91,2.02],[-56,1.82],[-56.54,1.9],[-57.15,2.77],[-57.28,3.33],[-57.6,3.33],[-58.05,4.06],[-57.86,4.58],[-57.92,4.81],[-57.31,5.07],[-57.15,5.97],[-55.95,5.77],[-55.84,5.95],[-55.03,6.03],[-53.96,5.76],[-54.48,4.9],[-54.4,4.21],[-54.01,3.62],[-54.18,3.19],[-54.27,2.73],[-54.52,2.31]],[[-51.66,4.16],[-52.25,3.24],[-52.56,2.5],[-52.94,2.12],[-53.42,2.05],[-53.56,2.33],[-53.78,2.38],[-54.09,2.11],[-54.52,2.31],[-54.27,2.73],[-54.18,3.19],[-54.01,3.62],[-54.4,4.21],[-54.48,4.9],[-53.96,5.76],[-53.62,5.65],[-52.88,5.41],[-51.82,4.57],[-51.66,4.16]],[[6.19,49.46],[6.66,49.2],[8.1,49.02],[7.59,48.33],[7.47,47.62],[7.19,47.45],[6.74,47.54],[6.77,47.29],[6.04,46.73],[6.02,46.27],[6.5,46.43],[6.84,45.99],[6.8,45.71],[7.1,45.33],[6.75,45.03],[7.01,44.25],[7.55,44.13],[7.44,43.69],[6.53,43.13],[4.56,43.4],[3.1,43.07],[2.99,42.47],[1.83,42.34],[.7,42.8],[.34,42.58],[-1.5,43.03],[-1.9,43.42],[-1.38,44.02],[-1.19,46.01],[-2.23,47.06],[-2.96,47.57],[-4.49,47.95],[-4.59,48.68],[-3.3,48.9],[-1.62,48.64],[-1.94,49.78],[-.99,49.35],[1.34,50.13],[1.64,50.95],[2.51,51.15],[2.66,50.8],[3.12,50.78],[3.59,50.38],[4.29,49.91],[4.8,49.99],[5.68,49.53],[5.9,49.44],[6.19,49.46]],[[8.75,42.63],[9.39,43.01],[9.56,42.15],[9.23,41.38],[8.78,41.58],[8.54,42.26],[8.75,42.63]],[[-75.37,-.15],[-75.24,-.91],[-75.54,-1.56],[-76.64,-2.61],[-77.84,-3],[-78.45,-3.87],[-78.64,-4.55],[-79.21,-4.96],[-79.62,-4.45],[-80.03,-4.35],[-80.44,-4.43],[-80.47,-4.06],[-80.19,-3.82],[-80.3,-3.4],[-79.77,-2.66],[-79.99,-2.22],[-80.37,-2.69],[-80.97,-2.25],[-80.77,-1.96],[-80.93,-1.06],[-80.59,-.91],[-80.4,-.28],[-80.02,.36],[-80.09,.77],[-79.54,.98],[-78.86,1.38],[-77.86,.81],[-77.67,.83],[-77.42,.39],[-76.58,.26],[-76.29,.42],[-75.8,.09],[-75.37,-.15]],[[-66.28,18.52],[-65.77,18.43],[-65.59,18.23],[-65.85,17.98],[-66.6,17.98],[-67.19,17.95],[-67.24,18.37],[-67.1,18.52],[-66.28,18.52]],[[-77.57,18.49],[-76.89,18.4],[-76.37,18.16],[-76.2,17.89],[-76.9,17.87],[-77.2,17.7],[-77.77,17.86],[-78.34,18.23],[-78.22,18.45],[-77.8,18.52],[-77.57,18.49]],[[-82.27,23.19],[-81.41,23.12],[-80.62,23.11],[-79.68,22.77],[-79.28,22.4],[-78.35,22.51],[-77.99,22.28],[-77.15,21.66],[-76.52,21.21],[-76.19,21.22],[-75.6,21.02],[-75.67,20.73],[-74.93,20.69],[-74.18,20.28],[-74.3,20.05],[-74.96,19.92],[-75.63,19.87],[-76.32,19.95],[-77.76,19.86],[-77.09,20.41],[-77.49,20.67],[-78.14,20.74],[-78.48,21.03],[-78.72,21.6],[-79.29,21.56],[-80.22,21.83],[-80.52,22.04],[-81.82,22.19],[-82.17,22.39],[-81.79,22.64],[-82.78,22.69],[-83.49,22.17],[-83.91,22.15],[-84.05,21.91],[-84.55,21.8],[-84.97,21.9],[-84.45,22.21],[-84.23,22.57],[-83.78,22.79],[-83.27,22.98],[-82.51,23.08],[-82.27,23.19]],[[31.19,-22.25],[30.66,-22.15],[30.32,-22.27],[29.84,-22.1],[29.43,-22.09],[28.79,-21.64],[28.02,-21.49],[27.73,-20.85],[27.73,-20.5],[27.3,-20.39],[26.16,-19.29],[25.85,-18.71],[25.65,-18.54],[25.26,-17.74],[26.38,-17.85],[26.71,-17.96],[27.05,-17.94],[27.6,-17.29],[28.47,-16.47],[28.83,-16.39],[28.95,-16.04],[29.52,-15.65],[30.27,-15.51],[30.34,-15.88],[31.17,-15.86],[31.64,-16.07],[31.85,-16.32],[32.33,-16.39],[32.85,-16.71],[32.85,-17.98],[32.65,-18.67],[32.61,-19.42],[32.77,-19.72],[32.66,-20.31],[32.51,-20.39],[32.24,-21.12],[31.19,-22.25]],[[29.43,-22.09],[28.02,-22.83],[27.12,-23.58],[26.79,-24.24],[26.49,-24.62],[25.94,-24.7],[25.77,-25.17],[25.67,-25.49],[25.03,-25.72],[24.21,-25.67],[23.73,-25.39],[23.31,-25.27],[22.83,-25.5],[22.58,-25.98],[22.11,-26.28],[21.61,-26.73],[20.89,-26.83],[20.67,-26.48],[20.76,-25.87],[20.17,-24.92],[19.9,-24.77],[19.9,-21.85],[20.88,-21.81],[20.91,-18.25],[21.66,-18.22],[23.2,-17.87],[23.58,-18.28],[24.22,-17.89],[24.52,-17.89],[25.08,-17.66],[25.26,-17.74],[25.65,-18.54],[25.85,-18.71],[26.16,-19.29],[27.3,-20.39],[27.73,-20.5],[27.73,-20.85],[28.02,-21.49],[28.79,-21.64],[29.43,-22.09]],[[19.9,-24.77],[19.9,-28.46],[19,-28.97],[18.47,-29.05],[17.84,-28.86],[17.39,-28.78],[17.22,-28.36],[16.82,-28.08],[16.35,-28.58],[15.6,-27.82],[15.21,-27.09],[14.99,-26.12],[14.74,-25.39],[14.41,-23.85],[14.38,-22.66],[14.26,-22.11],[13.87,-21.7],[13.35,-20.87],[12.83,-19.67],[12.61,-19.05],[11.8,-18.07],[11.73,-17.3],[12.22,-17.11],[12.81,-16.94],[13.46,-16.97],[14.06,-17.42],[14.21,-17.35],[18.26,-17.31],[18.96,-17.79],[21.38,-17.93],[23.21,-17.52],[24.04,-17.3],[24.68,-17.35],[25.08,-17.58],[25.08,-17.66],[24.52,-17.89],[24.22,-17.89],[23.58,-18.28],[23.2,-17.87],[21.66,-18.22],[20.91,-18.25],[20.88,-21.81],[19.9,-21.85],[19.9,-24.77]],[[-16.71,13.6],[-17.13,14.37],[-17.62,14.73],[-17.18,14.92],[-16.7,15.62],[-16.46,16.14],[-16.12,16.46],[-15.62,16.37],[-15.14,16.59],[-14.58,16.6],[-14.1,16.3],[-13.44,16.04],[-12.83,15.3],[-12.17,14.62],[-12.12,13.99],[-11.93,13.42],[-11.55,13.14],[-11.47,12.75],[-11.51,12.44],[-11.66,12.39],[-12.2,12.47],[-12.28,12.35],[-12.5,12.33],[-13.22,12.58],[-13.7,12.59],[-15.55,12.63],[-15.82,12.52],[-16.15,12.55],[-16.68,12.39],[-16.84,13.15],[-15.93,13.13],[-15.69,13.27],[-15.51,13.28],[-15.14,13.51],[-14.71,13.3],[-14.28,13.28],[-13.84,13.51],[-14.05,13.79],[-14.38,13.63],[-14.69,13.63],[-15.08,13.88],[-15.4,13.86],[-15.63,13.62],[-16.71,13.6]],[[-11.51,12.44],[-11.47,12.75],[-11.55,13.14],[-11.93,13.42],[-12.12,13.99],[-12.17,14.62],[-11.84,14.8],[-11.67,15.39],[-11.35,15.41],[-10.65,15.13],[-10.09,15.33],[-9.7,15.26],[-9.55,15.49],[-5.54,15.5],[-5.32,16.2],[-5.49,16.33],[-5.97,20.64],[-6.45,24.96],[-4.92,24.97],[-1.55,22.79],[1.82,20.61],[2.06,20.14],[2.68,19.86],[3.15,19.69],[3.16,19.06],[4.27,19.16],[4.27,16.85],[3.72,16.18],[3.64,15.57],[2.75,15.41],[1.38,15.32],[1.02,14.97],[.38,14.93],[-.26,14.92],[-.52,15.12],[-1.07,14.97],[-2,14.56],[-2.19,14.25],[-2.97,13.8],[-3.11,13.54],[-3.52,13.34],[-4.01,13.47],[-4.28,13.23],[-4.43,12.54],[-5.22,11.71],[-5.2,11.37],[-5.47,10.95],[-5.41,10.37],[-5.82,10.22],[-6.05,10.1],[-6.2,10.52],[-6.49,10.41],[-6.67,10.43],[-6.85,10.14],[-7.62,10.15],[-7.9,10.3],[-8.03,10.21],[-8.34,10.49],[-8.28,10.79],[-8.41,10.91],[-8.62,10.81],[-8.58,11.14],[-8.38,11.39],[-8.79,11.81],[-8.9,12.09],[-9.13,12.31],[-9.33,12.33],[-9.57,12.19],[-9.89,12.06],[-10.16,11.84],[-10.59,11.92],[-10.87,12.18],[-11.04,12.21],[-11.3,12.08],[-11.46,12.08],[-11.51,12.44]],[[-17.06,21],[-16.85,21.33],[-12.93,21.33],[-13.12,22.77],[-12.88,23.29],[-11.94,23.37],[-11.97,25.93],[-8.69,25.88],[-8.69,27.4],[-4.92,24.97],[-6.45,24.96],[-5.97,20.64],[-5.49,16.33],[-5.32,16.2],[-5.54,15.5],[-9.55,15.49],[-9.7,15.26],[-10.09,15.33],[-10.65,15.13],[-11.35,15.41],[-11.67,15.39],[-11.84,14.8],[-12.17,14.62],[-12.83,15.3],[-13.44,16.04],[-14.1,16.3],[-14.58,16.6],[-15.14,16.59],[-15.62,16.37],[-16.12,16.46],[-16.46,16.14],[-16.55,16.67],[-16.27,17.17],[-16.15,18.11],[-16.26,19.1],[-16.38,19.59],[-16.28,20.09],[-16.54,20.57],[-17.06,21]],[[2.69,6.26],[1.87,6.14],[1.62,6.83],[1.67,9.13],[1.46,9.34],[1.42,9.83],[1.08,10.18],[.77,10.47],[.9,11],[1.24,11.11],[1.45,11.55],[1.94,11.64],[2.15,11.94],[2.49,12.23],[2.85,12.24],[3.61,11.66],[3.57,11.33],[3.8,10.73],[3.6,10.33],[3.71,10.06],[3.22,9.44],[2.91,9.14],[2.72,8.51],[2.75,7.87],[2.69,6.26]],[[14.85,22.86],[15.1,21.31],[15.47,21.05],[15.49,20.73],[15.9,20.39],[15.69,19.96],[15.3,17.93],[15.25,16.63],[13.97,15.68],[13.54,14.37],[13.96,14],[13.96,13.35],[14.6,13.33],[14.5,12.86],[14.21,12.8],[14.18,12.48],[14,12.46],[13.32,13.56],[13.08,13.6],[12.3,13.04],[11.53,13.33],[10.99,13.39],[10.7,13.25],[10.11,13.28],[9.52,12.85],[9.02,12.83],[7.8,13.34],[7.33,13.1],[6.82,13.11],[6.45,13.49],[5.44,13.87],[4.37,13.75],[4.11,13.53],[3.97,12.96],[3.68,12.55],[3.61,11.66],[2.85,12.24],[2.49,12.23],[2.15,11.94],[2.18,12.63],[1.02,12.85],[.99,13.34],[.43,13.99],[.3,14.44],[.38,14.93],[1.02,14.97],[1.38,15.32],[2.75,15.41],[3.64,15.57],[3.72,16.18],[4.27,16.85],[4.27,19.16],[5.68,19.6],[8.57,21.57],[12,23.47],[13.58,23.04],[14.14,22.49],[14.85,22.86]],[[2.69,6.26],[2.75,7.87],[2.72,8.51],[2.91,9.14],[3.22,9.44],[3.71,10.06],[3.6,10.33],[3.8,10.73],[3.57,11.33],[3.61,11.66],[3.68,12.55],[3.97,12.96],[4.11,13.53],[4.37,13.75],[5.44,13.87],[6.45,13.49],[6.82,13.11],[7.33,13.1],[7.8,13.34],[9.02,12.83],[9.52,12.85],[10.11,13.28],[10.7,13.25],[10.99,13.39],[11.53,13.33],[12.3,13.04],[13.08,13.6],[13.32,13.56],[14,12.46],[14.18,12.48],[14.58,12.09],[14.47,11.9],[14.42,11.57],[13.57,10.8],[13.31,10.16],[13.17,9.64],[12.95,9.42],[12.75,8.72],[12.22,8.31],[12.07,7.8],[11.84,7.4],[11.75,6.98],[11.06,6.64],[10.5,7.06],[10.12,7.04],[9.52,6.45],[9.23,6.44],[8.76,5.48],[8.5,4.77],[7.46,4.41],[7.08,4.46],[6.7,4.24],[5.9,4.26],[5.36,4.89],[5.03,5.61],[4.33,6.27],[3.57,6.26],[2.69,6.26]],[[14.5,12.86],[14.9,12.22],[14.96,11.56],[14.92,10.89],[15.47,9.98],[14.91,9.99],[14.63,9.92],[14.17,10.02],[13.96,9.55],[14.55,8.97],[14.98,8.8],[15.12,8.38],[15.44,7.69],[15.28,7.42],[14.78,6.41],[14.54,6.23],[14.46,5.45],[14.56,5.03],[14.48,4.73],[14.95,4.21],[15.04,3.85],[15.41,3.33],[15.86,3.01],[15.91,2.56],[16.01,2.27],[15.94,1.73],[15.15,1.96],[14.34,2.23],[13.08,2.27],[12.95,2.32],[12.36,2.19],[11.75,2.33],[11.28,2.26],[9.65,2.28],[9.79,3.07],[9.41,3.73],[8.95,3.9],[8.75,4.35],[8.49,4.5],[8.5,4.77],[8.76,5.48],[9.23,6.44],[9.52,6.45],[10.12,7.04],[10.5,7.06],[11.06,6.64],[11.75,6.98],[11.84,7.4],[12.07,7.8],[12.22,8.31],[12.75,8.72],[12.95,9.42],[13.17,9.64],[13.31,10.16],[13.57,10.8],[14.42,11.57],[14.47,11.9],[14.58,12.09],[14.18,12.48],[14.21,12.8],[14.5,12.86]],[[.9,11],[.77,10.47],[1.08,10.18],[1.42,9.83],[1.46,9.34],[1.67,9.13],[1.62,6.83],[1.87,6.14],[1.06,5.93],[.84,6.28],[.57,6.91],[.49,7.41],[.71,8.31],[.46,8.68],[.37,9.47],[.37,10.19],[-.05,10.71],[.02,11.02],[.9,11]],[[.02,11.02],[-.05,10.71],[.37,10.19],[.37,9.47],[.46,8.68],[.71,8.31],[.49,7.41],[.57,6.91],[.84,6.28],[1.06,5.93],[-.51,5.34],[-1.06,5],[-1.96,4.71],[-2.86,5],[-2.81,5.39],[-3.25,6.25],[-2.98,7.38],[-2.56,8.22],[-2.83,9.64],[-2.96,10.39],[-2.94,10.96],[-1.2,11.01],[-.76,10.94],[-.44,11.1],[.02,11.02]],[[-8.03,10.21],[-7.9,10.3],[-7.62,10.15],[-6.85,10.14],[-6.67,10.43],[-6.49,10.41],[-6.2,10.52],[-6.05,10.1],[-5.82,10.22],[-5.41,10.37],[-4.96,10.15],[-4.78,9.82],[-4.33,9.61],[-3.98,9.86],[-3.51,9.9],[-2.83,9.64],[-2.56,8.22],[-2.98,7.38],[-3.25,6.25],[-2.81,5.39],[-2.86,5],[-3.31,4.98],[-4.01,5.18],[-4.65,5.17],[-5.83,4.99],[-6.53,4.71],[-7.52,4.34],[-7.71,4.36],[-7.63,5.19],[-7.54,5.31],[-7.57,5.71],[-7.99,6.13],[-8.31,6.19],[-8.6,6.47],[-8.39,6.91],[-8.49,7.4],[-8.44,7.69],[-8.28,7.69],[-8.22,8.12],[-8.3,8.32],[-8.2,8.45],[-7.83,8.58],[-8.08,9.38],[-8.31,9.79],[-8.23,10.13],[-8.03,10.21]],[[-13.7,12.59],[-13.22,12.58],[-12.5,12.33],[-12.28,12.35],[-12.2,12.47],[-11.66,12.39],[-11.51,12.44],[-11.46,12.08],[-11.3,12.08],[-11.04,12.21],[-10.87,12.18],[-10.59,11.92],[-10.16,11.84],[-9.89,12.06],[-9.57,12.19],[-9.33,12.33],[-9.13,12.31],[-8.9,12.09],[-8.79,11.81],[-8.38,11.39],[-8.58,11.14],[-8.62,10.81],[-8.41,10.91],[-8.28,10.79],[-8.34,10.49],[-8.03,10.21],[-8.23,10.13],[-8.31,9.79],[-8.08,9.38],[-7.83,8.58],[-8.2,8.45],[-8.3,8.32],[-8.22,8.12],[-8.28,7.69],[-8.44,7.69],[-8.72,7.71],[-8.93,7.31],[-9.21,7.31],[-9.41,7.53],[-9.34,7.93],[-9.75,8.54],[-10.02,8.43],[-10.23,8.41],[-10.51,8.35],[-10.5,8.72],[-10.65,8.98],[-10.62,9.27],[-10.84,9.69],[-11.12,10.05],[-11.92,10.05],[-12.15,9.86],[-12.43,9.84],[-12.6,9.62],[-12.71,9.34],[-13.25,8.9],[-13.69,9.49],[-14.07,9.89],[-14.33,10.02],[-14.58,10.22],[-14.69,10.66],[-14.84,10.88],[-15.13,11.04],[-14.69,11.53],[-14.38,11.51],[-14.12,11.68],[-13.9,11.68],[-13.74,11.81],[-13.83,12.14],[-13.72,12.25],[-13.7,12.59]],[[-16.68,12.39],[-16.15,12.55],[-15.82,12.52],[-15.55,12.63],[-13.7,12.59],[-13.72,12.25],[-13.83,12.14],[-13.74,11.81],[-13.9,11.68],[-14.12,11.68],[-14.38,11.51],[-14.69,11.53],[-15.13,11.04],[-15.67,11.46],[-16.09,11.53],[-16.31,11.81],[-16.31,11.96],[-16.61,12.17],[-16.68,12.39]],[[-8.44,7.69],[-8.49,7.4],[-8.39,6.91],[-8.6,6.47],[-8.31,6.19],[-7.99,6.13],[-7.57,5.71],[-7.54,5.31],[-7.63,5.19],[-7.71,4.36],[-7.98,4.36],[-9.01,4.83],[-9.91,5.59],[-10.77,6.14],[-11.44,6.79],[-11.2,7.11],[-11.15,7.4],[-10.69,7.94],[-10.23,8.41],[-10.02,8.43],[-9.75,8.54],[-9.34,7.93],[-9.41,7.53],[-9.21,7.31],[-8.93,7.31],[-8.72,7.71],[-8.44,7.69]],[[-13.25,8.9],[-12.71,9.34],[-12.6,9.62],[-12.43,9.84],[-12.15,9.86],[-11.92,10.05],[-11.12,10.05],[-10.84,9.69],[-10.62,9.27],[-10.65,8.98],[-10.5,8.72],[-10.51,8.35],[-10.23,8.41],[-10.69,7.94],[-11.15,7.4],[-11.2,7.11],[-11.44,6.79],[-11.71,6.86],[-12.43,7.26],[-12.95,7.8],[-13.12,8.16],[-13.25,8.9]],[[-5.41,10.37],[-5.47,10.95],[-5.2,11.37],[-5.22,11.71],[-4.43,12.54],[-4.28,13.23],[-4.01,13.47],[-3.52,13.34],[-3.11,13.54],[-2.97,13.8],[-2.19,14.25],[-2,14.56],[-1.07,14.97],[-.52,15.12],[-.26,14.92],[.38,14.93],[.3,14.44],[.43,13.99],[.99,13.34],[1.02,12.85],[2.18,12.63],[2.15,11.94],[1.94,11.64],[1.45,11.55],[1.24,11.11],[.9,11],[.02,11.02],[-.44,11.1],[-.76,10.94],[-1.2,11.01],[-2.94,10.96],[-2.96,10.39],[-2.83,9.64],[-3.51,9.9],[-3.98,9.86],[-4.33,9.61],[-4.78,9.82],[-4.96,10.15],[-5.41,10.37]],[[27.37,5.23],[27.05,5.13],[26.4,5.15],[25.65,5.26],[25.28,5.17],[25.13,4.93],[24.81,4.9],[24.41,5.11],[23.3,4.61],[22.84,4.71],[22.7,4.63],[22.4,4.03],[21.66,4.22],[20.93,4.32],[20.29,4.69],[19.47,5.03],[18.93,4.71],[18.54,4.2],[18.45,3.5],[17.81,3.56],[17.13,3.73],[16.54,3.2],[16.01,2.27],[15.91,2.56],[15.86,3.01],[15.41,3.33],[15.04,3.85],[14.95,4.21],[14.48,4.73],[14.56,5.03],[14.46,5.45],[14.54,6.23],[14.78,6.41],[15.28,7.42],[16.1,7.5],[16.29,7.75],[16.46,7.74],[16.71,7.51],[17.97,7.89],[18.39,8.28],[18.91,8.63],[18.81,8.98],[19.09,9.07],[20.06,9.01],[21,9.48],[21.72,10.57],[22.23,10.97],[22.87,11.14],[22.98,10.71],[23.55,10.09],[23.56,9.68],[23.39,9.27],[23.46,8.95],[23.81,8.67],[24.57,8.23],[25.12,7.83],[25.12,7.5],[25.8,6.98],[26.21,6.55],[26.47,5.95],[27.21,5.55],[27.37,5.23]],[[18.45,3.5],[18.39,2.9],[18.1,2.37],[17.9,1.74],[17.78,.86],[17.83,.29],[17.66,-.06],[17.64,-.42],[17.52,-.74],[16.86,-1.23],[16.41,-1.74],[15.97,-2.71],[16.01,-3.54],[15.75,-3.86],[15.17,-4.34],[14.58,-4.97],[14.21,-4.79],[14.15,-4.51],[13.6,-4.5],[13.26,-4.88],[12.99,-4.78],[12.62,-4.44],[12.32,-4.61],[11.91,-5.04],[11.09,-3.98],[11.86,-3.43],[11.48,-2.77],[11.82,-2.51],[12.49,-2.39],[12.58,-1.95],[13.11,-2.43],[13.99,-2.47],[14.3,-2],[14.43,-1.33],[14.32,-.55],[13.84,.04],[14.28,1.2],[14.03,1.4],[13.28,1.31],[13,1.83],[13.08,2.27],[14.34,2.23],[15.15,1.96],[15.94,1.73],[16.01,2.27],[16.54,3.2],[17.13,3.73],[17.81,3.56],[18.45,3.5]],[[11.28,2.26],[11.75,2.33],[12.36,2.19],[12.95,2.32],[13.08,2.27],[13,1.83],[13.28,1.31],[14.03,1.4],[14.28,1.2],[13.84,.04],[14.32,-.55],[14.43,-1.33],[14.3,-2],[13.99,-2.47],[13.11,-2.43],[12.58,-1.95],[12.49,-2.39],[11.82,-2.51],[11.48,-2.77],[11.86,-3.43],[11.09,-3.98],[10.07,-2.97],[9.41,-2.14],[8.8,-1.11],[8.83,-.78],[9.05,-.46],[9.29,.27],[9.49,1.01],[9.83,1.07],[11.28,1.06],[11.28,2.26]],[[9.65,2.28],[11.28,2.26],[11.28,1.06],[9.83,1.07],[9.49,1.01],[9.3,1.16],[9.65,2.28]],[[30.74,-8.34],[31.16,-8.59],[31.56,-8.76],[32.19,-8.93],[32.76,-9.23],[33.23,-9.68],[33.49,-10.53],[33.32,-10.8],[33.11,-11.61],[33.31,-12.44],[32.99,-12.78],[32.69,-13.71],[33.22,-13.97],[30.18,-14.8],[30.27,-15.51],[29.52,-15.65],[28.95,-16.04],[28.83,-16.39],[28.47,-16.47],[27.6,-17.29],[27.05,-17.94],[26.71,-17.96],[26.38,-17.85],[25.26,-17.74],[25.08,-17.66],[25.08,-17.58],[24.68,-17.35],[24.04,-17.3],[23.21,-17.52],[22.56,-16.9],[21.89,-16.08],[21.93,-12.9],[24.02,-12.91],[23.93,-12.57],[24.08,-12.19],[23.9,-11.72],[24.02,-11.24],[23.91,-10.93],[24.26,-10.95],[24.31,-11.26],[24.78,-11.24],[25.42,-11.33],[25.75,-11.78],[26.55,-11.93],[27.16,-11.61],[27.39,-12.13],[28.15,-12.27],[28.52,-12.7],[28.94,-13.25],[29.7,-13.26],[29.62,-12.18],[29.34,-12.36],[28.64,-11.97],[28.37,-11.79],[28.5,-10.79],[28.67,-9.61],[28.45,-9.16],[28.73,-8.53],[29,-8.41],[30.35,-8.24],[30.74,-8.34]],[[32.76,-9.23],[33.74,-9.42],[33.94,-9.69],[34.28,-10.16],[34.56,-11.52],[34.28,-12.28],[34.56,-13.58],[34.91,-13.57],[35.27,-13.89],[35.69,-14.61],[35.77,-15.9],[35.34,-16.11],[35.03,-16.8],[34.38,-16.18],[34.31,-15.48],[34.52,-15.01],[34.46,-14.61],[34.07,-14.36],[33.79,-14.45],[33.22,-13.97],[32.69,-13.71],[32.99,-12.78],[33.31,-12.44],[33.11,-11.61],[33.32,-10.8],[33.49,-10.53],[33.23,-9.68],[32.76,-9.23]],[[34.56,-11.52],[35.31,-11.44],[36.51,-11.72],[36.78,-11.6],[37.47,-11.57],[37.83,-11.27],[38.43,-11.29],[39.52,-10.9],[40.32,-10.32],[40.48,-10.77],[40.44,-11.76],[40.56,-12.64],[40.6,-14.2],[40.78,-14.69],[40.48,-15.41],[40.09,-16.1],[39.45,-16.72],[38.54,-17.1],[37.41,-17.59],[36.28,-18.66],[35.9,-18.84],[35.2,-19.55],[34.79,-19.78],[34.7,-20.5],[35.18,-21.25],[35.37,-21.84],[35.39,-22.14],[35.56,-22.09],[35.53,-23.07],[35.37,-23.54],[35.61,-23.71],[35.46,-24.12],[35.04,-24.48],[34.22,-24.82],[33.01,-25.36],[32.57,-25.73],[32.66,-26.15],[32.92,-26.22],[32.83,-26.74],[32.07,-26.73],[31.98,-26.29],[31.84,-25.84],[31.75,-25.48],[31.93,-24.37],[31.67,-23.66],[31.19,-22.25],[32.24,-21.12],[32.51,-20.39],[32.66,-20.31],[32.77,-19.72],[32.61,-19.42],[32.65,-18.67],[32.85,-17.98],[32.85,-16.71],[32.33,-16.39],[31.85,-16.32],[31.64,-16.07],[31.17,-15.86],[30.34,-15.88],[30.27,-15.51],[30.18,-14.8],[33.22,-13.97],[33.79,-14.45],[34.07,-14.36],[34.46,-14.61],[34.52,-15.01],[34.31,-15.48],[34.38,-16.18],[35.03,-16.8],[35.34,-16.11],[35.77,-15.9],[35.69,-14.61],[35.27,-13.89],[34.91,-13.57],[34.56,-13.58],[34.28,-12.28],[34.56,-11.52]],[[32.07,-26.73],[31.87,-27.18],[31.28,-27.29],[30.68,-26.74],[30.68,-26.4],[30.95,-26.02],[31.04,-25.73],[31.33,-25.66],[31.84,-25.84],[31.98,-26.29],[32.07,-26.73]],[[12.99,-4.78],[12.63,-4.99],[12.47,-5.25],[12.44,-5.68],[12.18,-5.79],[11.91,-5.04],[12.32,-4.61],[12.62,-4.44],[12.99,-4.78]],[[12.32,-6.1],[12.74,-5.97],[13.02,-5.98],[13.38,-5.86],[16.33,-5.88],[16.57,-6.62],[16.86,-7.22],[17.09,-7.54],[17.47,-8.07],[18.14,-7.99],[18.46,-7.85],[19.02,-7.99],[19.17,-7.74],[19.42,-7.16],[20.04,-7.12],[20.09,-6.94],[20.6,-6.94],[20.51,-7.3],[21.73,-7.29],[21.75,-7.92],[21.95,-8.31],[21.8,-8.91],[21.88,-9.52],[22.21,-9.89],[22.16,-11.08],[22.4,-10.99],[22.84,-11.02],[23.46,-10.87],[23.91,-10.93],[24.02,-11.24],[23.9,-11.72],[24.08,-12.19],[23.93,-12.57],[24.02,-12.91],[21.93,-12.9],[21.89,-16.08],[22.56,-16.9],[23.21,-17.52],[21.38,-17.93],[18.96,-17.79],[18.26,-17.31],[14.21,-17.35],[14.06,-17.42],[13.46,-16.97],[12.81,-16.94],[12.22,-17.11],[11.73,-17.3],[11.64,-16.67],[11.78,-15.79],[12.12,-14.88],[12.18,-14.45],[12.5,-13.55],[12.74,-13.14],[13.31,-12.48],[13.64,-12.04],[13.74,-11.3],[13.69,-10.73],[13.39,-10.37],[13.12,-9.77],[12.88,-9.17],[12.93,-8.96],[13.24,-8.56],[12.93,-7.6],[12.73,-6.93],[12.23,-6.29],[12.32,-6.1]],[[30.47,-2.41],[30.53,-2.81],[30.74,-3.03],[30.75,-3.36],[30.5,-3.57],[30.12,-4.09],[29.75,-4.45],[29.34,-4.5],[29.28,-3.29],[29.03,-2.84],[29.63,-2.92],[29.94,-2.35],[30.47,-2.41]],[[35.72,32.71],[35.54,32.39],[35.18,32.53],[34.98,31.87],[35.22,31.75],[34.97,31.62],[34.93,31.35],[35.4,31.49],[35.42,31.1],[34.92,29.5],[34.82,29.76],[34.27,31.22],[34.55,31.55],[34.49,31.61],[34.75,32.07],[34.95,32.83],[35.1,33.08],[35.13,33.09],[35.46,33.09],[35.55,33.26],[35.82,33.28],[35.84,32.87],[35.7,32.72],[35.72,32.71]],[[35.82,33.28],[35.55,33.26],[35.46,33.09],[35.13,33.09],[35.48,33.91],[35.98,34.61],[36,34.65],[36.45,34.59],[36.61,34.2],[36.07,33.82],[35.82,33.28]],[[49.54,-12.47],[49.81,-12.9],[50.06,-13.56],[50.22,-14.76],[50.48,-15.23],[50.38,-15.71],[50.2,-16],[49.86,-15.41],[49.67,-15.71],[49.86,-16.45],[49.78,-16.87],[49.5,-17.11],[49.43,-17.95],[49.04,-19.12],[48.55,-20.5],[47.93,-22.39],[47.55,-23.78],[47.1,-24.94],[46.28,-25.18],[45.41,-25.6],[44.83,-25.35],[44.04,-24.99],[43.76,-24.46],[43.7,-23.57],[43.35,-22.78],[43.25,-22.06],[43.43,-21.34],[43.89,-21.16],[43.9,-20.83],[44.38,-20.07],[44.47,-19.44],[44.23,-18.96],[44.04,-18.33],[43.96,-17.41],[44.31,-16.85],[44.45,-16.22],[44.94,-16.18],[45.5,-15.97],[45.87,-15.79],[46.31,-15.78],[46.88,-15.21],[47.71,-14.59],[48,-14.09],[47.87,-13.66],[48.29,-13.78],[48.84,-13.09],[48.87,-12.49],[49.2,-12.04],[49.54,-12.47]],[[35.4,31.49],[34.93,31.35],[34.97,31.62],[35.22,31.75],[34.98,31.87],[35.18,32.53],[35.54,32.39],[35.54,31.78],[35.4,31.49]],[[-16.71,13.6],[-15.63,13.62],[-15.4,13.86],[-15.08,13.88],[-14.69,13.63],[-14.38,13.63],[-14.05,13.79],[-13.84,13.51],[-14.28,13.28],[-14.71,13.3],[-15.14,13.51],[-15.51,13.28],[-15.69,13.27],[-15.93,13.13],[-16.84,13.15],[-16.71,13.6]],[[9.48,30.31],[9.06,32.1],[8.44,32.51],[8.43,32.75],[7.61,33.34],[7.53,34.1],[8.14,34.66],[8.38,35.48],[8.22,36.43],[8.42,36.95],[9.51,37.35],[10.21,37.23],[10.18,36.72],[11.03,37.09],[11.1,36.9],[10.6,36.41],[10.59,35.95],[10.94,35.7],[10.81,34.83],[10.15,34.33],[10.34,33.79],[10.86,33.77],[11.11,33.29],[11.49,33.14],[11.43,32.37],[10.95,32.08],[10.64,31.76],[9.95,31.38],[10.06,30.96],[9.97,30.54],[9.48,30.31]],[[-8.69,27.4],[-8.66,27.59],[-8.67,27.66],[-8.67,28.84],[-7.06,29.58],[-6.06,29.73],[-5.24,30],[-4.86,30.5],[-3.69,30.9],[-3.65,31.64],[-3.07,31.72],[-2.62,32.09],[-1.31,32.26],[-1.13,32.65],[-1.39,32.86],[-1.73,33.92],[-1.79,34.53],[-2.17,35.17],[-1.21,35.72],[-.13,35.89],[.5,36.3],[1.47,36.61],[3.16,36.78],[4.82,36.86],[5.32,36.72],[6.26,37.11],[7.33,37.12],[7.74,36.89],[8.42,36.95],[8.22,36.43],[8.38,35.48],[8.14,34.66],[7.53,34.1],[7.61,33.34],[8.43,32.75],[8.44,32.51],[9.06,32.1],[9.48,30.31],[9.8,29.42],[9.86,28.96],[9.68,28.14],[9.76,27.69],[9.63,27.14],[9.71,26.51],[9.32,26.09],[9.91,25.37],[9.95,24.94],[10.31,24.38],[10.77,24.56],[11.56,24.1],[12,23.47],[8.57,21.57],[5.68,19.6],[4.27,19.16],[3.16,19.06],[3.15,19.69],[2.68,19.86],[2.06,20.14],[1.82,20.61],[-1.55,22.79],[-4.92,24.97],[-8.69,27.4]],[[35.54,32.39],[35.72,32.71],[36.83,32.31],[38.79,33.38],[39.2,32.16],[39,32.01],[37,31.51],[38,30.51],[37.67,30.34],[37.5,30],[36.74,29.87],[36.5,29.51],[36.07,29.2],[34.95,29.36],[34.92,29.5],[35.42,31.1],[35.4,31.49],[35.54,31.78],[35.54,32.39]],[[51.58,24.24],[51.76,24.29],[51.8,24.02],[52.58,24.18],[53.4,24.15],[54.01,24.12],[54.69,24.8],[55.44,25.44],[56.07,26.06],[56.26,25.71],[56.4,24.93],[55.89,24.92],[55.8,24.27],[55.98,24.13],[55.53,23.93],[55.53,23.53],[55.23,23.11],[55.21,22.71],[55.01,22.5],[52,23],[51.62,24.01],[51.58,24.24]],[[50.81,24.75],[50.74,25.48],[51.01,26.01],[51.29,26.12],[51.59,25.8],[51.61,25.22],[51.39,24.63],[51.11,24.56],[50.81,24.75]],[[47.98,29.98],[48.18,29.53],[48.09,29.31],[48.42,28.55],[47.71,28.53],[47.46,29],[46.57,29.1],[47.3,30.06],[47.98,29.98]],[[39.2,32.16],[38.79,33.38],[41.01,34.42],[41.38,35.63],[41.29,36.36],[41.84,36.61],[42.35,37.23],[42.78,37.39],[43.94,37.26],[44.29,37],[44.77,37.17],[45.42,35.98],[46.08,35.68],[46.15,35.09],[45.65,34.75],[45.42,33.97],[46.11,33.02],[47.34,32.47],[47.85,31.71],[47.68,30.98],[48,30.98],[48.02,30.45],[48.57,29.93],[47.98,29.98],[47.3,30.06],[46.57,29.1],[44.71,29.18],[41.89,31.19],[40.4,31.89],[39.2,32.16]],[[55.21,22.71],[55.23,23.11],[55.53,23.53],[55.53,23.93],[55.98,24.13],[55.8,24.27],[55.89,24.92],[56.4,24.93],[56.85,24.24],[57.4,23.88],[58.14,23.75],[58.73,23.57],[59.18,22.99],[59.45,22.66],[59.81,22.53],[59.81,22.31],[59.44,21.71],[59.28,21.43],[58.86,21.11],[58.49,20.43],[58.03,20.48],[57.83,20.24],[57.67,19.74],[57.79,19.07],[57.7,18.95],[57.24,18.95],[56.61,18.57],[56.51,18.09],[56.28,17.88],[55.66,17.88],[55.27,17.63],[55.27,17.23],[54.79,16.95],[54.24,17.04],[53.57,16.71],[53.11,16.65],[52.78,17.35],[52,19],[55,20],[55.67,22],[55.21,22.71]],[[56.26,25.71],[56.07,26.06],[56.36,26.4],[56.49,26.31],[56.39,25.9],[56.26,25.71]],[[167.22,-15.89],[167.85,-16.47],[167.52,-16.6],[167.18,-16.16],[167.22,-15.89]],[[166.79,-15.67],[166.65,-15.39],[166.63,-14.63],[167.11,-14.93],[167.27,-15.74],[167,-15.61],[166.79,-15.67]],[[102.58,12.19],[102.35,13.39],[102.99,14.23],[104.28,14.42],[105.22,14.27],[106.04,13.88],[106.5,14.57],[107.38,14.2],[107.61,13.54],[107.49,12.34],[105.81,11.57],[106.25,10.96],[105.2,10.89],[104.33,10.49],[103.5,10.63],[103.09,11.15],[102.58,12.19]],[[105.22,14.27],[104.28,14.42],[102.99,14.23],[102.35,13.39],[102.58,12.19],[101.69,12.65],[100.83,12.63],[100.98,13.41],[100.1,13.41],[100.02,12.31],[99.48,10.85],[99.15,9.96],[99.22,9.24],[99.87,9.21],[100.28,8.3],[100.46,7.43],[101.02,6.86],[101.62,6.74],[102.14,6.22],[101.81,5.81],[101.16,5.69],[101.08,6.21],[100.26,6.64],[100.09,6.46],[99.69,6.85],[99.52,7.34],[98.99,7.91],[98.5,8.38],[98.34,7.79],[98.15,8.35],[98.26,8.97],[98.55,9.93],[99.04,10.96],[99.59,11.89],[99.2,12.8],[99.21,13.27],[99.1,13.83],[98.43,14.62],[98.19,15.12],[98.54,15.31],[98.9,16.18],[98.5,16.84],[97.86,17.57],[97.38,18.45],[97.8,18.63],[98.25,19.71],[98.96,19.75],[99.54,20.19],[100.12,20.42],[100.55,20.11],[100.6,19.51],[101.28,19.46],[101.04,18.41],[101.06,17.51],[102.11,18.11],[102.41,17.93],[103,17.96],[103.2,18.31],[103.96,18.24],[104.72,17.43],[104.78,16.44],[105.59,15.57],[105.54,14.72],[105.22,14.27]],[[107.38,14.2],[106.5,14.57],[106.04,13.88],[105.22,14.27],[105.54,14.72],[105.59,15.57],[104.78,16.44],[104.72,17.43],[103.96,18.24],[103.2,18.31],[103,17.96],[102.41,17.93],[102.11,18.11],[101.06,17.51],[101.04,18.41],[101.28,19.46],[100.6,19.51],[100.55,20.11],[100.12,20.42],[100.33,20.79],[101.18,21.44],[101.27,21.2],[101.8,21.17],[101.65,22.32],[102.17,22.46],[102.75,21.68],[103.2,20.77],[104.44,20.76],[104.82,19.89],[104.18,19.62],[103.9,19.27],[105.09,18.67],[105.93,17.48],[106.56,16.6],[107.31,15.91],[107.56,15.2],[107.38,14.2]],[[100.12,20.42],[99.54,20.19],[98.96,19.75],[98.25,19.71],[97.8,18.63],[97.38,18.45],[97.86,17.57],[98.5,16.84],[98.9,16.18],[98.54,15.31],[98.19,15.12],[98.43,14.62],[99.1,13.83],[99.21,13.27],[99.2,12.8],[99.59,11.89],[99.04,10.96],[98.55,9.93],[98.46,10.68],[98.77,11.44],[98.43,12.03],[98.51,13.12],[98.1,13.64],[97.78,14.84],[97.6,16.1],[97.16,16.93],[96.5,16.43],[95.37,15.71],[94.81,15.8],[94.19,16.04],[94.54,17.28],[94.33,18.21],[93.54,19.37],[93.66,19.73],[93.08,19.86],[92.37,20.67],[92.3,21.48],[92.65,21.32],[92.67,22.04],[93.17,22.28],[93.06,22.7],[93.29,23.04],[93.33,24.08],[94.11,23.85],[94.55,24.67],[94.6,25.16],[95.15,26],[95.13,26.57],[96.42,27.26],[97.13,27.08],[97.05,27.7],[97.4,27.88],[97.33,28.26],[97.91,28.34],[98.25,27.75],[98.68,27.51],[98.71,26.74],[98.67,25.92],[97.72,25.08],[97.61,23.9],[98.66,24.06],[98.9,23.14],[99.53,22.95],[99.24,22.12],[99.98,21.74],[100.42,21.56],[101.15,21.85],[101.18,21.44],[100.33,20.79],[100.12,20.42]],[[104.33,10.49],[105.2,10.89],[106.25,10.96],[105.81,11.57],[107.49,12.34],[107.61,13.54],[107.38,14.2],[107.56,15.2],[107.31,15.91],[106.56,16.6],[105.93,17.48],[105.09,18.67],[103.9,19.27],[104.18,19.62],[104.82,19.89],[104.44,20.76],[103.2,20.77],[102.75,21.68],[102.17,22.46],[102.71,22.71],[103.5,22.7],[104.48,22.82],[105.33,23.35],[105.81,22.98],[106.72,22.79],[106.57,22.22],[107.04,21.81],[108.05,21.55],[106.71,20.7],[105.88,19.75],[105.66,19.06],[106.43,18],[107.36,16.7],[108.27,16.08],[108.88,15.28],[109.33,13.43],[109.2,11.67],[108.37,11.01],[107.22,10.36],[106.4,9.53],[105.16,8.6],[104.8,9.24],[105.08,9.92],[104.33,10.49]],[[130.78,42.22],[130.78,42.22],[130.78,42.22],[130.78,42.22]],[[130.64,42.4],[130.78,42.22],[130.4,42.28],[129.97,41.94],[129.67,41.6],[129.7,40.88],[129.19,40.66],[129.01,40.48],[128.63,40.19],[127.97,40.03],[127.53,39.76],[127.5,39.32],[127.39,39.21],[127.79,39.05],[128.35,38.61],[128.21,38.37],[127.78,38.3],[127.07,38.26],[126.68,37.81],[126.24,37.84],[126.18,37.75],[125.69,37.94],[125.57,37.75],[125.28,37.67],[125.24,37.86],[124.98,37.95],[124.71,38.11],[124.98,38.55],[125.22,38.67],[125.13,38.85],[125.39,39.39],[125.32,39.55],[124.74,39.66],[124.26,39.93],[125.08,40.57],[126.18,41.11],[126.87,41.82],[127.34,41.5],[128.21,41.47],[128.05,41.99],[129.6,42.42],[130,42.98],[130.64,42.4]],[[126.18,37.75],[126.24,37.84],[126.68,37.81],[127.07,38.26],[127.78,38.3],[128.21,38.37],[128.35,38.61],[129.21,37.43],[129.46,36.78],[129.47,35.63],[129.09,35.08],[128.18,34.89],[127.39,34.48],[126.49,34.39],[126.37,34.93],[126.56,35.68],[126.12,36.73],[126.86,36.89],[126.18,37.75]],[[87.75,49.3],[88.8,49.47],[90.71,50.33],[92.23,50.8],[93.11,50.49],[94.15,50.48],[94.82,50.01],[95.81,49.98],[97.26,49.73],[98.23,50.42],[97.83,51.01],[98.86,52.05],[99.98,51.63],[100.89,51.52],[102.07,51.26],[102.26,50.51],[103.68,50.09],[104.62,50.27],[105.89,50.41],[106.89,50.27],[107.87,49.79],[108.47,49.28],[109.4,49.29],[110.66,49.13],[111.58,49.38],[112.9,49.54],[114.36,50.25],[114.96,50.14],[115.49,49.81],[116.68,49.89],[116.19,49.13],[115.48,48.14],[115.74,47.73],[116.31,47.85],[117.29,47.7],[118.06,48.07],[118.87,47.75],[119.77,47.05],[119.66,46.69],[118.87,46.8],[117.42,46.67],[116.72,46.39],[115.98,45.73],[114.46,45.34],[113.46,44.81],[112.43,45.01],[111.87,45.1],[111.35,44.46],[111.67,44.07],[111.83,43.74],[111.13,43.41],[110.41,42.87],[109.24,42.52],[107.74,42.48],[106.13,42.14],[104.96,41.6],[104.52,41.91],[103.31,41.91],[101.83,42.51],[100.85,42.66],[99.52,42.52],[97.45,42.75],[96.35,42.73],[95.76,43.32],[95.31,44.24],[94.69,44.35],[93.48,44.98],[92.13,45.12],[90.95,45.29],[90.59,45.72],[90.97,46.89],[90.28,47.69],[88.85,48.07],[88.02,48.6],[87.75,49.3]],[[97.33,28.26],[97.4,27.88],[97.05,27.7],[97.13,27.08],[96.42,27.26],[95.13,26.57],[95.15,26],[94.6,25.16],[94.55,24.67],[94.11,23.85],[93.33,24.08],[93.29,23.04],[93.06,22.7],[93.17,22.28],[92.67,22.04],[92.14,23.63],[91.87,23.62],[91.71,22.99],[91.16,23.5],[91.47,24.07],[91.91,24.13],[92.38,24.98],[91.8,25.15],[90.87,25.13],[89.92,25.27],[89.83,25.96],[89.35,26.02],[88.56,26.45],[88.21,25.77],[88.93,25.24],[88.31,24.87],[88.08,24.5],[88.7,24.23],[88.53,23.63],[88.88,22.88],[89.03,22.06],[88.89,21.69],[88.21,21.7],[86.98,21.5],[87.03,20.74],[86.5,20.15],[85.06,19.48],[83.94,18.3],[83.19,17.67],[82.19,17.02],[82.19,16.56],[81.69,16.31],[80.79,15.95],[80.33,15.9],[80.02,15.14],[80.23,13.84],[80.29,13.01],[79.86,12.06],[79.86,10.36],[79.34,10.31],[78.89,9.55],[79.19,9.22],[78.28,8.93],[77.94,8.25],[77.54,7.97],[76.59,8.9],[76.13,10.3],[75.75,11.31],[75.4,11.78],[74.86,12.74],[74.62,13.99],[74.44,14.62],[73.53,15.99],[73.12,17.93],[72.82,19.21],[72.82,20.42],[72.63,21.36],[71.17,20.76],[70.47,20.88],[69.17,22.09],[69.64,22.45],[69.35,22.84],[68.18,23.69],[68.84,24.36],[71.04,24.36],[70.84,25.21],[70.28,25.72],[70.17,26.49],[69.51,26.94],[70.62,27.99],[71.78,27.91],[72.82,28.96],[73.45,29.98],[74.42,30.98],[74.41,31.69],[75.26,32.27],[74.45,32.77],[74.1,33.44],[73.75,34.32],[74.24,34.75],[75.76,34.51],[76.87,34.65],[77.84,35.49],[78.91,34.32],[78.81,33.51],[79.21,32.99],[79.18,32.48],[78.46,32.62],[78.74,31.52],[79.72,30.88],[81.11,30.18],[80.48,29.73],[80.09,28.79],[81.06,28.42],[82,27.93],[83.3,27.36],[84.67,27.24],[85.25,26.73],[86.02,26.63],[87.23,26.4],[88.06,26.41],[88.17,26.81],[88.04,27.45],[88.12,27.88],[88.73,28.09],[88.81,27.3],[88.84,27.1],[89.74,26.72],[90.37,26.88],[91.22,26.81],[92.03,26.84],[92.11,27.45],[91.7,27.77],[92.5,27.9],[93.41,28.64],[94.57,29.28],[95.41,29.03],[96.12,29.45],[96.59,28.83],[96.25,28.41],[97.33,28.26]],[[92.67,22.04],[92.65,21.32],[92.3,21.48],[92.37,20.67],[92.08,21.19],[92.03,21.7],[91.84,22.18],[91.42,22.77],[90.5,22.8],[90.59,22.39],[90.27,21.84],[89.85,22.04],[89.7,21.86],[89.42,21.97],[89.03,22.06],[88.88,22.88],[88.53,23.63],[88.7,24.23],[88.08,24.5],[88.31,24.87],[88.93,25.24],[88.21,25.77],[88.56,26.45],[89.35,26.02],[89.83,25.96],[89.92,25.27],[90.87,25.13],[91.8,25.15],[92.38,24.98],[91.91,24.13],[91.47,24.07],[91.16,23.5],[91.71,22.99],[91.87,23.62],[92.14,23.63],[92.67,22.04]],[[91.7,27.77],[92.11,27.45],[92.03,26.84],[91.22,26.81],[90.37,26.88],[89.74,26.72],[88.84,27.1],[88.81,27.3],[89.48,28.04],[90.02,28.3],[90.73,28.06],[91.26,28.04],[91.7,27.77]],[[88.12,27.88],[88.04,27.45],[88.17,26.81],[88.06,26.41],[87.23,26.4],[86.02,26.63],[85.25,26.73],[84.67,27.24],[83.3,27.36],[82,27.93],[81.06,28.42],[80.09,28.79],[80.48,29.73],[81.11,30.18],[81.52,30.42],[82.33,30.11],[83.34,29.46],[83.9,29.32],[84.24,28.84],[85.01,28.64],[85.82,28.2],[86.95,27.97],[88.12,27.88]],[[77.84,35.49],[76.87,34.65],[75.76,34.51],[74.24,34.75],[73.75,34.32],[74.1,33.44],[74.45,32.77],[75.26,32.27],[74.41,31.69],[74.42,30.98],[73.45,29.98],[72.82,28.96],[71.78,27.91],[70.62,27.99],[69.51,26.94],[70.17,26.49],[70.28,25.72],[70.84,25.21],[71.04,24.36],[68.84,24.36],[68.18,23.69],[67.44,23.95],[67.15,24.66],[66.37,25.42],[64.53,25.24],[62.91,25.22],[61.5,25.08],[61.88,26.24],[63.32,26.76],[63.23,27.22],[62.75,27.38],[62.73,28.26],[61.77,28.7],[61.37,29.3],[60.87,29.83],[62.55,29.32],[63.55,29.47],[64.15,29.34],[64.35,29.56],[65.05,29.47],[66.35,29.89],[66.38,30.74],[66.94,31.3],[67.68,31.3],[67.79,31.58],[68.56,31.71],[68.93,31.62],[69.32,31.9],[69.26,32.5],[69.69,33.11],[70.32,33.36],[69.93,34.02],[70.88,33.99],[71.16,34.35],[71.11,34.73],[71.61,35.15],[71.5,35.65],[71.26,36.07],[71.85,36.51],[72.92,36.72],[74.07,36.84],[74.58,37.02],[75.16,37.13],[75.9,36.67],[76.19,35.9],[77.84,35.49]],[[66.52,37.36],[67.07,37.36],[67.83,37.15],[68.14,37.02],[68.86,37.34],[69.19,37.15],[69.52,37.61],[70.12,37.59],[70.27,37.73],[70.38,38.14],[70.81,38.49],[71.35,38.26],[71.24,37.95],[71.54,37.91],[71.45,37.07],[71.84,36.74],[72.19,36.95],[72.64,37.05],[73.26,37.5],[73.95,37.42],[74.98,37.42],[75.16,37.13],[74.58,37.02],[74.07,36.84],[72.92,36.72],[71.85,36.51],[71.26,36.07],[71.5,35.65],[71.61,35.15],[71.11,34.73],[71.16,34.35],[70.88,33.99],[69.93,34.02],[70.32,33.36],[69.69,33.11],[69.26,32.5],[69.32,31.9],[68.93,31.62],[68.56,31.71],[67.79,31.58],[67.68,31.3],[66.94,31.3],[66.38,30.74],[66.35,29.89],[65.05,29.47],[64.35,29.56],[64.15,29.34],[63.55,29.47],[62.55,29.32],[60.87,29.83],[61.78,30.74],[61.7,31.38],[60.94,31.55],[60.86,32.18],[60.54,32.98],[60.96,33.53],[60.53,33.68],[60.8,34.4],[61.21,35.65],[62.23,35.27],[62.98,35.4],[63.19,35.86],[63.98,36.01],[64.55,36.31],[64.74,37.11],[65.59,37.3],[65.75,37.66],[66.22,37.39],[66.52,37.36]],[[67.83,37.15],[68.39,38.16],[68.18,38.9],[67.44,39.14],[67.7,39.58],[68.54,39.53],[69.01,40.09],[69.33,40.73],[70.67,40.96],[70.46,40.5],[70.6,40.22],[71.01,40.24],[70.65,39.94],[69.56,40.1],[69.46,39.53],[70.55,39.6],[71.78,39.28],[73.68,39.43],[73.93,38.51],[74.26,38.61],[74.86,38.38],[74.83,37.99],[74.98,37.42],[73.95,37.42],[73.26,37.5],[72.64,37.05],[72.19,36.95],[71.84,36.74],[71.45,37.07],[71.54,37.91],[71.24,37.95],[71.35,38.26],[70.81,38.49],[70.38,38.14],[70.27,37.73],[70.12,37.59],[69.52,37.61],[69.19,37.15],[68.86,37.34],[68.14,37.02],[67.83,37.15]],[[70.96,42.27],[71.19,42.7],[71.84,42.85],[73.49,42.5],[73.64,43.09],[74.21,43.3],[75.64,42.88],[76,42.99],[77.66,42.96],[79.14,42.86],[79.65,42.5],[80.26,42.35],[80.12,42.12],[78.54,41.58],[78.19,41.19],[76.91,41.07],[76.53,40.43],[75.47,40.56],[74.78,40.37],[73.82,39.89],[73.96,39.66],[73.68,39.43],[71.78,39.28],[70.55,39.6],[69.46,39.53],[69.56,40.1],[70.65,39.94],[71.01,40.24],[71.78,40.15],[73.05,40.87],[71.87,41.39],[71.16,41.14],[70.42,41.52],[71.26,42.17],[70.96,42.27]],[[52.5,41.78],[52.94,42.12],[54.08,42.32],[54.75,42.04],[55.46,41.26],[55.97,41.31],[57.09,41.32],[56.93,41.83],[57.79,42.17],[58.63,42.75],[59.97,42.22],[60.08,41.43],[60.46,41.22],[61.55,41.27],[61.88,41.08],[62.38,40.05],[63.52,39.36],[64.17,38.89],[65.22,38.4],[66.54,37.97],[66.52,37.36],[66.22,37.39],[65.75,37.66],[65.59,37.3],[64.74,37.11],[64.55,36.31],[63.98,36.01],[63.19,35.86],[62.98,35.4],[62.23,35.27],[61.21,35.65],[61.12,36.49],[60.38,36.53],[59.23,37.41],[58.44,37.52],[57.33,38.03],[56.62,38.12],[56.18,37.94],[55.51,37.96],[54.8,37.39],[53.92,37.2],[53.74,37.91],[53.88,38.95],[53.1,39.29],[53.36,39.98],[52.7,40.03],[52.92,40.88],[53.86,40.63],[54.74,40.95],[54.01,41.55],[53.72,42.12],[52.92,41.87],[52.81,41.13],[52.5,41.78]],[[48.57,29.93],[48.02,30.45],[48,30.98],[47.68,30.98],[47.85,31.71],[47.34,32.47],[46.11,33.02],[45.42,33.97],[45.65,34.75],[46.15,35.09],[46.08,35.68],[45.42,35.98],[44.77,37.17],[44.22,37.97],[44.42,38.28],[44.11,39.43],[44.79,39.71],[44.95,39.34],[45.46,38.87],[46.14,38.74],[46.51,38.77],[47.68,39.51],[48.06,39.58],[48.35,39.29],[48.01,38.79],[48.63,38.27],[48.88,38.32],[49.2,37.58],[50.15,37.37],[50.84,36.87],[52.26,36.7],[53.83,36.96],[53.92,37.2],[54.8,37.39],[55.51,37.96],[56.18,37.94],[56.62,38.12],[57.33,38.03],[58.44,37.52],[59.23,37.41],[60.38,36.53],[61.12,36.49],[61.21,35.65],[60.8,34.4],[60.53,33.68],[60.96,33.53],[60.54,32.98],[60.86,32.18],[60.94,31.55],[61.7,31.38],[61.78,30.74],[60.87,29.83],[61.37,29.3],[61.77,28.7],[62.73,28.26],[62.75,27.38],[63.23,27.22],[63.32,26.76],[61.88,26.24],[61.5,25.08],[59.61,25.38],[58.52,25.61],[57.4,25.74],[56.97,26.97],[56.49,27.14],[55.72,26.96],[54.72,26.48],[53.49,26.81],[52.48,27.58],[51.52,27.87],[50.85,28.81],[50.11,30.15],[49.58,29.99],[48.94,30.32],[48.57,29.93]],[[35.72,32.71],[35.7,32.72],[35.84,32.87],[35.82,33.28],[36.07,33.82],[36.61,34.2],[36.45,34.59],[36,34.65],[35.9,35.41],[36.15,35.82],[36.42,36.04],[36.69,36.26],[36.74,36.82],[37.07,36.62],[38.17,36.9],[38.7,36.71],[39.52,36.72],[40.68,37.09],[41.21,37.07],[42.35,37.23],[41.84,36.61],[41.29,36.36],[41.38,35.63],[41.01,34.42],[38.79,33.38],[36.83,32.31],[35.72,32.71]],[[46.51,38.77],[46.14,38.74],[45.74,39.32],[45.74,39.47],[45.3,39.47],[45,39.74],[44.79,39.71],[44.4,40],[43.66,40.25],[43.75,40.74],[43.58,41.09],[44.97,41.25],[45.18,40.99],[45.56,40.81],[45.36,40.56],[45.89,40.22],[45.61,39.9],[46.04,39.63],[46.48,39.46],[46.51,38.77]],[[11.03,58.86],[11.47,59.43],[12.3,60.12],[12.63,61.29],[11.99,61.8],[11.93,63.13],[12.58,64.07],[13.57,64.05],[13.92,64.44],[13.56,64.79],[15.11,66.19],[16.11,67.3],[16.77,68.01],[17.73,68.01],[17.99,68.57],[19.88,68.41],[20.03,69.07],[20.64,69.11],[21.98,68.62],[23.54,67.94],[23.57,66.4],[23.9,66.01],[22.18,65.72],[21.21,65.03],[21.37,64.41],[19.78,63.61],[17.85,62.75],[17.12,61.34],[17.83,60.64],[18.79,60.08],[17.87,58.95],[16.83,58.72],[16.45,57.04],[15.88,56.1],[14.67,56.2],[14.1,55.41],[12.94,55.36],[12.62,56.31],[11.79,57.44],[11.03,58.86]],[[28.18,56.17],[29.23,55.92],[29.37,55.67],[29.9,55.79],[30.88,55.55],[30.97,55.08],[30.76,54.81],[31.38,54.16],[31.79,53.97],[31.73,53.79],[32.41,53.62],[32.69,53.35],[32.3,53.13],[31.5,53.17],[31.3,53.07],[31.54,52.74],[31.79,52.1],[30.93,52.04],[30.62,51.82],[30.56,51.32],[30.16,51.42],[29.26,51.37],[28.99,51.6],[28.62,51.43],[28.24,51.57],[27.46,51.59],[26.34,51.83],[25.33,51.91],[24.55,51.89],[24.01,51.62],[23.53,51.58],[23.51,52.02],[23.2,52.49],[23.8,52.69],[23.81,53.09],[23.53,53.47],[23.48,53.91],[24.45,53.91],[25.54,54.28],[25.77,54.85],[26.59,55.17],[26.49,55.61],[27.1,55.78],[28.18,56.17]],[[31.79,52.1],[32.16,52.06],[32.41,52.29],[32.72,52.24],[33.75,52.33],[34.39,51.77],[34.14,51.57],[34.22,51.26],[35.02,51.21],[35.38,50.77],[35.36,50.58],[36.62,50.23],[37.39,50.38],[38.01,49.92],[38.59,49.93],[40.07,49.6],[40.08,49.31],[39.67,48.78],[39.9,48.23],[39.74,47.9],[38.77,47.83],[38.26,47.55],[38.22,47.1],[37.42,47.02],[36.76,46.7],[35.82,46.65],[34.96,46.27],[35.01,45.74],[34.86,45.77],[34.73,45.97],[34.41,46],[33.7,46.22],[33.44,45.97],[33.3,46.08],[31.74,46.33],[31.67,46.71],[30.75,46.58],[30.38,46.03],[29.6,45.29],[29.15,45.46],[28.68,45.3],[28.23,45.49],[28.49,45.6],[28.66,45.94],[28.94,46.26],[28.86,46.44],[29.07,46.52],[29.17,46.38],[29.76,46.35],[30.03,46.42],[29.84,46.53],[29.91,46.67],[29.56,46.93],[29.41,47.35],[29.05,47.51],[29.12,47.85],[28.67,48.12],[28.26,48.16],[27.52,48.47],[26.86,48.37],[26.62,48.22],[26.2,48.22],[25.95,47.99],[25.21,47.89],[24.87,47.74],[24.4,47.98],[23.76,47.99],[23.14,48.1],[22.71,47.88],[22.64,48.15],[22.08,48.42],[22.28,48.83],[22.56,49.09],[22.78,49.03],[22.52,49.48],[23.43,50.31],[23.92,50.43],[24.03,50.71],[23.53,51.58],[24.01,51.62],[24.55,51.89],[25.33,51.91],[26.34,51.83],[27.46,51.59],[28.24,51.57],[28.62,51.43],[28.99,51.6],[29.26,51.37],[30.16,51.42],[30.56,51.32],[30.62,51.82],[30.93,52.04],[31.79,52.1]],[[23.48,53.91],[23.53,53.47],[23.81,53.09],[23.8,52.69],[23.2,52.49],[23.51,52.02],[23.53,51.58],[24.03,50.71],[23.92,50.43],[23.43,50.31],[22.52,49.48],[22.78,49.03],[22.56,49.09],[21.61,49.47],[20.89,49.33],[20.42,49.43],[19.82,49.22],[19.32,49.57],[18.91,49.44],[18.85,49.5],[18.39,49.99],[17.65,50.05],[17.56,50.36],[16.87,50.47],[16.72,50.22],[16.18,50.42],[16.24,50.7],[15.49,50.78],[15.02,51.11],[14.61,51.75],[14.69,52.09],[14.44,52.63],[14.07,52.98],[14.35,53.25],[14.12,53.76],[14.8,54.05],[16.36,54.51],[17.62,54.85],[18.62,54.68],[18.7,54.44],[19.66,54.43],[20.89,54.31],[22.73,54.33],[23.24,54.22],[23.48,53.91]],[[16.98,48.12],[16.9,47.72],[16.34,47.71],[16.53,47.5],[16.2,46.85],[16.01,46.68],[15.14,46.66],[14.63,46.43],[13.81,46.51],[12.38,46.77],[12.15,47.11],[11.17,46.94],[11.05,46.75],[10.44,46.89],[9.93,46.92],[9.48,47.1],[9.63,47.35],[9.6,47.52],[9.89,47.58],[10.4,47.3],[10.54,47.57],[11.42,47.52],[12.14,47.7],[12.62,47.67],[12.93,47.47],[13.03,47.64],[12.88,48.29],[13.24,48.42],[13.6,48.88],[14.34,48.56],[14.9,48.96],[15.26,49.04],[16.03,48.73],[16.5,48.79],[16.96,48.6],[16.88,48.47],[16.98,48.12]],[[22.08,48.42],[22.64,48.15],[22.71,47.88],[22.1,47.67],[21.63,46.99],[21.02,46.32],[20.22,46.13],[19.6,46.17],[18.83,45.91],[18.46,45.76],[17.63,45.95],[16.88,46.38],[16.57,46.5],[16.37,46.84],[16.2,46.85],[16.53,47.5],[16.34,47.71],[16.9,47.72],[16.98,48.12],[17.49,47.87],[17.86,47.76],[18.7,47.88],[18.78,48.08],[19.18,48.11],[19.66,48.27],[19.77,48.2],[20.24,48.33],[20.48,48.56],[20.8,48.62],[21.87,48.32],[22.08,48.42]],[[26.62,48.22],[26.86,48.37],[27.52,48.47],[28.26,48.16],[28.67,48.12],[29.12,47.85],[29.05,47.51],[29.41,47.35],[29.56,46.93],[29.91,46.67],[29.84,46.53],[30.03,46.42],[29.76,46.35],[29.17,46.38],[29.07,46.52],[28.86,46.44],[28.94,46.26],[28.66,45.94],[28.49,45.6],[28.23,45.49],[28.05,45.95],[28.16,46.37],[28.13,46.81],[27.55,47.41],[27.23,47.83],[26.92,48.12],[26.62,48.22]],[[28.23,45.49],[28.68,45.3],[29.15,45.46],[29.6,45.29],[29.63,45.04],[29.14,44.82],[28.84,44.91],[28.56,43.71],[27.97,43.81],[27.24,44.18],[26.07,43.94],[25.57,43.69],[24.1,43.74],[23.33,43.9],[22.94,43.82],[22.66,44.24],[22.47,44.41],[22.71,44.58],[22.46,44.7],[22.15,44.48],[21.56,44.77],[21.48,45.18],[20.87,45.42],[20.76,45.74],[20.22,46.13],[21.02,46.32],[21.63,46.99],[22.1,47.67],[22.71,47.88],[23.14,48.1],[23.76,47.99],[24.4,47.98],[24.87,47.74],[25.21,47.89],[25.95,47.99],[26.2,48.22],[26.62,48.22],[26.92,48.12],[27.23,47.83],[27.55,47.41],[28.13,46.81],[28.16,46.37],[28.05,45.95],[28.23,45.49]],[[26.49,55.61],[26.59,55.17],[25.77,54.85],[25.54,54.28],[24.45,53.91],[23.48,53.91],[23.24,54.22],[22.73,54.33],[22.65,54.58],[22.76,54.86],[22.31,55.02],[21.27,55.19],[21.05,56.03],[22.2,56.34],[23.88,56.27],[24.86,56.37],[25,56.16],[25.53,56.1],[26.49,55.61]],[[27.29,57.47],[27.77,57.24],[27.86,56.76],[28.18,56.17],[27.1,55.78],[26.49,55.61],[25.53,56.1],[25,56.16],[24.86,56.37],[23.88,56.27],[22.2,56.34],[21.05,56.03],[21.09,56.78],[21.58,57.41],[22.52,57.75],[23.32,57.01],[24.12,57.03],[24.31,57.79],[25.17,57.97],[25.6,57.85],[26.46,57.48],[27.29,57.47]],[[27.98,59.48],[28.13,59.3],[27.42,58.72],[27.72,57.79],[27.29,57.47],[26.46,57.48],[25.6,57.85],[25.17,57.97],[24.31,57.79],[24.43,58.38],[24.06,58.26],[23.43,58.61],[23.34,59.19],[24.6,59.47],[25.86,59.61],[26.95,59.45],[27.98,59.48]],[[14.12,53.76],[14.35,53.25],[14.07,52.98],[14.44,52.63],[14.69,52.09],[14.61,51.75],[15.02,51.11],[14.57,51],[14.31,51.12],[14.06,50.93],[13.34,50.73],[12.97,50.48],[12.24,50.27],[12.41,49.97],[12.52,49.55],[13.03,49.31],[13.6,48.88],[13.24,48.42],[12.88,48.29],[13.03,47.64],[12.93,47.47],[12.62,47.67],[12.14,47.7],[11.42,47.52],[10.54,47.57],[10.4,47.3],[9.89,47.58],[9.6,47.52],[8.52,47.83],[8.32,47.61],[7.47,47.62],[7.59,48.33],[8.1,49.02],[6.66,49.2],[6.19,49.46],[6.24,49.9],[6.04,50.13],[6.16,50.8],[5.99,51.85],[6.59,51.85],[6.84,52.23],[7.09,53.14],[6.91,53.48],[7.1,53.69],[7.94,53.75],[8.12,53.53],[8.8,54.02],[8.57,54.4],[8.53,54.96],[9.28,54.83],[9.92,54.98],[9.94,54.6],[10.95,54.36],[10.94,54.01],[11.96,54.2],[12.52,54.47],[13.65,54.08],[14.12,53.76]],[[22.66,44.24],[22.94,43.82],[23.33,43.9],[24.1,43.74],[25.57,43.69],[26.07,43.94],[27.24,44.18],[27.97,43.81],[28.56,43.71],[28.04,43.29],[27.68,42.58],[28,42.01],[27.14,42.14],[26.12,41.83],[26.11,41.33],[25.2,41.23],[24.49,41.58],[23.69,41.31],[22.95,41.34],[22.88,42],[22.38,42.32],[22.55,42.46],[22.44,42.58],[22.61,42.9],[22.98,43.21],[22.5,43.64],[22.41,44.01],[22.66,44.24]],[[26.29,35.3],[26.16,35],[24.72,34.92],[24.73,35.09],[23.51,35.28],[23.7,35.71],[24.25,35.37],[25.03,35.43],[25.77,35.35],[25.75,35.18],[26.29,35.3]],[[22.95,41.34],[23.69,41.31],[24.49,41.58],[25.2,41.23],[26.11,41.33],[26.12,41.83],[26.6,41.56],[26.29,40.94],[26.06,40.82],[25.45,40.85],[24.92,40.95],[23.72,40.69],[24.41,40.12],[23.9,39.96],[23.34,39.96],[22.82,40.48],[22.63,40.26],[22.85,39.66],[23.35,39.19],[22.97,38.97],[23.53,38.51],[24.02,38.22],[24.04,37.65],[23.11,37.92],[23.41,37.41],[22.78,37.3],[23.15,36.42],[22.49,36.41],[21.67,36.84],[21.3,37.64],[21.12,38.31],[20.73,38.77],[20.22,39.34],[20.15,39.63],[20.62,40.11],[20.67,40.44],[21,40.58],[21.02,40.84],[21.67,40.93],[22.06,41.15],[22.6,41.13],[22.76,41.3],[22.95,41.34]],[[44.77,37.17],[44.29,37],[43.94,37.26],[42.78,37.39],[42.35,37.23],[41.21,37.07],[40.68,37.09],[39.52,36.72],[38.7,36.71],[38.17,36.9],[37.07,36.62],[36.74,36.82],[36.69,36.26],[36.42,36.04],[36.15,35.82],[35.78,36.28],[36.16,36.65],[35.55,36.56],[34.71,36.8],[34.03,36.22],[32.51,36.11],[31.7,36.64],[30.62,36.68],[30.39,36.26],[29.7,36.15],[28.73,36.68],[27.64,36.66],[27.05,37.65],[26.32,38.21],[26.8,38.99],[26.17,39.46],[27.28,40.42],[28.82,40.46],[29.24,41.22],[31.15,41.09],[32.35,41.74],[33.51,42.02],[35.17,42.04],[36.91,41.33],[38.35,40.95],[39.51,41.1],[40.37,41.01],[41.55,41.54],[42.62,41.58],[43.58,41.09],[43.75,40.74],[43.66,40.25],[44.4,40],[44.79,39.71],[44.11,39.43],[44.42,38.28],[44.22,37.97],[44.77,37.17]],[[26.12,41.83],[27.14,42.14],[28,42.01],[28.11,41.62],[28.99,41.3],[28.81,41.06],[27.62,41],[27.19,40.69],[26.36,40.15],[26.04,40.62],[26.06,40.82],[26.29,40.94],[26.6,41.56],[26.12,41.83]],[[21.02,40.84],[21,40.58],[20.67,40.44],[20.62,40.11],[20.15,39.63],[19.98,39.69],[19.96,39.91],[19.41,40.25],[19.32,40.73],[19.4,41.41],[19.54,41.72],[19.37,41.88],[19.31,42.2],[19.74,42.69],[19.8,42.5],[20.07,42.59],[20.28,42.32],[20.52,42.22],[20.59,41.86],[20.46,41.52],[20.6,41.09],[21.02,40.84]],[[16.57,46.5],[16.88,46.38],[17.63,45.95],[18.46,45.76],[18.83,45.91],[19.07,45.52],[19.39,45.24],[19.01,44.86],[18.55,45.08],[17.86,45.07],[17,45.23],[16.53,45.21],[16.32,45],[15.96,45.23],[15.75,44.82],[16.24,44.35],[16.46,44.04],[16.91,43.67],[17.3,43.45],[17.67,43.03],[18.56,42.65],[18.45,42.48],[17.51,42.85],[16.93,43.21],[16.01,43.51],[15.18,44.24],[15.38,44.32],[14.92,44.74],[14.9,45.08],[14.26,45.23],[13.95,44.8],[13.66,45.14],[13.68,45.48],[13.71,45.5],[14.41,45.47],[14.6,45.64],[14.93,45.47],[15.33,45.45],[15.32,45.73],[15.67,45.83],[15.77,46.24],[16.57,46.5]],[[9.6,47.52],[9.63,47.35],[9.48,47.1],[9.93,46.92],[10.44,46.89],[10.36,46.48],[9.92,46.31],[9.18,46.44],[8.97,46.04],[8.49,46],[8.32,46.16],[7.76,45.82],[7.27,45.78],[6.84,45.99],[6.5,46.43],[6.02,46.27],[6.04,46.73],[6.77,47.29],[6.74,47.54],[7.19,47.45],[7.47,47.62],[8.32,47.61],[8.52,47.83],[9.6,47.52]],[[6.04,50.13],[6.24,49.9],[6.19,49.46],[5.9,49.44],[5.68,49.53],[5.78,50.09],[6.04,50.13]],[[6.16,50.8],[6.04,50.13],[5.78,50.09],[5.68,49.53],[4.8,49.99],[4.29,49.91],[3.59,50.38],[3.12,50.78],[2.66,50.8],[2.51,51.15],[3.31,51.35],[4.05,51.27],[4.97,51.47],[5.61,51.04],[6.16,50.8]],[[6.91,53.48],[7.09,53.14],[6.84,52.23],[6.59,51.85],[5.99,51.85],[6.16,50.8],[5.61,51.04],[4.97,51.47],[4.05,51.27],[3.31,51.35],[3.83,51.62],[4.71,53.09],[6.08,53.51],[6.91,53.48]],[[-9.03,41.88],[-8.67,42.14],[-8.26,42.28],[-8.01,41.79],[-7.42,41.79],[-7.25,41.92],[-6.67,41.88],[-6.39,41.38],[-6.85,41.11],[-6.86,40.33],[-7.03,40.19],[-7.07,39.71],[-7.5,39.63],[-7.1,39.03],[-7.37,38.37],[-7.03,38.08],[-7.17,37.8],[-7.54,37.43],[-7.45,37.1],[-7.86,36.84],[-8.38,36.98],[-8.9,36.87],[-8.75,37.65],[-8.84,38.27],[-9.29,38.36],[-9.53,38.74],[-9.45,39.39],[-9.05,39.76],[-8.98,40.16],[-8.77,40.76],[-8.79,41.18],[-8.99,41.54],[-9.03,41.88]],[[-7.45,37.1],[-7.54,37.43],[-7.17,37.8],[-7.03,38.08],[-7.37,38.37],[-7.1,39.03],[-7.5,39.63],[-7.07,39.71],[-7.03,40.19],[-6.86,40.33],[-6.85,41.11],[-6.39,41.38],[-6.67,41.88],[-7.25,41.92],[-7.42,41.79],[-8.01,41.79],[-8.26,42.28],[-8.67,42.14],[-9.03,41.88],[-8.98,42.59],[-9.39,43.03],[-7.98,43.75],[-6.76,43.57],[-5.41,43.57],[-4.35,43.4],[-3.52,43.46],[-1.9,43.42],[-1.5,43.03],[.34,42.58],[.7,42.8],[1.83,42.34],[2.99,42.47],[3.04,41.89],[2.09,41.23],[.81,41.01],[.72,40.68],[.11,40.12],[-.28,39.31],[.11,38.74],[-.47,38.29],[-.68,37.64],[-1.44,37.44],[-2.15,36.67],[-3.41,36.66],[-4.37,36.68],[-5,36.32],[-5.38,35.95],[-5.87,36.03],[-6.24,36.37],[-6.52,36.94],[-7.45,37.1]],[[-6.2,53.87],[-6.03,53.15],[-6.79,52.26],[-8.56,51.67],[-9.98,51.82],[-9.17,52.86],[-9.69,53.88],[-8.33,54.67],[-7.57,55.13],[-7.37,54.6],[-7.57,54.06],[-6.95,54.07],[-6.2,53.87]],[[165.78,-21.08],[166.6,-21.7],[167.12,-22.16],[166.74,-22.4],[166.19,-22.13],[165.47,-21.68],[164.83,-21.15],[164.17,-20.45],[164.03,-20.11],[164.46,-20.12],[165.02,-20.46],[165.46,-20.8],[165.78,-21.08]],[[162.12,-10.48],[162.4,-10.83],[161.7,-10.82],[161.32,-10.21],[161.92,-10.45],[162.12,-10.48]],[[161.68,-9.6],[161.53,-9.78],[160.79,-8.92],[160.58,-8.32],[160.92,-8.32],[161.28,-9.12],[161.68,-9.6]],[[160.85,-9.87],[160.46,-9.9],[159.85,-9.79],[159.64,-9.64],[159.7,-9.24],[160.36,-9.4],[160.69,-9.61],[160.85,-9.87]],[[159.64,-8.02],[159.88,-8.34],[159.92,-8.54],[159.13,-8.11],[158.59,-7.75],[158.21,-7.42],[158.36,-7.32],[158.82,-7.56],[159.64,-8.02]],[[157.14,-7.02],[157.54,-7.35],[157.34,-7.4],[156.9,-7.18],[156.49,-6.77],[156.54,-6.6],[157.14,-7.02]],[[176.89,-40.07],[176.51,-40.61],[176.01,-41.29],[175.24,-41.69],[175.07,-41.43],[174.65,-41.28],[175.23,-40.46],[174.9,-39.91],[173.82,-39.51],[173.85,-39.15],[174.57,-38.8],[174.74,-38.03],[174.7,-37.38],[174.29,-36.71],[174.32,-36.53],[173.84,-36.12],[173.06,-35.24],[172.63,-34.53],[173.01,-34.45],[173.55,-35.01],[174.33,-35.27],[174.61,-36.16],[175.34,-37.21],[175.36,-36.53],[175.81,-36.8],[175.96,-37.56],[176.76,-37.88],[177.44,-37.96],[178.01,-37.58],[178.52,-37.7],[178.28,-38.58],[177.97,-39.17],[177.21,-39.15],[176.94,-39.45],[177.03,-39.88],[176.89,-40.07]],[[169.67,-43.56],[170.52,-43.03],[171.13,-42.51],[171.57,-41.77],[171.95,-41.51],[172.1,-40.96],[172.8,-40.49],[173.02,-40.92],[173.25,-41.33],[173.96,-40.93],[174.25,-41.35],[174.25,-41.77],[173.88,-42.23],[173.22,-42.97],[172.71,-43.37],[173.08,-43.85],[172.31,-43.87],[171.45,-44.24],[171.18,-44.9],[170.62,-45.91],[169.83,-46.36],[169.33,-46.64],[168.41,-46.62],[167.76,-46.29],[166.68,-46.22],[166.51,-45.85],[167.05,-45.11],[168.3,-44.12],[168.95,-43.94],[169.67,-43.56]],[[147.69,-40.81],[148.29,-40.87],[148.36,-42.06],[148.02,-42.41],[147.91,-43.21],[147.56,-42.94],[146.87,-43.64],[146.66,-43.58],[146.05,-43.55],[145.43,-42.69],[145.3,-42.03],[144.72,-41.16],[144.74,-40.7],[145.4,-40.79],[146.36,-41.14],[146.91,-41],[147.69,-40.81]],[[126.15,-32.22],[125.09,-32.73],[124.22,-32.96],[124.03,-33.48],[123.66,-33.89],[122.81,-33.91],[122.18,-34],[121.3,-33.82],[120.58,-33.93],[119.89,-33.98],[119.3,-34.51],[119.01,-34.46],[118.5,-34.75],[118.03,-35.06],[117.29,-35.03],[116.62,-35.03],[115.56,-34.39],[115.03,-34.2],[115.05,-33.62],[115.54,-33.49],[115.71,-33.26],[115.68,-32.9],[115.8,-32.21],[115.69,-31.61],[115.16,-30.6],[115,-30.03],[115.04,-29.46],[114.64,-28.81],[114.62,-28.52],[114.17,-28.12],[114.05,-27.33],[113.48,-26.54],[113.34,-26.12],[113.78,-26.55],[113.44,-25.62],[113.94,-25.91],[114.23,-26.3],[114.22,-25.79],[113.72,-25],[113.63,-24.68],[113.39,-24.38],[113.5,-23.81],[113.71,-23.56],[113.84,-23.06],[113.74,-22.47],[114.15,-21.76],[114.22,-22.52],[114.65,-21.83],[115.46,-21.49],[115.95,-21.07],[116.71,-20.7],[117.16,-20.62],[117.44,-20.75],[118.23,-20.37],[118.84,-20.26],[118.99,-20.04],[119.25,-19.95],[119.8,-19.98],[120.86,-19.68],[121.4,-19.24],[121.65,-18.71],[122.24,-18.2],[122.29,-17.8],[122.31,-17.26],[123.01,-16.41],[123.43,-17.27],[123.86,-17.07],[123.5,-16.6],[123.82,-16.11],[124.26,-16.33],[124.38,-15.57],[124.93,-15.08],[125.17,-14.68],[125.67,-14.51],[125.69,-14.23],[126.13,-14.35],[126.14,-14.1],[126.58,-13.95],[127.07,-13.82],[127.8,-14.28],[128.36,-14.87],[128.98,-14.88],[129.62,-14.97],[129.41,-14.42],[129.89,-13.62],[130.34,-13.36],[130.18,-13.11],[130.62,-12.54],[131.22,-12.18],[131.73,-12.3],[132.58,-12.11],[132.56,-11.6],[131.82,-11.27],[132.36,-11.13],[133.02,-11.38],[133.55,-11.79],[134.39,-12.04],[134.68,-11.94],[135.3,-12.25],[135.88,-11.96],[136.26,-12.05],[136.49,-11.86],[136.95,-12.35],[136.68,-12.89],[136.31,-13.29],[135.96,-13.32],[136.08,-13.72],[135.78,-14.22],[135.43,-14.72],[135.5,-15],[136.3,-15.55],[137.07,-15.87],[137.58,-16.22],[138.3,-16.81],[138.59,-16.81],[139.11,-17.06],[139.26,-17.37],[140.22,-17.71],[140.87,-17.37],[141.07,-16.83],[141.27,-16.39],[141.4,-15.84],[141.7,-15.04],[141.56,-14.56],[141.63,-14.27],[141.52,-13.7],[141.65,-12.94],[141.84,-12.74],[141.69,-12.41],[141.93,-11.88],[142.12,-11.33],[142.14,-11.04],[142.52,-10.67],[142.8,-11.16],[142.87,-11.78],[143.12,-11.9],[143.16,-12.33],[143.52,-12.83],[143.6,-13.4],[143.56,-13.76],[143.92,-14.55],[144.56,-14.17],[144.9,-14.59],[145.37,-14.99],[145.27,-15.43],[145.49,-16.29],[145.64,-16.78],[145.89,-16.91],[146.16,-17.76],[146.06,-18.28],[146.39,-18.96],[147.47,-19.48],[148.18,-19.96],[148.85,-20.39],[148.72,-20.63],[149.29,-21.26],[149.68,-22.34],[150.08,-22.12],[150.48,-22.56],[150.73,-22.4],[150.9,-23.46],[151.61,-24.08],[152.07,-24.46],[152.86,-25.27],[153.14,-26.07],[153.16,-26.64],[153.09,-27.26],[153.57,-28.11],[153.51,-28.99],[153.34,-29.46],[153.07,-30.35],[153.09,-30.92],[152.89,-31.64],[152.45,-32.55],[151.71,-33.04],[151.34,-33.82],[151.01,-34.31],[150.71,-35.17],[150.33,-35.67],[150.08,-36.42],[149.95,-37.11],[150,-37.43],[149.42,-37.77],[148.31,-37.81],[147.38,-38.22],[146.92,-38.61],[146.32,-39.04],[145.49,-38.59],[144.88,-38.42],[145.03,-37.9],[144.49,-38.09],[143.61,-38.81],[142.75,-38.54],[142.18,-38.38],[141.61,-38.31],[140.64,-38.02],[139.99,-37.4],[139.81,-36.64],[139.58,-36.14],[139.08,-35.73],[138.12,-35.61],[138.45,-35.13],[138.21,-34.39],[137.72,-35.08],[136.83,-35.26],[137.35,-34.71],[137.51,-34.13],[137.89,-33.64],[137.81,-32.9],[137,-33.75],[136.37,-34.09],[135.99,-34.89],[135.21,-34.48],[135.24,-33.95],[134.61,-33.22],[134.09,-32.85],[134.27,-32.62],[132.99,-32.01],[132.29,-31.98],[131.33,-31.5],[129.53,-31.59],[128.24,-31.95],[127.1,-32.28],[126.15,-32.22]],[[81.79,7.52],[81.64,6.48],[81.22,6.2],[80.35,5.97],[79.87,6.76],[79.7,8.2],[80.15,9.82],[80.84,9.27],[81.31,8.56],[81.79,7.52]],[[109.48,18.2],[108.65,18.51],[108.63,19.37],[109.12,19.82],[110.21,20.1],[110.79,20.08],[111.01,19.7],[110.57,19.26],[110.34,18.68],[109.48,18.2]],[[80.26,42.35],[80.18,42.92],[80.87,43.18],[79.97,44.92],[81.95,45.32],[82.46,45.54],[83.18,47.33],[85.16,47],[85.72,47.45],[85.77,48.46],[86.6,48.55],[87.36,49.22],[87.75,49.3],[88.02,48.6],[88.85,48.07],[90.28,47.69],[90.97,46.89],[90.59,45.72],[90.95,45.29],[92.13,45.12],[93.48,44.98],[94.69,44.35],[95.31,44.24],[95.76,43.32],[96.35,42.73],[97.45,42.75],[99.52,42.52],[100.85,42.66],[101.83,42.51],[103.31,41.91],[104.52,41.91],[104.96,41.6],[106.13,42.14],[107.74,42.48],[109.24,42.52],[110.41,42.87],[111.13,43.41],[111.83,43.74],[111.67,44.07],[111.35,44.46],[111.87,45.1],[112.43,45.01],[113.46,44.81],[114.46,45.34],[115.98,45.73],[116.72,46.39],[117.42,46.67],[118.87,46.8],[119.66,46.69],[119.77,47.05],[118.87,47.75],[118.06,48.07],[117.29,47.7],[116.31,47.85],[115.74,47.73],[115.48,48.14],[116.19,49.13],[116.68,49.89],[117.88,49.51],[119.29,50.14],[119.28,50.58],[120.18,51.64],[120.74,51.96],[120.73,52.52],[120.18,52.75],[121,53.25],[122.24,53.43],[123.57,53.46],[125.07,53.16],[125.95,52.79],[126.56,51.78],[126.94,51.35],[127.29,50.74],[127.66,49.76],[129.4,49.44],[130.58,48.73],[130.99,47.79],[132.51,47.79],[133.37,48.18],[135.02,48.48],[134.5,47.58],[134.11,47.21],[133.77,46.12],[133.1,45.14],[131.88,45.32],[131.03,44.97],[131.29,44.11],[131.14,42.93],[130.63,42.9],[130.64,42.4],[130,42.98],[129.6,42.42],[128.05,41.99],[128.21,41.47],[127.34,41.5],[126.87,41.82],[126.18,41.11],[125.08,40.57],[124.26,39.93],[122.87,39.64],[122.13,39.17],[121.05,38.9],[121.59,39.36],[121.38,39.75],[122.17,40.42],[121.64,40.95],[120.77,40.59],[119.64,39.9],[119.02,39.25],[118.04,39.2],[117.53,38.74],[118.06,38.06],[118.88,37.9],[118.91,37.45],[119.7,37.16],[120.82,37.87],[121.71,37.48],[122.36,37.46],[122.52,36.93],[121.1,36.65],[120.64,36.11],[119.66,35.61],[119.15,34.91],[120.23,34.36],[120.62,33.38],[121.23,32.46],[121.91,31.69],[121.89,30.95],[121.27,30.68],[121.5,30.14],[122.09,29.83],[121.94,29.02],[121.68,28.23],[121.13,28.14],[120.39,27.05],[119.58,25.74],[118.66,24.55],[117.28,23.63],[115.89,22.78],[114.76,22.67],[114.15,22.22],[113.81,22.55],[113.24,22.05],[111.84,21.55],[110.79,21.4],[110.44,20.34],[109.89,20.28],[109.63,21.01],[109.86,21.39],[108.52,21.71],[108.05,21.55],[107.04,21.81],[106.57,22.22],[106.72,22.79],[105.81,22.98],[105.33,23.35],[104.48,22.82],[103.5,22.7],[102.71,22.71],[102.17,22.46],[101.65,22.32],[101.8,21.17],[101.27,21.2],[101.18,21.44],[101.15,21.85],[100.42,21.56],[99.98,21.74],[99.24,22.12],[99.53,22.95],[98.9,23.14],[98.66,24.06],[97.61,23.9],[97.72,25.08],[98.67,25.92],[98.71,26.74],[98.68,27.51],[98.25,27.75],[97.91,28.34],[97.33,28.26],[96.25,28.41],[96.59,28.83],[96.12,29.45],[95.41,29.03],[94.57,29.28],[93.41,28.64],[92.5,27.9],[91.7,27.77],[91.26,28.04],[90.73,28.06],[90.02,28.3],[89.48,28.04],[88.81,27.3],[88.73,28.09],[88.12,27.88],[86.95,27.97],[85.82,28.2],[85.01,28.64],[84.24,28.84],[83.9,29.32],[83.34,29.46],[82.33,30.11],[81.52,30.42],[81.11,30.18],[79.72,30.88],[78.74,31.52],[78.46,32.62],[79.18,32.48],[79.21,32.99],[78.81,33.51],[78.91,34.32],[77.84,35.49],[76.19,35.9],[75.9,36.67],[75.16,37.13],[74.98,37.42],[74.83,37.99],[74.86,38.38],[74.26,38.61],[73.93,38.51],[73.68,39.43],[73.96,39.66],[73.82,39.89],[74.78,40.37],[75.47,40.56],[76.53,40.43],[76.91,41.07],[78.19,41.19],[78.54,41.58],[80.12,42.12],[80.26,42.35]],[[121.78,24.39],[121.18,22.79],[120.75,21.97],[120.22,22.81],[120.11,23.56],[120.69,24.54],[121.5,25.3],[121.95,25],[121.78,24.39]],[[10.44,46.89],[11.05,46.75],[11.17,46.94],[12.15,47.11],[12.38,46.77],[13.81,46.51],[13.7,46.02],[13.94,45.59],[13.14,45.74],[12.33,45.38],[12.38,44.89],[12.26,44.6],[12.59,44.09],[13.53,43.59],[14.03,42.76],[15.14,41.96],[15.92,41.96],[16.17,41.74],[15.89,41.54],[16.79,41.18],[17.52,40.88],[18.38,40.36],[18.48,40.17],[18.29,39.81],[17.74,40.28],[16.87,40.44],[16.45,39.8],[17.17,39.43],[17.05,38.9],[16.63,38.84],[16.1,37.99],[15.68,37.91],[15.69,38.22],[15.89,38.75],[16.11,38.96],[15.72,39.54],[15.41,40.05],[15,40.17],[14.7,40.61],[14.06,40.79],[13.63,41.19],[12.89,41.25],[12.11,41.71],[11.19,42.36],[10.51,42.93],[10.2,43.92],[9.7,44.04],[8.89,44.37],[8.43,44.23],[7.85,43.77],[7.44,43.69],[7.55,44.13],[7.01,44.25],[6.75,45.03],[7.1,45.33],[6.8,45.71],[6.84,45.99],[7.27,45.78],[7.76,45.82],[8.32,46.16],[8.49,46],[8.97,46.04],[9.18,46.44],[9.92,46.31],[10.36,46.48],[10.44,46.89]],[[14.76,38.14],[15.52,38.23],[15.16,37.44],[15.31,37.13],[15.1,36.62],[14.33,37],[13.83,37.1],[12.43,37.61],[12.57,38.13],[13.74,38.04],[14.76,38.14]],[[8.71,40.9],[9.21,41.21],[9.81,40.5],[9.67,39.18],[9.21,39.24],[8.81,38.91],[8.43,39.17],[8.39,40.38],[8.16,40.95],[8.71,40.9]],[[9.92,54.98],[9.28,54.83],[8.53,54.96],[8.12,55.52],[8.09,56.54],[8.26,56.81],[8.54,57.11],[9.42,57.17],[9.78,57.45],[10.58,57.73],[10.55,57.22],[10.25,56.89],[10.37,56.61],[10.91,56.46],[10.67,56.08],[10.37,56.19],[9.65,55.47],[9.92,54.98]],[[12.37,56.11],[12.69,55.61],[12.09,54.8],[11.04,55.36],[10.9,55.78],[12.37,56.11]],[[-6.2,53.87],[-6.95,54.07],[-7.57,54.06],[-7.37,54.6],[-7.57,55.13],[-6.73,55.17],[-5.66,54.56],[-6.2,53.87]],[[-3.09,53.4],[-3.09,53.4],[-2.95,53.98],[-3.62,54.6],[-3.63,54.61],[-4.84,54.79],[-5.08,55.06],[-4.72,55.51],[-5.05,55.78],[-5.59,55.31],[-5.65,56.27],[-6.15,56.78],[-5.79,57.82],[-5.01,58.63],[-4.21,58.55],[-3,58.63],[-4.07,57.55],[-3.05,57.69],[-1.96,57.68],[-2.22,56.87],[-3.12,55.97],[-2.09,55.91],[-2.01,55.8],[-1.11,54.62],[-.43,54.46],[.19,53.32],[.47,52.93],[1.68,52.74],[1.56,52.1],[1.05,51.81],[1.45,51.29],[.55,50.77],[-.79,50.78],[-2.49,50.5],[-2.96,50.7],[-3.62,50.23],[-4.54,50.34],[-5.24,49.96],[-5.78,50.16],[-4.31,51.21],[-3.41,51.43],[-3.42,51.43],[-4.98,51.59],[-5.27,51.99],[-4.22,52.3],[-4.77,52.84],[-4.58,53.5],[-3.09,53.4]],[[-14.51,66.46],[-14.74,65.81],[-13.61,65.13],[-14.91,64.36],[-17.79,63.68],[-18.66,63.5],[-19.97,63.64],[-22.76,63.96],[-21.78,64.4],[-23.96,64.89],[-22.19,65.08],[-22.23,65.38],[-24.33,65.61],[-23.65,66.26],[-22.13,66.41],[-20.58,65.73],[-19.06,66.28],[-17.8,65.99],[-16.17,66.53],[-14.51,66.46]],[[46.41,41.86],[46.69,41.83],[47.37,41.22],[47.81,41.15],[47.99,41.41],[48.58,41.81],[49.11,41.28],[49.62,40.57],[50.09,40.53],[50.39,40.26],[49.57,40.18],[49.39,39.4],[49.22,39.05],[48.86,38.82],[48.88,38.32],[48.63,38.27],[48.01,38.79],[48.35,39.29],[48.06,39.58],[47.68,39.51],[46.51,38.77],[46.48,39.46],[46.04,39.63],[45.61,39.9],[45.89,40.22],[45.36,40.56],[45.56,40.81],[45.18,40.99],[44.97,41.25],[45.22,41.41],[45.96,41.12],[46.5,41.06],[46.64,41.18],[46.15,41.72],[46.41,41.86]],[[46.14,38.74],[45.46,38.87],[44.95,39.34],[44.79,39.71],[45,39.74],[45.3,39.47],[45.74,39.47],[45.74,39.32],[46.14,38.74]],[[39.95,43.44],[40.08,43.55],[40.92,43.38],[42.4,43.22],[43.76,42.74],[43.93,42.55],[44.54,42.71],[45.47,42.5],[45.78,42.09],[46.41,41.86],[46.15,41.72],[46.64,41.18],[46.5,41.06],[45.96,41.12],[45.22,41.41],[44.97,41.25],[43.58,41.09],[42.62,41.58],[41.55,41.54],[41.7,41.96],[41.45,42.64],[40.88,43.01],[40.32,43.13],[39.95,43.44]],[[120.83,12.7],[120.32,13.47],[121.18,13.43],[121.53,13.07],[121.26,12.21],[120.83,12.7]],[[122.59,9.98],[122.84,10.26],[122.95,10.88],[123.5,10.94],[123.34,10.27],[124.08,11.23],[123.98,10.28],[123.62,9.95],[123.31,9.32],[123,9.02],[122.38,9.71],[122.59,9.98]],[[126.38,8.41],[126.48,7.75],[126.54,7.19],[126.2,6.27],[125.83,7.29],[125.36,6.79],[125.68,6.05],[125.4,5.58],[124.22,6.16],[123.94,6.89],[124.24,7.36],[123.61,7.83],[123.3,7.42],[122.82,7.46],[122.09,6.9],[121.92,7.19],[122.31,8.04],[122.94,8.32],[123.49,8.69],[123.84,8.24],[124.6,8.51],[124.76,8.96],[125.47,8.99],[125.41,9.76],[126.22,9.29],[126.31,8.78],[126.38,8.41]],[[118.5,9.32],[117.18,8.37],[117.67,9.07],[118.39,9.68],[118.99,10.38],[119.51,11.37],[119.69,10.55],[119.03,10],[118.5,9.32]],[[122.34,18.22],[122.17,17.81],[122.51,17.09],[122.25,16.26],[121.66,15.93],[121.51,15.13],[121.73,14.33],[122.26,14.22],[122.7,14.34],[123.95,13.78],[123.85,13.24],[124.18,13],[124.08,12.54],[123.3,13.03],[122.93,13.55],[122.67,13.19],[122.04,13.78],[121.13,13.64],[120.63,13.86],[120.68,14.27],[120.99,14.53],[120.69,14.76],[120.56,14.4],[120.07,14.97],[119.92,15.41],[119.88,16.36],[120.29,16.03],[120.39,17.6],[120.71,18.51],[121.32,18.5],[121.94,18.22],[122.24,18.48],[122.34,18.22]],[[122.04,11.42],[121.88,11.89],[122.48,11.58],[123.12,11.58],[123.1,11.17],[122.64,10.74],[122,10.44],[121.97,10.91],[122.04,11.42]],[[125.5,12.16],[125.78,11.05],[125.01,11.31],[125.03,10.98],[125.28,10.36],[124.8,10.13],[124.76,10.84],[124.46,10.89],[124.3,11.49],[124.89,11.42],[124.88,11.79],[124.27,12.56],[125.23,12.54],[125.5,12.16]],[[100.09,6.46],[100.26,6.64],[101.08,6.21],[101.16,5.69],[101.81,5.81],[102.14,6.22],[102.37,6.13],[102.96,5.53],[103.38,4.85],[103.44,4.18],[103.33,3.73],[103.43,3.38],[103.5,2.79],[103.86,2.52],[104.25,1.63],[104.23,1.29],[103.52,1.23],[102.57,1.97],[101.39,2.76],[101.27,3.27],[100.69,3.94],[100.56,4.77],[100.2,5.31],[100.31,6.04],[100.09,6.46]],[[117.88,4.14],[117.01,4.31],[115.87,4.31],[115.52,3.17],[115.13,2.82],[114.62,1.43],[113.81,1.22],[112.86,1.5],[112.38,1.41],[111.8,.9],[111.16,.98],[110.52,.77],[109.83,1.34],[109.66,2.01],[110.4,1.66],[111.17,1.85],[111.37,2.7],[111.8,2.89],[113,3.1],[113.71,3.89],[114.21,4.53],[114.66,4.01],[114.87,4.35],[115.35,4.32],[115.4,4.95],[115.45,5.45],[116.22,6.14],[116.73,6.92],[117.13,6.93],[117.64,6.42],[117.69,5.99],[118.35,5.71],[119.18,5.41],[119.11,5.02],[118.44,4.97],[118.62,4.48],[117.88,4.14]],[[115.45,5.45],[115.4,4.95],[115.35,4.32],[114.87,4.35],[114.66,4.01],[114.21,4.53],[114.6,4.9],[115.45,5.45]],[[13.81,46.51],[14.63,46.43],[15.14,46.66],[16.01,46.68],[16.2,46.85],[16.37,46.84],[16.57,46.5],[15.77,46.24],[15.67,45.83],[15.32,45.73],[15.33,45.45],[14.93,45.47],[14.6,45.64],[14.41,45.47],[13.71,45.5],[13.94,45.59],[13.7,46.02],[13.81,46.51]],[[28.59,69.07],[28.45,68.36],[29.98,67.7],[29.05,66.94],[30.22,65.81],[29.54,64.95],[30.44,64.2],[30.04,63.55],[31.52,62.87],[31.14,62.36],[30.21,61.78],[28.07,60.5],[26.26,60.42],[24.5,60.06],[22.87,59.85],[22.29,60.39],[21.32,60.72],[21.54,61.7],[21.06,62.61],[21.54,63.19],[22.44,63.82],[24.73,64.9],[25.4,65.11],[25.3,65.53],[23.9,66.01],[23.57,66.4],[23.54,67.94],[21.98,68.62],[20.64,69.11],[21.25,69.37],[22.36,68.84],[23.66,68.89],[24.73,68.65],[25.69,69.09],[26.18,69.83],[27.73,70.16],[29.01,69.77],[28.59,69.07]],[[22.56,49.09],[22.28,48.83],[22.08,48.42],[21.87,48.32],[20.8,48.62],[20.48,48.56],[20.24,48.33],[19.77,48.2],[19.66,48.27],[19.18,48.11],[18.78,48.08],[18.7,47.88],[17.86,47.76],[17.49,47.87],[16.98,48.12],[16.88,48.47],[16.96,48.6],[17.1,48.82],[17.54,48.8],[17.89,48.9],[17.91,49],[18.11,49.04],[18.17,49.27],[18.4,49.31],[18.56,49.49],[18.85,49.5],[18.91,49.44],[19.32,49.57],[19.82,49.22],[20.42,49.43],[20.89,49.33],[21.61,49.47],[22.56,49.09]],[[15.02,51.11],[15.49,50.78],[16.24,50.7],[16.18,50.42],[16.72,50.22],[16.87,50.47],[17.56,50.36],[17.65,50.05],[18.39,49.99],[18.85,49.5],[18.56,49.49],[18.4,49.31],[18.17,49.27],[18.11,49.04],[17.91,49],[17.89,48.9],[17.54,48.8],[17.1,48.82],[16.96,48.6],[16.5,48.79],[16.03,48.73],[15.26,49.04],[14.9,48.96],[14.34,48.56],[13.6,48.88],[13.03,49.31],[12.52,49.55],[12.41,49.97],[12.24,50.27],[12.97,50.48],[13.34,50.73],[14.06,50.93],[14.31,51.12],[14.57,51],[15.02,51.11]],[[36.43,14.42],[36.32,14.82],[36.75,16.29],[36.85,16.96],[37.17,17.26],[37.9,17.43],[38.41,18],[38.99,16.84],[39.27,15.92],[39.81,15.44],[41.18,14.49],[41.73,13.92],[42.28,13.34],[42.59,13],[43.08,12.7],[42.78,12.46],[42.35,12.54],[42.01,12.87],[41.6,13.45],[41.15,13.77],[40.9,14.12],[40.03,14.52],[39.34,14.53],[39.1,14.74],[38.51,14.51],[37.91,14.96],[37.59,14.21],[36.43,14.42]],[[141.88,39.18],[140.96,38.17],[140.98,37.14],[140.6,36.34],[140.77,35.84],[140.25,35.14],[138.97,34.67],[137.22,34.61],[135.79,33.46],[135.12,33.85],[135.08,34.6],[133.34,34.38],[132.16,33.9],[130.99,33.89],[132,33.15],[131.33,31.45],[130.69,31.03],[130.2,31.42],[130.45,32.32],[129.82,32.61],[129.41,33.3],[130.36,33.6],[130.88,34.23],[131.89,34.75],[132.62,35.43],[134.61,35.73],[135.68,35.53],[136.72,37.3],[137.39,36.83],[138.86,37.83],[139.43,38.22],[140.05,39.44],[139.88,40.56],[140.31,41.2],[141.37,41.38],[141.92,39.99],[141.88,39.18]],[[144.61,43.96],[145.32,44.38],[145.54,43.26],[144.06,42.99],[143.18,41.99],[141.61,42.68],[141.07,41.59],[139.96,41.57],[139.82,42.56],[140.31,43.33],[141.38,43.39],[141.67,44.77],[141.97,45.55],[143.14,44.51],[143.91,44.17],[144.61,43.96]],[[132.37,33.46],[132.93,34.06],[133.49,33.94],[133.91,34.36],[134.64,34.15],[134.77,33.81],[134.2,33.2],[133.79,33.52],[133.28,33.29],[133.02,32.7],[132.36,32.99],[132.37,33.46]],[[-58.17,-20.18],[-57.87,-20.73],[-57.94,-22.09],[-56.88,-22.28],[-56.47,-22.09],[-55.8,-22.36],[-55.61,-22.66],[-55.52,-23.57],[-55.4,-23.96],[-55.03,-24],[-54.65,-23.84],[-54.29,-24.02],[-54.29,-24.57],[-54.43,-25.16],[-54.63,-25.74],[-54.79,-26.62],[-55.69,-27.39],[-56.49,-27.55],[-57.61,-27.4],[-58.62,-27.12],[-57.63,-25.6],[-57.78,-25.16],[-58.81,-24.77],[-60.03,-24.03],[-60.85,-23.88],[-62.69,-22.25],[-62.29,-21.05],[-62.26,-20.51],[-61.79,-19.63],[-60.04,-19.34],[-59.11,-19.36],[-58.18,-19.87],[-58.17,-20.18]],[[52,19],[52.78,17.35],[53.11,16.65],[52.39,16.38],[52.19,15.94],[52.17,15.6],[51.17,15.18],[49.57,14.71],[48.68,14],[48.24,13.95],[47.94,14.01],[47.35,13.59],[46.72,13.4],[45.88,13.35],[45.63,13.29],[45.41,13.03],[45.14,12.95],[44.99,12.7],[44.49,12.72],[44.17,12.59],[43.48,12.64],[43.22,13.22],[43.25,13.77],[43.09,14.06],[42.89,14.8],[42.6,15.21],[42.81,15.26],[42.7,15.72],[42.82,15.91],[42.78,16.35],[43.22,16.67],[43.12,17.09],[43.38,17.58],[43.79,17.32],[44.06,17.41],[45.22,17.43],[45.4,17.33],[46.37,17.23],[46.75,17.28],[47,16.95],[47.47,17.12],[48.18,18.17],[49.12,18.62],[52,19]],[[34.95,29.36],[36.07,29.2],[36.5,29.51],[36.74,29.87],[37.5,30],[37.67,30.34],[38,30.51],[37,31.51],[39,32.01],[39.2,32.16],[40.4,31.89],[41.89,31.19],[44.71,29.18],[46.57,29.1],[47.46,29],[47.71,28.53],[48.42,28.55],[48.81,27.69],[49.3,27.46],[49.47,27.11],[50.15,26.69],[50.21,26.28],[50.11,25.94],[50.24,25.61],[50.53,25.33],[50.66,25],[50.81,24.75],[51.11,24.56],[51.39,24.63],[51.58,24.24],[51.62,24.01],[52,23],[55.01,22.5],[55.21,22.71],[55.67,22],[55,20],[52,19],[49.12,18.62],[48.18,18.17],[47.47,17.12],[47,16.95],[46.75,17.28],[46.37,17.23],[45.4,17.33],[45.22,17.43],[44.06,17.41],[43.79,17.32],[43.38,17.58],[43.12,17.09],[43.22,16.67],[42.78,16.35],[42.65,16.77],[42.35,17.08],[42.27,17.47],[41.76,17.83],[41.22,18.67],[40.94,19.49],[40.25,20.17],[39.8,20.34],[39.14,21.29],[39.02,21.99],[39.07,22.58],[38.49,23.69],[38.03,24.08],[37.49,24.29],[37.15,24.86],[37.21,25.08],[36.93,25.6],[36.64,25.83],[36.25,26.57],[35.64,27.38],[35.13,28.06],[34.63,28.06],[34.79,28.61],[34.83,28.96],[34.95,29.36]],[[-48.66,-78.05],[-48.15,-78.05],[-46.66,-77.83],[-45.15,-78.05],[-43.92,-78.48],[-43.49,-79.09],[-43.37,-79.52],[-43.33,-80.03],[-44.88,-80.34],[-46.51,-80.59],[-48.39,-80.83],[-50.48,-81.03],[-52.85,-80.97],[-54.16,-80.63],[-53.99,-80.22],[-51.85,-79.95],[-50.99,-79.61],[-50.37,-79.18],[-49.91,-78.81],[-49.31,-78.46],[-48.66,-78.05]],[[-66.29,-80.26],[-64.04,-80.29],[-61.88,-80.39],[-61.14,-79.98],[-60.61,-79.63],[-59.57,-80.04],[-59.87,-80.55],[-60.16,-81],[-62.25,-80.86],[-64.49,-80.92],[-65.74,-80.59],[-65.74,-80.55],[-66.29,-80.26]],[[-73.91,-71.27],[-73.23,-71.15],[-72.07,-71.19],[-71.78,-70.68],[-71.72,-70.31],[-71.74,-69.51],[-71.17,-69.04],[-70.25,-68.88],[-69.72,-69.25],[-69.49,-69.62],[-69.06,-70.07],[-68.73,-70.5],[-68.45,-70.96],[-68.33,-71.41],[-68.51,-71.8],[-68.78,-72.17],[-69.96,-72.31],[-71.08,-72.5],[-72.39,-72.48],[-71.9,-72.09],[-73.08,-72.23],[-74.19,-72.37],[-74.95,-72.07],[-75.01,-71.66],[-73.91,-71.27]],[[-102.33,-71.89],[-101.7,-71.72],[-100.43,-71.86],[-98.98,-71.93],[-97.88,-72.07],[-96.79,-71.95],[-96.2,-72.52],[-96.98,-72.44],[-98.2,-72.48],[-99.43,-72.44],[-100.78,-72.5],[-101.8,-72.31],[-102.33,-71.89]],[[-122.62,-73.66],[-122.41,-73.32],[-121.21,-73.5],[-119.92,-73.66],[-118.72,-73.48],[-119.29,-73.83],[-120.23,-74.09],[-121.62,-74.01],[-122.62,-73.66]],[[-127.28,-73.46],[-126.56,-73.25],[-125.56,-73.48],[-124.03,-73.87],[-124.62,-73.83],[-125.91,-73.74],[-127.28,-73.46]],[[-163.71,-78.6],[-163.11,-78.22],[-161.24,-78.38],[-160.25,-78.69],[-159.48,-79.05],[-159.21,-79.5],[-161.13,-79.63],[-162.44,-79.28],[-163.03,-78.93],[-163.07,-78.87],[-163.71,-78.6]],[[-180,-84.71],[-179.94,-84.72],[-179.06,-84.14],[-177.26,-84.45],[-177.14,-84.42],[-176.08,-84.1],[-175.95,-84.11],[-175.83,-84.12],[-174.38,-84.53],[-173.12,-84.12],[-172.89,-84.06],[-169.95,-83.88],[-169,-84.12],[-168.53,-84.24],[-167.02,-84.57],[-164.18,-84.83],[-161.93,-85.14],[-158.07,-85.37],[-155.19,-85.1],[-150.94,-85.3],[-148.53,-85.61],[-145.89,-85.31],[-143.11,-85.04],[-142.89,-84.57],[-146.83,-84.53],[-150.06,-84.3],[-150.9,-83.9],[-153.59,-83.69],[-153.41,-83.24],[-153.04,-82.83],[-152.66,-82.45],[-152.86,-82.04],[-154.53,-81.77],[-155.29,-81.41],[-156.84,-81.1],[-154.41,-81.16],[-152.1,-81],[-150.65,-81.34],[-148.87,-81.04],[-147.22,-80.67],[-146.42,-80.34],[-146.77,-79.93],[-148.06,-79.65],[-149.53,-79.36],[-151.59,-79.3],[-153.39,-79.16],[-155.33,-79.06],[-155.98,-78.69],[-157.27,-78.38],[-158.05,-78.03],[-158.36,-76.89],[-157.87,-76.99],[-156.97,-77.3],[-155.33,-77.2],[-153.74,-77.07],[-152.92,-77.5],[-151.33,-77.4],[-150,-77.18],[-148.75,-76.91],[-147.61,-76.58],[-146.11,-76.48],[-146.15,-76.11],[-146.49,-75.73],[-146.2,-75.38],[-144.91,-75.2],[-144.32,-75.54],[-142.79,-75.34],[-141.64,-75.09],[-140.21,-75.07],[-138.86,-74.97],[-137.51,-74.73],[-136.43,-74.52],[-135.22,-74.3],[-134.43,-74.36],[-133.75,-74.44],[-132.26,-74.3],[-130.92,-74.48],[-129.55,-74.46],[-128.24,-74.32],[-126.89,-74.42],[-125.4,-74.52],[-124.01,-74.48],[-122.56,-74.5],[-121.07,-74.52],[-119.7,-74.48],[-118.68,-74.18],[-117.47,-74.03],[-116.21,-74.24],[-115.02,-74.07],[-113.94,-73.72],[-113.3,-74.03],[-112.95,-74.38],[-112.3,-74.71],[-111.26,-74.42],[-110.07,-74.79],[-108.72,-74.91],[-107.56,-75.18],[-106.15,-75.13],[-104.87,-74.95],[-103.37,-74.99],[-102.02,-75.13],[-100.64,-75.3],[-100.12,-74.87],[-100.76,-74.54],[-101.25,-74.18],[-102.55,-74.11],[-103.11,-73.73],[-103.33,-73.36],[-103.68,-72.62],[-102.92,-72.75],[-101.61,-72.81],[-100.31,-72.75],[-99.14,-72.91],[-98.12,-73.21],[-97.69,-73.56],[-96.34,-73.62],[-95.04,-73.48],[-93.67,-73.28],[-92.44,-73.17],[-91.42,-73.4],[-90.09,-73.32],[-89.23,-72.56],[-88.42,-73.01],[-87.27,-73.19],[-86.01,-73.09],[-85.19,-73.48],[-83.88,-73.52],[-82.67,-73.64],[-81.47,-73.85],[-80.69,-73.48],[-80.3,-73.13],[-79.3,-73.52],[-77.92,-73.42],[-76.91,-73.64],[-76.22,-73.97],[-74.89,-73.87],[-73.85,-73.66],[-72.83,-73.4],[-71.62,-73.26],[-70.21,-73.15],[-68.94,-73.01],[-67.96,-72.79],[-67.37,-72.48],[-67.14,-72.05],[-67.25,-71.64],[-67.56,-71.25],[-67.92,-70.85],[-68.23,-70.46],[-68.49,-70.11],[-68.54,-69.72],[-68.45,-69.32],[-67.98,-68.95],[-67.59,-68.54],[-67.43,-68.15],[-67.62,-67.72],[-67.74,-67.33],[-67.25,-66.88],[-66.7,-66.58],[-66.06,-66.21],[-65.37,-65.9],[-64.57,-65.6],[-64.18,-65.17],[-63.63,-64.9],[-63,-64.64],[-62.04,-64.58],[-61.41,-64.27],[-60.71,-64.07],[-59.89,-63.96],[-59.16,-63.7],[-58.6,-63.39],[-57.81,-63.27],[-57.22,-63.53],[-57.6,-63.86],[-58.61,-64.15],[-59.05,-64.37],[-59.79,-64.21],[-60.61,-64.31],[-61.3,-64.55],[-62.02,-64.8],[-62.51,-65.09],[-62.65,-65.48],[-62.59,-65.86],[-62.12,-66.19],[-62.8,-66.43],[-63.74,-66.5],[-64.29,-66.84],[-64.88,-67.15],[-65.51,-67.58],[-65.67,-67.95],[-65.31,-68.37],[-64.78,-68.68],[-63.96,-68.91],[-63.2,-69.23],[-62.79,-69.62],[-62.57,-69.99],[-62.28,-70.38],[-61.81,-70.72],[-61.51,-71.09],[-61.38,-72.01],[-61.08,-72.38],[-61,-72.77],[-60.69,-73.17],[-60.83,-73.7],[-61.38,-74.11],[-61.96,-74.44],[-63.29,-74.58],[-63.74,-74.93],[-64.35,-75.26],[-65.86,-75.63],[-67.19,-75.79],[-68.45,-76.01],[-69.8,-76.22],[-70.6,-76.64],[-72.21,-76.67],[-73.97,-76.64],[-75.56,-76.71],[-77.24,-76.71],[-76.93,-77.11],[-75.4,-77.28],[-74.28,-77.56],[-73.65,-77.91],[-74.77,-78.22],[-76.5,-78.12],[-77.92,-78.38],[-77.99,-78.79],[-78.03,-79.18],[-76.85,-79.51],[-76.63,-79.89],[-75.36,-80.26],[-73.24,-80.42],[-71.44,-80.69],[-70.01,-81],[-68.19,-81.32],[-65.71,-81.47],[-63.25,-81.75],[-61.55,-82.04],[-59.69,-82.38],[-58.71,-82.85],[-58.22,-83.22],[-57.01,-82.87],[-55.36,-82.57],[-53.62,-82.26],[-51.54,-82],[-49.76,-81.73],[-47.27,-81.71],[-44.83,-81.85],[-42.81,-82.08],[-42.16,-81.65],[-40.77,-81.36],[-38.24,-81.34],[-36.26,-81.12],[-34.39,-80.91],[-32.31,-80.77],[-30.1,-80.59],[-28.55,-80.34],[-29.26,-79.98],[-29.68,-79.63],[-29.68,-79.26],[-31.62,-79.3],[-33.68,-79.46],[-35.64,-79.46],[-35.92,-79.08],[-35.78,-78.34],[-35.33,-78.12],[-33.9,-77.89],[-32.21,-77.65],[-31,-77.36],[-29.78,-77.07],[-28.88,-76.67],[-27.51,-76.5],[-26.16,-76.36],[-25.48,-76.28],[-23.93,-76.24],[-22.46,-76.11],[-21.22,-75.91],[-20.01,-75.67],[-18.91,-75.44],[-17.52,-75.13],[-16.64,-74.79],[-15.7,-74.5],[-15.41,-74.11],[-16.46,-73.87],[-16.11,-73.46],[-15.45,-73.15],[-14.41,-72.95],[-13.31,-72.72],[-12.29,-72.4],[-11.51,-72.01],[-11.02,-71.54],[-10.29,-71.26],[-9.1,-71.32],[-8.61,-71.66],[-7.42,-71.7],[-7.38,-71.32],[-6.87,-70.93],[-5.79,-71.03],[-5.54,-71.4],[-4.34,-71.46],[-3.05,-71.28],[-1.79,-71.17],[-.66,-71.23],[-.23,-71.64],[.87,-71.31],[1.89,-71.13],[3.02,-70.99],[4.14,-70.85],[5.16,-70.62],[6.27,-70.46],[7.14,-70.25],[7.74,-69.89],[8.49,-70.15],[9.52,-70.01],[10.25,-70.48],[10.82,-70.83],[11.95,-70.64],[12.4,-70.25],[13.42,-69.97],[14.74,-70.03],[15.13,-70.4],[15.95,-70.03],[17.03,-69.91],[18.2,-69.88],[19.26,-69.89],[20.37,-70.01],[21.45,-70.07],[21.92,-70.4],[22.57,-70.7],[23.66,-70.52],[24.84,-70.48],[25.98,-70.48],[27.09,-70.46],[28.09,-70.33],[29.15,-70.21],[30.03,-69.93],[30.97,-69.76],[31.99,-69.66],[32.75,-69.38],[33.3,-68.84],[33.87,-68.5],[34.91,-68.66],[35.3,-69.01],[36.16,-69.25],[37.2,-69.17],[37.91,-69.52],[38.65,-69.78],[39.67,-69.54],[40.02,-69.11],[40.92,-68.93],[41.96,-68.6],[42.94,-68.46],[44.11,-68.27],[44.9,-68.05],[45.72,-67.82],[46.5,-67.6],[47.44,-67.72],[48.34,-67.37],[48.99,-67.09],[49.93,-67.11],[50.76,-66.88],[50.95,-66.52],[51.79,-66.25],[52.61,-66.05],[53.61,-65.9],[54.54,-65.82],[55.41,-65.88],[56.36,-65.98],[57.16,-66.25],[57.26,-66.68],[58.14,-67.01],[58.74,-67.29],[59.94,-67.41],[60.6,-67.68],[61.43,-67.95],[62.39,-68.01],[63.19,-67.82],[64.05,-67.41],[64.99,-67.62],[65.97,-67.74],[66.91,-67.86],[67.89,-67.93],[68.89,-67.93],[69.71,-68.97],[69.67,-69.23],[69.55,-69.68],[68.6,-69.93],[67.81,-70.3],[67.95,-70.7],[69.06,-70.68],[68.93,-71.07],[68.42,-71.44],[67.95,-71.85],[68.71,-72.17],[69.87,-72.26],[71.02,-72.09],[71.57,-71.7],[71.91,-71.32],[72.46,-71.01],[73.08,-70.72],[73.33,-70.36],[73.86,-69.88],[74.49,-69.78],[75.63,-69.74],[76.62,-69.62],[77.64,-69.46],[78.13,-69.07],[78.43,-68.7],[79.11,-68.33],[80.09,-68.07],[80.93,-67.88],[81.49,-67.54],[82.05,-67.37],[82.78,-67.21],[83.77,-67.31],[84.67,-67.21],[85.65,-67.09],[86.75,-67.15],[87.48,-66.88],[87.99,-66.21],[88.36,-66.48],[88.83,-66.96],[89.67,-67.15],[90.63,-67.23],[91.59,-67.11],[92.61,-67.19],[93.55,-67.21],[94.18,-67.11],[95.02,-67.17],[95.78,-67.39],[96.68,-67.25],[97.76,-67.25],[98.68,-67.11],[99.72,-67.25],[100.39,-66.91],[100.89,-66.58],[101.58,-66.31],[102.83,-65.56],[103.48,-65.7],[104.24,-65.98],[104.91,-66.33],[106.18,-66.94],[107.16,-66.96],[108.08,-66.96],[109.16,-66.84],[110.23,-66.7],[111.06,-66.43],[111.74,-66.13],[112.86,-66.09],[113.6,-65.88],[114.39,-66.07],[114.9,-66.39],[115.6,-66.7],[116.7,-66.66],[117.38,-66.91],[118.58,-67.17],[119.83,-67.27],[120.87,-67.19],[121.65,-66.88],[122.32,-66.56],[123.22,-66.48],[124.12,-66.62],[125.16,-66.72],[126.1,-66.56],[127,-66.56],[127.88,-66.66],[128.8,-66.76],[129.7,-66.58],[130.78,-66.43],[131.8,-66.39],[132.94,-66.39],[133.85,-66.29],[134.76,-66.21],[135.03,-65.72],[135.07,-65.31],[135.7,-65.58],[135.87,-66.03],[136.21,-66.45],[136.62,-66.78],[137.46,-66.96],[138.6,-66.9],[139.91,-66.88],[140.81,-66.82],[142.12,-66.82],[143.06,-66.8],[144.37,-66.84],[145.49,-66.91],[146.2,-67.23],[146,-67.6],[146.65,-67.89],[147.72,-68.13],[148.84,-68.39],[150.13,-68.56],[151.48,-68.72],[152.5,-68.87],[153.64,-68.9],[154.28,-68.56],[155.17,-68.84],[155.93,-69.15],[156.81,-69.38],[158.03,-69.48],[159.18,-69.6],[159.67,-69.99],[160.81,-70.23],[161.57,-70.58],[162.69,-70.74],[163.84,-70.72],[164.92,-70.78],[166.11,-70.76],[167.31,-70.83],[168.43,-70.97],[169.46,-71.21],[170.5,-71.4],[171.21,-71.7],[171.09,-72.09],[170.56,-72.44],[170.11,-72.89],[169.76,-73.24],[169.29,-73.66],[167.98,-73.81],[167.39,-74.17],[166.09,-74.38],[165.64,-74.77],[164.96,-75.15],[164.24,-75.46],[163.82,-75.87],[163.57,-76.24],[163.47,-76.69],[163.49,-77.07],[164.06,-77.46],[164.28,-77.83],[164.74,-78.18],[166.6,-78.32],[167,-78.75],[165.19,-78.91],[163.67,-79.12],[161.77,-79.16],[160.92,-79.73],[160.75,-80.2],[160.32,-80.57],[159.79,-80.95],[161.12,-81.28],[161.63,-81.69],[162.49,-82.06],[163.71,-82.39],[165.1,-82.71],[166.6,-83.02],[168.89,-83.34],[169.41,-83.83],[172.29,-84.04],[172.48,-84.12],[173.22,-84.41],[175.99,-84.16],[178.28,-84.47],[180,-84.71],[-180,-84.71]],[[32.73,35.14],[32.8,35.14],[32.95,35.39],[33.67,35.37],[34.58,35.67],[33.9,35.25],[33.98,35.06],[33.87,35.09],[33.68,35.02],[33.53,35.04],[33.47,35],[33.46,35.1],[33.38,35.16],[33.19,35.17],[32.92,35.09],[32.73,35.14]],[[32.73,35.14],[32.92,35.09],[33.19,35.17],[33.38,35.16],[33.46,35.1],[33.47,35],[33.53,35.04],[33.68,35.02],[33.87,35.09],[33.98,35.06],[34,34.98],[32.98,34.57],[32.49,34.7],[32.26,35.1],[32.73,35.14]],[[-2.17,35.17],[-1.79,34.53],[-1.73,33.92],[-1.39,32.86],[-1.13,32.65],[-1.31,32.26],[-2.62,32.09],[-3.07,31.72],[-3.65,31.64],[-3.69,30.9],[-4.86,30.5],[-5.24,30],[-6.06,29.73],[-7.06,29.58],[-8.67,28.84],[-8.67,27.66],[-8.82,27.66],[-8.79,27.12],[-9.41,27.09],[-9.74,26.86],[-10.19,26.86],[-10.55,26.99],[-11.39,26.88],[-11.72,26.1],[-12.03,26.03],[-12.5,24.77],[-13.89,23.69],[-14.22,22.31],[-14.63,21.86],[-14.75,21.5],[-17,21.42],[-17.02,21.42],[-16.97,21.89],[-16.59,22.16],[-16.26,22.68],[-16.33,23.02],[-15.98,23.72],[-15.42,24.36],[-15.09,24.52],[-14.82,25.1],[-14.8,25.64],[-14.44,26.25],[-13.78,26.62],[-13.14,27.64],[-13.12,27.65],[-12.62,28.04],[-11.69,28.15],[-10.9,28.83],[-10.4,29.1],[-9.56,29.93],[-9.82,31.18],[-9.43,32.04],[-9.3,32.57],[-8.66,33.24],[-7.66,33.7],[-6.91,34.11],[-6.24,35.15],[-5.93,35.76],[-5.19,35.76],[-4.59,35.33],[-3.64,35.4],[-2.6,35.18],[-2.17,35.17]],[[36.87,22],[32.9,22],[29.02,22],[25,22],[25,25.68],[25,29.24],[24.7,30.04],[24.96,30.66],[24.8,31.09],[25.17,31.57],[26.49,31.59],[27.46,31.32],[28.45,31.03],[28.91,30.87],[29.68,31.19],[30.09,31.47],[30.98,31.56],[31.69,31.43],[31.96,30.93],[32.19,31.26],[32.99,31.02],[33.77,30.97],[34.27,31.22],[34.82,29.76],[34.92,29.5],[34.64,29.1],[34.43,28.34],[34.16,27.82],[33.92,27.65],[33.59,27.97],[33.14,28.42],[32.42,29.85],[32.32,29.76],[32.73,28.7],[33.35,27.7],[34.1,26.14],[34.47,25.6],[34.8,25.03],[35.69,23.93],[35.49,23.75],[35.53,23.1],[36.69,22.21],[36.87,22]],[[25,22],[25,20],[23.85,20],[23.84,19.58],[19.85,21.49],[15.86,23.41],[14.85,22.86],[14.14,22.49],[13.58,23.04],[12,23.47],[11.56,24.1],[10.77,24.56],[10.31,24.38],[9.95,24.94],[9.91,25.37],[9.32,26.09],[9.71,26.51],[9.63,27.14],[9.76,27.69],[9.68,28.14],[9.86,28.96],[9.8,29.42],[9.48,30.31],[9.97,30.54],[10.06,30.96],[9.95,31.38],[10.64,31.76],[10.95,32.08],[11.43,32.37],[11.49,33.14],[12.66,32.79],[13.08,32.88],[13.92,32.71],[15.24,32.27],[15.71,31.38],[16.61,31.18],[18.02,30.76],[19.09,30.27],[19.58,30.53],[20.05,30.99],[19.82,31.75],[20.13,32.24],[20.85,32.71],[21.54,32.84],[22.89,32.64],[23.24,32.19],[23.61,32.19],[23.93,32.02],[24.92,31.9],[25.17,31.57],[24.8,31.09],[24.96,30.66],[24.7,30.04],[25,29.24],[25,25.68],[25,22]],[[47.79,8],[44.96,5],[43.66,4.96],[42.77,4.25],[42.13,4.23],[41.86,3.92],[41.17,3.92],[40.77,4.26],[39.85,3.84],[39.56,3.42],[38.89,3.5],[38.67,3.62],[38.44,3.59],[38.12,3.6],[36.86,4.45],[36.16,4.45],[35.82,4.78],[35.82,5.34],[35.3,5.51],[34.71,6.59],[34.25,6.83],[34.08,7.23],[33.57,7.71],[32.95,7.78],[33.29,8.36],[33.82,8.38],[33.98,8.69],[33.96,9.58],[34.26,10.63],[34.73,10.91],[34.83,11.32],[35.26,12.08],[35.87,12.58],[36.27,13.56],[36.43,14.42],[37.59,14.21],[37.91,14.96],[38.51,14.51],[39.1,14.74],[39.34,14.53],[40.03,14.52],[40.9,14.12],[41.15,13.77],[41.6,13.45],[42.01,12.87],[42.35,12.54],[42,12.1],[41.66,11.63],[41.74,11.36],[41.76,11.05],[42.31,11.03],[42.55,11.11],[42.78,10.93],[42.56,10.57],[42.93,10.02],[43.3,9.54],[43.68,9.18],[46.95,8],[47.79,8]],[[42.35,12.54],[42.78,12.46],[43.08,12.7],[43.32,12.39],[43.29,11.98],[42.72,11.74],[43.14,11.46],[42.78,10.93],[42.55,11.11],[42.31,11.03],[41.76,11.05],[41.74,11.36],[41.66,11.63],[42,12.1],[42.35,12.54]],[[48.95,11.41],[48.94,11.39],[48.94,10.98],[48.94,9.97],[48.94,9.45],[48.49,8.84],[47.79,8],[46.95,8],[43.68,9.18],[43.3,9.54],[42.93,10.02],[42.56,10.57],[42.78,10.93],[43.14,11.46],[43.47,11.28],[43.67,10.86],[44.12,10.45],[44.61,10.44],[45.56,10.7],[46.64,10.82],[47.53,11.13],[48.02,11.19],[48.38,11.38],[48.95,11.41]],[[33.9,-.95],[31.87,-1.03],[30.77,-1.01],[30.42,-1.14],[29.82,-1.44],[29.58,-1.34],[29.59,-.59],[29.82,-.21],[29.87,.6],[30.09,1.06],[30.47,1.58],[30.85,1.85],[31.17,2.2],[30.77,2.34],[30.83,3.51],[31.25,3.78],[31.88,3.56],[32.69,3.79],[33.39,3.79],[34,4.25],[34.48,3.55],[34.59,3.05],[35.04,1.91],[34.67,1.18],[34.18,.52],[33.89,.11],[33.9,-.95]],[[30.42,-1.14],[30.81,-1.7],[30.76,-2.29],[30.47,-2.41],[29.94,-2.35],[29.63,-2.92],[29.03,-2.84],[29.12,-2.29],[29.26,-2.21],[29.29,-1.62],[29.58,-1.34],[29.82,-1.44],[30.42,-1.14]],[[18.56,42.65],[17.67,43.03],[17.3,43.45],[16.91,43.67],[16.46,44.04],[16.24,44.35],[15.75,44.82],[15.96,45.23],[16.32,45],[16.53,45.21],[17,45.23],[17.86,45.07],[18.55,45.08],[19.01,44.86],[19.37,44.86],[19.12,44.42],[19.6,44.04],[19.45,43.57],[19.22,43.52],[19.03,43.43],[18.71,43.2],[18.56,42.65]],[[22.38,42.32],[22.88,42],[22.95,41.34],[22.76,41.3],[22.6,41.13],[22.06,41.15],[21.67,40.93],[21.02,40.84],[20.6,41.09],[20.46,41.52],[20.59,41.86],[20.72,41.85],[20.76,42.05],[21.35,42.21],[21.58,42.25],[21.92,42.3],[22.38,42.32]],[[18.83,45.91],[19.6,46.17],[20.22,46.13],[20.76,45.74],[20.87,45.42],[21.48,45.18],[21.56,44.77],[22.15,44.48],[22.46,44.7],[22.71,44.58],[22.47,44.41],[22.66,44.24],[22.41,44.01],[22.5,43.64],[22.98,43.21],[22.61,42.9],[22.44,42.58],[22.55,42.46],[22.38,42.32],[21.92,42.3],[21.58,42.25],[21.54,42.32],[21.66,42.44],[21.77,42.68],[21.63,42.68],[21.44,42.86],[21.27,42.91],[21.14,43.07],[20.96,43.13],[20.81,43.27],[20.63,43.22],[20.5,42.88],[20.26,42.81],[20.34,42.9],[19.96,43.11],[19.63,43.21],[19.49,43.35],[19.22,43.52],[19.45,43.57],[19.6,44.04],[19.12,44.42],[19.37,44.86],[19.01,44.86],[19.39,45.24],[19.07,45.52],[18.83,45.91]],[[20.07,42.59],[19.8,42.5],[19.74,42.69],[19.31,42.2],[19.37,41.88],[19.16,41.96],[18.88,42.28],[18.45,42.48],[18.56,42.65],[18.71,43.2],[19.03,43.43],[19.22,43.52],[19.49,43.35],[19.63,43.21],[19.96,43.11],[20.34,42.9],[20.26,42.81],[20.07,42.59]],[[20.59,41.86],[20.52,42.22],[20.28,42.32],[20.07,42.59],[20.26,42.81],[20.5,42.88],[20.63,43.22],[20.81,43.27],[20.96,43.13],[21.14,43.07],[21.27,42.91],[21.44,42.86],[21.63,42.68],[21.77,42.68],[21.66,42.44],[21.54,42.32],[21.58,42.25],[21.35,42.21],[20.76,42.05],[20.72,41.85],[20.59,41.86]],[[-61.68,10.76],[-61.11,10.89],[-60.9,10.85],[-60.94,10.11],[-61.77,10],[-61.95,10.09],[-61.66,10.37],[-61.68,10.76]],[[30.83,3.51],[29.95,4.17],[29.72,4.6],[29.16,4.39],[28.7,4.46],[28.43,4.29],[27.98,4.41],[27.37,5.23],[27.21,5.55],[26.47,5.95],[26.21,6.55],[25.8,6.98],[25.12,7.5],[25.12,7.83],[24.57,8.23],[23.89,8.62],[24.19,8.73],[24.54,8.92],[24.8,9.81],[25.07,10.27],[25.79,10.41],[25.96,10.14],[26.48,9.55],[26.75,9.47],[27.11,9.64],[27.83,9.6],[27.97,9.4],[28.97,9.4],[29,9.6],[29.51,9.79],[29.62,10.08],[30,10.29],[30.84,9.71],[31.35,9.81],[31.85,10.53],[32.4,11.08],[32.32,11.68],[32.07,11.97],[32.68,12.02],[32.74,12.25],[33.21,12.18],[33.09,11.44],[33.21,10.72],[33.72,10.33],[33.84,9.98],[33.82,9.48],[33.96,9.46],[33.98,8.69],[33.82,8.38],[33.29,8.36],[32.95,7.78],[33.57,7.71],[34.08,7.23],[34.25,6.83],[34.71,6.59],[35.3,5.51],[34.62,4.85],[34,4.25],[33.39,3.79],[32.69,3.79],[31.88,3.56],[31.25,3.78],[30.83,3.51]]],sources:{scale:"\u4EFB\u52A1\u4E8C A_\u9010\u5C4A\u89C4\u6A21\u4E0E\u96C6\u4E2D\u5EA6.csv",female:"\u4EFB\u52A1\u4E8C C_\u5973\u6027\u53C2\u4E0E\u83B7\u5956\u4E0E\u5C0F\u9879.csv",delegation:"\u4EFB\u52A1\u4E8C B_\u5341\u4E8C\u4EE3\u8868\u56E2\u9010\u5C4A\u4EFD\u989D.csv",sport:"\u4EFB\u52A1\u4E8C D_\u4EE3\u8868\u9879\u76EE\u51FA\u73B0\u77E9\u9635.csv",map:"world-atlas 2.0.2 / Natural Earth 110m"},note:"\u4E3E\u529E\u57CE\u5E02\u5750\u6807\u4E3A\u57CE\u5E02\u4E2D\u5FC3\u7684\u793A\u610F\u5B9A\u4F4D\uFF0C\u4E0D\u4EE3\u8868\u5177\u4F53\u573A\u9986\u6216\u8FD0\u52A8\u5458\u6765\u6E90\uFF1B1956\u9A6C\u672F\u53E6\u5728\u65AF\u5FB7\u54E5\u5C14\u6469\u4E3E\u884C\uFF0C\u4E3B\u6807\u8BB0\u91C7\u7528\u58A8\u5C14\u672C\u3002"};var Xe=i=>document.getElementById(i),Al=matchMedia("(prefers-reduced-motion: reduce)").matches,fn=Lt.editions.map(i=>i.year),Je={index:fn.length-1,noc:"CHN",sport:"Skateboarding",timer:null},_i="#adc4cb",H2="#ffffff19",Ha="#77cee8",Wa="#f1c478",Sl=window.echarts,Xa={scale:Sl.init(Xe("scale-chart")),country:Sl.init(Xe("country-chart")),sport:Sl.init(Xe("sport-chart"))},zh=i=>Number(i).toLocaleString("zh-CN");for(let[i,e]of Object.entries(Lt.nocNames)){let t=document.createElement("option");t.value=i,t.textContent=e,Xe("country-select").append(t)}Xe("country-select").value=Je.noc;for(let i of Lt.sportSeries){let e=document.createElement("option");e.value=i.key,e.textContent=i.name,Xe("sport-select").append(e)}Xe("sport-select").value=Je.sport;var Vs={animationDuration:Al?0:650,textStyle:{fontFamily:"Microsoft YaHei, sans-serif",color:_i},tooltip:{trigger:"axis",backgroundColor:"#102c39",borderColor:"#688592",textStyle:{color:"#f4f4ee"},extraCssText:"border-radius:10px;box-shadow:0 15px 35px #0007"}},Ml=(i=8)=>({color:_i,interval:Math.max(0,Math.ceil(fn.length/(innerWidth<760?4:i))-1)}),bl={lineStyle:{color:"#48636f"}},El={lineStyle:{color:H2}},Tl=i=>({silent:!0,symbol:"none",lineStyle:{color:Wa,width:1.5,type:"dashed",opacity:.85},label:{show:!1},data:[{xAxis:String(i)}]});function wl(){let i=Lt.editions[Je.index];Xa.scale.setOption({...Vs,grid:{left:54,right:52,top:28,bottom:35,containLabel:!0},legend:{top:0,right:8,textStyle:{color:_i,fontSize:11}},xAxis:{type:"category",data:fn.map(String),boundaryGap:!1,axisLabel:Ml(),axisLine:bl},yAxis:[{type:"value",axisLabel:{color:_i,formatter:o=>o>=1e3?`${o/1e3}\u5343`:o},splitLine:El},{type:"value",axisLabel:{color:_i},splitLine:{show:!1}}],series:[{name:"\u53C2\u8D5B\u884C\u6570",type:"line",smooth:.18,showSymbol:!1,lineStyle:{color:Ha,width:3},itemStyle:{color:Ha},areaStyle:{color:"#77cee814"},markLine:Tl(i.year),data:Lt.editions.map(o=>o.records)},{name:"\u4EE3\u8868\u56E2",type:"line",yAxisIndex:1,smooth:.18,showSymbol:!1,lineStyle:{color:Wa,width:3},itemStyle:{color:Wa},data:Lt.editions.map(o=>o.delegations)}]});let e=Lt.delegationSeries[Je.noc],t=new Map(e.map(o=>[o.year,o])),n=fn.map(o=>t.get(o)?.present?t.get(o).medalShare:null);Xa.country.setOption({...Vs,grid:{left:54,right:19,top:20,bottom:38,containLabel:!0},xAxis:{type:"category",data:fn.map(String),boundaryGap:!1,axisLabel:Ml(6),axisLine:bl},yAxis:{type:"value",min:0,axisLabel:{color:_i,formatter:"{value}%"},splitLine:El},tooltip:{...Vs.tooltip,formatter:o=>{let l=+o[0]?.axisValue,c=t.get(l);return`${l} \u5E74 \xB7 ${Lt.nocNames[Je.noc]}<br>${c?.present?`\u83B7\u5956\u884C\u4EFD\u989D <b>${c.medalShare}%</b>`:"\u672A\u53C2\u8D5B\u6216\u65E0\u53EF\u7528\u8BB0\u5F55"}`}},series:[{type:"line",data:n,connectNulls:!1,showSymbol:!1,smooth:.12,lineStyle:{color:Ha,width:3},itemStyle:{color:Ha},areaStyle:{color:"#77cee813"},markLine:Tl(i.year)}]});let s=t.get(i.year);Xe("country-readout").textContent=`${i.year} \xB7 ${Lt.nocNames[Je.noc]}\uFF1A${s?.present&&s.medalShare!==null?`\u83B7\u5956\u884C\u4EFD\u989D ${s.medalShare}%`:"\u7F3A\u5E2D\u6216\u65E0\u53EF\u7528\u8BB0\u5F55"}`;let r=Lt.sportSeries.find(o=>o.key===Je.sport);Xa.sport.setOption({...Vs,grid:{left:35,right:18,top:21,bottom:38,containLabel:!0},xAxis:{type:"category",data:fn.map(String),axisLabel:Ml(6),axisLine:bl},yAxis:{type:"value",min:0,max:1,interval:1,axisLabel:{color:_i,formatter:o=>o===1?"\u51FA\u73B0":"\u672A\u51FA\u73B0"},splitLine:El},tooltip:{...Vs.tooltip,formatter:o=>`${o[0].axisValue} \u5E74 \xB7 ${r.name}<br>${o[0].value?"\u51FA\u73B0\u4E8E\u672C\u5C4A\u9879\u76EE\u8868":"\u672A\u51FA\u73B0\u4E8E\u672C\u5C4A\u9879\u76EE\u8868"}`},series:[{type:"bar",barMaxWidth:17,data:r.present.map((o,l)=>({value:o,itemStyle:{color:l===Je.index?Wa:"#69bcd5",opacity:o?1:.05,borderRadius:[3,3,0,0]}})),markLine:Tl(i.year)}]});let a=r.present.reduce((o,l,c)=>(l&&o.push(fn[c]),o),[]);Xe("sport-readout").textContent=`${i.year} \xB7 ${r.name}\uFF1A${r.present[Je.index]?"\u51FA\u73B0":"\u672A\u51FA\u73B0"}\uFF1B\u6837\u672C 30 \u5C4A\u4E2D\u51FA\u73B0 ${a.length} \u5C4A\u3002`}var kh=null;function gi(i,e,t=1){let n=(90-i)*Math.PI/180,s=(e+180)*Math.PI/180;return new U(-t*Math.sin(n)*Math.cos(s),t*Math.cos(n),t*Math.sin(n)*Math.sin(s))}function W2(){let i=Xe("globe"),e=new us,t=new Ut(42,1,.1,100);t.position.set(0,.2,4.3);let n=new Ba({antialias:!0,alpha:!0,powerPreference:"high-performance"});n.setPixelRatio(Math.min(devicePixelRatio,1.7)),n.setSize(i.clientWidth,i.clientHeight),n.outputColorSpace=Nt,i.appendChild(n.domElement);let s=new Va(t,n.domElement);s.enablePan=!1,s.enableDamping=!Al,s.dampingFactor=.065,s.minDistance=2.8,s.maxDistance=6,s.rotateSpeed=.65,e.add(new As(7444906,1.1));let r=new Ts(13166832,2);r.position.set(3,2,4),e.add(r);let a=new wn;e.add(a);let o=new Ot(new hi(1,64,48),new vs({color:1193798,emissive:335916,specular:4293786,shininess:35}));a.add(o);let l=new Ot(new hi(1.12,48,32),new tn({transparent:!0,depthWrite:!1,side:Tt,uniforms:{glowColor:{value:new Be(5948638)}},vertexShader:"varying vec3 vNormal;varying vec3 vWorld;void main(){vNormal=normalize(normalMatrix*normal);vec4 world=modelMatrix*vec4(position,1.0);vWorld=world.xyz;gl_Position=projectionMatrix*viewMatrix*world;}",fragmentShader:"varying vec3 vNormal;varying vec3 vWorld;uniform vec3 glowColor;void main(){float a=pow(1.0-abs(dot(normalize(vNormal),normalize(cameraPosition-vWorld))),2.5);gl_FragColor=vec4(glowColor,a*.25);}"}));a.add(l);let c=[];for(let f of Lt.geography)for(let v=1;v<f.length;v++){let N=gi(f[v-1][1],f[v-1][0],1.009),I=gi(f[v][1],f[v][0],1.009);N.distanceTo(I)<.17&&c.push(...N.toArray(),...I.toArray())}let h=new kt;h.setAttribute("position",new ct(c,3)),a.add(new ps(h,new ci({color:7517885,transparent:!0,opacity:.72})));for(let f=-60;f<=60;f+=30){let v=[];for(let N=-180;N<=180;N+=4)v.push(gi(f,N,1.005));a.add(new ki(new kt().setFromPoints(v),new ci({color:7908796,transparent:!0,opacity:.13})))}let g=[];Lt.editions.forEach((f,v)=>{let N=gi(f.lat,f.lon,1.055),I=new li({color:v===Je.index?15910004:7919079,transparent:!0,opacity:v===Je.index?1:.73}),D=new Ot(new hi(v===Je.index?.027:.015,12,8),I);D.position.copy(N),D.userData.index=v,a.add(D),g.push(D)});let d=new Ot(new ys(.039,.046,48),new li({color:15910004,transparent:!0,opacity:.85,side:nn,depthWrite:!1}));a.add(d);let m=new ws,_=new Re,S=-1;function p(f){let v=i.getBoundingClientRect();_.set((f.clientX-v.left)/v.width*2-1,-(f.clientY-v.top)/v.height*2+1),m.setFromCamera(_,t);let N=m.intersectObjects([o,...g],!1);return N[0]?.object===o?-1:N[0]?.object?.userData?.index??-1}i.addEventListener("pointermove",f=>{S=p(f);let v=Xe("globe-tooltip");if(S>=0){let N=Lt.editions[S];v.textContent=`${N.year} \xB7 ${N.city}`,v.hidden=!1,v.style.left=`${Math.min(i.clientWidth-90,Math.max(90,f.offsetX))}px`,v.style.top=`${Math.max(25,f.offsetY-47)}px`}else v.hidden=!0}),i.addEventListener("pointerleave",()=>{Xe("globe-tooltip").hidden=!0,S=-1});let u=null;i.addEventListener("pointerdown",f=>{u=[f.clientX,f.clientY]}),i.addEventListener("pointerup",f=>{u&&Math.hypot(f.clientX-u[0],f.clientY-u[1])<5&&S>=0&&xi(S),u=null});let M=0;function w(f){let v=Lt.editions[f],N=gi(v.lat,v.lon);M=-Math.atan2(N.x,N.z);let I=a.rotation.y;for(;M-I>Math.PI;)M-=2*Math.PI;for(;M-I<-Math.PI;)M+=2*Math.PI;g.forEach((D,z)=>{D.material.color.setHex(z===f?15910004:7919079),D.material.opacity=z===f?1:.73,D.scale.setScalar(z===f?1.8:1)}),d.position.copy(gi(v.lat,v.lon,1.065)),d.quaternion.setFromUnitVectors(new U(0,0,1),gi(v.lat,v.lon).normalize())}let E=()=>{let f=i.clientWidth,v=i.clientHeight;f&&v&&(t.aspect=f/v,t.updateProjectionMatrix(),n.setSize(f,v))};new ResizeObserver(E).observe(i),E(),w(Je.index);let A=new Rs;function T(){if(requestAnimationFrame(T),document.hidden)return;let f=A.getElapsedTime();Al?a.rotation.y=M:(a.rotation.y+=(M-a.rotation.y)*.055,d.scale.setScalar(1+.23*Math.sin(f*2.7)),d.material.opacity=.55+.35*Math.sin(f*2.7)),s.update(),n.render(e,t)}return T(),{focus:w,resize:E}}try{kh=W2()}catch(i){console.warn("WebGL unavailable:",i),Xe("globe-fallback").hidden=!1}function xi(i){Je.index=Math.max(0,Math.min(fn.length-1,i));let e=Lt.editions[Je.index];Xe("year-label").textContent=e.year,Xe("city-label").textContent=e.city,Xe("edition-note").textContent=`\u7B2C ${Je.index+1} \u4E2A\u6570\u636E\u5C4A\u6B21 \xB7 \u590F\u5B63\u5965\u8FD0`,Xe("records-value").textContent=zh(e.records),Xe("delegations-value").textContent=zh(e.delegations),Xe("female-value").textContent=e.female.toFixed(1)+"%",Xe("coordinate-label").textContent=`${Math.abs(e.lat).toFixed(2)}\xB0 ${e.lat>=0?"N":"S"} \xB7 ${Math.abs(e.lon).toFixed(2)}\xB0 ${e.lon>=0?"E":"W"}`,Xe("year-slider").value=Je.index,Xe("year-slider").style.setProperty("--pct",`${Je.index/(fn.length-1)*100}%`),Xe("dock-year").textContent=`${e.year} ${e.city}`,Xe("progress").textContent=`${Je.index+1} / ${fn.length}`,kh?.focus(Je.index),wl()}Xe("previous").addEventListener("click",()=>xi(Je.index-1));Xe("next").addEventListener("click",()=>xi(Je.index+1));Xe("year-slider").addEventListener("input",i=>xi(+i.target.value));Xe("country-select").addEventListener("change",i=>{Je.noc=i.target.value,wl()});Xe("sport-select").addEventListener("change",i=>{Je.sport=i.target.value,wl()});Xe("play").addEventListener("click",()=>{if(Je.timer){clearInterval(Je.timer),Je.timer=null,Xe("play").textContent="\u64AD\u653E\u5386\u5C4A \u25C9",Xe("play").setAttribute("aria-pressed","false");return}xi(0),Xe("play").textContent="\u6682\u505C \u2161",Xe("play").setAttribute("aria-pressed","true"),Je.timer=setInterval(()=>{if(Je.index===fn.length-1){Xe("play").click();return}xi(Je.index+1)},1100)});addEventListener("resize",()=>Object.values(Xa).forEach(i=>i.resize()));xi(Je.index);})();
/*! Bundled license information:

three/build/three.core.js:
three/build/three.module.js:
  (**
   * @license
   * Copyright 2010-2026 Three.js Authors
   * SPDX-License-Identifier: MIT
   *)
*/
