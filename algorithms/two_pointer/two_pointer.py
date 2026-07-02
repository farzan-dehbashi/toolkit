def pair_with_target_sum(arr, target):
    """Find pair in sorted array that sums to target — O(n)."""
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return [left, right]
        elif s < target:
            left += 1
        else:
            right -= 1
    return []


def remove_duplicates(arr):
    """Remove duplicates in-place from sorted array — O(n)."""
    if not arr:
        return 0
    next_non_dup = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[next_non_dup] = arr[i]
            next_non_dup += 1
    return next_non_dup


def is_palindrome(s):
    """Check if string is palindrome using two pointers — O(n)."""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(pair_with_target_sum([1, 2, 3, 4, 6], 6))   # [1, 3]
    arr = [2, 3, 3, 3, 6, 9, 9]
    print(remove_duplicates(arr))                       # 4
    print(is_palindrome("racecar"))                     # True
