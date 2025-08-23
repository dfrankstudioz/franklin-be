#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$HOME/docker"
VENV_PYTEST="$ROOT/venv/bin/pytest"
PYTEST_BIN="${VENV_PYTEST}"
if [[ ! -x "$PYTEST_BIN" ]]; then
  PYTEST_BIN="$(command -v pytest || true)"
fi
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1

# Wait for API route (/chat) up to ~20s.
# We accept any HTTP status (200..599) as "server is responding" to avoid 404 spam.
echo "Waiting for API route /chat to respond..."
for i in {1..20}; do
  code="$(curl -s -o /dev/null -w '%{http_code}' http://localhost:9006/chat || true)"
  if [[ "$code" =~ ^[0-9]{3}$ && "$code" != "000" ]]; then
    break
  fi
  sleep 1
done

TARGET_DIR="$HOME/docker/tests/active/api"
if [[ -n "$PYTEST_BIN" && -d "$TARGET_DIR" ]] && compgen -G "$TARGET_DIR/test_*.py" > /dev/null; then
  echo "Running API Tests via: $PYTEST_BIN -vv -s $TARGET_DIR"
  "$PYTEST_BIN" -vv -s "$TARGET_DIR"
else
  echo "No API Tests found in $TARGET_DIR — placeholder OK."
  exit 0
fi
