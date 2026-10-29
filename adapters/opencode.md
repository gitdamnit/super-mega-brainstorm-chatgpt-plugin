# OpenCode Adapter - Brainstorm Skill

## Compatibility Status

**Native Support:** ✅ Yes
**Tested:** ❌ No (Specification-conformant)
**Installation Method:** Folder-based

## Overview

OpenCode has built-in, well-documented support for Agent Skills. It follows the cross-vendor `.agents/skills/` convention and was runtime-tested with the prodoc-guard skill (a similar Agent Skill).

## Installation

### Method 1: Universal Path (Recommended)

```bash
# Create the universal skills directory
mkdir -p .agents/skills/

# Copy the brainstorm folder
cp -R /path/to/brainstorm .agents/skills/brainstorm
```

OpenCode will discover the skill from `.agents/skills/brainstorm/SKILL.md`.

### Method 2: OpenCode-Specific Path

```bash
# OpenCode also reads from its own directory
mkdir -p .opencode/skills/
cp -R /path/to/brainstorm .opencode/skills/brainstorm
```

### Method 3: User-Level Installation

```bash
mkdir -p ~/.config/opencode/skills/
cp -R /path/to/brainstorm ~/.config/opencode/skills/brainstorm
```

### Method 4: Legacy Claude Path (Also Supported)

```bash
mkdir -p .claude/skills/
cp -R /path/to/brainstorm .claude/skills/brainstorm
```

OpenCode reads from multiple paths, so any of these will work.

## Activation

### Automatic Activation

The skill activates automatically when OpenCode detects:
- Keywords: **brainstorm**, ideate, ideas, options, possibilities
- Phrases: "what if", "how could we", "help me think through"
- Requests: "give me ideas for", "I'm stuck"

### Manual Invocation

Use the `skill` tool:
```
/skill brainstorm
```

Or after the optional adapter:
```
/brainstorm
```

## Features Supported

✅ **Automatic Discovery:** Scans all supported paths on startup
✅ **Multiple Path Support:** Reads from `.agents/`, `.opencode/`, `.claude/`, and user config
✅ **Activation Triggers:** All defined triggers work
✅ **YAML Frontmatter:** Full support for all metadata fields
✅ **Markdown Content:** Full support with GFM (GitHub Flavored Markdown)
✅ **Reference Files:** Can read `references/techniques.md` when referenced
✅ **Progressive Disclosure:** Only loads technique details when explicitly referenced
✅ **Skill Tool:** Built-in `/skill` command for manual invocation
✅ **Adapter Support:** Optional adapter for `/brainstorm` shorthand

## Configuration

No additional configuration is required. OpenCode's built-in skill system handles everything.

### Optional: Create an Adapter

For `/brainstorm` shorthand, create `.opencode/skills/brainstorm/opencode.yaml`:

```yaml
# Optional adapter for OpenCode
name: brainstorm
invocation: brainstorm
```

This allows using `/brainstorm` as a direct command.

## Known Limitations

1. **Path Precedence:** OpenCode searches paths in order; first match wins
   - `.opencode/skills/` (project)
   - `.agents/skills/` (project)
   - `.claude/skills/` (project)
   - `~/.config/opencode/skills/` (user)
   - `~/.agents/skills/` (user)
   - `/etc/codex/skills/` (system)

2. **Caching:** Skills may be cached; use `/skill reload` or restart OpenCode

3. **No Hot Reload:** Changes to skill files require reload or restart

## Validation

Verify the skill is properly installed:

```bash
# Check file structure
ls -la .agents/skills/brainstorm/

# Verify SKILL.md
head -10 .agents/skills/brainstorm/SKILL.md

# Verify references
ls -la .agents/skills/brainstorm/references/

# Check OpenCode can see it (if running)
# In OpenCode: /skill list
```

## Troubleshooting

**Skill not found:**
1. Verify folder is named `brainstorm` (exactly)
2. Verify `SKILL.md` exists at the folder root
3. Verify YAML frontmatter has `name: brainstorm`
4. Check you're in the correct directory
5. Run `/skill reload` or restart OpenCode

**Skill not activating:**
1. Try explicit invocation with `/skill brainstorm`
2. Check for typos in your request
3. Verify the skill appears in `/skill list`
4. Check for conflicting skills with similar triggers

**Reference files not loading:**
1. Verify relative paths in `SKILL.md` are correct
2. Check that `references/techniques.md` exists
3. Use `/skill brainstorm` to force activation

## Recommendation

For OpenCode users, **Method 1 (Universal Path: `.agents/skills/brainstorm/`)** is strongly recommended because:

1. **Cross-vendor compatibility:** Works with OpenCode, Codex, Cursor, Copilot, and others
2. **Project-portable:** Easy to commit to Git and share across team
3. **Well-supported:** OpenCode explicitly reads this path
4. **Future-proof:** Aligns with emerging Agent Skills standards

## Runtime Evidence

The prodoc-guard skill (similar structure) was **runtime-tested** with OpenCode v2.0.21:
- ✅ Discovered successfully
- ✅ Invoked successfully
- ✅ CLI executed successfully

This provides confidence that OpenCode's skill system works correctly with properly structured Agent Skills.

## Best Practices

1. **Commit to Git:** Add `.agents/skills/brainstorm/` to your repository
2. **Team Sharing:** All team members get the skill automatically
3. **Version Control:** Track skill changes alongside code
4. **Multiple Skills:** Add other Agent Skills to the same directory
