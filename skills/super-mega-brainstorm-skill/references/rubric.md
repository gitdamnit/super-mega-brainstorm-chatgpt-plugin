# Reasoning-Integrity Rubric

Use this to grade a completed Super Mega Brainstorm run. Score each criterion **0, 1, or 2**. Maximum 26. A shippable output scores **20 or higher** and has no zero in the hard-gate rows.

This rubric is for human or model-based evaluation. The package validator and output linter check structure and formal properties; they cannot certify semantic quality, truth, or soundness.

## Hard gates

A zero in any of these means the run is not a completed reasoning pass, regardless of total score.

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 1 | **Framing and baseline** | Restates the prompt; no baseline | Names the problem but omits the zero option or decision owner | Separates problem from proposed solution; states baseline as a comparator, constraints, success evidence, owner, and unknowns |
| 2 | **Claim and evidence calibration** | Facts, guesses, and values blurred | Some statuses, but decisive claims lack basis | Each decisive claim has a label, truth status, basis, scope, and impact if wrong |
| 3 | **Uncertainty and unverified premises** | Unverified claims presented as fact | Some gaps acknowledged | Explicit `UNVERIFIED`/`UNKNOWN` tags, what would settle them, and effect on the decision |
| 4 | **Advanced Smell Test quality** | Missing, or fallacy-name dumping | Findings exist but lack exact defect or repair | Exact claim → mechanism → defect → legitimate reading → repair, across the applicable categories |
| 5 | **Decision honesty** | Forced winner or false certainty | Outcome present but unsupported by evidence | Honest outcome: recommendation, open menu, defer, investigate, reject premise, change problem, one defensible option, or no defensible solution |
| 6 | **Audit scope and agency** | Claims complete audit without required references, or implements without authorization | Scope or authorization stated briefly | Names missing package components/evidence, distinguishes provisional from complete, and states the authorization boundary |

## Judgment criteria

| # | Criterion | 0 | 1 | 2 |
|---|---|---|---|---|
| 7 | **Mechanism diversity** | Cosmetic variants; twins survive | Some distinct mechanisms, some padding | Candidates differ in mechanism; twins are merged or distinguished; saturation is explained without claiming exhaustiveness |
| 8 | **Candidate tracking** | Bare names only | Some fields present | Mechanism, distinctive assumption, origin, constraints, relationships, and novelty recorded |
| 9 | **Cost and dependency honesty** | No costs; invented precision | Costs listed but incomplete | Direct, indirect, opportunity, reversibility, dependencies, second-order effects, and failure conditions as relevant |
| 10 | **Criteria and sensitivity** | Scores before criteria; hidden weights | Criteria stated but sensitivity absent | Criteria chosen before scoring; ordinal reasons; sensitivity and preference dependence shown |
| 11 | **Adversarial challenge** | No serious attack on the favorite | Pre-mortem or rival explanation present | Strongest rival, pre-mortem, disconfirming evidence, and cheapest falsifier are explicit |
| 12 | **Formal argument discipline** | Fake proof; validity confused with truth | Formalization attempted but limits unstated | Validity, premise status, soundness, formalization limits, and practical desirability are separated |
| 13 | **Decision genealogy** | Ideas disappear without reasons | Some rejections recorded | Rejected, deferred, unverified, defensible, and superseded statuses with reopen conditions |

## Score bands

| Score | Verdict |
|---|---|
| 23–26 | Reference standard. Defensible, traceable, honest about limits. |
| 20–22 | Usable. Fix the lowest row before shipping. |
| 14–19 | Not done. The audit or decision outcome is probably decorative. |
| 0–13 | Start over. The reasoning is likely one conclusion in costumes. |

## Red flags

Delete or repair on sight:

- "Proven" when the argument is only valid, probabilistic, or supported.
- "Sound" when a premise is unverified.
- "Full audit" or "complete audit" when a required reference, tool, or evidence source was unavailable.
- A fallacy label with no exact passage and no identified defect.
- A forced winner when the evidence supports an open menu or no solution.
- An invented candidate to avoid an empty result.
- A quota of ideas, a compulsory absurd option, or a mandatory ranking.
- A fake decimal score without measurement.
- "The data shows" without a source, sample, or scope.
- A citation to a source that was not read.
- A recommendation that depends on an unverified premise without saying so.
- Implementation, deployment, or outreach presented as authorized when it was not.
- A simulated panel presented as independent evidence.
- "The only possible option" when the search space was not exhaustively enumerated.

## Self-audit

1. Does the frame add something the user did not already say?
2. Is the baseline genuinely evaluated as a comparator, not assumed acceptable?
3. Which claim, if false, changes the decision? Is it flagged?
4. Are the candidates different in mechanism, or only in adjectives?
5. Did I choose criteria before scoring, or rationalize afterward?
6. What is the strongest case against my conclusion? Did I state it fairly?
7. Did I use a fallacy label as a substitute for explaining the defect?
8. Did I claim validity when I only established that the premises imply the conclusion?
9. Is the outcome supported by the evidence — including zero, one, defer, or inconclusive?
10. Did I claim a complete audit I could not perform?
11. Did I stop before implementation?
12. Will a later reader know why each option was chosen, rejected, or parked?

## Grading notes

- **Do not reward volume.** A short, honest run can score 26.
- **Do not reward confidence.** A calibrated "indeterminate" outranks fake certainty.
- **Do not penalize an empty candidate set.** Zero defensible solutions is a valid result when justified.
- **Do not reward a kill list that kills only the weak decoy.** The strongest rival must be represented.
- **Do not treat the linter as a grade.** A structurally valid output can still be semantically hollow.
- **Do not treat "no known fallacy" as soundness.** It means no defect was identified at the performed depth.
