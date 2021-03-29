#!/usr/bin/node

const haha = parseInt(process.argv[2]);

if (isNaN(haha)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + haha);
}
