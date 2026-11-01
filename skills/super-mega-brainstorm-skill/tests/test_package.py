import importlib.util
from pathlib import Path
import tempfile
import shutil
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('pkgcheck', ROOT/'scripts/validate_package.py')
pkgcheck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pkgcheck)

class PackageTests(unittest.TestCase):
    def test_current_package(self):
        self.assertEqual(pkgcheck.validate(ROOT), [])
    def test_missing_critical_reference(self):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            for rel in pkgcheck.REQUIRED:
                file = tmp/rel
                file.parent.mkdir(parents=True,exist_ok=True)
                if rel!='references/fallacy-atlas.md':
                    shutil.copy2(ROOT/rel, file)
            errors=pkgcheck.validate(tmp)
            self.assertTrue(any('fallacy-atlas.md' in e for e in errors))
    def test_invocation_rules_present(self):
        skill=(ROOT/'SKILL.md').read_text()
        for term in ['Super Mega Brainstorm', 'brainstorm', 'other explicitly named', 'full stages 0–10']:
            self.assertIn(term,skill)
    def test_no_numerical_idea_quota(self):
        skill=(ROOT/'SKILL.md').read_text()
        self.assertIn('No idea count', skill)
        self.assertIn('zero',skill.lower())
        self.assertIn('one',skill.lower())
    def test_syllogism_guide_distinguishes_truth(self):
        guide=(ROOT/'references/formal-argument-guide.md').read_text()
        self.assertIn('soundness',guide.lower())
        self.assertIn('valid',guide.lower())
        self.assertIn('countermodel',guide.lower())

if __name__ == '__main__': unittest.main()
