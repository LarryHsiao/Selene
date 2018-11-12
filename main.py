import threading
import time

from flask import Flask, request
from sense_hat import SenseHat

sense = SenseHat()
app = Flask(__name__)
running = True


@app.route("/")
def hello():
    sense.show_letter('Y')
    return ""


@app.route("/clear")
def clear():
    sense.show_letter(' ')
    return ""


@app.route("/stop")
def stop():
    global running
    running = False
    shutdown_server()
    return ""


def start_flask():
    app.run(host="10.42.0.1", debug=False, load_dotenv=False)


# Somehow shutdown the server
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


r = 0
g = 0
b = 0


def loop():
    global r, g, b
    while running:
        time.sleep(0.05)
        r = (r + 1) % 122
        g = (g + 2) % 122
        b = (b + 3) % 122
        sense.clear((r, g, b))

    sense.clear((0, 0, 0))


if __name__ == "__main__":
    threading.Thread(target=start_flask).start()
    loop()
