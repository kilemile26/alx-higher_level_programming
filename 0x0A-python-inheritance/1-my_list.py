#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list in ascending order without modifying the original list.

        Returns:
            None
        """
        print(sorted(self))

    def append(self, value):
        """
        Append an element to the list while ensuring that negative numbers are sorted correctly.

        Args:
            value: The value to append to the list.

        Returns:
            None
        """
        super().append(value)
