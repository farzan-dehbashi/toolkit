class Solution:
    @staticmethod
    def bin_search(nums, target, l, r):
        m = (l+r) // 2
        print(f'l= {l}, r={r}')
        if l<=r: 
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return Solution.bin_search(nums, target, l, m -1)
            elif nums[m] < target:
                return Solution.bin_search(nums, target, m + 1, r)
        else:
            return l


    @staticmethod
    def searchInsert(nums, target: int) -> int:
        return Solution.bin_search(nums, target, l= 0, r= len(nums) -1)


print(Solution.searchInsert(nums = [1,3,5,6,7,8], target = 2))