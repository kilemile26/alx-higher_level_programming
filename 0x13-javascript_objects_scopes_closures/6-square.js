#!/usr/bin/node

const BaseSquare = require('./5-square');

class Square extends BaseSquare
{
	charPrint(c)
	{
		// Instance method to print the square using the character c (default to X)
		if (c === undefined)
		{
			c = 'X';
		}

		for (let i = 0; i < this.height; i++)
		{
			console.log(c.repeat(this.width));
		}
	}
}

module.exports = Square;

