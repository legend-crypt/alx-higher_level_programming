#!/usr/bin/node

const fs = require('fs').promises;

const writeFile = async function writeFile () {
  const content = process.argv[3];
  const filePath = process.argv[2];
  try {
    await fs.writeFile(filePath, content, { encoding: 'utf8' });
  } catch (error) {
    console.log(error);
  }
};

writeFile();
