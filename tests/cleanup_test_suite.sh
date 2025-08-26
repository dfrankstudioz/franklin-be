#!/bin/bash
# clean_test_suite.sh
# Franklin Test Suite Cleanup Script (v1.0)

TEST_DIR="$(dirname "$0")"
ARCHIVE_DIR="$TEST_DIR/archive"
LOG_FILE="$TEST_DIR/cleanup_log.txt"

mkdir -p "$ARCHIVE_DIR"
echo "[+] Franklin Test Suite Cleanup Log - $(date)" > "$LOG_FILE"

echo "[+] Archiving placeholder and dev-only tests..." | tee -a "$LOG_FILE"

# Move test files with 'placeholder' in name
find "$TEST_DIR" -type f -name '*placeholder*.py' -exec mv {} "$ARCHIVE_DIR/" \; -exec echo "Archived: {}" >> "$LOG_FILE" \;

# Move legacy or inactive tests
for file in \
  test_rag_tools_only_in_dev.py \
  test_summarize_file_additional.py \
  test_ui_rag_flow_root.py \
  test_rag.txt test_summary.txt test_preflight.sh
  do
  if [ -f "$TEST_DIR/$file" ]; then
    mv "$TEST_DIR/$file" "$ARCHIVE_DIR/"
    echo "Archived: $file" >> "$LOG_FILE"
  fi
done

# Delete backup .bak files and compiled .pyc
echo "[+] Deleting .bak and __pycache__ files..." | tee -a "$LOG_FILE"
find "$TEST_DIR" -type f -name '*.bak_*' -delete -print >> "$LOG_FILE"
find "$TEST_DIR" -type d -name '__pycache__' -exec rm -rf {} + -exec echo "Deleted: {}" >> "$LOG_FILE" \;
find "$TEST_DIR" -type d -name '.pytest_cache' -exec rm -rf {} + -exec echo "Deleted: {}" >> "$LOG_FILE" \;

# Optionally remove .txt test output
find "$TEST_DIR" -type f -name '*.txt' -exec rm -f {} \; -exec echo "Deleted test log: {}" >> "$LOG_FILE" \;

# Optional: Clean up old shell scripts in menu
find "$TEST_DIR/menu" -type f -name '*.bak_*' -delete -print >> "$LOG_FILE"

# Summary
TOTAL_ARCHIVED=$(ls "$ARCHIVE_DIR" | wc -l)
echo "[+] Archived $TOTAL_ARCHIVED files to $ARCHIVE_DIR" | tee -a "$LOG_FILE"
echo "[+] Cleanup complete. Log saved to $LOG_FILE" | tee -a "$LOG_FILE"
