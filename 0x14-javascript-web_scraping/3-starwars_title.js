#!/usr/bin/node

const request = require('request');
const thewars = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(thewars, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
