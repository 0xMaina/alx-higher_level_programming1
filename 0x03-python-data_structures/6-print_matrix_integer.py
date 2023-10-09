#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    else:
        for il in matrix:
            length = len(il)
            for i in range(0, length):
                if i < length - 1:
                    print("{:d}".format(il[i]), end=" ")
                else:
                    print("{:d}".format(il[i]))
