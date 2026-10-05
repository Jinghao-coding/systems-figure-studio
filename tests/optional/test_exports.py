"""Opt-in dependency/editor exports, separate from core tests and GUI round trips."""
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'scripts'))
from audit_vector_figure import audit_pdf

class OptionalExports(unittest.TestCase):
    @unittest.skipUnless(importlib.util.find_spec('pymupdf'),'PyMuPDF not installed in this runtime')
    def test_pdf_fonts_at_width(self):
        import pymupdf
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'figure.pdf'
            doc=pymupdf.open();page=doc.new_page(width=300,height=200);page.insert_text((25,30),'GPU',fontsize=12);page.draw_rect((20,40,180,100));doc.save(p);doc.close()
            self.assertFalse(audit_pdf(p,['GPU'],False,300,8)['issues'])
            self.assertTrue(audit_pdf(p,['GPU'],False,100,8)['issues'])
    @unittest.skipUnless(os.environ.get('DRAWIO_BINARY'),'DRAWIO_BINARY not set; real exporter optional')
    def test_drawio_export(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'export.svg'
            subprocess.run([os.environ['DRAWIO_BINARY'],'--export','--format','svg','--output',str(p),str(ROOT/'assets/visual-library/gpu-flat-native.drawio')],check=True,timeout=45,capture_output=True)
            self.assertTrue(p.is_file());self.assertIn('<svg',p.read_text())

if __name__=='__main__':unittest.main()
