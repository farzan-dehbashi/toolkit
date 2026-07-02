def build_prefix(arr):
    """Build prefix sum array — O(n)."""
    prefix = [0] * (len(arr) + 1)
    for i, v in enumerate(arr):
        prefix[i + 1] = prefix[i] + v
    return prefix


def range_sum(prefix, l, r):
    """Query sum from index l to r inclusive — O(1)."""
    return prefix[r + 1] - prefix[l]


def subarray_sum_equals_k(arr, k):
    """Count subarrays that sum to k — O(n)."""
    from collections import defaultdict
    count = 0
    running = 0
    seen = defaultdict(int)
    seen[0] = 1
    for num in arr:
        running += num
        count += seen[running - k]
        seen[running] += 1
    return count


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    prefix = build_prefix(arr)
    print(range_sum(prefix, 1, 3))          # 9 (2+3+4)
    print(subarray_sum_equals_k([1, 1, 1], 2))  # 2
