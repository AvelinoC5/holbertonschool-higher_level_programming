#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for i in matrix:
        tmp_list = list(map(lambda x: x * x, i))
        n_matrix.append(tmp_list)
    return (n_matrix)
