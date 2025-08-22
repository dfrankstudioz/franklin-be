#!/bin/bash

SNAPSHOT_DIR="$HOME/docker/franklin-be"
cd "$SNAPSHOT_DIR"

# Tag version from zip builder
TAG=$(cat "$SNAPSHOT_DIR/snapshots/.last_version" 2>/dev/null)

echo "[⬆️] Committing and pushing to GitHub..."
git init
git add .
git commit -m "Push Builder’s Edition snapshot"
git remote add origin git@github.com:dfrankstudioz/franklin-be.git 2>/dev/null
git push -u origin main

# Auto-tag if version found
if [[ "$TAG" == v* ]]; then
  echo "[🏷️] Tagging release as $TAG..."
  git tag -a "$TAG" -m "Builder’s Edition $TAG"
  git push origin "$TAG"
else
  echo "[⚠️] No tag version found. Skipping tagging."
fi
