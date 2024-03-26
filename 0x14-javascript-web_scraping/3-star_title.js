#!/usr/bin/node
const request = require('request');

const movieTitle = function movieTitle () {
  const id = process.argv[2];
  const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
  request.get(url, (response, body) => {
    const data = JSON.parse(body.body);
    console.log(data.title);
  });
};

movieTitle();
