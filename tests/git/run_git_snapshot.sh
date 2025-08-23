#!/bin/bash
set -euo pipefail

# Ensure we're in the project root (the directory that contains .git)
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../" && pwd)"
cd "$ROOT_DIR"

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "[❌] Not a Git repository: $ROOT_DIR"
  exit 1
fi

STAMP="$(date +%Y%m%d_%H%M%S)"
TAG="snapshot_rag_green_${STAMP}"
MESSAGE="🟢 Snapshot: Franklin snapshot on ${STAMP}"

echo "[+] Staging changes..."
git add -A

echo "[+] Committing..."
if git commit -m "${MESSAGE}" >/dev/null 2>&1; then
  echo "[✅] Commit created."
else
  echo "[ℹ️] Nothing to commit — working tree clean."
fi

echo "[+] Tagging as ${TAG}"
if git tag "${TAG}" 2>/dev/null; then
  echo "[✅] Git snapshot completed and tagged successfully: ${TAG}"
  exit 0
else
  echo "[⚠️] Tag already exists — skipping tag creation."
  exit 0
fi
