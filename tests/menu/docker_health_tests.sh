#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$HOME/docker"
VENV_PYTEST="$ROOT/venv/bin/pytest"
PYTEST_BIN="${VENV_PYTEST}"
if [[ ! -x "$PYTEST_BIN" ]]; then
  PYTEST_BIN="$(command -v pytest || true)"
fi
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1

TARGET_DIR="$HOME/docker/tests/active/system"
if [[ -n "$PYTEST_BIN" && -d "$TARGET_DIR" ]] && compgen -G "$TARGET_DIR/test_*.py" > /dev/null; then
  echo "Running Docker Health Checks via: $PYTEST_BIN -vv -s $TARGET_DIR"
  "$PYTEST_BIN" -vv -s "$TARGET_DIR"
else
  echo "No Docker Health Checks found in $TARGET_DIR — placeholder OK."
  exit 0
fi
