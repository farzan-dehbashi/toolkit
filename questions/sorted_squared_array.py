def sort_squered_arr(arr):
    neg_sub_arr = []
    pos_sub_arr = []
    for item in arr:
        if item < 0:
            neg_sub_arr.append(item)
        else:
            pos_sub_arr.append(item)
    neg_sub_arr = [abs(item) for item in neg_sub_arr]
    neg_sub_arr.reverse()
    sorted_arr = []
    while len(pos_sub_arr) > 0 and len(neg_sub_arr) > 0:
        if pos_sub_arr[0] <= neg_sub_arr[0]:
            sorted_arr.append(pos_sub_arr[0])
            del pos_sub_arr[0]
        else:
            sorted_arr.append(neg_sub_arr[0])
            del neg_sub_arr[0]
    sorted_arr = sorted_arr + neg_sub_arr + pos_sub_arr
    return sorted_arr


if __name__ == '__main__':
    arr = [-6, -4, 1,2,3,4,5]
    print(sort_squered_arr(arr))