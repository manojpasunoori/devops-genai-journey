#!/bin/bash
# Usage: ./focus_long.sh 5  (runs 5 x 5-min cycles)
CYCLES="${1:-4}"
MIN=5
for c in $(seq 1 "$CYCLES"); do
  echo " Cycle $c/$CYCLES — $MIN minutes"
  for s in $(seq $((MIN*60)) -1 1); do
    printf "\r%02d:%02d remaining" "$((s/60))" "$((s%60))"
    sleep 1
  done
  echo -e "\n Break 1 minute"; sleep 60
done
echo " All cycles done!"

