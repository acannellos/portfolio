import sqlite3 as sql

con = sql.connect('db.db')
imdb = con.execute(
    '''
    SELECT primaryTitle, startYear, primaryName, runtimeMinutes, genres, averageRating
    FROM titles, ratings AS r, crew AS c, names AS n
    WHERE titleID = r.tconst
    AND titleID = c.tconst
    AND directors = nconst
    ORDER BY numVotes DESC
    '''
    ).fetchall()

con.close()

ymin = 1915
ymax = 2022
rmax = 500