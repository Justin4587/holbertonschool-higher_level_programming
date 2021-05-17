#!/usr/bin/node

const request = require('request');
const thewars = process.argv[2];

request(thewars, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const char = {};
    const list = JSON.parse(body);
    list.forEach(task => {
      if (task.completed) {
        if (typeof char[task.userId] === 'undefined') {
          char[task.userId] = 0;
        }
        char[task.userId]++;
      }
    });
    console.log(char);
  }
});
