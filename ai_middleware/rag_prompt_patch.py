import os
import re

def list_dir(path: str):
    try:
        return os.listdir(path)
    except Exception as e:
        return [f"Error: {str(e)}"]

def read_file(path: str):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        return f"Error: {str(e)}"

def summarize_file(path: str):
    # Basic placeholder summary
    content = read_file(path)
    if isinstance(content, str):
        lines = content.strip().splitlines()
        return f"Summary: {len(lines)} lines, {len(content)} characters"
    return content

def improve_prompt_context(prompt: str):
    prompt_lower = prompt.lower()

    # List directory
    if "list" in prompt_lower and "/memory" in prompt_lower:
        return list_dir("/memory")

    # Read file
    if "read" in prompt_lower or "show contents" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.(txt|md|log))', prompt)
        if match:
            filename = match.group(1)
            return read_file(f"/memory/{filename}")

    # Summarize file
    if "summarize" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.(txt|md|log))', prompt)
        if match:
            filename = match.group(1)
            return summarize_file(f"/memory/{filename}")

    return "Sorry, I couldn't understand the prompt."
