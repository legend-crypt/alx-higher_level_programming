const fs = require('fs').promises;

const readFile = async function readFile (filePath) {
  try {
    const data = await fs.readFile(filePath);
    console.log(data.toString());
  } catch (error) {
    console.error(`Got an error trying to read file: ${error.message}`);
  }
};
readFile('greetings.txt');
