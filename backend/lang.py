from flask import Flask
from flask import url_for
from flask import render_template

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



# with app.test_request_context():
#     for route in ("home", "practice", "settings", "game"):
#         print(url_for(route))
    