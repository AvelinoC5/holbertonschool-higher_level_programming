#!/usr/bin/node

const process = require('process');

const arg = process.argv[2];

if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
