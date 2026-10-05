import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from catalog_model import ROOT, CatalogError, parse_document, parse_topics, read_json, final_assets, variant_brief, combination_brief
from rebuild_navigation import build, safe_payload, GENERATED
from validate import link_errors, source_errors, artifact_errors
from check_history import validate_history
from audit_vector_figure import audit_svg

TEXT='''<a id="example"></a>
## 示例 Example
**词条 ID：** `example`
**词汇与别名：** 示例、sample
**含义：** Input and output 输入输出。
### One construction
A native shape with a label.
**参考与取舍：** [R01](../references/sourcebook.md#r01)
**必要边界：** No invented facts.
'''
REGISTRY=[dict(id='v-stable',term_id='example',heading='One construction',selection_status='unreviewed',cases=[])]
PROVENANCE={'example':{'origin':'new'}}
TOPIC={'id':'demo','title':'示例'}

def parse(text=TEXT,registry=None):return parse_document(text,'topics/example.md',TOPIC,registry or REGISTRY,PROVENANCE)

class ParserTests(unittest.TestCase):
    def test_minimal_bilingual(self):
        t=parse()[0];self.assertEqual(t['id'],'example');self.assertEqual(t['aliases'],['示例','sample']);self.assertEqual(t['variants'][0]['id'],'v-stable')
    def test_missing_title_has_context(self):
        with self.assertRaisesRegex(CatalogError,r'topics/example.md:1\nterm: example\nerror: missing level-2 title'):parse(TEXT.replace('## 示例 Example','示例 Example'))
    def test_missing_field(self):
        for name in ['词条 ID','词汇与别名','含义','必要边界']:
            with self.subTest(name=name),self.assertRaisesRegex(CatalogError,'missing field'):parse(TEXT.replace('**'+name+'：**',''))
    def test_missing_variant(self):
        with self.assertRaisesRegex(CatalogError,'missing level-3'):parse(TEXT.replace('### One construction','One construction'))
    def test_missing_registry(self):
        with self.assertRaisesRegex(CatalogError,'variant One construction'):parse(TEXT, [dict(REGISTRY[0],heading='Other')])
    def test_duplicate_selector(self):
        with self.assertRaisesRegex(CatalogError,'got 2'):parse(TEXT,REGISTRY*2)
    def test_stable_id_after_rename(self):
        self.assertEqual(parse(TEXT.replace('One construction','Renamed'),[dict(REGISTRY[0],heading='Renamed')])[0]['variants'][0]['id'],'v-stable')
    def test_source_missing(self):self.assertIn('missing source R01',source_errors(parse(),[])[0])
    def test_legacy_compatibility(self):self.assertEqual(validate_history(),[])
    def test_single_variant_and_combination(self):
        t=parse()[0];v=t['variants'][0];text=variant_brief(t,v)
        for fragment in ['v-stable','No invented facts','Connect:','Sources: R01']:self.assertIn(fragment,text)
        self.assertIn('not automatically compatible',combination_brief([(t,v),(t,v)]))
    def test_asset_filter(self):
        items=[{'final_use':'eligible','status':'clean'},{'final_use':'reference_only'},{'final_use':'eligible','legacy_status':'truncated'},{'final_use':'eligible','legacy_status':'superseded'}]
        self.assertEqual(final_assets(items),items[:1])
    def test_payload_escape(self):
        text={'x':'</script><script>alert(1)</script>&\u2028\u2029'}
        s=safe_payload(text);self.assertNotIn('<',s);self.assertNotIn('&',s);self.assertEqual(json.loads(s),text)

class TemporaryRepository(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__','validation.json'))
    def tearDown(self):self.temp.cleanup()
    def test_rebuild_without_generated_inputs_and_determinism(self):
        expected=build(self.root)
        for name in GENERATED:(self.root/name).unlink(missing_ok=True)
        for _ in range(2):
            subprocess.run([sys.executable,str(self.root/'scripts/rebuild_navigation.py')],check=True,capture_output=True)
            self.assertEqual({n:(self.root/n).read_text() for n in GENERATED},expected)
    def test_duplicate_variant_id(self):
        p=self.root/'catalog/variants.json';d=read_json(p);d[1]['id']=d[0]['id'];p.write_text(json.dumps(d))
        with self.assertRaisesRegex(CatalogError,'duplicate variant ID'):parse_topics(self.root)
    def test_duplicate_term_id(self):
        p=self.root/'catalog/topics.json';d=read_json(p);d.append(d[0]);p.write_text(json.dumps(d))
        with self.assertRaisesRegex(CatalogError,'duplicate term ID'):parse_topics(self.root)
    def test_missing_link_and_anchor(self):
        (self.root/'broken.md').write_text('[bad](absent.md)\n[bad anchor](SKILL.md#not-a-real-anchor)\n')
        errors=link_errors(self.root);self.assertTrue(any('absent.md' in x for x in errors));self.assertTrue(any('not-a-real-anchor' in x for x in errors))
    def test_missing_asset(self):
        p=self.root/'assets/visual-library/catalog.json';d=read_json(p);d['items'][0]['file']='missing.png';p.write_text(json.dumps(d))
        self.assertTrue(any('missing asset' in x for x in artifact_errors(self.root)))

class SVGTests(unittest.TestCase):
    def audit(self,body,required=(),allow=False):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'test.svg';p.write_text('<svg xmlns="http://www.w3.org/2000/svg">'+body+'</svg>');return audit_svg(p,required,allow)
    def test_valid(self):self.assertEqual(self.audit('<rect id="a"/><text>CPU</text>',['CPU'])['issues'],[])
    def test_missing_labels(self):self.assertTrue(self.audit('<rect/>',['GPU'])['issues'])
    def test_duplicate_ids(self):self.assertEqual(self.audit('<rect id="x"/><text id="x">A</text>')['duplicate_ids'],['x'])
    def test_image_elements(self):
        s='<rect/><text>GPU</text><image href="data:image/png;base64,AAAA"/>'
        self.assertTrue(self.audit(s)['issues']);self.assertFalse(self.audit(s,allow=True)['issues'])
        self.assertEqual(self.audit(s,allow=True)['image_count'],1)
    def test_foreign_object(self):self.assertTrue(self.audit('<rect/><text>A</text><foreignObject/>')['issues'])

if __name__=='__main__':unittest.main()
