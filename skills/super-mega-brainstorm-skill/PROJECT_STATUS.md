# Project Status

## Current Phase

In Progress

The v0.2.0-based integration is implemented and locally tested. Manual live-client and cross-model acceptance remain pending, and no license, Git history, or publication exists.

## Repository State

<!-- Machine-maintained by `prodoc update`. Do not hand-edit. -->
<!-- prodoc:observed:start -->
- **Observed branch:** not a Git repository
- **Observed commit:** none
- **Observed working tree:** not under version control
- **Observed at:** 2026-10-31
<!-- prodoc:observed:end -->

## Verification Evidence

Local verification is recorded in `docs/test-results.txt`, `docs/validation.json`, `docs/argument-checker-results.txt`, `docs/install-test.txt`, and `docs/zip-test.txt`. The automated suite covers the preserved v0.2.0 propositional logic and package tests, the invariant linter, and the optional categorical checker.

No commit-bound verification entry exists because the project is not under version control. No live-client or cross-model acceptance run has been performed.

## Completed Work

- [Implemented] Re-based the project on the exact GPT-6 v0.2.0 package — `SKILL.md`, `references/`, `assets/`, `scripts/`, `tests/`
- [Implemented] Preserved v0.2.0 invocation, stages 0–10, no-quota, no-abbreviated-mode, and package-completion rules — `SKILL.md`
- [Implemented] Added candidate record, cost/dependency analysis, decision genealogy, overturn conditions, and zero/one-solution protocol — `references/techniques.md`, `references/evaluation-and-workflow.md`
- [Implemented] Added six final epistemic outcomes and outcome mapping — `references/formal-argument-guide.md`
- [Implemented] Added reasoning-integrity rubric, calibrated examples, and facilitation guide — `references/rubric.md`, `references/examples.md`, `references/facilitation.md`
- [Implemented] Added invariant output linter and optional categorical checker — `scripts/lint_output.py`, `scripts/categorical_checker.py`
- [Implemented] Extended the v0.2.0 package validator while preserving `validate(root)` — `scripts/validate_package.py`
- [Implemented] Added linter and categorical tests, fixtures, and acceptance checks — `tests/`
- [Tested] Automated unit suite — `docs/test-results.txt`
- [Tested] Package validator — `docs/validation.json`
- [Tested] Argument checker — `docs/argument-checker-results.txt`
- [Tested] Install and ZIP smoke checks — `docs/install-test.txt`, `docs/zip-test.txt`
- [Implemented] Added requirements, decision log, status, integration matrix/report — `PRODUCT_REQUIREMENTS.md`, `DECISION_LOG.md`, `docs/`
- [Planned] Manual live-client and cross-model acceptance
- [Planned] Owner decision on license
- [Planned] Git initialization and publication, only with explicit authorization

## Tests

| Suite | Command | Result | Evidence |
| --- | --- | --- | --- |
| unit | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | Pass (44) | `docs/test-results.txt` |
| package validation | `python3 scripts/validate_package.py .` | Pass | `docs/validation.json` |
| fixture lint | `scripts/lint_output.py` on five valid fixtures | Pass | `docs/test-results.txt` |
| propositional checker | `scripts/argument_checker.py` valid and invalid forms | Pass | `docs/argument-checker-results.txt` |
| categorical checker | `scripts/categorical_checker.py` valid and invalid forms | Pass | `docs/argument-checker-results.txt` |
| install smoke | `make install` to a temporary directory, then validate and lint | Pass | `docs/install-test.txt` |
| ZIP smoke | `make package`, inspect exclusions, extract, validate, and lint | Pass | `docs/zip-test.txt` |
| manual | `tests/acceptance.md` checks 1–15 | Not run | — |
| cross-model | portable prompts in `tests/acceptance.md` | Not run | — |

## Known Defects

None known in the automated suite.

Known limitations, not defects:

- The linter is structural. It cannot judge whether an idea is good, whether a premise is true, whether a fallacy label is justified, or whether a recommendation is wise.
- The propositional checker does not verify premise meaning or truth, general first-order validity, causation, or empirical support.
- The categorical checker is a finite-model aid, not a general first-order prover.
- No live-client installation or cross-model behavior has been verified. Package validation is not client compatibility certification.
- No license has been chosen; the package is not open source until the maintainer decides.
- The source tree contains `.opencode/` and `.git-that-shit/` development state; the distributable ZIP excludes them.
- No Git repository or commit SHA exists. No publication or push has occurred.

## Blockers

- **Live-client acceptance:** requires an installed client session and a model capable of running the scenarios.
- **License decision:** owned by the maintainer. Unblocks redistribution and publication.
- **Publishing:** requires explicit owner authorization. The global operating rules forbid autonomous commits, pushes, and publication.

No technical blocker prevents local use of the current package.

## Next Actions

1. Run `bash tests/run_tests.sh` and save the final output to `docs/test-results.txt`.
2. Run `tests/acceptance.md` checks 1–15 in OpenCode and one second client; record results.
3. Build and inspect the clean distributable ZIP with `make package`.
4. Ask the owner to choose a license before any publication.
5. Ask the owner before any Git initialization, commit, push, or publication.

## Release Status

**v0.2.0 local integration:** implemented and locally tested. Not published. Manual acceptance, cross-model validation, and the license decision remain pending.

Distributable artifact: `dist/super-mega-brainstorm-skill-0.2.0.zip`.
