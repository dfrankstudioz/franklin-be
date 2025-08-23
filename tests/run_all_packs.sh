#!/bin/bash
set -u

LOG_DIR="/home/frank/docker/logs"
RUN_PACK="/home/frank/docker/run_pack.sh"
mkdir -p "$LOG_DIR"

STAMP="$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$LOG_DIR/test_output_${STAMP}.log"
echo "[🧪] Starting full test run — $(date)" | tee "$LOG_FILE"

PACKS=(api_pack rag_pack webui_pack system_pack fallback_pack env_pack logs_pack plugins_pack)
EXIT_CODES=()

for PACK in "${PACKS[@]}"; do
  echo -e "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"
  echo "[🔹] Running ${PACK}..." | tee -a "$LOG_FILE"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"

  if [[ -x "$RUN_PACK" ]]; then
    if bash "$RUN_PACK" "$PACK" "$PACK" 2>&1 | tee -a "$LOG_FILE"; then
      echo "[✅] ${PACK} passed." | tee -a "$LOG_FILE"
      EXIT_CODES+=("0")
    else
      echo "[❌] ${PACK} failed." | tee -a "$LOG_FILE"
      EXIT_CODES+=("1")
    fi
  else
    echo "[⛔] run_pack.sh not found at $RUN_PACK — skipping ${PACK}." | tee -a "$LOG_FILE"
    EXIT_CODES+=("1")
  fi
done

echo -e "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" | tee -a "$LOG_FILE"
echo "[📦] All packs finished." | tee -a "$LOG_FILE"

OVERALL="PASS"
for code in "${EXIT_CODES[@]}"; do
  if [[ "$code" != "0" ]]; then
    OVERALL="FAIL"
    break
  fi
done

echo "[🧾] Final status: ${OVERALL}" | tee -a "$LOG_FILE"
echo "Full log saved to: $LOG_FILE"
exit 0
pytest -s ./tests/stress_pack/test_stress_suite.py | tee -a ./logs/run_all_packs_output.log
