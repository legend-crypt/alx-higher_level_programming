#!/usr/bin/node

const arg = process.argv[2];
const num = parseInt(arg);

function factorial (num) {
  if (num === 1) {
    return 1;
  } else if (isNaN(num)) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const result = factorial(num);
console.log(result);
