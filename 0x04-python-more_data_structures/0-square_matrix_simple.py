#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if isinstance(matrix, list):
        if len(matrix) == 0:
            return (matrix)
        new_matrix = matrix.copy()
        for i in range(len(matrix)):
            new_matrix[i] = list(map(lambda n: n**2, matrix[i]))
        return (new_matrix)
