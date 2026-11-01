## Decision brief

- **Decision question:** How should we back up the legacy records system?
- **Desired outcome:** A restorable backup with a tested recovery path.
- **Constraints:** Only one vendor supports the proprietary format; two-week deadline.
- **Baseline / zero option:** Continue with the current untested tape process.
- **Decision owner:** Operations lead.
- **Unknowns:** Restore time and vendor exit cost.

## Claim ledger

- **C1 [F / OBSERVED]** The current tape restore has never been tested. Basis: operations log. Impact if false: the baseline is stronger.
- **C2 [A / UNVERIFIED]** The vendor's restore time meets the recovery objective. Basis: vendor claim, not a drill. Impact if false: the recommendation changes.

Unverified premises affecting the decision: C2.

## Candidates

1. **Vendor-managed backup** — *mechanism: outsourced recovery* — use the sole format-compatible vendor and require a restore drill.
   Assumption: the vendor can meet the recovery-time objective. · Origin: constraint-driven scan. · Constraints: single vendor, two-week deadline. · Relationship: baseline replacement. · Novelty: adds a tested restore path.
   Costs: license plus setup, ~2 engineer-days · Gives up: vendor independence · Needs: a contractual restore-time commitment · Reversibility: medium · Failure conditions: restore exceeds the objective or the vendor exits.

## Evaluation

Criteria chosen before scoring: recoverability, time to restore, cost, vendor risk, deadline fit. Recoverability is a hard gate. The vendor is the only format-compatible path, but that does not make it automatically acceptable.

## Advanced Smell Test

- **F1 [CAUTION]** Claim: "The vendor meets the recovery objective." → Defect: vendor claim, not measured. → Legitimate reading: it is a contractual starting point. → Repair: require a drill before cutover.
- **F2 [CLEAR]** Claim: "Only one vendor supports the format." → No identified defect at the performed depth; the support call is evidence, not a market-wide proof.

## Formal gate

**NOT APPLICABLE** — the decision is a risk judgment under an unverified vendor claim, not a deductive proof.

## Decision and next step

**ONE DEFENSIBLE OPTION IDENTIFIED**, not "the only possible option." The vendor is the only format-compatible path, and a contractual restore drill converts an untested claim into evidence.

**Overturn condition:** if the vendor refuses a restore drill or misses the recovery objective, switch to investigate and keep the tape process until a tested alternative exists.

**Next action:** ask the vendor for a written restore-time commitment and schedule a test restore on a copy.

**Authorization:** no contract signed and no system changed.
