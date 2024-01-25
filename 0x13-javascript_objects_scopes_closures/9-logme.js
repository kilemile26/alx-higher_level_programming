#!/usr/bin/node
let counter = 0; // Counter to keep track of the number of arguments printed

exports.logMe = function (item)
{
	// Print the number of arguments already printed and the new argument value

	console.log(`${counter}: ${item}`);
	counter++;
};
