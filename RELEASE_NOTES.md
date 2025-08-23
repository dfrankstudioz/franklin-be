# Franklin Builder’s Edition Release Notes

---

## v2025.08.22 (Current)

- ✅ API and Web UI fully functional
- ✅ Natural prompt routing
- ✅ Local tools: `list_dir`, `read_file`, `summarize_file`
- ✅ Fallback LLM via TinyLlama (Ollama)
- ✅ GPT-4o prompt interpretation (OpenAI optional)
- ✅ All core tests pass (60+)

---

## Known Issues
- Web UI styling is basic (polish planned in v2025.09)
- Encrypted logic is present in ai_middleware; source not included
- Memory and timeline features are not yet available (planned v3.0)

---

## Upgrade Notes
- Remove old containers before upgrading:
  ```bash
  docker compose down
  docker compose pull
  docker compose up -d --build
  ```

---

## Next Planned Release
- `v2025.09.xx` → Web UI improvements, roadmap.md, and agent framework preview.
