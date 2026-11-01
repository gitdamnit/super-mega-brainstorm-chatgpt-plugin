# SUPER MEGA BRAINSTORM SKILL™

**Advanced Smell Test NOW INCLUDED**

Model-agnostic, local-first Agent Skill. Invoke **“Super Mega Brainstorm”** (including natural variations), or **“brainstorm”** when no other specific named brainstorming skill is explicitly requested. A capable agent with the complete folder installed/loadable executes the full workflow: framing, epistemics, divergent methods, synthesis, responsible evaluation, adversarial challenge, and mandatory fallacy / formal reasoning gates.

## What this release is

This is **v0.2.0, a feature-complete prototype** of the reasoning package, *not a scientifically validated guarantee of error-free conclusions*. The fallacy atlas and formal guide are bundled locally, along with an offline argument checker and structural tests. No links or external APIs are necessary to run the core workflow. Some facts may still require external verification when a task depends on them.

## Local integration of v0.2.0

This local build starts from the exact **GPT-6 v0.2.0 replacement package** and keeps its behavioral specification authoritative: every recognized invocation runs stages 0–10, there is no abbreviated mode, no numeric idea quota, no compulsory absurd option, and no mandatory winner.

Additive engineering that does not change that specification:

- `references/rubric.md` — reasoning-integrity rubric, adapted to the v0.2.0 workflow.
- `references/examples.md` — calibrated scenarios, including zero/one-defensible-solution, insufficient-evidence science, valid-but-false premise, and correlation/causation.
- `references/facilitation.md` — group and user-plus-model facilitation without creating a separate abbreviated workflow.
- `scripts/lint_output.py` — structural linter for the v0.2.0 invariants; not a semantic quality certificate.
- `scripts/categorical_checker.py` — optional finite-model categorical checker with explicit limits; the manual countermodel method remains authoritative.
- `tests/acceptance.md`, `tests/test_lint_output.py`, `tests/test_categorical_checker.py`, fixtures, CI, Makefile, and project documentation.

The original DeepSeek/OpenCode implementation contributed mechanism tracking, cost/dependency analysis, decision genealogy, overturn conditions, facilitation, and engineering patterns. Those are integrated as methodology in the references, not as a replacement for the v0.2.0 behavioral spec. See `docs/INTEGRATION_MATRIX.md` and `docs/INTEGRATION_REPORT.md`.

The package does **not** choose a license on the maintainer's behalf. No license file is included.

## Contents

```text
super-mega-brainstorm-skill/
├── SKILL.md                        Agent Skills frontmatter + workflow / invocation
├── README.md                       This file
├── MIGRATION.md                    Backup-first replacement procedure
├── CHANGELOG.md                    Local integration change summary
├── PRODUCT_REQUIREMENTS.md         Integrated requirements
├── DECISION_LOG.md                 Append-only decision history
├── PROJECT_STATUS.md               Current status and limitations
├── references/
│   ├── techniques.md               Divergent thinking and search-space exploration
│   ├── evaluation-and-workflow.md  Evaluation, decisions, genealogy, overturn conditions
│   ├── evidence-and-epistemics.md  Evidence, causality and bias calibration
│   ├── fallacy-atlas.md            Advanced Smell Test, categories and aliases
│   ├── formal-argument-guide.md    Validity, soundness, syllogisms, outcomes
│   ├── source-inventory.md         Attribution/provenance, NOT a runtime fetch-list
│   ├── rubric.md                   Reasoning-integrity rubric
│   ├── examples.md                 Calibrated scenarios
│   └── facilitation.md             Group and user-plus-model facilitation
├── assets/
│   └── session-template.md         Optional durable brainstorming record
├── scripts/
│   ├── argument_checker.py         Optional propositional truth-table check
│   ├── categorical_checker.py      Optional finite-model categorical check
│   ├── lint_output.py              Structural linter for the v0.2.0 invariants
│   └── validate_package.py         Structural validator
├── tests/
│   ├── run_tests.sh                Run offline checks
│   ├── test_logic.py
│   ├── test_package.py
│   ├── test_lint_output.py
│   ├── test_categorical_checker.py
│   ├── acceptance.md
│   └── fixtures/
├── docs/
│   ├── INTEGRATION_MATRIX.md
│   ├── INTEGRATION_REPORT.md
│   └── VERIFICATION_REPORT.md
├── Makefile
└── .github/workflows/ci.yml
```

**The complete extracted directory is the installable skill.** `SKILL.md` alone is not the full product. Missing local required references must be disclosed rather than papered over with fabricated compliance. Don't attempt to give a chatbot a ZIP and assume it extracted it unless its environment can actually read archived files.

## Install / use

1. Extract the ZIP.
2. Place the resulting **whole** `super-mega-brainstorm-skill/` folder into the skills location recognized by your host, or provide the folder to an agent that can read local files. Exact paths vary by agent implementation.
3. Invoke **“Super Mega Brainstorm: [topic]”**, **“brainstorm [topic]”**, or the invocation rules in `SKILL.md`.
4. Full-fidelity run requires the five core references: techniques, evaluation, evidence, fallacy atlas, formal argument guide. Source inventory and session template are supplementary.

No OpenCode, Claude, Gemini, GPT, DeepSeek, or Mistral-specific adapter required for the core reasoning workflow. **Automatic discovery is a feature of the host, not the Markdown itself**; the host must load or expose the skill. Optional Python scripts only perform more reliable *formal syntax/inference* checks, not the thinking process.

## Test package

```bash
cd super-mega-brainstorm-skill
bash tests/run_tests.sh
python3 scripts/argument_checker.py --premise 'P -> Q' --premise 'Q' --conclusion 'P'
python3 scripts/categorical_checker.py --premise 'All M are P' --premise 'All S are M' --conclusion 'All S are P'
python3 scripts/lint_output.py tests/fixtures/valid_workshop.md --mode workshop
```

Tests prove that files are present, that the linter checks the documented structural invariants, and that the checkers evaluate selected formal forms. They do **not** prove that an arbitrary model will obey routing, classify fallacies correctly, or identify true premises. Those require model-in-the-loop acceptance testing. Package validation is not client-compatibility certification.

## Invariants

- No numeric quota or promised number of ideas; zero or one viable candidate is a legitimate outcome.
- Exploration and criticism are separate operations. Escalation increases *scrutiny*, not the *idea count*.
- Do-nothing/defer remains a comparator, not a magically acceptable answer.
- Do not prove an empirical prediction by syllogism. Test inference **and** premises.
- No invented studies, citations, tool executions, proof results, or source checks.
- Respect requested different named skill; generic `brainstorm` defaults here.
- Never silently degrade full package to partial `SKILL.md`-only execution.

## Migration from previous OpenCode project

See `MIGRATION.md` for a **backup-first** procedure targeting `/home/evan/Projects/super-mega-brainstorm-skill/`. Existing `.git`, checkpoints, and historical artifacts should be preserved in the backup. The release ZIP intentionally omits `.opencode` state, `.git-that-shit` snapshots, and local config. Nothing on your computer is changed merely by downloading the ZIP.

## Source/license note

The technique taxonomy is a new synthesis informed by many public skills; source acknowledgments are in `references/source-inventory.md`. Do not assume the source projects' text/code is freely reusable without checking their licenses. This package's own text and scripts are supplied for your use; a repository publication license should be chosen deliberately by its maintainer. This local integration does not choose or add a license.
