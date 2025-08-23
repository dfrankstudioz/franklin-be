import re
from tools import list_dir, read_file, summarize_file

def improve_prompt_context(prompt: str):
    p = (prompt or "").lower().strip()

    if any(k in p for k in ["what files", "show files", "list"]) and "/memory" in p:
        return list_dir("/memory")

    if any(k in p for k in ["read", "show contents", "open"]) or ".txt" in p:
        m = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt or "")
        if m:
            return read_file(f"/memory/{m.group(1)}")

    if "summarize" in p or "summary" in p:
        m = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt or "")
        if m:
            return summarize_file(f"/memory/{m.group(1)}")

    return "Sorry, I couldn't understand the request."