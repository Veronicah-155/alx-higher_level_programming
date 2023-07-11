#!/usr/bin/python3
"""
Write to a file
"""


def write_file(filename="", text=""):
     """
     Write a function that writes a string to a text file
     (UTF8) and returns the number of characters written
     """
     with open(filename, "w", encoding="utf-8") as file:
          chars_written = file.write(text)
          return chars_written
