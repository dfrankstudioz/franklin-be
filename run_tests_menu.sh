#!/bin/bash

PACKS="$HOME/docker/franklin-be/tests"

while true; do
  clear
  echo "Franklin Test Suite (builders-2025.08.21)"
  echo "------------------------------------"
  echo "[ Test Mode: Minimal BE Tests ]"
  echo
  echo "1) API Smoke Test"
  echo "2) Web UI Build Check"
  echo "3) Snapshot Validation"
  echo "4) 📦 Build ZIP Snapshot"
  echo "5) Validate Builder’s Edition ZIP file"
  echo "6) Push Builder’s Edition to GitHub"
  echo "7) 🚀 Finalize and Push Builder’s Edition (Full Pipeline)"
  echo "q) Quit"
  echo
  read -p "Choose: " choice

  case "$choice" in
      1) pytest "$PACKS/api_pack/test_api_smoke.py" ;;
      2) pytest "$PACKS/web_ui_pack/test_web_build_exists.py" ;;
      3) pytest "$PACKS/git_pack/test_be_snapshot_validation.py" ;;
      4) bash "$PACKS/git_pack/build_be_zip.sh" ;;
      5) pytest "$PACKS/git_pack/test_zip_snapshot.py" ;;
      6) bash "$PACKS/git_pack/git_push_snapshot.sh" ;;
      7)
          echo "[🔍] Running API Smoke Test..."
          pytest "$PACKS/api_pack/test_api_smoke.py" || break
          echo "[🌐] Checking Web UI Build..."
          pytest "$PACKS/web_ui_pack/test_web_build_exists.py" || break
          echo "[📦] Validating Snapshot Files..."
          pytest "$PACKS/git_pack/test_be_snapshot_validation.py" || break
          echo "[🛠] Building ZIP Snapshot..."
          bash "$PACKS/git_pack/build_be_zip.sh" || break
          echo "[🧪] Validating ZIP..."
          pytest "$PACKS/git_pack/test_zip_snapshot.py" || break
          echo "[⬆️] Pushing to GitHub..."
          bash "$PACKS/git_pack/git_push_snapshot.sh"
          ;;
      q) echo "Exiting..." ; exit 0 ;;
      *) echo "Invalid option." ;;
  esac

  echo
  read -p "Press Enter to return to the menu..."
done
