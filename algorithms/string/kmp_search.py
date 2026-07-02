def build_lps(pattern):
    """Build Longest Proper Prefix which is also Suffix table — O(m)."""
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
    return lps


def kmp_search(text, pattern):
    """KMP pattern search — O(n + m)."""
    if not pattern:
        return [0]
    lps = build_lps(pattern)
    result = []
    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == len(pattern):
            result.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and text[i] != pattern[j]:
            if j:
                j = lps[j - 1]
            else:
                i += 1
    return result


if __name__ == "__main__":
    print(kmp_search("AABAACAADAABAABA", "AABA"))   # [0, 9, 12]
    print(kmp_search("hello world", "world"))         # [6]
