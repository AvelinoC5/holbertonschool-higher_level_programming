#!/usr/bin/node

const process = require('process');

const converted = parseInt(process.argv[2]);

if (!converted) {
  console.log('Not a number');
} else {
  console.log('My number:', converted);
}
