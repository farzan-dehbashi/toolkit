from collections import Counter


def is_anagram(s, t):
    """Check if two strings are anagrams — O(n)."""
    return Counter(s) == Counter(t)


def is_anagram_sort(s, t):
    """Check anagram by sorting — O(n log n)."""
    return sorted(s) == sorted(t)


def find_all_anagrams(s, p):
    """Find all starting indices where anagram of p appears in s — O(n)."""
    result = []
    p_count = Counter(p)
    window = Counter(s[:len(p)])
    if window == p_count:
        result.append(0)
    for i in range(len(p), len(s)):
        window[s[i]] += 1
        left = s[i - len(p)]
        window[left] -= 1
        if window[left] == 0:
            del window[left]
        if window == p_count:
            result.append(i - len(p) + 1)
    return result


if __name__ == "__main__":
    print(is_anagram("anagram", "nagaram"))     # True
    print(is_anagram("rat", "car"))             # False
    print(find_all_anagrams("cbaebabacd", "abc"))  # [0, 6]
