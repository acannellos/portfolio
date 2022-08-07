from flask import Flask, redirect, render_template, request, url_for
import sqlite3 as sql

from helpers import imdb, ymin, ymax, rmin, rmax

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/tas')
def tas():
    return render_template('tas.html')


@app.route('/movies', methods=['GET', 'POST'])
def movies():

    con = sql.connect('db.db')

    movielist = con.execute(
        '''
        SELECT *
        FROM imdb
        WHERE id IN
        (SELECT tconst FROM movielist)
        ORDER BY runtime
        '''
        ).fetchall()

    if request.method == 'POST':

        title = ('%' + request.form.get('title') + '%')
        year = ('%' + request.form.get('year') + '%')
        director = ('%' + request.form.get('director') + '%')
        runtime = request.form.get('runtime')
        genre = ('%' + request.form.get('genre') + '%')

        addition = con.execute(
            '''
            SELECT id
            FROM imdb
            WHERE title LIKE ?
            AND year LIKE ?
            AND director LIKE ?
            AND genres LIKE ?
            AND runtime < ?
            ''',
            (title, year, director, genre, runtime)).fetchall()

        if len(addition) != 1:
            return redirect(url_for('movies'))

        dupes = con.execute(
            '''
            SELECT *
            FROM movielist
            WHERE tconst = ?
            ''',
            addition[0]).fetchall()

        if len(dupes) > 0:
            return redirect(url_for('movies'))      

        with con:
            con.execute('INSERT INTO movielist (tconst) VALUES (?)', addition[0])
        
        con.close()
        return redirect(url_for('movies'))

    con.close()
    return render_template('movies.html', imdb=imdb, movielist=movielist, ymin=ymin, ymax=ymax, rmin=rmin, rmax=rmax)


@app.route('/remove', methods=['POST'])
def remove():
    con = sql.connect('db.db')

    id = [request.form.get('id')]

    with con:
        con.execute('DELETE FROM movielist WHERE tconst = ?', id)

    con.close()
    return redirect(url_for('movies'))