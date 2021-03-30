#!/usr/bin/node

const i = parseInt(process.argv[2], 10);
let j = 0;

if (isNaN(i)) {
  console.log('Missing size');
} else {
  while (j < i) {
    console.log('X'.repeat(i));
    j++;
  }
}
