#!/usr/bin/node
// get the status code

const url = process.argv[2];
const request = require('request');

request.get(url, (error, response) => {
  if (!error) console.log(`code: ${response.statusCode}`);
});
