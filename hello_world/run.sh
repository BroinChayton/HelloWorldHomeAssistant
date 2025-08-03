#!/usr/bin/env bash

echo "[INFO] [run.sh] Starte Hello World Add-on ..."
echo "[INFO] [run.sh] Prüfe Python-Version:"
python3 --version || echo "[ERROR] Python nicht gefunden"

echo "[INFO] $(date) Starte Add-on-Prozess"
echo "[INFO] [run.sh] Starte main.py ..."
python3 /app/main.py
EXIT_CODE=$?
if [ "$EXIT_CODE" -ne 0 ]; then
  echo "[ERROR] main.py beendet sich mit Fehlercode $EXIT_CODE"
fi
