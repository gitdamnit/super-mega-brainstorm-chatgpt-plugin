# Brainstorm Universal Agent Skill

A production-quality, portable, platform-independent Agent Skill for structured brainstorming that produces genuinely different, constraint-aware options and converges on actionable decisions.

## Overview

This skill implements a rigorous brainstorming methodology that:
- Produces **structurally different** ideas (not cosmetic variations)
- Anchors to **actual project constraints** and context
- Explicitly states **costs, trade-offs, and dependencies** for every option
- Includes **exactly one deliberately absurd idea** per session
- **Kills weak ideas** with clear reasons
- **Ranks** surviving options with winner-versus-runner-up justification
- States **overturn conditions** (what would change the recommendation)
- Provides a **concrete next action**
- Separates **rejected** and **parked** ideas

## Package Structure

```
brainstorm/
├── SKILL.md                    # Canonical skill instructions
├── README.md                   # This file
├── references/
│   └── techniques.md           # Complete technique catalog (30+ methods)
├── adapters/
│   ├── chatgpt.md              # ChatGPT installation notes
│   ├── codex.md                # OpenAI Codex installation notes
│   ├── claude.md               # Claude installation notes
│   ├── mistral.md              # Mistral Le Chat installation notes
│   └── opencode.md             # OpenCode installation notes
└── tests/
    └── acceptance.md            # Manual acceptance test cases
```

## Installation

### Universal Installation (Recommended)

The portable Agent Skills convention uses `.agents/skills/`:

```bash
# Clone or download this repository
mkdir -p .agents/skills/
# Copy the brainstorm folder to .agents/skills/brainstorm
cp -R /path/to/brainstorm .agents/skills/brainstorm
```

### Platform-Specific Paths

| Platform | Primary Path | Secondary Paths | Notes |
|----------|--------------|-----------------|-------|
| **OpenCode** | `.opencode/skills/` | `.claude/skills/`, `~/.config/opencode/skills/` | Use `/brainstorm` to invoke |
| **Claude Code** | `.claude/skills/` | `~/.claude/skills/` | Directory name is the command |
| **Cursor** | `.cursor/skills/` | `~/.cursor/skills/` | Use `/` in Agent chat |
| **GitHub Copilot** | `.github/skills/` | `~/.copilot/skills/` | Automatic by description |
| **Gemini CLI** | `.gemini/skills/` | `~/.gemini/skills/` | Use `activate_skill` tool |
| **OpenAI Codex** | `.agents/skills/` | Up the tree, `/etc/codex/skills` | `$brainstorm` or `/skills` |
| **Mistral Le Chat** | Varies | Varies | See adapter notes |

See individual adapter files for platform-specific details.

## Activation

The skill activates automatically when users:
- Say **brainstorm**, ideate, ideas, options, possibilities
- Ask for **names, titles, taglines, features, domain names**
- Describe being **stuck** without asking a specific question
- Use phrases like "what if", "how could we", "help me think through"

## Operating Modes

| Mode | Trigger | Options | Questions | Use Case |
|------|---------|---------|-----------|----------|
| **QUICK** | "10 names for...", casual requests | 4-6 | 0 (state assumptions) | Fast, low-context requests |
| **STANDARD** | Default for "give me ideas for..." | 5-8 | ≤3 (missing context only) | Typical brainstorming |
| **DEEP** | "help me think this through", big decisions | 8-12 (2 waves) | 1-2 rounds | Complex, high-stakes decisions |

## Output Contract

Every brainstorming session produces **exactly five sections** in this order:

1. **Framing** — The actual problem being solved (1-2 sentences)
2. **Options** — Structurally different ideas, each with:
   - Bold 2-4 word name
   - *mechanism: description*
   - One-line pitch
   - **Constraint line** (Costs, Gives up, Needs)
   - Exactly one absurd option marked *(the absurd one)*
3. **Kill list** — Discarded ideas with reasons ("Not doing X because Y")
4. **Ranking** — Best → worst, with:
   - Winner justified **against runner-up**
   - **Overturn condition** (what would change the ranking)
5. **Next action** — Chosen direction, single action, parked items

## Offline Operation

This skill is **fully offline** and requires:
- ✅ No API keys
- ✅ No external services
- ✅ No internet access
- ✅ No paid subscriptions
- ✅ No proprietary dependencies

All techniques, methodologies, and reference material are included locally.

## Compatibility

| Platform | Native Support | Tested | Notes |
|----------|----------------|--------|-------|
| OpenCode | ✅ Yes | ❌ No | Spec-conformant |
| Claude Code | ✅ Yes | ❌ No | Spec-conformant |
| Cursor | ✅ Yes | ❌ No | Spec-conformant |
| GitHub Copilot | ✅ Yes | ❌ No | Spec-conformant |
| Gemini CLI | ✅ Yes | ❌ No | Spec-conformant |
| OpenAI Codex | ✅ Yes | ❌ No | Spec-conformant |
| Mistral Le Chat | ⚠️ Varies | ❌ No | See adapter |

**Note:** Compatibility is based on the [Agent Skills specification](https://agentskills.io). Actual behavior may vary by platform implementation and version.

## Validation

Run the included validation script to verify the skill package:

```bash
python3 validate_skill.py [/path/to/brainstorm]
```

This checks:
- Required files exist
- YAML frontmatter is valid
- Skill name matches directory
- Internal references resolve
- All five output sections defined
- Three operating modes preserved
- Technique catalog present
- No unexpected dependencies

## Testing

See `tests/acceptance.md` for manual acceptance test cases covering:
- All three operating modes (QUICK, STANDARD, DEEP)
- Various problem domains (naming, architecture, strategy)
- Edge cases (insufficient context, redundant options)
- Methodology requirements (absurd idea, kill list, ranking)

## License

No license has been assigned to this package. The original methodology and content are preserved as-is from the source material.

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Canonical skill instructions (authoritative) |
| `references/techniques.md` | Complete technique catalog (30+ methods) |
| `adapters/*.md` | Platform-specific installation notes |
| `tests/acceptance.md` | Manual acceptance test cases |
| `validate_skill.py` | Automated validation script |
| `CHANGELOG.md` | Change history and improvements |

## Changelog

See `CHANGELOG.md` for detailed change history.

## Contributing

This is a production-ready, validated skill package. Modifications should:
1. Preserve the original methodology and contracts
2. Maintain cross-platform compatibility
3. Not introduce external dependencies
4. Pass all validation checks

## Support

For issues or questions about this skill package, refer to the original methodology documentation in `SKILL.md` and the technique catalog in `references/techniques.md`.
