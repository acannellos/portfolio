import csv
import sqlite3 as sql

'''
https://www.imdb.com/interfaces/
download current tsv files from imdb.com, and save within /data

/data/title.basics.tsv
/data/title.ratings.tsv
/data/title.crew.tsv
/data/name.basics.tsv
'''

def main():

    # connect to helper db
    con = sql.connect('./data/helper.db')
    cur = con.cursor()

    insert_titles = 'INSERT INTO titles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
    insert_ratings = 'INSERT INTO ratings VALUES(?, ?, ?)'
    insert_crew = 'INSERT INTO crew VALUES(?, ?, ?)'
    insert_names = 'INSERT INTO names VALUES(?, ?, ?, ?, ?, ?)'

    # create schema
    run_script('schema.sql', con)

    # load tsv to helper db
    load_tsv('./data/title.basics.tsv', cur, insert_titles)
    load_tsv('./data/title.ratings.tsv', cur, insert_ratings)
    load_tsv('./data/title.crew.tsv', cur, insert_crew)
    load_tsv('./data/name.basics.tsv', cur, insert_names)

    # transform helper db for popular movies
    run_script('transform.sql', con)

    # extract SELECT to csv
    imdb = con.execute(
        '''
        SELECT titleID, primaryTitle, startYear, primaryName, runtimeMinutes, genres, averageRating, numVotes
        FROM titles, ratings AS r, crew AS c, names AS n
        WHERE titleID = r.tconst
        AND titleID = c.tconst
        AND directors = nconst
        ORDER BY numVotes DESC
        '''
        ).fetchall()

    with open('../imdb.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in imdb:
            writer.writerow(row)

    con.commit()
    con.close()


def run_script(file, conn):
    with open(file) as f:
        conn.executescript(f.read())


def load_tsv(file, curs, insert):
    with open(file, 'r', encoding='utf-8') as f:
        contents = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
        curs.executemany(insert, contents)


if __name__ == "__main__":
    main()