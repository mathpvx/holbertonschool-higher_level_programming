#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    result = [tuple_a[i] + tuple_b[i] for i in range(2)]

    return tuple(result)
