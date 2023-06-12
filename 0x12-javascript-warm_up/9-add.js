#!/usr/bin/node

const arg = process.argv[2];
const arg2 = process.argv[3];
const a = parseInt(arg);
const b = parseInt(arg2);

function add (a, b) {
  console.log(a + b);
}
add(a, b);
