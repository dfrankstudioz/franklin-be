#!/bin/bash
echo "[📦] Preparing Franklin v1.0 release package..."

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BE_ROOT="$SCRIPT_DIR/../../franklin-be"
V1_ROOT="$SCRIPT_DIR/../../franklin-v1.0"
RELEASE_TAG="v1.0_$(date +%Y%m%d_%H%M%S)"

# Clean and create folder
rm -rf "$V1_ROOT"
mkdir -p "$V1_ROOT"

# Copy everything from Builder’s Edition
rsync -av --exclude='.git' "$BE_ROOT/" "$V1_ROOT/"

# Add version file and metadata
echo "$RELEASE_TAG" > "$V1_ROOT/VERSION.txt"
date > "$V1_ROOT/BUILD_TIMESTAMP.txt"

# Optional: run verify check
echo "[🔍] Re-validating release build..."
bash "$SCRIPT_DIR/verify_git_clean.sh" "$V1_ROOT" || echo "[⚠️] Warning: Post-build check has warnings."

# Create zip
cd "$V1_ROOT/.."
zip -r "franklin-v1.0_$RELEASE_TAG.zip" franklin-v1.0

echo "[✅] Release package ready: franklin-v1.0_$RELEASE_TAG.zip"
