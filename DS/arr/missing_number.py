
arr = [1,2,3,5]

def missing_numbr(arr = []):
    missing_number = None
    for index, item in enumerate(arr):
        if index < len(arr) - 1:
            if item + 1 != arr[index + 1]:
                missing_number = item + 1
    return missing_number

if __name__ == '__main__':
    print(missing_numbr(arr))