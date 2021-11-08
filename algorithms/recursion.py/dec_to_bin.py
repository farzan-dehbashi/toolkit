def to_binary(n):
    if n > 0:
        return str(to_binary(n // 2)) + str(n % 2)
    else:
        return ''


if __name__ == '__main__':
    n = 7
    print(to_binary(n))