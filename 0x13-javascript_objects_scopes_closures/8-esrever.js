#!/usr/bin/node

exports.esrever = function (list) {
  const tsil = [];
  while (list.length) {
    tsil.push(list.pop());
  }
  return tsil;
};
