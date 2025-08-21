import os
import logging
from openai import OpenAI


try:
    from secret_logic import secret_summary
except ImportError:
    def secret_summary(*args, **kwargs):
        raise NotImplementedError("secret_summary() is only available in the private edition.")

logging.basicConfig(level=logging.INFO)

client = None
try:
    client = OpenAI()
except Exception:
    logging.warning("OpenAI client could not be initialized.")

def list_dir(path: str) -> str:
    try:
        entries = os.listdir(path)
        lines = []
        for entry in entries:
            full_path = os.path.join(path, entry)
            if os.path.isdir(full_path):
                lines.append(f"{entry}/ (folder)")
            else:
                try:
                    size = os.path.getsize(full_path)
                    lines.append(f"{entry} ({size} bytes)")
                except Exception as e:
                    lines.append(f"{entry} (error: {str(e)})")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {str(e)}"

def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
            return content if len(content) < 4000 else content[:4000] + "\n... [truncated]"
    except Exception as e:
        return f"Error reading file: {str(e)}"

def summarize_file(path: str) -> str:
    try:
        content = read_file(path)
        if "Error" in content:
            return content
        if not client:
            return "[Fallback] Summary unavailable (OpenAI not configured)."
        messages = [
            {"role": "system", "content": "Summarize the following file for a human reader."},
            {"role": "user", "content": content}
        ]
        result = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.3,
        )
        return result.choices[0].message.content.strip()
    except Exception as e:
        return f"Unable to summarize: {str(e)}"

def fallback_chat_response(prompt: str) -> str:
    if not client:
        return "[FALLBACK] No GPT-4o client available."
    messages = [
        {"role": "system", "content": "You are Franklin, a helpful and friendly AI assistant."},
        {"role": "user", "content": prompt}
    ]
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0.7,
        )
        reply = completion.choices[0].message.content.strip()
        logging.info("[GPT-4o fallback] → %s", reply)
        return reply
    except Exception as e:
        return f"[FALLBACK ERROR] {str(e)}"

def improve_prompt_context(prompt: str) -> str:
    if not client:
        return "Invalid command"
    messages = [
        {"role": "system", "content": "You are a prompt router. Given a natural language prompt, respond ONLY with the correct Python function call: list_dir(path), read_file(path), or summarize_file(path). If no function fits, say 'none'."},
        {"role": "user", "content": prompt}
    ]
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            temperature=0,
        )
        parsed = completion.choices[0].message.content.strip()
        logging.info("[GPT-4o interpretation] → %s", parsed)
        return parsed
    except Exception as e:
        logging.error("Error contacting OpenAI: %s", str(e))
        return "none"

def normalize_path_command(cmd: str) -> str:
    try:
        for tool in ["list_dir", "read_file", "summarize_file"]:
            if cmd.startswith(f"{tool}("):
                parts = cmd[len(tool) + 1:-1].strip()
                if parts == "path":
                    if tool == "list_dir":
                        return f'{tool}("/memory")'
                    elif tool == "read_file":
                        return f'{tool}("/memory/example.txt")'
                    elif tool == "summarize_file":
                        return f'{tool}("/memory/memory.txt")'
                if parts.startswith('"') and parts.endswith('"'):
                    inner = parts.strip('"')
                    if not inner.startswith("/"):
                        inner = f"/memory/{inner}"
                    return f'{tool}("{inner}")'
    except Exception as e:
        logging.warning("Failed to normalize path: %s", str(e))
    return cmd

def chat(prompt: str) -> str:
    prompt = prompt.strip()

    # Direct command call
    if prompt.startswith(("list_dir(", "read_file(", "summarize_file(")):
        try:
            safe_prompt = normalize_path_command(prompt)
            return eval(safe_prompt)
        except Exception as e:
            return f"Invalid command: {str(e)}"

    # Ask GPT to improve the prompt
    improved = improve_prompt_context(prompt)

    # If GPT returns a tool command, run it
    if improved.startswith(("list_dir(", "read_file(", "summarize_file(")):
        try:
            safe_prompt = normalize_path_command(improved)
            return eval(safe_prompt)
        except Exception as e:
            return f"Invalid command: {str(e)}"

    # Otherwise, fallback to chat
    return fallback_chat_response(prompt)