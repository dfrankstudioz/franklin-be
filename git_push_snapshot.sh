#!/bin/bash
set -e

# --- Config ---
TAG="v2.0.0-be"
MSG="📦 Final Builder’s Edition $TAG snapshot"
DIR="$(dirname "$(realpath "$0")")"

cd "$DIR"

echo "[🚀] Committing and tagging Builder’s Edition ($TAG)..."
git add .
git commit -m "$MSG" || echo "[ℹ️] Nothing to commit — working tree clean."
git tag "$TAG" || echo "[ℹ️] Tag $TAG already exists."
git push origin main --tags

echo "[✅] Git push complete for Builder’s Edition ($TAG)."
