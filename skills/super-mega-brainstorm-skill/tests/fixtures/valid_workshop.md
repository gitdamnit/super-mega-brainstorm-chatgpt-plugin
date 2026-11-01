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
