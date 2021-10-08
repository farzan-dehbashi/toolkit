
def sum_of_digits(n):
    assert n>=0 and int(n)==n, 'n should be a positive integer'
    if int(n/10) == 0:
        return n
    else:
        return sum_of_digits(int(n/10))+n%10

print(sum_of_digits(21))