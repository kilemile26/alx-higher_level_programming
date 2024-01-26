#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 5) {
  console.log('Usage: ./102-concat.js fileA fileB fileC');
  process.exit(1);
}

const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

// Read the contents of the first file
const fileAContent = fs.readFileSync(fileAPath, 'utf-8');

// Read the contents of the second file
const fileBContent = fs.readFileSync(fileBPath, 'utf-8');

// Concatenate the contents of the two files
const concatenatedContent = fileAContent + fileBContent;

// Write the concatenated content to the destination file
fs.writeFileSync(fileCPath, concatenatedContent);
