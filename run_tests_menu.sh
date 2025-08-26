export PYTHONPATH=$(pwd)
#!/bin/bash
PACKS="./tests"

echo "-----------------------------------------"
echo " Franklin Test Suite Menu"
echo "-----------------------------------------"
echo " 1) API Pack"
echo " 2) RAG Pack"
echo " 3) Web UI Pack"
echo " 4) System Pack"
echo " 5) Fallback Pack"
echo " 6) Env Pack"
echo " 7) Logs Pack"
echo " 8) Plugins Pack"
echo " 9) Run ALL Packs"
echo " q) Quit"
echo "-----------------------------------------"
read -p "Choose: " choice

case "$choice" in
    1) pytest "$PACKS/api_pack" ;;
    2) pytest "$PACKS/rag_pack" ;;
    3) pytest "$PACKS/web_ui_pack" ;;
    4) pytest "$PACKS/system_pack" ;;
    5) pytest "$PACKS/fallback_pack" ;;
    6) pytest "$PACKS/env_pack" ;;
    7) pytest "$PACKS/logs_pack" ;;
    8) pytest "$PACKS/plugins_pack" ;;
    9) 
        echo "[+] Running ALL packs..."
        pytest "$PACKS/api_pack" "$PACKS/rag_pack" "$PACKS/web_ui_pack" "$PACKS/system_pack" \
               "$PACKS/fallback_pack" "$PACKS/env_pack" "$PACKS/logs_pack" "$PACKS/plugins_pack"
        ;;
    q) echo "Exiting..."; exit 0 ;;
    *) echo "Invalid option." ;;
esac
