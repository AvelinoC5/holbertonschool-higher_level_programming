#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, data) {
  if (!error) {
    const result = JSON.parse(data).results;
    console.log(result.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
