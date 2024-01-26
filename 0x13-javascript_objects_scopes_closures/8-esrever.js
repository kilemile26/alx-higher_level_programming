#!/usr/bin/node
exports.esrever = function (list) {
  // Clone the original list to avoid modifying it directly
  const reversedList = [...list];

  // Swap elements to reverse the list without using reverse method
  for (let i = 0, j = reversedList.length - 1; i < j; i++, j--) {
    const temp = reversedList[i];
    reversedList[i] = reversedList[j];
    reversedList[j] = temp;
  }
  return reversedList;
};
