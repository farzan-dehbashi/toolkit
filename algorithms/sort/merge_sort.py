

def merge(arr, left, middle, right):
    # The second param is non inclusive so it should be increased by one
    left_copy = arr[left: middle+1]
    right_copy = arr[middle+1:right+1]

    left_index = 0
    right_index = 0
    sorted_index = 0

    while left_index < len(left_copy) and right_index < len(right_copy):
        print(f'left_index= {left_index}, right_index= {right_index}, sortedindex= {sorted_index}, arr={arr}')
        if left_copy[left_index] < right_copy[right_index]:
            arr[sorted_index] = left_copy[left_index]
            left_index += 1
        else:
            arr[sorted_index] = right_copy[right_index]
            right_index += 1

        sorted_index += 1

    while left_index < len(left_copy):
        arr[sorted_index] = left_copy[left_index]
        left_index += 1
        sorted_index += 1
    while right_index < len(right_copy):
        arr[sorted_index] = right_copy[right_index]
        right_index += 1
        sorted_index += 1

    return arr

def merge_sort(arr, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle+1, right)
        merge(arr, left, middle, right)
    return arr

array = [1,2,3,1,2,3]

print(merge_sort(array, 0, len(array)-1))