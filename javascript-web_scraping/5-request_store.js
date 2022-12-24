#!/usr/bin/node

const url = process.argv[2];
const file = process.argv[3];
const fs = require('fs');
const request = require('request');

request.get(url, (error, response, data) => {
  if (!error && response.statusCode === 200) {
    fs.writeFile(file, data, (error) => {
      if (error) console.log(error);
    });
  }
});
