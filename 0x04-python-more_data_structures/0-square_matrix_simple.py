#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        tmp = list(map(lambda x: x * x, i))
        new_matrix.append(tmp)
    return new_matrix
