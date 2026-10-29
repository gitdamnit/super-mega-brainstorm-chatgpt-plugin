---
name: brainstorm
description: Use this skill when the user asks to brainstorm, ideate, come up with ideas, explore options, or think through a problem — e.g. "brainstorm names for X", "give me some ideas for Y", "help me figure out how to Z", "I'm stuck, any thoughts?". Produces genuinely different, constraint-aware options, kills the weak ones with reasons, ranks the survivors, and converges on a decision with a concrete next action.
license: ""
compatibility: Fully offline. No API keys, external services, or proprietary dependencies required. Works with any Agent Skills-compatible environment.
metadata:
  author: ""
  version: "1.0.0"
---

# Brainstorm

Purpose: produce **genuinely different, constraint-aware options** and **converge on a decision**. If the output is many shallow variations of one idea, the skill has failed. Generic output is worthless — everything anchors to the user's actual project.

## 1. When to activate

Activate when the user:

- Says **brainstorm**, ideate, ideas, options, possibilities, "what if", "how could we", "help me think through"
- Asks for **names, titles, taglines, features, domain names, marketing angles, content ideas, gift ideas**
- Pastes raw notes, goals, or a vague situation and asks what to do with it
- Describes being **stuck** without asking a specific question

Don't activate for factual lookups or how-to questions with one known answer. Just answer those directly.

## 2. Operating principles

1. **Divergence is mechanical, not cosmetic.** Every option must differ in mechanism, approach, or framing — not wording. Five structurally different options beat fifty variations of one idea.
2. **No idea without its constraints.** What it costs, what it gives up, what must be true. An idea presented without its constraints is incomplete output.
3. **Killing is part of the job.** Explicitly discard weak ideas with reasons. No filler, no manufactured balance. "Not doing X because Y" is a deliverable, not a failure.
4. **Take a position.** Rank, pick a winner, say why — and what would change your mind. "These are all interesting, which do you prefer?" is a failure to decide.
5. **Context beats brilliance.** Anchor everything to the actual project: goals, constraints, what exists, what must not break. Never brainstorm in generic idea space.
6. **One absurd idea, judged like the others.** Exactly one deliberately ridiculous option per session, carrying the same constraint line and the same right to die. It earns its place on merit or dies in the kill list.
7. **Land the plane.** Every session ends with: the chosen direction, the first action, and what's parked.

## 3. Modes — they change volume, never the contract

The five-part output contract (§5) holds in **every** mode. Modes only set question count, option count, and waves:

| Mode | When | Questions | Options | Extras |
|---|---|---|---|---|
| **QUICK** | "10 names for...", casual, obvious context | 0 — state assumptions in one line | 4-6 | Contract compressed, never skipped |
| **STANDARD** (default) | Ordinary "give me ideas for..." | ≤1 round, ≤3, only missing context | 5-8 | — |
| **DEEP** | Big decision, launch, "help me think this through" | 1-2 rounds | 8-12, in 2 waves (different mechanisms per wave) | Confirm context back before diverging |

Missing project context? Ask for it **before generating**. If truly nothing is known, one round of ≤3 questions; otherwise state assumptions in one line and proceed — don't ceremony.

## 4. Workflow

### Phase 0 — Context binding
Before any idea, anchor to the project:

- **Goals** — what winning looks like, in numbers or moments
- **Constraints** — time, money, effort, skill, maintenance appetite, existing stack/architecture
- **What exists** — assets, audience, prior attempts (these become idea fuel — see resource raid, B11)
- **What must not break** — workflow, revenue, anything they'd hate to lose

Ask for what's missing, one round, ≤3 numbered questions. If the context is already in the prompt, *mine it* instead of asking: extract goals, constraints, must-not-break, prior attempts — then build on their assets.

### Phase 1 — Framing
State the actual problem in one or two sentences. It must add the constraint or the goal — restating the premise in fancier words is not a framing, it's decoration. If two framings genuinely diverge, STANDARD/DEEP may offer both (counts as the one question round; if you asked in Phase 0, just pick and say why in a clause). QUICK picks silently.

### Phase 2 — Options (structural divergence)
Generate:

- **Format:** numbered. **Bold 2-4-word name** — *mechanism: 2-4 words* — one-line pitch. Then the constraint line. No paragraphs.
- **Constraint line, every option, no exceptions (absurd included):**
  `Costs: time/money/complexity/maintenance · Gives up: what it sacrifices vs. the others · Needs: assumptions and dependencies to hold`
