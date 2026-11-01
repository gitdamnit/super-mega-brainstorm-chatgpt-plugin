# Calibrated Examples

Four full runs and six scenario cards. These are illustrative shapes, not a rigid output template. The complete workflow and the Advanced Smell Test still apply; presentation detail may be compressed.

---

## 1. WORKSHOP — naming a podcast

> **User:** "Super Mega Brainstorm: names for a podcast about overlooked local history. Curious, not academic. 12 episodes banked."

**Assumptions:** solo host, no brand yet, audience is locally curious people rather than historians.

### Decision brief

- **Decision question:** What name should the podcast use?
- **Desired outcome:** a name a stranger repeats correctly after hearing it once, and that signals local-history discovery.
- **Stakeholders:** host, listeners, local interviewees.
- **Constraints:** low budget, no trademark search yet, must work spoken aloud.
- **Baseline / zero option:** keep the working title "Local History Podcast" — clear, forgettable, and searchable only by category.
- **Stakes and reversibility:** low stakes; the name is reversible but costs some early brand equity.
- **Decision owner:** host.
- **Unknowns:** whether local listeners respond to "map" or "history" language.

### Claim ledger

- **C1 [A / UNVERIFIED]** Locals will find a "map" metaphor intuitive. Basis: common cartographic language in local tourism. Impact if false: the name needs a tagline.
- **C2 [E / SUPPORTED]** Short, concrete names are easier to repeat than abstract ones. Basis: general branding practice; not a local test. Impact if false: low.
- **C3 [V / VALUE JUDGMENT]** The host prefers curious over academic. Basis: stated preference. Impact if false: tone changes.

Unverified premises affecting the decision: C1.

### Candidate ledger

1. **The Other Map** — *mechanism: cartographic inversion* — the version of the town not on the tourist sign.
   Assumption: listeners infer "history" from "map." · Origin: boundary-shift lens. · Constraints: none. · Relationship: independent. · Novelty: combines place and hiddenness.
   Costs: low; no trademark check · Gives up: immediate topic clarity · Needs: cover art that shows the inversion · Reversibility: high · Failure conditions: people think it is a travel show.

2. **The Back Row** — *mechanism: underdog framing* — the history that never made the front row.
   Assumption: the underdog frame reads as curious, not political. · Origin: inversion. · Constraints: none. · Relationship: independent. · Novelty: warm and human.
   Costs: low · Gives up: searchability · Needs: a tagline to carry "history" · Reversibility: high · Failure conditions: sounds like a sports show.

3. **Lost & Found** — *mechanism: recovery framing* — a weekly recovery of something the town forgot.
   Assumption: the phrase is not too generic to own. · Origin: resource raid. · Constraints: crowded phrase. · Relationship: twin of #1 in promise, weaker in distinctiveness. · Novelty: low.
   Costs: low · Gives up: distinctiveness · Needs: strong episode titles · Reversibility: high · Failure conditions: lost in search results.

4. **Municipal Secrets** — *mechanism: bureaucratic intrigue* — boring council minutes, read like a thriller.
   Assumption: the archive has genuinely weird material. · Origin: worst-idea flip. · Constraints: depends on archives. · Relationship: independent. · Novelty: high, but narrow.
   Costs: low · Gives up: broad appeal · Needs: deadpan delivery · Reversibility: high · Failure conditions: one-note premise.

5. **Hometown Ghosts** — *mechanism: haunted framing* — the traces still walking around.
   Assumption: listeners tolerate a ghost trope without expecting paranormal content. · Origin: analogy raid. · Constraints: genre expectation. · Relationship: independent. · Novelty: medium.
   Costs: low · Gives up: listeners who dislike ghost tropes · Needs: the host to resist going paranormal · Reversibility: high · Failure conditions: wrong-audience mismatch.

### Evaluation

Criteria chosen before scoring: memorability, topic clarity, distinctiveness, searchability, tone fit. Weights: memorability and tone fit are the host's priorities.

| Candidate | Memorability | Clarity | Distinctiveness | Searchability | Tone fit |
|---|---|---|---|---|---|
| The Other Map | High | Medium | High | Medium | High |
| The Back Row | High | Low | Medium | Low | High |
| Lost & Found | Medium | Medium | Low | Low | Medium |
| Municipal Secrets | High | Medium | High | Low | Medium |
| Hometown Ghosts | High | Medium | Medium | Medium | Low |

Sensitivity: if searchability is weighted above tone, "Hometown Ghosts" moves up; if topic clarity is decisive, "Lost & Found" moves up but remains generic.

