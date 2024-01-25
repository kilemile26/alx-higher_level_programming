#!/usr/bin/python3
"""
module that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization
of an object
"""


def class_to_json(obj):
    """
    Serialize an object of a class into a dictionary for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary containing the serializable attributes of
        the object.
    """
    obj_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (int, str, bool, list, dict)):
            obj_dict[key] = value
    return obj_dict
