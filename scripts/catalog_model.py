"""Maintained Markdown + independent metadata; no generated input dependencies."""
from pathlib import Path
import json
import re
import collections

ROOT = Path(__file__).resolve().parents[1]

class CatalogError(ValueError):
    pass

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def field(text, name):
    match = re.search(r'\*\*' + re.escape(name) + r'：\*\*\s*(.*?)(?=\n|$)', text)
    return match.group(1).strip() if match else ''

def parse_document(text, path, topic, registry, provenance):
    terms = []
    chunks = list(re.finditer(r'<a id="([\w-]+)"></a>\s*', text))
    for i, chunk in enumerate(chunks):
        ident = chunk.group(1)
        body = text[chunk.end():chunks[i+1].start() if i+1 < len(chunks) else len(text)]
        line = text[:chunk.start()].count('\n') + 1
        def fail(message):
            raise CatalogError(f'{path}:{line}\nterm: {ident}\nerror: {message}')
        title = re.search(r'^## (.+)$', body, re.M)
        if not title:
            fail('missing level-2 title')
        for name in ('词条 ID', '词汇与别名', '含义', '必要边界'):
            if not field(body, name):
                fail('missing field: ' + name)
        if field(body, '词条 ID').strip('` ') != ident:
            fail('term ID differs from anchor')
        variants = []
        for m in re.finditer(r'^### (.+)\n+([\s\S]*?)(?=^### |^\*\*参考与取舍：|\Z)', body, re.M):
            heading, description = m.group(1).strip(), m.group(2).strip()
            candidates = [v for v in registry if v['term_id'] == ident and v['heading'] == heading]
            if len(candidates) != 1:
                fail(f'variant {heading}: expected one registry entry, got {len(candidates)}')
            if not description:
                fail(f'variant {heading}: empty description')
            variants.append(dict(candidates[0], name=heading, description=description))
        if not variants:
            fail('missing level-3 variant')
        if ident not in provenance:
            fail('missing independent term provenance')
        refs = re.findall(r'\[([A-Z]+\d+)\]\(\.\./references/sourcebook\.md#', body)
        terms.append(dict(id=ident, title=title.group(1), topic=topic['id'], topic_title=topic['title'],
                          path=str(path), anchor=ident, aliases=field(body,'词汇与别名').split('、'),
                          meaning=field(body,'含义'), variants=variants, guard=field(body,'必要边界'),
                          take=re.sub(r'\[([^]]+)\]\([^)]+\)',r'\1',field(body,'参考与取舍')),
                          refs=refs, recipe_status='description_ready', origin=provenance[ident]['origin']))
    if not terms:
        raise CatalogError(f'{path}:1\nerror: no explicit term anchors')
    return terms

def parse_topics(root=ROOT):
    topics = read_json(root/'catalog/topics.json')
    registry = read_json(root/'catalog/variants.json')
    provenance = read_json(root/'catalog/term-provenance.json')
    vids = [v['id'] for v in registry]
    if len(vids) != len(set(vids)):
        raise CatalogError('catalog/variants.json: duplicate variant ID')
    terms = []
    for topic in topics:
        terms.extend(parse_document((root/topic['path']).read_text(encoding='utf-8'), topic['path'], topic, registry, provenance))
    ids = [t['id'] for t in terms]
    if len(ids) != len(set(ids)):
        raise CatalogError('topics: duplicate term ID')
    if {v['id'] for t in terms for v in t['variants']} != set(vids):
        raise CatalogError('catalog/variants.json: orphaned variant selector')
    return topics, terms

def statistics(topics, terms, root=ROOT):
    return dict(package_version=(root/'VERSION').read_text().strip(),
                knowledge_base_version=(root/'catalog/source-version.txt').read_text().strip(),
                term_count=len(terms), variant_count=sum(len(t['variants']) for t in terms),
                theme_count=len(topics), counts_by_topic=dict(collections.Counter(t['topic'] for t in terms)),
                source_count=len(read_json(root/'catalog/sources.json')),
                worked_example_count=len(read_json(root/'examples/cases.json')))

def final_assets(items):
    return [a for a in items if a.get('final_use') == 'eligible'
            and not any(x in a.get('legacy_status', a.get('status','')) for x in ('reference','truncated','superseded','error'))]

def variant_brief(term, variant):
    fields = [('Object role', variant.get('level','Unreviewed; determine from target material')),
              ('Construction', variant['name']+' ['+variant['id']+']'),
              ('Description', variant['description']), ('Connect', variant.get('connect','Determine actual endpoint from target material')),
              ('Use',variant.get('suitable','Unreviewed')),('Avoid',variant.get('unsuitable','Unreviewed')),
              ('Boundary',term['guard']), ('Sources',', '.join(term['refs'])),
              ('Cases',', '.join(variant.get('cases',[])) or 'No example')]
    return '\n'.join(k+': '+v for k,v in fields)

def combination_brief(pairs):
    return 'Selection notes; alternatives are not automatically compatible. Resolve roles and conflicts against target material.\n\n' + '\n\n'.join(variant_brief(t,v) for t,v in pairs)
