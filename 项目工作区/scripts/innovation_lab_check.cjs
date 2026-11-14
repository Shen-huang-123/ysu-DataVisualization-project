const fs=require('fs'),path=require('path'),vm=require('vm');
const root=path.resolve(__dirname,'../..');
function read(rel){return fs.readFileSync(path.join(root,rel),'utf8')}
const lens=read('交付文件/任务三_专题深挖/S2_口径的魔力/07_口径实验室/index.html');
const survival=read('交付文件/任务三_专题深挖/S3_冠军的保质期/07_王朝生存图/index.html');
const score=read('交付文件/任务四_开放创作/06_赛后验收单/index.html');
function jsonBetween(text,a,b){let i=text.indexOf(a);if(i<0)throw Error('missing '+a);i+=a.length;let j=text.indexOf(b,i);if(j<0)throw Error('missing '+b);return JSON.parse(text.slice(i,j))}
const delegations=jsonBetween(lens,'const DATA=',', SPORTS=');
const streaks=jsonBetween(survival,'const DATA=',',$=');
const forecasts=jsonBetween(score,'const P=',',D=');
const demo=jsonBetween(score,',D=',',$=');
if(delegations.length!==91||streaks.length!==3833||forecasts.length!==127||demo.length!==117)throw Error('embedded data counts changed');
const ned=delegations.find(x=>x.code==='NED');
if(ned.official!==15||ned.rows!==67)throw Error('NED lens values changed');
const start=score.indexOf('function csvRows(text){'),end=score.indexOf('function ranks(data,key){',start);
if(start<0||end<0)throw Error('CSV parser missing');
const parser=vm.runInNewContext(score.slice(start,end)+';csvRows');
const rows=parser('NOC,Gold,Silver,Bronze\n"USA",46,44,43\nCHN,40,27,24');
if(rows.length!==3||rows[1][0]!=='USA'||rows[2][3]!=='24')throw Error('CSV parser failed');
const sample=parser('NOC,Gold,Silver,Bronze\n"C,1",1,2,3');
if(sample[1][0]!=='C,1')throw Error('quoted CSV parser failed');
console.log(JSON.stringify({passed:true,delegations:delegations.length,streaks:streaks.length,forecasts:forecasts.length,demo:demo.length,csvParser:'passed'}));
