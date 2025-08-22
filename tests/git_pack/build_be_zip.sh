#!/bin/bash

SNAPSHOT_DIR="$HOME/docker/franklin-be"
DATE_TAG=$(date +v%Y.%m.%d)
ZIP_NAME="franklin-be-${DATE_TAG}.zip"
ZIP_PATH="$SNAPSHOT_DIR/snapshots/$ZIP_NAME"

mkdir -p "$SNAPSHOT_DIR/snapshots"

echo "[📦] Building versioned ZIP: $ZIP_NAME"
cd "$SNAPSHOT_DIR"
zip -r "$ZIP_PATH" ai-middleware web-ui docker-compose README.md .gitignore > /dev/null

if [ -f "$ZIP_PATH" ]; then
  echo "[✅] ZIP created: $ZIP_PATH"
  echo "$DATE_TAG" > "$SNAPSHOT_DIR/snapshots/.last_version"
else
  echo "[❌] Failed to create ZIP."
  exit 1
fi
