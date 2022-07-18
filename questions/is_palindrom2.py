class Solution:

    @staticmethod
    def validPalindrome(s: str) -> bool:
        s = list(s)
        p1 = 0
        p2 = len(s) -1
        have_passed = False
        while p2 > p1:
            print(f'p1= {p1}, p2= {p2}, have_passed= {have_passed}')
            if s[p2] == s[p1]:
                p1 += 1
                p2 -= 1
                continue
            elif not have_passed:
                if s[p1 + 1] == s[p2]:
                    have_passed = True
                    p1 +=1
                elif s[p2 - 1] == s[p1]:
                    have_passed = True
                    p2 -= 1
                else:
                    return False
        return True



print(Solution.validPalindrome("eeccccbebaeeabebccceea"))