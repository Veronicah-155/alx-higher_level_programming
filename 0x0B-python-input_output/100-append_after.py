#!/usr/bin/python3
"""Search and update"""


def append_after(filename="", search_string="", new_string=""):
    """Write a function that inserts a line of text to a file"""
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for line in lines:
            if search_string in line:
                file.write(line + new_string)
            else:
                file.write(line)
