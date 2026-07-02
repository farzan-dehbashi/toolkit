def infinite_counter(start=0):
    """Infinite counter generator."""
    n = start
    while True:
        yield n
        n += 1


def fibonacci_gen():
    """Infinite Fibonacci sequence generator."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def take(n, gen):
    """Take first n items from a generator."""
    for _ in range(n):
        yield next(gen)


def read_large_file(filepath):
    """Memory-efficient large file reader."""
    with open(filepath) as f:
        for line in f:
            yield line.rstrip()


if __name__ == "__main__":
    print(list(take(5, infinite_counter(10))))    # [10, 11, 12, 13, 14]
    print(list(take(8, fibonacci_gen())))         # [0, 1, 1, 2, 3, 5, 8, 13]
