from sense_hat import SenseHat
from flask import Flask

sense = SenseHat()
app = Flask(__name__)


@app.route("/")
def hello():
    sense.show_letter('Y')
    return ""


@app.route("/clear")
def clear():
    sense.show_letter(' ')
    return ""
