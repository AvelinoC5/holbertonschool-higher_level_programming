#!/usr/bin/node

const axios = require('axios');
const Id = process.argv[2];
const IdURL = `https://swapi-api.hbtn.io/api/films/${Id}`;

axios.get(IdURL).then((response) => {
  console.log(response.data.title);
});
