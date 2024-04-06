#!/usr/bin/node
const args = process.argv;
const x = Math.floor(Number(args[2]));
if (!isNaN(x)) {
  console.log('My number: ' + x);
} else {
  console.log('Not a number');
}
