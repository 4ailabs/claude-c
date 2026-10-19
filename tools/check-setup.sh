#!/usr/bin/env bash
# Verifica los prerrequisitos del evento: Git, Python 3.11+, uv y Claude Code.
set -u
ok=0
check() { # nombre comando...
  local name=$1; shift
  if out=$("$@" 2>&1 | head -1); then printf '  ✓ %-12s %s\n' "$name" "$out"; else printf '  ✗ %-12s no encontrado\n' "$name"; ok=1; fi
}
echo "Prerrequisitos:"
check git git --version
check uv uv --version
check claude claude --version
if python3 -c 'import sys; sys.exit(sys.version_info < (3, 11))' 2>/dev/null; then
  printf '  ✓ %-12s %s\n' python "$(python3 --version)"
else
  printf '  ✗ %-12s se necesita 3.11+\n' python; ok=1
fi
exit $ok
