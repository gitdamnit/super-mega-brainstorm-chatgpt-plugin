# Verification Report

**Date:** 2026-10-31
**Environment:** Linux, Python 3.12.3
**Project:** `/home/evan/Projects/super-mega-brainstorm-skill`
**Behavioral specification:** GPT-6 v0.2.0 (SHA-256 `d55cde4400ce3ed39e0de624296dfea06d74c3967a0c4700c5e34b8adcb64370`)
**Git:** not a repository; no commit SHA

## Result summary

| Check | Result | Evidence |
|---|---|---|
| Unit tests | Pass (44) | `docs/test-results.txt` |
| Package validator | Pass | `docs/validation.json` |
| Valid fixture lint | Pass | `docs/test-results.txt` |
| Propositional checker | Pass | `docs/argument-checker-results.txt` |
| Categorical checker | Pass | `docs/argument-checker-results.txt` |
| Install smoke | Pass | `docs/install-test.txt` |
| ZIP smoke | Pass — extracted copy validates and runs the full 44-test suite | `docs/zip-test.txt` |
| ProDoc validate/check | Pass | command output |
| Manual live-client acceptance | Not run | pending |
| Cross-model acceptance | Not run | pending |

## Automated suite

Command:

```bash
bash tests/run_tests.sh
```

Coverage:

- Preserved v0.2.0 propositional logic tests: modus ponens, modus tollens, hypothetical syllogism, disjunctive syllogism, affirming the consequent, denying the antecedent, underdetermination, commutativity, nesting, implication associativity, tautological conclusion, counterexample, lexical/syntax errors, variable cap.
- Preserved v0.2.0 package tests: current package, missing critical reference, invocation rules, no numerical quota, syllogism guide distinctions.
- New linter tests: valid creative/workshop/false-premise/one-solution/zero-solution outputs; quota, compulsory absurd, and mandatory winner rejection; missing audit, missing formal gate, false complete-audit claim, unauthorized implementation, missing uncertainty, missing authorization; CLI JSON.
- New categorical tests: Barbara, Darii, undistributed middle, existential fallacy, malformed input, CLI JSON.

## Failures encountered and repairs

| Failure | Cause | Repair |
|---|---|---|
| Linter crashed on import | A second inline `(?i)` flag appeared after an alternation | Moved the flag to the start of the expression |
| Linter authorization test used wrong fixture text | The workshop fixture was the naming example, not the queue example | Added a separate creative fixture and kept the queue fixture for mutation tests |
| False-complete-audit test did not trigger | The fixture contained the word “provisional” in an unrelated ledger line | Narrowed the suppression to “provisional audit/reasoning/run/assessment” or “incomplete installation” |
| Validator missing required docs during first run | Integration docs were not yet created | Created `PROJECT_STATUS.md`, `INTEGRATION_REPORT.md`, and this report |

## Scenario coverage

| Scenario | Coverage | Status |
|---|---|---|
| Ordinary creative brainstorming | `valid_creative.md`; examples 1 | Automated structure; human quality pending |
| Complex technical architecture | `valid_workshop.md`; examples 2 | Automated structure; human quality pending |
| Scientific hypothesis with insufficient evidence | examples 3 | Automated structure; human quality pending |
| Formally valid but factually false premise | `valid_false_premise.md`; examples 4; propositional checker | Automated structure and formal validity; human premise review pending |
| Correlation mistaken for causation | Scenario card 5; evidence guide | Manual scenario pending |
| Irreversible high-consequence decision | Scenario card 6; DEEP mode | Manual scenario pending |
| One identified defensible solution | `valid_one_solution.md` | Automated structure |
| No identified acceptable solution | `valid_zero_solution.md` | Automated structure |
| User demands certainty | Scenario card 9; examples 3 | Manual scenario pending |
| Generic “brainstorm” invocation | Invocation contract; acceptance check 2 | Manual scenario pending |

## Claims not verified

- Exact model behavior under the v0.2.0 workflow: not verified. The tests check structure and selected logic.
- Live-client compatibility: not verified.
- Cross-model consistency: not verified.
- Semantic quality or truth of the examples: not empirically tested.
- General first-order validity or causal certainty: not claimed by the checker or guide.
- Empirical effectiveness of the skill: not measured.
- License suitability: no license was chosen; the maintainer must decide.

## Remaining work

1. Run `tests/acceptance.md` in OpenCode and one second client; record outputs.
2. Add a cross-model comparison report.
3. Ask the owner to choose a license.
4. With owner authorization, initialize Git and commit/tag the release.
5. Optionally add a rubric-based evaluation harness for real model outputs.

## Evidence index

- `docs/test-results.txt` — full automated run.
- `docs/validation.json` — package validator output.
- `docs/argument-checker-results.txt` — propositional and categorical results.
- `docs/install-test.txt` — install smoke.
- `docs/zip-test.txt` — ZIP inspection and extraction test.
- `docs/INTEGRATION_MATRIX.md` — functional comparison.
- `docs/INTEGRATION_REPORT.md` — salvage/adapt/retire record.
- `PROJECT_STATUS.md` — current status and limitations.
- `DECISION_LOG.md` — decisions D-0001 through D-0010.
