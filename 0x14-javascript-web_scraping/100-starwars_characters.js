#!/usr/bin/node

const request = require('request');
const thewars = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(thewars, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    JSON.parse(body).characters.forEach(character => {
      request(character, (err, res, body) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
