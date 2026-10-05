#!/usr/bin/env python3
"""Prepare a local static bundle; never publish or modify hosting settings."""
import argparse
from pathlib import Path
import shutil
from catalog_model import ROOT
from rebuild_navigation import build


def prepare(destination):
    destination = Path(destination).resolve()
    if destination == ROOT.resolve() or ROOT.resolve() in destination.parents:
        raise ValueError("Use a temporary output directory outside the maintained repository.")
    destination.mkdir(parents=True,exist_ok=False)
    for folder in ['topics','references','examples','assets','catalog','templates','evaluations']:
        shutil.copytree(ROOT/folder,destination/folder,dirs_exist_ok=True,ignore=shutil.ignore_patterns('validation.json'))
    for name in ['README.md','README.zh-CN.md','SKILL.md','LICENSE','THIRD_PARTY_NOTICES.md','CONTRIBUTING.md','RELEASE_CHECKLIST.md','CHANGELOG.md','VERSION']:
        shutil.copy2(ROOT/name,destination/name)
    for name,text in build().items():
        out=destination/name;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(text,encoding='utf-8')
    (destination/'index.html').write_text((destination/'guide.html').read_text(),encoding='utf-8')
    (destination/'.nojekyll').write_text('')
    print('Prepared static files in '+str(destination))

if __name__=='__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True, help='New temporary directory outside the repository')
    prepare(parser.parse_args().output)
