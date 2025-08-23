
#!/usr/bin/env bash
set -euo pipefail

PREFLIGHT="$HOME/docker/preflight/run_preflight.sh"
LOG_DIR="$HOME/docker/logs"
mkdir -p "$LOG_DIR"

if [[ ! -x "$PREFLIGHT" ]]; then
  echo "[x] Pre-Flight script not found or not executable: $PREFLIGHT"
  echo "    Please unzip the original preflight bundle and run: chmod +x ~/docker/preflight/run_preflight.sh"
  exit 2
fi

"$PREFLIGHT" "$@"
