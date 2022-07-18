class Solution:

    @staticmethod
    def rotateString( s: str, goal: str) -> bool:
        assert len(s) != 0 and len(goal) != 0 and len(goal) <= 100, 'Invalid input to rotateString func'
        def rotate(s):
            return s[len(s)-1]+s[:len(s)-1]
        
        if len(s) != len(goal):
            return False

        for char in s:
            if rotate(s) == goal:
                return True
            else:
                s = rotate(s)
        
        return False

print(Solution.rotateString('1234', '3411'))