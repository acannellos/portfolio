DROP TABLE IF EXISTS imdb;
DROP TABLE IF EXISTS movielist;

CREATE TABLE imdb (
    id TEXT NOT NULL PRIMARY KEY,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    director TEXT NOT NULL,
    runtime INTEGER NOT NULL,
    genres TEXT NOT NULL,
    rating NUMERIC NOT NULL,
    votes INTEGER NOT NULL
);

CREATE TABLE movielist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    tconst TEXT NOT NULL,
    added DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (tconst) REFERENCES titles(id)
);

CREATE INDEX ix_titles ON imdb (title);
CREATE INDEX ix_years ON imdb (year, title);
CREATE INDEX ix_crew ON imdb (director, title);
CREATE INDEX ix_time ON imdb (runtime);