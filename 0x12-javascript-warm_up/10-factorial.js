#!/usr/bin/node
const args = process.argv;
const x = Math.floor(Number(args[2]));
if (isNaN(x)) {
  console.log(1);
} else {
  function fac (x) {
    if (x === 0) return 1;
    return x * fac(x - 1);
  }
  console.log(fac(x));
}
