# Product Requirements

## Project Identity

**Name:** Super Mega Brainstorm Skill
**Repository:** `/home/evan/Projects/super-mega-brainstorm-skill` (local; no Git remote)
**Licence:** None selected; maintainer decision required
**Maintainer:** Evan Zellner

**Behavioral specification:** GPT-6 replacement v0.2.0 (`super-mega-brainstorm-skill-replacement-v0.2.0.zip`, SHA-256 `d55cde4400ce3ed39e0de624296dfea06d74c3967a0c4700c5e34b8adcb64370`).
**Integration base:** the exact v0.2.0 package, with additive engineering that does not replace its workflow.

## Purpose

Provide a model-agnostic, evidence-aware brainstorming and decision workflow with an integrated Advanced Smell Test. The skill expands the solution space before narrowing it, tracks claims and assumptions, preserves a decision ledger, challenges its own conclusions, and formally validates only genuinely deductive decision-critical arguments.

The package must run offline from local files and must not require proprietary APIs, agent orchestration systems, paid services, or runtime internet access. It must not promise a number of ideas, a compulsory absurd option, or a mandatory winner.

## Intended Users

- Individuals, founders, product teams, and operators facing ambiguous or consequential decisions.
- Researchers and analysts who need explicit evidence calibration, causal caution, and formal-inference discipline.
- Facilitators running group or user-plus-model sessions who need independent collection, dissent, and decision ownership.
- Models invoking the skill, which need a compact orchestration file plus local references and optional deterministic checks.

## Functional Requirements

| ID | Requirement | Acceptance signal |
| --- | --- | --- |
| FR-1 | Preserve the v0.2.0 invocation contract: recognized "Super Mega Brainstorm" variations activate the full workflow; generic "brainstorm" defaults here unless another skill is explicitly named. | `SKILL.md` invocation section; `tests/acceptance.md` checks 1–3; package validator invariant checks. |
| FR-2 | Preserve the full stages 0–10 workflow and the no-abbreviated-mode guarantee. | `SKILL.md` execution protocol and execution guarantee; validator key invariants. |
| FR-3 | Forbid numeric idea quotas, compulsory absurd options, and mandatory winner/ranking language. | `scripts/lint_output.py`; `scripts/validate_package.py`; negative tests. |
| FR-4 | Allow zero, one, or multiple defensible candidates, including `NO DEFENSIBLE SOLUTION IDENTIFIED` and `ONE DEFENSIBLE OPTION IDENTIFIED`. | Valid fixtures; examples; linter tests. |
| FR-5 | Require explicit claim, assumption, unknown, and evidence disclosure. | Linter `no-uncertainty`/`no-claim-ledger`; examples. |
| FR-6 | Require the complete Advanced Smell Test at the depth the evidence allows, with exact claim → mechanism → defect → legitimate reading → repair and severity. | `references/fallacy-atlas.md`; `references/evidence-and-epistemics.md`; linter audit checks. |
| FR-7 | Require the formal argument gate for decision-critical deductive claims; separate validity, premise truth, soundness, empirical verification, and practical desirability. | `references/formal-argument-guide.md`; `scripts/argument_checker.py`; linter formal-gate checks. |
| FR-8 | Disclose missing required local references as an incomplete installation; do not claim the complete workflow or comprehensive Smell Test. | `SKILL.md` incomplete-installation rule; `scripts/validate_package.py`; acceptance check 13. |
| FR-9 | Stop before implementation, deployment, outreach, purchase, or publication without explicit authorization. | Linter `unauthorized-implementation`; acceptance check 14. |
| FR-10 | Remain model-agnostic and offline: no required network, proprietary API, paid service, adapter, or orchestration system. | `SKILL.md` portability requirement; validator no-runtime-URL check. |
| FR-11 | Provide optional deterministic utilities: output linter, propositional checker, categorical finite-model checker, package validator. | `scripts/`; automated tests. |
| FR-12 | Integrate original DeepSeek/OpenCode mechanisms without replacing v0.2.0: mechanism tracking, cost/sacrifice/dependency analysis, decision genealogy, overturn conditions, facilitation. | `references/techniques.md`, `references/evaluation-and-workflow.md`, `references/facilitation.md`; integration report. |
| FR-13 | Document provenance, adaptation, licenses, and the exact source status. | `references/source-inventory.md`; `docs/INTEGRATION_MATRIX.md`; `docs/INTEGRATION_REPORT.md`. |
| FR-14 | Provide reproducible offline tests and manual acceptance scenarios. | `tests/run_tests.sh`; `tests/acceptance.md`; `docs/VERIFICATION_REPORT.md`. |

