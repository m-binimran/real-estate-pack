#!/usr/bin/env bash
# Remove real-estate-pack from a target workspace. Only deletes files it installed.
# Usage: ./uninstall.sh /path/to/your/workspace
set -euo pipefail

PROJECT_PATH="${1:-}"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -z "$PROJECT_PATH" || ! -d "$PROJECT_PATH" ]]; then
  echo "Usage: ./uninstall.sh /path/to/your/workspace" >&2
  exit 1
fi

echo "Removing real-estate-pack from $PROJECT_PATH"

for f in "$SRC"/hooks/*.py;  do rm -f "$PROJECT_PATH/.claude/hooks/$(basename "$f")"; done
for d in "$SRC"/skills/*/;   do rm -rf "$PROJECT_PATH/.claude/skills/$(basename "$d")"; done
for f in "$SRC"/loops/*.md;  do rm -f "$PROJECT_PATH/.claude/commands/$(basename "$f")"; done
for f in "$SRC"/commands/*.md; do rm -f "$PROJECT_PATH/.claude/commands/$(basename "$f")"; done
for f in "$SRC"/agents/*.md; do rm -f "$PROJECT_PATH/.claude/agents/$(basename "$f")"; done
echo "  removed hooks, skills, commands, agents"

CLAUDE="$PROJECT_PATH/CLAUDE.md"
MARKER="<!-- ===== real-estate-pack rules (auto-installed) ===== -->"
if [[ -f "$CLAUDE" ]] && grep -qF "$MARKER" "$CLAUDE"; then
  awk -v m="$MARKER" 'index($0,m){exit} {print}' "$CLAUDE" > "$CLAUDE.tmp"
  mv "$CLAUDE.tmp" "$CLAUDE"
  echo "  stripped real-estate-pack rules from CLAUDE.md"
elif [[ -f "$CLAUDE" ]]; then
  echo "  WARNING: marker not found in CLAUDE.md; remove the rules manually" >&2
fi

DEST="$PROJECT_PATH/.claude/settings.json"
if [[ -f "$DEST" ]]; then
  if diff -q "$DEST" "$SRC/hooks/settings.json" >/dev/null 2>&1; then
    rm -f "$DEST"
    echo "  removed .claude/settings.json (was real-estate-pack's)"
  else
    echo "  WARNING: settings.json has your own changes; remove the 'hooks' block manually" >&2
  fi
fi

echo "Done. Restart Claude Code so the changes take effect."
