import numpy as np


def binary_search(l, r, arr, val):
    if r >= l:
        m = (l+r) // 2

        if arr[m] == val:
            return m

        elif val > arr[m]:
            return binary_search(m+1, r, arr, val)

        elif val < arr[m]:
            return binary_search(l, m-1, arr, val)

    else:
        print('value '+str(val)+' not found')


def isUnique(list):

    unique = True
    for index,element in enumerate(list):
        if binary_search(0, len(list), list, element) != index:
            print(str(element)+' is not unique')
            unique = False

    if unique:
        print('list elements are unique')


def main():
    #if the list is sorted (if not sort by nlogn)
    list = np.array([1,5,6,8,9,9,12, 12])
    isUnique(list)

main()