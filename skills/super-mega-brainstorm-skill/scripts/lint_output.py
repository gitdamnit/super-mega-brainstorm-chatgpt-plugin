#!/usr/bin/env python3
"""Structural linter for a Super Mega Brainstorm v0.2.0 output.

This checks the v0.2.0 invariants that can be checked mechanically:
no numeric idea quota, no compulsory absurd option, no mandatory winner,
complete-workflow elements, audit disclosure, formal-gate disclosure, and
the authorization boundary.

It is not a semantic quality certificate. It cannot decide whether a premise
is true, whether a fallacy label is justified, or whether a recommendation is
wise. Use references/rubric.md for judgment.

Usage:
  python3 scripts/lint_output.py output.md
  python3 scripts/lint_output.py output.md --mode deep --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

MODES = ("workshop", "deep", "red-team")

QUOTA_PATTERNS = [
    r"(?i)\b(?:at least|minimum(?: of)?|no fewer than|exactly)\s+\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b\d+\s*[-–—]\s*\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b(?:generate|produce|list|give me|come up with)\s+\d+\s+(?:ideas?|options?|candidates?|alternatives?)\b",
    r"(?i)\b\d+\+\s+(?:ideas?|options?|candidates?)\b",
]

MANDATORY_ABSURD = re.compile(r"(?i)\b(?:must|required|compulsory|mandatory)\b[^.\n]{0,60}\babsurd\b|\babsurd\s+(?:option|idea)\s+(?:is\s+)?(?:required|compulsory|mandatory)\b")
MANDATORY_WINNER = re.compile(r"(?i)\b(?:must|required|compulsory|mandatory)\b[^.\n]{0,60}\b(?:recommend|winner|rank(?:ing)?|choose)\b")
NEGATION = re.compile(r"(?i)\b(?:no|not|never|without|avoid|forbid|prohibit)\b")
CERTAINTY = re.compile(r"(?i)\b(?:proves?|proven|guarantees?|guaranteed|100%|infallible|certainly)\b")
IMPLEMENTATION = re.compile(r"(?i)\b(?:I|we)\s+(?:have\s+)?(?:implemented|deployed|sent|purchased|contacted|committed|merged|published|released|changed\s+the\s+code)\b")
URL = re.compile(r"https?://[^\s)>\]]+")

CORE_ELEMENTS = {
    "frame": (
        r"(?i)\b(?:decision brief|decision question|problem statement|desired outcome|frame|framing)\b",
        r"(?i)\b(?:baseline|zero option|do nothing|status quo|inaction)\b",
    ),
    "claims": (
        r"(?i)\b(?:claim ledger|claim|assumption|evidence|unknown|unverified)\b",
        r"(?i)\b(?:claim|assumption|unknown|evidence|unverified)\b",
    ),
    "candidates": (
        r"(?i)\b(?:candidate|option|alternative|solution|rival)\b",
        r"(?i)\b(?:no defensible solution|no viable candidate|one defensible option|not applicable)\b",
    ),
    "evaluation": (
        r"(?i)\b(?:criteria|tradeoff|trade-off|evaluation|scorecard|comparison|sensitivity)\b",
        r"(?i)\b(?:criteria|tradeoff|trade-off|evaluation|scorecard|comparison|sensitivity)\b",
    ),
    "audit": (
        r"(?i)\b(?:smell test|fallacy|reasoning audit|audit|evidence review)\b",
        r"(?i)\b(?:BLOCKER|MAJOR|CAUTION|CLEAR|UNVERIFIABLE|no identified defect|no material defect)\b",
    ),
    "formal": (
        r"(?i)\b(?:formal gate|formal argument|validity|soundness|VALID|INVALID|NOT DEMONSTRABLE|NOT APPLICABLE)\b",
        r"(?i)\b(?:VALID|INVALID|NOT DEMONSTRABLE|NOT APPLICABLE|validity|soundness)\b",
    ),
    "next": (
        r"(?i)\b(?:next action|next step|test|experiment|decision)\b",
        r"(?i)\b(?:authorization|not authorized|no implementation|stop before implementation)\b",
    ),
}


@dataclass
class Finding:
    level: str
    code: str
    message: str

    def as_dict(self) -> dict:
        return {"level": self.level, "code": self.code, "message": self.message}


@dataclass
class Result:
    errors: list[Finding] = field(default_factory=list)
    warnings: list[Finding] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return not self.errors

    def error(self, code: str, message: str) -> None:
        self.errors.append(Finding("error", code, message))

    def warn(self, code: str, message: str) -> None:
        self.warnings.append(Finding("warning", code, message))

    def as_dict(self, path: str | None = None, mode: str | None = None) -> dict:
        return {
            "file": path,
            "mode": mode,
            "ok": self.ok,
            "errors": [f.as_dict() for f in self.errors],
            "warnings": [f.as_dict() for f in self.warnings],
            "stats": self.stats,
        }


def _positive_matches(pattern: re.Pattern[str], text: str):
    for match in pattern.finditer(text):
        prefix = text[max(0, match.start() - 40) : match.start()]
        if NEGATION.search(prefix):
            continue
        yield match


def lint(text: str, mode: str = "workshop") -> Result:
    result = Result()
    mode = mode.lower()
    if mode not in MODES:
        result.error("bad-mode", f"Unknown mode '{mode}'. Use one of: {', '.join(MODES)}.")
        return result
    if not text.strip():
        result.error("empty", "The output is empty.")
        return result

    result.stats["mode"] = mode

    for pattern in QUOTA_PATTERNS:
        match = re.search(pattern, text)
        if match:
            result.error("idea-quota", f"Numeric idea quota detected: {match.group(0)!r}. The v0.2.0 contract forbids quotas.")
    if any(_positive_matches(MANDATORY_ABSURD, text)):
        result.error("compulsory-absurd", "Compulsory absurd option detected. Wild-tail candidates are optional.")
    if any(_positive_matches(MANDATORY_WINNER, text)):
        result.error("mandatory-winner", "Mandatory winner/ranking language detected. A recommendation is optional.")

    if re.search(r"(?i)\b(?:full audit|complete audit|audit complete|all categories checked)\b", text) and re.search(
        r"(?i)\b(?:unavailable|not available|missing reference|incomplete installation|no access)\b", text
    ):
        if not re.search(r"(?i)\b(?:incomplete installation|provisional (?:audit|reasoning|run|assessment))\b", text):
            result.error("false-complete-audit", "The output claims a complete audit while naming unavailable material. Label it provisional or incomplete installation.")

    if IMPLEMENTATION.search(text):
        result.error("unauthorized-implementation", "The output claims implementation, deployment, outreach, purchase, or publication. Stop before implementation unless explicitly authorized.")

    if CERTAINTY.search(text):
        result.warn("certainty-language", "Certainty language found. Verify the evidence supports it or qualify it.")
    for match in URL.finditer(text):
        if not re.search(r"(?im)^\s*(?:[-*]\s*)?\*{0,2}(?:Source|Accessed)\*{0,2}\s*:", text):
            result.warn("citation-without-source", f"URL present without a Source/Accessed field: {match.group(0)}")

    for name, patterns in CORE_ELEMENTS.items():
        if not re.search(patterns[0], text):
            result.error(f"missing-{name}", f"Could not find the {name} element required by the complete workflow.")
        elif not re.search(patterns[1], text):
            result.error(f"incomplete-{name}", f"The {name} element is present but lacks its required detail.")

    if not re.search(r"(?i)\b(?:UNVERIFIED|UNKNOWN|assumption|assumptions|unknowns)\b", text):
        result.error("no-uncertainty", "No explicit uncertainty or assumption disclosure found.")
    if not re.search(r"(?i)\b(?:claim ledger|claims?|assumptions?)\b", text):
        result.error("no-claim-ledger", "No claim or assumption ledger found.")

    if mode == "deep":
        if not re.search(r"(?i)\b(?:formal gate|formal argument|validity|soundness)\b", text):
            result.error("deep-formal", "DEEP output must disclose the formal argument gate or state why it is not applicable.")
        if not re.search(r"(?i)\b(?:BLOCKER|MAJOR|CAUTION|CLEAR|UNVERIFIABLE|no identified defect)\b", text):
            result.error("deep-audit", "DEEP output must include severity-tagged audit findings or an explicit no-defect statement.")
    elif mode == "red-team":
        if not re.search(r"(?i)\b(?:claim|premise|rival|alternative|hypothesis)\b", text):
            result.error("red-team-claims", "RED TEAM output must identify claims, premises, rivals, or hypotheses.")
        if not re.search(r"(?i)\b(?:BLOCKER|MAJOR|CAUTION|CLEAR|UNVERIFIABLE|no identified defect)\b", text):
            result.error("red-team-audit", "RED TEAM output must include severity-tagged audit findings or an explicit no-defect statement.")

    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Structural linter for a Super Mega Brainstorm v0.2.0 output.")
    parser.add_argument("path", help="Markdown file containing one output, or '-' for stdin.")
    parser.add_argument("--mode", choices=MODES, default="workshop", help="Expected mode (default: workshop).")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args(argv)

    if args.path == "-":
        text = sys.stdin.read()
        label = "<stdin>"
    else:
        path = Path(args.path)
        if not path.exists():
            print(f"ERROR: file not found: {path}", file=sys.stderr)
            return 2
        text = path.read_text(encoding="utf-8")
        label = str(path)

    result = lint(text, args.mode)

    if args.json:
        print(json.dumps(result.as_dict(label, args.mode), indent=2, ensure_ascii=False))
    else:
        for finding in result.errors:
            print(f"ERROR [{finding.code}] {finding.message}")
        for finding in result.warnings:
            print(f"WARN  [{finding.code}] {finding.message}")
        print(f"{'PASS' if result.ok else 'FAIL'}: {label} — {len(result.errors)} errors, {len(result.warnings)} warnings")

    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
