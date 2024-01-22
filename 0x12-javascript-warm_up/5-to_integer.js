#!/usr/bin/node

const input = process.argv[2];

const convertedNumber = parseInt(input);

if (!isNaN(convertedNumber)) {
  console.log(`My number: ${convertedNumber}`);
} else {
  console.log('Not a number');
}
