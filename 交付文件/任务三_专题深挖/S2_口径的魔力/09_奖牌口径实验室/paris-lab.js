(() => {
  const {records, names} = window.parisEvidence;
  const get = id => document.getElementById(id);
  const label = code => names[code] || code;
  const escape = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const options = [...new Set(records.map(row => row[2]))].sort();
  const codes = [...new Set(records.map(row => row[1]))].sort();
  const sportNames = {Football:'足球','Water Polo':'水球',Athletics:'田径',Sailing:'帆船',Basketball:'篮球',Volleyball:'排球',Swimming:'游泳',Gymnastics:'体操',Cycling:'自行车',Canoeing:'皮划艇',Rowing:'赛艇',Fencing:'击剑',Shooting:'射击',Wrestling:'摔跤','Table Tennis':'乒乓球',Badminton:'羽毛球',Tennis:'网球',Judo:'柔道',Boxing:'拳击',Weightlifting:'举重',Archery:'射箭',Hockey:'曲棍球',Handball:'手球',Rugby:'橄榄球',Diving:'跳水',Taekwondo:'跆拳道',Golf:'高尔夫',Skateboarding:'滑板',Surfing:'冲浪','Sport Climbing':'攀岩',Triathlon:'铁人三项','Artistic Swimming':'花样游泳','Modern Pentathlon':'现代五项','Equestrianism':'马术',Equestrian:'马术',Breaking:'霹雳舞'};
  const sportName = sport => sportNames[sport] || sport;
  const method = ['官方小项','运动员获奖行'];
  const colors = ['金','银','铜'];
  const chart = get('rank-chart');
  const teams = get('teams');
  let selected = new Set(['ESP']);
  let sport = '';
  let points = [];

  get('exclude').innerHTML = '<option value="">全部运动</option>' + options.map(s => '<option value="' + escape(s) + '">排除' + escape(sportName(s)) + '</option>').join('');
  teams.innerHTML = codes.map(code => '<option value="' + code + '">' + escape(label(code)) + ' · ' + code + '</option>').join('');

  function calculate(excluded) {
    const totals = [new Map(), new Map()];
    for (const [lens, code, family, color, , count] of records) {
      if (family === excluded) continue;
      if (!totals[lens].has(code)) totals[lens].set(code, [0, 0, 0]);
      totals[lens].get(code)[color] += count;
    }
    return totals.map(values => {
      const ranks = new Map();
      const sorted = [...values].sort(([, a], [, b]) => b[0]-a[0] || b[1]-a[1] || b[2]-a[2]);
      let previous = '', rank = 0;
      sorted.forEach(([code, counts], index) => {
        const key = counts.join('/');
        if (key !== previous) rank = index + 1;
        ranks.set(code, rank);
        previous = key;
      });
      return ranks;
    });
  }

  const baseline = calculate('');
  const readRank = (map, code) => map.get(code) ?? '未上榜';
  const signed = n => n > 0 ? '+' + n : String(n);
  const coord = event => {
    const b = chart.getBoundingClientRect();
    return (event.clientX - b.left) / b.width * 480;
  };

  function drawRanks(current) {
    const order = get('lens').value;
    const plotted = codes.filter(code => current.every(map => map.has(code))).map(code => ({
      code, shift: current[0].get(code) - current[1].get(code)
    }));
    const extent = Math.max(1, ...plotted.map(row => Math.abs(row.shift)));
    plotted.sort((a,b) => order === 'shift' ? b.shift-a.shift : current[order].get(a.code)-current[order].get(b.code));
    points = plotted.map((row, index) => ({...row, x:240 + row.shift/extent*208, y:16 + index/Math.max(1,plotted.length-1)*173}));
    chart.innerHTML = '<path d="M240 10V195" stroke="currentColor" opacity=".35"/><text x="32" y="213">−'+extent+'</text><text x="240" y="213" text-anchor="middle">0</text><text x="448" y="213" text-anchor="end">+'+extent+'</text>' +
      points.slice().sort((a,b) => Number(selected.has(a.code))-Number(selected.has(b.code))).map(({code,x,y,shift}) =>
        '<circle class="'+(selected.has(code)?'selected':'')+'" data-code="'+code+'" cx="'+x+'" cy="'+y+'" r="'+(selected.has(code)?6:3.8)+'"><title>'+escape(label(code))+' '+signed(shift)+'</title></circle>').join('') +
      '<rect id="brush" y="9" height="188" fill="currentColor" opacity=".13" pointer-events="none" hidden/>';
    get('ranks').innerHTML = '<div class="scroll"><table><thead><tr><th>代表团</th><th>官方 原 → 当前</th><th>获奖行 原 → 当前</th><th>当前升幅</th></tr></thead><tbody>' +
      [...selected].map(code => '<tr><th scope="row">'+escape(label(code))+'</th>'+current.map((map,i)=>'<td>'+readRank(baseline[i],code)+' → '+readRank(map,code)+'</td>').join('')+'<td>'+(current.every(map=>map.has(code))?signed(current[0].get(code)-current[1].get(code)):'—')+'</td></tr>').join('')+'</tbody></table></div>';
    for (const option of teams.options) option.selected = selected.has(option.value);
  }

  function drawSports(active) {
    const groups = new Map([...selected].map(code => [code, new Map()]));
    for (const [lens,code,family,color,,count] of active) {
      if (color !== 0 || !groups.has(code)) continue;
      const group = groups.get(code);
      if (!group.has(family)) group.set(family, [0,0]);
      group.get(family)[lens] += count;
    }
    const max = Math.max(1,...[...groups.values()].flatMap(group=>[...group.values()].flat()));
    get('sports').innerHTML = [...groups].map(([code, group]) => '<section><h3>'+escape(label(code))+'</h3>'+
      ([...group].sort((a,b)=>Math.abs(b[1][1]-b[1][0])-Math.abs(a[1][1]-a[1][0])).map(([family, [off,raw]]) =>
        '<button class="sport" data-sport="'+escape(family)+'" aria-pressed="'+(sport===family)+'" type="button"><strong>'+escape(sportName(family))+' · 差额 '+signed(raw-off)+'</strong><span>'+off+' 枚小项金牌 / '+raw+' 条金牌记录</span><i style="width:'+off/max*100+'%"></i><i style="width:'+raw/max*100+'%"></i></button>').join('') || '<p>当前情景无金牌记录。</p>')+'</section>').join('');
  }

  function drawEvidence(active) {
    get('evidence-scope').textContent = [...selected].map(label).join('、') + (sport ? ' · '+sportName(sport) : ' · 全部运动');
    const filtered = active.filter(([,code,family])=>selected.has(code) && (!sport || family===sport));
    get('evidence').innerHTML = method.map((title,lens) => '<section><h3>'+title+'</h3><div class="scroll"><table><thead><tr><th>代表团 · 运动</th><th>小项或原始标签</th><th>奖牌 · 计数</th></tr></thead><tbody>'+
      filtered.filter(row=>row[0]===lens).map(([,code,family,color,event,count,url])=>{
        const link = /^https:\/\//.test(url) ? '<a href="'+escape(url)+'">'+escape(event)+'</a>' : escape(event);
        return '<tr><td>'+escape(label(code)+' · '+sportName(family))+'</td><td>'+link+'</td><td>'+colors[color]+' · '+count+'</td></tr>';
      }).join('')+'</tbody></table></div></section>').join('');
  }

  function render() {
    const excluded = get('exclude').value;
    const active = records.filter(row=>row[2]!==excluded);
    const current = excluded ? calculate(excluded) : baseline;
    get('scenario').textContent = (excluded ? '排除'+sportName(excluded) : '全部运动')+' · 全榜重算范围：官方 '+current[0].size+' 队，获奖行 '+current[1].size+' 队。当前选看 '+selected.size+' 队。';
    drawRanks(current);
    drawSports(active);
    drawEvidence(active);
  }

  let start = null;
  chart.addEventListener('pointerdown', event => {
    if (event.pointerType !== 'mouse' || event.button !== 0) return;
    start = {x:coord(event), code:event.target.dataset.code};
    chart.setPointerCapture(event.pointerId);
  });
  chart.addEventListener('pointermove', event => {
    if (!start) return;
    const rect = get('brush');
    const x = coord(event);
    rect.removeAttribute('hidden');
    rect.setAttribute('x',Math.min(x,start.x));
    rect.setAttribute('width',Math.abs(x-start.x));
  });
  chart.addEventListener('pointerup', event => {
    if (!start) return;
    const x = coord(event);
    if (Math.abs(x-start.x)>5) {
      const chosen = points.filter(p=>p.x>=Math.min(x,start.x) && p.x<=Math.max(x,start.x));
      if (chosen.length) selected = new Set(chosen.map(p=>p.code));
    } else if (start.code) {
      if (event.shiftKey) {
        if (selected.has(start.code) && selected.size>1) selected.delete(start.code);
        else selected.add(start.code);
      } else selected = new Set([start.code]);
    }
    start = null;
    render();
  });
  chart.addEventListener('pointercancel',()=>{start=null;get('brush').setAttribute('hidden','');});
  teams.addEventListener('change', () => {
    const next = [...teams.selectedOptions].map(option=>option.value);
    if (next.length) selected = new Set(next);
    render();
  });
  get('exclude').addEventListener('change',()=>{sport='';render();});
  get('lens').addEventListener('change',render);
  get('sports').addEventListener('click',event=>{
    const button=event.target.closest('[data-sport]');
    if (button) {
      sport=button.dataset.sport;
      drawSports(records.filter(row=>row[2]!==get('exclude').value));
      get('sports').querySelector('[aria-pressed="true"]')?.focus();
      drawEvidence(records.filter(row=>row[2]!==get('exclude').value));
    }
  });
  get('clear-sport').addEventListener('click',()=>{sport='';render();});
  get('reset').addEventListener('click',()=>{
    selected=new Set(['ESP']);sport='';get('exclude').value='';get('lens').value='shift';render();
  });
  render();
})();
