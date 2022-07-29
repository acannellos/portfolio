title.addEventListener('keyup', helper, false);
year.addEventListener('keyup', helper, false);
director.addEventListener('keyup', helper, false);

year.addEventListener('input', helper, false);

clear.addEventListener('click', function(event) {
    document.querySelector('[name="query"]').innerHTML = '';
});

function helper(event) {

    let html = `<tr>
        <th>title</th>
        <th>year</th>
        <th>director</th>
        <th>runtime</th>
        <th>genres</th>
        <th>rating</th>
        </tr>`;

    for (movie of movies) {
        if (noNulls(arrTYD)) {
            if (searchTitles(movie) && searchYear(movie) && searchDir(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrTY)) {
            if (searchTitles(movie) && searchYear(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrTD)) {
            if (searchTitles(movie) && searchDir(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrYD)) {
            if (searchYear(movie) && searchDir(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrT)) {
            if (searchTitles(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrY)) {
            if (searchYear(movie)) {
                html += build(movie);
            }
        } else if (noNulls(arrD)) {
            if (searchDir(movie)) {
                html += build(movie);
            }
        }
    }
    document.querySelector('[name="query"]').innerHTML = html
};

function noNulls(arr) {
    return !arr.includes(null)
}

function searchTitles(m) {
    return m[0].toLowerCase().includes(title.value.toLowerCase())
};

function searchYear(m) {
    return String(m[1]).includes(String(year.value))
};

function searchDir(m) {
    return m[2].toLowerCase().includes(director.value.toLowerCase())
};

function build(m) {
    let rows = `<tr>
        <td>${m[0]}</td>
        <td>${m[1]}</td>
        <td>${m[2]}</td>
        <td>${m[3]}</td>
        <td>${m[4]}</td>
        <td>${m[5]}</td>
        </tr>`;
    return rows
};