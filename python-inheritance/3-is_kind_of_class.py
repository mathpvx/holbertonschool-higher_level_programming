#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if obj
    is instance of input class or one's herited from"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
