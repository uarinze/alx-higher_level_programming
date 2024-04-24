#!/usr/bin/node
const args = process.argv;
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + args[2];
request(url, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    characters.forEach((character) => {
      request(character, function (error, response, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
