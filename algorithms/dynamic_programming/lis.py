def lis(arr):
    """Longest Increasing Subsequence length — O(n^2)."""
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


def lis_binary_search(arr):
    """LIS using patience sorting — O(n log n)."""
    import bisect
    tails = []
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


if __name__ == "__main__":
    arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis(arr))                # 4
    print(lis_binary_search(arr))  # 4
