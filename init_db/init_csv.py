import csv
import sqlite3 as sql

# write a .csv of top movies

'''
https://www.imdb.com/interfaces/
download current zip files from imdb.com

extract and name files, respectively
save within /data directory
'''

titles = './data/title.basics.tsv'
ratings = './data/title.ratings.tsv'
crew = './data/title.crew.tsv'
names = './data/name.basics.tsv'

def main():

    con = sql.connect('./data/helper.db')
    cur = con.cursor()

    insert_titles = 'INSERT INTO titles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
    insert_ratings = 'INSERT INTO ratings VALUES(?, ?, ?)'
    insert_crew = 'INSERT INTO crew VALUES(?, ?, ?)'
    insert_names = 'INSERT INTO names VALUES(?, ?, ?, ?, ?, ?)'

    run_script('schema.sql', con)

    load_tsv(titles, cur, insert_titles)
    load_tsv(ratings, cur, insert_ratings)
    load_tsv(crew, cur, insert_crew)
    load_tsv(names, cur, insert_names)

    run_script('transform.sql', con)

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

    with open('imdb.csv', 'w', newline='') as f:
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