def already_seen(char, chars):
    if char in chars:
        return True
    else:
        return False


class Solution:
    def lengthOfLongestSubstring(self, s):
        length = 0
        r = 0
        for l, cursor_c in enumerate(s):
            seen_chars = set()
            print(f'l = {l}, char= {cursor_c}, r= {r}')
            if len(s) > 1 and l + 1 < len(s) - 1:
                r = l + 1
            if l + 1 == len(s) - 1:
                r = l
            elif len(s) == 1:
                return 1
            elif l + 1 > len(s) - 1:
                print(f'end of string, l = {l}, char= {cursor_c}, r= {r}')
                return r - l
            seen_chars.add(s[l])
            while not (s[r] in seen_chars):
                seen_chars.add(s[r])
                print(f'l = {l}, added_char = {s[r]}, r= {r}')
                r += 1
                if not (r in [i for i, x in enumerate(s)]):
                    # print(f'end of string, l = {l}, char= {cursor_c}, r= {r}')
                    break
            if length < r - l:
                length = r - l
                print(f'length = {length}, l = {l}, r= {r}')
        return length





s = "aa"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))