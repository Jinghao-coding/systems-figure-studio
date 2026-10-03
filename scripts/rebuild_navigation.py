#!/usr/bin/env python3
"""Rebuild navigation and the offline text guide from authoritative topic Markdown.
Python 3.10+, standard library only. Does not access the network or generate images.
"""
from pathlib import Path
import re, json, html, collections
ROOT=Path(__file__).resolve().parents[1]

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def field(text,name):
    m=re.search(r'\*\*'+re.escape(name)+r'：\*\*\s*(.*?)(?=\n|$)',text)
    return m.group(1).strip() if m else ''

def parse_topics():
    meta=read_json(ROOT/'catalog/topics.json')
    old={x['id']:x for x in read_json(ROOT/'catalog/index.json')}
    terms=[]
    for topic in meta:
        path=ROOT/topic['path']
        text=path.read_text(encoding='utf-8')
        chunks=re.split(r'<a id="([\w-]+)"></a>\s*',text)
        for i in range(1,len(chunks),2):
            id,body=chunks[i],chunks[i+1]
            title=re.search(r'^## (.+)$',body,re.M).group(1)
            variants=[]
            for m in re.finditer(r'^### (.+)\n+([\s\S]*?)(?=^### |^\*\*参考与取舍：|\Z)',body,re.M):
                variants.append(dict(name=m.group(1).strip(),description=m.group(2).strip()))
            refs=re.findall(r'\[([A-Z]+\d+)\]\(\.\./references/sourcebook\.md#',body)
            aliases=field(body,'词汇与别名').split('、')
            terms.append(dict(id=id,title=title,topic=topic['id'],topic_title=topic['title'],path=topic['path'],anchor=id,
                aliases=aliases,meaning=field(body,'含义'),variants=variants,guard=field(body,'必要边界'),
                take=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',field(body,'参考与取舍')),refs=refs,
                recipe_status='description_ready',image_status='not_generated',origin=old.get(id,{}).get('origin','added_in_topic')))
    return meta,terms

