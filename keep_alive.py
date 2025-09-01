
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.get("/")
def root():
    return "18th Mech bot is alive"

def _run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=_run, daemon=True)
    t.start()
