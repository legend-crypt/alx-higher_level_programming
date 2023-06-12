#!/usr/bin/node

const arr = parseInt(process.argv[2]);

if (!isNaN(arr)) {
  console.log(`My number: ${arr}`);
} else {
  console.log('Not a number');
}
