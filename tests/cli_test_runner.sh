#!/bin/bash

STACK_VERSION="v4.4"
STACK_DIR="/home/frank/docker/docker-compose"
TEST_DIR="/home/frank/docker/tests"
LOG_BASE="/home/frank/docker/logs"
DELAY_RUNNER="$TEST_DIR/run_with_delay.sh"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_DIR="$LOG_BASE/$TIMESTAMP"
mkdir -p "$TEST_DIR" "$LOG_DIR"

# --- Category Definitions ---
AI_RAG_TESTS=(
  "test_ai_stack.py"
  "test_rag.py"
  "test_rag_fallback.py"
  "test_streaming_response.py"
  "test_file_upload.py"
  "test_model_list.py"
  "test_version_output.py"
  "test_errors.py"
  "test_middleware.py"
  "test_routing.py"
)

API_RELAY_TESTS=(
  "test_gpt_relay.py"
  "test_health.py"
  "test_ollama_status.py"
  "test_openai_key.py"
  "test_internal_errors_in_response.py"
  "test_all_endpoints_respond.py"
)

DOCKER_INFRA_TESTS=(
  "test_container_status.py"
  "test_restart_loops.py"
  "test_no_unhealthy_containers.py"
  "test_no_exited_containers.py"
  "test_shared_host_ports.py"
  "test_orphaned_volumes.py"
  "test_dangling_volumes.py"
  "test_unused_docker_networks.py"
  "test_container_logs.py"
  "test_image_updates_available.py"
  "test_config_drift.py"
  "test_env_vars_loaded.py"
)

HYBRID_MODE_TESTS=(
  "test_hybrid_mode.py"
)

# --- Display Menu ---
clear
echo "=== 🧪 AI Stack Categorized Test Runner – ${STACK_VERSION} ==="
echo "1. Run 🧠 AI & RAG tests (${#AI_RAG_TESTS[@]} files)"
echo "2. Run 🌐 API & Relay tests (${#API_RELAY_TESTS[@]} files)"
echo "3. Run ⚙️ Docker & Infra Health tests (${#DOCKER_INFRA_TESTS[@]} files)"
echo "4. 🧪 Run Hybrid Mode feature tests (${#HYBRID_MODE_TESTS[@]} file)"
echo "5. 📦 Package current build as stable snapshot"
echo "6. Exit"
echo "==========================================="
read -p "Choose an option [1-6]: " choice

if [[ "$choice" == "6" ]]; then
  echo "👋 Exiting."
  exit 0
fi

# Restart option
read -p "♻️ Restart Docker stack before testing? (y/n): " restart
if [[ "$restart" == "y" ]]; then
  echo "🔁 Restarting Docker stack..."
  cd "$STACK_DIR"
  docker compose down >> "$LOG_DIR/deploy.log" 2>&1
  docker compose up -d >> "$LOG_DIR/deploy.log" 2>&1
fi

run_tests() {
  local tests=("$@")
  for file in "${tests[@]}"; do
    echo "🧪 Running $file..." | tee -a "$LOG_DIR/test.log"
    pytest -v "$TEST_DIR/$file" 2>&1 | tee -a "$LOG_DIR/test.log"
  done
}

case $choice in
  1) run_tests "${AI_RAG_TESTS[@]}" ;;
  2) run_tests "${API_RELAY_TESTS[@]}" ;;
  3) run_tests "${DOCKER_INFRA_TESTS[@]}" ;;
  4) run_tests "${HYBRID_MODE_TESTS[@]}" ;;
  5)
    echo "📦 Creating stable snapshot package..."
    ZIP_NAME="ai_middleware-${STACK_VERSION//./_}-stable-${TIMESTAMP}.zip"
    ZIP_PATH="$LOG_BASE/$ZIP_NAME"
    run_tests "${AI_RAG_TESTS[@]}" "${API_RELAY_TESTS[@]}" "${DOCKER_INFRA_TESTS[@]}" "${HYBRID_MODE_TESTS[@]}"
    zip -rq "$ZIP_PATH" "$STACK_DIR" "$TEST_DIR" "$LOG_DIR"
    echo "✅ Stable snapshot created:"
    echo "   $ZIP_PATH"
    ;;
  *) echo "❌ Invalid selection."; exit 1 ;;
esac
