def linear_search(arr, item):
    if item in arr:
        return arr.index(item)
    else:
        return 'Not found'

print(linear_search([1,2,3,4,5], 3))
