
from flask import Flask
from pwgen import Pwgen

app = Flask(__name__)
generator = Pwgen()

@app.route("/")
def index():
    try:
        return f"<p>{generator.pwgen()}</p>"
    except Exception as e:
        return f"<p>[Exception]: {e}</p>"


@app.route("/raw")
def raw():
    try:
        return [generator.pwgen().rstrip()]
    except Exception as e:
        return [f"[EXCEPTION]: {e}"]
