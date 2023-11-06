#!/usr/bin/python3
"""A module defining the BaseGeometry class and tests it"""


class BaseGeometry:
    """Empty BaseGeometry class"""
    def area(self):
        """An area method not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate a named integer argument correctly"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
