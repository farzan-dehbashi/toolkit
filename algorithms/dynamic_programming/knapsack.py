def knapsack(weights, values, capacity):
    """0/1 Knapsack — O(n * capacity) time and space."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]


def coin_change(coins, amount):
    """Min coins to make amount — O(n * amount)."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == "__main__":
    print(knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5))  # 7
    print(coin_change([1, 5, 6, 9], 11))              # 2
