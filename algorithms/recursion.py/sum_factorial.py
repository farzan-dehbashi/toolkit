n = 5


def sum_factorial(num):
    if num > 0:
        return sum_factorial(num-1) + num
    return num

print(sum_factorial(n))
