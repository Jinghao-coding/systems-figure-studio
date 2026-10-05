import json
import sys
import tempfile
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog_model import ROOT,read_json
from evaluate_behavior import fixtures_errors,score

class BehaviorFixtures(unittest.TestCase):
    def test_fixed_inputs_complete(self):self.assertEqual(fixtures_errors(read_json(ROOT/'evaluations/behavior-cases.json')),[])
    def test_no_execution_is_not_run(self):
        cases=read_json(ROOT/'evaluations/behavior-cases.json')
        self.assertTrue(all(r['status']=='not_run' for r in score(cases,{},ROOT)))
    def test_self_report_without_trace_fails(self):
        self.assertEqual(score([{'id':'a','expected':{'drawing_calls':0}}],{'a':{'observed':{'drawing_calls':0}}},ROOT)[0]['status'],'failed')
    def test_constraint_failure(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d);(p/'trace.json').write_text('[]')
            self.assertEqual(score([{'id':'a','expected':{'drawing_calls':0}}],{'a':{'trace':'trace.json','observed':{'drawing_calls':1}}},p)[0]['status'],'failed')
