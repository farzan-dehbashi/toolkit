def find_end(arr, target, l, r):
    m = (l + r) // 2
    if arr[m] == target and arr[m+1] != target:
        return m
    elif target >= arr[m]:
        return find_end(arr, target, m, r)
    else:
        return find_end(arr, target, l, m)


def find_start(arr, target, l, r):
    m = (l + r) // 2
    if arr[m] == target and arr[m - 1] != target:
        return m
    elif target <= arr[m] :
        return find_start(arr, target, l, m)
    else:
        return find_start(arr, target, m, r)


def find_target_range(arr, target):
    start = find_start(arr, target, 0, len(arr))
    end = find_end(arr, target, 0, len(arr))
    return start, end


if __name__ == '__main__':
    arr = [2, 4, 5, 5, 5, 5, 5, 5, 6, 7, 9, 10]
    target = 5
    print(find_target_range(arr, target))