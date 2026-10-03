#!/usr/bin/env python3
"""Offline portability/package checks; not visual QA or legal clearance."""
from pathlib import Path
import ast
import json
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
errors = []
checks = 0


def check(condition, label):
    global checks
    checks += 1
    if not condition:
        errors.append(label)


required = ['SKILL.md', 'README.md', 'README.zh-CN.md', 'LICENSE', 'VERSION',
            'THIRD_PARTY_NOTICES.md', 'CONTRIBUTING.md', 'examples/showcase.md',
            'agents/openai.yaml', 'assets/visual-library/RIGHTS.md']
for name in required:
    check((ROOT / name).is_file(), 'required file: ' + name)

skill = (ROOT / 'SKILL.md').read_text()
check(skill.startswith('---\nname: systems-figure-studio\n'), 'skill identity')
check('$systems-figure-studio' in (ROOT / 'agents/openai.yaml').read_text(), 'invocation')
check(bool(re.fullmatch(r'\d+\.\d+\.\d+\n?', (ROOT / 'VERSION').read_text())), 'release version')

suffixes = {'.md', '.json', '.yaml', '.yml', '.py', '.html', '.txt', '.svg', '.drawio'}
for path in ROOT.rglob('*'):
    rel = path.relative_to(ROOT)
    if any(part in {'.git', '.venv', '__pycache__', 'dist'} for part in rel.parts):
        continue
    if not path.is_file() or path.suffix not in suffixes:
        continue
    text = path.read_text(encoding='utf-8')
    # Build literals in parts so this checker does not match itself.
    private = re.search('/' + r'Users/[^/\s]+/|/' + r'tmp/|file' + r'://', text)
    check(not private, 'no machine-local paths: ' + str(rel))
    legacy = 'jh-' + 'systems-paper-fig'
    check(legacy not in text, 'current naming: ' + str(rel))
    if path.suffix == '.py':
        try:
            ast.parse(text)
        except SyntaxError:
            check(False, 'Python syntax: ' + str(rel))
    if path.suffix == '.json':
        try:
            json.loads(text)
        except ValueError:
            check(False, 'JSON syntax: ' + str(rel))
    if path.suffix in {'.svg', '.drawio'}:
        try:
            tree = ET.fromstring(text)
            for node in tree.iter():
                for key, value in node.attrib.items():
                    if key.rsplit('}', 1)[-1] in {'href', 'src'}:
                        if value.startswith(('data:', '#', 'http://', 'https://')):
                            continue
                        check((path.parent / value).is_file(), 'asset dependency: ' + str(rel))
        except ET.ParseError:
            check(False, 'XML syntax: ' + str(rel))

base = ROOT / 'assets/visual-library'
for record in json.loads((base / 'catalog.json').read_text())['items']:
    check((base / record['file']).is_file(), 'asset exists: ' + record['id'])
    check(bool(record.get('status')), 'asset status: ' + record['id'])
    if record.get('source'):
        check((base / record['source']).is_file(), 'asset source: ' + record['id'])

print(json.dumps({'passed': not errors, 'checks': checks, 'errors': errors}, indent=2))
sys.exit(bool(errors))
