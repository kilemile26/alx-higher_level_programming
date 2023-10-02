#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Compute the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in derived classes.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not a positive integer.

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
