#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const theurl = process.argv[2];
const thepath = process.argv[3];

request(theurl, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(thepath, body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
