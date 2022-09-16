#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getRowIndexWithMostPositiveNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def getRowIndexWithMostPositiveNumbers(matrix):
# Write your code here
    max_pos_num = 0
    index = None
    for row in matrix:
        pos_count = 0
        for item in row:
            if item > 0:
                pos_count += 1
        if pos_count > max_pos_num:
            max_pos_num = pos_count
            index = matrix.index(row)
    return index

print(getRowIndexWithMostPositiveNumbers(    matrix = [
    [-87, -82, -67, -65, -62,   0,   2,   3,   4,  10,  44,  46,  64,  87,  97],
    [-74, -67, -58, -34, -29, -21,   5,  19,  20,  25,  41,  58,  63,  80,  98],
    [-93, -68, -51, -47, -39,  -4,  -2,   4,   5,  12,  35,  48,  60,  80,  99],
    [-96, -95, -77, -72, -64, -33, -27, -23, -15,  -9,  22,  60,  62,  88,  98],
    [-89, -76, -43, -24,   9,  38,  45,  45,  48,  53,  62,  69,  79,  89,  95],
    [-99, -98, -73, -65, -40, -37, -32, -31,  -6,   7,   8,  43,  53,  79,  88],
    [-77, -72, -33, -27, -22, -17,  29,  31,  37,  38,  50,  50,  52,  66,  79],
    [-96, -83, -77, -62, -44, -30, -28,  -5,  16,  39,  50,  53,  58,  84,  95]
    ]
    )
    )


