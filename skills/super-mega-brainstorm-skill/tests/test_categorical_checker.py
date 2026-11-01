#!/usr/bin/env python3
"""Tests for scripts/categorical_checker.py."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import categorical_checker  # noqa: E402


class CategoricalTests(unittest.TestCase):
    def test_barbara_is_valid(self) -> None:
        result = categorical_checker.check(["All M are P", "All S are M"], "All S are P")
        self.assertEqual(result["verdict"], "VALID")
        self.assertIn("finite-model", result["scope"])

    def test_undistributed_middle_is_invalid(self) -> None:
        result = categorical_checker.check(["All P are M", "All S are M"], "All S are P")
        self.assertEqual(result["verdict"], "INVALID")
        self.assertIsNotNone(result["counterexample"])

    def test_existential_fallacy_is_invalid(self) -> None:
        result = categorical_checker.check(["All S are P"], "Some S are P")
        self.assertEqual(result["verdict"], "INVALID")
        self.assertTrue(any("Boolean" in limit for limit in result["limits"]))

    def test_darii_is_valid(self) -> None:
        result = categorical_checker.check(["All M are P", "Some S are M"], "Some S are P")
        self.assertEqual(result["verdict"], "VALID")

    def test_malformed_statement_raises(self) -> None:
        with self.assertRaises(categorical_checker.CheckError):
            categorical_checker.check(["Every S is P"], "All S are P")

    def test_double_negative_no_does_not_silently_flip_meaning(self) -> None:
        with self.assertRaises(categorical_checker.CheckError):
            categorical_checker.check(["No S are not P"], "All S are P")

    def test_json_cli(self) -> None:
        completed = subprocess.run(
            [
                sys.executable,
                str(ROOT / "scripts" / "categorical_checker.py"),
                "--premise",
                "All M are P",
                "--premise",
                "All S are M",
                "--conclusion",
                "All S are P",
                "--json",
            ],
            capture_output=True,
            text=True,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertEqual(payload["verdict"], "VALID")


if __name__ == "__main__":
    unittest.main()
