##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 2]
    print(bubble_sort(arr))
