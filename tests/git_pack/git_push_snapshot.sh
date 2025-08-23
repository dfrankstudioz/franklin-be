#!/bin/bash
set -euo pipefail

REPO=~/docker/franklin-be
cd "$REPO"

TAG="v2025.08.22"
ZIP="franklin-be-${TAG}.zip"

if [ ! -f "$ZIP" ]; then
  echo "[❌] ZIP not found: $ZIP"
  exit 1
fi

echo "[⬆️] Uploading asset to GitHub release $TAG..."
gh release upload "$TAG" "$ZIP" --clobber
echo "[✅] Done."