- **The mechanism test:** after three options, the fourth must not be predictable from them. If it is, stop and force a new angle — invert it (B2), swap the actor (C2), change the resource (B11), or the medium (B5, B12).
- **Twins:** two options sharing a mechanism = keep the stronger, kill the weaker by name in Phase 3.
- **Exactly one absurd option**, marked *(the absurd one)* — judged with the same seriousness as the rest, constraint line included. Absurdity is a rut-escaping tool, not the skill's personality; it earns its place on merit or dies.
- **Volume:** QUICK 4-6, STANDARD 5-8, DEEP 8-12 in two waves. Five mechanically different options beat fifty variations.
- Use 1-2 techniques from §7 / `references/techniques.md` — chosen by symptom, shown by their *fruit*, not their names. Remixes count only when the remix changes mechanism.
- No praise, no evaluation here. Weaknesses get named where they belong: the kill list.

### Phase 3 — Kill list
Discard weak ideas explicitly, each with its reason: **"Not doing X because Y."**

- Mechanism twins land here (weak cousin of a stronger option).
- No padding to look thorough; if the option set is 5, you never owed anyone 12.
- If one option clearly dominates, say so — no manufactured balance.
- **Parked ≠ killed.** Killed = weak (goes here). Parked = good but not now (goes in Phase 5). Both are named.

### Phase 4 — Ranking
Rank surviving options **best → worst**.

- For the winner: why it wins — *specifically against the runner-up*, not in general.
- Every ranked option keeps its weaknesses named. Praise proportional to merit.
- State the **overturn condition**: what evidence or constraint change would flip the ranking ("if the deadline doubles, #2 wins because..."). A ranking without an overturn condition is a mood, not a decision.

### Phase 5 — Convergence (mandatory, every session, every mode)
End with, in this order:

1. **Chosen direction + why** — your position, one sentence. It may agree with the user's hunch; either way it commits.
2. **Next action** — the single most useful thing to do or test first. Prefer the cheapest test of the winner's biggest assumption. Concrete, ≤1 hour, startable today.
3. **Parked list** — what's explicitly parked and why, plus the condition that brings it back.

Commit, then (optionally, one clause) offer follow-up. Never end "these are all interesting — which do you prefer?"

### Phase 6 — Artifacts (on request only)
Decision doc, comparison table, 30-day experiment plan, 1-pager. Keep the full options list, kill list, and parked items intact at the end — the graveyard is part of the record.

## 5. Output contract (all modes — exactly these five sections, in this order)

1. **Framing** — the actual problem being solved, in one or two sentences.
2. **Options** — structurally different; each with name, mechanism, pitch, and its constraint line. Exactly one deliberately absurd, judged on merit.
3. **Kill list** — discarded ideas, each with its reason.
4. **Ranking** — best → worst; the winner justified; the overturn condition stated.
5. **Next action** — the chosen direction (the position), the single most useful thing to do or test first, and what's parked.

Nothing precedes the Framing except a one-line assumptions note in QUICK mode when no questions were asked.

Skeleton:

```markdown
**Framing:** <the actual problem, 1-2 sentences>

## Options
1. **Name** — *mechanism: loyalty loop.* Pitch: ...
   Costs: ~$50/mo, 1h/wk · Gives up: cash · Needs: 10% of readers willing to share
2. ...
5. **Name** *(the absurd one)* — *mechanism: scarcity ritual.* Pitch: ...
   Costs: ... · Gives up: ... · Needs: ...

## Kill list
- **#5** — not doing it because <reason>
- **Twin of #2** — same mechanism, weaker because <reason>

## Ranking
1. **#1** — wins because ... (over #2 specifically: ...) — weakness: ...
2. **#3** — ...
   *Overturn: if <constraint change / evidence>, #2 wins because ...*

## Next action
**Chosen: #1** — <why, one sentence: the position.>
Do/test <the single most useful thing> — it's the cheapest test of the winner's biggest assumption.
*(Parked: #4 until <condition>. Killed: #5 — see above.)*
```

## 6. Hard rules

**Do**
- Name each option's mechanism; never let the 4th option be predictable from the first 3.
- Attach the constraint line to **every** option, absurd included.
- Keep a real kill list — "Not doing X because Y."
- Rank, justify the winner *against the runner-up*, state the overturn condition.
- Anchor to the project: reference their actual assets, stack, and constraints by name — "Needs: your existing 400-reader list", not "Needs: an audience."
- Make the next action the cheapest test of the winner's biggest assumption.
- Ask for missing project context before generating.

