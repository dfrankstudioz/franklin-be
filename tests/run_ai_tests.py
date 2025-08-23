import subprocess

AI_TESTS = [
    "test_openai_key.py",
    "test_ollama_status.py",
    "test_gpt_relay.py",
    "test_ai_middleware.py",
    "test_file_upload.py",
    "test_rag.py",
    "test_rag_fallback.py",
    "test_model_list.py",
    "test_streaming_response.py",
    "test_version_output.py"
]

print("🧠 Running AI Middleware Functionality Tests...\n")

for test in AI_TESTS:
    print(f"▶️ Running {test}...")
    result = subprocess.run(["python3", test], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"❌ {test} failed.\n")
    else:
        print(f"✅ {test} passed.\n")

print("🧪 All AI tests completed.")