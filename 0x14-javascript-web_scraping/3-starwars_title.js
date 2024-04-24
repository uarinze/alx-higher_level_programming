#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
