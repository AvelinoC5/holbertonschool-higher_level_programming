#!/usr/bin/node
/* class Square that defines a square and inherits from Rectangle of 4-rectangle
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super()) */

const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (typeof c === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
