#!/usr/bin/node

const i = parseInt(process.argv[2], 10);

if (isNaN(i)) {
  console.log(1);
} else {
  console.log(facts(i));
}

function facts (i) {
  if (i === 0) {
    return (1);
  } else {
    return (i * facts(i - 1));
  }
}
