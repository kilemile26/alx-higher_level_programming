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


class BaseRectangle(BaseGeometry):
    """A base class for rectangles."""

    def __init__(self, width, height):
        """Initialize a BaseRectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
