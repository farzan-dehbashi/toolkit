def compress_string(s):
    if not s:
        return s
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + (str(count) if count > 1 else ''))
            count = 1
    result.append(s[-1] + (str(count) if count > 1 else ''))
    compressed = ''.join(result)
    return compressed if len(compressed) < len(s) else s


if __name__ == "__main__":
    print(compress_string("aabcccdddd"))   # a2bc3d4
    print(compress_string("abcd"))         # abcd (no benefit)
