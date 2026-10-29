# Brainstorm Skill - Acceptance Tests

This document contains manual acceptance test cases for the Brainstorm Universal Agent Skill. These tests verify that the skill preserves the original methodology, produces correct output, and handles edge cases appropriately.

## Test Execution Notes

- **Status:** All tests are **manual** (require human execution with an AI agent)
- **Environment:** Can be run in any Agent Skills-compatible environment
- **Method:** Execute the skill with the specified input and verify the output
- **Automation:** These tests are designed for manual verification; automated validation is provided by `validate_skill.py`

## Test Categories

1. [Mode Tests](#1-mode-tests) - Verify all three operating modes
2. [Methodology Tests](#2-methodology-tests) - Verify core methodology requirements
3. [Output Contract Tests](#3-output-contract-tests) - Verify five-section output
4. [Edge Case Tests](#4-edge-case-tests) - Verify handling of difficult inputs
5. [Compatibility Tests](#5-compatibility-tests) - Verify cross-platform behavior

---

## 1. Mode Tests

### Test 1.1: QUICK Mode Activation
**ID:** T-MODE-QUICK-001
**Description:** Verify QUICK mode activates and produces compressed output
**Input:** "brainstorm 10 names for a coffee shop"
**Expected:**
- ✅ Activates automatically
- ✅ Produces 4-6 options
- ✅ All five output sections present
- ✅ No clarification questions (assumptions stated in one line)
- ✅ Constraint line on every option
- ✅ Exactly one absurd option
- ✅ Kill list present
- ✅ Ranking with overturn condition
- ✅ Concrete next action

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 1.2: STANDARD Mode Activation
**ID:** T-MODE-STD-001
**Description:** Verify STANDARD mode activates and produces full output
**Input:** "give me ideas for growing my newsletter"
**Expected:**
- ✅ Activates automatically
- ✅ Produces 5-8 options
- ✅ Asks ≤3 clarification questions if context missing
- ✅ All five output sections present
- ✅ Constraint line on every option
- ✅ Exactly one absurd option
- ✅ Kill list with reasons
- ✅ Ranking with winner vs. runner-up justification
- ✅ Overturn condition stated
- ✅ Concrete next action
- ✅ Parked items if applicable

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 1.3: DEEP Mode Activation
**ID:** T-MODE-DEEP-001
**Description:** Verify DEEP mode activates for complex decisions
**Input:** "help me think through whether I should quit my job and start a consulting business"
**Expected:**
- ✅ Activates automatically (DEEP mode)
- ✅ Confirms context back before diverging
- ✅ 1-2 rounds of clarification questions
- ✅ Produces 8-12 options in 2 waves
- ✅ All five output sections present
- ✅ Different mechanisms per wave
- ✅ Constraint line on every option
- ✅ Exactly one absurd option
- ✅ Comprehensive kill list
- ✅ Detailed ranking with overturn condition
- ✅ Concrete next action

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 1.4: Mode Selection with Explicit Request
**ID:** T-MODE-EXPLICIT-001
**Description:** Verify mode can be explicitly requested
**Input:** "Use DEEP mode to brainstorm marketing strategies for my SaaS product"
**Expected:**
- ✅ Recognizes DEEP mode request
- ✅ Produces 8-12 options in 2 waves
- ✅ All DEEP mode characteristics from T-MODE-DEEP-001

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

## 2. Methodology Tests

### Test 2.1: Structural Divergence
**ID:** T-METH-DIVERGE-001
**Description:** Verify options are structurally different, not cosmetic variations
**Input:** "brainstorm ways to improve user engagement on my website"
**Expected:**
- ✅ Options have different mechanisms (not just wording changes)
- ✅ Mechanism identified for each option (e.g., "gamification", "personalization", "community building")
- ✅ After 3 options, 4th is not predictable from first 3
- ✅ No "wording-twins" (options that are the same mechanism with different words)

**Verification Method:**
1. Read the options
2. Identify the mechanism for each
3. Verify mechanisms are distinct
4. Check that option 4+ introduce new mechanisms

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.2: Constraint Lines
**ID:** T-METH-CONSTRAINT-001
**Description:** Verify every option has a constraint line
**Input:** "brainstorm features for my mobile app"
**Expected:**
- ✅ Every option has a constraint line
- ✅ Constraint line format: `Costs: ... · Gives up: ... · Needs: ...`
- ✅ Absurd option also has constraint line
- ✅ Constraints are specific and meaningful (not generic)

**Verification Method:**
1. Count the options
2. Verify each has a constraint line
3. Check the format matches the pattern
4. Verify absurd option has constraints

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.3: Exactly One Absurd Idea
**ID:** T-METH-ABSURD-001
**Description:** Verify exactly one absurd idea per session
**Input:** "brainstorm ideas for a team building event"
**Expected:**
- ✅ Exactly one option marked as absurd (e.g., *(the absurd one)*)
- ✅ Absurd option has same structure as others (name, mechanism, pitch, constraints)
- ✅ Absurd option is judged on merit (appears in ranking or kill list)
- ✅ Only one absurd option (not zero, not two)

**Verification Method:**
1. Count absurd-marked options
2. Verify it has full structure
3. Check it's treated seriously (included in ranking or kill list)

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.4: Kill List Accuracy
**ID:** T-METH-KILL-001
**Description:** Verify kill list contains weak ideas with reasons
**Input:** "brainstorm product ideas for a niche market"
**Expected:**
- ✅ Kill list contains discarded ideas
- ✅ Each killed idea has a reason ("Not doing X because Y")
- ✅ Mechanism twins are in kill list (if applicable)
- ✅ No padding (kill list size proportional to option set)
- ✅ Killed ideas don't appear in ranking

**Verification Method:**
1. Check kill list exists and has entries
2. Verify each entry has a reason
3. Verify no killed ideas appear in ranking

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.5: Ranking and Overturn Condition
**ID:** T-METH-RANK-001
**Description:** Verify ranking has winner vs. runner-up justification and overturn condition
**Input:** "brainstorm which programming language to use for my new project"
**Expected:**
- ✅ Options ranked from best to worst
- ✅ Winner justified **specifically against runner-up** (not generic praise)
- ✅ Every ranked option has weaknesses named
- ✅ Overturn condition stated ("if X changes, Y wins because...")
- ✅ Overturn condition is specific and testable

**Verification Method:**
1. Check ranking order
2. Verify winner justification mentions runner-up
3. Check for overturn condition
4. Verify it's specific (not vague)

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.6: Context Binding
**ID:** T-METH-CONTEXT-001
**Description:** Verify context is extracted and used
**Input:** "I have a coffee newsletter with 400 subscribers, 3 hours/week, and archives. Brainstorm growth ideas."
**Expected:**
- ✅ Context extracted (goals, constraints, assets)
- ✅ Options reference specific context (e.g., "your existing 400 readers", "within 3 hours/week")
- ✅ Constraints are project-specific, not generic
- ✅ No generic advice (e.g., "Needs: an audience" → "Needs: your existing 400-reader list")

**Verification Method:**
1. Check that context from input appears in framing
2. Verify options reference specific numbers/assets from input
3. Check constraints are tailored to the project

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.7: Missing Context Handling
**ID:** T-METH-NOCONTEXT-001
**Description:** Verify handling when context is missing
**Input:** "brainstorm ideas"
**Expected:**
- ✅ Asks for missing context (≤3 numbered questions)
- ✅ Questions are specific and relevant
- ✅ Doesn't generate options without context
- ✅ Or states assumptions in one line and proceeds (QUICK mode)

**Verification Method:**
1. Verify questions are asked
2. Count questions (≤3)
3. Check they're numbered
4. Verify no options generated before context received

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.8: Next Action Specificity
**ID:** T-METH-NEXTACTION-001
**Description:** Verify next action is concrete and actionable
**Input:** "brainstorm how to launch my new product"
**Expected:**
- ✅ Next action is concrete and specific
- ✅ Can be started today
- ✅ Takes ≤1 hour
- ✅ Tests the winner's biggest assumption
- ✅ Format: "Do/test <specific action>"

**Verification Method:**
1. Check next action is specific (not vague)
2. Verify it's actionable today
3. Check time estimate (implied or stated ≤1 hour)
4. Verify it tests a key assumption

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 2.9: Parked vs. Killed Distinction
**ID:** T-METH-PARKED-001
**Description:** Verify parked and killed ideas are properly distinguished
**Input:** "brainstorm features for my app - we have limited development time"
**Expected:**
- ✅ Parked items are good but not for now
- ✅ Killed items are weak/fundamentally flawed
- ✅ Both are explicitly named
- ✅ Parked items have conditions for revisiting
- ✅ Killed items have reasons

**Verification Method:**
1. Check for parked items section
2. Check for killed items section
3. Verify distinction is clear
4. Verify parked items have "until" conditions

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

## 3. Output Contract Tests

### Test 3.1: Five Sections Present
**ID:** T-CONTRACT-5SECTION-001
**Description:** Verify all five output sections are present in correct order
**Input:** Any brainstorming request
**Expected:**
- ✅ Section 1: **Framing** (actual problem, 1-2 sentences)
- ✅ Section 2: **Options** (numbered, with constraints)
- ✅ Section 3: **Kill list** (discarded ideas with reasons)
- ✅ Section 4: **Ranking** (best to worst, with overturn condition)
- ✅ Section 5: **Next action** (chosen direction, action, parked items)
- ✅ Sections appear in this exact order

**Verification Method:**
1. Scan output for section headers
2. Verify all five are present
3. Check order is correct

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 3.2: Output Format Consistency
**ID:** T-CONTRACT-FORMAT-001
**Description:** Verify output format matches the skeleton
**Input:** "brainstorm marketing strategies for my new book"
**Expected:**
- ✅ Framing starts with **Framing:** or similar
- ✅ Options section has numbered list
- ✅ Each option has: **Bold name** — *mechanism: ...* — pitch
- ✅ Constraint line follows each option
- ✅ Kill list uses bullet points with "Not doing X because Y" format
- ✅ Ranking is numbered with justification
- ✅ Next action has chosen direction, action, parked items

**Verification Method:**
1. Compare output to skeleton in SKILL.md §8
2. Check each formatting element

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

## 4. Edge Case Tests

### Test 4.1: Insufficient Project Context
**ID:** T-EDGE-NOCONTEXT-001
**Description:** Verify handling when user provides no context
**Input:** "brainstorm"
**Expected:**
- ✅ Asks for context (≤3 questions)
- ✅ Or states assumptions in one line (QUICK mode)
- ✅ Doesn't generate generic, context-free options

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 4.2: Contradictory Constraints
**ID:** T-EDGE-CONTRADICT-001
**Description:** Verify handling of contradictory constraints
**Input:** "brainstorm ideas for a project that must be done in 1 day but also must be perfect"
**Expected:**
- ✅ Acknowledges the contradiction in framing
- ✅ Options address or resolve the contradiction
- ✅ Constraint lines reflect the tension
- ✅ Kill list may include options that can't satisfy both constraints

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 4.3: Request for Fewer Ideas
**ID:** T-EDGE-FEWER-001
**Description:** Verify handling when user requests fewer ideas than mode default
**Input:** "brainstorm 3 ideas for a logo"
**Expected:**
- ✅ Respects the explicit count (3 options)
- ✅ Still produces all five output sections
- ✅ Still includes constraint lines
- ✅ Still includes exactly one absurd option (if ≥3 options)
- ✅ Still has kill list, ranking, next action

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** This tests whether the skill respects explicit user requirements over default mode behavior

---

### Test 4.4: Request to Skip Absurd Idea
**ID:** T-EDGE-NOABSURD-001
**Description:** Verify handling when user explicitly requests no absurd ideas
**Input:** "brainstorm ideas for my startup but no absurd suggestions please"
**Expected:**
- ⚠️ **Behavior undefined in original spec**
- ✅ Either: Respects request (no absurd option)
- ✅ Or: Explains that absurd option is mandatory per methodology
- ⚠️ Document actual behavior

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** This is a conflict test - user request vs. methodology requirement

---

### Test 4.5: Request for Factual Answer
**ID:** T-EDGE-FACTUAL-001
**Description:** Verify skill doesn't activate for factual questions
**Input:** "What is the capital of France?"
**Expected:**
- ✅ Skill does NOT activate
- ✅ Direct factual answer provided
- ✅ No brainstorming output

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** Tests that activation triggers are specific

---

### Test 4.6: Complex Decision with Limited Resources
**ID:** T-EDGE-COMPLEX-001
**Description:** Verify handling of complex decisions with resource constraints
**Input:** "I have $1000, 2 weeks, and no technical skills. Brainstorm how to launch an online business."
**Expected:**
- ✅ Context properly extracted and used
- ✅ Options respect all constraints ($1000, 2 weeks, no technical skills)
- ✅ Constraint lines explicitly mention resource limitations
- ✅ Kill list eliminates options that violate constraints
- ✅ Ranking considers resource efficiency

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 4.7: Naming Exercise
**ID:** T-EDGE-NAMING-001
**Description:** Verify handling of naming/brainstorming exercises
**Input:** "brainstorm 10 names for a coffee shop called Brew Haven"
**Expected:**
- ✅ QUICK mode activates (explicit count + casual context)
- ✅ 4-6 or 10 options (respects explicit count)
- ✅ Each name has mechanism and constraints
- ✅ Mechanisms are different (not just word variations)
- ✅ Absurd name included
- ✅ All five output sections present

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 4.8: Ambiguous User Request
**ID:** T-EDGE-AMBIGUOUS-001
**Description:** Verify handling of vague/ambiguous requests
**Input:** "I need ideas"
**Expected:**
- ✅ Asks for clarification (≤3 questions)
- ✅ Questions are specific and helpful
- ✅ Doesn't generate options until context is clear

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** 

---

### Test 4.9: User Changes Direction Midway
**ID:** T-EDGE-DIRECTION-001
**Description:** Verify handling when user changes direction during brainstorming
**Input:** 
1. "brainstorm ideas for a mobile app"
2. After options are generated: "Actually, let's focus on web instead"
**Expected:**
- ✅ Acknowledges the change
- ✅ Either: Restarts brainstorming with new context
- ✅ Or: Adapts existing options to new context
- ✅ Doesn't produce inconsistent output

**Status:** ⏸️ Unexecuted (requires live agent)
**Result:** 
**Notes:** Tests conversational robustness

---

## 5. Compatibility Tests

### Test 5.1: Offline Operation
**ID:** T-COMPAT-OFFLINE-001
**Description:** Verify skill works without internet access
**Setup:** Disable internet access for the agent
**Input:** Any brainstorming request
**Expected:**
- ✅ Skill activates and functions normally
- ✅ All techniques are available locally
- ✅ No errors about missing external resources
- ✅ Full output generated

**Status:** ⏸️ Unexecuted (requires offline environment)
**Result:** 
**Notes:** 

---

### Test 5.2: Missing Optional Reference Files
**ID:** T-COMPAT-MISSINGREF-001
**Description:** Verify handling when optional files are missing
**Setup:** Remove `references/techniques.md`
**Input:** Any brainstorming request
**Expected:**
- ✅ Skill still activates and functions
- ✅ Technique quick-pick table in SKILL.md is used
- ✅ No errors about missing reference file
- ⚠️ May not be able to use full technique catalog

**Status:** ⏸️ Unexecuted (requires file manipulation)
**Result:** 
**Notes:** Tests graceful degradation

---

### Test 5.3: Platform-Specific Installation
**ID:** T-COMPAT-INSTALL-001
**Description:** Verify installation works on different platforms
**Platforms to test:**
- [ ] OpenCode
- [ ] Claude Code
- [ ] Cursor
- [ ] GitHub Copilot
- [ ] ChatGPT (manual injection)
- [ ] Mistral Le Chat (manual injection)

**For each platform:**
1. Install according to adapter instructions
2. Verify skill is discovered
3. Test activation with a simple request
4. Verify output is correct

**Status:** ⏸️ Unexecuted (requires multiple platforms)
**Result:** 
**Notes:** 

---

## Test Summary

### Total Tests: 25
- Mode Tests: 4
- Methodology Tests: 10
- Output Contract Tests: 2
- Edge Case Tests: 9
- Compatibility Tests: 3

### Execution Status
- ✅ Automated: 0 (all manual)
- ⏸️ Unexecuted: 25
- ✅ Passed: 0
- ❌ Failed: 0
- ⚠️ Blocked: 0

### Notes

1. **All tests are manual** and require execution with a live AI agent
2. **No tests have been executed** in this validation cycle
3. **Automated validation** is provided by `validate_skill.py` for structural checks
4. **Behavioral tests** cannot be automated without an AI agent to test against
5. **Test results should be documented** when executed

## How to Execute Tests

1. **Set up a test environment** with the brainstorm skill installed
2. **For each test:**
   - Note the test ID and description
   - Provide the specified input to the agent
   - Capture the full output
   - Compare against expected results
   - Record pass/fail and any notes
3. **Update this document** with actual results

## Expected vs. Actual Behavior

If any test reveals a discrepancy between expected and actual behavior:

1. **Document the actual behavior** in the test notes
2. **Determine if it's a bug or a valid interpretation**
3. **If bug:** Fix the skill and re-test
4. **If valid interpretation:** Update the expected results
5. **If methodology conflict:** Document as a known limitation

## Known Limitations

1. **Absurd Option Mandatory:** The original methodology requires exactly one absurd option. If users explicitly request no absurd options, the skill must either comply (breaking methodology) or refuse (breaking user request). This is an intentional design tension.

2. **Minimum Options:** The methodology specifies minimum option counts per mode. If users request fewer options than the minimum, the skill must decide whether to comply or use the minimum.

3. **Context Requirements:** The skill requires project context. For requests with truly no context, the skill must ask questions, which may frustrate users expecting immediate answers.

4. **Platform Variability:** Different platforms may have slightly different activation behavior, even with identical skill files.

---

*Last updated: Initial test suite definition*
*Next review: After first execution cycle*
