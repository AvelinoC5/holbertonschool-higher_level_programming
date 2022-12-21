#!/usr/bin/node

const array = require('./100-data').list;
const newArray = array.map((element, index) => element * index);

console.log(array);
console.log(newArray);
