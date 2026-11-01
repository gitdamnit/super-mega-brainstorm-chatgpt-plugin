# Decision Log

Append-only. Every record that would be expensive to reverse gets an entry. Never edit or delete a past record; append a superseding entry instead.

## How to Use This Log

1. Copy the block below to the end of the `## Decisions` section.
2. Use the next free four-digit ID. IDs are never reused and never renumbered.
3. Date the record the day the decision was actually made (`YYYY-MM-DD`).
4. Record the alternatives you rejected and why. A decision without context is a rumour, not a record.
5. Never rewrite history. If a decision changes, append a superseding record.

```markdown
### D-0001 — Short imperative title

- **Date:** YYYY-MM-DD
- **Status:** Accepted
- **Context:** the situation and the constraint that forced a choice
- **Alternatives Considered:** option A (rejected because ...), option B (rejected because ...)
- **Decision:** what was decided, in one or two sentences
- **Rationale:** why this option wins, including what it costs
- **Consequences:** what follows from it — new constraints, follow-up work, risks
- **Supersedes:** None
```

Allowed statuses: `Proposed`, `Accepted`, `Superseded`, `Deprecated`, `Rejected`.

## Decisions

### D-0001 — Treat GPT-6 v0.2.0 as the authoritative behavioral specification

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The exact `super-mega-brainstorm-skill-replacement-v0.2.0.zip` was supplied after an earlier integration was built against the v0.1.0 draft. The assignment names v0.2.0 as authoritative; the older DeepSeek/OpenCode project is a source of mechanisms and engineering, not the behavioral spec.
- **Alternatives Considered:** Keep the earlier six-section integration (rejected: it imposed SPARK, abbreviated audit, a rigid output contract, and MIT, conflicting with v0.2.0); merge v0.2.0 into the earlier build (rejected: would preserve contradictory behavior); start from v0.2.0 and add only non-conflicting engineering (chosen).
- **Decision:** Re-base the project on the exact v0.2.0 package. Preserve its `SKILL.md`, references, assets, scripts, tests, and migration guide. Add only engineering and methodology that do not change the behavioral contract.
- **Rationale:** The authoritative target must win. Additive engineering can improve testability without rewriting established design decisions.
- **Consequences:** The earlier six-section build is retired and backed up. No SPARK mode, no abbreviated audit, no numeric quotas, no compulsory absurdity, and no mandatory winner.
- **Supersedes:** None

### D-0002 — Preserve v0.2.0 files; additive sections are explicitly marked

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The assignment asks for a stronger unified implementation while forbidding silent changes to established decisions.
- **Alternatives Considered:** Rewrite the v0.2.0 references to a unified style (rejected: risks behavioral drift and loses provenance); leave them untouched and add separate files only (partially chosen); append clearly scoped sections for cost analysis, decision genealogy, overturn conditions, final outcomes, and candidate records (chosen).
- **Decision:** Keep v0.2.0 text intact. Append new sections to `evaluation-and-workflow.md`, `formal-argument-guide.md`, and `techniques.md`; add `rubric.md`, `examples.md`, and `facilitation.md` as new files.
- **Rationale:** The original wording remains auditable, and the additions can be reviewed independently.
- **Consequences:** The integration report must list every additive section and why it does not conflict.
- **Supersedes:** None

### D-0003 — Do not choose a license

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** v0.2.0 has no license field, and its README says the maintainer must choose deliberately. The earlier build added MIT without authorization.
- **Alternatives Considered:** MIT (rejected: unauthorized); Apache-2.0 (rejected: unauthorized); no license (chosen).
- **Decision:** Add no license file and no license field. State the omission in the README and requirements.
- **Rationale:** Choosing legal terms is the owner's decision.
- **Consequences:** The package is not open source until the maintainer chooses. Source attribution remains in `references/source-inventory.md`.
- **Supersedes:** None

### D-0004 — Do not introduce new behavioral modes or abbreviated execution

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The earlier build added SPARK and abbreviated audits. v0.2.0 explicitly forbids an abbreviated brainstorming mode and requires full stages 0–10 on every invocation.
- **Alternatives Considered:** Keep SPARK as a convenience (rejected: conflicts with the authoritative contract); add an explicit "quick" mode (rejected: same conflict); preserve v0.2.0 modes and adjust presentation detail only (chosen).
- **Decision:** No SPARK, no quick mode, no abbreviated audit. WORKSHOP, DEEP, and RED TEAM remain; presentation detail may shrink, but the workflow and audits do not.
- **Rationale:** Escalation changes rigor, not the presence of required checks.
- **Consequences:** The linter does not require a fixed output length; it checks the invariants, not a template.
- **Supersedes:** None

