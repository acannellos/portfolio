from flask import Flask, redirect, render_template
from helpers import imdb, ymin, ymax, rmin, rmax

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tas")
def tas():
    return render_template("tas.html")


@app.route("/movies")
def movies():
    return render_template("movies.html", imdb=imdb, ymin=ymin, ymax=ymax, rmin=rmin, rmax=rmax)