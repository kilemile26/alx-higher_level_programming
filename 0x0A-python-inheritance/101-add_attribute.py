#!/usr/bin/python3
"""function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute (str): The name of the attribute to be added.
        value: The value to be assigned to the new attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    """
    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__")
            and attribute in obj.__slots__):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
