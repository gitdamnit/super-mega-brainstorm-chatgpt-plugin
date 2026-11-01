# SUPER MEGA BRAINSTORM PLUGIN FOR CHATGPT

<img width="874" height="487" alt="image" src="https://github.com/user-attachments/assets/927aed46-a15f-4e21-a3a2-fe4c4140fbb3" />


### The ChatGPT plugin for ideas that survive scrutiny.

**Brainstorm without the bullshit.** Super Mega Brainstorm explores possibilities and then makes the reasoning earn its keep. It is a reusable workflow for strategic decisions, research, product design, technical planning, creative problems, and arguments that sound persuasive but might be completely wrong.

This repository packages **Super Mega Brainstorm for ChatGPT** as a portable [Agent Plugin](https://agent-plugins.org/specification), with the complete original reasoning workflow bundled under [`skills/super-mega-brainstorm-skill/`](skills/super-mega-brainstorm-skill/).

**Version 0.2.0 · Feature-complete prototype · Created by Evan Zellner**

## What it does

- **Diverges first.** Explores materially different mechanisms, not 20 superficial variations.
- **Recombines ideas.** Finds connections, contradictions, and missed possibilities.
- **Evaluates openly.** Weighs benefits, assumptions, trade-offs, risks, and a real *do-nothing* baseline.
- **Red-teams its own recommendations.** Looks for alternative explanations and conditions that would overturn the answer.
- **Runs the Advanced Smell Test.** Applies the bundled fallacy atlas, evidence standards, causal and statistical checks, and reasoning audit.
- **Checks formal arguments.** Distinguishes logical validity from the truth of real-world premises. Includes optional offline truth-table and categorical checkers.
- **Allows uncomfortable answers.** One defensible option, several, postponement, or **NO DEFENSIBLE SOLUTION IDENTIFIED** are all valid outcomes.

### How the complete workflow fits together

`Frame → Evidence → Baseline → Diverge → Connect → Evaluate → Attack → Smell Test → Formal argument gate → Decision record`

Every invocation uses stages **0–10**, without a fake quick mode or required idea quota. See [the full specification](skills/super-mega-brainstorm-skill/SKILL.md).

## Using it in ChatGPT

If **Super Mega Brainstorm** is available through your ChatGPT Plugin Directory or a supported share, install it using ChatGPT's normal plugin flow. Then invoke the plugin in a chat:

```text
@super-mega-brainstorm Brainstorm better ways to cut recruiting time without reducing candidate experience.
```

```text
@super-mega-brainstorm Red-team this proposal and tell me what would make it fail.
```

```text
@super-mega-brainstorm Audit the evidence and logic behind this claim.
```

When this workflow is installed and discoverable, **“Super Mega Brainstorm”** explicitly activates it. A generic **“brainstorm”** can also route here when the host recognizes the skill and no different named brainstorming skill takes precedence.

**Important:** Uploading a ZIP or publishing this repository **does not automatically install the plugin in ChatGPT** or publish it to ChatGPT's Plugin Directory. Account/workspace installation and public plugin sharing are separate from GitHub source distribution.

## Running the standalone skill

The underlying [portable skill](skills/super-mega-brainstorm-skill/) is included in full.

For clients supporting Agent Plugins, use the repository's **root `plugin.json`** and the complete `skills/` directory according to that client's installation instructions.

For clients supporting standalone skills, install the *entire* `skills/super-mega-brainstorm-skill/` folder into the location your host actually recognizes. Do not install just `SKILL.md`: the bundled reference files are required for a full run. Model-agnostic does not imply all hosts implement identical skill discovery.

There is no hosted service, MCP server, account integration, or API key required for the *reasoning workflow*. Optional external verification may require whatever research tools the host provides.

## Repository layout

```text
plugin.json                             Portable Agent Plugin manifest
.codex-plugin/plugin.json               Codex/OpenAI-oriented metadata
skills/super-mega-brainstorm-skill/
  SKILL.md                              Full behavioral specification
  references/                           Techniques, evidence, fallacies, formal logic
  scripts/                              Optional checkers and validators
  tests/                                Unit tests and scenario fixtures
  docs/                                 Integration and verification history
.github/workflows/ci.yml                Plugin-level continuous integration
docs/INSTALLATION.md                     How to use the plugin and skill
docs/PLUGIN_VS_SKILL.md                  Exact distinction between releases
```

## Verify the release locally

```bash
cd skills/super-mega-brainstorm-skill
bash tests/run_tests.sh
```

The supplied plugin release candidate passed **45 unit tests**, package checks, and logic-checker smoke tests on October 31, 2026. These are structural and selected logical checks, **not scientific validation** or a promise of error-free reasoning.

## Origins and rights

Maintained by **Evan Zellner**. The v0.2.0 behavioral specification was developed with GPT-6; selected engineering and facilitation ideas from prior DeepSeek/OpenCode work were incorporated without replacing that specification. Refer to [the integration report](skills/super-mega-brainstorm-skill/docs/INTEGRATION_REPORT.md) and [source inventory](skills/super-mega-brainstorm-skill/references/source-inventory.md).

This is an independent community project, **not an official or OpenAI-verified product**.

**License:** The maintainer has not selected a license. Public visibility is **not** an open-source license and does not grant general rights to reproduce, modify, or redistribute this work. A license can be added by its owner later.

[Installation notes](docs/INSTALLATION.md) · [Plugin versus original skill](docs/PLUGIN_VS_SKILL.md)
