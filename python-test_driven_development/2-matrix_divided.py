def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number.
    Returns: list of lists: new matrix with elements divided by div.
    The results are rounded to 2 decimal places.
    Raises: TypeError: If matrix is not a list of lists of integers/floats
    or  not have the same size, or if div is not a number.
            ZeroDivisionError: If div is zero."""
    if not isinstance(
        matrix,
        list) or not all(
        isinstance(
            row,
            list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not matrix or not all(row for row in matrix) or not all(
            isinstance(item, (int, float)) for row in matrix for item in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]

    return new_matrix
