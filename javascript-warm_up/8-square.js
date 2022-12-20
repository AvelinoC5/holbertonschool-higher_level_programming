#!/usr/bin/node

const process = require('process');

const size = parseInt(process.argv[2]);

if (!size) {
  console.log('Missing size');
} else {
  let output = '';

  for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
      output += 'X';
    }
    output += '\n';
  }
  console.log(output.trim());
}
