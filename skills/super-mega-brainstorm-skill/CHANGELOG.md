# Changelog

This package is based on the GPT-6 v0.2.0 replacement. The behavioral specification remains v0.2.0; this changelog records additive local engineering.

## v0.2.0 — local integration (2026-10-31)

### Preserved from v0.2.0

- `SKILL.md` invocation contract, stages 0–10, full-workflow guarantee, no abbreviated mode, no numeric idea quotas, optional wild-tail, zero/one/multiple outcomes, and no mandatory winner.
- `references/techniques.md`, `evaluation-and-workflow.md`, `evidence-and-epistemics.md`, `fallacy-atlas.md`, `formal-argument-guide.md`, `source-inventory.md`.
- `assets/session-template.md`, `MIGRATION.md`, `README.md`.
- `scripts/argument_checker.py` (propositional truth-table checker) and `scripts/validate_package.py` (extended without changing its public `validate(root)` API).
- `tests/test_logic.py` and `tests/test_package.py`.

### Added

- `references/rubric.md` — reasoning-integrity rubric adapted to the v0.2.0 workflow.
- `references/examples.md` — calibrated scenarios: creative, technical, insufficient-evidence science, valid-but-false premise, correlation/causation, irreversible decision, one solution, zero solutions, certainty demand, generic brainstorm.
- `references/facilitation.md` — group and user-plus-model facilitation without a separate abbreviated mode.
- `scripts/lint_output.py` — structural linter for v0.2.0 invariants: no quotas, no compulsory absurdity, no mandatory winner, complete-workflow elements, audit disclosure, formal-gate disclosure, authorization boundary.
- `scripts/categorical_checker.py` — optional finite-model categorical checker with explicit limits; the manual countermodel method remains authoritative.
- `tests/test_lint_output.py`, `tests/test_categorical_checker.py`, fixtures, `tests/acceptance.md`.
- `Makefile`, `.gitignore`, CI workflow.
- `PRODUCT_REQUIREMENTS.md`, `DECISION_LOG.md`, `PROJECT_STATUS.md`, `docs/INTEGRATION_MATRIX.md`, `docs/INTEGRATION_REPORT.md`, `docs/VERIFICATION_REPORT.md`.

### Extended without changing the behavioral spec

- `references/evaluation-and-workflow.md` — cost/sacrifice/dependency analysis, decision genealogy, overturn conditions, zero/one-defensible-solution protocol, escalation as rigor not volume, facilitation pointer.
- `references/formal-argument-guide.md` — six final epistemic outcomes (`supported`, `provisionally supported`, `unsupported`, `contradicted`, `invalid inference`, `indeterminate`) with precise definitions, an outcome-mapping table, and a note on practical desirability.
- `references/techniques.md` — candidate record and mechanism-map fields: core mechanism, distinctive assumption, origin, constraints, relationship, novel contribution, costs.

### Not changed

- No license was chosen or added. The maintainer must choose deliberately.
- No publication, Git initialization, commit, or push was performed.
- No claim of model behavior or client compatibility is made from package validation alone.
- The exact v0.2.0 behavioral requirements were not rewritten to fit the older DeepSeek/OpenCode contract.

### Known limitations

- The linter and validator check structure and selected formal properties, not semantic quality or truth.
- The categorical checker is a finite-model aid, not a general first-order prover.
- Live-client and cross-model acceptance testing remain pending.
