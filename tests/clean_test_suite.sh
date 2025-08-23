#!/bin/bash

echo "🧹 Cleaning ~/docker/tests for clean suite install..."

cd ~/docker/tests || exit 1

# Remove old test_*.py files from root
echo "➤ Removing root-level test_*.py files..."
find . -maxdepth 1 -name "test_*.py" -exec rm {} \;

# Remove venv, __pycache__, and lib*/ folders
echo "➤ Removing venv/, __pycache__/, lib*/..."
rm -rf venv __pycache__ lib lib64

# Remove old run_all_tests.py if it exists
echo "➤ Removing old run_all_tests.py..."
rm -f run_all_tests.py

# Move legacy skipped files to archive
mkdir -p archive
for file in test_web_ui_build.py test_middleware.py test_status_endpoint.py test_ai_middleware_expanded.py; do
  if [ -f "$file" ]; then
    echo "➤ Archiving $file..."
    mv "$file" archive/
  fi
done

echo "✅ Done. You're ready to extract the new categorized suite."
