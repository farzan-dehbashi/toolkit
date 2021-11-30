import numpy as np
arr = np.array([[1,2,3],[1,2,3],[1,2,3]])

def sum(arr = np.array([])):
    sum = 0
    for i in range(0, len(arr), 1):
        sum += arr[i,i]
    return sum

if __name__ == '__main__':
    print(sum(arr))