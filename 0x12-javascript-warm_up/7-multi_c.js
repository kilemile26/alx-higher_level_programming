#!/usr/bin/node
/*
const occurrences = parseInt(process.argv[2]);

if (!isNaN(occurrences) && occurrences > 0) {
  for (let i = 0; i < occurrences; i++) {
    console.log('C is fun');
  }
} else if (occurrences < 0) {
  ;
} else {
  console.log('Missing number of occurrences');
}
*/
if (process.argv[2] === undefined || isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
