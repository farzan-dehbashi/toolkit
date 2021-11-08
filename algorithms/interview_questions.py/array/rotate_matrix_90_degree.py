##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################
import numpy as np


def rotate_matrix(m=[]):
    new_m = np.zeros(np.shape(m))
    (rows, columns) = np.shape(m)
    print(columns)
    for row_i in range(rows-1,-1,-1):
        new_m[:, row_i] = m[(rows-1)-row_i,:]
    return new_m

if __name__ == '__main__':
    m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(rotate_matrix(m))
    print(m)
