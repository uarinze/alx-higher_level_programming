#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
fs.writeFile(args[2], args[3], 'UTF-8', error => {
  if (error) console.log(error);
});
