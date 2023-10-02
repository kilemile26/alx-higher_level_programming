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
