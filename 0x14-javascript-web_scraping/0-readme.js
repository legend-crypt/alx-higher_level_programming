#!/usr/bin/node

const fs = require('fs').promises;

const readFile = async function readFile () {
  const filePath = process.argv[2];
  try {
    const data = await fs.readFile(filePath, { encoding: 'utf8' });
    console.log(data);
  } catch (error) {
    console.log(error);
  }
};
readFile();
