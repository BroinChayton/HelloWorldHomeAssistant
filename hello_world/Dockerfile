FROM python:3.11-alpine

WORKDIR /app

# Abhängigkeiten installieren
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Dateien kopieren
COPY . .
RUN chmod +x /app/run.sh

EXPOSE 8080

# Shell-Skript ausführen
CMD ["/bin/sh", "/app/run.sh"]
