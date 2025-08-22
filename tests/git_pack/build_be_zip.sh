#!/bin/bash

SNAPSHOT_DIR="$HOME/docker/franklin-be"
ZIP_NAME="franklin-be.zip"
ZIP_PATH="$SNAPSHOT_DIR/snapshots/$ZIP_NAME"

mkdir -p "$SNAPSHOT_DIR/snapshots"

echo "[📦] Building ZIP snapshot at: $ZIP_PATH"
cd "$SNAPSHOT_DIR"
zip -r "$ZIP_PATH" ai-middleware web-ui docker-compose README.md .gitignore > /dev/null

if [ -f "$ZIP_PATH" ]; then
  echo "[✅] ZIP created: $ZIP_PATH"
else
  echo "[❌] Failed to create ZIP."
  exit 1
fi
