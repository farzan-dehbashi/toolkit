class Solution:
    @staticmethod
    def reverseString(s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i, char in enumerate(s[:(len(s)//2) ]):
            s[len(s) - i -1], s[i] = s[i], s[len(s) - i -1]      
        return s


print(Solution.reverseString(["1","2"]))