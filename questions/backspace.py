class Solution:
    @staticmethod
    def _process(s: str) -> str:
        skip = 0
        res = []
        for char in reversed(s):
            if char == '#':
                skip += 1
            elif skip > 0:
                skip -= 1
            else:
                res.append(char)
        return ''.join(reversed(res))

    @staticmethod
    def backspace_compare(s: str, t: str) -> bool:
        return Solution._process(s) == Solution._process(t)


if __name__ == "__main__":
    print(Solution.backspace_compare("ab#c", "ad#c"))   # True
    print(Solution.backspace_compare("ab##", "c#d#"))   # True
    print(Solution.backspace_compare("a#c", "b"))       # False
