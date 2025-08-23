#!/bin/bash

LOG_FILE="$1"
SUMMARY_FILE="$2"

if [[ ! -f "$LOG_FILE" ]]; then
  echo "Missing log file: $LOG_FILE"
  exit 1
fi

TOTAL=$(grep -c "^🧪 Running" "$LOG_FILE")
PASSED=$(grep -c "^✅ " "$LOG_FILE")
FAILED=$(grep -c "^❌ " "$LOG_FILE")

{
  echo "=== Test Summary ==="
  echo "Total tests: $TOTAL"
  echo "Passed:      $PASSED"
  echo "Failed:      $FAILED"
  echo ""
  echo "Failed Tests:"
  grep "^❌ " "$LOG_FILE"
} > "$SUMMARY_FILE"

echo "📄 Summary written to: $SUMMARY_FILE"
