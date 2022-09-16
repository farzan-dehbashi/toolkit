class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        rev_x = x.copy()
        rev_x.reverse()
        rev_x = ''.join(rev_x)
        x = ''.join(x)
        print(rev_x)
        print(x)
        if rev_x == x:
            return True
        else:
            return False
solution = Solution()
print(solution.isPalindrome(10))