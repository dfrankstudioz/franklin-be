import re
from ai_middleware.tools import list_dir, read_file, summarize_file

def improve_prompt_context(prompt: str):
    if not prompt or not prompt.strip():
        return "Empty prompt provided."

    prompt_lower = prompt.lower()

    # List files in memory
    if "list" in prompt_lower and "/memory" in prompt_lower:
        return list_dir("/memory")

    # Read file
    if "read" in prompt_lower or "show contents" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt)
        if match:
            filename = match.group(1)
            return read_file(f"/memory/{filename}")
        return "Please specify a valid filename to read."

    # Summarize file
    if "summarize" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt)
        if match:
            filename = match.group(1)
            return summarize_file(f"/memory/{filename}")
        return "Please specify a valid filename to summarize."

    # Fallback
    return "Sorry, I couldn't understand the prompt."
