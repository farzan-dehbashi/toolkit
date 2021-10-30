##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: Oct 29th 2021
## Modified: Oct 29th 2021
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################
import numpy as np

def arePermutations_hash(arr1, arr2):

    if len(arr1) != len(arr2):
        print('Arr1 and 2 are not the same size')
        return False

    else: #two arrays have same size
        hm1 = {}
        hm2 = {}
        for i in range(len(arr1)):
            hm1[arr1[i]] = True # hm1 is true where that key value is available in arr 1
            hm2[arr2[i]] = True # hm2 is true where that key value is available in arr 2

        are_the_same = True
        for key in hm1:
            if not (hm2.get(key, False)): # if val is not present in hm2, it returns False and enters if
                print(str(key)+' is not present in arr 2')
                are_the_same = False
        for key in hm2:
            if not (hm1.get(key, False)): # if val is not present in hm2, it returns False and enters if
                print(str(key)+' is not present in arr 1')
                are_the_same = False
        return are_the_same

if __name__ == '__main__':
    print(arePermutations_hash(np.array([3, 2, 1, 7, 5]), np.array([0,1, 2, 3, 12])))
