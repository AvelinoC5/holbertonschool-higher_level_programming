#!/usr/bin/node

const FileSystem = require('fs');
const Processes = require('process');
const File = Processes.argv[2];
const StringToWrite = Processes.argv[3];

FileSystem.writeFile(File, StringToWrite, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  }
});
