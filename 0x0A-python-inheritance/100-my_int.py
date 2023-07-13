#!/usr/bin/python3
"""
My Integer module
"""


class MyInt(int):
    """
    a class MyInt that inherits from int
    """
    def __eq__(self, other):
        """
        overriding the methods
        """
        return super().__ne__(other)
    def __ne__(self, other):
        return super().__eq__(other)
