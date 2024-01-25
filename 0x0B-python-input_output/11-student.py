#!/usr/bin/python3
"""that defines a student based on 10-student.py"""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to retrieve
            (default is None).

        Returns:
            dict: A dictionary containing the specified attributes of
            the Student instance.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance with the
        values from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names
            and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
