##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021,
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

import numpy as np

obj1 = {
    "outer": 2,
    "obj": {
        "inner": 2,
        "otherObj": {
            "superInner": 2,
            "notANumber": True,
            "alsoNotANumber": "yup"
        }
    }
}


def nested_even_sum(objects, sum = 0):
    for key in objects:
        if type(objects[key]) == dict:
            sum = sum + nested_even_sum(objects[key])
        else:
            if type(objects[key]) == int and objects[key] % 2 == 0:
                sum = sum + int(objects[key])
    return sum


if __name__ == '__main__':
    print(nested_even_sum(obj1))
