#!/usr/bin/node

const request = require('request');
if (!process.argv || process.argv.length < 3) {
  console.log('Missing arguments');
  process.exit(1);
}
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    const results = JSON.parse(body).results;
    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
}
);
