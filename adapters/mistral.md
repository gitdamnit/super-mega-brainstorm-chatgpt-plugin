# Mistral Le Chat Adapter - Brainstorm Skill

## Compatibility Status

**Native Support:** ⚠️ Varies by Interface
**Tested:** ❌ No
**Installation Method:** Interface-dependent

## Overview

Mistral Le Chat's support for Agent Skills depends on the specific interface and version. The web interface, desktop app, and API may have different capabilities.

## Installation Options

### Option 1: Manual Context Injection (Most Portable)

```
User: Use the following Brainstorm skill for this conversation:
[Paste contents of SKILL.md here]

Now, brainstorm [your request]
```

**Pros:**
- Works in any Mistral interface
- No installation required
- Fully portable

**Cons:**
- Must re-inject for each new conversation
- Adds token overhead
- No automatic activation

### Option 2: Local Skills Directory (If Supported)

Some Mistral interfaces may support a local skills directory:

```bash
# Check if your interface supports this
mkdir -p ~/.mistral/skills/
cp -R /path/to/brainstorm ~/.mistral/skills/brainstorm
```

**Note:** This path is **not guaranteed** to work. Check your specific Mistral interface documentation.

### Option 3: Project-Level Skills (If Supported)

```bash
mkdir -p .mistral/skills/
cp -R /path/to/brainstorm .mistral/skills/brainstorm
```

**Note:** Support varies by interface version.

## Activation

With manual context injection:
- Use natural language: "brainstorm", "ideate", "give me ideas"
- The skill context will guide the response

With native support (if available):
- May activate automatically on triggers
- Or use explicit invocation if supported

## Features Supported

✅ **Manual Injection:** Always works with context pasting
⚠️ **Automatic Discovery:** Depends on interface
⚠️ **YAML Frontmatter:** Depends on interface
✅ **Markdown Content:** Supported when injected manually
⚠️ **Reference Files:** Only with manual inclusion or native support

## Known Limitations

1. **Interface Variability:** Different Mistral interfaces have different skill support
2. **No Universal Standard:** Unlike OpenCode/Claude, Mistral doesn't have a single documented skill path
3. **Token Overhead:** Manual injection adds ~14K tokens
4. **No Persistence:** Manual context doesn't persist across conversations
5. **Documentation Gap:** Official skill support documentation may be limited

## Workarounds

### For Technique Access

Include the relevant technique sections when needed:

```
User: For technique reference, also include this from references/techniques.md:
[Paste relevant technique sections]

Now brainstorm [your request]
```

### For Persistence

Create a text file with the skill instructions and reference it:

```bash
# Save to a file
echo "Brainstorm skill instructions:" > mistral_brainstorm.txt
cat SKILL.md >> mistral_brainstorm.txt

# Then in Mistral:
User: Load instructions from mistral_brainstorm.txt
User: brainstorm [your request]
```

## Validation

Verify your installation method:

```bash
# For manual injection
wc -l SKILL.md  # Should be ~400+ lines

# For directory-based (if supported)
ls -la ~/.mistral/skills/brainstorm/ 2>/dev/null || echo "Path not supported"
```

## Troubleshooting

**Skill not activating:**
1. Try manual context injection
2. Check if your Mistral interface version supports skills
3. Verify the skill folder structure is correct
4. Try different activation phrases

**Inconsistent behavior:**
1. Ensure full skill context is included
2. Check for conflicting instructions in your prompt
3. Verify the technique catalog is accessible when referenced

## Recommendation

For Mistral Le Chat users, **Option 1 (Manual Context Injection)** is the most reliable approach because:
- It works across all interface versions
- It doesn't depend on undocumented features
- It's fully portable
- It gives you control over when the skill is active

If your specific Mistral interface supports folder-based skills, use the appropriate path from Options 2 or 3.

## Interface-Specific Notes

### Web Interface
- Most likely to require manual injection
- Check for any "Skills" or "Plugins" settings
- May support file upload for context

### Desktop App
- More likely to support local skills directory
- Check preferences for skill/plugin settings
- May support `.mistral/skills/` or similar

### API
- Unlikely to support Agent Skills natively
- Use manual context injection in your API calls
- Include skill instructions in the messages array

### Mobile App
- Least likely to support skills
- Manual injection is the only reliable method
