#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request.get(url, (error, response, data) => {
  const dataURL = JSON.parse(data);
  const completTASK = {};

  if (!error && response.statusCode === 200) {
    dataURL.forEach(task => {
      if (task.completed === true) {
        if (task.userId in completTASK) completTASK[task.userId]++;
        if (!(task.userId in completTASK)) completTASK[task.userId] = 1;
      }
    });
    console.log(completTASK);
  }
});
