from flask import Flask, redirect, render_template, request
import sqlite3 as sql

from helpers import imdb, ymin, ymax, rmin, rmax

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tas")
def tas():
    return render_template("tas.html")


@app.route("/movies", methods=["GET", "POST"])
def movies():

    con = sql.connect('db.db')

    
    movielist = con.execute(
        '''
        SELECT title, year, director, runtime, genres, rating
        FROM imdb
        WHERE id IN
        (SELECT tconst FROM movielist)
        ORDER BY runtime
        '''
        ).fetchall()

    if request.method == "POST":

        title = request.form.get("title")
        args = ['%' + title + '%']

        addition = con.execute("SELECT id FROM imdb WHERE title LIKE ?", args).fetchone()
        with con:
            con.execute("INSERT INTO movielist (tconst) VALUES (?)", addition)
        
        con.close()
        return redirect("/movies")

    con.close()
    return render_template("movies.html", imdb=imdb, movielist=movielist, ymin=ymin, ymax=ymax, rmin=rmin, rmax=rmax)