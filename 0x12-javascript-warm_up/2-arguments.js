#!/usr/bin/node

const myVar = ['No argument', 'Argument found', 'Arguments found'];

const arglist = process.argv;

const i = arglist.length;

if (i <= 2) {
  console.log(myVar[0]);
} else if (i === 3) {
  console.log(myVar[1]);
} else {
  console.log(myVar[2]);
}
