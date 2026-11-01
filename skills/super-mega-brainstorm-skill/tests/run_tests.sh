#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."

echo "== package validation =="
python3 scripts/validate_package.py .

echo "== unit tests =="
python3 -m unittest discover -s tests -p 'test_*.py' -v

echo "== output linter fixtures =="
python3 scripts/lint_output.py tests/fixtures/valid_creative.md --mode workshop
python3 scripts/lint_output.py tests/fixtures/valid_workshop.md --mode workshop
python3 scripts/lint_output.py tests/fixtures/valid_false_premise.md --mode deep
python3 scripts/lint_output.py tests/fixtures/valid_one_solution.md --mode workshop
python3 scripts/lint_output.py tests/fixtures/valid_zero_solution.md --mode workshop

echo "== argument checker smoke =="
python3 scripts/argument_checker.py --premise "P -> Q" --premise "P" --conclusion "Q"
python3 scripts/argument_checker.py --premise "P -> Q" --premise "Q" --conclusion "P" || test $? -eq 1
python3 scripts/categorical_checker.py --premise "All M are P" --premise "All S are M" --conclusion "All S are P"
python3 scripts/categorical_checker.py --premise "All P are M" --premise "All S are M" --conclusion "All S are P" || test $? -eq 1
