#!/usr/bin/node

const args = process.argv.slice(2);
const argument = args[0];

if (argument) {
  console.log(argument);
} else {
  console.log('No argument');
}
