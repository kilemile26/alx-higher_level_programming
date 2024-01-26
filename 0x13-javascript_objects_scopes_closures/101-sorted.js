#!/usr/bin/node
const { dict } = require('./101-data');

// Function to reverse the keys and values in the dictionary
function reverseDict(originalDict) {
  const reversedDict = {};

  for (const key in originalDict) {
    const value = originalDict[key];

    if (!(value in reversedDict)) {
      reversedDict[value] = [];
    }

    reversedDict[value].push(key);
  }

  return reversedDict;
}

// Compute the new dictionary
const reversedDict = reverseDict(dict);

// Print the new dictionary
console.log(reversedDict);
