#!/usr/bin/node
const args = process.argv;
const x = Math.floor(Number(args[2]));
const y = Math.floor(Number(args[3]));
function add(a, b) {
  const sum = a + b;
  return sum;
}
console.log(add(x, y));
