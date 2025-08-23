Franklin UI Debug Patch

✅ Fixes:
- Increases wait time for .message.bot to 10 seconds
- Keeps screenshot on error for review

Install:
1. Replace your test script:
   cp test_ui_prompt_end_to_end.py ~/docker/tests/

2. Re-run the test:
   source venv/bin/activate
   python test_ui_prompt_end_to_end.py

3. Check screenshot if it fails:
   error_ui_prompt.png will show what the UI looked like
