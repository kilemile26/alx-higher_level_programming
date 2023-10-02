#!/usr/bin/python3
"""Module for Square class"""


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
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A class representing a square."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(
                self._Rectangle__size, self._Rectangle__size)


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
