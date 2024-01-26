#!/usr/bin/node
class Rectangle {
  constructor(w, h) {
    if (w > 0 && h > 0) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      this.width = w;
      this.height = h;
    } else {
      return {};
    }
  }
  print () {
    // Instance method to print the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
/*#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      // If w or h is equal to 0 or not a positive integer, create an empty object
      this.width = w;
      this.height = h;
    } else {
      return {}; // You might want to handle this case differently
    }
  }

  print () {
    // Instance method to print the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
*/
