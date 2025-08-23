#!/bin/bash
set -euo pipefail

REPO=~/docker/franklin-be
cd "$REPO"

TAG="v2025.08.22"
ZIP="franklin-be-${TAG}.zip"

echo "[📦] Building versioned ZIP: $ZIP"
rm -f "$ZIP"
zip -r "$ZIP"   ai_middleware   web-ui/dist   docker-compose   README.md INSTALL.md CONTRIBUTING.md LICENSE.md RELEASE_NOTES.md VERSION .gitignore

echo "[✅] ZIP created: ${REPO}/${ZIP}"
