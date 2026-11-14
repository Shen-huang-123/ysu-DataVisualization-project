/** Build a small offline evidence bundle for the spatial Olympic presentation. */
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '../..');
const out = path.join(root, '交付文件/任务四_开放创作/08_奥运时空剧场');
const {feature} = require(path.join(out,'node_modules/topojson-client'));
const atlas = require(path.join(out,'node_modules/world-atlas/countries-110m.json'));

function csv(relative) {
  const lines = fs.readFileSync(path.join(root,relative),'utf8').replace(/^\uFEFF/,'').trim().split(/\r?\n/);
  const headers=lines.shift().split(',');
  return lines.map(line=>Object.fromEntries(line.split(',').map((value,i)=>[headers[i],value])));
}
const scale=csv('交付文件/任务二_百年全景/02_数据表/A_逐届规模与集中度.csv');
const female=new Map(csv('交付文件/任务二_百年全景/02_数据表/C_女性参与获奖与小项.csv').map(x=>[+(x.Year||x['']),x]));
const delegations=csv('交付文件/任务二_百年全景/02_数据表/B_十二代表团逐届份额.csv');
const sports=csv('交付文件/任务二_百年全景/02_数据表/D_代表项目出现矩阵.csv');

const hosts={
  1896:['雅典',37.98,23.73],1900:['巴黎',48.86,2.35],1904:['圣路易斯',38.63,-90.20],1908:['伦敦',51.51,-0.13],1912:['斯德哥尔摩',59.33,18.07],
  1920:['安特卫普',51.22,4.40],1924:['巴黎',48.86,2.35],1928:['阿姆斯特丹',52.37,4.90],1932:['洛杉矶',34.05,-118.24],1936:['柏林',52.52,13.40],
  1948:['伦敦',51.51,-0.13],1952:['赫尔辛基',60.17,24.94],1956:['墨尔本',-37.81,144.96],1960:['罗马',41.90,12.50],1964:['东京',35.68,139.69],
  1968:['墨西哥城',19.43,-99.13],1972:['慕尼黑',48.14,11.58],1976:['蒙特利尔',45.50,-73.57],1980:['莫斯科',55.75,37.62],1984:['洛杉矶',34.05,-118.24],
  1988:['首尔',37.56,126.98],1992:['巴塞罗那',41.38,2.17],1996:['亚特兰大',33.75,-84.39],2000:['悉尼',-33.87,151.21],2004:['雅典',37.98,23.73],
  2008:['北京',39.90,116.40],2012:['伦敦',51.51,-0.13],2016:['里约热内卢',-22.91,-43.20],2020:['东京',35.68,139.69],2024:['巴黎',48.86,2.35]
};
const editions=scale.map(x=>{
  const year=+x.Year, f=female.get(year), host=hosts[year];
  if(!host||!f)throw Error('Missing source for '+year);
  return {year,city:host[0],lat:host[1],lon:host[2],records:+x.participation_records,delegations:+x.delegations,
    female:+(100*(+f.participation_share)).toFixed(1),medalRecords:+x.medal_records};
});
if(editions.length!==30)throw Error('Expected 30 official Summer Olympic editions');
const nocNames={USA:'美国',CHN:'中国',GBR:'英国',JPN:'日本',AUS:'澳大利亚',FRA:'法国',GER:'德国',FRG:'西德',GDR:'东德',URS:'苏联',KOR:'韩国',NED:'荷兰'};
const delegationSeries={};
for(const row of delegations){
  if(!delegationSeries[row.NOC])delegationSeries[row.NOC]=[];
  delegationSeries[row.NOC].push({year:+row.Year,present:row.present==='True',medalShare:row.medal_share?+(100*+row.medal_share).toFixed(2):null});
}
const sportNames={'Tug-Of-War':'拔河','Croquet':'槌球','Art Competitions':'艺术竞赛','Polo':'马球','Figure Skating':'花样滑冰','Ice Hockey':'冰球','Taekwondo':'跆拳道','Triathlon':'铁人三项','Rugby':'橄榄球','Skateboarding':'滑板','Surfing':'冲浪','Sport Climbing':'运动攀岩','Breaking':'霹雳舞'};
const sportSeries=sports.map(row=>({key:row.sport_family,name:sportNames[row.sport_family]||row.sport_family,
  present:editions.map(e=>+row[e.year]||0)}));
const geography=feature(atlas,atlas.objects.countries).features.flatMap(country=>{
  const g=country.geometry;
  return g.type==='Polygon'?[g.coordinates[0]]:g.type==='MultiPolygon'?g.coordinates.map(poly=>poly[0]):[];
}).map(ring=>ring.map(([lon,lat])=>[+lon.toFixed(2),+lat.toFixed(2)]))
 .filter(ring=>ring.length>=3);
const data={editions,delegationSeries,nocNames,sportSeries,geography,
  sources:{scale:'任务二 A_逐届规模与集中度.csv',female:'任务二 C_女性参与获奖与小项.csv',delegation:'任务二 B_十二代表团逐届份额.csv',sport:'任务二 D_代表项目出现矩阵.csv',map:'world-atlas 2.0.2 / Natural Earth 110m'},
  note:'举办城市坐标为城市中心的示意定位，不代表具体场馆或运动员来源；1956马术另在斯德哥尔摩举行，主标记采用墨尔本。'};
fs.mkdirSync(path.join(out,'src'),{recursive:true});
fs.writeFileSync(path.join(out,'src/data.json'),JSON.stringify(data));
console.log(`Built ${editions.length} editions, ${Object.keys(delegationSeries).length} delegations, ${sportSeries.length} sports, ${geography.length} map rings.`);
