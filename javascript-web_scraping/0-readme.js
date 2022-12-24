#!/usr/bin/node

const FileSystem = require('fs');
const Processes = require('process');
const File = Processes.argv[2];

FileSystem.readFile(File, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
