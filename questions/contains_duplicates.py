class Solution:
    @staticmethod
    def containsDuplicate(nums):
        contains_dup = False
        dict = {}
        for item in nums:
            if item in dict.keys():
                dict[item] += 1
            else:
                dict[item] = 1
        for val in dict.values():
            if val > 1:
                contains_dup = True
        return contains_dup



print(Solution.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2]))