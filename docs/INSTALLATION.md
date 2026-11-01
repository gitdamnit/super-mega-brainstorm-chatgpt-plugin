# Installation, distribution and verification

## ChatGPT
Install the shared or directory-listed **Super Mega Brainstorm** plugin through ChatGPT's supported Plugins interface when available. Invoke it with `@super-mega-brainstorm` or by name.

Publishing source code on GitHub **does not** install the plugin to a user's ChatGPT account and **does not** itself create a public ChatGPT Plugin Directory listing. Directory publication/sharing is a separate product workflow.

## Agent Plugin hosts
Install this complete repository as a plugin, rooted at `plugin.json`, if your host supports the portable Agent Plugins specification. Vendor-specific support varies. `.codex-plugin/plugin.json` provides additional product-facing metadata.

## Standalone skill hosts
Install the complete `skills/super-mega-brainstorm-skill/` directory in your host's supported skills path. Preserve all references, scripts, and related files. The skill cannot run to full fidelity using `SKILL.md` alone.

## Local tests
```bash
cd skills/super-mega-brainstorm-skill
bash tests/run_tests.sh
```

Python is optional for the conversational workflow, but required to run the packaged test and checker scripts.

## Limits
The workflow does not guarantee truth. A structurally valid proof cannot establish empirical premise truth. Optional tests and checkers have intentionally limited scope. The package is neither an online service nor a proprietary AI model.
