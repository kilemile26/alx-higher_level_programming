#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """A base class for geometric shapes."""

    def area(self):
        """Compute the area of the geometric shape.

        Raises:
            Exception: This method should be implemented in derived classes.

        """
        raise Exception("area() is not implemented")

