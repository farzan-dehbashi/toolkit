##################################################
## Author: Farzan Dehbashi
## Copyright: Copyright 2021, {project_name}
## Date: ${DATE}
## Modified: ${DATE}
## Email: farzan.dehbashi95@gmail.com
## Status: developed
##################################################
#algorithm video = https://www.youtube.com/watch?v=g-PGLbMth_g&ab_channel=MichaelSambol
def selection_sort(arr = []):
    for i in range(len(arr)): #i represents number of sorted items
        min_index = i
        for j in range( i +1 ,len(arr)):
            print(arr)
            print(f'min index = {min_index} / i = {i} / j = {j}')
            if arr[j] < arr[min_index]:
                min_index = j
        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


selection_sort([4,3,2,1,4])