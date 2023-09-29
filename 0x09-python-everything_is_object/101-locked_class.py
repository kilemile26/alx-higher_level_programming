#!/usr/bin/python3
"""
class for lockinguser from creating new dynamic instance attributes 
except the specified ones
"""


class LockedClass:
    """
    A class that prevents the user from dynamically creating new instance attributes
    except for 'first_name'.
    """

    def __init__(self):
        """
        Initialize an instance of LockedClass.
        """
        self.first_name = None


    def __setattr__(self, name, value):
        """
        Set an instance attribute.

        Args:
            name (str): The name of the attribute.
            value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute name is not 'first_name'.
        """
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
