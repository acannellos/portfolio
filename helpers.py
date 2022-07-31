import sqlite3 as sql

con = sql.connect('db.db')
imdb = con.execute(
    '''
    SELECT title, year, director, runtime, genres, rating
    FROM imdb
    '''
    ).fetchall()

con.close()

ymin = 1915
ymax = 2022
rmax = 500