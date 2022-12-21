#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (!c) {
      c = 'X';
    }

    let output = '';

    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        output += c;
      }
      output += '\n';
    }
    console.log(output.trim());
  }
}

module.exports = Square;
