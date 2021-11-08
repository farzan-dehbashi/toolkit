import sys
sys.setrecursionlimit(1000)
def factorial(n):
    assert n>=0 and int(n)==n, 'n must be a positive integer only!'
    if n == 1:
        return 1
    else:
        #print(n)
        return n*factorial(n-1)


print(factorial(-2))
