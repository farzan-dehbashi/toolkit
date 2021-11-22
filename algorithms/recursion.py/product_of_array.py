import numpy as np

def product_of_array(arr = []):
    assert type(arr) == list and len(arr) > 0, 'List object is expected as an input of product_of_array and it should not be empty'
    if len(arr) == 1:
        return arr[0]
    elif len(arr) > 1:
        element = arr.pop()
        try:
            return product_of_array(arr) * float(element)
        except:
            print('Float element is expected')
            return 1

if __name__ == '__main__':
    arr = [1, 2, 3]
    print(product_of_array(arr))
