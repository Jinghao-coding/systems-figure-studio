#!/usr/bin/env python3
"""Validate fixed evaluation inputs or score normalized actual execution evidence."""
import argparse
import json
from pathlib import Path
from catalog_model import ROOT, read_json


def fixtures_errors(cases):
    errors=[];ids=[]
    for c in cases:
        ids.append(c.get('id'))
        for key in ['id','request','material','expected','deterministic_method','agent_method','visual_method']:
            if not c.get(key):errors.append(str(c.get('id'))+': missing '+key)
    if len(ids)!=len(set(ids)):errors.append('duplicate evaluation ID')
    return errors


def score(cases,evidence,base):
    """Evidence must come from retained execution traces; this checks fields, not visual truth."""
    results=[]
    for c in cases:
        run=evidence.get(c['id'])
        if not run:results.append(dict(id=c['id'],status='not_run'));continue
        if not run.get('trace') or not (base/run['trace']).is_file():
            results.append(dict(id=c['id'],status='failed',reason='missing actual execution trace'));continue
        failed=[k for k,v in c['expected'].items() if run.get('observed',{}).get(k)!=v]
        results.append(dict(id=c['id'],status='failed' if failed else 'passed',failed_fields=failed,
                            scope='normalized trace constraints only',visual_status=run.get('visual_status','not_run')))
    return results


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--evidence',type=Path);args=p.parse_args()
    cases=read_json(ROOT/'evaluations/behavior-cases.json');errors=fixtures_errors(cases)
    result={'fixture_validation':'failed' if errors else 'passed','errors':errors,
            'agent_execution':'not_run','visual_evaluation':'not_run'}
    if args.evidence:
        result['results']=score(cases,read_json(args.evidence),args.evidence.parent)
        result['agent_execution']='external_evidence_provided; verify provenance separately'
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return bool(errors) or any(r['status']=='failed' for r in result.get('results',[]))
if __name__=='__main__':raise SystemExit(main())
