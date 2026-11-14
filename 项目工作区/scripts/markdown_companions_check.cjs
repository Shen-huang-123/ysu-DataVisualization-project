const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../../交付文件');
function walk(d){return fs.readdirSync(d,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(d,e.name)):(e.name.endsWith('.md')?[path.join(d,e.name)]:[]))}
const files=walk(root),broken=[];
for(const md of files){const file=md.slice(0,-3)+'.html',source=fs.readFileSync(file,'utf8');for(const match of source.matchAll(/(?:href|src)="([^"]+)"/g)){const ref=match[1];if(/^(https?:|mailto:|#|data:)/.test(ref))continue;const target=path.resolve(path.dirname(file),decodeURI(ref.split('#')[0]));if(!fs.existsSync(target))broken.push([path.relative(root,file),ref])}}
console.log(JSON.stringify({documents:files.length,broken},null,2));if(broken.length)process.exit(1);
