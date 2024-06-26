#!/usr/bin/node
const request = require('request');

const statusCode = function printStatusCode () {
  const url = process.argv[2];
  request.get(url, (err, response) => {
    if (err) {
      process.exit(1);
    }
    console.log('code: ' + response.statusCode);
  });
};

statusCode();
