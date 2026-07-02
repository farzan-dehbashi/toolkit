import functools


def memoize(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    wrapper.cache = cache
    wrapper.cache_clear = lambda: cache.clear()
    return wrapper


if __name__ == "__main__":
    @memoize
    def fib(n):
        if n < 2:
            return n
        return fib(n - 1) + fib(n - 2)

    print(fib(30))              # fast
    print(fib.cache)            # see cached values
