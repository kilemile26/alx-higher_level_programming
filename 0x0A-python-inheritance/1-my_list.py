#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.
        """

        if not self:
            # Handle an empty list

            print([])
        else:
            # Handle negative numbers by converting them to positive for sorting

            sorted_list = sorted(self, key=abs)
            print(sorted_list)
