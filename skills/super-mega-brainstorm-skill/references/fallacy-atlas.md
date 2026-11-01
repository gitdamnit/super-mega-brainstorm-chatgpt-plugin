# Advanced Smell Test: Fallacy & Reasoning Atlas

**Purpose:** A locally bundled, categorical audit of defective inference. It is a *diagnostic reference*, not a keyword detector, a machine proof, or a claim to enumerate every possible reasoning error.

There is **no universally agreed finite list of every fallacy**. Academic taxonomies differ, labels overlap, and infinitely many invalid deductive forms have no conventional name. The *Internet Encyclopedia of Philosophy* lists 231 common names, including synonyms; it notes that classification is disputed. This atlas groups the underlying **mechanisms**, records common aliases, and applies them through a context-sensitive procedure. The names below are a working, broad-coverage set; not all names denote universally accepted independent fallacies.

## Mandatory diagnostic process

1. Identify the **exact claim**, its type (deductive, inductive, abductive, causal, normative, empirical, forecast, rhetorical), and the **precise premise(s)** offered in support.
2. Identify its best **charitable interpretation** and the context in which the disputed move could be reasonable.
3. Apply **acceptability, relevance, sufficiency** to the premises; separately inspect inference form, scope, language, selection, and real-world evidence.
4. Search *all* applicable categories below. Mark `NOT APPLICABLE` where a category cannot sensibly apply. Do not manufacture violations.
5. A positive finding must state: **claim → quoted evidence/reasoning fragment → defect mechanism → why the inference fails → non-fallacious possible reading → repair or test → severity**.
6. Severity: `BLOCKER` decisive; `MAJOR` could reverse decision; `CAUTION` material uncertainty or weaker support; `CLEAR` no identified defect (never proof of truth). Use separate evidence status `VERIFIED`, `CONTESTED`, `UNVERIFIED`, `FALSE`.
7. Rerun on any *repaired* argument. Apply to the model's recommendation as aggressively as the user's favorite theory.

## A. Formal inference and quantifiers

| Name / common aliases | Core defect | Diagnostic question |
|---|---|---|
| Affirming the consequent / converse error | From P→Q and Q, assert P | Could another cause produce Q? |
| Denying the antecedent / inverse error | From P→Q and ¬P, assert ¬Q | Could Q happen another way? |
| Undistributed middle | Two classes overlap a third; overlap each other is assumed | Can the classes occupy different parts? |
| Illicit major / illicit minor | Conclusion distributes a categorical term its premise did not | Does the conclusion say *all* where support covers only *some*? |
| Four terms / equivocal middle | Syllogism quietly changes a term's meaning | Are there exactly three consistent terms? |
| Exclusive-premises error | Two negative categorical premises are treated as yielding a categorical conclusion | Is the needed positive connection absent? |
| Existential fallacy | Infers that something exists merely from universal statements | Are there known members of the class? |
| Quantifier shift / every-and-all / scope | Switches ∀∃ and ∃∀ or changes quantifier scope | Does "everyone has someone" become "one person for everyone"? |
| Illicit conversion | From All A are B infer All B are A | Is the converse actually supported? |
| Modal scope fallacy | Shifts between possible/necessary and who/what is possible | Does "necessarily" modify the right proposition? |
| Denying a disjunct incorrectly | Treats inclusive OR as exclusive | Could both alternatives be true? |
| Affirming a disjunct incorrectly | From A∨B and A infer ¬B without exclusivity | Was exclusivity established? |
| Conjunction fallacy | Treats A∧B as more probable than A | Can a subset exceed its containing set? |
| Non sequitur / invalid entailment | Conclusion does not follow from premises | Can all premises be true with conclusion false? |
| Contradiction / inconsistency | Premises assert P and ¬P (classical logic: explosion risk) | Can the premise set even be jointly true? |
| Denying a rule's preconditions / converse necessity | Confuses sufficient and necessary conditions | Which direction does the implication actually run? |

**Truth-table counterexample:** P→Q; Q; therefore P is invalid under P=false, Q=true. **Valid example:** P→Q; P; therefore Q. Formal validity is separate from premise truth.

## B. Relevance and interpersonal pressure

| Name / aliases | Core defect |
|---|---|
| Ad hominem (abusive) / name calling | Attack the person rather than argument evidence |
| Circumstantial ad hominem / vested-interest fallacy | Treat motive or interest as sufficient refutation |
| Tu quoque / you too | Hypocrisy is offered as rebuttal to a substantive claim |
| Genetic fallacy / source poisoning | Judge claim solely by its origin |
| Poisoning the well | Preemptively discredit an argument before evaluating it |
| Guilt by association / bad seed | Association alone substitutes for relevant evidence |
| Straw man / caricature / refutation by caricature | Attack a materially weakened or distorted version |
| Red herring / digression / smokescreen | Change attention away from decisive issue |
| Ignoratio elenchi / irrelevant conclusion / missing point | Support a conclusion other than the disputed one |
| Appeal to popularity / ad populum / bandwagon / ad numerum | Popularity used as evidence of truth outside relevant contexts |
| Appeal to emotion / outrage / pity / fear / flattery | Feeling used in place of evidence, not merely communicated |
| Appeal to force / ad baculum / scare tactic | Coercion used as proof |
| Appeal to wealth / ad crumenum / poverty / snobbery | Status or wealth used as truth criterion |
| Appeal to authority / ad verecundiam / unqualified authority | Authority outside expertise or unexamined methods replaces relevant support |
| Appeal to tradition / past practice / ad antiquitatem | Age of practice treated as proof it works or ought to continue |
| Appeal to novelty / ad novitatem | Newness treated as proof of superiority |
| Appeal to nature / naturalistic rhetoric | Naturalness offered as sufficient safety, goodness, or merit |
| Appeal to consequences / ad consequentiam | Desired/undesired outcomes used to declare a proposition true/false |
| Style over substance / rhetoric over evidence | Eloquence substituted for demonstrated truth |

