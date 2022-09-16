def find_paths(n):
    result = []
    if n == 1:
        result = [[0, 1]]
        return result
    if n == 2:
        result = [[0, 1, 2], [0, 2]]
        return result
    else:
        for path in find_paths(n-1):
            result.append(path+[n])
        for path in find_paths(n-2):
            result.append(path+[n])
        return result


if __name__ == '__main__':
    n = 4
    print(find_paths(n))