
import os
from datetime import datetime
from pathlib import Path
import shutil

def mask_env_file(src, dest):
    with open(src) as f_in, open(dest, "w") as f_out:
        for line in f_in:
            if line.startswith("OPENAI_API_KEY"):
                f_out.write("OPENAI_API_KEY=***MASKED***\n")
            else:
                f_out.write(line)

def export_diagnostic_snapshot():
    base_dir = Path.home() / "docker"
    diagnostics_root = base_dir / "logs" / "diagnostics"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    snapshot_dir = diagnostics_root / timestamp
    os.makedirs(snapshot_dir, exist_ok=True)

    files_to_snapshot = {
        "docker-compose.yml": base_dir / "docker-compose.yml",
        "main.py": base_dir / "ai_middleware" / "main.py",
        "rag_analyzer.py": base_dir / "ai_middleware" / "rag_analyzer.py",
        ".env": base_dir / ".env"
    }

    for name, path in files_to_snapshot.items():
        dest_path = snapshot_dir / name
        if path.exists():
            if name == ".env":
                mask_env_file(path, dest_path)
            else:
                shutil.copy2(path, dest_path)

    with open(snapshot_dir / "folder_tree.txt", "w") as f:
        os.system(f"tree {base_dir} > {f.name}")

    with open(snapshot_dir / "memory_dir.txt", "w") as f:
        os.system(f"ls -lh {base_dir / 'memory'} > {f.name}")

    with open(snapshot_dir / "logs_dir.txt", "w") as f:
        os.system(f"ls -lh {base_dir / 'logs'} > {f.name}")

    print(f"📦 Diagnostic snapshot exported to: {snapshot_dir}")
