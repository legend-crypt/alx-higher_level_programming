#!/usr/bin/node

const request = require('request');

const printCharacters = function printCharacters () {
  if (!process.argv || process.argv.length < 3) {
    process.exit(1);
  }
  const id = process.argv[2];
  const url = 'https://swapi-api.alx-tools.com/api/films/' + id + '/';
  request.get(url, (err, response, body) => {
    if (err) {
      console.log(err);
    }
    //  console.log(url);
    //  console.log(body);
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err, response, body) => {
        if (err) {
          process.exit(1);
        }
        const characterName = JSON.parse(body).name;
        console.log(characterName);
      });
    }
  });
};

printCharacters();
