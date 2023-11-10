#!/usr/bin/python3
"""module that contains a definition of square class"""


class Square(Rectangle):
    """Square class, inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor for Square class."""
        super().__init__(size, size, x, y, id)  # Call the superclass constructor

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            "id": self.id,
            "size": self.width,  # size is the same as width for a square
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """String representation of the Square instance."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
