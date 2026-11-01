## Decision brief

- **Decision question:** Is there a lawful way to launch the proposed product in this jurisdiction?
- **Desired outcome:** A compliant launch, or an explicit decision not to launch.
- **Constraints:** The product's core feature is illegal in the target jurisdiction.
- **Baseline / zero option:** Do not launch in that jurisdiction.
- **Decision owner:** Founders.
- **Unknowns:** Whether a compliant adjacent product would serve the same need.

## Claim ledger

- **C1 [F / OBSERVED]** The core feature is prohibited. Basis: counsel's written summary. Impact if false: the constraint may not be hard.
- **C2 [A / UNVERIFIED]** An adjacent compliant product retains enough demand. Basis: no user research. Impact if false: no viable path.

Unverified premises affecting the decision: C2.

## Candidates

`NO DEFENSIBLE SOLUTION IDENTIFIED UNDER CURRENT EVIDENCE`. Every version that preserves the core feature violates the hard legal constraint, and no compliant adjacent version has been validated. What could change this: a legal opinion identifying a compliant mechanism, or user research showing the adjacent product solves the same job.

## Evaluation

Criteria chosen before scoring: legality, user need, cost, reversibility, reputational risk. Legality is a hard gate, not a weighted preference. No weight change can make an illegal candidate acceptable.

## Advanced Smell Test

- **F1 [BLOCKER]** Claim: "A compliant version can keep the core feature." → Defect: the feature itself is prohibited; relabeling does not change the legal category. → Legitimate reading: a different feature might serve the same need. → Repair: investigate the adjacent product, not a workaround.
- **F2 [CAUTION]** Claim: "Users will accept the adjacent product." → Defect: no user evidence. → Repair: interview target users before building.

The BLOCKER remains until the core feature is removed or the law changes.

## Formal gate

**NOT APPLICABLE** — the conclusion is a legal and empirical constraint, not a decision-critical deductive argument.

## Decision and next step

**NO DEFENSIBLE SOLUTION IDENTIFIED.** The core feature is prohibited and the compliant alternative is unvalidated.

**What would change this:** a written legal opinion plus evidence that the adjacent product serves the same need.

**Next action:** obtain a written legal opinion on the adjacent product and interview five target users.

**Authorization:** no launch, filing, or legal workaround performed.
