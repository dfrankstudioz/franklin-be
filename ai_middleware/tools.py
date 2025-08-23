import os
from typing import List, Union

def list_dir(path: str) -> List[str]:
    if not os.path.exists(path):
        return []
    try:
        return sorted(os.listdir(path))
    except Exception as e:
        return [f"ERROR: {type(e).__name__}: {e}"]

def read_file(path: str, max_bytes: int = 200_000) -> Union[str, list]:
    try:
        if not os.path.exists(path):
            return f"ERROR: File not found: {path}"
        if os.path.isdir(path):
            return f"ERROR: Path is a directory: {path}"
        if os.path.getsize(path) > max_bytes:
            return f"ERROR: File too large."
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            return f.read()
    except Exception as e:
        return f"ERROR: {type(e).__name__}: {e}"

def summarize_file(path: str, max_bytes: int = 200_000) -> str:
    content = read_file(path, max_bytes=max_bytes)
    if isinstance(content, str) and content.startswith("ERROR:"):
        return content
    if not isinstance(content, str):
        return "ERROR: Unexpected content type"
    lines = content.splitlines()
    head = "\n".join(lines[:20])
    return f"Summary: {len(lines)} lines, {len(content)} chars\nFirst 20 lines:\n{head}"