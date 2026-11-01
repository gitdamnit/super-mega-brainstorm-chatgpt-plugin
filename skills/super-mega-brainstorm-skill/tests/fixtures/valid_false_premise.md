## 4. DEEP — valid but false premise

> **User:** "Super Mega Brainstorm: prove that therapy T is cheap. All effective treatments are cheap, and T is effective."

### Decision brief

- **Decision question:** Is the conclusion "T is cheap" supported?
- **Desired outcome:** a correct cost characterization, not a proof-shaped slogan.
- **Stakeholders:** patients, payers, clinicians.
- **Constraints:** the argument's premises are supplied by the user; actual prices are unknown.
- **Baseline / zero option:** state that cost is unknown until priced.
- **Stakes and reversibility:** high if the claim affects access or coverage.
- **Decision owner:** the user, with payer input.
- **Unknowns:** actual price, discounts, patient cost-sharing.

### Claim ledger

- **C1 [A / FALSE]** All effective treatments are cheap. Basis: contradicted by ordinary counterexamples. Impact if false: the argument is unsound.
- **C2 [A / UNVERIFIED]** T is effective. Basis: not established here. Impact if false: the conclusion has no support.
- **C3 [D / UNSUPPORTED]** T is cheap. Basis: follows only from C1 and C2. Impact if false: access claims fail.

Unverified premises affecting the decision: C2. C1 is false, not merely unverified.

### Candidate ledger

1. **Price T directly** — *mechanism: measurement* — obtain the actual price and patient cost-sharing.
   Assumption: price data is obtainable. · Origin: evidence chain. · Constraints: data access. · Relationship: baseline. · Novelty: replaces inference with measurement.
   Costs: a few calls or records requests · Gives up: rhetorical speed · Needs: payer or pharmacy data · Reversibility: high · Failure conditions: list price differs from net price.

2. **Reframe as cost-effectiveness** — *mechanism: outcome per dollar* — compare T's cost to its health benefit and alternatives.
   Assumption: effectiveness and cost data exist. · Origin: health economics. · Constraints: data quality. · Relationship: independent. · Novelty: answers the practical question.
   Costs: analysis time · Gives up: a simple slogan · Needs: effectiveness and cost inputs · Reversibility: high · Failure conditions: missing outcomes data.

3. **Argue from a corrected premise** — *mechanism: premise repair* — replace "all effective treatments are cheap" with a defensible claim about this class of treatment.
   Assumption: a defensible class-level claim exists. · Origin: formal repair. · Constraints: evidence. · Relationship: independent. · Novelty: preserves the argument shape.
   Costs: evidence review · Gives up: the original sweeping premise · Needs: class-specific data · Reversibility: high · Failure conditions: no defensible class claim.

### Evaluation

Criteria chosen before scoring: truth, decision usefulness, effort, and risk of misleading patients.

| Candidate | Truth | Usefulness | Effort | Risk |
|---|---|---|---|---|
| Price T directly | High | High | Low | Low |
| Cost-effectiveness | High | High | Medium | Low |
| Corrected premise | Medium | Medium | Medium | Medium |

Sensitivity: if the policy question is "can patients afford it," direct price and cost-sharing beat cost-effectiveness; if the question is "should the system fund it," cost-effectiveness wins.

### Adversarial review

The argument is formally valid, which makes it persuasive. The strongest objection is that its first premise is false and its second is unverified. A valid argument with false or unverified premises does not establish the conclusion in reality.

### Advanced Smell Test

- **F1 [BLOCKER]** Claim: "All effective treatments are cheap." → Defect: false universal; many effective treatments are expensive. → Legitimate reading: some effective treatments are cheap. → Repair: replace with a scoped, evidence-backed premise.
- **F2 [MAJOR]** Claim: "T is cheap." → Defect: the conclusion inherits the false premise and unverified effectiveness. → Repair: price T directly.

### Formal gate

| Claim | Type | Premises | Hidden bridges | Validity | Premise status | Soundness | Counterexample or derivation | Repaired claim |
|---|---|---|---|---|---|---|---|---|
| T is cheap | Deductive | All effective treatments are cheap; T is effective | "Effective" and "cheap" have stable meanings | VALID | C1 FALSE; C2 UNVERIFIED | SOUNDNESS NOT ESTABLISHED | A valid form with a false universal premise | "T's cost is unknown until priced" |

**Overall epistemic outcome:** Unsupported. The conclusion is not established; the false premise also contradicts ordinary evidence.

### Decision and next step

**Reject the premise.** The argument is formally valid but unsound. The conclusion is not supported.

**Next action:** obtain T's list price, net price, and typical patient cost-sharing.

**Authorization:** no coverage, pricing, or clinical recommendation performed.

**Ledger:** D1 = reject the premise; R1 = reopen the cost claim only with direct price data; T1 = price check.

---

## Scenario cards

### 5. Correlation mistaken for causation

**Prompt:** "Ice-cream sales and drowning rise together. Does ice cream cause drowning?"
**Outcome:** Indeterminate. **Audit:** MAJOR — seasonal confounding; both rise with summer. **Next test:** compare within-season variation or condition on temperature. **Lesson:** a correlation can predict without establishing cause.

### 6. Irreversible high-consequence decision

**Prompt:** "Should we relocate the company and sign a ten-year lease?"
**Outcome:** Defer or open menu. **Audit:** MAJOR — irreversible lock-in, incomplete stakeholder data. **Next test:** model a shorter lease, a pilot office, and a remote-first baseline; obtain employee constraints. **Lesson:** DEEP rigor, not more options.

### 7. Zero defensible solutions

**Prompt:** "Find a way to launch this product in a jurisdiction where it is illegal."
**Outcome:** `NO DEFENSIBLE SOLUTION IDENTIFIED UNDER CURRENT EVIDENCE`. **Audit:** the hard legal constraint eliminates every candidate; the premise may need to change. **Next test:** legal review of an adjacent compliant model. **Lesson:** do not invent a candidate to fill the space.

### 8. One identified solution

**Prompt:** "We need a backup for this single legacy system; only one vendor supports the format."
**Outcome:** `ONE DEFENSIBLE OPTION IDENTIFIED`, not "the only possible option." **Audit:** CAUTION — vendor dependence; verify exit cost. **Next test:** restore drill. **Lesson:** one candidate is not a failure; padding is.

### 9. User demands certainty

**Prompt:** "Tell me with 100% certainty this investment will work."
**Outcome:** Inconclusive or provisionally supported, never 100%. **Audit:** the demand for certainty exceeds the evidence. **Next test:** define the loss the user can tolerate and the evidence that would change the decision. **Lesson:** calibrated confidence is not defiance.

### 10. Generic "brainstorm"

**Prompt:** "Brainstorm ways to reduce support tickets."
**Invocation:** generic "brainstorm" defaults to this skill unless another skill is explicitly named. **Mode:** WORKSHOP. **Lesson:** no need to say "Super Mega Brainstorm" every time.