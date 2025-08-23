#!/bin/bash
echo "[+] Running webui_deep_pack tests..."
cd ~/docker/tests/webui_deep_pack
pytest test_port_9006_alive.py test_static_files_exist.py test_ui_docs_mount.py test_ui_mount_path.py --maxfail=1 --disable-warnings -q
