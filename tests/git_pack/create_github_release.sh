#!/bin/bash
# ~/docker/franklin-be/tests/git_pack/create_github_release.sh

set -e

TAG="v2025.08.22"
ZIP="franklin-be-${TAG}.zip"
NOTES_FILE="RELEASE_NOTES.md"

cd ~/docker/franklin-be

if [ ! -f "$ZIP" ]; then
  echo "❌ $ZIP not found, build it first with your snapshot step."
  exit 1
fi

if [ ! -f "$NOTES_FILE" ]; then
  echo "❌ $NOTES_FILE missing."
  exit 1
fi

echo "🚀 Creating GitHub Release: Franklin Builder’s Edition $TAG"

gh release create "$TAG" "$ZIP" \
  --title "Franklin Builder’s Edition $TAG" \
  --notes-file "$NOTES_FILE"
