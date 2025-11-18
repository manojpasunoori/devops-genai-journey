#!/bin/bash

# Simple focus timer (10 x 1s demo cycles). Change SLEEP to 300 for 5-min pomodoros.
SLEEP=1
echo " Focus session started ($(date)) — I showed up."
for i in {1..10}; do
  printf "Deep Work Cycle %02d ...\n" "$i"
  sleep "$SLEEP"
done
echo " Session complete ($(date)). Commit your progress now."

