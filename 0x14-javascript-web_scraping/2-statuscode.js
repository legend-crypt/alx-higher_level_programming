#!/usr/bin/node
const request = require('request');

const statusCode = function printStatusCode () {
  const url = process.argv[2];
  request.get(url, (response) => {
    console.log('code: ' + response && response.statusCode);
  });
};

statusCode();
