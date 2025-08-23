import os
import subprocess
from datetime import datetime

def main():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir = os.path.join(os.path.dirname(__file__), "../test_logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"test_output_{timestamp}.txt")

    print(f"🔍 Running ALL tests... Log: {log_file}")

    with open(log_file, "w") as f:
        subprocess.run(["pytest", "-v"], stdout=f, stderr=subprocess.STDOUT)

    print("✅ Tests complete. Log saved.")

if __name__ == "__main__":
    main()