def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def single_number(nums):
    """Find the element that appears once (others appear twice) — XOR trick."""
    result = 0
    for num in nums:
        result ^= num
    return result


def get_bit(n, i):
    return (n >> i) & 1


def set_bit(n, i):
    return n | (1 << i)


def clear_bit(n, i):
    return n & ~(1 << i)


def toggle_bit(n, i):
    return n ^ (1 << i)


if __name__ == "__main__":
    print(is_power_of_two(16))       # True
    print(count_set_bits(7))         # 3 (111)
    print(single_number([4, 1, 2, 1, 2]))  # 4
    print(bin(set_bit(0b1010, 0)))   # 0b1011
