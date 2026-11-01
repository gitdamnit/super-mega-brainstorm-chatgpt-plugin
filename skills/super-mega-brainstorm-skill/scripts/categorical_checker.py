#!/usr/bin/env python3
"""Optional finite-model checker for standard-form categorical syllogisms.

This checks a formal pattern over a finite domain. It does not verify the
meaning or truth of the terms, and a finite pass is not a general first-order
proof. The manual countermodel method remains authoritative for edge cases.

Usage:
  python3 scripts/categorical_checker.py \
    --premise "All M are P" --premise "All S are M" --conclusion "All S are P"

  python3 scripts/categorical_checker.py ... --domain 3 --json
"""

from __future__ import annotations

import argparse
import itertools
import json
import re
import sys

STATEMENT_RE = re.compile(r"^(all|no|some)\s+(.+?)\s+(are|is)(?:\s+(not))?\s+(.+?)$", re.IGNORECASE)


class CheckError(ValueError):
    pass


def parse_statement(text: str):
    match = STATEMENT_RE.match(text.strip())
    if not match:
        raise CheckError(
            f"Cannot parse categorical statement: {text!r}. "
            "Use 'All S are P', 'No S are P', 'Some S are P', or 'Some S are not P'."
        )
    quantifier = match.group(1).lower()
    subject = match.group(2).strip().lower()
    negated = bool(match.group(4))
    predicate = match.group(5).strip().lower()
    # Reject a non-standard double-negated form rather than silently changing
    # its meaning. "No S are not P" is NOT equivalent to "No S are P".
    if quantifier == "no" and negated:
        raise CheckError("Non-standard double-negative categorical form. Rewrite explicitly as 'All S are P' or another supported standard form.")
    if quantifier == "some" and negated:
        return ("some_not", subject, predicate)
    if quantifier == "some":
        return ("some", subject, predicate)
    if quantifier == "no" or (quantifier == "all" and negated):
        return ("no", subject, predicate)
    return ("all", subject, predicate)


def holds(kind: str, subject: set[int], predicate: set[int]) -> bool:
    if kind == "all":
        return subject <= predicate
    if kind == "no":
        return subject.isdisjoint(predicate)
    if kind == "some":
        return bool(subject & predicate)
    if kind == "some_not":
        return bool(subject - predicate)
    raise CheckError(f"Unknown categorical kind: {kind}")


def check(premises, conclusion, domain_size=3):
    if not premises:
        raise CheckError("At least one premise required.")
    if domain_size < 1 or domain_size > 5:
        raise CheckError("Domain size must be between 1 and 5.")
    parsed_premises = [parse_statement(p) for p in premises]
    parsed_conclusion = parse_statement(conclusion)
    terms = sorted({term for item in parsed_premises + [parsed_conclusion] for term in (item[1], item[2])})
    if len(terms) > 4:
        raise CheckError(f"Too many categorical terms ({len(terms)}); limit is 4 for a finite check.")

    domain = list(range(domain_size))
    subsets = []
    for r in range(domain_size + 1):
        for combo in itertools.combinations(domain, r):
            subsets.append(set(combo))

    for extensions in itertools.product(subsets, repeat=len(terms)):
        model = dict(zip(terms, extensions))
        if all(holds(kind, model[s], model[p]) for kind, s, p in parsed_premises):
            kind, s, p = parsed_conclusion
            if not holds(kind, model[s], model[p]):
                return {
                    "verdict": "INVALID",
                    "counterexample": {term: sorted(model[term]) for term in terms},
                    "terms": terms,
                    "domain_size": domain_size,
                    "scope": f"finite-model check over {domain_size} individuals",
                    "limits": [
                        "Modern/Boolean reading: 'All S are P' does not imply that S exists.",
                        "A finite countermodel refutes the form; a finite pass is not a general first-order proof.",
                        "Does not verify the meaning or truth of the terms.",
                    ],
                }

    return {
        "verdict": "VALID",
        "counterexample": None,
        "terms": terms,
        "domain_size": domain_size,
        "scope": f"finite-model check over {domain_size} individuals",
        "limits": [
            "Modern/Boolean reading: 'All S are P' does not imply that S exists.",
            "A finite pass is not a general first-order proof; it is evidence against a countermodel in this domain.",
            "Does not verify the meaning or truth of the terms.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--premise", action="append", required=True)
    parser.add_argument("--conclusion", required=True)
    parser.add_argument("--domain", type=int, default=3)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        result = check(args.premise, args.conclusion, args.domain)
    except CheckError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(result["verdict"])
        if result["counterexample"] is not None:
            print("Counterexample:", json.dumps(result["counterexample"], sort_keys=True))
        print("Scope:", result["scope"])
        for limit in result["limits"]:
            print("Limit:", limit)
    return 0 if result["verdict"] == "VALID" else 1


if __name__ == "__main__":
    sys.exit(main())