**Do not auto-flag:** credible expert testimony when domain-qualified and appropriately weighted; motives when evaluating conflicts of interest and testimony; emotion when values or harms genuinely matter.

## C. Presumptions and question framing

| Name / aliases | Core defect |
|---|---|
| Begging the question / petitio principii / circular reasoning | The conclusion is assumed in a premise or proof chain |
| Loaded/complex question / many questions | Question presupposes a disputed fact |
| False dilemma / bifurcation / black-or-white / either-or | Alternatives are presented as exhaustive without warrant |
| False middle / false compromise / golden-mean fallacy | Truth assumed to be between two positions |
| No true Scotsman / ad hoc redefinition | Counterexamples excluded by shifting membership definition |
| Special pleading / double standard | Unjustified exception for a favored case |
| Burden-of-proof shift / appeal to ignorance / ad ignorantiam | Absence of disproof taken as proof, without a justified evidential framework |
| Perfectionist fallacy / nirvana fallacy | Imperfect improvement rejected versus imaginary perfect alternative |
| Moving goalposts | Evidential threshold changes after being met |
| Proof surrogate / bare assertion | “It's proven,” “experts say,” or unnamed data replaces actual evidence |
| Victory by definition / persuasive definition / definist | Redefinition builds the contested verdict into terms |
| Is–ought gap / Hume's law | Derive a normative prescription from purely descriptive premises without value bridge |
| Moralistic fallacy | Infer what is factually true from what ought to be true |
| Equivocation | Same word silently changes meaning across premises |
| Amphiboly / syntactic ambiguity | Grammar yields multiple readings; one supports a different conclusion |
| Accent / contextomy / quoting out of context | Selectively emphasizing or extracting words changes meaning |
| Reification / hypostatization / misplaced concreteness | Treat an abstraction as an independent concrete cause/entity |
| Etymological fallacy | Original word meaning imposed on current use |
| Line-drawing / sorites misuse | Vague boundary taken to deny meaningful distinctions |
| Fallacy fallacy / argument from fallacy | A bad argument for P is treated as proof ¬P |

## D. Causality, explanation, and prediction

| Name / aliases | Core defect |
|---|---|
| Post hoc ergo propter hoc | Temporal sequence alone becomes causal proof |
| Cum hoc ergo propter hoc | Correlation alone becomes causal proof |
| Confounding / common-cause neglect | Third factor explains association |
| Reverse causation | Direction of effect is mistaken |
| Oversimplified / single-cause fallacy | Complex process assigned one unproven sufficient cause |
| Spurious mechanism / pseudomechanism | Mechanism asserted without credible pathway or evidence |
| Slippery slope / domino | Chain of consequences asserted without warranted link probabilities |
| False analogy / weak analogy | Differences undermine transferred relationship |
| Regression-to-mean fallacy | Natural fluctuation mistaken for intervention effect |
| Gambler's fallacy / Monte Carlo fallacy | Independent outcomes expected to “even out” locally |
| Hot-hand overclaim | Random clustering mistaken for established persistent causal streak |
| Survivorship bias | Only surviving/successful cases studied |
| Selection/collider bias | Conditioning on a selection outcome creates spurious association |
| Self-fulfilling prophecy | Belief changes behavior and then appears to verify itself |
| Overfitting / curve fitting | Model learns noise, generalization untested |
| Texas sharpshooter / post hoc subgroup selection | Pattern chosen after seeing data, then treated as predicted |
| Unfalsifiability / ad hoc rescue | No conceivable observation can count against claim; failures reframed as support |
| Misuse of Occam's razor | Simpler story declared proven, rather than provisionally preferred |
| Ignoring alternative hypotheses | Plausible competing models never examined |

**Causal audit:** Define exposure, outcome, comparison, mechanism, timeframe, sample selection, temporal order, confounders, possible reverse path, and strongest disconfirmation. Observational evidence may support causality with suitable methodology; absence of an RCT does not automatically refute it.

## E. Sampling, statistics, and evidence