### Adversarial review

The strongest case against "The Other Map" is that it may sound like a travel show. The cheapest disconfirmation is five locals hearing the name with no context. If three cannot guess history, place, or maps, the name fails the clarity test.

### Advanced Smell Test

- **F1 [CAUTION]** Claim: "The Other Map is clear." → Defect: clarity is inferred from general naming practice, not tested with the target audience. → Legitimate reading: the metaphor may be clear with cover art. → Repair: test with five locals before committing.
- **F2 [CLEAR]** Claim: "Municipal Secrets is narrow." → No identified defect; the narrowness is a real tradeoff, not a reasoning error.

No BLOCKER identified. This is not a truth certificate.

### Formal gate

**NOT APPLICABLE** — the choice is a preference under uncertainty, not a decision-critical deductive claim. No syllogism is required.

### Decision and next step

**Recommendation:** The Other Map. It does the most work with the fewest words and leaves room for the show to grow beyond one topic. Confidence: moderate, based on naming principles rather than local listener data.

**Overturn condition:** if three of five locals cannot guess the show is about history after hearing the name, The Back Row becomes preferable because it is warmer and easier to explain with a tagline.

**Next action:** text the five names to five locals with no context and ask, "What do you think this is?" Pass/fail: at least three say history, place, or maps by tomorrow.

**Authorization:** no brand registration or implementation performed.

**Ledger:** I1–I5 recorded; D1 = provisional choice; R1 = Lost & Found reopened if searchability becomes the top criterion.

---

## 2. WORKSHOP — queue architecture for a small SaaS

> **User:** "Super Mega Brainstorm: we run a small SaaS with a cron-based job queue. It is getting fragile. Should we move to a managed queue, Postgres-backed jobs, Redis streams, or buy a workflow engine? Two engineers, 8k jobs/day, moderate growth."

### Decision brief

- **Decision question:** Which queue architecture should replace the cron system?
- **Desired outcome:** fewer stuck jobs, observable retries, and no on-call burden increase for two engineers.
- **Stakeholders:** two engineers, customers waiting on jobs, finance.
- **Constraints:** two-engineer maintenance budget, 8k jobs/day, existing Postgres, no dedicated ops.
- **Baseline / zero option:** keep cron and add alerting — cheapest now, but does not fix retry or visibility.
- **Stakes and reversibility:** moderate; a queue migration is reversible but expensive after data and workers accumulate.
- **Decision owner:** engineering lead.
- **Unknowns:** growth rate, tolerance for vendor cost, appetite for operating Redis.

### Claim ledger

- **C1 [F / OBSERVED]** Cron jobs fail silently and retries are manual. Basis: current incidents. Impact if false: the baseline is stronger.
- **C2 [E / SUPPORTED]** Postgres-backed queues can handle 8k jobs/day. Basis: known workload range; needs a spike. Impact if false: managed queue wins faster.
- **C3 [A / UNVERIFIED]** Managed queue cost stays under $300/month at projected growth. Basis: vendor list price, not a negotiated quote. Impact if false: cost criterion changes.
- **C4 [V / VALUE JUDGMENT]** The team prefers fewer moving parts over lowest marginal cost. Basis: stated maintenance constraint.

Unverified premises affecting the decision: C3.

### Candidate ledger

1. **Keep cron, add alerting** — *mechanism: observe the existing system* — baseline; no migration.
   Assumption: failures are visible enough to alert on. · Origin: zero option. · Constraints: no retry semantics. · Relationship: baseline. · Novelty: none.
   Costs: ~2 engineer-days · Gives up: retry automation · Needs: good logs · Reversibility: high · Failure conditions: silent failures continue.

2. **Managed queue** — *mechanism: outsource operations* — hosted queue with retries and dashboards.
   Assumption: cost stays within budget. · Origin: opportunity map. · Constraints: vendor dependency. · Relationship: independent. · Novelty: removes ops burden.
   Costs: ~$150–300/mo, low ops · Gives up: some control and portability · Needs: vendor reliability and a migration plan · Reversibility: medium · Failure conditions: cost spike or lock-in.

3. **Postgres-backed jobs** — *mechanism: reuse existing infrastructure* — a jobs table, workers, and `SKIP LOCKED`.
   Assumption: 8k/day is well within Postgres capacity. · Origin: resource raid. · Constraints: database load and schema ownership. · Relationship: independent. · Novelty: no new service.
   Costs: ~1–2 engineer-weeks, low cash · Gives up: database simplicity · Needs: worker discipline and monitoring · Reversibility: high · Failure conditions: queue traffic competes with product queries.