HTML=r'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Systems Figure Studio · 画法知识库</title>
<style>
:root{--ink:#203244;--muted:#687887;--line:#dce3e8;--bg:#fbfcfd;--accent:#285c79;--wash:#eef4f7}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.7 system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
header{padding:34px 5vw 24px;background:white;border-bottom:1px solid var(--line)}.eyebrow{font-size:12px;letter-spacing:.18em;color:var(--accent)}h1{font-size:32px;line-height:1.25;margin:10px 0 12px;font-weight:670}header p{max-width:960px;margin:0;color:var(--muted)}.stat{font-size:13px;margin-top:17px;color:var(--accent)}
.layout{display:grid;grid-template-columns:235px minmax(0,1fr);gap:32px;max-width:1340px;margin:28px auto;padding:0 4vw 60px}aside{position:sticky;top:15px;align-self:start}aside button{display:block;width:100%;background:none;border:0;border-left:3px solid transparent;text-align:left;padding:9px 10px;margin:3px 0;color:var(--muted);font:inherit;cursor:pointer;line-height:1.45}aside button.active{border-color:var(--accent);background:var(--wash);color:var(--ink);font-weight:600}.number{float:right;color:var(--muted);font-size:12px}.aside-note{border-top:1px solid var(--line);padding:14px 8px;margin-top:20px;font-size:12px;color:var(--muted)}
.controls{display:flex;gap:10px;align-items:center;flex-wrap:wrap}label[for=q]{font-size:13px;color:var(--muted);width:100%}input{min-width:230px;flex:1;border:1px solid #bfcbd3;border-radius:5px;background:white;padding:11px 13px;font:inherit;color:var(--ink)}button:focus-visible,summary:focus-visible,input:focus-visible{outline:3px solid #a6c4d8;outline-offset:2px}.plain{border:1px solid var(--line);background:white;color:var(--accent);padding:8px 12px;border-radius:4px;cursor:pointer;font:inherit;font-size:13px}.result-meta{font-size:13px;color:var(--muted);margin:15px 0}.topic-desc{font-size:14px;color:var(--muted);margin:5px 0 20px}
details.term{background:white;border:1px solid var(--line);border-radius:5px;margin-bottom:10px;overflow:hidden}details.term[open]{border-color:#a7bdcb}summary{list-style:none;cursor:pointer;padding:15px 18px;display:flex;align-items:center;gap:12px}summary::-webkit-details-marker{display:none}summary:before{content:'＋';color:var(--accent);font-size:17px}details[open]>summary:before{content:'−'}summary strong{font-size:17px;font-weight:630;flex:1}.tag{font-size:11px;color:var(--muted);background:#f3f6f8;padding:2px 7px;border-radius:3px;white-space:nowrap}.body{border-top:1px solid var(--line);padding:18px 24px}.aliases{font-size:12px;color:var(--muted);margin:0 0 10px}.meaning{margin:4px 0 14px}.variant{border-left:2px solid #c9d9e2;padding:2px 0 2px 16px;margin:18px 0}.variant h3{font-size:15px;margin:0 0 7px;font-weight:650}.variant p{margin:0}.notes{background:#f8fafb;padding:12px 14px;font-size:13px;color:#556575;margin-top:18px}.notes p{margin:6px 0}.sources button{background:none;color:var(--accent);border:0;border-bottom:1px solid #bdced9;cursor:pointer;padding:0;margin:0 8px 0 0;font:inherit}.foot{display:flex;justify-content:space-between;align-items:center;gap:16px;margin-top:15px;font-size:12px;color:var(--muted)}.empty{border:1px dashed var(--line);padding:35px;text-align:center;color:var(--muted)}
.extra{background:white;border:1px solid var(--line);padding:20px;margin-bottom:16px}.extra h2{font-size:20px;margin-top:0}.extra pre{font:inherit;font-size:14px;line-height:1.9;white-space:pre-wrap;overflow-wrap:anywhere;margin:0;color:#33495a}.tabbar{display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap}.tabbar .selected{background:var(--accent);color:white;border-color:var(--accent)}dialog{width:min(800px,92vw);max-height:85vh;overflow:auto;border:1px solid var(--line);border-radius:8px;padding:28px;color:var(--ink)}dialog::backdrop{background:#16253570}.close{float:right}dialog h2{font-size:21px;margin:6px 0 16px}dialog p{font-size:14px}a{color:var(--accent);text-underline-offset:3px}.source-id{letter-spacing:.08em;font-size:12px;color:var(--muted)}.toast{position:fixed;bottom:20px;left:50%;transform:translateX(-50%);background:var(--ink);color:white;padding:9px 20px;border-radius:5px;display:none;font-size:13px}.small{font-size:12px;color:var(--muted)}footer{font-size:12px;color:var(--muted);text-align:center;padding:20px;border-top:1px solid var(--line)}
@media(max-width:820px){.layout{grid-template-columns:1fr;gap:18px}aside{position:static;display:flex;gap:4px;flex-wrap:wrap}aside button{width:auto;padding:5px 9px;border-left:0;border-bottom:2px solid transparent;font-size:12px}.number,.aside-note{display:none}h1{font-size:26px}.body{padding:14px}summary{padding:13px 11px}summary strong{font-size:15px}.tag{font-size:10px}}
@media print{aside,.controls,.tabbar,.plain,footer{display:none}.layout{display:block}details{break-inside:avoid}.body{display:block}header{padding:10px}dialog{display:none}}
</style></head><body>
<header><div class="eyebrow">SYSTEMS FIGURE STUDIO</div><h1>绘图词条与构造描述</h1><p>按研究主题找对象，比较不同形体、结构和组织方式。允许适量 icon；优先保持架构逻辑、整体协调与自然观感。这里是文字画法库，不是已生成图片图库。</p><div class="stat" id="stats"></div></header>
<div class="layout"><aside id="themes" aria-label="主题选择"></aside><main>
<div class="tabbar"><button class="plain selected" id="tab-main">词条目录</button><button class="plain" id="tab-agent">已保留的 Agent 内容</button><button class="plain" id="tab-guide">整图组合与使用规则</button></div>
<section id="main-view"><div class="controls"><label for="q">检索名称、别名或具体画法</label><input id="q" type="search" placeholder="例如：Cloud、CPU、GPU、存储、Logo、连接线…"><button class="plain" id="clear">清除</button><button class="plain" id="expand">展开本页</button></div><p class="result-meta" id="count" aria-live="polite"></p><p class="topic-desc" id="scope"></p><div id="list"></div></section>
<section id="extra-view" hidden></section>
</main></div><footer>主题 Markdown 为维护正文；本页为同版离线浏览快照。来源链接需要联网。未生成的描述不能视为通过视觉验收的图形。</footer>
<dialog id="source-dialog"><button class="plain close" id="close-source">关闭</button><div id="source-body"></div></dialog><div class="toast" id="toast" role="status"></div>
<script type="application/json" id="payload">__PAYLOAD__</script>
<script>
'use strict';
const D=JSON.parse(document.getElementById('payload').textContent), E=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let theme='all',currentTab='main';const $=s=>document.querySelector(s);
$('#stats').textContent=`${D.stats.theme_count} 个主题 · ${D.stats.term_count} 个主词条 · ${D.stats.variant_count} 种画法 · 含 Agent 扩展示例`;
function themeButtons(){let out='<button data-topic="all" class="'+(theme==='all'?'active':'')+'">全部主题<span class="number">'+D.terms.length+'</span></button>';
for(const t of D.topics){let n=D.terms.filter(x=>x.topic===t.id||(t.related_ids||[]).includes(x.id)).length;out+=`<button data-topic="${E(t.id)}" class="${theme===t.id?'active':''}" aria-pressed="${theme===t.id}">${E(t.title)}<span class="number">${n}</span></button>`;}
out+='<p class="aside-note">同义词共用词条，画法可按任务调整。数量、状态、连接与性能结论以实际研究为准。</p>';$('#themes').innerHTML=out;
$('#themes').querySelectorAll('button').forEach(b=>b.onclick=()=>{theme=b.dataset.topic;setTab('main');themeButtons();render();});}
function plainTerm(t){return `${t.title}\n${t.meaning}\n\n`+t.variants.map(v=>`${v.name}\n${v.description}`).join('\n\n')+`\n\n必要边界：${t.guard}\n参考与取舍：${t.take}\n状态：绘图描述可用，未生成示例图。`;}
function render(){let q=$('#q').value.toLowerCase().trim(),parts=q.split(/\s+/).filter(Boolean);const ts=D.terms.filter(t=>(theme==='all'||t.topic===theme||(D.topics.find(x=>x.id===theme)?.related_ids||[]).includes(t.id))&&parts.every(p=>(t.title+' '+t.id+' '+t.aliases.join(' ')+' '+t.meaning+' '+t.variants.map(v=>v.name+' '+v.description).join(' ')).toLowerCase().includes(p)));
$('#count').textContent=`找到 ${ts.length} 个词条；各条目可展开查看并复制。`;
$('#scope').textContent=theme==='all'?'优先读取与你当前问题有关的主题，避免将全部图元拼进同一张图。':D.topics.find(x=>x.id===theme).scope;
$('#list').innerHTML=ts.length?ts.map(t=>`<details class="term" id="term-${E(t.id)}" ${q?'open':''}><summary><strong>${E(t.title)}</strong><span class="tag">${E(t.topic_title)}</span><span class="tag">${t.variants.length} 种</span></summary><div class="body"><p class="aliases">${E(t.id)} · ${E(t.aliases.join(' / '))}</p><p class="meaning">${E(t.meaning)}</p>${t.variants.map(v=>`<div class="variant"><h3>${E(v.name)}</h3><p>${E(v.description)}</p></div>`).join('')}<div class="notes"><p><strong>必要边界：</strong>${E(t.guard)}</p><p><strong>参考与取舍：</strong>${E(t.take)}</p><p class="sources">${t.refs.map(id=>`<button data-source="${E(id)}">${E(id)}</button>`).join('')||'原创／通用构造，尚无专门原图'}</p></div><div class="foot"><span>描述可用 · 示例图未生成</span><button class="plain" data-copy="${E(t.id)}">复制词条描述</button></div></div></details>`).join(''):'<p class="empty">没有匹配词条。可以改用对象名称、英文别名或更宽的主题。</p>';
$('#list').querySelectorAll('[data-source]').forEach(b=>b.onclick=()=>source(b.dataset.source));$('#list').querySelectorAll('[data-copy]').forEach(b=>b.onclick=()=>copy(plainTerm(D.terms.find(t=>t.id===b.dataset.copy))));}
function source(id){const s=D.sources.find(x=>x.id===id);if(!s)return;let inherited=s.record_origin!=='new_v0.4.1';$('#source-body').innerHTML=`<div class="source-id">${E(s.id)} · ${s.review_status==='visually_reviewed'?'图面已审':'技术文本依据，未核图面'} · ${inherited?'继承记录':'本轮记录'}</div><h2>${E(s.title)}</h2><p>${E(s.venue)}<br>${E(s.version)}<br>${E(s.figure)} · PDF 页：${E(s.pdf_pages||s.pdf_page||'未记录')}</p><p><strong>观察／依据：</strong>${E(s.observation)}</p><p><strong>保留：</strong>${E(s.retain)}</p><p><strong>取舍：</strong>${E(s.avoid)}</p><p><a href="${E(s.url)}" target="_blank" rel="noopener noreferrer">打开原始来源</a>${s.image_url?' · <a href="'+E(s.image_url)+'" target="_blank" rel="noopener noreferrer">原图入口</a>':''}</p><p class="small">原图审阅不等于改编图已生成；本页面没有将原图提交给生图工具。</p>`;$('#source-dialog').showModal();}
async function copy(text){try{if(navigator.clipboard&&window.isSecureContext){await navigator.clipboard.writeText(text);}else{const ta=document.createElement('textarea');ta.value=text;document.body.appendChild(ta);ta.select();if(!document.execCommand('copy'))throw Error('copy');ta.remove();}toast('已复制词条描述');}catch(e){toast('浏览器未允许复制，可手动选择正文。');}}
function toast(s){$('#toast').textContent=s;$('#toast').style.display='block';setTimeout(()=>$('#toast').style.display='none',2200);}
function setTab(which){currentTab=which;$('#main-view').hidden=which!=='main';$('#extra-view').hidden=which==='main';for(const a of ['main','agent','guide'])$('#tab-'+a).classList.toggle('selected',a===which);if(which!=='main'){let docs=which==='agent'?D.agent_docs:D.guide_docs;$('#extra-view').innerHTML=docs.map(d=>`<article class="extra"><h2>${E(d.title)}</h2><pre>${E(d.text)}</pre></article>`).join('');}}
$('#q').oninput=render;$('#clear').onclick=()=>{$('#q').value='';render();};$('#expand').onclick=()=>$('#list').querySelectorAll('details').forEach(d=>d.open=true);$('#close-source').onclick=()=>$('#source-dialog').close();$('#source-dialog').onclick=e=>{if(e.target===$('#source-dialog'))$('#source-dialog').close();};for(const a of ['main','agent','guide'])$('#tab-'+a).onclick=()=>setTab(a);
themeButtons();render();
</script></body></html>'''

def main():
    meta,terms=parse_topics()
    index=[]
    for t in terms:
        index.append({k:t[k] for k in ['id','title','topic','aliases','path','anchor','refs','recipe_status','image_status','origin']}|{'variant_count':len(t['variants'])})
    (ROOT/'catalog/index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2),encoding='utf-8')
    stats=read_json(ROOT/'catalog/statistics.json')
    stats.update(term_count=len(terms),variant_count=sum(len(t['variants']) for t in terms),theme_count=len(meta),counts_by_topic=dict(collections.Counter(t['topic'] for t in terms)))
    (ROOT/'catalog/statistics.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
    agent_docs=[dict(title='Agent 样板：身份、结构与组合',text=(ROOT/'topics/agents-approved-samples.md').read_text()),dict(title='九种 Agent / Multi-agent 参考改编',text=(ROOT/'topics/agents-arxiv-patterns.md').read_text())]
    guide_docs=[dict(title='Framework Studio 方法取舍',text=(ROOT/'references/framework-studio-ideas.md').read_text()),dict(title='配色方案',text=(ROOT/'references/visual-system.md').read_text()),dict(title='构图与比较',text=(ROOT/'references/figure-grammars.md').read_text()),dict(title='figures4papers 图例与取舍',text=(ROOT/'references/figures4papers-ideas.md').read_text()),dict(title='Cloud、Logo 与整图组合',text=(ROOT/'references/cloud-logo-composition.md').read_text()),dict(title='跨主题组合',text=(ROOT/'examples/combined-recipes.md').read_text()),dict(title='统一视觉规则',text=(ROOT/'references/visual-quality.md').read_text())]
    data=dict(terms=terms,topics=meta,stats=stats,sources=read_json(ROOT/'catalog/sources.json'),agent_docs=agent_docs,guide_docs=guide_docs)
    payload=json.dumps(data,ensure_ascii=False).replace('</','<\\/')
    (ROOT/'guide.html').write_text(HTML.replace('__PAYLOAD__',payload),encoding='utf-8')
    print(json.dumps({'terms':len(terms),'variants':stats['variant_count'],'guide_bytes':(ROOT/'guide.html').stat().st_size},ensure_ascii=False))
if __name__=='__main__':main()
