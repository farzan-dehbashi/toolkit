def next_greater_element(nums):
    """Next greater element for each position using monotonic stack — O(n)."""
    result = [-1] * len(nums)
    stack = []
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            idx = stack.pop()
            result[idx] = num
        stack.append(i)
    return result


def daily_temperatures(temps):
    """Days until warmer temperature — LeetCode #739 O(n)."""
    result = [0] * len(temps)
    stack = []
    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result


if __name__ == "__main__":
    print(next_greater_element([4, 1, 2]))          # [-1, 2, -1]
    print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
