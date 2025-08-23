#!/bin/bash
set -e

BE_PATH="$HOME/docker/franklin-be"
cd "$BE_PATH"

echo "[🔄] Initializing clean Git repo in Builder’s Edition..."

rm -rf .git
git init
git remote add origin git@github.com:dfrankstudioz/franklin-be.git

git add .
git commit -m "Builder’s Edition Snapshot $(date +%Y-%m-%d_%H%M)"
git tag v1.0.0-be
git push -f origin master
git push origin v1.0.0-be

echo "[✅] Public snapshot pushed to GitHub."
