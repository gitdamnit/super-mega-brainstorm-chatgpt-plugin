# Replace local project safely (Linux)

**Target:** `/home/evan/Projects/super-mega-brainstorm-skill/`.

This is a replacement of **project contents**, not of your local Git history without consent. Keep existing projects as backups until the new package is verified.

### 1. Put the new release ZIP at `~/Downloads/super-mega-brainstorm-skill-release.zip`

### 2. Run these commands in your terminal

```bash
set -euo pipefail
root="$HOME/Projects"
target="$root/super-mega-brainstorm-skill"
zipfile="$HOME/Downloads/super-mega-brainstorm-skill-release.zip"
stamp="$(date +%Y%m%d-%H%M%S)"
mkdir -p "$root"
test -f "$zipfile" || { echo "Missing $zipfile"; exit 1; }
# Keep the entire old project, including Git and OpenCode state, recoverable.
if [ -e "$target" ]; then
  mv -- "$target" "${target}.legacy-${stamp}"
  echo "Backup saved: ${target}.legacy-${stamp}"
fi
# Release archive includes one top-level project directory.
unzip -q "$zipfile" -d "$root"
cd "$target"
bash tests/run_tests.sh
```

If tests fail, your old project remains in the timestamped `.legacy-*` directory. Inspect or restore it, do not delete backups until you are satisfied. If your original directory contained a `.git` repository, it remains inside the backup; the newly extracted directory does **not** automatically inherit that history or a remote connection. You can deliberately reinitialize or reconnect a repository afterward. The prior Git That Shit snapshot is archived rather than distributed.

### 3. Invoke via your host's recognized skills location

A project folder alone does not guarantee a host auto-indexes the skill. Configure or install this folder through the standard skills path your version of OpenCode supports. If the agent can directly read the project folder, instruct it to load the folder's `SKILL.md` and local references.

### 4. Verify user-visible behavior

- “Super Mega Brainstorm my new product idea” loads full workflow.
- Unqualified “brainstorm this” routes here unless another exact named skill was requested.
- An idea with no defensible solutions is allowed to return zero, without padding.
- Deliberately false causal argument triggers a substantive fallacy/evidence warning.
- Valid conditional proof with unknown empirical premises is called valid but not established sound.

**No local files were modified by ChatGPT. These commands act only when you choose to run them.**
