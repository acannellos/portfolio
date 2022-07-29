import csv
import sqlite3 as sql

def main():

    con = sql.connect('../db.db')
    cur = con.cursor()

    insert_titles = 'INSERT INTO titles VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)'
    insert_ratings = 'INSERT INTO ratings VALUES(?, ?, ?)'
    insert_crew = 'INSERT INTO crew VALUES(?, ?, ?)'
    insert_names = 'INSERT INTO names VALUES(?, ?, ?, ?, ?, ?)'

    run_script('schema.sql', con)

    load_tsv('./data/title.basics.tsv', cur, insert_titles)
    load_tsv('./data/title.ratings.tsv', cur, insert_ratings)
    load_tsv('./data/title.crew.tsv', cur, insert_crew)
    load_tsv('./data/name.basics.tsv', cur, insert_names)

    run_script('transform.sql', con)

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