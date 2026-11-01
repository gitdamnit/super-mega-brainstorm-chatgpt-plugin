# Evaluation, orchestration, and decision logic

## Conflict resolver: compatible rules, not incompatible mandates

Source skills disagree about whether all work needs a design, whether every question must receive human approval, and how many ideas to generate. Resolve by **user intent > stakes > reversibility > time > breadth needed**. Never require serial questions from someone who said to proceed. Never auto-implement because the brainstorming yielded a confident plan.

| Phase | Must produce | Exit test | Recover if blocked |
|---|---|---|---|
| Frame | Objective, stakeholder, constraints, baseline | Can state what success means without naming a solution | Reframe and ask one discriminating question if essential |
| Evidence | Claim/assumption ledger | Decisive facts and uncertainties identified | State unknown, do not manufacture findings |
| Diverge | Different mechanisms, wild tail | Novelty / mechanism diversity | Invert, eliminate, shift boundary |
| Connect | Clusters and hybrids | No duplicate ideas disguised as choices | Merge and restore distinctions |
| Converge | Criteria and defensible finalists | Baseline tested, rankings sensitivity checked | Show contingent rather than categorical ranking |
| Attack | Pre-mortem, strong opponent, cheapest key test | At least one possible falsifier | Label as a value preference if not testable |
| Audit | Claim-level flags and repairs | Material errors repaired, qualified, or blocked | Report unresolved blocker |
| Proof gate | Formalization + validity & truth status | No false proof of empirical truth | NOT DEMONSTRABLE + substantive evidence |
| Close | Recommendation or open menu + next step | User agency preserved; no invisible implementation | End at options or test plan |

## Scorecard: ordinal default

Each finalist gets `Expected benefit | evidence | effort | risk | reversibility | total dependence on uncertain assumptions` rated low / medium / high with **one reason** per dimension. Don't sum ordinal labels into a fake mathematical value. If the user provides measurable values and weights, calculate transparently, including sensitivity. Avoid one-size-fits-all weights.

## Key assumptions test

For each top candidate record:
1. What needs to be true? Name it in a falsifiable way.
2. What observations already support or contradict it?
3. Impact if false (low/medium/high).
4. Confidence with specific grounds (not arbitrary percentages).
5. Fastest ethical test, real-world data needed, and what action follows each result.

Prioritize the highest decision-impact uncertainty that can feasibly be reduced. Experiments may be observational, interview, pilot, simulation, retrospective, or controlled; choose design to match causal and ethical constraints.

## Scientific hypothesis package

A scientific-sounding hypothesis must have: operationally defined concepts, measurable variables or observable consequences, plausible mechanism, rival explanations, controls/confounders, expected effect direction, uncertainty and measurement error, data collection, test threshold/analysis approach, reproducibility provisions, and criteria for updating the claim. In exploratory research, exploratory outcomes can remain exploratory; don't mislabel post-hoc findings as pre-registered confirmation.

## Role council protocol

Optional experts: affected-user advocate, domain/technical expert, operator/maintainer, skeptic, ethicist, experimentalist, financial/effort analyst. Give each the same neutral problem description, independent task criterion, and no pre-declared winner. Each returns strongest idea, weakest assumption, alternative, and disconfirming observation. Detect fake consensus when all simulated roles use the same original reasoning. Real independent sources are preferable to invented agreement.

## Compact capture schema

`I### idea: mechanism, differentiator, assumptions, status`
`C### claim: type, support, strength, freshness, counterevidence`
`D### decision: options, criterion, reason, decision owner, reversal trigger`
`R### rejection: idea, reason, reopen condition`
`T### test: hypothesis, sample, metric, rule, outcome`
`F### fallacy concern: claim, mechanism, justified verdict, repair`
`P### proof: formalization, validity, premises, soundness, model limitations`

Mark each as draft, proposed, approved, superseded, or unknown. If storage is unavailable, paste a 10-line session checkpoint in the reply; never claim saved persistence.

## Negative controls for bullshit audits

- **Legitimate expert testimony** is evidence of a degree, not automatically an authority fallacy.
- **Correlation** can support prediction; it is insufficient alone to establish cause.
- **Nonfalsifiable values** are not scientific claims and don't have to be falsifiable.
- **Anecdotes** can establish existence and suggest hypotheses; they usually can't estimate population frequencies.
- **Inductive inference** can be rational and strong despite not being deductively valid.
- **Counterexamples** to universal claims differ from counterexamples to probabilistic trends.
- **No found fallacy** is not evidence that an argument is sound.
- **Not all disagreement** is bias, and labeling a fallacy is not itself a refutation without demonstrating the defect.

