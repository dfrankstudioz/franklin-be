#!/bin/bash
set -euo pipefail
PACK_ROOT="$HOME/docker/tests/webui_pack"
echo "[+] Running webui_pack tests..."
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -vv -s "$PACK_ROOT" \
  --json-report \
  --json-report-file="$HOME/docker/logs/test_results_$(date +%Y%m%d_%H%M%S).json"
