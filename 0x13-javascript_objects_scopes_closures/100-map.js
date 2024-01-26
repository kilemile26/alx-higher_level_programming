#!/usr/bin/node
const { list } = require('./100-data');

// Using map to create a new array with values multiplied by their index
const newList = list.map((value, index) => value * index);

// Print the initial and new arrays
console.log(list);
console.log(newList);