**Don't**
- Don't ship forty variations of one idea as breadth.
- Don't restate the premise in fancier words and call it an idea.
- Don't use motivational language — "unlock your imagination", "think outside the box", "get creative" — delete it on sight. The word "creativity" need not appear at all.
- Don't ship an unranked, undifferentiated option dump.
- Don't praise every idea equally; weak ideas get named as weak.
- Don't manufacture false balance when one option clearly dominates.
- Don't replace convergence with "which do you prefer?" — the skill takes a position.
- Don't brainstorm in generic idea space — no context, ask first.

## 7. Technique quick-pick

| You notice... | Reach for |
|---|---|
| Options are wording-twins of each other | Mechanism map (B0), then inversion / analogy raid |
| Problem statement keeps wobbling | HMW ladder, assumption smash (A1, A5) |
| Everything is safe and predictable | Inversion (B2), worst-idea → the absurd slot (B9), constraint squeeze (B5) |
| Too many options, no conviction | Weighted scorecard (D3), overturn condition (D7), kill/park (D8) |
| Ranking feels vibes-y | D3 scorecard + D7 overturn condition |
| User says "yes, but..." repeatedly | Premortem (D4), then success criteria (A3) |

Full details, prompts, and 30+ techniques: read `references/techniques.md` when a phase needs more firepower. Otherwise don't load it.

## 8. Worked example (abridged — the contract, end to end)

> **User:** "brainstorm how to get my coffee newsletter past 400 subscribers. Solo, ~3 hrs/week, archives exist, #12 is the best thing I've written."

**Framing:** The 400 readers are an audience, not a distribution mechanism — growth is capped at friends-of-friends. Success: +200 real readers in 60 days, inside 3 hrs/week.

**Options**
1. **Swap issues** — *mechanism: borrowed audience.* Trade guest issues with 2-3 adjacent newsletters of 2-5k. Costs: 4 cold emails + 2 extra issues/mo · Gives up: an issue slot · Needs: 2-3 bigger fishes who say yes.
2. **Giveaway ladder** — *mechanism: paid referral.* Readers who land 2 sign-ups get a coffee; ~$12/convert. Costs: ~$50/mo, 1h/wk · Gives up: cash · Needs: 10% of 400 willing to share — the weakest assumption in this set.
3. **Archive guides** — *mechanism: SEO artifacts.* 40 issues → 8 "best of" guides, #12 leads. Costs: 1 weekend + $40/yr · Gives up: 2 weekends · Needs: nothing you don't have.
4. **Quarterly unlaunch** *(the absurd one)* — *mechanism: scarcity ritual.* Once a quarter, publicly cull to the 100 most-active readers. Costs: 30 min/quarter · Gives up: vanity list size · Needs: the numbers, publicly. Sounds silly, but ~30% of any list is dead weight, and a public cull is a story.

**Kill list**
- **#5 IG clips** — mechanism twin of #1 (borrowed attention vs. borrowed trust); you'd own nothing on the platform and it fails the 3h/week constraint.

**Ranking**
1. **#1** — only option whose upside compounds; costs almost nothing; the emails *are* the test. Over #3 specifically: #3's costs are known but its upside is linear, #1's grows through other people's lists. Weakness: depends on other people's calendars.
2. **#3** — zero assumptions, slow, linear. Weakness: nobody searches for coffee newsletters; it's a basement, not a launchpad.
3. **#2** — decent mechanic, weakest Needs. Named, not forgiven.
4. **#4** — judged on merit: retention ritual + great story, weak as *growth*.
   *Overturn: if 2 of the 4 emails get no reply by Friday, #3 wins by default — decision pre-made, no re-litigation.*

**Next action:** **Chosen: #1** — the only option that costs less than it might return, and its biggest assumption dies or survives by Friday. Tonight: send 4 one-paragraph swap emails (twenty minutes). *Parked: #4 until the 60-day review — it's retention, not growth. Killed: #5.*

## 9. Tone

Direct, committed, zero hedging. First line is the framing. Use the user's own vocabulary from their message; match their register — startup founders get punchy, seventh-graders get simpler words, same contract underneath. Hedge words ("maybe", "possibly") appear only inside constraint lines, where they're honest.
