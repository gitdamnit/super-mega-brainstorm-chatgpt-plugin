# Super Mega Brainstorm plugin versus the original skill

**The skill** supplies the reasoning method: `SKILL.md`, the local evidence, fallacy and formal-logic reference corpus, checkers, examples, tests, and workflow instructions.

**The plugin** wraps that complete skill with a portable plugin identity and client presentation metadata.

| Detail | Base skill ZIP | Plugin ZIP / this repository |
| --- | --- | --- |
| Primary entry point | `SKILL.md` | Root `plugin.json` |
| Packaging | One complete `super-mega-brainstorm-skill/` directory | `skills/super-mega-brainstorm-skill/` inside plugin |
| ChatGPT-oriented metadata | None at root | `.codex-plugin/plugin.json` |
| Core stages 0–10 and Advanced Smell Test | Included | Included, unchanged |
| References and examples | Included | Included |
| Categorical checker | v0.2.0 baseline | Small fix rejecting ambiguous `No S are not P` forms |
| Regression test | v0.2.0 baseline | Adds explicit double-negative test |

The uploaded archives differed in only two bundled skill source files: `scripts/categorical_checker.py` and `tests/test_categorical_checker.py`. Other skill files matched.

This plugin is **not** a standalone AI model or server, an automatic ChatGPT installation, or a certification that every conclusion is correct.
