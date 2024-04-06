#!/usr/bin/node
const args = process.argv;
const x = Math.floor(Number(args[2]));
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    let str = '';
    for (let j = 0; j < x; j++) {
      str += 'X';
    }
    console.log(str);
  }
} else {
  console.log('Missing size');
}
