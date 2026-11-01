# Formal Argument & Syllogism Gate

**Purpose:** Make key inferential leaps explicit and test them when formalization is appropriate. A formal proof confirms a relation among abstract propositions, not whether those propositions describe the world.

## 1. Triage claim type before formalizing

- **Deductive:** Conclusion claimed to follow necessarily from premises. Apply validity/countermodel tests.
- **Inductive or statistical:** Data support probability or generalization. Assess representativeness, uncertainty, and rivals; a syllogism is not a proof of the empirical result.
- **Abductive:** Best available explanation. Compare alternatives and predictive performance; not deductive proof.
- **Causal:** Identify mechanisms, confounders, counterfactuals, and research design.
- **Normative/ethical:** Expose value premises and impacts. Logic cannot prove the values are objectively mandated.
- **Preference/aesthetic/creative:** Clarify values; `NOT DEMONSTRABLE / NOT APPLICABLE` often fits.

## 2. Validity versus soundness

**Valid** means there is **no** interpretation where every premise is true and the conclusion false. **Sound** means valid **and** all premises are actually true. An invalid argument may accidentally reach a true conclusion. A valid argument with a false premise does not establish its conclusion in reality.

- Modus ponens: `P -> Q`, `P`, therefore `Q`. VALID.
- Modus tollens: `P -> Q`, `NOT Q`, therefore `NOT P`. VALID.
- Hypothetical syllogism: `P -> Q`, `Q -> R`, therefore `P -> R`. VALID.
- Disjunctive syllogism: `P OR Q`, `NOT P`, therefore `Q`. VALID for inclusive OR.
- Affirming consequent: `P -> Q`, `Q`, therefore `P`. INVALID; countermodel P=false, Q=true.
- Denying antecedent: `P -> Q`, `NOT P`, therefore `NOT Q`. INVALID; countermodel P=false, Q=true.
- False dilemma: `P OR Q` alone is not evidence there are only two real-world possibilities.

**Proof reporting:** claim; premises; hidden bridges; abstraction and meaning caveat; validity; premise evidence; soundness (`ESTABLISHED` only when both supported); counterexample or derivation; corrected, calibrated claim.

## 3. Translate language without smuggling in facts

Original: “If we install tool X, defects will fall. We installed X, therefore defects fell.”
Formalization: `P -> Q`, `P`; hence `Q`: VALID *for the abstract form*.
But the crucial premise `P -> Q` needs empirical verification, and “defects fall” needs a specified population and period. If the causal premise is unknown, **soundness is NOT ESTABLISHED**. This is the central anti-bullshit distinction.

Translate `only if` carefully: “P only if Q” means `P -> Q`, not `Q -> P`. “Unless” and natural-language “or” may be ambiguous. Time, probability, causality, norms, and counterfactuals generally require richer models than plain propositional logic.

## 4. Propositional countermodels (tool-optional)

Given premises P1...Pn and conclusion C, enumerate every assignment of truth values to the distinct atomic propositions. If at least one makes every premise true and C false, show it: the argument is **INVALID**. Otherwise it is **VALID** *under the translation*.

The bundled `scripts/argument_checker.py` implements truth tables for ASCII `!` (NOT), `&` (AND), `|` (inclusive OR), `->` (implication), and parentheses. It is finite propositional logic only. It cannot decide whether a natural-language translation is faithful, or whether its premises are true.

Example:
```bash
python3 scripts/argument_checker.py --premise 'P -> Q' --premise P --conclusion Q
# VALID
python3 scripts/argument_checker.py --premise 'P -> Q' --premise Q --conclusion P
# INVALID with counterexample
```

## 5. Categorical syllogisms

The four standard categorical forms:

| Form | Meaning |
|---|---|
| A: All S are P | ∀x(S(x)→P(x)) |
| E: No S are P | ∀x(S(x)→¬P(x)) |
| I: Some S are P | ∃x(S(x)∧P(x)) |
| O: Some S are not P | ∃x(S(x)∧¬P(x)) |

Two premises link major P, minor S, middle M. The middle must mean the same thing in both premises; detect equivocation and illicit quantifier scope. Do **not** infer that S exists just because a universal premise says all S are P. In modern logic, universal claims may be vacuously true for empty classes.

Examples:
- **Barbara:** All M are P; All S are M; therefore All S are P. VALID; S may be empty.
- **Celarent:** No M are P; All S are M; therefore No S are P. VALID.
- **Darii:** All M are P; Some S are M; therefore Some S are P. VALID.
- **Undistributed middle:** All S are M; All P are M; therefore All S are P. INVALID. Set S and P to disjoint, nonempty subsets of M.
- **Existential error:** All S are P; therefore Some S are P. INVALID where S is empty.

