from functools import lru_cache


@lru_cache(maxsize=None)
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


if __name__ == "__main__":
    for i in range(10):
        print(f"fibo({i}) = {fibo(i)}")
