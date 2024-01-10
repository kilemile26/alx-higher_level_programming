#!/usr/bin/node
exports.converter = function (base)
{
	return function (number)
	{
		// Use toString with the specified base to convert the number
		return number.toString(base);
	};
};
