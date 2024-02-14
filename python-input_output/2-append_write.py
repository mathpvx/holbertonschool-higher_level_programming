#!/usr/bin/python3
"""
Append file function
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file with utf 8
    returns the number of added char"""
    with open(filename, 'a+', encoding='utf-8') as file:
        file.write(text)
        return len(text)
