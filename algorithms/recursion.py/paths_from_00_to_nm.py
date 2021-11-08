def count_path (n,m):
    if n==1 or m==1:
        return 1
    return count_path(n-1, m) + count_path(n, m-1)

print(count_path(3,3))