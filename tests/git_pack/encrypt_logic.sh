#!/bin/bash
TARGET_DIR="${1:-$(pwd)/ai_middleware}"
echo "[🔐] Encrypting sensitive logic in: $TARGET_DIR"

FILES=(
  "rag_prompt_patch.py"
  "fallback_router.py"
  "secret_logic.py"
  "read_file.py"
  "list_dir.py"
  "summarize_file.py"
)

mkdir -p "$TARGET_DIR/pyarmor_output"

for file in "${FILES[@]}"; do
  src="$TARGET_DIR/$file"
  if [[ -f "$src" ]]; then
    echo "Encrypting $src..."
    pyarmor gen --output "$TARGET_DIR/pyarmor_output" "$src"
    mv "$TARGET_DIR/pyarmor_output/$file" "$src"
  fi
done

echo "[✅] Encryption complete. Runtime assumed in pyarmor_runtime/"
