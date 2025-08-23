import os
from typing import List, Union

def list_dir(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    try:
        return sorted(os.listdir(path))
    except Exception as e:
        return [f"ERROR: {type(e).__name__}: {e}"]

def read_file(path: str) -> str:
    if not os.path.isfile(path):
        return "File not found."
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"

def summarize_file(path: str) -> str:
    content = read_file(path)
    if isinstance(content, str):
        lines = content.strip().split("\n")
        return f"Summary: {len(lines)} lines, {sum(len(l) for l in lines)} characters."
    return "Could not summarize."
