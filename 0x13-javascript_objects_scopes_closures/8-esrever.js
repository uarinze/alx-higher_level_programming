#!/usr/bin/node
exports.esrever = function (list) {
  const tsil = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    tsil.push(list[i]);
  }
  return tsil;
};
