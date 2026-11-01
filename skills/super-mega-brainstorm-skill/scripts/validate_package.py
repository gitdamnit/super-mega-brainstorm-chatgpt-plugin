#!/usr/bin/env python3
"""Validate package structure, dependencies, and documented invariants.

This is a structural validator, not a reasoning-quality certificate and not a
client-compatibility guarantee.

Usage:
  python3 scripts/validate_package.py .
  python3 scripts/validate_package.py extracted-package --distribution
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED = [
    'SKILL.md',
    'README.md',
    'MIGRATION.md',
    'CHANGELOG.md',
    'PRODUCT_REQUIREMENTS.md',
    'DECISION_LOG.md',
    'PROJECT_STATUS.md',
    'references/techniques.md',
    'references/evaluation-and-workflow.md',
    'references/evidence-and-epistemics.md',
    'references/fallacy-atlas.md',
    'references/formal-argument-guide.md',
    'references/source-inventory.md',
    'references/rubric.md',
    'references/examples.md',
    'references/facilitation.md',
    'assets/session-template.md',
    'scripts/argument_checker.py',
    'scripts/categorical_checker.py',
    'scripts/lint_output.py',
    'scripts/validate_package.py',
    'tests/run_tests.sh',
    'tests/test_logic.py',
    'tests/test_package.py',
    'tests/test_lint_output.py',
    'tests/test_categorical_checker.py',
    'tests/acceptance.md',
    'tests/fixtures/valid_creative.md',
    'tests/fixtures/valid_workshop.md',
    'tests/fixtures/valid_one_solution.md',
    'tests/fixtures/valid_zero_solution.md',
    'tests/fixtures/valid_false_premise.md',
    'docs/INTEGRATION_MATRIX.md',
    'docs/INTEGRATION_REPORT.md',
    'docs/VERIFICATION_REPORT.md',
    'Makefile',
    '.gitignore',
    '.github/workflows/ci.yml',
]

QUOTA_PATTERNS = [
    r"(?i)\b(?:at least|minimum(?: of)?|no fewer than|exactly)\s+\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b\d+\s*[-–—]\s*\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b(?:generate|produce|list|give me|come up with)\s+\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b\d+\+\s+(?:ideas?|options?|candidates?)\b",
]

MANDATORY_ABSURD = re.compile(r"(?i)\b(?:must|required|compulsory|mandatory)\b[^.\n]{0,60}\babsurd\b|\babsurd\s+(?:option|idea)\s+(?:is\s+)?(?:required|compulsory|mandatory)\b")
MANDATORY_WINNER = re.compile(r"(?i)\b(?:must|required|compulsory|mandatory)\b[^.\n]{0,60}\b(?:recommend|winner|ranking|rank|choose)\b")
NEGATION = re.compile(r"(?i)\b(?:no|not|never|without|avoid|forbid|prohibit)\b")

KEY_INVARIANTS = [
    'Default brainstorm activation',
    'fallacy-atlas.md',
    'formal-argument-guide.md',
    'No idea count',
    'NO DEFENSIBLE SOLUTION IDENTIFIED',
    'full stages 0–10',
    'No abbreviated brainstorming mode',
]

FRONTMATTER_NAME = re.compile(r'(?m)^name:\s*super-mega-brainstorm-skill\s*$')
FRONTMATTER_VERSION = re.compile(r'(?m)^\s{2}version:\s*["\']?0\.2\.0["\']?\s*$')
REFERENCE_RE = re.compile(r"`((?:references|scripts|assets|tests|docs)/[A-Za-z0-9_./-]+\.(?:md|py|sh))`")
TEXT_SUFFIXES = {'.md', '.py', '.sh', '.yml', '.yaml', '.json', '.txt'}


def _positive_matches(pattern: re.Pattern[str], text: str):
    for match in pattern.finditer(text):
        prefix = text[max(0, match.start() - 40) : match.start()]
        if NEGATION.search(prefix):
            continue
        yield match


def validate(root, distribution: bool = False):
    root = Path(root)
    problems = []

    for path in REQUIRED:
        if not (root / path).is_file():
            problems.append(f'Missing required: {path}')

    skill_path = root / 'SKILL.md'
    if not skill_path.is_file():
        return problems

    text = skill_path.read_text('utf-8')
    if not text.startswith('---\n') or not text.count('\n---\n'):
        problems.append('Missing YAML frontmatter')
    if text.lstrip().startswith('---\n') and text.lstrip().count('\n---\n') > 1:
        problems.append('Duplicate frontmatter block')
    if not FRONTMATTER_NAME.search(text):
        problems.append('Skill name mismatch')
    if not FRONTMATTER_VERSION.search(text):
        problems.append('Version is not 0.2.0')
    for literal in KEY_INVARIANTS:
        if literal not in text:
            problems.append(f'Key invariant absent: {literal}')

    if len(text.splitlines()) > 500:
        problems.append('SKILL.md exceeds 500 lines')
    if re.search(r'(?mi)^\*\*Draft status:', text):
        problems.append('Draft status retained in main SKILL.md')

    for pattern in QUOTA_PATTERNS:
        match = re.search(pattern, text)
        if match:
            problems.append(f'Numeric idea quota found: {match.group(0)!r}')
    if any(_positive_matches(MANDATORY_ABSURD, text)):
        problems.append('Compulsory absurd option language found')
    if any(_positive_matches(MANDATORY_WINNER, text)):
        problems.append('Mandatory winner/ranking language found')

    if re.search(r'https?://', text):
        problems.append('SKILL.md contains a runtime URL; local references should carry attribution URLs')

    body = text.split('\n---\n', 1)[1] if '\n---\n' in text else text
    for rel in sorted(set(REFERENCE_RE.findall(body))):
        if not (root / rel).is_file():
            problems.append(f'SKILL.md references missing file: {rel}')

    for folder in ['scripts', 'tests']:
        for path in sorted((root / folder).glob('*.py')):
            try:
                compile(path.read_text('utf-8'), str(path), 'exec')
            except SyntaxError as exc:
                problems.append(f'Python syntax error in {path.relative_to(root)}: {exc}')

    if distribution:
        for forbidden in ['.git', '.opencode', '.git-that-shit', '__pycache__', 'dist']:
            if any(p.name == forbidden for p in root.rglob('*')):
                problems.append(f'Local repository/state/development directory bundled: {forbidden}')

    return problems


def hygiene_warnings(root):
    root = Path(root)
    warnings = []
    trailing = []
    for path in sorted(root.rglob('*')):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {'.git', '.opencode', '.git-that-shit', '__pycache__', 'dist'} for part in path.relative_to(root).parts):
            continue
        for number, line in enumerate(path.read_text('utf-8', errors='replace').splitlines(), 1):
            if line.rstrip() != line:
                trailing.append(f'{path.relative_to(root)}:{number}')
    if trailing:
        warnings.append(f'Trailing whitespace in {len(trailing)} line(s), first: {trailing[0]}')
    return warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', default='.', help='Skill root (default: .)')
    parser.add_argument('--distribution', action='store_true', help='Reject .git/.opencode/snapshots/caches/dist')
    parser.add_argument('--json', action='store_true', help='Emit JSON')
    args = parser.parse_args(argv)

    problems = validate(args.root, args.distribution)
    warnings = hygiene_warnings(args.root)

    if args.json:
        print(json.dumps({'ok': not problems, 'problems': problems, 'warnings': warnings}, indent=2))
    else:
        for problem in problems:
            print('FAIL', problem)
        for warning in warnings:
            print('WARN', warning)
        if problems:
            print(f'FAIL: {len(problems)} structural problem(s)')
        else:
            print('PASS package structure and documented invariants (not model behavior)')
    return 1 if problems else 0


if __name__ == '__main__':
    sys.exit(main())
