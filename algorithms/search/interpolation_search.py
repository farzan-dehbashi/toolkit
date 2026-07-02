def interpolation_search(arr, val):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= val <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == val:
                return low
            break
        pos = low + ((val - arr[low]) * (high - low) // (arr[high] - arr[low]))
        if arr[pos] == val:
            return pos
        elif arr[pos] < val:
            low = pos + 1
        else:
            high = pos - 1
    return -1


if __name__ == "__main__":
    arr = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    print(interpolation_search(arr, 18))
