#!/usr/bin/node

const axios = require('axios');
const URL = process.argv[2];
const file = process.argv[3];
const FileSystem = require('fs');

axios.get(URL).then((response) => {
  FileSystem.writeFile(file, response.data, 'utf-8', (err, data) => {
    if (err) {
      console.error(err);
    }
  });
});