4. **Redis streams** — *mechanism: dedicated in-memory log* — consumer groups and pending-entry recovery.
   Assumption: the team can operate Redis safely. · Origin: analogy raid from event systems. · Constraints: new stateful service. · Relationship: independent. · Novelty: strong throughput and replay.
   Costs: ~2 engineer-weeks + hosting, medium ops · Gives up: operational simplicity · Needs: Redis expertise · Reversibility: medium · Failure conditions: memory pressure or data-loss configuration.

5. **Buy a workflow engine** — *mechanism: buy orchestration* — hosted workflow with retries, schedules, and observability.
   Assumption: the workflow model fits the jobs. · Origin: vendor scan. · Constraints: cost and abstraction mismatch. · Relationship: hybrid with managed queue. · Novelty: visual operations.
   Costs: higher license, low ops · Gives up: control and simplicity · Needs: workflow fit and budget · Reversibility: low · Failure conditions: paying for features the team does not use.

### Evaluation

Criteria chosen before scoring: reliability, engineering effort, operating burden, cost, reversibility, fit with two engineers. Weights: operating burden and reliability are the lead's priorities.

| Candidate | Reliability | Effort | Ops burden | Cost | Reversibility | Fit |
|---|---|---|---|---|---|---|
| Cron + alerting | Low | Low | Low | Low | High | Low |
| Managed queue | High | Medium | Low | Medium | Medium | High |
| Postgres jobs | Medium | Medium | Low–Medium | Low | High | High |
| Redis streams | High | High | High | Medium | Medium | Medium |
| Workflow engine | High | Medium | Low | High | Low | Medium |

Sensitivity: if cash is the binding constraint, Postgres jobs wins; if the growth forecast doubles, managed queue wins more clearly; if operating Redis is unacceptable, Redis streams drops out.

### Adversarial review

The strongest case against the managed queue is vendor lock-in and a cost spike after the trial. The cheapest disconfirmation is a quote plus a two-week load spike at 3× current volume. If the quote exceeds $500/month, Postgres jobs wins on cash and reversibility.

### Advanced Smell Test

- **F1 [MAJOR]** Claim: "Managed queue stays under $300/month." → Defect: based on list price and projected volume, not a quote or load test. → Legitimate reading: it is a planning estimate. → Repair: obtain a quote and run a two-week spike before committing.
- **F2 [CAUTION]** Claim: "Postgres can handle 8k jobs/day." → Defect: likely true but untested with this schema and query mix. → Repair: benchmark with production-like load.
- **F3 [CLEAR]** Claim: "Redis adds operational burden." → No identified defect; it is a reasonable inference from the team's constraints, not a measured fact.

No unresolved BLOCKER. The recommendation is conditional on the quote and spike.

### Formal gate

**NOT APPLICABLE** — the decision is an inductive tradeoff, not a deductive proof. The premises are empirical and the conclusion is a practical recommendation.

### Decision and next step

**Recommendation:** Managed queue, conditional on the quote and load spike. It gives the largest reliability gain per engineering hour and matches the two-engineer operating constraint. Postgres jobs is the strongest runner-up and remains the fallback.

**Confidence:** moderate; the cost and load assumptions are unverified.

**Overturn condition:** if the managed queue quote exceeds $500/month at 8k jobs/day, Postgres jobs wins because it preserves cash and reversibility at a manageable engineering cost.

**Next action:** request a managed-queue quote and run a two-week load spike at 3× current volume.

**Authorization:** no migration or vendor purchase performed.

**Ledger:** D1 = provisional managed queue; R1 = Postgres jobs reopened if cost exceeds the threshold; T1 = load spike.

---

## 3. DEEP — a sleep supplement claim with insufficient evidence

> **User:** "Super Mega Brainstorm: a small pilot says compound X improves sleep. Should we claim it works?"

### Decision brief

- **Decision question:** Should the team claim that compound X improves sleep in adults?
- **Desired outcome:** a defensible public claim, or no claim.
- **Stakeholders:** users, researchers, regulators, the company.
- **Constraints:** one small pilot, no replication, no access to the full dataset.
- **Baseline / zero option:** make no efficacy claim and describe the evidence as preliminary.
- **Stakes and reversibility:** high; a public health claim is hard to retract.
- **Decision owner:** research and communications leads.
- **Unknowns:** effect size, blinding, attrition, publication status.

### Claim ledger

