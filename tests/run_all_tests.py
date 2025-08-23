#!/usr/bin/env python3
import subprocess
import os
from datetime import datetime

def find_tests(base_dir):
    for root, _, files in os.walk(base_dir):
        if 'archive' in root or 'venv' in root or '__pycache__' in root:
            continue
        for file in files:
            if file.endswith(".py"):
                yield os.path.join(root, file)

def main():
    script_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(script_path)
    base_dir = os.path.join(script_dir, 'tests', 'active')
    print(f"📂 Scanning test files in: {base_dir}")

    log_dir = os.path.expanduser("~/docker/logs")
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("test_output_%Y-%m-%d_%H-%M-%S.log")
    log_file = os.path.join(log_dir, timestamp)

    with open(log_file, "w") as log:
        for test_file in find_tests(base_dir):
            print(f"🔍 Running: {test_file}")
            log.write(f"🔍 Running: {test_file}\n")
            try:
                result = subprocess.run(
                    ["python3", test_file],
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                print(result.stdout)
                log.write(result.stdout + "\n")
                print(f"{'✅' if result.returncode == 0 else '❌'} Exit code: {result.returncode}\n")
                log.write(f"Exit code: {result.returncode}\n")
            except Exception as e:
                print(f"❌ Exception while running {test_file}: {e}")
                log.write(f"❌ Exception while running {test_file}: {e}\n")
            log.write("="*80 + "\n")

    print(f"📄 All logs saved to: {log_file}")

if __name__ == "__main__":
    main()
