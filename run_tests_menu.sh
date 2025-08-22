#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
PACKS=~/docker/franklin-dev/tests

while true; do
  clear
  echo "Franklin Test Suite (builders-2025.08.21)"
  echo "------------------------------------"
  echo "[ Test Mode: Minimal BE Tests ]"
  echo ""
  echo "1) API Smoke Test"
  echo "2) Web UI Build Check"
  echo "3) Snapshot Validation"
  echo "q) Quit"
  echo ""
  read -p "Choose: " choice

  case "$choice" in
    1)
      echo "[🔧] Running API Smoke Test..."
      pytest -v "$PACKS/api_pack/test_api_smoke.py"
      read -p "Press Enter to return to the menu..."
      ;;
    2)
      echo "[🔧] Running Web UI Build Check..."
      pytest -v "$PACKS/web_ui_pack/test_web_ui_build.py"
      read -p "Press Enter to return to the menu..."
      ;;
    3)
      echo "[🔧] Running Snapshot Validation..."
      pytest -v "$PACKS/git_pack/test_be_snapshot_validation.py"
      read -p "Press Enter to return to the menu..."
      ;;
    q|Q)
      echo "Exiting..."
      break
      ;;
    *)
      echo "Invalid choice. Press Enter to try again."
      read
      ;;
  esac
done