**Manual countermodel method:** Use Venn-region membership for S, P, M: eight possible regions (binary inside/outside each). Search for a set of occupied regions satisfying both premises while violating conclusion. For universal premises, ban incompatible occupied regions; for existential premises, require at least one witness. Empty domains require separate explicit assumptions; don't silently assume all sets nonempty. This is a method, not a claim that the included script implements categorical proof automation.

**Optional local extension:** `scripts/categorical_checker.py` searches finite membership models for standard-form categorical patterns. It can expose a countermodel or report a finite pass, but it does not establish general first-order validity, term meaning, or premise truth. Use it as a check on the manual countermodel, not as a certificate.

## 6. Proving “only option” and “none possible”

These are universally quantified over a solution space. Unless the search space is explicitly finite and completely enumerated under justified constraints, **the skill cannot prove there are no other possible ideas**. It can report:

- `ONE DEFENSIBLE OPTION IDENTIFIED`, NOT `THE ONLY POSSIBLE OPTION`;
- `NO DEFENSIBLE SOLUTION IDENTIFIED UNDER CURRENT EVIDENCE`, NOT `NO SOLUTION CAN EXIST`;
- `CURRENTLY DOMINATED` rather than `IMPOSSIBLE` when feasibility is merely unsupported.

## 7. Epistemic statuses

- `VALID`: formal entailment under an explicit interpretation.
- `INVALID`: a concrete countermodel or formal failure exists.
- `NOT DEMONSTRABLE`: formalization ambiguous, expressivity insufficient, or reliable verification unavailable.
- `NOT APPLICABLE`: claim is not proposing a deductive inference.
- `ESTABLISHED SOUNDNESS`: valid and all premises substantiated as true for the relevant interpretation. Use sparingly.
- `SOUNDNESS NOT ESTABLISHED`: truth/meaning of a premise is unresolved or false, regardless of validity.

**Never turn “valid” into “true,” “supported” into “proven,” or a value choice into a syllogism merely to fill a template.**

## 8. Final epistemic outcomes

Use one of these outcomes for the overall conclusion. They describe the support for the conclusion, not the quality of the model's prose.

- **Supported** — adequate evidence and an appropriate inference support the conclusion; no material unresolved defect remains at the performed depth. This is not absolute certainty and not a claim of infallibility.
- **Provisionally supported** — the available evidence and reasoning favor the conclusion, but a material premise is unverified, the evidence is limited, or a plausible rival remains. State what would upgrade or downgrade it.
- **Unsupported** — the evidence or reasoning is insufficient to justify the conclusion. This includes a valid argument with unverified premises and evidence that is too weak, irrelevant, or incomplete.
- **Contradicted** — adequate evidence supports the negation of the conclusion, or the conclusion conflicts with a better-supported claim.
- **Invalid inference** — the conclusion does not follow from the stated premises, even if the premises are true. Show the counterexample or formal defect.
- **Indeterminate** — the available evidence and reasoning justify neither the conclusion nor its negation, and more information could settle it. State what would settle it.

`NOT APPLICABLE` remains available for pure definitions, aesthetic judgments, and value choices where an empirical truth outcome does not apply. Do not use it to avoid a difficult audit.

**Practical desirability is separate.** A conclusion can be supported and still be undesirable because of costs, values, distributional effects, or risk. Say which question is being answered.

## 9. Overall outcome mapping

| Formal validity | Premise status | Overall outcome |
|---|---|---|
| VALID | All premises VERIFIED | Supported or provisionally supported, depending on scope and residual uncertainty |
| VALID | At least one CONTESTED or UNVERIFIED | Unsupported or provisionally supported, depending on materiality and evidence |
| VALID | At least one FALSE | Unsupported or contradicted |
| INVALID | Any | Invalid inference |
| NOT DEMONSTRABLE | Any | Indeterminate, or a non-deductive supported/provisionally supported judgment with the formal gap stated |
| NOT APPLICABLE | Any | Use the appropriate empirical, predictive, causal, or value outcome; do not claim deductive proof |

The mapping is a discipline, not an algorithm. Explain the materiality of the premise and the scope of the conclusion.

## Sources (reading not required for skill invocation)

- Stanford Encyclopedia of Philosophy, Informal Logic: https://plato.stanford.edu/entries/logic-informal/
- Internet Encyclopedia of Philosophy, Fallacies: https://iep.utm.edu/fallacy/
