def max_sum_subarray(arr, k):
    """Find max sum of any subarray of size k — O(n)."""
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def longest_substring_no_repeat(s):
    """Longest substring without repeating characters — O(n)."""
    char_index = {}
    left = 0
    max_len = 0
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))   # 9
    print(longest_substring_no_repeat("abcabcbb"))     # 3
