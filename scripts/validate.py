#!/usr/bin/env python3
"""Current catalog, links, artifacts and deterministic generated-content checks."""
import json
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import unquote
from catalog_model import ROOT, CatalogError, read_json, parse_topics
from rebuild_navigation import build


def link_errors(root):
    errors=[]
    for p in root.rglob('*.md'):
        if any(x in {'.git','.venv','node_modules','dist','__pycache__'} for x in p.relative_to(root).parts):continue
        text=p.read_text(encoding='utf-8')
        # Fenced examples contain syntax templates, not actual links.
        text=re.sub(r'```[^\n]*\n[\s\S]*?```','',text)
        for dest in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',text):
            if re.match(r'(?:https?://|mailto:)',dest):continue
            path,_,anchor=dest.partition('#');fp=(p.parent/unquote(path)).resolve() if path else p
            if not fp.exists():errors.append(f'{p.relative_to(root)}: missing local link {dest}');continue
            if anchor and fp.suffix=='.md':
                body=fp.read_text(encoding='utf-8')
                headings=[re.sub(r'[^\w\- ]','',h.lower()).replace(' ','-') for h in re.findall(r'^#+ (.+)$',body,re.M)]
                if f'id="{unquote(anchor)}"' not in body and unquote(anchor) not in headings:
                    errors.append(f'{p.relative_to(root)}: missing anchor {dest}')
    return errors


def source_errors(terms,sources):
    ids=[s['id'] for s in sources];errors=[]
    if len(ids)!=len(set(ids)):errors.append('duplicate source ID')
    for t in terms:
        for id in t['refs']:
            if id not in ids:errors.append(f'{t["path"]}: term {t["id"]}: missing source {id}')
    return errors


def artifact_errors(root):
    errors=[]
    items=read_json(root/'assets/visual-library/catalog.json')['items'];ids=[]
    for a in items:
        ids.append(a['id'])
        if a.get('final_use') not in {'reference_only','review_required','eligible','superseded','truncated'}:
            errors.append('invalid final_use: '+a['id'])
        for field in ['generation_record','source_review','visual_review','user_acceptance']:
            if not a.get(field):errors.append('missing '+field+': '+a['id'])
        for field in ['file','source']:
            if a.get(field) and not (root/'assets/visual-library'/a[field]).is_file():errors.append('missing asset '+a[field])
    if len(ids)!=len(set(ids)):errors.append('duplicate asset ID')
    for p in (root/'assets').rglob('*.svg'):
        try:
            doc=ET.parse(p)
            for e in doc.iter():
                for k,v in e.attrib.items():
                    if k.rsplit('}',1)[-1] in {'href','src'} and not v.startswith(('data:','#','http://','https://')):
                        if not (p.parent/unquote(v)).exists():errors.append('missing SVG dependency: '+str(p.relative_to(root)))
        except ET.ParseError as exc:errors.append(f'{p.relative_to(root)}: {exc}')
    return errors


def validate(root=ROOT):
    errors=[]
    try:
        topics,terms=parse_topics(root)
        sources=read_json(root/'catalog/sources.json');cases=read_json(root/'examples/cases.json')
        errors.extend(source_errors(terms,sources));errors.extend(link_errors(root));errors.extend(artifact_errors(root))
        ids={t['id'] for t in terms}
        for asset in read_json(root/'assets/visual-library/catalog.json')['items']:
            if not set(asset.get('term_ids',[])) <= ids:errors.append('invalid asset term links: '+asset['id'])
        case_ids=[c['id'] for c in cases]
        if len(case_ids)!=len(set(case_ids)):errors.append('duplicate case ID')
        variants={v['id']:v for t in terms for v in t['variants']}
        for topic in topics:
            if not set(topic.get('related_ids',[])) <= ids:errors.append('invalid related terms: '+topic['id'])
        for v in variants.values():
            for key in ['id','term_id','heading','selection_status','cases']:
                if key not in v:errors.append('variant missing '+key+': '+v['id'])
            if v.get('selection_status','').startswith('reviewed'):
                for key in ['suitable','unsuitable','level','connect','boundary_source']:
                    if not v.get(key):errors.append('reviewed variant missing '+key+': '+v['id'])
            for path in v.get('scenario_inputs',[]):
                if not (root/path).exists():errors.append('missing scenario: '+path)
            for cid in v['cases']:
                c=next((c for c in cases if c['id']==cid),None)
                if not c or v['id'] not in c['variants']:errors.append('invalid reciprocal case: '+v['id']+' / '+cid)
        for c in cases:
            for key in ['path','preview','source','checks']:
                if not c.get(key) or not (root/c[key]).is_file():errors.append('missing case '+key+': '+c['id'])
            for vid in c['variants']:
                if vid not in variants or c['id'] not in variants[vid]['cases']:errors.append('invalid reciprocal variant: '+c['id'])
        for name,text in build(root).items():
            if not (root/name).exists() or (root/name).read_text(encoding='utf-8')!=text:errors.append('generated file missing or stale: '+name)
        for folder in ['topics','examples','assets']:
            for p in (root/folder).rglob('*'):
                if p.suffix not in {'.md','.txt'}:continue
                if re.search(r'---BEGIN PROMPT---|\{VISIBLE_TEXT_RULE\}',p.read_text(encoding='utf-8')):
                    errors.append('unfinished prompt placeholder: '+str(p.relative_to(root)))
    except (OSError,ValueError,KeyError,CatalogError) as exc:errors.append(str(exc))
    return errors

if __name__=='__main__':
    errors=validate();report={'passed':not errors,'failed':errors,'scope':'current structure, IDs, links, sources, metadata, asset dependencies and generated-content consistency'}
    (ROOT/'catalog/validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2));sys.exit(bool(errors))
