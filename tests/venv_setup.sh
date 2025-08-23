#!/bin/bash
# Setup script for Python virtual environment

echo "📦 Creating virtual environment in ./venv"
python3 -m venv venv

echo "✅ Activating virtual environment"
source venv/bin/activate

echo "⬇️ Installing dependencies from requirements.txt"
pip install -r requirements.txt

echo "🎉 Setup complete. Run tests with: source venv/bin/activate && python run_tests.py"