## Nonfunctional Requirements

| ID | Requirement | Target |
| --- | --- | --- |
| NFR-1 | Portability | Standard Agent Skills frontmatter; no vendor-specific fields required. |
| NFR-2 | Dependency footprint | Python standard library only; no network, API key, or SDK. |
| NFR-3 | Context efficiency | `SKILL.md` under 500 lines; depth in `references/`. |
| NFR-4 | Frontmatter validity | `name: super-mega-brainstorm-skill`; `metadata.version: "0.2.0"`; description present. |
| NFR-5 | Determinism | Same input to each script produces the same output. |
| NFR-6 | Testability | Every hard structural requirement has an automated or manual check. |
| NFR-7 | Honest limits | Linter and checkers report what they cannot establish; no semantic or client-compatibility certification. |
| NFR-8 | Clean distribution | The ZIP excludes `.git`, `.opencode`, `.git-that-shit`, caches, temporary artifacts, and development-state files. |

## Scope and Exclusions

**In scope:**

- The v0.2.0 `SKILL.md` and local references, preserved as the behavioral specification.
- Additive references for rubric, examples, and facilitation.
- Optional linter and categorical checker.
- Extended package validator that preserves the v0.2.0 `validate(root)` API.
- Unit tests, acceptance checks, fixtures, CI, Makefile, install and package targets.
- Integration matrix, integration report, verification report, decision log, requirements, status.

**Out of scope:**

- A hosted service, web UI, database, or model API.
- Automatic client installation.
- Automatic semantic grading of brainstorm quality.
- General first-order theorem proving or empirical verification.
- Publishing, committing, or pushing without explicit authorization.
- Rewriting the v0.2.0 behavioral contract to match the older DeepSeek/OpenCode contract.
- Choosing a license on the maintainer's behalf.

## Technical Constraints

- `SKILL.md` must remain a Markdown file with YAML frontmatter at the root.
- Scripts must run on Python 3.9+ using only the standard library.
- The package must not require a build step to be usable as a skill.
- The linter is structural; it must not pretend to judge idea quality or truth.
- The propositional checker must not claim empirical truth, general first-order validity, or causal certainty.
- The categorical checker is a finite-model aid, not a general first-order prover.
- The skill must remain vendor-neutral; client-specific instructions belong in the README.

## Acceptance Criteria

1. `bash tests/run_tests.sh` exits 0 with all automated tests passing.
2. `python3 scripts/validate_package.py .` exits 0 with no structural problems.
3. All valid fixtures lint clean at their stated mode.
4. The package installs to a temporary directory and the installed copy validates and lints.
5. The propositional checker returns correct valid/invalid results and counterexamples.
6. The categorical checker returns correct finite-model results with explicit limits.
7. The manual acceptance scenarios in `tests/acceptance.md` are run and recorded, or explicitly marked pending.
8. The distributable ZIP excludes development-state files and contains the complete local package.
9. No numeric idea quota, compulsory absurd option, mandatory winner, or unauthorized implementation claim appears in `SKILL.md` or the tests.
10. The v0.2.0 behavioral files are preserved except for documented additive sections.

## Release Objectives

- **v0.2.0 local integration:** Complete the additive engineering, tests, documentation, and clean ZIP without changing the v0.2.0 behavioral contract. Target: complete locally.
- **v0.2.1 candidate:** Live-client and cross-model acceptance; reconcile any behavioral drift.
- **v0.3.0 candidate:** Add domain packs only if they do not reintroduce quotas or bloat the core.
