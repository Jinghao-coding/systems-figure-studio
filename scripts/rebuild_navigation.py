#!/usr/bin/env python3
"""Deterministic, offline rebuild. Python 3.10+, standard library only."""
from pathlib import Path
import json
import sys
from catalog_model import ROOT, CatalogError, read_json, parse_topics, statistics

GENERATED = ['catalog/index.json','catalog/statistics.json','catalog/browser.json','guide.html']

def dump(value): return json.dumps(value,ensure_ascii=False,indent=2)+'\n'
def safe_payload(value):
    return json.dumps(value,ensure_ascii=False).replace('&','\\u0026').replace('<','\\u003c').replace('>','\\u003e').replace('\u2028','\\u2028').replace('\u2029','\\u2029')

def build(root=ROOT):
    topics,terms=parse_topics(root)
    cases=read_json(root/'examples/cases.json')
    stats=statistics(topics,terms,root)
    docs=[]
    paths=[('agent-samples','Agent 扩展','topics/agents-approved-samples.md'),('agent-patterns','Agent 扩展','topics/agents-arxiv-patterns.md')]
    for p in sorted((root/'references').glob('*.md')):
        paths.append(('rule-'+p.stem,'使用规则',str(p.relative_to(root))))
    paths.append(('combinations','组合案例','examples/combined-recipes.md'))
    for id,type,path in paths:
        text=(root/path).read_text(encoding='utf-8')
        docs.append(dict(id=id,type=type,path=path,title=text.splitlines()[0].lstrip('# '),text=text,topics=['agent'] if type=='Agent 扩展' else []))
    for c in cases:
        docs.append(dict(c,type='完整案例',text=(root/c['path']).read_text(encoding='utf-8')))
    data=dict(terms=terms,topics=topics,stats=stats,sources=read_json(root/'catalog/sources.json'),docs=docs,cases=cases,
              assets=read_json(root/'assets/visual-library/catalog.json')['items'])
    index=[{k:t[k] for k in ['id','title','topic','aliases','path','anchor','refs','recipe_status','origin']}|
           {'variant_count':len(t['variants']),'variant_ids':[v['id'] for v in t['variants']]} for t in terms]
    template=(root/'scripts/web/guide.html').read_text()
    page=template.replace('__CSS__',(root/'scripts/web/guide.css').read_text()).replace('__JS__',(root/'scripts/web/guide.js').read_text()).replace('__PAYLOAD__',safe_payload(data))
    return dict(zip(GENERATED,[dump(index),dump(stats),dump(data),page]))

def main():
    try:
        outputs=build()
        for name,text in outputs.items():(ROOT/name).write_text(text,encoding='utf-8')
        print(json.dumps({'generated':list(outputs),'statistics':read_json(ROOT/'catalog/statistics.json')},ensure_ascii=False))
        return 0
    except (CatalogError,ValueError,OSError,KeyError) as exc:
        print(str(exc),file=sys.stderr);return 1
if __name__=='__main__':sys.exit(main())
