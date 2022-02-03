def find_root_palindroms(s):
    doubles = []
    singels = []
    for index, char in enumerate(s):
        print(f'index = {index}, char= {char}')
        if index > 0 and index < len(s) - 1:
            if s[index -1] == s[index + 1]:
                singels.append(index)
            if s[index] == s[index + 1]:
                doubles.append(index)
    return singels, doubles


def find_longest_palindrom(s, singles, doubles):
    longest_pal = (0, 0)
    for single_pal_i in singles:
        l = single_pal_i - 1
        r = single_pal_i + 1
        while l > 0 and r < len(s) - 1:
            if s[l-1] == s[r+1]:
                l -= 1
                r += 1
            else:
                break
        if r - l > longest_pal[1] - longest_pal[0]:
            longest_pal = l, r
    return longest_pal


s = 'dabababaccdcc'
(singles, doubles) = find_root_palindroms(s)
print(find_longest_palindrom(s, singles, doubles))