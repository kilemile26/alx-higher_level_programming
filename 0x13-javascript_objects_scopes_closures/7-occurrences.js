#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // Count the occurrences of searchElement in the list
  return list.reduce((count, element) => (element === searchElement ? count + 1 : count), 0);
};
