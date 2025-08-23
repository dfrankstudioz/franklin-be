#!/bin/bash
echo "[🧹] Cleaning Builder's Edition snapshot..."

# Remove secrets
rm -f ~/docker/franklin-be/docker-compose/.env

# Remove all pycache/log/test files
find ~/docker/franklin-be -type d -name "__pycache__" -exec rm -rf {} +
find ~/docker/franklin-be -type d -name ".pytest_cache" -exec rm -rf {} +
find ~/docker/franklin-be -type f -name "*.log" -exec rm -f {} +
find ~/docker/franklin-be -type f -name "*.bak" -exec rm -f {} +

echo "[✅] Snapshot cleaned."
