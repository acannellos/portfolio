DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS ratings;
DROP TABLE IF EXISTS crew;
DROP TABLE IF EXISTS names;
DROP TABLE IF EXISTS movielist;

CREATE TABLE titles (
    titleId TEXT NOT NULL PRIMARY KEY,
    titleType TEXT NOT NULL,
    primaryTitle TEXT NOT NULL,
    originalTitle TEXT,
    isAdult BOOLEAN NOT NULL,
    startYear INTEGER NOT NULL,
    endYear INTEGER,
    runtimeMinutes INTEGER NOT NULL,
    genres TEXT NOT NULL
);

CREATE TABLE ratings (
    tconst TEXT NOT NULL,
    averageRating NUMERIC NOT NULL,
    numVotes INTEGER NOT NULL,
    FOREIGN KEY (tconst) REFERENCES titles(titleId)
);

CREATE TABLE crew (
    tconst TEXT NOT NULL,
    directors TEXT,
    writers TEXT,
    FOREIGN KEY (tconst) REFERENCES titles(titleId),
    FOREIGN KEY (directors) REFERENCES names(nconst)
);

CREATE TABLE names (
    nconst TEXT NOT NULL PRIMARY KEY,
    primaryName TEXT NOT NULL,
    birthYear INTEGER,
    deathYear INTEGER,
    primaryProfession TEXT,
    knownForTitles TEXT
);

CREATE TABLE movielist (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER NOT NULL,
    director TEXT NOT NULL,
    runtime INTEGER NOT NULL,
    genres TEXT NOT NULL,
    added DATETIME DEFAULT CURRENT_TIMESTAMP
);