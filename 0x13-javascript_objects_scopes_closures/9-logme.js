#!/usr/bin/node
let idx = 0;
const lst = [];
exports.logMe = function (item) {
  lst.push(item);
  console.log(idx + ': ' + lst[idx]);
  idx++;
};
