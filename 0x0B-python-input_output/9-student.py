#!/usr/bin/python3
"""
Student to JSON
"""


class Student:
    """
    creating Student class
    """
    def __init__(self, first_name, last_name, age):
        """intialize the student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """Convert too JSON"""
        return self.__dict__
