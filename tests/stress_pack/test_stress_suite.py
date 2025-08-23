import pytest
import subprocess
import time
import requests

BASE_URL = "http://localhost:9006/chat"
HEADERS = {"Content-Type": "application/json"}

def send_prompt(prompt):
    return requests.post(BASE_URL, headers=HEADERS, json={"prompt": prompt})

def test_rag_loop():
    for i in range(100):
        response = send_prompt('read_file("/memory/example.txt")')
        assert response.status_code == 200
        time.sleep(0.05)  # light pause to prevent thrashing

def test_concurrent_requests():
    import threading
    responses = []

    def worker(prompt):
        res = send_prompt(prompt)
        responses.append(res)

    prompts = [
        'read_file("/memory/example.txt")',
        "who are you?"
    ] * 5  # 10 total

    threads = [threading.Thread(target=worker, args=(p,)) for p in prompts]

    for t in threads: t.start()
    for t in threads: t.join()

    assert all(r.status_code == 200 for r in responses)

def test_nonsense_prompts():
    for i in range(20):
        response = send_prompt(f"what does 🐙🌋💣 mean {i}?")
        assert response.status_code == 200
        time.sleep(0.05)

def test_log_and_stats_capture():
    subprocess.run("docker stats --no-stream > /home/frank/docker/logs/stress_docker_stats.txt", shell=True)
    subprocess.run("docker compose logs ai_middleware --tail=100 > /home/frank/docker/logs/stress_tail_logs.txt", shell=True)
