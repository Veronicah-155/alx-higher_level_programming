#!/usr/bin/python3
"""creating student class"""


class Student:
    """Defining a class"""
    def __init__(self, first_name, last_name, age):
        """Initialize the class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        else:
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
