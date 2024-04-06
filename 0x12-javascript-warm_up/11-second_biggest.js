#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < args.length; i++) {
    if (args[i] > args[i + 1]) {
      const tmp = args[i + 1];
      args[i + 1] = args[i];
      args[i] = tmp;
      i = 2;
    }
  } console.log(args[args.length - 2]);
}
