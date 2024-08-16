
# Append pwgen to path
import sys
PWGEN_PATH = "/home/nkam/dev/py-web-pwgen/pwgen"
sys.path.append(PWGEN_PATH)
print(f"[PATH ADDED]: {PWGEN_PATH}")

from flask import Flask
from pwgen import Pwgen

MAN = open("man_pwgen.txt", "r")

app = Flask(__name__)
generator = Pwgen()

@app.route("/")
def index():
    try:
        return f"<p>{MAN.read()}</p>"
    except Exception as e:
        return f"<p>[Exception]: {e}</p>"

@app.route("/new")
def new():
    try:
        return f"<p>{generator.pwgen()}</p>"
    except Exception as e:
        return f"<p>[EXCEPTION]: {e}</p>"