| Name / aliases | Core defect |
|---|---|
| Hasty generalization / unrepresentative generalization | General inference from inadequate sample |
| Biased sample / self-selection / sampling frame error | Observed group differs from target population |
| Anecdotal fallacy / misleading vividness | Single vivid case substituted for representative evidence |
| Cherry-picking / one-sidedness / stacking the deck / suppressed evidence | Relevant contrary cases selectively omitted |
| Base-rate neglect | Prior prevalence ignored when interpreting conditional evidence |
| Prosecutor's fallacy / inverse probability error | P(evidence|innocence) confused with P(innocence|evidence) |
| Ecological fallacy | Aggregate relationship assumed to hold for individuals |
| Atomistic fallacy | Individual relationship assumed to hold for aggregates |
| Simpson's paradox neglect | Aggregated trend misread without segment composition |
| Multiple comparisons / data dredging | Repeated testing ignored while interpreting a selected discovery |
| Optional stopping / p-hacking | Analysis or sample stopping depends on desired result |
| Publication bias / file drawer | Positive findings selectively visible |
| Nonresponse bias | Missing participants differ systematically |
| Small-n certainty | Imprecise estimates reported as stable predictions |
| Denominator neglect | Ratio/percentage without base or meaningful comparison |
| False precision | Decimal scoring claims unwarranted measurement accuracy |
| Conditional probability confusion | Condition or reference class quietly switched |
| Conjunction and disjunction probability errors | Probability axioms violated |
| Relative risk presentation bias | Relative change hides absolute risk and starting baseline |
| Confidence-interval misuse | Interval assigned impossible interpretive meaning |
| Statistical-significance overclaim | P-value interpreted as effect size, practical importance, or truth probability |
| Correlation/causation collapse | Association or prediction treated as intervention effect |
| Data-leakage / test-set contamination | Evaluation information was used to fit/tune model |

**Quantitative audit:** units, denominator, inclusion criteria, data source/date, uncertainty, base rate, multiplicity, sample power, missingness, measurement validity, and competing explanations.

## F. Cognitive biases and decision distortions (not automatically “fallacies”)

| Mechanism | What to check |
|---|---|
| Confirmation bias / selective attention | Was disconfirming evidence actively sought? |
| Motivated reasoning / rationalization / wishful thinking | Are standards changed to protect a favored outcome? |
| Anchoring | Did initial number or example distort assessment? |
| Availability / salience bias | Are vivid cases overweighted versus frequencies? |
| Framing / loss aversion | Does logically equivalent framing alter verdict? |
| Sunk-cost fallacy / escalation of commitment | Would we choose this again without past spending? |
| Status quo bias / omission bias | Is inaction treated as harmless without examining costs? |
| Hindsight bias | Are outcomes portrayed as obvious in advance? |
| Outcome bias | Is decision quality judged only by one result? |
| Overconfidence / illusion of explanatory depth | Does the agent claim mechanisms it cannot actually explain? |
| Groupthink / social proof | Have dissenting or outsider models been included? |
| Automation bias / authority laundering | Are AI statements accepted because of fluent formatting? |
| Planning fallacy | Are cost, coordination, and maintenance underestimated? |
| Hyperbolic discounting / present bias | Are immediate gains overweighted? |
| Scope insensitivity | Does the analysis scale with number of affected people? |

## G. AI-specific bullshit alarms

- Fabricated study, quotation, citation, statistic, API capability, tool run, repo inspection, “verified” status, or test result.
- Source-trace laundering: multiple citations copied from one unverified source and miscounted as independent confirmation.
- Citation does not support the precise asserted proposition, dates, population, or causal claim.
- Reasoning repeatedly states an assumption until it sounds observed.
- Simulation or thought experiment presented as empirical evidence.
- LLM roleplay personas treated as independent expert consensus.
- Invented numeric scoring/percent confidence without calibration.
- Mathematical formalization silently changes the claim or inserts an unverified bridge premise.
- Overly specific recommendation when decision-critical data are missing.
- Invalid alternatives created to fulfill a quota.
- “Everything checks out” claimed without examining actual claims, counterexamples, and sources.

## Example: detect and repair

> “All successful startups iterate. We iterate. Therefore we will succeed.”

- **Pattern:** affirming the consequent if rewritten “Success → iteration; iteration; therefore success.”
- **Other issues:** selection/survivorship and insufficient evidence about success rate among iterators.
- **Contextual possibility:** iteration may still be a reasonable practice; defect lies in claimed guarantee.
- **Repair:** “Iteration is one candidate practice. Its effect depends on problem-market fit, execution, resources, and relevant outcome data.”
- **Verdict:** original inference `BLOCKER`; repaired statement is a hypothesis until tested.

## Completeness discipline

This taxonomy is categorical rather than a purported proof of exhaustiveness. Some listed mechanisms are cognitive biases or empirical research errors rather than formal logical fallacies; that distinction must be preserved. Never claim “we checked every known fallacy,” or assert “no fallacies exist” merely because no named pattern matched.

## Grounding and further bibliography (not required at runtime)

- Internet Encyclopedia of Philosophy, **Fallacies** (231 names, taxonomic caveats): https://iep.utm.edu/fallacy/
- Stanford Encyclopedia of Philosophy, **Informal Logic**, revision 2026-01-28: https://plato.stanford.edu/entries/logic-informal/
