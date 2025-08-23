#!/usr/bin/env python3
import argparse, json, os, subprocess, sys, time
from pathlib import Path

def run_pytest(pytest_bin, repo_root, test_path):
    start = time.time()
    cmd = [pytest_bin, "-vv", "--maxfail=1", "-rA", str(test_path)]
    env = os.environ.copy()
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    proc = subprocess.run(cmd, cwd=str(repo_root), capture_output=True, text=True, env=env)
    duration = time.time() - start
    return proc.returncode, proc.stdout, proc.stderr, duration

def safe_outcome(line):
    known = ("PASSED", "FAILED", "SKIPPED", "ERROR", "XFAIL", "XPASS")
    return next((w for w in known if w in line), None)

def parse_report(stdout):
    results = []
    for line in stdout.splitlines():
        if "::" not in line:
            continue
        parts = line.strip().split()
        if len(parts) < 2:
            continue
        nodeid = parts[0]
        outcome = safe_outcome(line)
        if outcome:
            results.append({"name": nodeid, "outcome": outcome})
    return results

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pytest", required=True)
    ap.add_argument("--root", required=True)
    ap.add_argument("--path", required=True)
    ap.add_argument("--pack", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    repo_root = Path(args.root).resolve()
    test_path = (repo_root / args.path).resolve()
    test_path.mkdir(parents=True, exist_ok=True)

    code, out, err, dur = run_pytest(args.pytest, repo_root, test_path)
    items = parse_report(out)

    summary = {
        "pack": args.pack,
        "path": str(test_path),
        "status": "pass" if code == 0 else "fail",
        "duration_sec": round(dur, 2),
        "num_tests": len(items),
        "results": items,
        "stdout": out[-5000:],
        "stderr": err[-5000:],
        "exit_code": code,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    Path(args.out).write_text(json.dumps(summary, indent=2))
    print(json.dumps({"ok": True, "pack": args.pack, "status": summary["status"], "json": str(args.out)}, indent=2))
    sys.exit(code)

if __name__ == "__main__":
    main()