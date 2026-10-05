/* No dependencies; shared functions are also exercised by node:test. */
(function(root){
'use strict';
const E=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function safeURL(url,base=''){
 let u=String(url).trim();
 if(/[\u0000-\u0020\u007f\\]/.test(u)||u.startsWith('//'))return '';
 if(/^[a-z][a-z\d+.-]*:/i.test(u))return /^https?:\/\//i.test(u)?u:'';
 // Decode once to reject encoded protocols and controls, too.
 try{const dec=decodeURIComponent(u);if(/[\u0000-\u0020\u007f\\]/.test(dec)||/^[a-z][a-z\d+.-]*:/i.test(dec)||dec.startsWith('//'))return '';}catch(e){return '';}
 if(!base)return u;
 const path=base.split('/').slice(0,-1);
 if(u.startsWith('#'))return base+u;
 for(const part of u.split('/')){if(part==='..')path.pop();else if(part!=='.')path.push(part);}
 return path.join('/');
}
function inline(text,base){
 const out=[];let pos=0;
 const regex=/(`[^`]+`)|\[([^\]\n]+)\]\(([^)\n]+)\)/g;
 for(const m of text.matchAll(regex)){
  out.push(E(text.slice(pos,m.index)));
  if(m[1])out.push('<code>'+E(m[1].slice(1,-1))+'</code>');
  else{const url=safeURL(m[3],base);out.push(url?'<a href="'+E(url)+'" rel="noopener noreferrer">'+E(m[2])+'</a>':E(m[2]));}
  pos=m.index+m[0].length;
 }
 out.push(E(text.slice(pos)));return out.join('').replace(/\*\*([^*]+)\*\*/g,'<strong>$1</strong>');
}
function markdown(text,base=''){
 let out=[],code=null,list=false,table=false;
 const close=()=>{if(list){out.push('</ul>');list=false;}if(table){out.push('</tbody></table>');table=false;}};
 for(const line of text.split('\n')){
  if(/^```/.test(line)){close();if(code!==null){out.push('<pre><code>'+E(code.join('\n'))+'</code></pre>');code=null;}else code=[];continue;}
  if(code!==null){code.push(line);continue;}
  if(/^\s*<a id="[\w-]+"><\/a>\s*$/.test(line)){continue;}
  let m=line.match(/^(#{1,6})\s+(.+)$/);
  if(m){close();const n=Math.min(6,m[1].length+1);out.push(`<h${n}>${inline(m[2],base)}</h${n}>`);}
  else if(/^\s*(?:[-*]|\d+\.)\s+/.test(line)){if(table)close();if(!list){out.push('<ul>');list=true;}out.push('<li>'+inline(line.replace(/^\s*(?:[-*]|\d+\.)\s+/,''),base)+'</li>');}
  else if(line.startsWith('|')){if(list)close();if(/^\|[\s:|\-]+\|?$/.test(line))continue;if(!table){out.push('<table><tbody>');table=true;}out.push('<tr>'+line.replace(/^\||\|$/g,'').split('|').map(v=>'<td>'+inline(v.trim(),base)+'</td>').join('')+'</tr>');}
  else{close();if(line.trim())out.push('<p>'+inline(line,base)+'</p>');}
 }
 close();if(code!==null)out.push('<pre><code>'+E(code.join('\n'))+'</code></pre>');return out.join('\n');
}
function variantBrief(t,v){return [['Object role',v.level||'Unreviewed; determine from target material'],['Construction',`${v.name} [${v.id}]`],['Description',v.description],['Connect',v.connect||'Determine actual endpoint from target material'],['Use',v.suitable||'Unreviewed'],['Avoid',v.unsuitable||'Unreviewed'],['Boundary',t.guard],['Sources',t.refs.join(', ')],['Cases',v.cases.join(', ')||'No example']].map(([k,v])=>k+': '+v).join('\n');}
function combine(pairs){return 'Selection notes; alternatives are not automatically compatible. Resolve roles and conflicts against target material.\n\n'+pairs.map(([t,v])=>variantBrief(t,v)).join('\n\n');}
function eligible(a){return a.final_use==='eligible'&&!/reference|truncated|superseded|error/.test(a.legacy_status||a.status||'');}
function matches(value,q){return q.toLocaleLowerCase().trim().split(/\s+/).filter(Boolean).every(p=>value.toLocaleLowerCase().includes(p));}
const api={E,safeURL,markdown,variantBrief,combine,eligible,matches};
if(typeof module!=='undefined')module.exports=api;
root.SFS=api;
if(typeof document==='undefined')return;
const D=JSON.parse(document.querySelector('#payload').textContent), $=s=>document.querySelector(s);
let selection=new Set(), state={topic:'all',q:'',term:'',variant:'',doc:''};
const findVariant=id=>{for(const t of D.terms){const v=t.variants.find(v=>v.id===id);if(v)return [t,v];}return null;};
function link(fields){return '#'+new URLSearchParams({...state,...fields}).toString();}
function readState(){const h=location.hash.slice(1);const p=new URLSearchParams(h);for(const key of Object.keys(state))state[key]=p.get(key)|| (key==='topic'?'all':'');if(h&&!h.includes('=')){state.term=h.replace(/^term-/,'');}if(!D.topics.some(t=>t.id===state.topic))state.topic='all';$('#q').value=state.q;$('#topic').value=state.topic;}
function writeState(){history.replaceState(null,'',link({}));}
function copy(text){$('#export').hidden=false;$('#copytext').value=text;$('#copytext').focus();$('#copytext').select();const promise=navigator.clipboard&&window.isSecureContext?navigator.clipboard.writeText(text):Promise.resolve(document.execCommand('copy'));promise.then(()=>$('#notice').textContent='内容已准备，可复制或保存。').catch(()=>$('#notice').textContent='复制受限，请选择文本后手动复制。');}
function variant(t,v){return `<section class="variant" id="${E(v.id)}"><h3><a href="${E(link({term:t.id,variant:v.id,doc:''}))}">${E(v.name)}</a> <small>变体</small></h3>${markdown(v.description,t.path)}<p>${E(v.level||'选择元数据尚未审阅')} · ${E(v.suitable||'适用问题待结合目标材料判断')}</p><p>连接：${E(v.connect||'需从目标材料确定端点')}</p><p>不适用：${E(v.unsuitable||'尚未专门审阅')}</p><p>${v.cases.length?v.cases.map(id=>{const c=D.cases.find(c=>c.id===id);return `<a href="${E(link({doc:id,term:'',variant:'',q:'',topic:'all'}))}">${E(c?.title||id)}</a>`;}).join(' · '):'无完整示例'}</p><button class="plain" data-variant="${E(v.id)}">复制此画法</button> <label><input type="checkbox" data-select="${E(v.id)}" ${selection.has(v.id)?'checked':''}>加入组合</label></section>`;}
function render(){
 const ts=D.terms.filter(t=>(state.topic==='all'||t.topic===state.topic||(D.topics.find(x=>x.id===state.topic)?.related_ids||[]).includes(t.id))&&matches(JSON.stringify(t),state.q));
 const docs=D.docs.filter(d=>(state.topic==='all'||(d.topics||[]).includes(state.topic))&&matches(d.title+' '+d.text+' '+d.type,state.q));
 $('#count').textContent=`${ts.length} 个词条（含变体） · ${docs.length} 个扩展 / 案例 / 规则`;
 $('#list').innerHTML=ts.map(t=>`<details class="term" id="term-${E(t.id)}" ${state.q||state.term===t.id?'open':''}><summary><strong>${E(t.title)}</strong><span class="tag">词条 · ${E(t.topic_title)}</span></summary><div class="body"><p>${E(t.aliases.join(' / '))}</p><p>${E(t.meaning)}</p>${t.variants.map(v=>variant(t,v)).join('')}<div class="notes">必要边界：${E(t.guard)}<p>来源：${t.refs.map(id=>`<button class="plain" data-source="${E(id)}">${E(id)}</button>`).join('')}</p>文字画法：description-ready；案例检查见各案例记录。<p>关联素材：${D.assets.filter(a=>(a.term_ids||[]).includes(t.id)).map(a=>`<a href="${E(safeURL('assets/visual-library/'+a.file))}">${E(a.id)}</a> (${E(a.final_use)})`).join(' · ')||'无关联素材'}</p></div><div class="foot"><a href="${E(link({term:t.id,variant:'',doc:''}))}">定位此词条</a><button class="plain" data-term="${E(t.id)}">复制整个词条</button></div></div></details>`).join('');
 $('#docs').innerHTML=docs.map(d=>`<details class="card" id="doc-${E(d.id)}" ${state.doc===d.id?'open':''}><summary><strong>${E(d.title)}</strong><span class="tag">${E(d.type)}</span></summary><a href="${E(link({doc:d.id,term:'',variant:''}))}">定位</a><div class="doc-body">${markdown(d.text,d.path)}</div>${d.preview?`<img loading="lazy" src="${E(safeURL(d.preview))}" alt="${E(d.title)} preview"><p><a href="${E(safeURL(d.source))}">权威源文件</a> · <a href="${E(safeURL(d.path))}">制作及检查记录</a></p>`:''}${(d.variants||[]).map(id=>{const pair=findVariant(id);return pair?`<a href="${E(link({term:pair[0].id,variant:id,doc:'',q:'',topic:'all'}))}">${E(pair[1].name)}</a> · `:'';}).join('')}</details>`).join('');
 if(!ts.length&&!docs.length)$('#list').innerHTML='<p class="empty">没有匹配结果。尝试英文术语、中文名称，或清除主题筛选。</p>';
 document.querySelectorAll('[data-variant]').forEach(b=>b.onclick=()=>copy(variantBrief(...findVariant(b.dataset.variant))));
 document.querySelectorAll('[data-term]').forEach(b=>b.onclick=()=>{const t=D.terms.find(t=>t.id===b.dataset.term);copy(t.title+'\n'+t.meaning+'\n\n'+t.variants.map(v=>variantBrief(t,v)).join('\n\n'));});
 document.querySelectorAll('[data-select]').forEach(c=>c.onchange=()=>{if(c.checked&&selection.size>=8){c.checked=false;$('#notice').textContent='每次最多组合 8 个变体。';return;}c.checked?selection.add(c.dataset.select):selection.delete(c.dataset.select);updateSelection();});
 document.querySelectorAll('[data-source]').forEach(b=>b.onclick=()=>{const s=D.sources.find(s=>s.id===b.dataset.source);if(!s)return;$('#source-body').innerHTML='<h2>'+E(s.title)+'</h2>'+markdown([s.review_status,s.figure,s.observation,s.retain,s.avoid].filter(Boolean).join('\n\n'))+`<a href="${E(safeURL(s.url))}" rel="noopener noreferrer">来源</a>`;$('#source-dialog').showModal();});
}
function updateSelection(){$('#selected').textContent=[...selection].map(id=>findVariant(id)[1].name).join(' / ')||'尚未选择变体';}
function focusTarget(){const target=state.variant|| (state.term?'term-'+state.term:state.doc?'doc-'+state.doc:'');const el=document.getElementById(target);if(el){el.closest('details')?.setAttribute('open','');el.scrollIntoView({block:'center'});el.setAttribute('tabindex','-1');el.focus({preventScroll:true});}}
$('#topic').innerHTML='<option value="all">全部主题</option>'+D.topics.map(t=>`<option value="${E(t.id)}">${E(t.title)}</option>`).join('');
$('#stats').textContent=`${D.stats.theme_count} 主题 · ${D.stats.term_count} 词条 · ${D.stats.variant_count} 画法 · ${D.stats.worked_example_count} 完整案例${D.stats.worked_example_count?'':'（当前没有登记的完整案例）'}`;
$('#q').oninput=()=>{state.q=$('#q').value;state.term=state.variant=state.doc='';writeState();render();};
$('#topic').onchange=()=>{state.topic=$('#topic').value;writeState();render();};
$('#clear').onclick=()=>{state={topic:'all',q:'',term:'',variant:'',doc:''};writeState();readState();render();};
$('#combine').onclick=()=>selection.size?copy(combine([...selection].map(findVariant))):$('#notice').textContent='请先选择变体。';
$('#clear-selection').onclick=()=>{selection.clear();updateSelection();render();};
$('#close-source').onclick=()=>$('#source-dialog').close();
$('#asset-list').innerHTML=D.assets.map(a=>`<li><a href="${E(safeURL('assets/visual-library/'+a.file))}">${E(a.id)}</a> — <span class="status">${E(a.final_use)} / ${E(a.legacy_status||a.status)}</span>；视觉：${E(a.visual_review)}；当前接受：${E(a.user_acceptance)}</li>`).join('');
$('#asset-count').textContent=`默认可选最终素材 ${D.assets.filter(eligible).length}；其余保留为需审阅或参考素材。`;
window.addEventListener('hashchange',()=>{readState();render();focusTarget();});readState();render();updateSelection();focusTarget();
})(typeof globalThis!=='undefined'?globalThis:this);
