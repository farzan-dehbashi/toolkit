def reverse_string(s):
    return s[::-1]


def reverse_string_inplace(s):
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)


if __name__ == "__main__":
    print(reverse_string("hello"))
    print(reverse_string_inplace("hello"))
