class Solution:
    @staticmethod
    def arrayPairSum( nums) -> int:
        nums = sorted(nums)
        pairs = []
        res = 0
        for index in range(0, len(nums), 2):
            pairs.append((nums[index], nums[index + 1]))
        for (x,y) in pairs:
            res += min(x,y)
        return res
print(Solution.arrayPairSum([1,4,3,2]))