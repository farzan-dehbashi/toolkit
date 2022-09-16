class Solution:
    @staticmethod
    def isIncrising(nums):
        is_increasing = True
        for index, _ in enumerate(nums):
            if index > 0:
                if nums[index - 1] > nums[index]:
                    is_increasing = False
        return is_increasing

    @staticmethod
    def isMonotonic(nums) -> bool:
        assert len(nums) >= 1 and len(nums) < 100000, " Invalid size of nums"
        is_monotonic = True
        if Solution.isIncrising(nums[::-1]) == False and Solution.isIncrising(nums) == False:
            is_monotonic = False
        return is_monotonic

if __name__ == "__main__":
    print(Solution.isMonotonic([6,5,4,4,2,9]))