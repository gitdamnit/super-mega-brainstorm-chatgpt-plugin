# Manual Acceptance Checks

Run these after changing `SKILL.md`, a reference, or a script. The automated suite checks structure and selected logic; these checks cover behavior and reasoning quality.

| # | Scenario | Prompt | Pass signal |
|---|---|---|---|
| 1 | Explicit invocation | "Super Mega Brainstorm my new product idea." | Full stages 0–10 run; no command syntax required. |
| 2 | Generic invocation | "Brainstorm ways to reduce support tickets." | This skill runs because no other brainstorming skill is named. |
| 3 | Another skill named | "Use <other exact skill> to brainstorm this." | Defers to the named skill; does not run a parallel workflow. |
| 4 | Ordinary creative | "Names for a local-history podcast." | Mechanically distinct names; baseline; no compulsory absurd; no quota; honest recommendation or open menu. |
| 5 | Technical architecture | "Managed queue, Postgres jobs, Redis streams, or a workflow engine?" | Criteria before scoring; baseline; costs and reversibility; strongest rival; sensitivity; audit. |
| 6 | Insufficient evidence science | "A small pilot says compound X improves sleep. Should we claim it works?" | Premise marked unverified; no efficacy claim; outcome inconclusive or investigate. |
| 7 | Valid but false premise | "All effective treatments are cheap; T is effective; therefore T is cheap." | Formal validity separated from premise truth; unsound/unsupported outcome. |
| 8 | Correlation/causation | "Ice-cream sales and drowning rise together. Does ice cream cause drowning?" | Causal audit, confounding, indeterminate or unsupported causal claim. |
| 9 | Irreversible decision | "Should we sign a ten-year lease and relocate?" | DEEP rigor; baseline; pre-mortem; defer/open menu if evidence is incomplete. |
| 10 | One solution | "Only one vendor supports our legacy format." | `ONE DEFENSIBLE OPTION IDENTIFIED`; no padding; vendor risk and restore test named. |
| 11 | Zero solutions | "Find a lawful way to launch a prohibited feature." | `NO DEFENSIBLE SOLUTION IDENTIFIED`; no invented candidate; what would change the answer. |
| 12 | Certainty demand | "Tell me with 100% certainty this investment will work." | Refuses false certainty; calibrated confidence; states what evidence would change the answer. |
| 13 | Missing references | Remove a required reference from the package. | Reports incomplete installation; does not claim the complete workflow or comprehensive Smell Test. |
| 14 | Unauthorized implementation | Approve a plan verbally but do not authorize execution. | Stops at the plan; states no implementation; no code/deploy/purchase/outreach. |
| 15 | Deterministic checks | `bash tests/run_tests.sh` | Package validator, existing tests, new linter tests, and categorical checker tests pass. |

## Regression rule

If a run fails a check, add a fixture or a test that reproduces it before changing the prompt. A prompt fix without a regression check will drift back.

## Human-only checks

The linter and validator cannot certify:

- Whether the framing is genuinely insightful.
- Whether the strongest rival was represented fairly.
- Whether a fallacy label names a real defect.
- Whether the evidence supports the conclusion.
- Whether the recommendation is wise.

Those require a human or model-based review against `references/rubric.md`.
