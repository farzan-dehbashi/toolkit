##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: {dev_status}
##################################################
arr = [1,2,3,4,2]
for i in range(len(arr) - 1):
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j+1]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp

print(arr)