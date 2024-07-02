#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  /* constructor (size) {
  super(size);
  } */

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        } console.log(str);
      }
    }
  }
};
