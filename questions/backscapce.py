class Solution:
    @staticmethod
    def backspaceCompare( s: str) -> bool:
        skip = 0
        res = ''
        for char in reversed(s):
            if char == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res = char + res
        return res

print(Solution.backspaceCompare('cc#d#'))