- **C1 [E / SUPPORTED]** A small pilot reported improved sleep. Basis: supplied summary; strength weak; no full dataset. Impact if false: the claim collapses.
- **C2 [A / UNVERIFIED]** The pilot was adequately blinded and controlled. Basis: not stated. Impact if false: placebo and expectancy explain the result.
- **C3 [U / UNKNOWN]** The result replicates in a larger sample. Basis: no replication. Impact if false: no general claim.
- **C4 [V / VALUE JUDGMENT]** The team prefers a conservative public claim. Basis: stated risk appetite.

Unverified premises affecting the decision: C2, C3.

### Candidate ledger

1. **No efficacy claim** — *mechanism: evidence threshold* — describe the pilot as preliminary and make no health claim.
   Assumption: the product can launch without an efficacy claim. · Origin: baseline. · Constraints: marketing may be weaker. · Relationship: baseline. · Novelty: none.
   Costs: lower marketing upside · Gives up: a strong claim · Needs: alternative positioning · Reversibility: high · Failure conditions: commercial pressure to overclaim.

2. **Claim "may support sleep"** — *mechanism: qualified claim* — use hedged language with a link to the pilot.
   Assumption: the evidence clears the regulatory and scientific bar for a qualified claim. · Origin: legal review. · Constraints: jurisdiction-specific. · Relationship: independent. · Novelty: moderate.
   Costs: legal review, monitoring · Gives up: simplicity · Needs: regulatory approval and full data · Reversibility: medium · Failure conditions: regulator rejects the wording.

3. **Run a replication first** — *mechanism: evidence generation* — delay the claim until a larger, pre-registered study reports.
   Assumption: the team can fund and wait for a replication. · Origin: scientific hypothesis package. · Constraints: time and cost. · Relationship: independent. · Novelty: highest evidence value.
   Costs: study cost, delay · Gives up: speed · Needs: protocol, sample, funding · Reversibility: high · Failure conditions: replication is underpowered.

4. **Publish the pilot as a case study** — *mechanism: transparent exploration* — report the pilot with limitations and no causal claim.
   Assumption: transparency does not itself imply efficacy. · Origin: evidence chain. · Constraints: privacy and consent. · Relationship: hybrid with #1. · Novelty: builds trust.
   Costs: writing and review · Gives up: marketing punch · Needs: full methods · Reversibility: high · Failure conditions: readers infer efficacy anyway.

### Evaluation

Criteria chosen before scoring: evidential support, regulatory risk, user safety, commercial value, reversibility. Weights: evidential support and safety dominate.

| Candidate | Evidence | Regulatory risk | Safety | Commercial value | Reversibility |
|---|---|---|---|---|---|
| No efficacy claim | High | Low | Low | Low | High |
| "May support sleep" | Low–Medium | High | Medium | High | Medium |
| Replication first | High (eventually) | Low | Low | Medium | High |
| Case study | Medium | Medium | Low | Medium | High |

Sensitivity: if the pilot's full data show a large, pre-registered effect, the qualified claim moves up; if the regulator requires a randomized trial, it drops out.

### Adversarial review

The strongest case for claiming efficacy is commercial pressure and the pilot's positive signal. That case fails if the pilot was uncontrolled, unblinded, or underpowered. The cheapest disconfirmation is a methods review and a regulatory opinion; a replication is the stronger but slower test.

### Advanced Smell Test

- **F1 [BLOCKER]** Claim: "Compound X improves sleep." → Defect: a small uncontrolled or unreported pilot cannot support a causal efficacy claim. → Legitimate reading: it is a promising signal. → Repair: downgrade to "preliminary signal; efficacy unknown."
- **F2 [MAJOR]** Claim: "The effect is due to the compound." → Defect: placebo, expectancy, regression to the mean, and selection are not ruled out. → Repair: require a controlled replication.
- **F3 [CAUTION]** Claim: "The pilot is generalizable." → Defect: sample and setting are unknown. → Repair: state the population and setting before generalizing.

The BLOCKER remains until the claim is downgraded or stronger evidence is produced.

### Formal gate

**NOT APPLICABLE** — the claim is causal and empirical, not a decision-critical deductive argument. A syllogism would not establish efficacy.

### Decision and next step

**Inconclusive.** The pilot is too weak to support an efficacy claim, and the commercial decision depends on regulatory advice not yet obtained.

**What would settle it:** a full methods review, a pre-registered replication, and a regulatory opinion on any proposed wording.

**Next action:** obtain the full protocol and dataset; commission a regulatory review.

**Authorization:** no public claim, filing, or marketing change performed.

**Ledger:** D1 = no claim until review; R1 = qualified claim reopened only with regulatory approval and stronger evidence; T1 = methods review.

---

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
