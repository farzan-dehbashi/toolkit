def power_n(i,n):
    assert int(n)==n, 'Integer is expected'
    if n == 0:
        return 1
    elif n== 1:
        return i
    elif n>1:
        return power_n(i,n-1)*i

print(power_n(2,3))
