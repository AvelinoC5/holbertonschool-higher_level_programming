#!/usr/bin/node

const process = require('process');

const times = parseInt(process.argv[2]);

if (!times) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < times; x++) {
    console.log('C is fun');
  }
}
