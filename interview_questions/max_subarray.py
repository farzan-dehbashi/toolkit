class Solution:
    @staticmethod
    def maxSubArray(nums) -> int:
        max_sub = current_sub = nums[0]
        for num in nums[1:]:
            current_sub = max(num, current_sub + num)
            print(f'current = {current_sub}, num= {num}')
            if current_sub > max_sub:
                max_sub = current_sub
        return max_sub
print(Solution.maxSubArray(nums=[-2,1,-3,4,-1,2,1,-5,4]))