## Cost, sacrifice, and dependency analysis

The compact line is the minimum: `Costs: … · Gives up: … · Needs: …`. Extend it proportionately when the decision warrants:

| Dimension | Question |
|---|---|
| **Direct costs** | Money, hours, materials, compute, fees, headcount. |
| **Indirect costs** | Maintenance, coordination, training, support, compliance, technical debt, reputational load. |
| **Opportunity costs** | What else the same time, money, attention, or political capital could buy. |
| **Reversibility** | How expensive is it to undo? What is locked in? |
| **Dependencies** | People, platforms, permissions, data, suppliers, skills, or luck that must hold. |
| **Resource constraints** | Hard limits on budget, time, capability, authority, or attention. |
| **Uncertain assumptions** | Which assumption, if false, changes the cost materially? |
| **Second-order consequences** | Incentive changes, workarounds, distributional effects, environmental or social spillovers. |
| **Failure conditions** | What would make this fail, and how would we see it early? |

Do not manufacture numerical precision or meaningless scores. A Low/Medium/High rating with a reason is more honest than a fake decimal.

## Decision genealogy

Extend kill/park into a persistent ledger. Each candidate has a status:

| Status | Meaning | Reopen condition |
|---|---|---|
| **Rejected by evidence** | Evidence contradicts a load-bearing assumption or expected benefit | New evidence that reverses the contradiction |
| **Excluded by hard constraint** | Violates law, safety, physics, budget, authority, or a must-not-break | The constraint changes or is shown not to be hard |
| **Viable but deferred** | Good enough, but the timing, sequence, or priority is wrong | A trigger date, resource, or dependency changes |
| **Unverified and requiring investigation** | Plausible, but the decisive assumption is untested | The named test is run |
| **Currently defensible** | Survives the evidence and criteria at the performed depth | New disconfirming evidence or a changed criterion weight |
| **Superseded by better evidence** | A later candidate explains or outperforms it | The better evidence is itself overturned |

**Do not permanently eliminate an idea based solely on an untested assumption.** Say "rejected because assumption X is untested" and record what would reopen it. Parked is not killed; killed is not erased. The original and rejected ideas stay in the ledger so they do not resurface as new discoveries.

## Overturn conditions

For every substantive recommendation or conclusion, record:

- **Load-bearing assumption** — what must be true for the conclusion to hold.
- **Supporting evidence** — what currently supports it, and how strong that support is.
- **Contradicting evidence** — what would count against it.
- **Decision flip** — what evidence or constraint change would change the recommendation.
- **Feasibility** — whether that evidence can realistically be obtained, and how.

Use overturn conditions in the Advanced Smell Test: a conclusion with no possible overturn condition is either a definition, a tautology, a pure value judgment, or an unfalsifiable claim. Do not force one where the concept does not apply.

## Zero and one defensible solution

The search may legitimately end with zero or one defensible candidate. This is not a failure to brainstorm, and it is not permission to invent filler.

When zero candidates survive:

- Report `NO DEFENSIBLE SOLUTION IDENTIFIED UNDER CURRENT EVIDENCE`.
- Say why each candidate fails: evidence, hard constraint, unsafe/illegal, unverified, or outside the decision owner's authority.
- Say what could change the result: new evidence, a changed constraint, a different problem definition, or a different decision owner.
- Name the cheapest investigation that could reopen the space, and what not to do in the meantime.

When one candidate survives:

- Report `ONE DEFENSIBLE OPTION IDENTIFIED`, not "the only possible option."
- Evaluate it against hard constraints and the consequences of inaction.
- Do not imply it must be acceptable merely because it is alone.
- Do not add a weaker candidate to make the set look balanced.

## Escalation: rigor, not volume

Escalate from WORKSHOP to DEEP when:

- The decision is irreversible or high-consequence.
- Evidence is conflicting, missing, or contested.
- The claim is scientific, legal, medical, financial, or safety-critical.
- Stakeholders disagree on values or criteria.
- The user demands certainty that the evidence cannot support.
- The apparent winner depends on one untested assumption.

Escalation adds evidence checks, sensitivity analysis, independent perspectives, formal validation, and pre-registration. It does **not** require more ideas. A DEEP answer may contain fewer candidates than a WORKSHOP answer if the space is genuinely constrained. The complete workflow and the complete Smell Test still run; only the presentation detail changes.

## Facilitation

For a group session or a user-plus-model workshop, use `references/facilitation.md`. The one-model/one-user case is the default; additional people or subagents are optional capabilities, not requirements. Simulated roles are prompts, not independent evidence.
