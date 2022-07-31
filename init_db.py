import csv
import sqlite3 as sql

def main():

    con = sql.connect('db.db')
    cur = con.cursor()

    insert_imdb = 'INSERT INTO imdb VALUES(?, ?, ?, ?, ?, ?, ?, ?)'

    run_script('./static/schema.sql', con)

    with open('imdb.csv', 'r') as f:
        contents = csv.reader(f)
        cur.executemany(insert_imdb, contents)

    con.commit()
    con.close()


def run_script(file, conn):
    with open(file) as f:
        conn.executescript(f.read())


if __name__ == "__main__":
    main()