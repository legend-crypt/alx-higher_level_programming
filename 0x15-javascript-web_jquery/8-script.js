#!/usr/bin/node

const ul = $('UL#list_movies');

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
  $.each(data.results, (i, movie) => {
    const title = $('<li></li>').text(movie.title);
    ul.append(title);
    });
});
