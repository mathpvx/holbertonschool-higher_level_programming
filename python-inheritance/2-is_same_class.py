#!/usr/bin/python3
def is_same_class(obj, a_class):
    """Function that returns True if object is an instance of the input class """
    if type(obj) == a_class:
        return True
    else:
        return False
