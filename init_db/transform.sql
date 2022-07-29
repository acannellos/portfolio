DELETE FROM titles WHERE titleType != 'movie';
DELETE FROM titles WHERE isAdult = 1;
DELETE FROM titles WHERE startYear = '\N';
DELETE FROM titles WHERE runtimeMinutes = '\N';
DELETE FROM titles WHERE genres = '\N';

DELETE FROM ratings WHERE numVotes < 10000;
DELETE FROM ratings WHERE tconst NOT IN (SELECT titleId FROM titles);
DELETE FROM titles WHERE titleId NOT IN (SELECT tconst FROM ratings);

DELETE FROM crew WHERE tconst NOT IN (SELECT titleId FROM titles);
DELETE FROM names WHERE nconst NOT IN (SELECT directors FROM crew);

ALTER TABLE titles DROP COLUMN isAdult;
ALTER TABLE titles DROP COLUMN titleType;
ALTER TABLE titles DROP COLUMN originalTitle;
ALTER TABLE titles DROP COLUMN endYear;
ALTER TABLE crew DROP COLUMN writers;
ALTER TABLE names DROP COLUMN birthYear;
ALTER TABLE names DROP COLUMN deathYear;
ALTER TABLE names DROP COLUMN primaryProfession;
ALTER TABLE names DROP COLUMN knownForTitles;
/*ALTER TABLE * REBUILD*/

UPDATE crew SET directors = 'nm9999998' WHERE directors LIKE '%,%';
INSERT INTO names VALUES ('nm9999998', 'various');

INSERT INTO crew (tconst) SELECT titleId FROM titles WHERE titleId NOT IN (SELECT tconst FROM crew);
UPDATE crew SET directors = 'nm9999999' WHERE directors IS NULL;
UPDATE crew SET directors = 'nm9999999' WHERE directors = '\N';
INSERT INTO names VALUES ('nm9999999', 'not listed');

CREATE INDEX ix_titles ON titles (primaryTitle);
CREATE INDEX ix_years ON titles (startYear, primaryTitle);
CREATE INDEX ix_ratings ON ratings (tconst);
CREATE INDEX ix_crew ON crew (tconst);