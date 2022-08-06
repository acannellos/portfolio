let title = document.querySelector('[name="title"]');
let year = document.querySelector('[name="year"]');
let director = document.querySelector('[name="director"]');
let runtime = document.querySelector('[name="runtime"]');
let genre = document.querySelector('[name="genre"]');
let clear = document.querySelector('[name="clear"]');

title.addEventListener('keyup', helper, false);
year.addEventListener('keyup', helper, false);
director.addEventListener('keyup', helper, false);
runtime.addEventListener('keyup', helper, false);
genre.addEventListener('keyup', helper, false);

year.addEventListener('input', helper, false);
runtime.addEventListener('input', helper, false);

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
        if (isEmpty(runtime.value)) {
            if (searchTitles(movie) && searchYear(movie) && searchDir(movie) && searchGen(movie)) {
                html += build(movie);
            }
        } else {
            if (searchTitles(movie) && searchYear(movie) && searchDir(movie) && searchRun(movie) && searchGen(movie)) {
                html += build(movie);
            }
        }
    }
    document.querySelector('[name="query"]').innerHTML = html
};

function isEmpty(v) {
    return Boolean(v == null || v == "")
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

function searchRun(m) {
    return (m[3] <= runtime.value)
};

function searchGen(m) {
    return m[4].toLowerCase().includes(genre.value.toLowerCase())
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