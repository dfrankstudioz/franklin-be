#!/bin/bash
PACK_NAME="rag_deep_pack"
PACK_DIR="$(dirname "$0")/tests"
LOGS=~/docker/logs
mkdir -p "$LOGS"
TS=$(date +%Y%m%d_%H%M%S)
OUT="$LOGS/test_output_${PACK_NAME}_$TS.log"

echo "[+] Running $PACK_NAME tests..." | tee "$OUT"
pytest -vv "$PACK_DIR" 2>&1 | tee -a "$OUT"
