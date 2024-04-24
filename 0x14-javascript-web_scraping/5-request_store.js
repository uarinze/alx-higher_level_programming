#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const request = require('request');
request(args[2]).pipe(fs.createWriteStream(process.argv[3]));
