def longest_palindrome(s):
    """Longest palindromic substring — O(n^2) expand around center."""
    if not s:
        return ""
    start, max_len = 0, 1

    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    for i in range(len(s)):
        # Odd length
        l, r = expand(i, i)
        if r - l + 1 > max_len:
            start, max_len = l, r - l + 1
        # Even length
        l, r = expand(i, i + 1)
        if r - l + 1 > max_len:
            start, max_len = l, r - l + 1

    return s[start:start + max_len]


if __name__ == "__main__":
    print(longest_palindrome("babad"))   # bab or aba
    print(longest_palindrome("cbbd"))    # bb
    print(longest_palindrome("racecar")) # racecar
