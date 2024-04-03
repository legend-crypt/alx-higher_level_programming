#!/usr/bin/node

const nameTag = $('DIV#character');

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', (data) => {
  const name = data.name;
  nameTag.text(name);
});
