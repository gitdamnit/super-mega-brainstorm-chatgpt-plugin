# Integration Report

## Executive summary

This build starts from the exact **GPT-6 v0.2.0 replacement package** and keeps its behavioral specification authoritative. The DeepSeek/OpenCode implementation contributed mechanisms and engineering, not a competing workflow.

The integration is deliberately conservative:

- v0.2.0 `SKILL.md`, references, assets, migration guide, propositional checker, and existing tests are preserved.
- Additions are either new files or clearly scoped sections in v0.2.0 references.
- No SPARK mode, no abbreviated audit, no numeric idea quota, no compulsory absurd option, no mandatory winner, and no unilateral license.
- The package version remains `0.2.0`; local changes are documented separately.

## Source provenance

| Source | Location | Status |
|---|---|---|
| GPT-6 v0.2.0 replacement | `/home/evan/Downloads/super-mega-brainstorm-skill-replacement-v0.2.0.zip` | Authoritative. SHA-256 `d55cde4400ce3ed39e0de624296dfea06d74c3967a0c4700c5e34b8adcb64370`. |
| DeepSeek/OpenCode v2 | Pre-rebase project | Source of mechanisms/engineering. Backup: `/home/evan/Projects/backups/super-mega-brainstorm-skill-2026-10-31-pre-v0.2.0-rebase.tar.gz`. |
| Earlier six-section integration | Retired | Backup in the same archive. Its SPARK mode, abbreviated audit, rigid contract, and MIT license conflicted with v0.2.0. |
| Pre-integration v2 snapshot | GTS `d53f2f2` | Recoverable pre-rebase state. |

The v0.2.0 ZIP was copied to `/home/evan/Projects/backups/super-mega-brainstorm-skill-replacement-v0.2.0.zip` for preservation.

## What was preserved from v0.2.0

- `SKILL.md` invocation contract, routing priority, stages 0–10, invariants, execution guarantee, package completion gate, and portability requirement.
- `references/techniques.md`, `evaluation-and-workflow.md`, `evidence-and-epistemics.md`, `fallacy-atlas.md`, `formal-argument-guide.md`, `source-inventory.md`.
- `assets/session-template.md`, `MIGRATION.md`, `README.md` (with additive contents and integration notes).
- `scripts/argument_checker.py` unchanged.
- `scripts/validate_package.py` extended while preserving its `REQUIRED` list and `validate(root)` API.
- `tests/test_logic.py` and `tests/test_package.py` unchanged.

## What was salvaged from DeepSeek/OpenCode, and why

| Mechanism | Why it survived | How it was integrated |
|---|---|---|
| **Mechanism map and candidate tracking** | Prevents cosmetic variation and forces each candidate to state its distinctive assumption. | Added a candidate record section to `references/techniques.md`: mechanism, assumption, origin, constraints, relationship, novelty, costs. |
| **`Costs / Gives up / Needs`** | Compact, checkable, honest about tradeoffs. | Added a cost/sacrifice/dependency section to `references/evaluation-and-workflow.md`. |
| **Kill/park distinction** | Prevents permanent elimination on an untested assumption. | Extended into a six-status decision genealogy with reopen conditions. |
| **Overturn conditions** | Turns a recommendation into a falsifiable claim. | Added a foundational overturn-condition section with load-bearing assumption, supporting/contradicting evidence, decision flip, and feasibility. |
| **Facilitation** | Independent collection, anchoring prevention, dissent, and decision ownership are practical. | Added `references/facilitation.md`; one model + one user is the default. |
| **Linter/validator/test/CI/install engineering** | Reproducible verification and packaging. | Rebuilt the linter around v0.2.0 invariants; extended the v0.2.0 validator; added tests, CI, Makefile, install/package targets. |
| **Project documentation discipline** | Traceability and honest status. | Added requirements, decision log, status, integration matrix/report, and verification report. |

## Additive sections in v0.2.0 files

- `references/evaluation-and-workflow.md`: cost/sacrifice/dependency analysis; decision genealogy; overturn conditions; zero/one-defensible-solution protocol; escalation as rigor, not volume; facilitation pointer.
- `references/formal-argument-guide.md`: six final epistemic outcomes with precise definitions; overall outcome mapping; practical-desirability distinction; optional categorical checker note.
- `references/techniques.md`: candidate record and mechanism map.

No v0.2.0 requirement was deleted or reworded to fit the older project.

## New files

- `references/rubric.md` — reasoning-integrity rubric.
- `references/examples.md` — calibrated scenarios and scenario cards.
- `references/facilitation.md` — group and user-plus-model facilitation.
- `scripts/lint_output.py` — structural invariant linter.
- `scripts/categorical_checker.py` — optional finite-model categorical checker.
- `tests/test_lint_output.py`, `tests/test_categorical_checker.py`, fixtures, `tests/acceptance.md`.
- `Makefile`, `.gitignore`, CI workflow.
- `PRODUCT_REQUIREMENTS.md`, `DECISION_LOG.md`, `PROJECT_STATUS.md`, this report, the integration matrix, and the verification report.

## Conflicts resolved

| Conflict | Resolution |
|---|---|
| SPARK / quick mode vs. “no abbreviated brainstorming mode” | Removed SPARK and any abbreviated workflow. |
| Abbreviated audit vs. complete Smell Test | No abbreviated audit. Missing package references trigger an incomplete-installation disclosure, not a shorter audit. |
| Numeric quotas vs. no quota | No quotas; zero, one, or several outcomes allowed. |
| Compulsory absurd option vs. optional wild-tail | Wild-tail remains optional and labeled speculative. |
| Mandatory winner vs. optional recommendation | Recommendation is optional; no-solution and open-menu outcomes are valid. |
| Rigid six-section output vs. v0.2.0 workflow | No rigid schema; the linter checks required reasoning elements and invariants. |
| MIT license vs. no license chosen | No license file or field; maintainer must choose. |
| Categorical automation vs. manual countermodel authority | Separate optional finite-model checker with explicit limits; the manual method remains authoritative. |

## Verification status at the time of this integration report

The paths below were local development evidence, not files in the current plugin distribution. Run the repository test suite and release verifier for current results. The licensing and Git statements below describe the earlier skill integration snapshot; the plugin repository now has committed history and component licenses in root `LICENSES/`.

- Automated unit tests: see `docs/test-results.txt`.
- Package validation: see `docs/validation.json`.
- Fixture lint: see `docs/test-results.txt`.
- Argument checker: see `docs/argument-checker-results.txt`.
- Install smoke: see `docs/install-test.txt`.
- ZIP smoke: see `docs/zip-test.txt`.
- Manual live-client and cross-model acceptance: **not run**.

## Remaining limitations

- The linter is structural; it cannot certify semantic quality or truth.
- The categorical checker is a finite-model aid, not a general first-order prover.
- No live-client or cross-model behavior has been verified.
- At the time of this report, no license had been chosen for the standalone skill snapshot.
- At the time of this report, that standalone snapshot had no Git history, commit, or publication.
