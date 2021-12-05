def merge(arr, l, m, r):
    l_arr = arr[l:m]
    r_arr = arr[m+1:r+1]
    l_cursor = 0
    r_cursor = 0
    result_arr = []
    result_cursor = 0
    while l_cursor < len(l_arr) and r_cursor < len(r_arr):
        if l_arr[l_cursor] < r_arr[r_cursor]:
            result_arr.append(l_arr[l_cursor])
            l_cursor += 1
            result_cursor += 1
        else:
            result_arr.append(r_arr[r_cursor])
            r_cursor += 1
            result_cursor += 1
        print(f'l_c= {l_cursor}, r_c= {r_cursor}, r_c= {result_cursor}')

    if len(l_arr) -1 > l_cursor:
        result_arr += l_arr[l_cursor:]
    elif len(r_arr) -1 > r_cursor:
        result_arr += r_arr[r_cursor:]
    arr = result_arr
    return arr


def merge_sort(list, l, r):
    if l < r:
        m = (l+(r-1)) // 2
        merge_sort(list,l,m)
        merge_sort(list,m+1,r)
        merge(list, l,m,r)
    return list


arr = [1,2,3,2,3,4,5,6,7]
merge(arr, 0,4, 8)
print(arr)