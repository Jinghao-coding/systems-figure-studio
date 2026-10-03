#!/usr/bin/env python3
"""Validate package structure and current content; this is not a visual QA test."""
from pathlib import Path
import json,re,hashlib,sys
from urllib.parse import unquote
P=Path(__file__).resolve().parents[1]
def load(name):return json.loads((P/name).read_text(encoding='utf-8'))
errors=[];checks=[]
def check(ok,msg):
    checks.append({'check':msg,'passed':bool(ok)})
    if not ok:errors.append(msg)
idx=load('catalog/index.json');stats=load('catalog/statistics.json');topics=load('catalog/topics.json');sources=load('catalog/sources.json');migration=load('catalog/migration.json')
ids=[t['id'] for t in idx];source_ids={s['id'] for s in sources}
check(len(ids)==len(set(ids)),'unique current term IDs')
check(len(topics)==stats['theme_count'],'theme count matches')
check(len(idx)==stats['term_count'],'term count matches')
check(sum(x['variant_count'] for x in idx)==stats['variant_count'],'variant count matches')
check(len(migration)==52 and all(x in ids for x in migration),'all 52 legacy IDs mapped into current topics')
check(sum(x['origin'] in ['original_or_adapted_candidate','added_v0.4.1'] for x in idx)==stats['new_non_agent_terms'],'cumulative added non-Agent term count matches')
check(sum(x['variant_count'] for x in idx if x['origin'] in ['original_or_adapted_candidate','added_v0.4.1'])==stats['new_non_agent_variants'],'cumulative added non-Agent variants match')
check(all(x['image_status']=='not_generated' for x in idx),'no text recipe falsely marked as generated')
check(len([s for s in sources if s['record_origin']=='new_v0.4' and s['review_status']=='visually_reviewed'])==7,'7 inherited v0.4 visual sources kept separate')
for meta in topics:
    check(all(i in ids for i in meta.get('related_ids',[])),f'cross-topic IDs exist: {meta["id"]}')
check(sum(x['origin']=='added_v0.4.1' for x in idx)==stats['added_in_this_revision']['terms'],'latest term delta matches')
check(sum(x['variant_count'] for x in idx if x['origin']=='added_v0.4.1')==stats['added_in_this_revision']['variants'],'latest variant delta matches')
for t in idx:
    fp=P/t['path']; check(fp.exists(),f"term file exists: {t['id']}")
    if fp.exists():check(f'id="{t["anchor"]}"' in fp.read_text(),f"term anchor exists: {t['id']}")
    check(all(s in source_ids for s in t['refs']),f"source IDs exist: {t['id']}")
# Local Markdown links and explicit anchors. Ignore remote URLs and pure illustrative placeholders.
for p in P.rglob('*.md'):
    txt=p.read_text(encoding='utf-8')
    for dest in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',txt):
        if re.match(r'(?:https?://|mailto:)',dest):continue
        path,_,anchor=dest.partition('#'); fp=(p.parent/unquote(path)).resolve() if path else p
        check(fp.exists(),f'local link: {p.relative_to(P)} → {dest}')
        if anchor and fp.exists() and fp.suffix=='.md':
            body=fp.read_text();explicit=f'id="{anchor}"' in body
            check(explicit,f'explicit local anchor: {p.relative_to(P)} → {dest}')
# No obsolete secondary entrypoint or duplicated legacy prompt library.
for obsolete in ['catalog/elements.json','prompts/element-prompts.md','visual-reference-atlas.html','UPDATE-0.3-DRAFT.md']:
    check(not (P/obsolete).exists(),f'obsolete runtime file absent: {obsolete}')
for p in (P/'topics').glob('*.md'):
    txt=p.read_text()
    for bad in ['一律禁止使用icon','一律禁用机器人','不用机器人头像','不使用速度仪表盘图标','采用局部结构而非服务器图标']:
        check(bad not in txt,f'no obsolete icon ban: {p.name} / {bad}')
    check('---BEGIN PROMPT---' not in txt and '{VISIBLE_TEXT_RULE}' not in txt,f'no unfinished prompt scaffolding: {p.name}')
# The two approved Agent recipe bodies must match the versions saved during migration.
for fn,rec in load('catalog/agent-preservation.json').items():
    txt=(P/'topics'/fn).read_text();body=txt[txt.index('## '):]
    check(hashlib.sha256(body.encode()).hexdigest()==rec['written_body_hash'],f'approved Agent body preserved: {fn}')
html=(P/'guide.html').read_text()
match=re.search(r'<script type="application/json" id="payload">(.*?)</script>',html,re.S)
check(match is not None,'offline guide has embedded payload')
if match:
    d=json.loads(match.group(1));check(len(d['terms'])==len(idx),'offline guide matches term count')
    check(sum(len(t['variants']) for t in d['terms'])==stats['variant_count'],'offline guide matches variants')
    check(all(v['description'].strip() for t in d['terms'] for v in t['variants']),'no empty descriptions')
    check(all(len(t['variants'])>=1 for t in d['terms']),'every term has a concrete drawing construction')
check((P/'SKILL.md').exists() and (P/'references/knowledge-base.md').exists() and load('catalog/import.json')['source_version']=='0.4.1', 'single skill entry and source provenance present')
report={'passed':not errors,'checks':len(checks),'failed':errors,'scope':'structure, local links, source IDs, counts, Agent preservation, latest-rule consistency; not visual approval','details':checks}
(P/'catalog/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='details'},ensure_ascii=False,indent=2))
sys.exit(0 if not errors else 1)
