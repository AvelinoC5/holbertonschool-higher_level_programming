#!/usr/bin/node

const axios = require('axios').default;
const Processes = require('process');
const URL = Processes.argv[2];

axios.get(URL).then(function (response) {
  console.log('code: ' + response.status);
})
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
