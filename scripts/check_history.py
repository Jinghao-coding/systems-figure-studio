#!/usr/bin/env python3
"""Historical compatibility and protected-body checks, separate from current statistics."""
import hashlib
import json
import sys
from catalog_model import ROOT, read_json, parse_topics

def validate_history(root=ROOT):
    errors=[]
    _,terms=parse_topics(root);ids={t['id']:t for t in terms}
    def check(ok,msg):
        if not ok:errors.append(msg)
    migration=read_json(root/'catalog/migration.json')
    check(len(migration)==52,'expected all 52 legacy compatibility mappings')
    for id,mapping in migration.items():
        check(id in ids and ids[id]['path']==mapping['path'] and ids[id]['anchor']==mapping['anchor'],'legacy link changed: '+id)
    for fn,record in read_json(root/'catalog/agent-preservation.json').items():
        text=(root/'topics'/fn).read_text(encoding='utf-8');start=text.find('## ')
        check(start>=0 and hashlib.sha256(text[start:].encode()).hexdigest()==record['written_body_hash'],'protected Agent body changed: '+fn)
    sources=read_json(root/'catalog/sources.json')
    check(len([s for s in sources if s['record_origin']=='new_v0.4' and s['review_status']=='visually_reviewed'])==7,'seven inherited visual-source records')
    history=read_json(root/'catalog/history.json')['inherited_statistics']
    check(history['version']=='0.4.1' and history['migrated_base_terms']==52,'inherited statistics provenance')
    check(read_json(root/'catalog/import.json')['source_version']=='0.4.1','source import version')
    for name in ['catalog/elements.json','prompts/element-prompts.md','visual-reference-atlas.html','UPDATE-0.3-DRAFT.md']:
        check(not (root/name).exists(),'obsolete secondary runtime: '+name)
    for p in (root/'topics').glob('*.md'):
        for ban in ['一律禁止使用icon','一律禁用机器人','不用机器人头像','不使用速度仪表盘图标','采用局部结构而非服务器图标']:
            check(ban not in p.read_text(encoding='utf-8'),'obsolete icon ban: '+p.name)
    return errors

if __name__=='__main__':
    errors=validate_history();print(json.dumps({'passed':not errors,'failed':errors,'scope':'legacy links, source inheritance and protected Agent bodies'},ensure_ascii=False,indent=2));sys.exit(bool(errors))
