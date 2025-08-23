import time
from pathlib import Path
from playwright.sync_api import sync_playwright

LOG_PATH = Path("/home/frank/docker/logs/ui_prompt_trace.log")

def dump_static_files(logfile: Path):
    static_paths = {
        "index.html": "/home/frank/docker/web-ui/build/index.html",
        "main.js": "/home/frank/docker/web-ui/build/main.js",
        "main.py": "/home/frank/docker/ai_middleware/main.py",
    }
    with open(logfile, "a") as f:
        for name, path in static_paths.items():
            try:
                f.write(f"\n--- {name} ---\n")
                content = Path(path).read_text()
                f.write(content[:2000] + "\n...\n" if len(content) > 2000 else content)
            except Exception as e:
                f.write(f"[ERROR] Could not read {path}: {e}\n")

def run_test():
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_PATH, "w") as f:
        f.write("")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:9006")
        time.sleep(1)

        # Send a test prompt
        page.fill("#prompt", "list files in /memory")
        page.click("text=Send")
        time.sleep(3)

        html = page.content()
        with open(LOG_PATH, "a") as f:
            f.write("Page HTML:\n" + html + "\n")

        # Console logs
        logs = []
        def on_console(msg):
            logs.append(f"[{msg.type}] {msg.text}")
        page.on("console", on_console)

        time.sleep(1)

        with open(LOG_PATH, "a") as f:
            f.write("\nConsole Logs:\n" + "\n".join(logs) + "\n")

        browser.close()

    dump_static_files(LOG_PATH)

if __name__ == "__main__":
    run_test()
