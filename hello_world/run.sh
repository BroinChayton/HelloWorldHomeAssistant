#!/usr/bin/env bash

echo "[INFO] [run.sh] Starte Hello World Add-on ..."
echo "[INFO] [run.sh] Prüfe Python-Version:"
python3 --version || echo "[ERROR] Python nicht gefunden"

echo "[INFO] [run.sh] Starte main.py ..."
python3 /app/main.py || echo "[ERROR] Fehler beim Start von main.py"
