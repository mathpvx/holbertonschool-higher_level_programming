#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        squared_row = []
        for element in row:
            squared_row.append(element ** 2)
        result.append(squared_row)
    return result
