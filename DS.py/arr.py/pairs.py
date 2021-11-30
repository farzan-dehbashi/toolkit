def pair(sum, arr = []):
    pairs = []
    for num1 in arr:
        for num2 in arr:
            if sum == num1+num2:
                pairs.append(f'{num1} + {num2}')
                arr.remove(num1)
                if num1 != num2:
                    arr.remove(num2)

    return pairs

if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7, 8, 9, 10, -1]
    sum = 6
    print(pair(sum, arr))