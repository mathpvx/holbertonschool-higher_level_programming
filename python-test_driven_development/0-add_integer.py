#!/usr/bin/python3
"""Adds two integers together."""


def add_integer(a, b=98):
    """Adds two integers or floats together. If the inputs are floats, they are
    converted to integers before addition.
    Returns: The sum of a and b.
    Raises: TypeError: If a or b are not integers or floats."""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
