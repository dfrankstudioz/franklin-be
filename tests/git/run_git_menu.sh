    #!/bin/bash
    set -euo pipefail

    # Project root (two levels up from tests/git/)
    ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../" && pwd)"
    cd "$ROOT_DIR"

    SNAPSHOT_SCRIPT="$ROOT_DIR/tests/git/run_git_snapshot.sh"

    ensure_git() {
      if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        echo "[❌] Not a Git repository: $ROOT_DIR"
        read -p "Press enter to return..." _
        exit 1
      fi
    }

    latest_snapshot_tag() {
      git tag --list 'snapshot_*' --sort=-creatordate | head -n1
    }

    do_snapshot() {
      bash "$SNAPSHOT_SCRIPT"
      read -p "Press enter to return to Git menu..." _
    }

    do_status() {
      ensure_git
      echo "────────── git status ──────────"
      git status
      echo "────────────────────────────────"
      read -p "Press enter to return..." _
    }

    do_log() {
      ensure_git
      echo "────────── latest commits ──────────"
      git --no-pager log --oneline -n 5
      echo "────────────────────────────────────"
      read -p "Press enter to return..." _
    }

    do_diff() {
      ensure_git
      echo "────────── unstaged diff ──────────"
      git --no-pager diff
      echo "───────────────────────────────────"
      read -p "Press enter to return..." _
    }

    do_soft_rollback() {
      ensure_git
      local TAG
      TAG="$(latest_snapshot_tag)"
      if [[ -z "$TAG" ]]; then
        echo "[⚠️] No snapshot_* tags found."
        read -p "Press enter to return..." _
        return
      fi
      local COMMIT
      COMMIT="$(git rev-parse -q --verify "${TAG}^{commit}")"
      if [[ -z "$COMMIT" ]]; then
        echo "[❌] Could not resolve commit for tag: $TAG"
        read -p "Press enter to return..." _
        return
      fi
      echo "[⏪] Soft resetting to ${TAG} (${COMMIT}) — keeping changes staged."
      git reset --soft "$COMMIT"
      echo "[✅] Done. (HEAD moved, changes kept)"
      read -p "Press enter to return..." _
    }

    do_hard_rollback() {
      ensure_git
      local TAG
      TAG="$(latest_snapshot_tag)"
      if [[ -z "$TAG" ]]; then
        echo "[⚠️] No snapshot_* tags found."
        read -p "Press enter to return..." _
        return
      fi
      local COMMIT
      COMMIT="$(git rev-parse -q --verify "${TAG}^{commit}")"
      if [[ -z "$COMMIT" ]]; then
        echo "[❌] Could not resolve commit for tag: $TAG"
        read -p "Press enter to return..." _
        return
      fi
      echo "[🔥] HARD RESET to ${TAG} (${COMMIT}) — this will discard uncommitted changes."
      read -p "Type 'YES' to confirm: " CONFIRM
      if [[ "$CONFIRM" == "YES" ]]; then
        git reset --hard "$COMMIT"
        echo "[✅] Hard reset complete."
      else
        echo "[ℹ️] Aborted."
      fi
      read -p "Press enter to return..." _
    }

    while true; do
      clear
      cat <<'MENU'
────────── Git Tools Menu ──────────
1) Snapshot (commit + tag)
2) Status
3) Log (last 5)
4) Diff (unstaged)
5) Rollback to latest snapshot (soft)
6) Rollback to latest snapshot (hard)  ⚠️ destructive
q) Back to Main Menu
MENU
      read -p "Choose: " CHOICE
      case "$CHOICE" in
        1) do_snapshot ;;
        2) do_status ;;
        3) do_log ;;
        4) do_diff ;;
        5) do_soft_rollback ;;
        6) do_hard_rollback ;;
        q|Q) exit 0 ;;
        *) echo "Invalid choice."; sleep 0.7 ;;
      esac
    done
