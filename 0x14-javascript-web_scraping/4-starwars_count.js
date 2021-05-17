#!/usr/bin/node

const request = require('request');
const thewars = process.argv[2];

request(thewars, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    let char = 0;
    const list = JSON.parse(body);
    list.results.forEach(dict => {
      dict.characters.forEach(character => {
        if (character.includes('18')) {
          char++;
        }
      });
    });
    console.log(char);
  }
});
