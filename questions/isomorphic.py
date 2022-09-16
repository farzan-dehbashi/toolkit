class Solution:
    @staticmethod
    def isIsomorphic(s: str, t: str) -> bool:
        is_isomorphic = False
        s = list(s)
        t = list(t)
        seen_chars = []
        for i, char in enumerate(s):
            if not (char in seen_chars):
                seen_chars.append(char)
                t[i] = char
            else:
                t[i] = s[s.index(char)]
        if t == s:
            is_isomorphic = True
        else:
            is_isomorphic = False
        return is_isomorphic

print(Solution.isIsomorphic(s = "eg", t = "add"))