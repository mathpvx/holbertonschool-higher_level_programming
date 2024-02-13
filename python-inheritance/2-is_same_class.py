#!/usr/bin/python3
"""
================================
module with method is_same_class
================================
"""


def is_same_class(obj, a_class):
    """Function that returns True
    if object is an instance of the input class """
    if type(obj) is a_class:
        return True
    else:
        return False
