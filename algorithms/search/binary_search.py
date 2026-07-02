def binary_search(l, r, arr, val):
    if r >= l:
        m = (l + r) // 2
        if arr[m] == val:
            return m
        elif val > arr[m]:
            return binary_search(m + 1, r, arr, val)
        else:
            return binary_search(l, m - 1, arr, val)
    else:
        print('value ' + str(val) + ' not found')
        return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 12, 19]
    print(binary_search(0, len(arr) - 1, arr, 12))
