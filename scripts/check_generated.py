#!/usr/bin/env python3
"""Compare committed generated outputs with a deterministic in-memory rebuild."""
import sys
from catalog_model import ROOT
from rebuild_navigation import build
missing=[]
for name,text in build().items():
    if not (ROOT/name).is_file() or (ROOT/name).read_text(encoding='utf-8')!=text:missing.append(name)
print('Generated outputs match.' if not missing else 'Missing/stale: '+', '.join(missing))
sys.exit(bool(missing))
