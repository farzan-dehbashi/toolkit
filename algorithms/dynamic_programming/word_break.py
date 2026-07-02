def word_break(s, word_dict):
    """Word break problem — can s be segmented using words in dict? O(n^2)."""
    word_set = set(word_dict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


def word_break_sentences(s, word_dict):
    """Return all ways to break s into valid words."""
    word_set = set(word_dict)
    memo = {}

    def backtrack(remaining):
        if remaining in memo:
            return memo[remaining]
        if not remaining:
            return [""]
        results = []
        for i in range(1, len(remaining) + 1):
            word = remaining[:i]
            if word in word_set:
                for rest in backtrack(remaining[i:]):
                    results.append(word + (" " + rest if rest else ""))
        memo[remaining] = results
        return results

    return backtrack(s)


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))       # True
    print(word_break("applepenapple", ["apple", "pen"]))  # True
    print(word_break_sentences("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
