#!/usr/bin/env python3
"""Tests for scripts/lint_output.py against the v0.2.0 invariants."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import lint_output  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures"


def fixture(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


def codes(result: lint_output.Result) -> set[str]:
    return {finding.code for finding in result.errors}


class ValidFixtureTests(unittest.TestCase):
    def test_creative_fixture_passes(self) -> None:
        result = lint_output.lint(fixture("valid_creative.md"), "workshop")
        self.assertTrue(result.ok, [f.message for f in result.errors])

    def test_workshop_fixture_passes(self) -> None:
        result = lint_output.lint(fixture("valid_workshop.md"), "workshop")
        self.assertTrue(result.ok, [f.message for f in result.errors])

    def test_one_solution_fixture_passes(self) -> None:
        result = lint_output.lint(fixture("valid_one_solution.md"), "workshop")
        self.assertTrue(result.ok, [f.message for f in result.errors])

    def test_zero_solution_fixture_passes(self) -> None:
        result = lint_output.lint(fixture("valid_zero_solution.md"), "workshop")
        self.assertTrue(result.ok, [f.message for f in result.errors])

    def test_false_premise_fixture_passes_deep(self) -> None:
        result = lint_output.lint(fixture("valid_false_premise.md"), "deep")
        self.assertTrue(result.ok, [f.message for f in result.errors])

    def test_red_team_fixture_passes(self) -> None:
        result = lint_output.lint(fixture("valid_false_premise.md"), "red-team")
        self.assertTrue(result.ok, [f.message for f in result.errors])


class ObsoleteRequirementTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = fixture("valid_workshop.md")

    def test_numeric_idea_quota_is_rejected(self) -> None:
        result = lint_output.lint(self.text + "\n\nGenerate 12 ideas.\n", "workshop")
        self.assertIn("idea-quota", codes(result))

    def test_compulsory_absurd_is_rejected(self) -> None:
        result = lint_output.lint(self.text + "\n\nYou must include an absurd option.\n", "workshop")
        self.assertIn("compulsory-absurd", codes(result))

    def test_mandatory_winner_is_rejected(self) -> None:
        result = lint_output.lint(self.text + "\n\nYou must recommend a winner.\n", "workshop")
        self.assertIn("mandatory-winner", codes(result))


class ContractFailureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = fixture("valid_workshop.md")

    def test_missing_audit_is_rejected(self) -> None:
        broken = self.text.split("## Advanced Smell Test")[0] + "## Formal gate" + self.text.split("## Formal gate", 1)[1]
        result = lint_output.lint(broken, "workshop")
        self.assertIn("missing-audit", codes(result))

    def test_missing_formal_gate_is_rejected(self) -> None:
        broken = self.text.split("## Formal gate")[0] + "## Decision and next step" + self.text.split("## Decision and next step", 1)[1]
        result = lint_output.lint(broken, "workshop")
        self.assertIn("missing-formal", codes(result))

    def test_false_complete_audit_is_rejected(self) -> None:
        broken = self.text + "\n\nComplete audit. The missing reference was unavailable.\n"
        result = lint_output.lint(broken, "workshop")
        self.assertIn("false-complete-audit", codes(result))

    def test_unauthorized_implementation_is_rejected(self) -> None:
        broken = self.text.replace(
            "**Authorization:** no migration or vendor purchase performed.",
            "**Authorization:** We implemented the migration and deployed it.",
        )
        result = lint_output.lint(broken, "workshop")
        self.assertIn("unauthorized-implementation", codes(result))

    def test_missing_uncertainty_is_rejected(self) -> None:
        minimal = "Decision brief: decide X. Baseline: do nothing. Claim ledger: C1 observed. Candidate: A. Criteria: cost. Audit: CLEAR. Formal gate: NOT APPLICABLE. Next action: test. Authorization: none."
        result = lint_output.lint(minimal, "workshop")
        self.assertIn("no-uncertainty", codes(result))

    def test_missing_authorization_is_rejected(self) -> None:
        broken = self.text.replace("**Authorization:** no migration or vendor purchase performed.\n", "")
        result = lint_output.lint(broken, "workshop")
        self.assertIn("incomplete-next", codes(result))


class DocumentationExampleTests(unittest.TestCase):
    def test_examples_document_lints(self) -> None:
        text = (ROOT / "references" / "examples.md").read_text(encoding="utf-8")
        lines = text.splitlines()
        starts = [i for i, line in enumerate(lines) if line.startswith("## ") and line[3:4].isdigit()]
        self.assertGreaterEqual(len(starts), 4)
        for index, start in enumerate(starts[:4]):
            end = starts[index + 1] if index + 1 < len(starts) else len(lines)
            result = lint_output.lint("\n".join(lines[start:end]), "deep")
            self.assertTrue(result.ok, [f.message for f in result.errors])


class CliTests(unittest.TestCase):
    def test_json_cli_passes_fixture(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "lint_output.py"),
                str(FIXTURES / "valid_workshop.md"),
                "--mode",
                "workshop",
                "--json",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertTrue(payload["ok"])

    def test_json_cli_fails_invalid_file(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.md"
            path.write_text("Decision brief: decide X. Baseline: do nothing.\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(ROOT / "scripts" / "lint_output.py"), str(path), "--json"],
                capture_output=True,
                text=True,
            )
            self.assertEqual(completed.returncode, 1)
            payload = json.loads(completed.stdout)
            self.assertFalse(payload["ok"])


if __name__ == "__main__":
    unittest.main()
