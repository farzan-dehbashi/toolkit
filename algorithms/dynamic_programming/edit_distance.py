def edit_distance(word1, word2):
    """
    Minimum edit distance (Levenshtein) — O(m*n) time and space.
    Operations: insert, delete, replace (each costs 1).
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1],  # replace
                )

    return dp[m][n]


if __name__ == "__main__":
    print(edit_distance("horse", "ros"))    # 3
    print(edit_distance("intention", "execution"))  # 5
    print(edit_distance("", "abc"))         # 3
