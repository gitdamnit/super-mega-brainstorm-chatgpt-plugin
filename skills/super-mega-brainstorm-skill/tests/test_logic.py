import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('argcheck', ROOT/'scripts/argument_checker.py')
argcheck = importlib.util.module_from_spec(spec)
spec.loader.exec_module(argcheck)

class ArgumentChecks(unittest.TestCase):
    def verify(self, premises, conclusion, expected):
        self.assertEqual(argcheck.check(premises, conclusion)['verdict'], expected)

    def test_modus_ponens(self): self.verify(['P -> Q', 'P'], 'Q', 'VALID')
    def test_modus_tollens(self): self.verify(['P -> Q', '!Q'], '!P', 'VALID')
    def test_hypothetical_syllogism(self): self.verify(['P -> Q', 'Q -> R'], 'P -> R', 'VALID')
    def test_disjunctive_syllogism(self): self.verify(['P | Q', '!P'], 'Q', 'VALID')
    def test_affirm_consequent(self): self.verify(['P -> Q', 'Q'], 'P', 'INVALID')
    def test_deny_antecedent(self): self.verify(['P -> Q', '!P'], '!Q', 'INVALID')
    def test_underdetermined(self): self.verify(['P'], 'Q', 'INVALID')
    def test_commutativity(self): self.verify(['P & Q'], 'Q & P', 'VALID')
    def test_nesting(self): self.verify(['P -> (Q | R)', 'P', '!Q'], 'R', 'VALID')
    def test_implies_right_assoc(self): self.verify(['P -> (Q -> R)', 'P', 'Q'], 'R', 'VALID')
    def test_tautological_conclusion(self): self.verify(['P'], 'Q | !Q', 'VALID')
    def test_counterexample(self): self.assertIsNotNone(argcheck.check(['P -> Q','Q'], 'P')['counterexample'])
    def test_bad_lexical_input(self):
        with self.assertRaises(argcheck.FormulaError): argcheck.check(['P ^ Q'], 'P')
    def test_bad_syntax(self):
        with self.assertRaises(argcheck.FormulaError): argcheck.check(['P ->'], 'P')
    def test_variable_cap(self):
        with self.assertRaises(argcheck.FormulaError): argcheck.check([' & '.join(f'P{i}' for i in range(13))], 'P1')

if __name__ == '__main__': unittest.main()
