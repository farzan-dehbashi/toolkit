##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import numpy as np


def flatten(arr = []):
    for item in arr:
        if type(item) == list:
            arr.remove(item)
            arr = arr + flatten(item)
    return arr


if __name__ == '__main__':
    print(flatten([1, 2, 3, [4, [[5]]], 2, 3]))
