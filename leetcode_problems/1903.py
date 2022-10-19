class Solution:
    @staticmethod
    def largestOddNumber(num: str) -> str:
        res = ""
        for index, char in enumerate(num[:-1]):
            if int(char) % 2 == 1:
                res = str(num[:len(num) - index])
                return res
        return res

print(Solution.largestOddNumber("52"))
