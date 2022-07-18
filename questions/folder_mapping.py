class Solution:
    @staticmethod
    def minOperations(logs) -> int:
        steps = 0
        for op in logs:
            if op == './':
                pass
            elif op == '../' and steps > 0:
                steps -= 1
            if op != '../' and op != './':
                steps += 1
        return steps

print(Solution.minOperations(["./","../","./"]))