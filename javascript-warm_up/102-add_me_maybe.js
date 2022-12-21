#!/usr/bin/node
// a function that increments and calls a function

exports.addMeMaybe = function (n, theFunction) {
  theFunction(n + 1);
};
