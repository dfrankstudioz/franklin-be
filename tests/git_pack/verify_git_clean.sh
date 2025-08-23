#!/bin/bash
ROOT="${1:-$(git rev-parse --show-toplevel)}"
cd "$ROOT" || exit 1

echo "[🔍] Git Repo Cleanliness & Secret Exposure Check"
errors=0

echo "[1] Checking for tracked *.env files..."
git ls-files | grep -i '\.env$' && {
  echo "❌ Tracked .env file(s) found!"
  ((errors++))
} || echo "✅ No tracked .env files."

echo "[2] Searching Git history for .env files..."
git log --all --name-only | grep -i '\.env$' | grep -v '.env.example' && {
  echo "❌ .env found in Git history!"
  ((errors++))
} || echo "✅ No .env in Git history."

echo "[3] Grepping for secret patterns..."
grep -r --color=always -Ei '(sk-[a-z0-9]{20,}|api[_-]?key|secret|token)' . \
  --exclude-dir=.git \
  --exclude='*.env*' \
  && { echo "❌ Potential secrets found in code!"; ((errors++)); } \
  || echo "✅ No secrets detected in codebase."

echo "[4] Checking rag_prompt_patch.py..."
if grep -q 'def improve_prompt_context' ai_middleware/rag_prompt_patch.py 2>/dev/null; then
  echo "❌ Unencrypted rag_prompt_patch.py"
  ((errors++))
else
  echo "✅ rag_prompt_patch.py appears encrypted"
fi

echo "[5] Checking pyarmor_runtime..."
[ -d "ai_middleware/pyarmor_runtime" ] && echo "✅ pyarmor_runtime present." || {
  echo "⚠️ pyarmor_runtime not found!"
  ((errors++))
}

echo "[6] Scanning logic files for unencrypted functions..."
for file in ai_middleware/rag_prompt_patch.py \
            ai_middleware/fallback_router.py \
            ai_middleware/secret_logic.py \
            ai_middleware/read_file.py \
            ai_middleware/list_dir.py \
            ai_middleware/summarize_file.py; do
  if [[ -f "$file" ]]; then
    if grep -q 'def ' "$file"; then
      echo "❌ $file contains plaintext logic"
      ((errors++))
    else
      echo "✅ $file appears obfuscated"
    fi
  fi
done

[[ $errors -gt 0 ]] && {
  echo "[🚨] Git safety check FAILED with $errors issue(s)."
  exit 1
} || {
  echo "[✅] Git repo is CLEAN."
}
