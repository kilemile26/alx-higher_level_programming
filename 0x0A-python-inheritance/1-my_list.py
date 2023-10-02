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
        print("{}".format(sorted(self)))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(3)
    my_list.append(1)
    my_list.append(2)
    my_list.print_sorted()  # Should print [1, 2, 3]
    my_list.append(3)
    my_list.append(-1)
    my_list.append(2)
    my_list.print_sorted()  # Should print [-1, 1, 2, 2, 3, 3]
    my_list.append(1)
    my_list.append(4)
    my_list.append(-2)
    my_list.print_sorted()  # Should print [-2, -1, 1, 1, 2, 2, 3, 3, 4]
    print(my_list)  # Should print [-2, -1, 1, 1, 2, 2, 3, 3, 4]
