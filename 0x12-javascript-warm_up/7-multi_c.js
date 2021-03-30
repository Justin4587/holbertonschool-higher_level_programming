#!/usr/bin/node

let i = parseInt(process.argv[2], 10);

if (isNaN(i)) {
  console.log('Missing number of occurrences');
} else {
  while (i) {
    console.log('C is fun');
    i--;
  }
}
