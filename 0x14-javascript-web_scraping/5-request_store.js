#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const streamBody = function streamBody () {
  if (!process.argv || process.argv.length < 4) {
    process.exit(1);
  }
  const url = process.argv[2];
  const filePath = process.argv[3];
  request(url).pipe(fs.createWriteStream(filePath));
};

streamBody();
