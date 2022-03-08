class Solution:
    @staticmethod
    def removeDuplicates( s: str) -> str:
        index = 0
        s = list(s)
        while index in range(0, len(s) - 1):
            print(f's= {s}, index= {index}')
            if s[index] == s[index + 1]:
                print(f'delete {s[index]}')
                del s[index]
                del s[index]
                if index > 0:
                    index -= 1
                else:
                    index = 0
            else:
                print(f'move, index = {index}')
                index += 1
        return s

print(Solution.removeDuplicates('aaaaaa'))