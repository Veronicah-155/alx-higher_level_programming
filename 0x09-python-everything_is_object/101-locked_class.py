#!/usr/bin/python3
"""
Creating a class lockedClass
"""


class LockedClass:
    """
    preventing user from dynamic attributes
    """
    __slots__ = ['first_name']
