def find_larger(n,m):
    if n > m:
        return (n,m)
    else:
        return(m,n)
def gcd(n,m):
    assert int(m)==m and int(n)==n and n>=0 and m>=0, 'positive integer numbers are expected'
    if n==1 or m==1:
        return 1
    else:
        (larger,smaller) = find_larger(n,m)
        if larger%smaller == 0:
            return smaller
        else:
            return gcd(larger%smaller,smaller)

print(gcd(18,4))