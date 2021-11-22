##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import numpy as np

def reverse(string):
    if len(string) == 1:
        return string
    elif len(string) > 1:
        return string[len(string)-1]+reverse(string[:len(string)-1])

if __name__ == '__main__':
    string = '1234'
    print(reverse(string))
