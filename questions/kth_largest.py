def flatten(arr):
    flatten_list = []
    while arr:
        for element in arr:
            if type(element) == list:
                for item in element:
                    arr.append(item)
                arr.remove(element)
            else:
                flatten_list.append(element)
                arr.remove(element)
        return flatten_list


def kth_largest(arr):
    return flatten(arr)

print(kth_largest([[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]))