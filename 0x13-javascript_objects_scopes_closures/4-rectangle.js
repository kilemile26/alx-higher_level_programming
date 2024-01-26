#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      return {};
    }
    this.width = w;
    this.height = h;
}

print () {
  // Instance method to print the rectangle using the character 'X'
  for (let i = 0; i < this.height; i++) {
    console.log('X'.repeat(this.width));
  }
}

rotate () {
  // Instance method to exchange the width and height of the rectangle
  const temp = this.width;
  this.width = this.height;
  this.height = temp;
}

double () {
  // Instance method to double the width and height of the rectangle
  this.width *= 2;
  this.height *= 2;
}
}

module.exports = Rectangle;
