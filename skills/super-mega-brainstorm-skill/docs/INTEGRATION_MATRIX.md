# Integration Matrix

## Source status

| Source | Status | Use |
|---|---|---|
| **GPT-6 v0.2.0 replacement** | Supplied at `/home/evan/Downloads/super-mega-brainstorm-skill-replacement-v0.2.0.zip`; SHA-256 `d55cde4400ce3ed39e0de624296dfea06d74c3967a0c4700c5e34b8adcb64370`. | **Authoritative behavioral specification.** |
| **DeepSeek/OpenCode v2** | Pre-integration project, backed up at `/home/evan/Projects/backups/super-mega-brainstorm-skill-2026-10-31-pre-v0.2.0-rebase.tar.gz`. | Source of salvageable mechanisms and engineering, not the behavioral spec. |
| **Earlier local integration** | Retired; backed up in the same archive. | Not authoritative; its SPARK mode, abbreviated audit, six-section contract, and MIT license conflicted with v0.2.0. |

## Functional comparison

| Capability | DeepSeek/OpenCode v2 | GPT-6 v0.2.0 | Conflict | Action | Rationale |
|---|---|---|---|---|---|
| **Invocation** | `brainstorm` and variants | Explicit Super Mega Brainstorm variations; generic `brainstorm` unless another named skill; routing priority | None if v0.2.0 is followed | **Preserve v0.2.0** | The authoritative routing is more precise and includes name-only and incomplete-installation rules. |
| **Modes** | QUICK, STANDARD, DEEP, FACILITATE | WORKSHOP, DEEP, RED TEAM; no abbreviated mode | Original QUICK/STANDARD conflict with “no abbreviated brainstorming mode” | **Preserve v0.2.0** | Every invocation runs stages 0–10; presentation detail may shrink, required checks may not. |
| **Output shape** | Fixed five sections | Workflow and quality gates, no rigid schema | Direct conflict | **Retire original; preserve v0.2.0** | A rigid schema would silently change the behavioral spec. |
| **Idea quotas** | 4–12 options by mode | No numeric quota; zero/one/several | Direct conflict | **Retire original** | The new quality standard is defensible reasoning, not volume. |
| **Absurd option** | Exactly one compulsory | Optional wild-tail, labeled speculative | Direct conflict | **Retire the mandate; preserve optional wild-tail** | Absurdity is a tool, not a requirement. |
| **Winner/ranking** | Mandatory winner and ranking | Recommendation optional; zero/one/multiple outcomes | Direct conflict | **Retire the mandate** | `NO DEFENSIBLE SOLUTION IDENTIFIED` and open menus are valid. |
| **Mechanism diversity** | Mechanism map, 12 families | Materially distinct mechanisms; candidate tracking | Complementary | **Adapt into v0.2.0** | Add a candidate record: mechanism, distinctive assumption, origin, constraints, relationship, novelty, costs. |
| **Cost analysis** | `Costs / Gives up / Needs` | Criteria, scorecard, assumptions test | Complementary | **Integrate additively** | Add direct/indirect cost, opportunity cost, reversibility, dependencies, second-order effects, failure conditions. |
| **Kill/park** | Kill list + parked list | Rejected-idea ledger and capture schema | Complementary | **Extend into decision genealogy** | Add six statuses and reopen conditions; never kill permanently on an untested assumption. |
| **Overturn conditions** | One per ranking | Key assumptions test and reversal triggers | Complementary | **Make foundational** | Add load-bearing assumption, supporting/contradicting evidence, decision flip, feasibility. |
| **Claim/evidence** | None dedicated | F/E/A/H/V/U/D ledger; truth statuses; evidence chain | v0.2.0 stronger | **Preserve v0.2.0** | It is already the epistemic backbone. |
| **Advanced Smell Test** | None | Fallacy atlas, evidence guide, mandatory audit | v0.2.0 stronger | **Preserve v0.2.0** | The atlas is broader and better grounded than the earlier build. |
| **Formal validation** | None | Validity/soundness, propositional checker, categorical manual method | Complementary | **Preserve + extend** | Add six final outcomes and a separate finite-model categorical checker. |
| **Facilitation** | Group agenda, roles, dissent | Role council, independent perspectives | Complementary | **Add new reference** | One model + one user is the default; groups/subagents are optional. |
| **Linter** | Contract linter with quotas/absurd/winner gates | None | Obsolete gates conflict | **Rebuild around v0.2.0 invariants** | Check required reasoning elements and forbidden patterns, not a template. |
| **Validator** | `validate_skill.py` | `validate_package.py` with `REQUIRED` and `validate(root)` | API conflict if replaced | **Extend v0.2.0 validator** | Preserve tests and add frontmatter, dependency, guardrail, syntax, and distribution checks. |
| **Tests** | 24 tests for the old contract | Propositional tests and package tests | Old assertions conflict | **Preserve v0.2.0 tests; add new tests** | Keep `test_logic.py` and `test_package.py`; add linter, categorical, and acceptance checks. |
| **CI/Makefile** | Present | Absent | Additive | **Add** | Reproducible offline checks, install, and packaging. |
| **Project docs** | Requirements, decisions, status | README and MIGRATION | Additive | **Add** | Preserve decision history and make the integration auditable. |
| **License** | MIT added without authorization | No license; maintainer must choose | Direct conflict | **Preserve v0.2.0; no license** | The owner must choose legal terms. |
| **Version** | 1.0.0 local | 0.2.0 | Conflict | **Keep 0.2.0** | The behavioral spec remains v0.2.0; local changes are documented separately. |

## Recommended integration shape

**Preserve from v0.2.0**

- `SKILL.md` invocation, stages 0–10, invariants, execution guarantee, package completion gate.
- `references/techniques.md`, `evaluation-and-workflow.md`, `evidence-and-epistemics.md`, `fallacy-atlas.md`, `formal-argument-guide.md`, `source-inventory.md`.
- `assets/session-template.md`, `MIGRATION.md`, `README.md` (with additive contents updates).
- `scripts/argument_checker.py`, `scripts/validate_package.py` API.
- `tests/test_logic.py`, `tests/test_package.py`.

**Add from the original, without changing v0.2.0 behavior**

- Candidate record fields in `references/techniques.md`.
- Cost/sacrifice/dependency analysis, decision genealogy, overturn conditions, zero/one-solution protocol, escalation rules, facilitation pointer in `references/evaluation-and-workflow.md`.
- Six final epistemic outcomes and outcome mapping in `references/formal-argument-guide.md`.
- `references/facilitation.md`, `references/rubric.md`, `references/examples.md`.
- `scripts/lint_output.py`, `scripts/categorical_checker.py`, additional tests, CI, Makefile, project docs.

**Retire**

- SPARK/quick modes and abbreviated audits.
- Numeric idea quotas, compulsory absurdity, mandatory winners.
- The rigid six-section output contract.
- The unilateral MIT license.
- Legacy tests that enforce the retired contract.
