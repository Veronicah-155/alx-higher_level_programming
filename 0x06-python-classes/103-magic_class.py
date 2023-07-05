#!/usr/bin/python3
"""Magic class from a given ByteCode."""
import math


class MagicClass:
    """Initialize the MagicClass."""
    def __init__(self, x=0):
        """Initialization of the data."""
        self.x = x
        if type(x) is not int and type(x) is not float:
            raise TypeError("radius must be a number")
        self.x = x

    def area(self):
        """Calculate the area."""
        return self.x ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference."""
        return 2 * math.pi * self.x
