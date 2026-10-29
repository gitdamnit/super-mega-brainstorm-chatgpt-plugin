# OpenAI Codex Adapter - Brainstorm Skill

## Compatibility Status

**Native Support:** ✅ Yes
**Tested:** ❌ No (Specification-conformant)
**Installation Method:** Folder-based

## Overview

OpenAI Codex has built-in support for Agent Skills using the `.agents/skills/` convention. The brainstorm skill should work natively with proper installation.

## Installation

### Method 1: Universal Path (Recommended)

```bash
# Ensure the skill folder is named 'brainstorm'
mkdir -p .agents/skills/
cp -R /path/to/brainstorm .agents/skills/brainstorm
```

Codex will discover and load the skill from `.agents/skills/brainstorm/SKILL.md`.

### Method 2: Local User Path

```bash
mkdir -p ~/.agents/skills/
cp -R /path/to/brainstorm ~/.agents/skills/brainstorm
```

This makes the skill available to all your projects.

### Method 3: System-wide Path

```bash
sudo mkdir -p /etc/codex/skills/
sudo cp -R /path/to/brainstorm /etc/codex/skills/brainstorm
```

This makes the skill available system-wide (requires appropriate permissions).

## Activation

The skill activates automatically when Codex detects:
- Keywords: **brainstorm**, ideate, ideas, options, possibilities
- Phrases: "what if", "how could we", "help me think through"
- Requests: "give me ideas for", "I'm stuck"

**Manual invocation:**
- Use `$brainstorm` in your prompt
- Or reference `/skills` list

## Configuration

Codex supports an optional `agents/openai.yaml` file for additional metadata:

```yaml
# Optional: .agents/openai.yaml
skills:
  brainstorm:
    display_name: "Brainstorm"
    description: "Structured brainstorming with constraint-aware options and convergence"
    version: "1.0.0"
```

This file is **optional** and not required for basic functionality.

## Features Supported

✅ **Automatic Discovery:** Codex scans `.agents/skills/` on startup
✅ **Activation Triggers:** All defined triggers work
✅ **YAML Frontmatter:** Full support for metadata
✅ **Markdown Content:** Full support for skill instructions
✅ **Reference Files:** Can read `references/techniques.md` when referenced
✅ **Progressive Disclosure:** Only loads technique details when explicitly referenced

## Known Limitations

1. **Path Precedence:** Local project paths take precedence over user and system paths
2. **Caching:** Skill may be cached; restart Codex to reload after changes
3. **No Hot Reload:** Changes to skill files require restart to take effect
4. **File Size:** Very large skill files may be truncated (unlikely with brainstorm)

## Validation

Verify the skill is properly installed:

```bash
# Check if Codex can find the skill
ls .agents/skills/brainstorm/SKILL.md

# Verify YAML frontmatter
head -10 .agents/skills/brainstorm/SKILL.md
```

## Troubleshooting

**Skill not activating:**
1. Verify the folder is named exactly `brainstorm`
2. Verify `SKILL.md` exists at the folder root
3. Verify YAML frontmatter has valid `name: brainstorm`
4. Restart Codex to reload skills

**Skill loading but not behaving correctly:**
1. Check for syntax errors in `SKILL.md`
2. Verify all required sections exist
3. Check that internal references (like `references/techniques.md`) are correct

## Recommendation

For Codex users, **Method 1 (Universal Path)** is recommended as it:
- Works across all projects
- Follows the cross-vendor convention
- Is compatible with other Agent Skills-enabled tools
- Allows per-project customization if needed

The brainstorm skill should work natively with Codex's Agent Skills implementation.
