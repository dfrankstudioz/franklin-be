#!/bin/bash
set -e

echo "[🌀] Syncing from franklin-dev → franklin-be (Builder’s Edition)"
BE_PATH=~/docker/franklin-be

echo "[📁] Copying clean files..."
mkdir -p "$BE_PATH"
rsync -a ~/docker/franklin-dev/ai_middleware "$BE_PATH/ai_middleware"
rsync -a ~/docker/franklin-dev/web-ui "$BE_PATH/web-ui"
rsync -a ~/docker/franklin-dev/docker-compose "$BE_PATH/docker-compose"

echo "[📁] Copying .pyarmor_runtime..."
mkdir -p "$BE_PATH/ai_middleware/.pyarmor_runtime"
cp -r ~/docker/franklin-dev/ai_middleware/.pyarmor_runtime/* "$BE_PATH/ai_middleware/.pyarmor_runtime/"

echo "[🔐] Verifying encrypted logic..."
if [ ! -f "$BE_PATH/ai_middleware/.pyarmor_runtime/pyarmor_runtime_000000/pyarmor_runtime.so" ]; then
  echo "[❌] Missing pyarmor_runtime.so!"
  exit 1
fi

echo "[✅] Sync complete: Builder’s Edition is ready."
