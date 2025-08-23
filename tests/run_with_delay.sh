#!/bin/bash

if [ -z "$1" ]; then
  echo "❌ No script provided. Usage: ./run_with_delay.sh script.py"
  exit 1
fi

echo "⏳ Waiting for containers to warm up..."
sleep 5
echo "✅ Running: $1"
exec python3 "$@"
