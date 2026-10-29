# Claude / Claude Code Adapter - Brainstorm Skill

## Compatibility Status

**Native Support:** ✅ Yes
**Tested:** ❌ No (Specification-conformant)
**Installation Method:** Folder-based

## Overview

Both Claude (web) and Claude Code support Agent Skills through folder-based installation. The skill discovery and activation behavior differs slightly between the two.

## Installation

### For Claude Code (Recommended)

```bash
# Create the skills directory
mkdir -p .claude/skills/

# Copy the brainstorm folder
cp -R /path/to/brainstorm .claude/skills/brainstorm
```

Claude Code will discover the skill from `.claude/skills/brainstorm/SKILL.md`.

**Alternative user-level installation:**
```bash
mkdir -p ~/.claude/skills/
cp -R /path/to/brainstorm ~/.claude/skills/brainstorm
```

### For Claude Web

Claude Web also supports skills, but the installation path may vary. Use the same folder structure:

```bash
mkdir -p ~/.claude/skills/
cp -R /path/to/brainstorm ~/.claude/skills/brainstorm
```

## Activation

### Claude Code

The skill activates automatically when you:
- Type `/brainstorm` (directory name is the command)
- Use natural language triggers in conversation

**Example:**
```
User: /brainstorm
User: brainstorm ideas for a new feature
User: give me some names for my startup
```

### Claude Web

Activation is similar but may require explicit invocation:
- Use `/brainstorm` command
- Or use natural language triggers

## Features Supported

✅ **Automatic Discovery:** Scans skills directory on startup
✅ **Directory-as-Command:** `/brainstorm` invokes the skill
✅ **Natural Language Triggers:** All defined triggers work
✅ **YAML Frontmatter:** Full support
✅ **Markdown Content:** Full support
✅ **Reference Files:** Can read `references/techniques.md` when referenced
✅ **Progressive Disclosure:** Only loads technique details when needed

## Configuration

No additional configuration is required. The skill metadata in `SKILL.md` frontmatter is sufficient.

## Known Limitations

1. **Claude Code Specific:**
   - Skills are project-local by default
   - User-level skills (`~/.claude/skills/`) are also supported
   - No automatic reload; restart to pick up changes

2. **Claude Web Specific:**
   - Skill support may vary by interface version
   - Some features may require explicit invocation
   - Check Claude's documentation for current skill support

3. **General:**
   - Skill folder name must match the `name` in YAML frontmatter
   - `SKILL.md` must be at the folder root
   - Internal file references use relative paths from the skill root

## Validation

Verify installation:

```bash
# Check file structure
ls -la .claude/skills/brainstorm/

# Verify SKILL.md exists and has correct name
head -5 .claude/skills/brainstorm/SKILL.md

# Verify references are accessible
ls -la .claude/skills/brainstorm/references/
```

## Troubleshooting

**Skill not found:**
1. Verify folder is named `brainstorm` (exactly)
2. Verify `SKILL.md` exists at `.claude/skills/brainstorm/SKILL.md`
3. Verify YAML frontmatter has `name: brainstorm`
4. Restart Claude Code

**Skill not activating:**
1. Try explicit invocation with `/brainstorm`
2. Check for typos in activation triggers
3. Verify the skill is listed in Claude's skill management

**Reference files not loading:**
1. Verify relative paths in `SKILL.md` are correct
2. Check that `references/techniques.md` exists
3. Use `/brainstorm` to force skill activation

## Recommendation

For Claude/Claude Code users:
- Use **project-level installation** (`.claude/skills/brainstorm/`) for project-specific skills
- Use **user-level installation** (`~/.claude/skills/brainstorm/`) for skills you want across all projects
- The brainstorm skill should work natively with both interfaces

The `/brainstorm` command is the most reliable activation method.
