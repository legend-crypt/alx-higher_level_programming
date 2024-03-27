const fs = require('fs').promises;

const openFile = async function openFile () {
  try {
    const csvHeaders = 'name,quantity,price';
    await fs.writeFile('groceries.csv', csvHeaders);
  } catch (error) {
    console.error(`Got an error tyring to write to a file ${error.message}`);
  }
};
openFile();
