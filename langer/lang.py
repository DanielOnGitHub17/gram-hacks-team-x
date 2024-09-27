import json

from flask import Flask
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/practice")
def practice():
    return render_template("practice.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/game")
def game():
    return render_template("game.html")


@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        data = json.loads(request.data)
        text = data["from"] + data["text"] + data["to"]
        translated_text = translator(text)
        result = {
            "translated": translated_text
        }
        return json.dumps(result)
    return "BAD REQUEST"


def translator(text):
    # Logic for translator
    return text[::-1]


# with app.test_request_context():
#     for route in ("home", "practice", "settings", "game"):
#         print(url_for(route))

# https://wbd.ms/share/v2/aHR0cHM6Ly93aGl0ZWJvYXJkLm1pY3Jvc29mdC5jb20vYXBpL3YxLjAvd2hpdGVib2FyZHMvcmVkZWVtL2I2NDI3NGVjOGVjNzQ1YTZhMWU5ZDFlYzNlMDgxOWE4X0JCQTcxNzYyLTEyRTAtNDJFMS1CMzI0LTVCMTMxRjQyNEUzRF8xOWVjY2JmOS1hNDA0LTRlNDAtOGM0ZS1iMjFkMDQwZjFiOTU=
