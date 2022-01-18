def sort_and_reverse(arr):
    arr.sort()
    arr.reverse()
    return arr

def nth_largest_element(arr, n):
    if n == 1:
        return arr[0]
    else:
        n = n -1
        arr.remove(arr[0])
        return nth_largest_element(arr, n)


if __name__ == '__main__':
    n = 3
    arr = [1, 2, 5, 4, 9, 11, 10]
    sort_and_reverse(arr)
    print(nth_largest_element(arr, n))