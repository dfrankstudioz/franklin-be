#!/bin/bash
set -euo pipefail

# Auto-detect base directory of Franklin BE
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PACK_DIR="${1}"
PACK_NAME="${2:-$(basename "$PACK_DIR")}"

LOGS="$SCRIPT_DIR/../logs"
mkdir -p "$LOGS"

TS=$(date +%Y%m%d_%H%M%S)
OUT="$LOGS/test_output_${PACK_NAME}_$TS.log"

echo "[+] Running $PACK_NAME tests..." | tee "$OUT"

pytest -s -q "$PACK_DIR" | tee -a "$OUT"

echo
echo "--------------------------------------------------------------------------------"
echo "[✔] Completed $PACK_NAME tests. Log saved at: $OUT"
echo "Press ENTER to return to the menu."
echo "--------------------------------------------------------------------------------"
read -r