### D-0005 — Add a categorical checker as an optional finite-model aid

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The v0.2.0 formal guide explains categorical countermodels manually and says the propositional script does not automate natural-language syllogisms. The assignment asks to extend the offline checker where appropriate.
- **Alternatives Considered:** Modify the propositional checker's CLI (rejected: breaks v0.2.0 tests and documentation); claim general first-order proof (rejected: false authority); add a separate finite-model checker with explicit limits (chosen).
- **Decision:** Add `scripts/categorical_checker.py` as an optional finite-model checker. It does not replace the manual method and does not claim general first-order validity.
- **Rationale:** It improves repeatability for standard forms without overclaiming.
- **Consequences:** The formal guide and README must state its limits. Tests cover valid, invalid, and existential-fallacy cases.
- **Supersedes:** None

### D-0006 — The output linter checks invariants, not a rigid output template

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** v0.2.0 defines a workflow and quality gates, not a fixed section schema. The earlier linter enforced a six-section contract that v0.2.0 does not require.
- **Alternatives Considered:** Reuse the six-section linter (rejected: imposes non-authoritative structure); no linter (rejected: loses a useful structural check); check for the presence of required reasoning elements and the hard invariants (chosen).
- **Decision:** `scripts/lint_output.py` checks for framing/baseline, claims/uncertainty, candidates or an explicit no-solution result, evaluation criteria, audit findings, formal-gate disclosure, next action/authorization, and the forbidden quota/absurd/winner patterns. It does not require exact headings or order.
- **Rationale:** Structure can be checked without turning v0.2.0 into a template.
- **Consequences:** The linter is structural only; semantic quality remains a human/model judgment.
- **Supersedes:** None

### D-0007 — Preserve the v0.2.0 validator API and add a distribution mode

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** v0.2.0 includes `scripts/validate_package.py` with a `REQUIRED` list and a `validate(root)` function used by `tests/test_package.py`. The project also needs stronger checks and a clean-distribution check.
- **Alternatives Considered:** Replace it with the earlier `validate_skill.py` (rejected: breaks v0.2.0 tests); keep it unchanged (rejected: misses new files and guardrails); extend it while preserving `validate(root)` (chosen).
- **Decision:** Extend `validate_package.py` with frontmatter, dependency, guardrail, syntax, and optional `--distribution` checks. Keep `REQUIRED` and `validate(root)` compatible with v0.2.0 tests.
- **Rationale:** Tests and documented behavior remain stable while validation improves.
- **Consequences:** The source tree may contain `.opencode`/`.git-that-shit`; default validation ignores them. Distribution validation rejects them.
- **Supersedes:** None

### D-0008 — Keep the package version at 0.2.0 and document local integration separately

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The authoritative package is v0.2.0. The local additions are engineering and methodology, not a new behavioral release.
- **Alternatives Considered:** Bump to 1.0.0 (rejected: implies a new authoritative contract); use `0.2.0-integrated` in frontmatter (rejected: non-semver and may confuse clients); keep `0.2.0` and document changes in `CHANGELOG.md` (chosen).
- **Decision:** Keep `metadata.version: "0.2.0"`. Record the local integration in `CHANGELOG.md`, `docs/INTEGRATION_REPORT.md`, and `PROJECT_STATUS.md`.
- **Rationale:** The version identifies the behavioral spec; the changelog identifies the local build.
- **Consequences:** A future version bump should be deliberate and tied to a behavioral change or owner decision.
- **Supersedes:** None

### D-0009 — No commit, push, publish, or deployment without explicit authorization

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The project is not a Git repository. The assignment requires a clean local ZIP but forbids publishing without authorization.
- **Alternatives Considered:** Initialize and commit automatically (rejected: unauthorized); publish the ZIP (rejected: not requested); build and verify a local ZIP only (chosen).
- **Decision:** Do not initialize Git, commit, push, publish, or deploy. Produce and verify a local distributable ZIP.
- **Rationale:** A local artifact satisfies the deliverable without an irreversible publishing action.
- **Consequences:** No commit SHA exists. Verification cites file paths and command output.
- **Supersedes:** None

### D-0010 — Retire the earlier six-section integration

- **Date:** 2026-10-31
- **Status:** Accepted
- **Context:** The earlier build imposed SPARK, abbreviated audits, a rigid six-section contract, and MIT, all conflicting with v0.2.0. It was backed up before the rebase.
- **Alternatives Considered:** Keep it alongside v0.2.0 (rejected: two conflicting behavioral specs); patch only the conflicts (rejected: the contract and license assumptions were load-bearing); replace it with the v0.2.0-based build (chosen).
- **Decision:** Retire the earlier build. The pre-rebase backup remains at `/home/evan/Projects/backups/super-mega-brainstorm-skill-2026-10-31-pre-v0.2.0-rebase.tar.gz`.
- **Rationale:** One authoritative workflow is required.
- **Consequences:** The project directory now reflects the v0.2.0 base plus additive engineering.
- **Supersedes:** None
