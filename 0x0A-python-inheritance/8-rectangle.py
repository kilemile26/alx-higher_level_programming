#!/usr/bin/python3
"""Module for Rectangle class"""

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


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initialisation function for the Rectangle class"""
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))
