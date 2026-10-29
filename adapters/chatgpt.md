# ChatGPT Adapter - Brainstorm Skill

## Compatibility Status

**Native Support:** ⚠️ Partial
**Tested:** ❌ No
**Installation Method:** Manual or Plugin-based

## Overview

ChatGPT's support for Agent Skills varies by interface:

- **ChatGPT Web:** Requires a plugin (not a standalone skill folder)
- **ChatGPT Desktop:** Skills view exists but documentation is unclear on external skill installation
- **ChatGPT API:** Does not support Agent Skills

## Installation Options

### Option 1: Manual Context Injection (Recommended)

Since ChatGPT Web doesn't support standalone skill folders, use manual context injection:

```
User: Use the following Brainstorm skill instructions for this conversation:
[Paste contents of SKILL.md here]

Now, brainstorm ideas for [your request]
```

**Limitations:**
- Skill instructions must be re-injected for each new conversation
- Token count increases with skill context
- No automatic activation

### Option 2: Custom GPT with Embedded Instructions

1. Create a new Custom GPT in ChatGPT
2. In the instructions, include the brainstorming methodology from `SKILL.md`
3. Save and use this Custom GPT for brainstorming sessions

**Limitations:**
- Custom GPTs are tied to your account
- Cannot share as easily as skill folders
- May have token limits on instructions

### Option 3: Local Plugin Development (Advanced)

Develop a ChatGPT plugin that:
1. Reads the `brainstorm` skill folder from a local directory
2. Injects the instructions into the conversation context
3. Handles activation triggers

**Limitations:**
- Requires plugin development skills
- Must be approved by OpenAI for public use
- Not portable across users

## Activation

With manual context injection or Custom GPT:
- Use natural language triggers: "brainstorm", "ideate", "give me ideas for"
- The skill should respond with the five-section output contract

## Known Limitations

1. **No Native Folder Support:** ChatGPT doesn't read `.agents/skills/` by default
2. **No Automatic Discovery:** Skills aren't auto-discovered from file system
3. **Token Overhead:** Manual injection adds ~14K tokens of context
4. **Conversation Scope:** Instructions apply only to current conversation
5. **No File Access:** Cannot read `references/techniques.md` without manual inclusion

## Workarounds

1. **For technique access:** Include relevant sections from `references/techniques.md` in your prompt when needed
2. **For persistence:** Create a Custom GPT with the full methodology embedded
3. **For portability:** Share the `brainstorm` folder; users can use their preferred installation method

## Recommendation

For ChatGPT users, **Option 1 (Manual Context Injection)** is the most portable and immediate solution. For frequent use, **Option 2 (Custom GPT)** provides better persistence.

Native folder-based skill support is not currently available for ChatGPT Web.
