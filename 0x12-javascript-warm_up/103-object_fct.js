#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12,
  incr: function ()
};

console.log(myObject);

  function () {
    this.value++;
  }

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
