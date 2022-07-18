class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_list = list(s)
        res = list()
        for char in s_list:
            if char.isalpha():
                res.append(char)
        rev_res = res.copy()
        rev_res.reverse()
        res = ''.join(res)
        rev_res = ''.join(rev_res)
        print(res)
        print(rev_res)
        if rev_res == res and len(res) > 1:
            return True
        else:
            return False

solution = Solution()
print(solution.isPalindrome(' '))