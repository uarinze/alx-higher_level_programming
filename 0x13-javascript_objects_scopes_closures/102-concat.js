#!/usr/bin/node
const fs = require('fs');
const args = process.argv.slice(2);
const rd1 = fs.readFileSync(args[0], 'utf-8');
const rd2 = fs.readFileSync(args[1], 'utf-8');
fs.writeFileSync(args[2], rd1 + rd2);
