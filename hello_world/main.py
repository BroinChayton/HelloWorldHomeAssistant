import logging
from flask import Flask

# Logging konfigurieren
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("[main.py] Initialisiere Flask App...")

app = Flask(__name__)

@app.route("/")
def hello():
    logger.info("[main.py] GET / aufgerufen")
    return '''
        <html><body>
        <h1>Hello World</h1>
        <button onclick="alert('Hello World!')">Click me</button>
        </body></html>
    '''

if __name__ == "__main__":
    logger.info("[main.py] Starte Flask Server auf 0.0.0.0:19810 ...")
    app.run(host="0.0.0.0", port=19810, use_reloader=False)
