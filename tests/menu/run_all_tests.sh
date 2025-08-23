#!/usr/bin/env bash
set -Eeuo pipefail

ROOT="$HOME/docker"
MENU_DIR="$ROOT/tests/menu"
LOG_DIR="$ROOT/logs"
mkdir -p "$LOG_DIR"
TS="$(date +%Y%m%d_%H%M%S)"
LOGFILE="$LOG_DIR/run_all_${TS}.log"

# Keep logs via tee; use /dev/tty (FD 9) for pinned status if available
exec 3>&1 4>&2
exec > >(tee -a "$LOGFILE") 2>&1

if [[ -w /dev/tty ]]; then
  exec 9>/dev/tty
  HAS_TTY=1
else
  HAS_TTY=0
fi

SCRIPTS=(
  "api_tests.sh"
  "rag_tests.sh"
  "web_ui_tests.sh"
  "routing_tests.sh"
  "env_config_tests.sh"
  "docker_health_tests.sh"
  "logs_snapshot.sh"
  "plugins_tests.sh"
)
total=${#SCRIPTS[@]}
ok=0
fail=0

human() { local s=$1; printf "%02d:%02d:%02d" "$((s/3600))" "$(((s%3600)/60))" "$((s%60))"; }
bar_pct(){
  local pct=$1 width=${2:-30}
  ((pct<0))&&pct=0; ((pct>100))&&pct=100
  local fill=$((pct*width/100))
  local rest=$((width-fill))
  printf "[%s%s] %3d%%" "$(printf '%*s' "$fill" '' | tr ' ' '#')" "$(printf '%*s' "$rest" '' | tr ' ' '-')" "$pct"
}

# Minimal cursor control
CSI=$'\033['
save(){ [[ $HAS_TTY -eq 1 ]] && printf '\0337' >&9 || true; }
rest(){ [[ $HAS_TTY -eq 1 ]] && printf '\0338' >&9 || true; }
pos_two_thirds(){
  [[ $HAS_TTY -eq 1 ]] || return 0
  local rows
  rows=$(stty size </dev/tty 2>/dev/null | awk '{print $1}')
  [[ -z "$rows" ]] && rows=24
  ROW=$(( rows*2/3 )); ((ROW<2)) && ROW=2
  printf "%s%d;1H" "$CSI" "$ROW" >&9
}
clr_eol(){ [[ $HAS_TTY -eq 1 ]] && printf "%sK" "$CSI" >&9 || true; }
down1(){   [[ $HAS_TTY -eq 1 ]] && printf "%s1B" "$CSI" >&9 || true; }

draw_status(){
  # Args: completed step_name elapsed_str
  [[ $HAS_TTY -eq 1 ]] || return 1
  local completed=$1 step="$2" elap="$3"
  local pct=$(( completed * 100 / total ))
  save
  pos_two_thirds
  clr_eol; printf "Overall: %d/%d (%d%%)" "$completed" "$total" "$pct" >&9
  down1
  clr_eol; printf "%s  •  %s  •  elapsed %s" "$(bar_pct "$pct" 30)" "$step" "$elap" >&9
  rest
  return 0
}

echo "Run ALL started at $(date '+%F %T')  → logging to $LOGFILE"
suite_start=$(date +%s)

for i in "${!SCRIPTS[@]}"; do
  step="${SCRIPTS[$i]}"

  # show where we are before starting the script (completed so far = i)
  echo
  echo "=== Running ${step} (Overall: ${i}/${total}) ==="

  start=$(date +%s)
  bash "$MENU_DIR/$step" &
  pid=$!

  # While running: keep elapsed updating; completed count stays at i
  hb=-1
  while kill -0 "$pid" 2>/dev/null; do
    el=$(( $(date +%s) - start ))
    draw_status "$i" "$step" "$(human "$el")" || {
      # no tty: heartbeat every 5s so logs show liveness
      if (( el/5 > hb )); then
        hb=$(( el/5 ))
        echo "Overall: ${i}/${total} • $(bar_pct $(( i*100/total )) 30) • ${step} • elapsed $(human "$el")"
      fi
    }
    sleep 1
  done

  status=0; wait "$pid" || status=$?
  el=$(( $(date +%s) - start ))
  if [[ $status -eq 0 ]]; then
    echo "✓ ${step} OK  (duration: $(human "$el"))"; ((ok++))
  else
    echo "✗ ${step} FAILED  (duration: $(human "$el"))"; ((fail++))
  fi

  # After completion: increment completed and redraw with new % immediately
  completed=$((i+1))
  draw_status "$completed" "$step" "$(human "$el")" || true
  echo "Overall: ${completed}/${total} • $(bar_pct $(( completed*100/total )) 30)"
done

# Clear the pinned two lines
if [[ $HAS_TTY -eq 1 ]]; then
  save; pos_two_thirds; clr_eol; down1; clr_eol; rest
fi

suite_elapsed=$(( $(date +%s) - suite_start ))
echo
echo "Summary: ${ok} OK, ${fail} failed  •  Total time: $(human "$suite_elapsed")"
exit 0
