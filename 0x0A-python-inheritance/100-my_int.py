#!/usr/bin/python3
"""
This module defines a custom integer class with
inverted '==' and '!=' operators.
"""


class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class.
    This class inverts the behavior of the equality (==) and 
    inequality (!=) operators.

    Attributes:
        No additional attributes.

    Methods:
        __eq__(self, other): Inverts the behavior of the 
        equality operator (==).
        __ne__(self, other): Inverts the behavior of the 
        inequality operator (!=).
    """
    def __eq__(self, other):
        """
        Inverts the behavior of the equality operator (==).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        # Invert the behavior of the equality operator (==)
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality operator (!=).

        Args:
            other: The value to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        # Invert the behavior of the inequality operator (!=)
        return super().__eq__(other)
