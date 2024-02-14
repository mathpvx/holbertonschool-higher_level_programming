#!/usr/bin/python3
"""
Write file function
"""


def write_file(filename="", text=""):
    """Write text in a file and returns the number of char in it."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
