# portfolio
#### Video Demo: <URL HERE>

<details>
<summary>Table of Contents</summary>

<ol>

<li><a href="#about">About</a></li>
<li><a href="#usage">Usage</a></li>
<li><a href="#thank-you">thank you</a></li>

</ol>

</details>
<br>

## About

Portfolio is my capstone to Harvard's CS50x, Introduction to Computer Science. It can be described in two parts

### get IMDb data
I wanted to continue to explore the idea of working with relational databases, and I enjoy movies. I found that IMDb provides current .tsv files for hobbyists at [IMDb Datasets](https://www.imdb.com/interfaces/). I did not find a free-tier movie API with reliable daily/monthly limits.

Included are a few Python scripts to help normalize the IMDb dataset into a lightweight list of top movies. The app herein includes normalized data as of **July 2022**, and it is ***not*** necessary to reperform the IMDb initialization (unless to update for current movies).

### Flask app
The Flask application is an expansion of my 'homepage' which includes an index, a project landing page, as well as one featured project 'Movies' built using Python, JavaScript, and SQLite. Partially inspired by [this](https://www.youtube.com/watch?v=-UKbwz6s6VY) SNL sketch, many of the app's features relate to movie runtime (in minutes).

Using the input fields, users can search for movies based on one or multiple criteria, including
1. max runtime
2. title
3. year
4. director
5. genre

The query will autopopulate. When **one** movie is returned, it may be added to the watchlist.

The app also includes a few ideas 'under construction', which may be projects I'd like to explore in the future.

<br>

## Usage

### get IMDb data

To update the app's IMDb database to a more current version, download and extract the following .tsv files from [IMDb Datasets](https://www.imdb.com/interfaces/). Rename and save the files within the /data directory

- /data/title.basics.tsv
- /data/title.ratings.tsv
- /data/title.crew.tsv
- /data/name.basics.tsv


Then in your terminal run
```sh
python init_csv.py
```

followed by
```sh
python init_db.py
```

### Flask app
Until I try to deploy the app, I suppose you will need to run the project with Flask and SQLite3 locally
```sh
flask run
```

<br>

***

## thank you

thank you to david & team :) it was a great experience!