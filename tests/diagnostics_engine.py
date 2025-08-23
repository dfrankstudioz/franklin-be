import re
import sys
import json
from pathlib import Path

def parse_log(log_path):
    with open(log_path, "r") as f:
        log_contents = f.read()

    issues = []

    patterns = [
        {
            "key": "fastapi",
            "pattern": r"FastAPI.*Connection.*(refused|reset)",
            "message": "🚫 FastAPI unreachable — check if it's running and listening on port 9006. Try `docker logs ai_middleware --tail=100`.",
            "status": "fail"
        },
        {
            "key": "chat",
            "pattern": r"/chat endpoint unreachable",
            "message": "⚠️ /chat API failed — FastAPI may have crashed or not fully started.",
            "status": "fail"
        },
        {
            "key": "env",
            "pattern": r".env found but missing OPENAI_API_KEY",
            "message": "🔐 .env file exists but is missing `OPENAI_API_KEY`. Add it to enable OpenAI access.",
            "status": "warn"
        },
        {
            "key": "env",
            "pattern": r".env file missing",
            "message": "📄 Missing .env file: Make sure it exists at /home/frank/docker/ai_middleware/.env.",
            "status": "fail"
        },
    ]

    report = {
        "timestamp": log_path.name.replace("test_output_", "").replace(".log", ""),
        "overall": "pass"
    }

    markdown_lines = ["# 🧠 Franklin Diagnostics Report\n"]

    for entry in patterns:
        if re.search(entry["pattern"], log_contents, re.IGNORECASE):
            issues.append(entry)
            report[entry["key"]] = entry["status"]
            markdown_lines.append(entry["message"] + "\n")
            if entry["status"] == "fail":
                report["overall"] = "fail"

    if not issues:
        markdown_lines.append("✅ No issues detected by diagnostics engine.\n")

    return markdown_lines, report

def main():
    if len(sys.argv) < 3:
        print("Usage: python diagnostics_engine.py <log_file> <report_path>")
        sys.exit(1)

    log_file = Path(sys.argv[1])
    report_base = Path(sys.argv[2]).with_suffix("")

    markdown_lines, report_data = parse_log(log_file)

    # Save Markdown
    with open(f"{report_base}.md", "w") as md_file:
        md_file.write("\n".join(markdown_lines))

    # Save JSON
    with open(f"{report_base}.json", "w") as json_file:
        json.dump(report_data, json_file, indent=2)

    print("\n".join(markdown_lines))

    if report_data["overall"] == "fail":
        sys.exit(1)  # non-zero exit for FAIL
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
