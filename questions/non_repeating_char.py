class Solution:
    @staticmethod
    def char_dict(string):
        dict = {}
        for char in string:
            if char in dict.keys():
                dict[char] += 1
            else:
                dict[char] = 1
        return dict
    @staticmethod
    def firstUniqChar( s: str) -> int:
        dict = Solution.char_dict(s)
        for index, char in enumerate(s):
            if dict[char] == 1:
                return index
        return -1

print(Solution.firstUniqChar('leetcode'))