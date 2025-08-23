import re
from tools import list_dir, read_file, summarize_file

def improve_prompt_context(prompt: str):
    prompt_lower = prompt.lower()

    # Match natural prompts for listing directory
    if any(keyword in prompt_lower for keyword in [
        "what’s in", "what is in", "what files", "show files", 
        "inside the /memory", "list /memory", "contents of /memory"
    ]):
        return list_dir("/memory")

    # Read specific file
    if "read" in prompt_lower or "show contents" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt)
        if match:
            filename = match.group(1)
            return read_file(f"/memory/{filename}")

    # Summarize file
    if "summarize" in prompt_lower:
        match = re.search(r'([a-zA-Z0-9_\-]+\.txt)', prompt)
        if match:
            filename = match.group(1)
            return summarize_file(f"/memory/{filename}")

    return "Sorry, I couldn't understand the prompt."
